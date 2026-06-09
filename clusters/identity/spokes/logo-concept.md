---
name: logo-concept
description: "Define logo direction, symbolism, style references, and generate image prompts for GPT-Image-2. Creates multiple concept directions for exploration."
cluster: brandmint-identity
wave: 3
dependencies:
  - brand-foundation
  - color-palette
  - typography
triggers:
  - "logo"
  - "logo concept"
  - "brand mark"
  - "symbol"
---

# Logo Concept Skill

Define logo direction and generate prompts for visual exploration with GPT-Image-2.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for brand essence, values, personality
- `color-palette.json` — for color direction
- `typography.json` — for type style direction

## Process

### Step 1: Logo Type Selection

**Choose the primary logo format:**

| Type | Description | Best For |
|------|-------------|----------|
| **Wordmark** | Brand name in styled type | Simple names, strong typography |
| **Lettermark** | Initials or acronym | Long names, tech brands |
| **Pictorial** | Recognizable image/icon | Universal recognition |
| **Abstract** | Geometric/abstract shape | Unique differentiation |
| **Mascot** | Character illustration | Friendly, approachable brands |
| **Emblem** | Text inside symbol/badge | Traditional, prestigious |
| **Combination** | Symbol + wordmark | Flexibility across uses |

### Step 2: Symbolism Exploration

**What should the logo represent?**

Map brand attributes to visual concepts:

| Brand Attribute | Visual Concept | Symbol Ideas |
|-----------------|----------------|--------------|
| [attribute 1] | [concept] | [symbols] |
| [attribute 2] | [concept] | [symbols] |
| [attribute 3] | [concept] | [symbols] |

**Questions:**
- What object/shape embodies the brand essence?
- What metaphor captures the value proposition?
- What would make this instantly recognizable?

### Step 3: Style Direction

**Define the visual style:**

| Dimension | Spectrum | Selection |
|-----------|----------|-----------|
| Complexity | Simple ←→ Detailed | |
| Weight | Light ←→ Heavy | |
| Shape | Organic ←→ Geometric | |
| Style | Classic ←→ Modern | |
| Mood | Serious ←→ Playful | |

### Step 4: Reference Brands

Identify 3-5 logos that represent the desired direction:
- Not to copy, but to establish visual territory
- Note what works about each reference
- Identify the gap/opportunity

### Step 5: Generate Concept Directions (3-5)

For each direction, create:

**Direction Name:** [e.g., "Geometric Shield"]
**Concept:** [What it represents]
**Style notes:** [Visual characteristics]
**GPT-Image-2 Prompt:**

```
Create a minimalist logo design for [brand name], a [category] brand.

The logo should feature [symbol/concept description].

Style: [geometric/organic], [modern/classic], [simple/detailed]
Colors: [primary color] on white background
Typography: [if wordmark, describe style]

The design should convey [key attributes: trust, energy, innovation, etc.]

Professional logo design, vector-style, clean lines, scalable.
```

### Step 6: Usage Specifications

Define how the logo should be used:
- Minimum size
- Clear space requirements
- Color variations (full color, mono, reversed)
- What NOT to do

## Output Schema

```json
{
    "skill": "logo-concept",
    "cluster": "identity",
    "wave": 3,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "logo_type": {
            "primary": "string (wordmark, lettermark, etc.)",
            "rationale": "string"
        },
        "symbolism": {
            "brand_attributes": ["string"],
            "visual_concepts": ["string"],
            "symbol_ideas": ["string"]
        },
        "style_direction": {
            "complexity": "string (simple to detailed)",
            "weight": "string (light to heavy)",
            "shape": "string (organic to geometric)",
            "style": "string (classic to modern)",
            "mood": "string (serious to playful)"
        },
        "references": [
            {
                "brand": "string",
                "what_works": "string",
                "gap_opportunity": "string"
            }
        ],
        "concept_directions": [
            {
                "name": "string",
                "concept": "string",
                "style_notes": "string",
                "generation_prompt": "string (full GPT-Image-2 prompt)"
            }
        ],
        "usage_specs": {
            "minimum_size": "string (e.g., 24px height)",
            "clear_space": "string (e.g., 1x height on all sides)",
            "color_variations": ["full_color", "monochrome", "reversed"],
            "dont_do": ["string"]
        }
    }
}
```

## Quality Checklist

- [ ] Logo type selected with clear rationale
- [ ] Symbolism connects to brand attributes
- [ ] Style direction defined across all dimensions
- [ ] 3-5 reference logos analyzed
- [ ] 3-5 concept directions with full prompts
- [ ] Prompts are specific and actionable for GPT-Image-2
- [ ] Usage specifications defined
