#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
test_root="$(mktemp -d)"
trap 'rm -rf "$test_root"' EXIT

# Isolate temp vault
export BRANDMINT_VAULT="$test_root/vault"
mkdir -p "$BRANDMINT_VAULT"

# shellcheck source=../runner/launch.sh
source "$repo_root/runner/launch.sh"

fixture_root="$test_root/project"
mkdir -p "$fixture_root/clusters"
PROJECT_ROOT="$fixture_root"

# Stub external side effects
vault_append_metric() { return 0; }
vault_log_failure() { return 0; }
vault_write_plan() { return 0; }
log_info() { return 0; }
log_success() { return 0; }
log_warn() { return 0; }
log_error() { return 0; }

fail() {
    printf 'FAIL: %s\n' "$*" >&2
    exit 1
}

assert_contains() {
    local haystack="$1"
    local needle="$2"
    local message="$3"
    if [[ "$haystack" != *"$needle"* ]]; then
        fail "$message (did not find '$needle')"
    fi
}

assert_not_contains() {
    local haystack="$1"
    local needle="$2"
    local message="$3"
    if [[ "$haystack" == *"$needle"* ]]; then
        fail "$message (unexpectedly found '$needle')"
    fi
}

assert_equal() {
    local actual="$1"
    local expected="$2"
    local message="$3"
    [[ "$actual" == "$expected" ]] || fail "$message (expected '$expected', got '$actual')"
}

# Helper to set up brand
new_test_brand() {
    local name="$1"
    local bdir="$test_root/brands/$name"
    mkdir -p "$bdir/.brandmint/outputs" "$bdir/.brandmint/prompts"
    printf 'name: %s\nindustry: AI Technology\n' "$name" > "$bdir/brand-config.yaml"
    state_init "$bdir"
    echo "$bdir"
}

# Helper to create spoke file
create_spoke_md() {
    local cluster="$1"
    local spoke="$2"
    local content="$3"
    mkdir -p "$fixture_root/clusters/$cluster/spokes"
    printf '%s\n' "$content" > "$fixture_root/clusters/$cluster/spokes/${spoke}.md"
}

# Helper to create cluster core
create_cluster_core() {
    local cluster="$1"
    local content="$2"
    mkdir -p "$fixture_root/clusters/$cluster"
    printf '%s\n' "$content" > "$fixture_root/clusters/$cluster/brandmint-${cluster}-core.md"
}

# Helper to write output JSON
write_json_output() {
    local bdir="$1"
    local skill="$2"
    local json_body="$3"
    local out="$bdir/.brandmint/outputs/${skill}.json"
    printf '%s\n' "$json_body" > "$out"
}

# -----------------------------------------------------------------------------
# Test 1: Required JSON included in full
# -----------------------------------------------------------------------------
brand1=$(new_test_brand "brand1")
create_spoke_md "foundation" "buyer-persona" $'---\nname: buyer-persona\ndependencies:\n  - brand-foundation\n---\n# Buyer Persona Instructions\nBuild buyer personas.'
full_foundation_json='{
  "skill": "brand-foundation",
  "cluster": "foundation",
  "status": "complete",
  "timestamp": "2026-10-02T10:00:00Z",
  "data": {
    "mission": "Deliver deterministic brand pipelines",
    "values": ["precision", "rigor", "clarity"],
    "long_claim": "Detailed narrative about enterprise architecture that must not be truncated."
  }
}'
write_json_output "$brand1" "brand-foundation" "$full_foundation_json"

prompt1=$(generate_spoke_prompt "foundation" "buyer-persona" "$brand1/brand-config.yaml" "$brand1")
assert_contains "$prompt1" "## Upstream Outputs" "Test 1: Upstream Outputs header missing"
assert_contains "$prompt1" "### brand-foundation" "Test 1: brand-foundation section missing"
assert_contains "$prompt1" "Detailed narrative about enterprise architecture that must not be truncated." "Test 1: full JSON content missing"
assert_contains "$prompt1" "## Skill Instructions" "Test 1: Skill Instructions missing"
assert_contains "$prompt1" "## Brand Context" "Test 1: Brand Context missing"
assert_contains "$prompt1" "## Output Requirements" "Test 1: Output Requirements missing"

# -----------------------------------------------------------------------------
# Test 2: Unrelated huge output excluded & prompt size bound (< 128 KiB)
# -----------------------------------------------------------------------------
brand2=$(new_test_brand "brand2")
create_spoke_md "foundation" "buyer-persona" $'---\nname: buyer-persona\ndependencies:\n  - brand-foundation\n---\n# Instructions\nOnly depends on foundation.'
write_json_output "$brand2" "brand-foundation" "$full_foundation_json"

# Write a 200KB huge unrelated output file into .brandmint/outputs/
huge_data=$(python3 -c 'import json; print(json.dumps({"skill": "huge-unrelated-output", "status": "complete", "payload": "X" * 200000}))')
write_json_output "$brand2" "huge-unrelated-output" "$huge_data"

prompt2=$(generate_spoke_prompt "foundation" "buyer-persona" "$brand2/brand-config.yaml" "$brand2")
assert_contains "$prompt2" "### brand-foundation" "Test 2: declared dependency missing"
assert_not_contains "$prompt2" "huge-unrelated-output" "Test 2: unrelated huge output was not excluded"
assert_not_contains "$prompt2" "XXXXXXXXXX" "Test 2: payload from unrelated output found in prompt"

prompt2_bytes=${#prompt2}
if [[ "$prompt2_bytes" -ge 131072 ]]; then
    fail "Test 2: prompt size ($prompt2_bytes bytes) exceeds 128 KiB guard"
fi

# -----------------------------------------------------------------------------
# Test 3: Duplicate dependency names emitted once
# -----------------------------------------------------------------------------
brand3=$(new_test_brand "brand3")
create_spoke_md "strategy" "product-positioning" $'---\nname: product-positioning\ndependencies:\n  - buyer-persona\n  - buyer-persona\n  - competitor-analysis\n  - buyer-persona\n---\n# Instructions\nPositioning.'
write_json_output "$brand3" "buyer-persona" '{"skill":"buyer-persona","status":"complete","data":{"persona":"CTO"}}'
write_json_output "$brand3" "competitor-analysis" '{"skill":"competitor-analysis","status":"complete","data":{"competitors":["CompA"]}}'

prompt3=$(generate_spoke_prompt "strategy" "product-positioning" "$brand3/brand-config.yaml" "$brand3")
occurrences=$(echo "$prompt3" | grep -c "### buyer-persona" || true)
assert_equal "$occurrences" "1" "Test 3: duplicate dependency name should appear exactly once"

# -----------------------------------------------------------------------------
# Test 4: Empty dependencies -> No Upstream Outputs header
# -----------------------------------------------------------------------------
brand4=$(new_test_brand "brand4")
create_spoke_md "foundation" "brand-foundation" $'---\nname: brand-foundation\ndependencies: []\n---\n# Instructions\nTracer spoke with no dependencies.'
write_json_output "$brand4" "some-prior" '{"skill":"some-prior","status":"complete"}'

prompt4=$(generate_spoke_prompt "foundation" "brand-foundation" "$brand4/brand-config.yaml" "$brand4")
assert_not_contains "$prompt4" "## Upstream Outputs" "Test 4: empty dependencies should not produce Upstream Outputs section"
assert_not_contains "$prompt4" "some-prior" "Test 4: unreferenced prior output included in empty dependencies spoke"

# -----------------------------------------------------------------------------
# Test 5: Shared content inputs automatically included for content & social-growth
# -----------------------------------------------------------------------------
brand5=$(new_test_brand "brand5")
create_spoke_md "content" "ad-creative-copy" $'---\nname: ad-creative-copy\ndependencies:\n  - custom-brief\n---\n# Ad Creative Copy\nGenerate ads.'
create_spoke_md "social-growth" "community-manager-brain" $'---\nname: community-manager-brain\ndependencies:\n  - custom-sop\n---\n# Community Manager\nHandle community.'

write_json_output "$brand5" "voice-and-tone" '{"skill":"voice-and-tone","status":"complete"}'
write_json_output "$brand5" "messaging-framework" '{"skill":"messaging-framework","status":"complete"}'
write_json_output "$brand5" "buyer-persona" '{"skill":"buyer-persona","status":"complete"}'
write_json_output "$brand5" "product-positioning" '{"skill":"product-positioning","status":"complete"}'
write_json_output "$brand5" "custom-brief" '{"skill":"custom-brief","status":"complete"}'

prompt5_content=$(generate_spoke_prompt "content" "ad-creative-copy" "$brand5/brand-config.yaml" "$brand5")
assert_contains "$prompt5_content" "### custom-brief" "Test 5 (content): custom declared dependency missing"
assert_contains "$prompt5_content" "### voice-and-tone" "Test 5 (content): shared voice-and-tone missing"
assert_contains "$prompt5_content" "### messaging-framework" "Test 5 (content): shared messaging-framework missing"
assert_contains "$prompt5_content" "### buyer-persona" "Test 5 (content): shared buyer-persona missing"
assert_contains "$prompt5_content" "### product-positioning" "Test 5 (content): shared product-positioning missing"

prompt5_social=$(generate_spoke_prompt "social-growth" "community-manager-brain" "$brand5/brand-config.yaml" "$brand5")
assert_contains "$prompt5_social" "### custom-sop" "Test 5 (social-growth): custom declared dependency missing"
assert_contains "$prompt5_social" "### voice-and-tone" "Test 5 (social-growth): shared voice-and-tone missing"
assert_contains "$prompt5_social" "### messaging-framework" "Test 5 (social-growth): shared messaging-framework missing"
assert_contains "$prompt5_social" "### buyer-persona" "Test 5 (social-growth): shared buyer-persona missing"
assert_contains "$prompt5_social" "### product-positioning" "Test 5 (social-growth): shared product-positioning missing"

# -----------------------------------------------------------------------------
# Test 6: Missing dependency explicitly marked with source requirement
# -----------------------------------------------------------------------------
brand6=$(new_test_brand "brand6")
create_spoke_md "strategy" "brand-story" $'---\nname: brand-story\ndependencies:\n  - brand-foundation\n  - missing-upstream-source\n---\n# Brand Story\nNarrative.'
write_json_output "$brand6" "brand-foundation" '{"skill":"brand-foundation","status":"complete"}'
# missing-upstream-source is NOT created

prompt6=$(generate_spoke_prompt "strategy" "brand-story" "$brand6/brand-config.yaml" "$brand6")
assert_contains "$prompt6" "### brand-foundation" "Test 6: existing dependency missing"
assert_contains "$prompt6" "### missing-upstream-source" "Test 6: missing dependency section header missing"
assert_contains "$prompt6" "Dependency output missing: required upstream source outputs/missing-upstream-source.json not available" "Test 6: missing dependency explicit notice missing"

# -----------------------------------------------------------------------------
# Test 7: Malicious and malformed frontmatter rejected with non-zero exit code
# -----------------------------------------------------------------------------
brand7=$(new_test_brand "brand7")

# Subtest 7a: Unclosed frontmatter fence
create_spoke_md "foundation" "bad-fence" $'---\nname: bad-fence\ndependencies:\n  - foo\n# Unclosed fence\nBody'
if generate_spoke_prompt "foundation" "bad-fence" "$brand7/brand-config.yaml" "$brand7" 2>/dev/null; then
    fail "Test 7a: unclosed frontmatter fence should fail prompt generation"
fi

# Subtest 7b: Malformed YAML syntax
create_spoke_md "foundation" "bad-yaml" $'---\n[broken yaml : {\n---\n# Body'
if generate_spoke_prompt "foundation" "bad-yaml" "$brand7/brand-config.yaml" "$brand7" 2>/dev/null; then
    fail "Test 7b: malformed YAML should fail prompt generation"
fi

# Subtest 7c: dependencies is a string instead of a list
create_spoke_md "foundation" "bad-type" $'---\nname: bad-type\ndependencies: "not-a-list"\n---\n# Body'
if generate_spoke_prompt "foundation" "bad-type" "$brand7/brand-config.yaml" "$brand7" 2>/dev/null; then
    fail "Test 7c: string dependencies should fail prompt generation"
fi

# Subtest 7d: Malicious dependency name (injection payload)
create_spoke_md "foundation" "malicious-name" $'---\nname: malicious-name\ndependencies:\n  - "foo; rm -rf /"\n---\n# Body'
if generate_spoke_prompt "foundation" "malicious-name" "$brand7/brand-config.yaml" "$brand7" 2>/dev/null; then
    fail "Test 7d: malicious dependency name should fail prompt generation"
fi

# Subtest 7e: Dependency with spaces or shell metacharacters
create_spoke_md "foundation" "bad-chars" $'---\nname: bad-chars\ndependencies:\n  - "invalid dep name"\n---\n# Body'
if generate_spoke_prompt "foundation" "bad-chars" "$brand7/brand-config.yaml" "$brand7" 2>/dev/null; then
    fail "Test 7e: dependency name with spaces should fail prompt generation"
fi

chmod +x "$repo_root/tests/runner-prompt-dependencies.test.sh"
printf 'runner prompt dependencies tests passed (all 7 scenarios verified)\n'
