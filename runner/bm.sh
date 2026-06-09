#!/usr/bin/env bash
#
# brandmint v2 - Agent-Native Brand Pipeline
# Main entry point
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

VERSION="2.0.0-alpha"

usage() {
    cat <<EOF
brandmint v2 - Agent-Native Brand Pipeline

Usage: bm <command> [options]

Commands:
    launch      Run pipeline (all waves or subset)
    status      Check pipeline state
    resume      Resume from last checkpoint
    plan        Generate execution plan (conducty-style)
    checkpoint  Run health check between waves
    improve     Extract learnings from last run

Options:
    --config <path>         Brand config YAML (required)
    --waves <range>         Wave range (e.g., 1-3, default: 1-7)
    --non-interactive       No prompts, fail on missing data
    --dry-run               Show plan without executing
    --verbose               Enable debug output

Wave Reference:
    1: Foundation   (brand-foundation, buyer-persona, competitor-analysis)
    2: Strategy     (voice-tone, positioning, messaging, brand-story)
    3: Identity     (logo, colors, typography, visual-language)
    4: Photography  (lifestyle, product, hero shots)
    5: Illustration (brand-illustrations, icons, patterns)
    6: Content      (landing-page, emails, ads, press-release)
    7: Synthesis    (notebooklm, brand-docs, wiki)

Examples:
    bm launch --config /path/to/brand-config.yaml --waves 1-3
    bm status --config /path/to/brand-config.yaml
    bm resume --config /path/to/brand-config.yaml
    bm plan --config /path/to/brand-config.yaml --waves 1-7 --dry-run

Environment:
    BRANDMINT_VAULT     Override vault location (default: ./orchestrator/vault)
    BRANDMINT_VERBOSE   Enable verbose output (set to 1)

Version: $VERSION
EOF
}

main() {
    [[ $# -lt 1 ]] && { usage; exit 1; }
    
    local cmd="$1"
    shift
    
    case "$cmd" in
        launch)
            exec "$SCRIPT_DIR/launch.sh" "$@"
            ;;
        status)
            exec "$SCRIPT_DIR/status.sh" "$@"
            ;;
        resume)
            exec "$SCRIPT_DIR/resume.sh" "$@"
            ;;
        plan)
            exec "$PROJECT_ROOT/orchestrator/plan.sh" "$@"
            ;;
        checkpoint)
            exec "$PROJECT_ROOT/orchestrator/checkpoint.sh" "$@"
            ;;
        improve)
            exec "$PROJECT_ROOT/orchestrator/improve.sh" "$@"
            ;;
        version|--version|-v)
            echo "brandmint v$VERSION"
            exit 0
            ;;
        -h|--help|help)
            usage
            exit 0
            ;;
        *)
            log_error "Unknown command: $cmd"
            echo "Run 'bm --help' for usage."
            exit 1
            ;;
    esac
}

main "$@"
