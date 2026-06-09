---
name: brandmint-identity-core
description: "Shared reference for the identity cluster: logo concept principles, color theory, typography pairing rules, and visual language system."
cluster: brandmint-identity
wave: 3
version: 1.0.0
---

# Brandmint Identity Core

Shared reference for all identity spokes. Wave 3 creates the visual identity system.

## The One Rule Everything Turns On

**Visual identity must be systematized.** Every element must have:
- Rationale (why this choice?)
- Rules (how to use it)
- Restrictions (what NOT to do)

## Visual Generation Constraint

**Images only via GPT-Image-2.** No FAL, no Replicate, no Midjourney.

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$prompt" \
    --out "$brand_dir/generated/$filename"
```

## Inputs from Prior Waves

| Input | From | Used By |
|-------|------|---------|
| `brand_foundation.json` | W1 | All identity spokes |
| `voice_and_tone.json` | W2 | visual-language |
| `product_positioning.json` | W2 | logo-concept |
| Visual preferences | config | color-palette, typography |

## Logo Concept Principles

### Logo Types

| Type | Best For | Example |
|------|----------|---------|
| Wordmark | Name is distinctive | Google, Coca-Cola |
| Lettermark | Long company name | IBM, HBO |
| Symbol | Universal recognition needed | Apple, Nike |
| Combination | New brand, flexibility | Adidas, Burger King |
| Emblem | Heritage, authority | Harley-Davidson |

### Logo Attributes to Define

```json
{
  "logo_type": "combination",
  "symbol_concept": "Abstract representation of flow/efficiency",
  "typography_style": "Geometric sans-serif",
  "color_usage": "Primary blue, accent on symbol only",
  "minimum_size": "32px height",
  "clear_space": "Height of 'x' character around all sides",
  "variations": ["full", "stacked", "symbol-only", "wordmark-only"]
}
```

## Color Theory Framework

### Color Psychology

| Color Family | Associations | Industries |
|--------------|--------------|------------|
| Blue | Trust, stability, tech | Finance, Tech, Healthcare |
| Green | Growth, nature, health | Wellness, Finance, Eco |
| Red | Energy, urgency, passion | Food, Entertainment, Sales |
| Orange | Friendly, creative, affordable | Retail, Creative, Youth |
| Purple | Luxury, creativity, wisdom | Beauty, Education, Luxury |
| Yellow | Optimism, warmth, attention | Food, Children, Caution |
| Black | Sophistication, luxury | Fashion, Luxury, Tech |

### Color System Structure

```
┌─────────────────────────────────────────┐
│           PRIMARY COLOR                 │  ← Brand recognition
├─────────────────────────────────────────┤
│  SECONDARY 1  │  SECONDARY 2 (optional) │  ← Support, variety
├───────────────┴─────────────────────────┤
│              ACCENT COLOR               │  ← CTAs, highlights
├─────────────────────────────────────────┤
│  NEUTRAL DARK  │  NEUTRAL LIGHT         │  ← Text, backgrounds
└─────────────────────────────────────────┘
```

### Accessibility Requirements

| Contrast Ratio | Use Case |
|----------------|----------|
| 4.5:1 minimum | Normal text |
| 3:1 minimum | Large text (18px+) |
| 3:1 minimum | UI components |

## Typography Pairing Rules

### Type Scale (Major Third — 1.25)

```
Display:    48px  (3rem)
H1:         38px  (2.4rem)
H2:         30px  (1.9rem)
H3:         24px  (1.5rem)
H4:         19px  (1.2rem)
Body:       16px  (1rem)
Small:      13px  (0.8rem)
Caption:    10px  (0.64rem)
```

### Pairing Strategies

| Strategy | Example | Best For |
|----------|---------|----------|
| Serif + Sans | Playfair + Open Sans | Editorial, Luxury |
| Sans + Sans | Montserrat + Source Sans | Tech, Modern |
| Slab + Sans | Roboto Slab + Roboto | Bold, Industrial |
| Display + Body | Bebas + Lato | Creative, Bold |

### Font Categories

- **Display/Headlines**: Character, distinctiveness
- **Body**: Readability at small sizes
- **UI/Monospace**: Interfaces, code

## Visual Language System

### Photography Direction

```json
{
  "style": "authentic | polished | editorial | lifestyle",
  "subjects": ["people", "product", "abstract", "environment"],
  "color_treatment": "natural | branded-tint | high-contrast",
  "composition": "rule-of-thirds | centered | asymmetric",
  "lighting": "natural | studio | dramatic"
}
```

### Illustration Direction

```json
{
  "style": "flat | 3d | line-art | hand-drawn | geometric",
  "complexity": "minimal | moderate | detailed",
  "color_usage": "monochrome | limited-palette | full-color",
  "stroke_weight": "thin | medium | bold",
  "animation_ready": true
}
```

### Iconography Rules

- **Style consistency**: All icons same weight/style
- **Grid**: 24x24 base, scale to 16, 32, 48
- **Stroke**: 2px standard, 1.5px small
- **Corners**: Consistent radius (2px or rounded)

## Output Schemas

### logo-concept.json

```json
{
  "skill": "logo-concept",
  "cluster": "identity",
  "wave": 3,
  "data": {
    "concepts": [
      {
        "id": "concept-1",
        "name": "Flow Mark",
        "type": "combination",
        "rationale": "...",
        "symbol_description": "...",
        "typography": "...",
        "generated_path": "./generated/logo-concept-1.png"
      }
    ],
    "selected": "concept-1",
    "usage_rules": { ... },
    "dont_rules": [ ... ]
  }
}
```

### color-palette.json

```json
{
  "skill": "color-palette",
  "cluster": "identity",
  "wave": 3,
  "data": {
    "primary": {
      "name": "Brand Blue",
      "hex": "#2563EB",
      "rgb": [37, 99, 235],
      "hsl": [217, 82, 53],
      "usage": "Primary brand color, headers, key CTAs"
    },
    "secondary": [ ... ],
    "accent": { ... },
    "neutrals": {
      "dark": { ... },
      "light": { ... }
    },
    "semantic": {
      "success": "#10B981",
      "warning": "#F59E0B",
      "error": "#EF4444",
      "info": "#3B82F6"
    },
    "accessibility": {
      "contrast_checks": [ ... ]
    }
  }
}
```

### typography.json

```json
{
  "skill": "typography",
  "cluster": "identity",
  "wave": 3,
  "data": {
    "display": {
      "family": "Inter",
      "weight": "700",
      "fallback": "system-ui, sans-serif",
      "source": "Google Fonts"
    },
    "body": {
      "family": "Inter",
      "weight": "400",
      "fallback": "system-ui, sans-serif"
    },
    "scale": { ... },
    "line_heights": {
      "tight": 1.25,
      "normal": 1.5,
      "relaxed": 1.75
    },
    "letter_spacing": {
      "headlines": "-0.02em",
      "body": "0"
    }
  }
}
```

### visual-language.json

```json
{
  "skill": "visual-language",
  "cluster": "identity",
  "wave": 3,
  "data": {
    "photography_direction": { ... },
    "illustration_direction": { ... },
    "iconography": { ... },
    "patterns_textures": { ... },
    "motion_principles": {
      "easing": "ease-out",
      "duration_scale": "fast | normal | slow"
    },
    "spacing_system": {
      "base": 8,
      "scale": [4, 8, 12, 16, 24, 32, 48, 64, 96]
    }
  }
}
```

## Quality Gates

| Check | Requirement |
|-------|-------------|
| Logo concepts | Min 2 options generated |
| Color accessibility | All pairs meet WCAG AA |
| Typography | Display + Body defined |
| Visual language | Photo + Illustration direction set |

## Generated Assets (Wave 3)

| Asset | Spoke | Path Pattern |
|-------|-------|--------------|
| Logo concepts | logo-concept | `generated/logo-concept-*.png` |
| Color swatches | color-palette | `generated/color-swatches.png` |
| Type specimens | typography | `generated/type-specimen.png` |
| Moodboard | visual-language | `generated/moodboard.png` |

All paths must be validated before Wave 7 synthesis.
