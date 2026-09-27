#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$repo_root/runner/launch.sh"
test_root=$(mktemp -d)
trap 'rm -rf "$test_root"' EXIT
failures=0
printf '{"current_wave":0}\n' > "$test_root/state.json"
original=$(cat "$test_root/state.json")
(
    mv() { return 71; }
    if json_update "$test_root/state.json" '.current_wave = 9'; then
        echo 'FAIL: failed rename returned success'; exit 1
    else
        code=$?
        [[ "$code" == 71 ]] || { echo 'FAIL: failed rename lost exit status'; exit 1; }
    fi
    [[ $(cat "$test_root/state.json") == "$original" ]] || { echo 'FAIL: failed rename changed state'; exit 1; }
    [[ -z $(find "$test_root" -name '.json-update.*') ]] || { echo 'FAIL: failed rename leaked temporary state'; exit 1; }
) || failures=$((failures + 1))
mkdir -p "$test_root/project/clusters/example/spokes" "$test_root/brand"
PROJECT_ROOT="$test_root/project"
printf '# source\n' > "$PROJECT_ROOT/clusters/example/spokes/demo.md"
if generate_spoke_prompt example demo "$test_root/brand/missing-config.yaml" "$test_root/brand" > "$test_root/prompt.md"; then
    echo 'FAIL: missing real config produced successful prompt'; failures=$((failures + 1))
fi
printf '{"skill":"other","status":"partial"}\n{"skill":"demo","status":"complete"}\n' > "$test_root/output.json"
if validate_spoke_output demo "$test_root/output.json"; then
    echo 'FAIL: multiple JSON documents accepted as one output'; failures=$((failures + 1))
fi
# Sourced main must propagate wave failure even when called in a conditional.
(
    mkdir -p "$PROJECT_ROOT/clusters/foundation/spokes"
    printf 'name: Fixture\n' > "$test_root/brand/brand-config.yaml"
    vault_write_plan() { return 0; }
    yaml_get() { printf 'Fixture'; }
    execute_wave() { return 72; }
    log_success() { printf '%s\n' "$*" >> "$test_root/success.log"; }
    if main --config "$test_root/brand/brand-config.yaml" --waves 1 --non-interactive; then
        echo 'FAIL: main swallowed wave failure'; exit 1
    else
        [[ "$?" == 72 ]] || { echo 'FAIL: main lost wave exit code'; exit 1; }
    fi
    [[ ! -e "$test_root/success.log" ]] || { echo 'FAIL: failed main announced completion'; exit 1; }
) || failures=$((failures + 1))

# A one-spoke wave exercises empty remainder slices under macOS Bash 3.2.
(
    mkdir -p "$PROJECT_ROOT/clusters/foundation/spokes" "$test_root/single/.brandmint/outputs"
    printf '# only spoke\n' > "$PROJECT_ROOT/clusters/foundation/spokes/only.md"
    printf 'name: Single\n' > "$test_root/single/brand-config.yaml"
    printf '{"skill":"only","status":"complete"}\n' > "$test_root/single/.brandmint/outputs/only.json"
    state_init "$test_root/single"
    wait_for_output() { return 0; }
    vault_append_metric() { return 0; }
    cluster=caller_scope_sentinel
    execute_wave 1 "$test_root/single" "$test_root/single/brand-config.yaml"
    [[ "$cluster" == caller_scope_sentinel ]] || { echo 'FAIL: wave leaked cluster variable'; exit 1; }
    jq -e '.completed_waves == [1] and .completed_skills == ["only"]' \
        "$test_root/single/.brandmint/state.json" >/dev/null
) || failures=$((failures + 1))

# Checkpoint failures cannot be masked by later health-summary commands.
(
    mkdir -p "$PROJECT_ROOT/orchestrator"
    printf '#!/usr/bin/env bash\nexit 73\n' > "$PROJECT_ROOT/orchestrator/checkpoint.sh"
    chmod +x "$PROJECT_ROOT/orchestrator/checkpoint.sh"
    if run_checkpoint 1 "$test_root/single"; then
        echo 'FAIL: checkpoint failure was swallowed'; exit 1
    else
        [[ "$?" == 73 ]] || { echo 'FAIL: checkpoint lost exit status'; exit 1; }
    fi
) || failures=$((failures + 1))

[[ "$failures" == 0 ]] || exit 1
printf 'runner review regressions passed (6 scenarios)\n'
