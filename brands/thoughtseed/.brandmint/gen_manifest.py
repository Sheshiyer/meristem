#!/usr/bin/env python3
"""Build a validated asset-manifest.json from what actually exists on disk.
No hallucinated paths: every entry is stat-checked. Wave/skill inferred from filename.
"""
import json
from pathlib import Path

BRAND = Path("/Volumes/madara/2026/twc-vault/01-Projects/thoughtseed/brandmint-v2/brands/thoughtseed")
ASSETS = BRAND / "assets"
GEN = BRAND / "generated"

USER_ASSETS = [
    ("logo-wordmark", "thoughtseed-horizontal-wordmark-3x.png", "logo", True),
    ("logo-tree-mark", "thoughtseed-tree-mark-black-3x.png", "logo-icon", False),
    ("logo-reference-01", "thoughtseed-logo-reference-01.jpg", "reference", False),
    ("logo-reference-02", "thoughtseed-logo-reference-02.jpg", "reference", False),
]

# filename-prefix -> (wave, skill)
def gen_meta(name):
    if name.startswith("hero-"):
        return 4, "hero-images"
    if name.startswith("lifestyle-"):
        return 4, "lifestyle-photography"
    if name.startswith("product-"):
        return 4, "product-photography"
    if name.startswith("social-"):
        return 4, "social-media-assets"
    if name.startswith("illus-"):
        return 5, "brand-illustrations"
    if name.startswith("icons-"):
        return 5, "icon-system"
    if name.startswith("pattern-"):
        return 5, "pattern-library"
    if name.startswith("visual-language-"):
        return 3, "visual-language"
    return 0, "unknown"

missing = []
user_list = []
for aid, fname, atype, required in USER_ASSETS:
    p = ASSETS / fname
    exists = p.exists()
    if required and not exists:
        missing.append(str(p))
    user_list.append({
        "id": aid, "path": f"./assets/{fname}", "type": atype,
        "exists": exists, "deterministic": True, "required": required,
    })

gen_list = []
for p in sorted(GEN.glob("*.png")):
    wave, skill = gen_meta(p.name)
    exists = p.exists() and p.stat().st_size > 10000
    if not exists:
        missing.append(str(p))
    gen_list.append({
        "id": p.stem, "path": f"./generated/{p.name}",
        "exists": exists, "deterministic": False,
        "source": "generated", "wave": wave, "skill": skill,
        "model": "gemini-3-pro-image-preview",
    })

manifest = {
    "brand": "thoughtseed",
    "generated_at": "2026-06-08T06:10:00Z",
    "user_provided_assets": user_list,
    "generated_assets": gen_list,
    "validation": {
        "all_paths_exist": len(missing) == 0,
        "missing_paths": missing,
        "user_count": len(user_list),
        "generated_count": len(gen_list),
    },
}
out = BRAND / ".brandmint" / "asset-manifest.json"
out.write_text(json.dumps(manifest, indent=2))
print(f"manifest written: {out}")
print(f"user={len(user_list)} generated={len(gen_list)} all_paths_exist={len(missing)==0} missing={missing}")
