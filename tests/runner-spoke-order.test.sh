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
assert_equal "$strategy_spokes" $'product-positioning\nvoice-and-tone\nmessaging-framework\nbrand-story' \
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

# 6. Dependency graph: canonical order satisfies declared frontmatter dependencies
#    for waves 1, 2, and 6 (all real spoke files in the repository).
#    Every dependency of each spoke must either (a) live in an earlier wave,
#    (b) appear earlier in the same wave's canonical ordering (cross-cluster
#    within the wave, respecting cluster execution order: content then social-growth),
#    or (c) appear earlier in the same cluster's canonical order.

PROJECT_ROOT="$repo_root"

extract_frontmatter_deps() {
    local spoke_file="$1"
    local in_frontmatter=0
    local in_deps=0
    local deps=""
    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if [[ $in_frontmatter -eq 0 ]]; then
                in_frontmatter=1
            else
                break
            fi
            continue
        fi
        if [[ $in_frontmatter -eq 1 ]]; then
            if [[ "$line" =~ ^dependencies:\ *$ ]]; then
                in_deps=1
                continue
            fi
            if [[ $in_deps -eq 1 ]]; then
                if [[ "$line" =~ ^[[:space:]]+-[[:space:]]+(.+)$ ]]; then
                    local dep
                    dep=$(echo "${BASH_REMATCH[1]}" | tr -d '"' | tr -d "'" | xargs)
                    [[ -n "$dep" ]] && deps="$deps $dep"
                elif [[ "$line" =~ ^[[:space:]]*$ ]]; then
                    continue
                else
                    in_deps=0
                fi
            fi
        fi
    done < "$spoke_file"
    echo "$deps"
}

# Canonical orders by wave — wave 6 clusters executed in order: content then social-growth
w1_canonical="brand-foundation buyer-persona competitor-analysis value-proposition"
w2_canonical="product-positioning voice-and-tone messaging-framework brand-story"
# Wave 6: content first, then social-growth (matches runner execution order)
w6_content_canonical="product-description landing-page-copy prelaunch-email-sequence launch-email-sequence welcome-email-sequence ad-creative-copy press-release"
w6_social_canonical="social-content-engine short-form-hook-generator update-strategy-sequencer community-manager-brain review-response-strategist"
w6_wave_ordered="$w6_content_canonical $w6_social_canonical"

# Resolve waves without associative arrays so macOS Bash 3.2 is supported.
spoke_wave_for() {
    local candidate="$1"
    local item
    for item in $w1_canonical; do
        if [[ "$item" == "$candidate" ]]; then echo 1; return; fi
    done
    for item in $w2_canonical; do
        if [[ "$item" == "$candidate" ]]; then echo 2; return; fi
    done
    for item in $w6_wave_ordered; do
        if [[ "$item" == "$candidate" ]]; then echo 6; return; fi
    done
    echo 0
}

# All spokes from earlier waves (wave < current)
w1_earlier=""
w2_earlier="$w1_canonical"
w6_earlier="$w1_canonical $w2_canonical"

dep_errors=0

check_cluster_deps() {
    local cluster="$1"
    local wave="$2"
    local earlier_spokes="$3"
    local wave_ordered_spokes="$4"
    local cluster_dir="$repo_root/clusters/$cluster/spokes"
    local canonical
    canonical=$(cluster_canonical_spokes "$cluster")

    for spoke in $canonical; do
        local spoke_file="$cluster_dir/$spoke.md"
        [[ -f "$spoke_file" ]] || continue
        local deps
        deps=$(extract_frontmatter_deps "$spoke_file")
        for dep in $deps; do
            local dep_wave
            dep_wave="$(spoke_wave_for "$dep")"
            if [[ "$dep_wave" -gt 0 && "$dep_wave" -lt "$wave" ]]; then
                continue  # earlier wave — always satisfied
            fi
            if [[ "$dep_wave" -eq "$wave" ]]; then
                # Check if dep is in earlier-wave spokes (shouldn't be for same wave, but guard)
                local in_earlier=false
                for e in $earlier_spokes; do
                    [[ "$e" == "$dep" ]] && in_earlier=true && break
                done
                if [[ "$in_earlier" == "true" ]]; then
                    continue
                fi
                # Check wave-level ordering: dep must appear before spoke in wave ordered list
                local found_spoke=false
                local found_dep=false
                for w in $wave_ordered_spokes; do
                    if [[ "$w" == "$spoke" ]]; then
                        found_spoke=true
                        break
                    fi
                    if [[ "$w" == "$dep" ]]; then
                        found_dep=true
                        break
                    fi
                done
                if [[ "$found_dep" == "false" ]]; then
                    printf 'DEPENDENCY ERROR: %s (wave %d) depends on %s which is not ordered before it\n' \
                        "$spoke" "$wave" "$dep" >&2
                    dep_errors=$((dep_errors + 1))
                fi
            elif [[ "$dep_wave" -eq 0 ]]; then
                printf 'DEPENDENCY WARNING: %s depends on unknown spoke %s (not in any canonical wave)\n' \
                    "$spoke" "$dep" >&2
            else
                printf 'DEPENDENCY ERROR: %s (wave %d) depends on %s (wave %d) — reverse dependency\n' \
                    "$spoke" "$wave" "$dep" "$dep_wave" >&2
                dep_errors=$((dep_errors + 1))
            fi
        done
    done
}

check_cluster_deps "foundation" 1 "$w1_earlier" "$w1_canonical"
check_cluster_deps "strategy" 2 "$w2_earlier" "$w2_canonical"
check_cluster_deps "content" 6 "$w6_earlier" "$w6_wave_ordered"
check_cluster_deps "social-growth" 6 "$w6_earlier" "$w6_wave_ordered"

if [[ $dep_errors -gt 0 ]]; then
    fail "$dep_errors dependency graph violation(s) found in canonical spoke ordering"
fi

printf 'dependency graph tests passed for waves 1, 2, 6\n'

chmod +x "$repo_root/tests/runner-spoke-order.test.sh"
printf 'runner spoke order tests passed\n'
