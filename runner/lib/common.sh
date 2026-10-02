#!/usr/bin/env bash
#
# brandmint v2 - Common Shell Functions
# Source this in all scripts: source "$(dirname "$0")/lib/common.sh"
#
# shellcheck shell=bash

# Exit on error, undefined vars, pipe failures
set -euo pipefail

# Colors (only if terminal supports it)
if [[ -t 1 ]] && command -v tput &>/dev/null; then
    RED=$(tput setaf 1)
    GREEN=$(tput setaf 2)
    YELLOW=$(tput setaf 3)
    BLUE=$(tput setaf 4)
    MAGENTA=$(tput setaf 5)
    CYAN=$(tput setaf 6)
    RESET=$(tput sgr0)
    BOLD=$(tput bold)
else
    RED="" GREEN="" YELLOW="" BLUE="" MAGENTA="" CYAN="" RESET="" BOLD=""
fi

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

log_info() {
    echo "${BLUE}[INFO]${RESET} $*" >&2
}

log_success() {
    echo "${GREEN}[OK]${RESET} $*" >&2
}

log_warn() {
    echo "${YELLOW}[WARN]${RESET} $*" >&2
}

log_error() {
    echo "${RED}[ERROR]${RESET} $*" >&2
}

log_debug() {
    if [[ "${BRANDMINT_VERBOSE:-0}" == "1" ]]; then
        echo "${MAGENTA}[DEBUG]${RESET} $*" >&2
    fi
}

die() {
    log_error "$@"
    exit 1
}

# -----------------------------------------------------------------------------
# Validation
# -----------------------------------------------------------------------------

require_file() {
    local file="$1"
    local desc="${2:-file}"
    [[ -f "$file" ]] || die "Required $desc not found: $file"
}

require_dir() {
    local dir="$1"
    local desc="${2:-directory}"
    [[ -d "$dir" ]] || die "Required $desc not found: $dir"
}

require_cmd() {
    local cmd="$1"
    command -v "$cmd" &>/dev/null || die "Required command not found: $cmd"
}

require_env() {
    local var
    for var in "$@"; do
        [[ -n "${!var:-}" ]] || die "Required environment variable not set: $var"
    done
}

require_in_range() {
    local val="$1"
    local min="$2"
    local max="$3"
    [[ "$val" -ge "$min" && "$val" -le "$max" ]] || \
        die "Value $val out of range [$min, $max]"
}

# -----------------------------------------------------------------------------
# YAML Parsing (minimal, no deps)
# -----------------------------------------------------------------------------

yaml_get() {
    local file="$1"
    local key="$2"
    local default="${3:-}"

    # JSON is valid YAML and is used by the portfolio configs.
    if jq -e 'type == "object"' "$file" >/dev/null 2>&1; then
        jq -r --arg key "$key" --arg fallback "$default" '.[$key] // $fallback' "$file"
        return
    fi

    # Simple key: value extraction (no nested support)
    local value
    value=$(grep -E "^${key}:" "$file" 2>/dev/null | head -1 | sed 's/^[^:]*: *//' | sed 's/^["'"'"']//' | sed 's/["'"'"']$//')

    if [[ -z "$value" ]]; then
        echo "$default"
    else
        echo "$value"
    fi
}

yaml_get_nested() {
    local file="$1"
    local path="$2"  # e.g., "brand.name"
    local default="${3:-}"

    # Use yq if available, otherwise fallback to grep
    if command -v yq &>/dev/null; then
        yq -r ".$path // \"$default\"" "$file" 2>/dev/null || echo "$default"
    else
        # Fallback: flatten dotted path to simple grep
        local key="${path##*.}"
        yaml_get "$file" "$key" "$default"
    fi
}

# -----------------------------------------------------------------------------
# JSON Handling (via jq)
# -----------------------------------------------------------------------------

json_get() {
    local file="$1"
    local path="$2"
    local default="${3:-}"

    require_cmd jq
    jq -r "$path // \"$default\"" "$file" 2>/dev/null || echo "$default"
}

json_update() {
    local file="$1"
    local filter="$2"
    shift 2

    if ! command -v jq &>/dev/null; then
        log_error "Required command not found: jq"
        return 127
    fi

    if [[ ! -f "$file" ]]; then
        log_error "JSON file not found: $file"
        return 1
    fi

    # Keep the replacement in the same directory so mv is an atomic rename.
    local tmp
    if ! tmp=$(mktemp "$(dirname "$file")/.json-update.XXXXXX"); then
        log_error "Unable to create temporary JSON update file for: $file"
        return 1
    fi

    local status
    if jq "$@" "$filter" "$file" > "$tmp" 2>/dev/null; then
        if mv -f "$tmp" "$file"; then
            return 0
        else
            status=$?
        fi
        log_error "Unable to replace JSON file: $file"
    else
        status=$?
        log_error "Unable to update JSON file: $file"
    fi

    rm -f "$tmp"
    return "$status"
}

json_set() {
    local file="$1"
    local path="$2"
    local value="$3"

    # Support two call forms:
    #  - json_set FILE '.path' VALUE         -> jq '.path = VALUE'
    #  - json_set FILE '.arr += [x]' '[]'    -> jq '.arr += [x]'  (path is already a full update expr)
    local filter
    if [[ "$path" == *"="* ]]; then
        filter="$path"
    else
        filter="$path = $value"
    fi

    json_update "$file" "$filter"
}

# -----------------------------------------------------------------------------
# State Management
# -----------------------------------------------------------------------------

state_file() {
    local brand_dir="$1"
    echo "$brand_dir/.brandmint/state.json"
}

state_init() {
    local brand_dir="$1"
    local state_file
    state_file=$(state_file "$brand_dir")

    mkdir -p "$(dirname "$state_file")"

    if [[ ! -f "$state_file" ]]; then
        cat > "$state_file" <<EOF
{
    "version": "2.0.0",
    "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "updated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "current_wave": 0,
    "completed_waves": [],
    "completed_skills": [],
    "failed_skills": [],
    "status": "initialized"
}
EOF
    fi
}

state_get() {
    local brand_dir="$1"
    local path="$2"
    local default="${3:-}"

    json_get "$(state_file "$brand_dir")" "$path" "$default"
}

state_set() {
    local brand_dir="$1"
    local path="$2"
    local value="$3"

    local mutation
    if [[ "$path" == *"="* ]]; then
        mutation="$path"
    else
        mutation="$path = $value"
    fi

    state_update "$brand_dir" "$mutation"
}

# Apply a state mutation and timestamp it in one jq rewrite. Additional arguments
# are passed directly to jq (for example: --arg skill "$skill").
state_update() {
    local brand_dir="$1"
    local filter="$2"
    shift 2

    local updated_at
    if ! updated_at=$(date -u +%Y-%m-%dT%H:%M:%SZ); then
        log_error "Unable to determine state update timestamp"
        return 1
    fi

    json_update "$(state_file "$brand_dir")" \
        "($filter) | .updated_at = \$updated_at" \
        --arg updated_at "$updated_at" "$@"
}

state_record_skill_success() {
    local brand_dir="$1"
    local skill="$2"

    state_update "$brand_dir" '
        .completed_skills = ((.completed_skills // []) |
            if index($skill) == null then . + [$skill] else . end)
        | .failed_skills = ((.failed_skills // []) | map(select(. != $skill)))
    ' --arg skill "$skill"
}

state_record_skill_failure() {
    local brand_dir="$1"
    local skill="$2"

    state_update "$brand_dir" '
        .failed_skills = ((.failed_skills // []) |
            if index($skill) == null then . + [$skill] else . end)
        | .completed_skills = ((.completed_skills // []) | map(select(. != $skill)))
    ' --arg skill "$skill"
}

state_mark_wave_started() {
    local brand_dir="$1"
    local wave="$2"

    state_update "$brand_dir" '
        .completed_waves = ((.completed_waves // []) | map(select(. != $wave)))
        | .current_wave = $wave
        | .status = "running"
    ' --argjson wave "$wave"
}

state_mark_wave_complete() {
    local brand_dir="$1"
    local wave="$2"

    state_update "$brand_dir" '
        .completed_waves = ((.completed_waves // []) |
            if index($wave) == null then . + [$wave] else . end)
        | .current_wave = $wave
        | .status = "running"
    ' --argjson wave "$wave"
}

state_mark_wave_failed() {
    local brand_dir="$1"
    local wave="$2"

    state_update "$brand_dir" '
        .completed_waves = ((.completed_waves // []) | map(select(. != $wave)))
        | .current_wave = $wave
        | .status = "failed"
    ' --argjson wave "$wave"
}

# -----------------------------------------------------------------------------
# Cluster Operations
# -----------------------------------------------------------------------------

WAVE_CLUSTERS=(
    "foundation"
    "strategy"
    "identity"
    "photography"
    "illustration"
    "content"
    "synthesis"
)

wave_to_cluster() {
    local wave="$1"
    require_in_range "$wave" 1 7
    echo "${WAVE_CLUSTERS[$((wave - 1))]}"
}

# Wave 6 has TWO clusters: content + social-growth
# Returns space-separated list of clusters for the wave.
wave_to_clusters() {
    local wave="$1"
    case "$wave" in
        6) echo "content social-growth" ;;
        *) wave_to_cluster "$wave" ;;
    esac
}

cluster_to_wave() {
    local cluster="$1"
    case "$cluster" in
        content|social-growth) echo 6; return ;;
    esac
    local i
    for i in "${!WAVE_CLUSTERS[@]}"; do
        if [[ "${WAVE_CLUSTERS[$i]}" == "$cluster" ]]; then
            echo "$((i + 1))"
            return
        fi
    done
    die "Unknown cluster: $cluster"
}

cluster_canonical_spokes() {
    local cluster="$1"
    case "$cluster" in
        foundation)
            echo "brand-foundation buyer-persona competitor-analysis value-proposition"
            ;;
        strategy)
            echo "voice-and-tone product-positioning messaging-framework brand-story"
            ;;
        identity)
            echo "color-palette typography logo-concept visual-language"
            ;;
        photography)
            echo "product-photography lifestyle-photography hero-images social-media-assets"
            ;;
        illustration)
            echo "brand-illustrations icon-system pattern-library"
            ;;
        content)
            echo "product-description landing-page-copy prelaunch-email-sequence launch-email-sequence welcome-email-sequence ad-creative-copy press-release"
            ;;
        social-growth)
            echo "social-content-engine short-form-hook-generator update-strategy-sequencer community-manager-brain review-response-strategist"
            ;;
        synthesis)
            echo "brand-documentation wiki-site-generator notebooklm-publishing deliverables-package campaign-orchestrator"
            ;;
        *)
            echo ""
            ;;
    esac
}

list_spokes() {
    local cluster="$1"
    local cluster_dir="${PROJECT_ROOT:-$(pwd)}/clusters/$cluster"

    require_dir "$cluster_dir/spokes" "cluster spokes directory"

    local canonical
    canonical=$(cluster_canonical_spokes "$cluster")

    local actual_files
    actual_files=$(find "$cluster_dir/spokes" -name "*.md" -type f | xargs -I {} basename {} .md | sort)

    if [[ -z "$actual_files" ]]; then
        return 0
    fi

    if [[ -z "$canonical" ]]; then
        echo "$actual_files"
        return 0
    fi

    local spoke
    for spoke in $canonical; do
        if [[ -f "$cluster_dir/spokes/${spoke}.md" ]]; then
            echo "$spoke"
        fi
    done

    local actual_spoke
    while IFS= read -r actual_spoke; do
        [[ -z "$actual_spoke" ]] && continue
        local is_canonical=false
        for spoke in $canonical; do
            if [[ "$actual_spoke" == "$spoke" ]]; then
                is_canonical=true
                break
            fi
        done
        if [[ "$is_canonical" == "false" ]]; then
            echo "$actual_spoke"
        fi
    done <<< "$actual_files"
}

# -----------------------------------------------------------------------------
# Prompt/Output Handling
# -----------------------------------------------------------------------------

prompt_path() {
    local brand_dir="$1"
    local skill="$2"
    echo "$brand_dir/.brandmint/prompts/${skill}.md"
}

output_path() {
    local brand_dir="$1"
    local skill="$2"
    echo "$brand_dir/.brandmint/outputs/${skill}.json"
}

wait_for_output() {
    local output_file="$1"
    local timeout_sec="${2:-300}"
    local poll_sec="${3:-5}"

    local elapsed=0
    while [[ ! -f "$output_file" ]] && [[ $elapsed -lt $timeout_sec ]]; do
        sleep "$poll_sec"
        elapsed=$((elapsed + poll_sec))
        log_debug "Waiting for output: $output_file ($elapsed/${timeout_sec}s)"
    done

    if [[ ! -f "$output_file" ]]; then
        log_error "Timeout waiting for output: $output_file"
        return 1
    fi

    log_success "Output received: $output_file"
    return 0
}

# -----------------------------------------------------------------------------
# Vault Operations (Obsidian/Conducty-style)
# -----------------------------------------------------------------------------

vault_root() {
    echo "${BRANDMINT_VAULT:-${PROJECT_ROOT:-$(pwd)}/orchestrator/vault}"
}

vault_write_plan() {
    local brand_name="$1"
    local waves="$2"
    local content="$3"

    local vault
    vault=$(vault_root)
    local timestamp
    timestamp=$(date +"%Y-%m-%d %H%M")
    local filename="Plan $timestamp $brand_name.md"

    mkdir -p "$vault/Plans"
    echo "$content" > "$vault/Plans/$filename"

    log_info "Plan written: $filename"
    echo "$vault/Plans/$filename"
}

vault_append_metric() {
    local metric_line="$1"

    local vault
    vault=$(vault_root)
    local metrics_file="$vault/Accumulators/Metrics.md"

    mkdir -p "$(dirname "$metrics_file")"

    if [[ ! -f "$metrics_file" ]]; then
        cat > "$metrics_file" <<EOF
# Metrics

| Timestamp | Brand | Wave | Skill | Duration | Status | Notes |
|-----------|-------|------|-------|----------|--------|-------|
EOF
    fi

    echo "$metric_line" >> "$metrics_file"
}

vault_log_failure() {
    local pattern="$1"
    local context="$2"

    local vault
    vault=$(vault_root)
    local failures_file="$vault/Accumulators/Failure Patterns.md"

    mkdir -p "$(dirname "$failures_file")"

    if [[ ! -f "$failures_file" ]]; then
        cat > "$failures_file" <<EOF
# Failure Patterns

Accumulated failure patterns from pipeline runs. Used to inform future plans.

---

EOF
    fi

    cat >> "$failures_file" <<EOF

## $(date +"%Y-%m-%d %H:%M")

**Pattern:** $pattern

**Context:** $context

---
EOF
}

# -----------------------------------------------------------------------------
# Visual Pipeline
# -----------------------------------------------------------------------------

generate_image() {
    local prompt="$1"
    local output="$2"
    local ref_image="${3:-}"

    local gen_script="${PROJECT_ROOT:-$(pwd)}/visual/gpt-image-2/scripts/gen.sh"
    require_file "$gen_script" "gpt-image-2 generator"

    local args=(--prompt "$prompt" --out "$output")
    [[ -n "$ref_image" ]] && args+=(--ref "$ref_image")

    log_info "Generating image: $output"
    bash "$gen_script" "${args[@]}"
}

generate_video() {
    local prompt="$1"
    local output="$2"
    local duration="${3:-30}"

    local gen_script="${PROJECT_ROOT:-$(pwd)}/visual/arcplume/scripts/gen-video.sh"
    require_file "$gen_script" "arcplume video generator"

    log_info "Generating video: $output"
    bash "$gen_script" "$prompt" "$output" "$duration"
}

# -----------------------------------------------------------------------------
# Utility
# -----------------------------------------------------------------------------

timestamp() {
    date -u +%Y-%m-%dT%H:%M:%SZ
}

timestamp_local() {
    date +"%Y-%m-%d %H:%M"
}

# Parse wave range: supports N, N-M, and comma-separated (e.g. "1-2,6" -> "1\n2\n6")
# Validates each segment is an integer 1..7, disallows reverse/empty ranges.
# Output: sorted unique wave numbers, one per line.
parse_wave_range() {
    local range="$1"
    local -a result=()
    local segment

    IFS=',' read -ra _segments <<< "$range"
    for segment in "${_segments[@]}"; do
        # Strip all whitespace from segment (handles "1 - 2" -> "1-2")
        segment="${segment//[[:space:]]/}"
        if [[ -z "$segment" ]]; then
            die "Invalid wave range: empty segment in '$range'"
        fi
        if [[ "$segment" =~ ^([0-9]+)-([0-9]+)$ ]]; then
            local start="${BASH_REMATCH[1]}"
            local end="${BASH_REMATCH[2]}"
            if [[ "$start" -gt "$end" ]]; then
                die "Invalid wave range: reverse range '$segment' in '$range'"
            fi
            if [[ "$start" -lt 1 || "$end" -gt 7 ]]; then
                die "Wave range out of bounds: '$segment' (must be 1..7)"
            fi
            local i
            for ((i=start; i<=end; i++)); do
                result+=("$i")
            done
        elif [[ "$segment" =~ ^[0-9]+$ ]]; then
            if [[ "$segment" -lt 1 || "$segment" -gt 7 ]]; then
                die "Wave number out of bounds: '$segment' (must be 1..7)"
            fi
            result+=("$segment")
        else
            die "Invalid wave range: '$segment' in '$range' (expected N or N-M)"
        fi
    done

    if [[ ${#result[@]} -eq 0 ]]; then
        die "Wave range produced no valid waves from '$range'"
    fi

    printf '%s\n' "${result[@]}" | sort -nu
}
