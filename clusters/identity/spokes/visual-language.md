---
name: visual-language
description: "Define the overall visual style — photography direction, illustration style, iconography, patterns, and visual principles that create brand consistency."
cluster: brandmint-identity
wave: 3
dependencies:
  - brand-foundation
  - color-palette
  - typography
  - logo-concept
triggers:
  - "visual language"
  - "visual style"
  - "photography style"
  - "illustration style"
  - "visual guidelines"
---

# Visual Language Skill

Define the comprehensive visual style system that ensures brand consistency across all touchpoints.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for brand personality
- `color-palette.json` — for color system
- `typography.json` — for type system
- `logo-concept.json` — for logo style direction

## Process

### Step 1: Visual Principles

Define 3-5 core principles that guide all visual decisions:

**Example principles:**
- **Bold simplicity** — Every element earns its place
- **Warm authenticity** — Real moments, not staged perfection
- **Dynamic balance** — Energetic but not chaotic

### Step 2: Photography Direction

**Style definition:**

| Dimension | Direction |
|-----------|-----------|
| **Lighting** | Natural/Studio, Soft/Hard, Warm/Cool |
| **Composition** | Centered/Rule-of-thirds, Minimal/Layered |
| **Color treatment** | Saturated/Desaturated, Warm/Cool cast |
| **Subject focus** | People/Product/Environment, Close/Wide |
| **Mood** | Aspirational/Relatable, Dynamic/Calm |
| **Context** | Lifestyle/Studio, Indoor/Outdoor |

**Reference images:**
- 3-5 example images that represent the direction
- Note what works about each

**GPT-Image-2 prompt template for photography:**
```
[Scene description] in a [style] photography style.
Lighting: [natural/studio], [soft/hard], [warm/cool].
Mood: [aspirational/authentic], [energetic/calm].
Color palette: [describe colors].
Shot composition: [close-up/wide], [rule of thirds/centered].
High quality, professional photography.
```

### Step 3: Illustration Style

**Style definition:**

| Dimension | Direction |
|-----------|-----------|
| **Style** | Flat/Dimensional, Line/Filled, Realistic/Abstract |
| **Complexity** | Simple/Detailed |
| **Line weight** | Thin/Thick, Uniform/Variable |
| **Color approach** | Duotone/Full color, Brand colors only |
| **Character style** | If people: geometric/organic, detailed/simplified |

**GPT-Image-2 prompt template for illustration:**
```
[Subject description] in a [flat/dimensional] illustration style.
Line work: [thin/thick], [uniform/variable].
Colors: [brand colors: list hex codes].
Style: [geometric/organic], [simple/detailed].
Background: [transparent/solid color].
Vector-style illustration, clean edges.
```

### Step 4: Iconography

**Icon style definition:**
- **Style:** Line/Filled/Duotone
- **Stroke weight:** [X]px
- **Corner radius:** Sharp/Rounded ([X]px)
- **Grid:** [X]px base grid
- **Optical adjustments:** Yes/No

**Icon categories needed:**
- UI icons (navigation, actions)
- Feature icons (product capabilities)
- Category icons (sections, topics)

### Step 5: Patterns & Textures

**Pattern style:**
- **Type:** Geometric/Organic/Abstract
- **Scale:** Small/Medium/Large
- **Usage:** Backgrounds, accents, dividers
- **Colors:** From brand palette only

**GPT-Image-2 prompt for patterns:**
```
Seamless repeating pattern featuring [elements].
Style: [geometric/organic], [minimal/complex].
Colors: [primary] and [secondary] only on [background].
Suitable for background use, tileable pattern.
```

### Step 6: Visual Do's and Don'ts

Document clear guidelines:

**Do:**
- [Specific guidance]
- [Specific guidance]

**Don't:**
- [Specific anti-pattern]
- [Specific anti-pattern]

## Output Schema

```json
{
    "skill": "visual-language",
    "cluster": "identity",
    "wave": 3,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "visual_principles": [
            {
                "name": "string",
                "description": "string"
            }
        ],
        "photography": {
            "style": {
                "lighting": "string",
                "composition": "string",
                "color_treatment": "string",
                "subject_focus": "string",
                "mood": "string",
                "context": "string"
            },
            "references": ["string (descriptions)"],
            "prompt_template": "string"
        },
        "illustration": {
            "style": {
                "type": "string",
                "complexity": "string",
                "line_weight": "string",
                "color_approach": "string",
                "character_style": "string"
            },
            "prompt_template": "string"
        },
        "iconography": {
            "style": "string (line/filled/duotone)",
            "stroke_weight": "string",
            "corner_radius": "string",
            "grid_size": "string",
            "categories": ["string"]
        },
        "patterns": {
            "type": "string",
            "scale": "string",
            "usage": ["string"],
            "prompt_template": "string"
        },
        "guidelines": {
            "do": ["string"],
            "dont": ["string"]
        }
    }
}
```

## Quality Checklist

- [ ] 3-5 visual principles defined
- [ ] Photography style fully specified
- [ ] Illustration style fully specified
- [ ] Iconography specifications complete
- [ ] Pattern style defined
- [ ] All styles align with brand personality
- [ ] GPT-Image-2 prompt templates provided
- [ ] Do's and Don'ts documented
