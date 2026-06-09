#!/usr/bin/env python3
import os, sys
from pathlib import Path

def load_key(preferred=None):
    keys = {}
    for line in (Path.home()/".claude"/".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k,_,v = line.partition("=")
        keys[k.strip()] = v.strip().strip('"').strip("'")
    order = ([preferred] if preferred else []) + ["GEMINI_API_KEY","GOOGLE_API_KEY","NANO_BANANA_API_KEY"]
    for c in order:
        if c and keys.get(c):
            return c, keys[c]
    raise SystemExit("no key")

name, key = load_key(sys.argv[1] if len(sys.argv) > 1 else None)
print("using key var:", name, "(len", len(key), ")")
os.environ["GEMINI_API_KEY"] = key
from google import genai
from google.genai import types
client = genai.Client(api_key=key)

# 1) Which models are available to this key?
try:
    print("--- listing image-capable models ---")
    for m in client.models.list():
        nm = getattr(m, "name", "?")
        if "image" in nm.lower() or "imagen" in nm.lower() or "flash-image" in nm.lower():
            print("  ", nm)
except Exception as e:
    print("model list error:", repr(e)[:300])

# 2) Try the preview model with the RAW error surfaced
for model in ["gemini-3-pro-image-preview", "gemini-2.5-flash-image", "gemini-2.0-flash-preview-image-generation"]:
    try:
        r = client.models.generate_content(
            model=model,
            contents=["a single matte teal circle on a deep blue-black background, minimal"],
            config=types.GenerateContentConfig(response_modalities=["IMAGE","TEXT"]),
        )
        parts = r.candidates[0].content.parts
        has_img = any(getattr(p,"inline_data",None) and p.inline_data.mime_type.startswith("image/") for p in parts)
        print(f"[{model}] OK image={has_img}")
        break
    except Exception as e:
        print(f"[{model}] RAW ERROR: {repr(e)[:400]}")
