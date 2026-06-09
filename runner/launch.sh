#!/usr/bin/env bash
#
# brandmint v2 - Pipeline Launcher
# Executes waves in order with conducty-style checkpoints
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
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

execute_wave() {
    local wave="$1"
    local brand_dir="$2"
    local brand_config="$3"
    
    local cluster
    cluster=$(wave_to_cluster "$wave")
    
    log_info "=== Wave $wave: $cluster ==="
    
    local cluster_dir="$PROJECT_ROOT/clusters/$cluster"
    require_dir "$cluster_dir" "cluster directory"
    
    # Get list of spokes
    local spokes
    spokes=$(list_spokes "$cluster")
    
    if [[ -z "$spokes" ]]; then
        log_warn "No spokes found for cluster: $cluster"
        return 0
    fi
    
    # Tracer-first: run first spoke to validate assumptions
    local tracer
    tracer=$(echo "$spokes" | head -1)
    log_info "Running tracer: $tracer"
    
    if ! execute_spoke "$cluster" "$tracer" "$brand_dir" "$brand_config"; then
        log_error "Tracer failed for wave $wave. Plan needs revision."
        vault_log_failure "Tracer failure: $tracer" "Wave $wave, cluster $cluster"
        return 1
    fi
    
    # Execute remaining spokes
    echo "$spokes" | tail -n +2 | while read -r spoke; do
        [[ -z "$spoke" ]] && continue
        log_info "Running spoke: $spoke"
        execute_spoke "$cluster" "$spoke" "$brand_dir" "$brand_config" || {
            log_error "Spoke failed: $spoke"
            state_set "$brand_dir" ".failed_skills += [\"$spoke\"]" "[]"
        }
    done
    
    # Mark wave complete
    state_set "$brand_dir" ".completed_waves += [$wave]" "[]"
    state_set "$brand_dir" ".current_wave" "$wave"
    
    log_success "Wave $wave complete"
}

execute_spoke() {
    local cluster="$1"
    local spoke="$2"
    local brand_dir="$3"
    local brand_config="$4"
    
    local start_time
    start_time=$(date +%s)
    
    local prompt_file
    prompt_file=$(prompt_path "$brand_dir" "$spoke")
    local output_file
    output_file=$(output_path "$brand_dir" "$spoke")
    
    # Generate prompt from spoke SKILL.md + brand context
    generate_spoke_prompt "$cluster" "$spoke" "$brand_config" "$brand_dir" > "$prompt_file"
    
    log_info "Prompt written: $prompt_file"
    log_info "Waiting for output: $output_file"
    
    # In non-interactive mode, wait for output
    # In interactive mode, agent will execute and save output
    if ! wait_for_output "$output_file" 600; then
        local end_time
        end_time=$(date +%s)
        local duration=$((end_time - start_time))
        vault_append_metric "| $(timestamp_local) | $(yaml_get "$brand_config" "name") | $cluster | $spoke | ${duration}s | TIMEOUT | Waiting for output |"
        return 1
    fi
    
    # Validate output
    if ! validate_spoke_output "$spoke" "$output_file"; then
        local end_time
        end_time=$(date +%s)
        local duration=$((end_time - start_time))
        vault_append_metric "| $(timestamp_local) | $(yaml_get "$brand_config" "name") | $cluster | $spoke | ${duration}s | INVALID | Output validation failed |"
        return 1
    fi
    
    # Log success
    local end_time
    end_time=$(date +%s)
    local duration=$((end_time - start_time))
    vault_append_metric "| $(timestamp_local) | $(yaml_get "$brand_config" "name") | $cluster | $spoke | ${duration}s | OK | |"
    
    state_set "$brand_dir" ".completed_skills += [\"$spoke\"]" "[]"
    
    return 0
}

generate_spoke_prompt() {
    local cluster="$1"
    local spoke="$2"
    local brand_config="$3"
    local brand_dir="$4"
    
    local spoke_file="$PROJECT_ROOT/clusters/$cluster/spokes/${spoke}.md"
    local core_file="$PROJECT_ROOT/clusters/$cluster/brandmint-${cluster}-core.md"
    
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
        cat "$core_file"
        echo ""
    fi
    
    # Include spoke
    if [[ -f "$spoke_file" ]]; then
        echo "## Skill Instructions"
        echo ""
        cat "$spoke_file"
        echo ""
    else
        log_warn "Spoke file not found: $spoke_file"
    fi
    
    # Include brand config context
    echo "## Brand Context"
    echo ""
    echo '```yaml'
    cat "$brand_config"
    echo '```'
    echo ""
    
    # Include upstream outputs if any
    local outputs_dir="$brand_dir/.brandmint/outputs"
    if [[ -d "$outputs_dir" ]] && ls "$outputs_dir"/*.json &>/dev/null; then
        echo "## Upstream Outputs"
        echo ""
        for output in "$outputs_dir"/*.json; do
            local name
            name=$(basename "$output" .json)
            echo "### $name"
            echo '```json'
            cat "$output"
            echo '```'
            echo ""
        done
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
    
    # Check file exists and is valid JSON
    require_file "$output_file" "output file"
    
    if ! jq empty "$output_file" 2>/dev/null; then
        log_error "Invalid JSON in output: $output_file"
        return 1
    fi
    
    # Check required fields
    local skill
    skill=$(json_get "$output_file" ".skill" "")
    local status
    status=$(json_get "$output_file" ".status" "")
    
    if [[ -z "$skill" ]]; then
        log_error "Output missing 'skill' field"
        return 1
    fi
    
    if [[ -z "$status" ]]; then
        log_error "Output missing 'status' field"
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
        bash "$checkpoint_script" --brand-dir "$brand_dir" --wave "$wave"
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
            local cluster
            cluster=$(wave_to_cluster "$wave")
            echo "Wave $wave: $cluster"
            echo "  Spokes:"
            list_spokes "$cluster" | sed 's/^/    - /'
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
    cluster=$(wave_to_cluster "$wave")
    echo "### Wave $wave: $cluster"
    echo ""
    list_spokes "$cluster" | sed 's/^/- /'
    echo ""
done)

## Status

- [ ] Execution started
EOF
)
    vault_write_plan "$(yaml_get "$CONFIG" "name")" "$WAVES" "$plan_content"
    
    # Execute waves
    for wave in $waves; do
        execute_wave "$wave" "$brand_dir" "$CONFIG"
        
        # Checkpoint between waves (except last)
        local last_wave
        last_wave=$(echo "$waves" | tail -1)
        if [[ "$wave" != "$last_wave" ]]; then
            run_checkpoint "$wave" "$brand_dir"
        fi
    done
    
    # Final summary
    log_success "=== Pipeline Complete ==="
    log_info "Completed waves: $(state_get "$brand_dir" ".completed_waves | join(\", \")")"
    log_info "Completed skills: $(state_get "$brand_dir" ".completed_skills | length")"
    log_info "Failed skills: $(state_get "$brand_dir" ".failed_skills | length")"
}

main "$@"
