#!/usr/bin/env bash
# Tests for parse_wave_range: comma-separated lists, validation, dedup, error cases
set -uo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$repo_root/runner/lib/common.sh"

pass=0
fail=0

fail_test() {
    printf 'FAIL: %s\n' "$*" >&2
    fail=$((fail + 1))
}

assert_equal() {
    local actual="$1"
    local expected="$2"
    local msg="$3"
    if [[ "$actual" != "$expected" ]]; then
        fail_test "$msg (expected '$expected', got '$actual')"
    else
        pass=$((pass + 1))
    fi
}

assert_dies() {
    local range="$1"
    local pattern="$2"
    local msg="$3"
    local output
    output=$(bash -c "source '$repo_root/runner/lib/common.sh'; parse_wave_range '$range'" 2>&1) && {
        fail_test "$msg: expected die but got success: '$output'"
        return
    }
    if [[ "$output" == *"$pattern"* ]]; then
        pass=$((pass + 1))
    else
        fail_test "$msg: expected pattern '$pattern' in error, got '$output'"
    fi
}

# --- Basic single wave ---
result=$(parse_wave_range "5")
assert_equal "$result" "5" "Single wave 5"

result=$(parse_wave_range "1")
assert_equal "$result" "1" "Single wave 1"

result=$(parse_wave_range "7")
assert_equal "$result" "7" "Single wave 7 (boundary)"

# --- Range ---
result=$(parse_wave_range "1-3")
assert_equal "$result" "$(printf '1\n2\n3')" "Range 1-3"

result=$(parse_wave_range "5-7")
assert_equal "$result" "$(printf '5\n6\n7')" "Range 5-7"

result=$(parse_wave_range "2-2")
assert_equal "$result" "2" "Degenerate range 2-2"

# --- Comma-separated ---
result=$(parse_wave_range "1-2,6")
assert_equal "$result" "$(printf '1\n2\n6')" "Comma range 1-2,6"

result=$(parse_wave_range "6,2,1-3")
assert_equal "$result" "$(printf '1\n2\n3\n6')" "Mixed comma 6,2,1-3 sorted"

result=$(parse_wave_range "1,3,5,7")
assert_equal "$result" "$(printf '1\n3\n5\n7')" "Individual commas 1,3,5,7"

# --- Deduplication ---
result=$(parse_wave_range "2,2,3")
assert_equal "$result" "$(printf '2\n3')" "Dedup 2,2,3"

result=$(parse_wave_range "1-3,2")
assert_equal "$result" "$(printf '1\n2\n3')" "Dedup 1-3,2"

result=$(parse_wave_range "1-7,5")
assert_equal "$result" "$(printf '1\n2\n3\n4\n5\n6\n7')" "Dedup 1-7,5"

# --- Whitespace tolerance ---
result=$(parse_wave_range " 1 - 2 , 6 ")
assert_equal "$result" "$(printf '1\n2\n6')" "Whitespace tolerant 1-2,6"

# --- Error cases ---
assert_dies "5-2" "reverse range" "Reverse range rejected"
assert_dies "0" "out of bounds" "Wave 0 rejected"
assert_dies "8" "out of bounds" "Wave 8 rejected"
assert_dies "1,,3" "empty segment" "Empty segment rejected"
assert_dies "abc" "Invalid wave range" "Non-numeric rejected"
assert_dies "1;rm" "Invalid wave range" "Injection rejected"
assert_dies "7-1" "reverse range" "Reverse large range rejected"

# --- Summary ---
printf '\n=== Wave Selection Tests: %d passed, %d failed ===\n' "$pass" "$fail"
[[ "$fail" -eq 0 ]] || exit 1
