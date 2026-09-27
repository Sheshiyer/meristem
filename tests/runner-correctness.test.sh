#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
test_root="$(mktemp -d)"
trap 'rm -rf "$test_root"' EXIT

# shellcheck source=../runner/launch.sh
source "$repo_root/runner/launch.sh"

fixture_root="$test_root/project"
mkdir -p "$fixture_root/clusters"
PROJECT_ROOT="$fixture_root"
ORDER_LOG="$test_root/order.log"

fail() {
    printf 'FAIL: %s\n' "$*" >&2
    exit 1
}

assert_equal() {
    local actual="$1"
    local expected="$2"
    local message="$3"

    [[ "$actual" == "$expected" ]] || fail "$message (expected '$expected', got '$actual')"
}

assert_json() {
    local file="$1"
    local filter="$2"
    jq -e "$filter" "$file" >/dev/null || fail "JSON assertion failed: $filter"
}

new_brand() {
    local name="$1"
    BRAND_DIR="$test_root/brands/$name"
    BRAND_CONFIG="$BRAND_DIR/brand-config.yaml"
    mkdir -p "$BRAND_DIR"
    printf 'name: Synthetic Test\n' > "$BRAND_CONFIG"
    state_init "$BRAND_DIR"
}

create_cluster() {
    local cluster="$1"
    shift

    mkdir -p "$fixture_root/clusters/$cluster/spokes"
    local spoke
    for spoke in "$@"; do
        printf '# synthetic %s\n' "$spoke" > "$fixture_root/clusters/$cluster/spokes/$spoke.md"
    done
}

write_output() {
    local brand_dir="$1"
    local skill="$2"
    local status="$3"
    local output_file
    output_file=$(output_path "$brand_dir" "$skill")
    mkdir -p "$(dirname "$output_file")"
    printf '{"skill":"%s","status":"%s"}\n' "$skill" "$status" > "$output_file"
}

generate_spoke_prompt() {
    local cluster="$1"
    local spoke="$2"
    printf '%s/%s\n' "$cluster" "$spoke" >> "$ORDER_LOG"
    printf 'prompt for %s\n' "$spoke"
}

# Synthetic output is prepared by each case, so never poll or sleep.
wait_for_output() { return 0; }
vault_append_metric() { return 0; }
vault_log_failure() { return 0; }
log_info() { return 0; }
log_success() { return 0; }
log_warn() { return 0; }
log_error() { return 0; }

# Wave 6 succeeds only after content then social-growth, every spoke completes,
# and the state contains each completion once.
create_cluster content a-content-tracer b-content-later
create_cluster social-growth a-social-tracer b-social-later
new_brand wave6-success
: > "$ORDER_LOG"
write_output "$BRAND_DIR" a-content-tracer complete
write_output "$BRAND_DIR" b-content-later complete
write_output "$BRAND_DIR" a-social-tracer complete
write_output "$BRAND_DIR" b-social-later complete
execute_wave 6 "$BRAND_DIR" "$BRAND_CONFIG"
assert_equal "$(<"$ORDER_LOG")" $'content/a-content-tracer\ncontent/b-content-later\nsocial-growth/a-social-tracer\nsocial-growth/b-social-later' \
    'wave 6 cluster/spoke order changed'
assert_json "$(state_file "$BRAND_DIR")" \
    '.completed_waves == [6] and .completed_skills == ["a-content-tracer", "b-content-later", "a-social-tracer", "b-social-later"] and .failed_skills == []'

# A missing cluster is a wave failure, not an empty successful wave.
new_brand missing-cluster
if execute_wave 2 "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'missing cluster completed its wave'
fi
assert_json "$(state_file "$BRAND_DIR")" \
    '(.completed_waves | index(2)) == null and .current_wave == 2 and .status == "failed"'

# An existing but empty spokes directory is also a wave failure.
mkdir -p "$fixture_root/clusters/strategy/spokes"
new_brand empty-cluster
if execute_wave 2 "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'empty cluster completed its wave'
fi
assert_json "$(state_file "$BRAND_DIR")" \
    '(.completed_waves | index(2)) == null and .current_wave == 2 and .status == "failed"'

# Tracer failure must stop the cluster before later spokes run.
create_cluster foundation a-tracer-fails b-later-not-run
new_brand tracer-failure
: > "$ORDER_LOG"
if execute_wave 1 "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'tracer failure completed its wave'
fi
assert_equal "$(<"$ORDER_LOG")" 'foundation/a-tracer-fails' 'later spoke ran after tracer failure'
assert_json "$(state_file "$BRAND_DIR")" \
    '(.completed_waves | index(1)) == null and .failed_skills == ["a-tracer-fails"]'

# A non-tracer failure must propagate and remove the wave completion marker.
create_cluster identity a-tracer-passes b-later-fails
new_brand later-failure
: > "$ORDER_LOG"
write_output "$BRAND_DIR" a-tracer-passes complete
write_output "$BRAND_DIR" b-later-fails partial
if execute_wave 3 "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'later spoke failure completed its wave'
fi
assert_equal "$(<"$ORDER_LOG")" $'identity/a-tracer-passes\nidentity/b-later-fails' \
    'later spoke did not run in tracer-first order'
assert_json "$(state_file "$BRAND_DIR")" \
    '(.completed_waves | index(3)) == null and .completed_skills == ["a-tracer-passes"] and .failed_skills == ["b-later-fails"]'

# A zero-status interactive wait is insufficient: skipped, missing, malformed,
# partial, and mismatched output files must all fail the spoke.
new_brand output-validation
for skill in skipped-output missing-output invalid-output empty-object-output partial-output mismatch-output; do
    : > "$ORDER_LOG"
    case "$skill" in
        skipped-output)
            write_output "$BRAND_DIR" "$skill" skipped
            ;;
        missing-output)
            ;;
        invalid-output)
            output_file=$(output_path "$BRAND_DIR" "$skill")
            mkdir -p "$(dirname "$output_file")"
            printf '{not json\n' > "$output_file"
            ;;
        empty-object-output)
            output_file=$(output_path "$BRAND_DIR" "$skill")
            mkdir -p "$(dirname "$output_file")"
            printf '{}\n' > "$output_file"
            ;;
        partial-output)
            write_output "$BRAND_DIR" "$skill" partial
            ;;
        mismatch-output)
            output_file=$(output_path "$BRAND_DIR" "$skill")
            mkdir -p "$(dirname "$output_file")"
            printf '{"skill":"different-skill","status":"complete"}\n' > "$output_file"
            ;;
    esac

    if execute_spoke synthetic "$skill" "$BRAND_DIR" "$BRAND_CONFIG"; then
        fail "invalid output unexpectedly completed: $skill"
    fi
    assert_json "$(state_file "$BRAND_DIR")" \
        ".failed_skills | index(\"$skill\") != null"
    assert_json "$(state_file "$BRAND_DIR")" \
        ".completed_skills | index(\"$skill\") == null"
done

# Successful retries are idempotent and clear an old failure for that skill.
new_brand retry-state
state_record_skill_failure "$BRAND_DIR" retry-spoke
write_output "$BRAND_DIR" retry-spoke complete
execute_spoke synthetic retry-spoke "$BRAND_DIR" "$BRAND_CONFIG"
execute_spoke synthetic retry-spoke "$BRAND_DIR" "$BRAND_CONFIG"
assert_json "$(state_file "$BRAND_DIR")" \
    '.completed_skills == ["retry-spoke"] and .failed_skills == []'

# A failed rerun revokes an old wave completion; a successful retry restores it
# once without retaining the stale failed skill.
create_cluster photography a-rerun-tracer b-rerun-later
new_brand rerun-wave
write_output "$BRAND_DIR" a-rerun-tracer complete
write_output "$BRAND_DIR" b-rerun-later complete
execute_wave 4 "$BRAND_DIR" "$BRAND_CONFIG"
write_output "$BRAND_DIR" b-rerun-later partial
if execute_wave 4 "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'failed rerun retained wave completion'
fi
assert_json "$(state_file "$BRAND_DIR")" \
    '(.completed_waves | index(4)) == null and .completed_skills == ["a-rerun-tracer"] and .failed_skills == ["b-rerun-later"]'
write_output "$BRAND_DIR" b-rerun-later complete
execute_wave 4 "$BRAND_DIR" "$BRAND_CONFIG"
assert_json "$(state_file "$BRAND_DIR")" \
    '.completed_waves == [4] and .completed_skills == ["a-rerun-tracer", "b-rerun-later"] and .failed_skills == []'

# Prompt-generation and state-write errors must be returned instead of being
# hidden by Bash's conditional errexit behavior.
new_brand prompt-generation-failure
saved_generate_spoke_prompt="$(declare -f generate_spoke_prompt)"
generate_spoke_prompt() { return 42; }
if execute_spoke synthetic prompt-failure "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'prompt-generation failure completed its spoke'
fi
assert_json "$(state_file "$BRAND_DIR")" \
    '.failed_skills == ["prompt-failure"] and .completed_skills == []'
eval "$saved_generate_spoke_prompt"

create_cluster synthetic prompt-source-failure
new_brand prompt-source-failure
missing_config="$test_root/missing-brand-config.yaml"
if execute_spoke synthetic prompt-source-failure "$BRAND_DIR" "$missing_config"; then
    fail 'unreadable prompt source completed its spoke'
fi
assert_json "$(state_file "$BRAND_DIR")" \
    '.failed_skills == ["prompt-source-failure"] and .completed_skills == []'

new_brand state-write-failure
write_output "$BRAND_DIR" state-write complete
saved_state_record_skill_success="$(declare -f state_record_skill_success)"
state_record_skill_success() { return 71; }
if execute_spoke synthetic state-write "$BRAND_DIR" "$BRAND_CONFIG"; then
    fail 'state-write failure completed its spoke'
fi
assert_json "$(state_file "$BRAND_DIR")" \
    '.completed_skills == [] and .failed_skills == []'
eval "$saved_state_record_skill_success"

# state_set remains a three-argument helper, returns jq failures, and preserves
# the last valid state rather than writing a partial file.
state_set "$BRAND_DIR" '.current_wave' '7'
assert_json "$(state_file "$BRAND_DIR")" '.current_wave == 7'
state_before="$(<"$(state_file "$BRAND_DIR")")"
if state_set "$BRAND_DIR" '.broken +=' '[]'; then
    fail 'invalid jq state update returned success'
fi
assert_equal "$(<"$(state_file "$BRAND_DIR")")" "$state_before" 'failed state update changed state'

printf 'runner correctness tests passed\n'
