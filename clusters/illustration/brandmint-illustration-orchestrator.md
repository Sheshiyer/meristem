---
name: brandmint-illustration-orchestrator
description: "Route illustration generation tasks to the right spoke — brand illustrations, icon system, pattern library. Uses GPT-Image-2 for all illustration generation."
cluster: brandmint-illustration
wave: 5
version: 1.0.0
---

# Brandmint Illustration Orchestrator

The entry skill for Wave 5: Illustration. Routes illustration generation intents to the appropriate spoke.

## Prerequisites

Waves 3-4 must be complete:
- `color-palette.json` — for color direction
- `visual-language.json` — for illustration style guidelines
- Photography complete (establishes visual canon)

## Cluster Map (Routing Targets)

- `brandmint-illustration-core` — shared reference: style consistency, export formats, quality gates
- `brand-illustrations` — hero illustrations, spot illustrations, mascots
- `icon-system` — product icons, UI icons, feature icons
- `pattern-library` — repeatable patterns, textures, backgrounds

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "illustrations", "hero illustration", "spot art" | `brand-illustrations` |
| "icons", "icon set", "feature icons" | `icon-system` |
| "patterns", "textures", "backgrounds" | `pattern-library` |
| "full illustration suite" | Run all spokes in order |

## Execution Order

Illustration spokes should run sequentially for style consistency:

1. `brand-illustrations` — establishes illustration style canon
2. `icon-system` — applies style to iconography
3. `pattern-library` — creates supporting visual textures

## Visual Generation Pipeline

All illustration spokes produce prompts that feed into GPT-Image-2:

```bash
# From within a spoke:
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/hero-illustration.txt)" \
    --out "$brand_dir/generated/illustration-hero.png" \
    --aspect 16:9
```

## Style Consistency

Illustrations must maintain consistency with:
- Color palette (primary/secondary colors only)
- Visual language style direction
- Typography personality (geometric = geometric illustrations, etc.)

## Quality Gates

From `brandmint-illustration-core`:
- All illustrations must use brand color palette exclusively
- Icons must be provided at 24px, 48px, 96px sizes
- Patterns must tile seamlessly
- Style must match visual-language illustration direction

## Loading Spokes On Demand

Spokes are not enumerated at startup. Load by reading:

`clusters/illustration/spokes/<spoke-name>.md`
