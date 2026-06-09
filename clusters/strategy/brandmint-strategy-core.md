---
name: brandmint-strategy-core
description: "Shared reference for the strategy cluster: voice-and-tone calibration, CBBE framework for positioning, messaging hierarchy rules, and brand story structure."
cluster: brandmint-strategy
wave: 2
version: 1.0.0
---

# Brandmint Strategy Core

Shared reference for all strategy spokes. Wave 2 transforms the foundation outputs into actionable brand strategy.

## The One Rule Everything Turns On

**Strategy must be actionable.** Every output must answer: "What do I DO with this?"

- Voice-and-tone → "How do I write?"
- Product positioning → "How do I describe us?"
- Messaging framework → "What do I say to whom?"
- Brand story → "How do I connect emotionally?"

## Inputs from Wave 1

Strategy spokes receive these outputs from foundation:

| Input | From Spoke | Used By |
|-------|------------|---------|
| `buyer_persona.json` | buyer-persona | voice-and-tone, messaging |
| `brand_foundation.json` | brand-foundation | all strategy spokes |
| `competitor_analysis.json` | competitor-analysis | product-positioning |
| `value_proposition.json` | value-proposition | messaging, brand-story |

## CBBE Framework (Customer-Based Brand Equity)

All positioning work uses Keller's CBBE pyramid:

```
         ┌─────────────┐
         │  RESONANCE  │  ← Loyalty, attachment, community
         ├─────────────┤
    ┌────┴─────┬───────┴────┐
    │ JUDGMENT │  FEELINGS  │  ← Quality, credibility, emotion
    ├──────────┴────────────┤
    │      PERFORMANCE      │  ← Functional benefits
    │        IMAGERY        │  ← Psychological benefits
    ├───────────────────────┤
    │       SALIENCE        │  ← Awareness, recognition
    └───────────────────────┘
```

**product-positioning** must address all levels.

## Voice Calibration Matrix

Voice-and-tone outputs a calibrated matrix:

| Dimension | Range | Description |
|-----------|-------|-------------|
| Formality | 0-1 | Casual ↔ Formal |
| Enthusiasm | 0-1 | Reserved ↔ Energetic |
| Technicality | 0-1 | Simple ↔ Technical |
| Warmth | 0-1 | Professional ↔ Friendly |
| Authority | 0-1 | Peer ↔ Expert |

**Context modifiers:**
- Homepage: +0.1 warmth, +0.1 enthusiasm
- Legal/Compliance: +0.3 formality, -0.2 warmth
- Support: +0.2 warmth, -0.1 formality
- Sales: +0.1 enthusiasm, +0.1 authority

## Messaging Hierarchy

```
┌──────────────────────────────────────────┐
│           BRAND PROMISE                  │  ← One sentence, universal
├──────────────────────────────────────────┤
│           VALUE PROPOSITION              │  ← For target audience
├──────────────────────────────────────────┤
│  KEY MESSAGE 1  │  KEY MESSAGE 2  │ ...  │  ← 3-5 pillars
├─────────────────┴─────────────────┴──────┤
│     PROOF POINTS / SUPPORTING CLAIMS     │  ← Evidence for each pillar
└──────────────────────────────────────────┘
```

## Brand Story Structure

StoryBrand framework (Donald Miller):

1. **Character** — The customer (not the brand)
2. **Problem** — External, internal, and philosophical
3. **Guide** — The brand (with empathy + authority)
4. **Plan** — Simple 3-step process
5. **Call to Action** — Direct + transitional
6. **Success** — What winning looks like
7. **Failure** — Stakes if they don't act

## Output Schemas

### voice-and-tone.json

```json
{
  "skill": "voice-and-tone",
  "cluster": "strategy",
  "wave": 2,
  "data": {
    "voice_matrix": {
      "formality": 0.6,
      "enthusiasm": 0.7,
      "technicality": 0.5,
      "warmth": 0.6,
      "authority": 0.7
    },
    "context_modifiers": { ... },
    "do_list": ["Use active voice", "Start with benefits"],
    "dont_list": ["Don't use jargon without explanation"],
    "example_phrases": {
      "instead_of": "Leverage our solution",
      "use": "Use our platform to..."
    },
    "tone_words": ["confident", "helpful", "clear"]
  }
}
```

### product-positioning.json

```json
{
  "skill": "product-positioning",
  "cluster": "strategy",
  "wave": 2,
  "data": {
    "positioning_statement": "For [target] who [need], [brand] is the [category] that [key benefit] because [reason to believe].",
    "cbbe_levels": {
      "salience": { ... },
      "performance": { ... },
      "imagery": { ... },
      "judgments": { ... },
      "feelings": { ... },
      "resonance": { ... }
    },
    "competitive_frame": "category-leader | challenger | niche-specialist",
    "points_of_parity": [...],
    "points_of_difference": [...]
  }
}
```

### messaging-framework.json

```json
{
  "skill": "messaging-framework",
  "cluster": "strategy",
  "wave": 2,
  "data": {
    "brand_promise": "...",
    "value_proposition": "...",
    "key_messages": [
      {
        "pillar": "Efficiency",
        "headline": "Save 10 hours per week",
        "proof_points": [...]
      }
    ],
    "audience_variants": {
      "technical_buyer": { ... },
      "economic_buyer": { ... }
    },
    "elevator_pitches": {
      "10_second": "...",
      "30_second": "...",
      "60_second": "..."
    }
  }
}
```

### brand-story.json

```json
{
  "skill": "brand-story",
  "cluster": "strategy",
  "wave": 2,
  "data": {
    "storybrand_framework": {
      "character": { ... },
      "problem": {
        "external": "...",
        "internal": "...",
        "philosophical": "..."
      },
      "guide": { ... },
      "plan": { ... },
      "call_to_action": { ... },
      "success": { ... },
      "failure": { ... }
    },
    "origin_story": "...",
    "founder_narrative": "...",
    "customer_transformation": "..."
  }
}
```

## Quality Gates

| Check | Requirement |
|-------|-------------|
| Voice matrix complete | All 5 dimensions scored |
| Positioning uses CBBE | All 6 levels addressed |
| Messaging has proof | Every pillar has evidence |
| Story has stakes | Failure state defined |

## Cross-Spoke Dependencies

```
brand-foundation ──┬──▶ voice-and-tone
                   │
buyer-persona ─────┼──▶ messaging-framework
                   │
value-proposition ─┼──▶ product-positioning
                   │
competitor-analysis┴──▶ brand-story
```

## Downstream Consumers

| Consumer (Wave) | Uses |
|-----------------|------|
| visual-language (3) | Voice matrix for visual tone |
| landing-page-copy (6) | Messaging framework |
| email-sequences (6) | Voice-and-tone + messaging |
| brand-documentation (7) | All strategy outputs |
