#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
test_root="$(mktemp -d)"
trap 'rm -rf "$test_root"' EXIT

# shellcheck source=../runner/launch.sh
source "$repo_root/runner/launch.sh"

generate_spoke_prompt() { printf 'prompt'; }
wait_for_output() { return 0; }
validate_spoke_output() { return 0; }
vault_append_metric() { return 0; }
state_set() { return 0; }
log_info() { return 0; }

brand_dir="$test_root/brand"
mkdir -p "$brand_dir"
brand_config="$brand_dir/brand-config.yaml"
printf 'name: Test Brand\n' > "$brand_config"

execute_spoke foundation audience "$brand_dir" "$brand_config"

test -d "$brand_dir/.brandmint/prompts"
test -d "$brand_dir/.brandmint/outputs"
test "$(cat "$brand_dir/.brandmint/prompts/audience.md")" = "prompt"

printf 'runner directory regression test passed\n'
