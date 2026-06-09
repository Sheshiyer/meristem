#!/usr/bin/env python3
import os, sys
from pathlib import Path

def load_key(preferred=None):
    keys = {}
    for line in (Path.home()/".claude"/".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k,_,v = line.partition("="); keys[k.strip()] = v.strip().strip('"').strip("'")
    order = ([preferred] if preferred else []) + ["GEMINI_API_KEY","GOOGLE_API_KEY","NANO_BANANA_API_KEY"]
    for c in order:
        if c and keys.get(c): return keys[c]
    raise SystemExit("no key")

key = load_key(sys.argv[1] if len(sys.argv) > 1 else "GOOGLE_API_KEY")
from google import genai
from google.genai import types
client = genai.Client(api_key=key)
for model in ["imagen-4.0-fast-generate-001", "imagen-4.0-generate-001"]:
    try:
        r = client.models.generate_images(
            model=model,
            prompt="a single matte teal circle centered on a deep blue-black textured background, minimal, no text",
            config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio="16:9"),
        )
        imgs = getattr(r, "generated_images", None) or []
        if imgs:
            out = Path("brands/thoughtseed/generated/_imagen_probe.png")
            out.parent.mkdir(parents=True, exist_ok=True)
            imgs[0].image.save(str(out))
            print(f"[{model}] OK saved {out}")
            break
        else:
            print(f"[{model}] no images returned: {r}")
    except Exception as e:
        print(f"[{model}] RAW ERROR: {repr(e)[:300]}")
