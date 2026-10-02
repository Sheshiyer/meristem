#!/usr/bin/env bash
#
# brandmint v2 - Pipeline Launcher
# Executes waves in order with conducty-style checkpoints
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

# Default values
CONFIG=""
WAVES="1-7"
NON_INTERACTIVE=false
DRY_RUN=false

usage() {
    cat <<EOF
Usage: bm launch [options]

Launch the brand pipeline for specified waves.

Options:
    --config <path>         Brand config YAML (required)
    --waves <range>         Wave range (default: 1-7)
    --non-interactive       No prompts, fail on missing data
    --dry-run               Show plan without executing
    --resume-from <wave>    Resume from specific wave

Examples:
    bm launch --config ./brand-config.yaml --waves 1-3
    bm launch --config ./brand-config.yaml --non-interactive
    bm launch --config ./brand-config.yaml --resume-from 4
EOF
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --config)
                CONFIG="$2"
                shift 2
                ;;
            --waves)
                WAVES="$2"
                shift 2
                ;;
            --non-interactive)
                NON_INTERACTIVE=true
                shift
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --resume-from)
                WAVES="$2-7"
                shift 2
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            *)
                die "Unknown option: $1"
                ;;
        esac
    done
    
    [[ -z "$CONFIG" ]] && die "Missing required option: --config"
    require_file "$CONFIG" "brand config"
}

# -----------------------------------------------------------------------------
# Core Execution
# -----------------------------------------------------------------------------

record_spoke_failure() {
    local brand_dir="$1"
    local spoke="$2"
    local failure_status="$3"

    if [[ "$failure_status" -eq 0 ]]; then
        failure_status=1
    fi

    local state_status
    if state_record_skill_failure "$brand_dir" "$spoke"; then
        return "$failure_status"
    else
        state_status=$?
    fi
    log_error "Unable to record failed spoke '$spoke' in runner state"
    return "$state_status"
}

record_wave_failure() {
    local wave="$1"
    local brand_dir="$2"
    local failure_status="$3"

    if [[ "$failure_status" -eq 0 ]]; then
        failure_status=1
    fi

    local state_status
    if state_mark_wave_failed "$brand_dir" "$wave"; then
        return "$failure_status"
    else
        state_status=$?
    fi
    log_error "Unable to record failed wave '$wave' in runner state"
    return "$state_status"
}

execute_wave() {
    local wave="$1"
    local brand_dir="$2"
    local brand_config="$3"
    local status

    # A rerun is not complete until every cluster and spoke succeeds again.
    if state_mark_wave_started "$brand_dir" "$wave"; then
        :
    else
        status=$?
        log_error "Unable to start wave $wave in runner state"
        return "$status"
    fi

    # Wave 6 has TWO clusters (content + social-growth)
    # Other waves have one cluster.
    local clusters
    if clusters=$(wave_to_clusters "$wave"); then
        :
    else
        status=$?
        log_error "Unable to resolve clusters for wave $wave"
        record_wave_failure "$wave" "$brand_dir" "$status"
        return $?
    fi

    if [[ -z "$clusters" ]]; then
        log_error "No clusters configured for wave $wave"
        record_wave_failure "$wave" "$brand_dir" 1
        return $?
    fi

    log_info "=== Wave $wave: $clusters ==="

    # Run all clusters in this wave sequentially.
    local cluster
    for cluster in $clusters; do
        local cluster_dir="$PROJECT_ROOT/clusters/$cluster"
        if [[ ! -d "$cluster_dir" ]]; then
            log_error "Cluster directory not found: $cluster_dir"
            record_wave_failure "$wave" "$brand_dir" 1
            return $?
        fi

        # Get list of spokes for this cluster
        local spokes
        if spokes=$(list_spokes "$cluster"); then
            :
        else
            status=$?
            log_error "Unable to list spokes for cluster: $cluster"
            record_wave_failure "$wave" "$brand_dir" "$status"
            return $?
        fi

        if [[ -z "$spokes" ]]; then
            log_error "No spokes found for cluster: $cluster"
            record_wave_failure "$wave" "$brand_dir" 1
            return $?
        fi

        local -a spoke_list=()
        local listed_spoke
        while IFS= read -r listed_spoke; do
            spoke_list+=("$listed_spoke")
        done <<< "$spokes"

        if [[ "${#spoke_list[@]}" -eq 0 || -z "${spoke_list[0]}" ]]; then
            log_error "No usable spokes found for cluster: $cluster"
            record_wave_failure "$wave" "$brand_dir" 1
            return $?
        fi

        log_info "--- Cluster $cluster (${#spoke_list[@]} spokes) ---"

        # Tracer-first: run first spoke to validate assumptions
        local tracer
        tracer="${spoke_list[0]}"
        log_info "Running tracer: $tracer"

        if execute_spoke "$cluster" "$tracer" "$brand_dir" "$brand_config"; then
            :
        else
            status=$?
            log_error "Tracer failed for $cluster. Plan needs revision."
            if vault_log_failure "Tracer failure: $tracer" "Wave $wave, cluster $cluster"; then
                :
            else
                log_warn "Unable to write tracer failure to vault"
            fi
            record_wave_failure "$wave" "$brand_dir" "$status"
            return $?
        fi

        # Execute remaining spokes
        local spoke
        for spoke in "${spoke_list[@]:1}"; do
            [[ -z "$spoke" ]] && continue
            log_info "Running spoke: $spoke"
            if execute_spoke "$cluster" "$spoke" "$brand_dir" "$brand_config"; then
                :
            else
                status=$?
                log_error "Spoke failed: $spoke"
                record_wave_failure "$wave" "$brand_dir" "$status"
                return $?
            fi
        done
    done

    # Mark wave complete
    if state_mark_wave_complete "$brand_dir" "$wave"; then
        :
    else
        status=$?
        log_error "Unable to mark wave $wave complete in runner state"
        # The complete-state update is atomic, so this best-effort cleanup cannot
        # leave a partial completion marker behind.
        if state_mark_wave_failed "$brand_dir" "$wave"; then
            :
        else
            log_error "Unable to record failed wave '$wave' after state write failure"
        fi
        return "$status"
    fi

    log_success "Wave $wave complete"
    return 0
}

execute_spoke() {
    local cluster="$1"
    local spoke="$2"
    local brand_dir="$3"
    local brand_config="$4"
    local status

    local start_time
    if start_time=$(date +%s); then
        :
    else
        status=$?
        log_error "Unable to start timing for spoke: $spoke"
        return "$status"
    fi

    local prompt_file
    prompt_file=$(prompt_path "$brand_dir" "$spoke")
    local output_file
    output_file=$(output_path "$brand_dir" "$spoke")

    # A brand may have imported outputs before its first coordinator run.
    # Ensure prompts have a durable home before shell redirection writes them.
    if mkdir -p "$(dirname "$prompt_file")" "$(dirname "$output_file")"; then
        :
    else
        status=$?
        log_error "Unable to create artifact directories for spoke: $spoke"
        record_spoke_failure "$brand_dir" "$spoke" "$status"
        return $?
    fi

    # Generate prompt from spoke SKILL.md + brand context
    if generate_spoke_prompt "$cluster" "$spoke" "$brand_config" "$brand_dir" > "$prompt_file"; then
        :
    else
        status=$?
        log_error "Prompt generation failed for spoke: $spoke"
        record_spoke_failure "$brand_dir" "$spoke" "$status"
        return $?
    fi

    log_info "Prompt written: $prompt_file"
    log_info "Waiting for output: $output_file"

    # In non-interactive mode, wait for output
    # In interactive mode, agent will execute and save output
    if wait_for_output "$output_file" 600; then
        :
    else
        status=$?
        local end_time
        end_time=$(date +%s) || end_time="$start_time"
        local duration=$((end_time - start_time))
        if vault_append_metric "| $(timestamp_local) | $(yaml_get "$brand_config" "name") | $cluster | $spoke | ${duration}s | TIMEOUT | Waiting for output |"; then
            :
        else
            log_warn "Unable to write timeout metric for spoke: $spoke"
        fi
        record_spoke_failure "$brand_dir" "$spoke" "$status"
        return $?
    fi

    # An interactive operator can skip submission, but a skipped/missing output
    # is never a completed spoke even when a wait implementation returns zero.
    if [[ ! -f "$output_file" ]]; then
        log_error "Output missing after wait for spoke: $spoke"
        record_spoke_failure "$brand_dir" "$spoke" 1
        return $?
    fi

    # Validate output
    if validate_spoke_output "$spoke" "$output_file"; then
        :
    else
        status=$?
        local end_time
        end_time=$(date +%s) || end_time="$start_time"
        local duration=$((end_time - start_time))
        if vault_append_metric "| $(timestamp_local) | $(yaml_get "$brand_config" "name") | $cluster | $spoke | ${duration}s | INVALID | Output validation failed |"; then
            :
        else
            log_warn "Unable to write invalid-output metric for spoke: $spoke"
        fi
        record_spoke_failure "$brand_dir" "$spoke" "$status"
        return $?
    fi

    # Log success
    local end_time
    end_time=$(date +%s) || end_time="$start_time"
    local duration=$((end_time - start_time))
    if state_record_skill_success "$brand_dir" "$spoke"; then
        :
    else
        status=$?
        log_error "Unable to record completed spoke '$spoke' in runner state"
        return "$status"
    fi

    if vault_append_metric "| $(timestamp_local) | $(yaml_get "$brand_config" "name") | $cluster | $spoke | ${duration}s | OK | |"; then
        :
    else
        log_warn "Unable to write success metric for spoke: $spoke"
    fi

    return 0
}

generate_spoke_prompt() {
    local cluster="$1"
    local spoke="$2"
    local brand_config="$3"
    local brand_dir="$4"
    
    local spoke_file="$PROJECT_ROOT/clusters/$cluster/spokes/${spoke}.md"
    local core_file="$PROJECT_ROOT/clusters/$cluster/brandmint-${cluster}-core.md"

    # Spoke file must exist
    if [[ ! -f "$spoke_file" ]]; then
        log_error "Spoke file not found: $spoke_file"
        return 1
    fi

    # Brand config must exist and be readable
    if [[ ! -f "$brand_config" ]]; then
        log_error "Unable to read brand config: $brand_config"
        return 1
    fi

    # Parse and validate dependencies from YAML frontmatter
    local resolved_deps
    if ! resolved_deps=$(python3 -c '
import sys, re, yaml

spoke_file, cluster, spoke = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    with open(spoke_file, "r", encoding="utf-8") as f:
        content = f.read()
except Exception as e:
    sys.stderr.write(f"Unable to read spoke file {spoke_file}: {e}\n")
    sys.exit(1)

deps = []
if content.startswith("---"):
    parts = content.split("---", 2)
    if len(parts) < 3:
        sys.stderr.write(f"Malformed frontmatter in {spoke_file}: unclosed frontmatter block\n")
        sys.exit(1)
    try:
        fm = yaml.safe_load(parts[1])
    except Exception as e:
        sys.stderr.write(f"Malformed YAML in frontmatter {spoke_file}: {e}\n")
        sys.exit(1)
    if fm is not None:
        if not isinstance(fm, dict):
            sys.stderr.write(f"Malformed frontmatter in {spoke_file}: root is not a mapping\n")
            sys.exit(1)
        raw_deps = fm.get("dependencies")
        if raw_deps is not None:
            if not isinstance(raw_deps, list):
                sys.stderr.write(f"Malformed dependencies in {spoke_file}: expected list, got {type(raw_deps).__name__}\n")
                sys.exit(1)
            name_re = re.compile(r"^[a-zA-Z0-9_-]+$")
            for item in raw_deps:
                if not isinstance(item, str) or not name_re.match(item.strip()):
                    sys.stderr.write(f"Malformed dependency name in {spoke_file}: {item!r}\n")
                    sys.exit(1)
                deps.append(item.strip())

if cluster in ("content", "social-growth", "brandmint-content", "brandmint-social-growth"):
    shared = ["voice-and-tone", "messaging-framework", "buyer-persona", "product-positioning"]
    for s in shared:
        if s not in deps:
            deps.append(s)

seen = set()
resolved = []
for d in deps:
    if d == spoke:
        continue
    if d not in seen:
        seen.add(d)
        resolved.append(d)

for d in resolved:
    print(d)
' "$spoke_file" "$cluster" "$spoke" 2>&1); then
        log_error "Dependency resolution failed for spoke $spoke: $resolved_deps"
        return 1
    fi

    # Build prompt from:
    # 1. Core cluster context
    # 2. Spoke instructions
    # 3. Brand config data
    # 4. Upstream outputs (dependencies)
    
    cat <<EOF
# Brandmint Skill Execution: $spoke

## Cluster: $cluster

EOF
    
    # Include core if exists
    if [[ -f "$core_file" ]]; then
        echo "## Core Reference"
        echo ""
        if ! cat "$core_file"; then
            log_error "Unable to read core file: $core_file"
            return 1
        fi
        echo ""
    fi
    
    # Include spoke
    echo "## Skill Instructions"
    echo ""
    if ! cat "$spoke_file"; then
        log_error "Unable to read spoke file: $spoke_file"
        return 1
    fi
    echo ""
    
    # Include brand config context
    echo "## Brand Context"
    echo ""
    echo '```yaml'
    if ! cat "$brand_config"; then
        log_error "Unable to read brand config: $brand_config"
        return 1
    fi
    echo '```'
    echo ""
    
    # Include upstream outputs for declared dependencies only
    local outputs_dir="$brand_dir/.brandmint/outputs"
    if [[ -n "$resolved_deps" ]]; then
        echo "## Upstream Outputs"
        echo ""
        local dep
        while IFS= read -r dep; do
            [[ -z "$dep" ]] && continue
            local output_path="$outputs_dir/${dep}.json"
            echo "### $dep"
            if [[ -f "$output_path" ]]; then
                echo '```json'
                if ! cat "$output_path"; then
                    log_error "Unable to read upstream output: $output_path"
                    return 1
                fi
                echo '```'
            else
                echo "*(Dependency output missing: required upstream source outputs/${dep}.json not available)*"
            fi
            echo ""
        done <<< "$resolved_deps"
    fi
    
    # Output instructions
    cat <<EOF
## Output Requirements

Write your output as valid JSON to:
\`$brand_dir/.brandmint/outputs/${spoke}.json\`

The output must include:
- \`skill\`: "$spoke"
- \`cluster\`: "$cluster"
- \`timestamp\`: ISO 8601 timestamp
- \`status\`: "complete" or "partial"
- \`data\`: skill-specific output data
EOF
}

validate_spoke_output() {
    local spoke="$1"
    local output_file="$2"

    if [[ ! -f "$output_file" ]]; then
        log_error "Output file missing: $output_file"
        return 1
    fi

    if ! jq empty "$output_file" 2>/dev/null; then
        log_error "Invalid JSON in output: $output_file"
        return 1
    fi

    if ! jq -e -s --arg spoke "$spoke" \
        'length == 1 and (.[0] | type == "object" and .skill == $spoke and .status == "complete")' \
        "$output_file" &>/dev/null; then
        log_error "Output must have matching skill '$spoke' and status 'complete'"
        return 1
    fi

    return 0
}

run_checkpoint() {
    local wave="$1"
    local brand_dir="$2"
    
    log_info "--- Checkpoint after wave $wave ---"
    
    # Run checkpoint script if exists
    local checkpoint_script="$PROJECT_ROOT/orchestrator/checkpoint.sh"
    if [[ -x "$checkpoint_script" ]]; then
        bash "$checkpoint_script" --brand-dir "$brand_dir" --wave "$wave" || return $?
    fi
    
    # Basic health check
    local completed
    completed=$(state_get "$brand_dir" ".completed_skills | length" "0")
    local failed
    failed=$(state_get "$brand_dir" ".failed_skills | length" "0")
    
    log_info "Completed skills: $completed"
    log_info "Failed skills: $failed"
    
    if [[ "$failed" -gt 0 ]]; then
        log_warn "Some skills failed. Review before continuing."
        if [[ "$NON_INTERACTIVE" != "true" ]]; then
            read -p "Continue? [y/N] " -n 1 -r
            echo
            [[ $REPLY =~ ^[Yy]$ ]] || return 1
        fi
    fi
}

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

main() {
    parse_args "$@"
    
    # Resolve brand directory
    local brand_dir
    brand_dir=$(dirname "$(realpath "$CONFIG")")
    
    log_info "Brand config: $CONFIG"
    log_info "Brand dir: $brand_dir"
    log_info "Waves: $WAVES"
    log_info "Non-interactive: $NON_INTERACTIVE"
    log_info "Dry-run: $DRY_RUN"
    
    # Initialize state
    state_init "$brand_dir"
    
    # Parse wave range
    local waves
    waves=$(parse_wave_range "$WAVES")
    
    # Dry run: just show plan
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "=== DRY RUN - Execution Plan ==="
        for wave in $waves; do
            local dry_clusters
            dry_clusters=$(wave_to_clusters "$wave")
            echo "Wave $wave: $dry_clusters"
            for cluster in $dry_clusters; do
                echo "  Cluster: $cluster"
                local spokes_list
                spokes_list=$(list_spokes "$cluster")
                if [[ -z "$spokes_list" ]]; then
                    echo "    (no spokes)"
                else
                    echo "$spokes_list" | sed 's/^/    - /'
                fi
            done
        done
        exit 0
    fi
    
    # Write plan to vault
    local plan_content
    plan_content=$(cat <<EOF
# Brandmint Execution Plan

**Brand:** $(yaml_get "$CONFIG" "name" "Unknown")
**Waves:** $WAVES
**Started:** $(timestamp_local)
**Mode:** $(if $NON_INTERACTIVE; then echo "Non-interactive"; else echo "Interactive"; fi)

## Wave Breakdown

$(for wave in $waves; do
    echo "### Wave $wave"
    for cluster in $(wave_to_clusters "$wave"); do
        echo "#### Cluster: $cluster"
        list_spokes "$cluster" | sed 's/^/- /'
        echo ""
    done
done)

## Status

- [ ] Execution started
EOF
)
    vault_write_plan "$(yaml_get "$CONFIG" "name")" "$WAVES" "$plan_content"
    
    # Execute waves
    for wave in $waves; do
        execute_wave "$wave" "$brand_dir" "$CONFIG" || return $?
        
        # Checkpoint between waves (except last)
        local last_wave
        last_wave=$(echo "$waves" | tail -1)
        if [[ "$wave" != "$last_wave" ]]; then
            run_checkpoint "$wave" "$brand_dir" || return $?
        fi
    done
    
    # Final summary
    log_success "=== Pipeline Complete ==="
    log_info "Completed waves: $(state_get "$brand_dir" ".completed_waves | join(\", \")")"
    log_info "Completed skills: $(state_get "$brand_dir" ".completed_skills | length")"
    log_info "Failed skills: $(state_get "$brand_dir" ".failed_skills | length")"
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    main "$@"
fi
