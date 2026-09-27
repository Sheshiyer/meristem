#!/usr/bin/env bash
# Watch BrandMint prompts appear; print ACTION lines for the coordinator.
set -euo pipefail
BRAND_DIR=${1:-brands/iverif}
PROMPT_DIR="$BRAND_DIR/.brandmint/prompts"
OUT_DIR="$BRAND_DIR/.brandmint/outputs"
mkdir -p "$PROMPT_DIR" "$OUT_DIR"
seen_file="$BRAND_DIR/.brandmint/.seen-prompts"
touch "$seen_file"
while true; do
  for p in "$PROMPT_DIR"/*.md; do
    [[ -e "$p" ]] || continue
    base=$(basename "$p" .md)
    if grep -qx "$base" "$seen_file"; then
      continue
    fi
    echo "$base" >> "$seen_file"
    if [[ -f "$OUT_DIR/$base.json" ]]; then
      echo "READY: $base already has output"
    else
      echo "ACTION_REQUIRED: prompt ready for spoke=$base path=$p"
    fi
  done
  sleep 2
done
