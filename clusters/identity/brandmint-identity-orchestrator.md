---
name: brandmint-identity-orchestrator
description: "Route visual identity tasks to the right spoke — logo concept, color palette, typography, visual language. USE WHEN defining brand visuals, creating identity systems, or specifying design direction."
cluster: brandmint-identity
wave: 3
version: 1.0.0
---

# Brandmint Identity Orchestrator

The entry skill for Wave 3: Visual Identity. Routes identity design intents to the appropriate spoke.

## Prerequisites

Waves 1-2 must be complete:
- Wave 1: Foundation (brand-foundation, buyer-persona, value-proposition)
- Wave 2: Strategy (voice-and-tone, product-positioning)

## Cluster Map (Routing Targets)

- `brandmint-identity-core` — shared reference: design principles, output specs, quality gates
- `logo-concept` — logo direction, symbolism, style references (text prompt for GPT-Image-2)
- `color-palette` — primary, secondary, accent colors with hex codes and usage rules
- `typography` — typeface selection, hierarchy, pairing rationale
- `visual-language` — photography style, illustration style, iconography direction

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "logo", "brand mark", "symbol" | `logo-concept` |
| "colors", "palette", "brand colors" | `color-palette` |
| "fonts", "typography", "typefaces" | `typography` |
| "visual style", "photography style", "imagery" | `visual-language` |
| "full identity" | Run all spokes in order |

## Execution Order

Identity spokes should run sequentially:

1. `color-palette` — establishes emotional foundation
2. `typography` — establishes voice in type
3. `logo-concept` — synthesizes color and type direction
4. `visual-language` — extends to photography/illustration

## Visual Generation

This cluster produces **prompts** for the visual pipeline, not images directly.

Each spoke outputs a `generation_prompt` field that feeds into:
- `gpt-image-2` for logo concepts and visual explorations
- Photography spokes use the visual language output

## Quality Gates

From `brandmint-identity-core`:
- Color palette must include accessibility contrast ratios
- Typography must specify web-safe fallbacks
- Logo concept must include 3+ style directions
- Visual language must reference real brand examples

## Loading Spokes On Demand

Spokes are not enumerated at startup. Load by reading:

`clusters/identity/spokes/<spoke-name>.md`
