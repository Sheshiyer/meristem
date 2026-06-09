#!/usr/bin/env python3
"""
Thoughtseed brandmint image helper.
Loads the Google/Gemini key from ~/.claude/.env in-process (no shell sourcing),
sets GEMINI_API_KEY, and delegates to the nanobanana generate_image().
Keeps the API key out of the shell command line and transcript.

Usage:
  python3 gen_image.py --prompt-file p.txt --out img.png --ratio 16:9 --size 2K
  python3 gen_image.py --prompt "..."      --out img.png --ratio 1:1
  python3 gen_image.py --prompt-file p.txt --out edit.png --input base.png   # edit mode
"""
import os
import sys
import argparse
from pathlib import Path

NB_SCRIPTS = "/Users/sheshnarayaniyer/.agents/skills/nanobanana/scripts"


def load_key(preferred=None) -> str:
    env_path = Path.home() / ".claude" / ".env"
    keys = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        keys[k.strip()] = v.strip().strip('"').strip("'")
    order = ([preferred] if preferred else []) + [
        "GEMINI_API_KEY", "GOOGLE_API_KEY", "NANO_BANANA_API_KEY"
    ]
    for cand in order:
        if cand and keys.get(cand):
            return keys[cand]
    raise SystemExit("No GEMINI/GOOGLE/NANO_BANANA API key found in ~/.claude/.env")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--ratio", default=None)
    ap.add_argument("--size", default=None)
    ap.add_argument("--input", default=None)
    ap.add_argument("--key-name", default=None, dest="key_name")
    a = ap.parse_args()

    if a.prompt_file:
        prompt = Path(a.prompt_file).read_text().strip()
    elif a.prompt:
        prompt = a.prompt
    else:
        raise SystemExit("Provide --prompt or --prompt-file")

    os.environ["GEMINI_API_KEY"] = load_key(a.key_name)
    sys.path.insert(0, NB_SCRIPTS)
    from generate import generate_image

    res = generate_image(
        prompt=prompt,
        output_path=a.out,
        input_path=a.input,
        aspect_ratio=a.ratio,
        image_size=a.size,
        verbose=False,
    )
    if res.get("success"):
        print("OK " + res["path"])
        sys.exit(0)
    else:
        print("FAIL " + str(res.get("error")))
        sys.exit(1)


if __name__ == "__main__":
    main()
