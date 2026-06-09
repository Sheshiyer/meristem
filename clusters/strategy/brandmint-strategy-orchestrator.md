---
name: brandmint-strategy-orchestrator
description: "Route strategy tasks to the right spoke — voice-and-tone, product-positioning, messaging-framework, brand-story. USE WHEN defining brand voice, crafting positioning, creating messaging hierarchies, or writing brand narratives."
cluster: brandmint-strategy
wave: 2
version: 1.0.0
---

# Brandmint Strategy Orchestrator

The entry skill for Wave 2: Strategy. Routes brand strategy intents to the appropriate spoke.

## Prerequisites

Wave 1 (Foundation) must be complete:
- `brand-foundation.json`
- `buyer-persona.json`
- `competitor-analysis.json`
- `value-proposition.json`

## Cluster Map (Routing Targets)

- `brandmint-strategy-core` — shared reference: voice guidelines, positioning frameworks, output schemas
- `voice-and-tone` — brand voice definition, tone variations by context
- `product-positioning` — CBBE-based positioning summary using the framework from buyer persona
- `messaging-framework` — hierarchical messaging: tagline, elevator pitch, value pillars
- `brand-story` — narrative arc: origin, mission, vision, customer transformation

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "voice", "tone", "how we speak" | `voice-and-tone` |
| "positioning", "market position", "how we're different" | `product-positioning` |
| "messaging", "tagline", "value pillars", "elevator pitch" | `messaging-framework` |
| "brand story", "narrative", "origin story", "why we exist" | `brand-story` |
| "full strategy" | Run all spokes in order |

## Execution Order

Strategy spokes have dependencies:

1. `voice-and-tone` — depends on buyer-persona (voice reflects audience)
2. `product-positioning` — depends on buyer-persona, competitor-analysis
3. `messaging-framework` — depends on voice-and-tone, product-positioning
4. `brand-story` — depends on all above (narrative synthesis)

## Quality Gates

From `brandmint-strategy-core`:
- Voice must include context variations (formal, casual, crisis)
- Positioning must reference CBBE framework sections
- Messaging must have 3-5 value pillars
- Brand story must follow narrative arc structure

## Loading Spokes On Demand

Spokes are not enumerated at startup. Load by reading:

`clusters/strategy/spokes/<spoke-name>.md`
