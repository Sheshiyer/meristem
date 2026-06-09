---
name: brandmint-foundation-orchestrator
description: "Route foundation tasks to the right spoke — brand-foundation, buyer-persona, competitor-analysis, value-proposition. USE WHEN starting a new brand, defining target audience, analyzing competition, or establishing core brand identity."
cluster: brandmint-foundation
wave: 1
version: 1.0.0
---

# Brandmint Foundation Orchestrator

The entry skill for Wave 1: Foundation. Routes brand-building intents to the appropriate spoke based on what aspect of the foundation is being developed.

## Cluster Map (Routing Targets)

- `brandmint-foundation-core` — shared reference: output schemas, dependency rules, quality gates, upstream/downstream contracts
- `brand-foundation` — core brand identity: mission, vision, values, brand essence
- `buyer-persona` — detailed buyer persona profiles using CBBE framework
- `competitor-analysis` — competitive landscape analysis and positioning gaps
- `value-proposition` — unique value proposition and differentiation

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "define the brand", "brand identity", "mission vision values" | `brand-foundation` |
| "who is the customer", "buyer persona", "target audience" | `buyer-persona` |
| "competition", "competitive analysis", "market landscape" | `competitor-analysis` |
| "value proposition", "why us", "differentiation" | `value-proposition` |
| "start from scratch", "new brand" | Run all spokes in order |

## Execution Order

Foundation spokes have dependencies:

1. `brand-foundation` — no dependencies (can run first)
2. `buyer-persona` — depends on `brand-foundation` (needs brand context)
3. `competitor-analysis` — depends on `brand-foundation` (needs product category)
4. `value-proposition` — depends on all above (synthesis)

## Standard Operating Flow

1. Classify the task into one or more spokes
2. Check dependencies are satisfied (upstream outputs exist)
3. Load `brandmint-foundation-core` for shared rules
4. Delegate to spoke(s) in dependency order
5. Validate outputs against schema
6. Return summary with next-wave readiness

## Quality Gates

From `brandmint-foundation-core`:
- All outputs must be valid JSON with required schema fields
- Buyer persona must include emotional drivers
- Competitor analysis must include at least 2 competitors
- Value proposition must reference buyer persona pain points

## Loading Spokes On Demand

Spokes are not enumerated at startup. Load by reading:

`clusters/foundation/spokes/<spoke-name>.md`
