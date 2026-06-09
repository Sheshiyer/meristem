---
name: brandmint-photography-orchestrator
description: "Route photography generation tasks to the right spoke — lifestyle shots, product photography, hero images. Uses GPT-Image-2 for all image generation."
cluster: brandmint-photography
wave: 4
version: 1.0.0
---

# Brandmint Photography Orchestrator

The entry skill for Wave 4: Photography. Routes photography generation intents to the appropriate spoke.

## Prerequisites

Wave 3 (Identity) must be complete:
- `color-palette.json` — for color direction
- `visual-language.json` — for photography style guidelines

## Cluster Map (Routing Targets)

- `brandmint-photography-core` — shared reference: prompt engineering, aspect ratios, quality gates
- `lifestyle-photography` — people using the product in context
- `product-photography` — clean product shots, detail shots, angles
- `hero-images` — dramatic, campaign-ready key visuals
- `social-media-assets` — platform-specific sized assets

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "lifestyle", "people", "in use", "context shots" | `lifestyle-photography` |
| "product shots", "pack shots", "detail shots" | `product-photography` |
| "hero image", "key visual", "campaign image" | `hero-images` |
| "social media", "Instagram", "Facebook assets" | `social-media-assets` |
| "full photography suite" | Run all spokes in order |

## Execution Order

Photography spokes are largely parallelizable:

```
                    ┌─► lifestyle-photography
                    │
visual-language ────┼─► product-photography
                    │
                    ├─► hero-images
                    │
                    └─► social-media-assets
```

Recommended order for coherence:
1. `product-photography` — establishes product visual canon
2. `lifestyle-photography` — shows product in context
3. `hero-images` — dramatic synthesis
4. `social-media-assets` — derived from above

## Visual Generation Pipeline

All photography spokes produce prompts that feed into GPT-Image-2:

```bash
# From within a spoke:
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/lifestyle-shot-1.txt)" \
    --out "$brand_dir/generated/lifestyle-1.png" \
    --aspect 16:9
```

## Quality Gates

From `brandmint-photography-core`:
- All prompts must reference visual-language style
- Hero images must be 16:9 or 3:2 aspect ratio
- Product shots must include white background variant
- Lifestyle shots must show target persona demographic

## Loading Spokes On Demand

Spokes are not enumerated at startup. Load by reading:

`clusters/photography/spokes/<spoke-name>.md`
