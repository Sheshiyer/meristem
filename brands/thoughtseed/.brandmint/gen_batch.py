#!/usr/bin/env python3
"""Batch image generator for the Thoughtseed brandmint run.
Reads a manifest [{id, subject, ratio, size}], appends the shared style DNA,
generates each via nanobanana (NANO_BANANA_API_KEY), retries on rate-limit,
paces calls, is idempotent (skips existing), and writes a results JSON + log.
"""
import os, sys, json, time
from pathlib import Path

NB_SCRIPTS = "/Users/sheshnarayaniyer/.agents/skills/nanobanana/scripts"
BRAND = Path("/Volumes/madara/2026/twc-vault/01-Projects/thoughtseed/brandmint-v2/brands/thoughtseed")
OUTDIR = BRAND / "generated"
LOG = BRAND / ".brandmint" / "image-batch.log"
RESULTS = BRAND / ".brandmint" / "image-batch-results.json"

STYLE = (
    "Rendered in the Thoughtseed 'Digital Wilderness' system: a deep quantum blue-black world "
    "where disciplined engineering precision meets organic emergence. Cool screen-glow lighting "
    "and architectural shadow; tactile materials such as matte black paper, brushed aluminum, "
    "weathered stone, living moss and oxidized copper; fine teal signal lines and faint directional "
    "node networks; at most one small warm golden-orange ignition accent. Editorial-documentary look, "
    "clean high contrast, premium and restrained, with intentional negative space and an architectural "
    "crop. Absolutely no text, no words, no letters, numbers or logos anywhere. No purple gradients, "
    "no stock people or faces, no glossy plastic, no sci-fi cliche, no mystical fog, no cartoon iconography."
)


def load_key(preferred="NANO_BANANA_API_KEY"):
    keys = {}
    for line in (Path.home()/".claude"/".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        keys[k.strip()] = v.strip().strip('"').strip("'")
    for c in [preferred, "GEMINI_API_KEY", "GOOGLE_API_KEY", "NANO_BANANA_API_KEY"]:
        if c and keys.get(c):
            return keys[c]
    raise SystemExit("no key")


def logp(msg):
    print(msg, flush=True)
    with open(LOG, "a") as f:
        f.write(msg + "\n")


def main():
    manifest = json.loads(Path(sys.argv[1]).read_text())
    OUTDIR.mkdir(parents=True, exist_ok=True)
    os.environ["GEMINI_API_KEY"] = load_key()
    sys.path.insert(0, NB_SCRIPTS)
    from generate import generate_image

    results = []
    logp(f"=== batch start: {len(manifest)} images ===")
    for item in manifest:
        out = OUTDIR / f"{item['id']}.png"
        if out.exists() and out.stat().st_size > 10000:
            logp(f"SKIP {item['id']} (exists)")
            results.append({**item, "status": "exists", "path": str(out)})
            continue
        prompt = item["subject"].strip() + " " + STYLE
        err = ""
        ok = False
        for attempt in range(1, 5):
            res = generate_image(
                prompt=prompt, output_path=str(out),
                aspect_ratio=item.get("ratio"), image_size=item.get("size"),
                verbose=False,
            )
            if res.get("success"):
                logp(f"OK {item['id']} -> {res['path']}")
                results.append({**item, "status": "ok", "path": res["path"]})
                ok = True
                break
            err = str(res.get("error"))
            logp(f"RETRY {item['id']} attempt {attempt}: {err[:90]}")
            time.sleep(8 * attempt)
        if not ok:
            results.append({**item, "status": "fail", "error": err})
            logp(f"FAIL {item['id']}: {err[:90]}")
        time.sleep(4)
        RESULTS.write_text(json.dumps(results, indent=2))

    done = sum(1 for r in results if r["status"] in ("ok", "exists"))
    logp(f"=== batch done: {done}/{len(manifest)} ok ===")


if __name__ == "__main__":
    main()
