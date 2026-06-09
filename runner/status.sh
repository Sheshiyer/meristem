#!/usr/bin/env bash
#
# brandmint v2 - Pipeline Status Checker
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

CONFIG=""

usage() {
    cat <<EOF
Usage: bm status [options]

Check pipeline execution status.

Options:
    --config <path>         Brand config YAML (required)
    --json                  Output as JSON
    --verbose               Show detailed skill status
EOF
}

parse_args() {
    JSON_OUTPUT=false
    VERBOSE=false
    
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --config)
                CONFIG="$2"
                shift 2
                ;;
            --json)
                JSON_OUTPUT=true
                shift
                ;;
            --verbose)
                VERBOSE=true
                shift
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

main() {
    parse_args "$@"
    
    local brand_dir
    brand_dir=$(dirname "$(realpath "$CONFIG")")
    
    local state_file
    state_file=$(state_file "$brand_dir")
    
    if [[ ! -f "$state_file" ]]; then
        if [[ "$JSON_OUTPUT" == "true" ]]; then
            echo '{"status": "not_initialized", "message": "Pipeline not initialized"}'
        else
            log_info "Pipeline not initialized for this brand"
            log_info "Run: bm launch --config $CONFIG"
        fi
        exit 0
    fi
    
    # Read state
    local status
    status=$(json_get "$state_file" ".status" "unknown")
    local current_wave
    current_wave=$(json_get "$state_file" ".current_wave" "0")
    local completed_waves
    completed_waves=$(json_get "$state_file" ".completed_waves | length" "0")
    local completed_skills
    completed_skills=$(json_get "$state_file" ".completed_skills | length" "0")
    local failed_skills
    failed_skills=$(json_get "$state_file" ".failed_skills | length" "0")
    local updated_at
    updated_at=$(json_get "$state_file" ".updated_at" "unknown")
    
    if [[ "$JSON_OUTPUT" == "true" ]]; then
        cat "$state_file"
        exit 0
    fi
    
    # Human-readable output
    echo ""
    echo "${BOLD}Brandmint Pipeline Status${RESET}"
    echo "========================="
    echo ""
    echo "Brand:            $(yaml_get "$CONFIG" "name" "Unknown")"
    echo "Config:           $CONFIG"
    echo "Status:           $status"
    echo "Current Wave:     $current_wave / 7"
    echo "Completed Waves:  $completed_waves"
    echo "Completed Skills: $completed_skills"
    echo "Failed Skills:    $failed_skills"
    echo "Last Updated:     $updated_at"
    echo ""
    
    # Wave breakdown
    echo "${BOLD}Wave Progress:${RESET}"
    for wave in 1 2 3 4 5 6 7; do
        local cluster
        cluster=$(wave_to_cluster "$wave")
        local wave_status="pending"
        
        # Check if wave is in completed_waves array
        if jq -e ".completed_waves | index($wave)" "$state_file" &>/dev/null; then
            wave_status="${GREEN}complete${RESET}"
        elif [[ "$current_wave" == "$wave" ]]; then
            wave_status="${YELLOW}in_progress${RESET}"
        fi
        
        printf "  Wave %d: %-15s %s\n" "$wave" "$cluster" "$wave_status"
    done
    echo ""
    
    if [[ "$VERBOSE" == "true" ]]; then
        echo "${BOLD}Completed Skills:${RESET}"
        jq -r '.completed_skills[]' "$state_file" 2>/dev/null | sed 's/^/  - /' || echo "  (none)"
        echo ""
        
        if [[ "$failed_skills" -gt 0 ]]; then
            echo "${BOLD}${RED}Failed Skills:${RESET}"
            jq -r '.failed_skills[]' "$state_file" 2>/dev/null | sed 's/^/  - /'
            echo ""
        fi
        
        # Check outputs
        echo "${BOLD}Outputs:${RESET}"
        local outputs_dir="$brand_dir/.brandmint/outputs"
        if [[ -d "$outputs_dir" ]]; then
            find "$outputs_dir" -name "*.json" -type f | while read -r f; do
                local name
                name=$(basename "$f" .json)
                local size
                size=$(wc -c < "$f" | tr -d ' ')
                printf "  %-25s %s bytes\n" "$name" "$size"
            done
        else
            echo "  (no outputs yet)"
        fi
    fi
    
    # Suggestions
    if [[ "$status" == "initialized" ]]; then
        echo "${CYAN}Next step:${RESET} bm launch --config $CONFIG"
    elif [[ "$failed_skills" -gt 0 ]]; then
        echo "${YELLOW}Warning:${RESET} Some skills failed. Review and resume:"
        echo "  bm resume --config $CONFIG"
    elif [[ "$current_wave" -lt 7 ]]; then
        local next_wave=$((current_wave + 1))
        echo "${CYAN}Next step:${RESET} Continue from wave $next_wave:"
        echo "  bm launch --config $CONFIG --resume-from $next_wave"
    else
        echo "${GREEN}Pipeline complete!${RESET}"
    fi
}

main "$@"
