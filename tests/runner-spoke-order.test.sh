#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
test_root="$(mktemp -d)"
trap 'rm -rf "$test_root"' EXIT

# shellcheck source=../runner/lib/common.sh
source "$repo_root/runner/lib/common.sh"

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

# 1. Real repository cluster canonical orders
PROJECT_ROOT="$repo_root"

foundation_spokes="$(list_spokes "foundation")"
assert_equal "$foundation_spokes" $'brand-foundation\nbuyer-persona\ncompetitor-analysis\nvalue-proposition' \
    'foundation spoke ordering incorrect'

strategy_spokes="$(list_spokes "strategy")"
assert_equal "$strategy_spokes" $'voice-and-tone\nproduct-positioning\nmessaging-framework\nbrand-story' \
    'strategy spoke ordering incorrect'

identity_spokes="$(list_spokes "identity")"
assert_equal "$identity_spokes" $'color-palette\ntypography\nlogo-concept\nvisual-language' \
    'identity spoke ordering incorrect'

photography_spokes="$(list_spokes "photography")"
assert_equal "$photography_spokes" $'product-photography\nlifestyle-photography\nhero-images\nsocial-media-assets' \
    'photography spoke ordering incorrect'

illustration_spokes="$(list_spokes "illustration")"
assert_equal "$illustration_spokes" $'brand-illustrations\nicon-system\npattern-library' \
    'illustration spoke ordering incorrect'

content_spokes="$(list_spokes "content")"
assert_equal "$content_spokes" $'product-description\nlanding-page-copy\nprelaunch-email-sequence\nlaunch-email-sequence\nwelcome-email-sequence\nad-creative-copy\npress-release' \
    'content spoke ordering incorrect'

social_growth_spokes="$(list_spokes "social-growth")"
assert_equal "$social_growth_spokes" $'social-content-engine\nshort-form-hook-generator\nupdate-strategy-sequencer\ncommunity-manager-brain\nreview-response-strategist' \
    'social-growth spoke ordering incorrect'

synthesis_spokes="$(list_spokes "synthesis")"
assert_equal "$synthesis_spokes" $'brand-documentation\nwiki-site-generator\nnotebooklm-publishing\ndeliverables-package\ncampaign-orchestrator' \
    'synthesis spoke ordering incorrect'

# 2. Fixture/unknown cluster fallback (deterministic alphabetical)
fixture_root="$test_root/fixtures"
PROJECT_ROOT="$fixture_root"
mkdir -p "$fixture_root/clusters/custom-cluster/spokes"
touch "$fixture_root/clusters/custom-cluster/spokes/zebra.md"
touch "$fixture_root/clusters/custom-cluster/spokes/alpha.md"
touch "$fixture_root/clusters/custom-cluster/spokes/middle.md"

custom_spokes="$(list_spokes "custom-cluster")"
assert_equal "$custom_spokes" $'alpha\nmiddle\nzebra' \
    'fixture cluster fallback alphabetical ordering incorrect'

# 3. Canonical cluster with subset of spokes (must not invent missing files)
mkdir -p "$fixture_root/clusters/strategy/spokes"
touch "$fixture_root/clusters/strategy/spokes/brand-story.md"
touch "$fixture_root/clusters/strategy/spokes/voice-and-tone.md"

subset_strategy="$(list_spokes "strategy")"
assert_equal "$subset_strategy" $'voice-and-tone\nbrand-story' \
    'canonical cluster subset ordering incorrect'

# 4. Canonical cluster with extra/unlisted spokes (canonical first, extra at end sorted)
touch "$fixture_root/clusters/strategy/spokes/z-extra.md"
touch "$fixture_root/clusters/strategy/spokes/a-extra.md"

extra_strategy="$(list_spokes "strategy")"
assert_equal "$extra_strategy" $'voice-and-tone\nbrand-story\na-extra\nz-extra' \
    'canonical cluster with unlisted spokes ordering incorrect'

# 5. Empty spokes directory
mkdir -p "$fixture_root/clusters/empty-cluster/spokes"
empty_spokes="$(list_spokes "empty-cluster")"
assert_equal "$empty_spokes" "" 'empty cluster spokes should be empty'

chmod +x "$repo_root/tests/runner-spoke-order.test.sh"
printf 'runner spoke order tests passed\n'
