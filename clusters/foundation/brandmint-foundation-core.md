---
name: brandmint-foundation-core
description: "Shared reference for the brandmint-foundation cluster: output schemas, dependency graph, quality gates, and the CBBE framework that governs buyer persona creation."
cluster: brandmint-foundation
wave: 1
version: 1.0.0
---

# Brandmint Foundation Core

Shared rules and conventions for all foundation spokes. Read this before implementing any foundation skill.

## Output Schema Contract

All foundation outputs must be valid JSON with this base structure:

```json
{
    "skill": "<spoke-name>",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "ISO 8601",
    "status": "complete|partial",
    "version": "1.0.0",
    "data": { /* skill-specific */ }
}
```

## Dependency Graph

```
brand-foundation
       │
       ├──► buyer-persona
       │
       ├──► competitor-analysis
       │
       └───────────┬───────────┘
                   │
                   ▼
           value-proposition
```

## Quality Gates

### brand-foundation
- Must include: mission, vision, values (3+), brand essence
- Mission must be one sentence
- Values must be actionable (not generic like "quality")

### buyer-persona
- Must follow CBBE framework sections:
  - Salience (who are you?)
  - Performance (what are you?)
  - Imagery (brand associations)
  - Judgments (credibility)
  - Feelings (emotional connection)
  - Resonance (loyalty drivers)
- Must include emotional drivers (positive AND negative)
- Demographics must be specific, not ranges

### competitor-analysis
- Minimum 2 competitors
- Each competitor must include: name, positioning, strengths, weaknesses
- Must identify positioning gaps (whitespace opportunities)

### value-proposition
- Must reference buyer persona pain points by name
- Must differentiate from competitors explicitly
- Must be one clear sentence (not a paragraph)

## CBBE Framework Reference

The Consumer-Based Brand Equity (CBBE) framework structures how we understand brand-customer relationships:

| Level | Consumer Question | What We Define |
|-------|------------------|----------------|
| Salience | "Who are you?" | Product category, problem solved |
| Performance | "What are you?" | Points of parity, points of difference |
| Imagery | "What do I associate with you?" | Brand personality, user imagery |
| Judgments | "How good are you?" | Quality, credibility, consideration |
| Feelings | "How do you make me feel?" | Emotional outcomes sought |
| Resonance | "What about you and me?" | Loyalty, attachment, community |

## Upstream/Downstream Contracts

### This cluster provides (downstream):
- Brand context for all subsequent waves
- Buyer persona for messaging/voice
- Competitive positioning for visual differentiation
- Value proposition for all marketing copy

### This cluster requires (upstream):
- `brand-config.yaml` with:
  - `name`: Brand name
  - `product.description`: What is being sold
  - `product.category`: Market category
  - `product.price`: Price point (affects positioning)

## Guardrails

1. **No generic personas** — "25-45 year old professional" is not a persona
2. **No feature lists** — value proposition is about outcomes, not features
3. **No empty values** — "integrity" without definition is meaningless
4. **No copied competitors** — analysis must be original research
5. **Evidence over claims** — back assertions with reasoning
