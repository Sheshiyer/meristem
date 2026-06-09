---
name: typography
description: "Select and configure brand typography — primary and secondary typefaces, type scale, hierarchy, and web font implementation."
cluster: brandmint-identity
wave: 3
dependencies:
  - brand-foundation
  - color-palette
triggers:
  - "typography"
  - "fonts"
  - "typefaces"
  - "type scale"
---

# Typography Skill

Define the brand typography system with typeface selection, hierarchy, and implementation guidelines.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for brand personality
- `color-palette.json` — for text colors

## Process

### Step 1: Personality-to-Type Mapping

Map brand attributes to typeface characteristics:

| Brand Personality | Typeface Style | Examples |
|-------------------|----------------|----------|
| Modern, minimal | Geometric sans | Inter, Outfit, Space Grotesk |
| Friendly, approachable | Humanist sans | Open Sans, Source Sans, Nunito |
| Professional, corporate | Neo-grotesque | Helvetica, Arial, Roboto |
| Premium, luxury | High-contrast serif | Playfair, Cormorant, Bodoni |
| Traditional, trustworthy | Old-style serif | Garamond, Georgia, Merriweather |
| Technical, precise | Monospace | JetBrains Mono, Fira Code |
| Playful, creative | Display | Custom, decorative |

### Step 2: Typeface Selection

**Primary typeface** — Used for headings and brand moments
- Must reflect brand personality
- Must have sufficient weights (400, 500, 600, 700 minimum)
- Must support required character sets

**Secondary typeface** — Used for body text and UI
- Must be highly readable at small sizes
- Must pair well with primary
- Consider: same family, complementary style, or contrast

**Pairing principles:**
- Serif + Sans (classic contrast)
- Geometric + Humanist (subtle contrast)
- Same family (different weights)

### Step 3: Type Scale

Define the modular scale for consistent sizing:

**Recommended scale (1.25 ratio):**

| Name | Size | Line Height | Use |
|------|------|-------------|-----|
| xs | 12px | 16px | Captions, labels |
| sm | 14px | 20px | Secondary text |
| base | 16px | 24px | Body text |
| lg | 18px | 28px | Lead text |
| xl | 20px | 28px | H6 |
| 2xl | 24px | 32px | H5 |
| 3xl | 30px | 36px | H4 |
| 4xl | 36px | 40px | H3 |
| 5xl | 48px | 48px | H2 |
| 6xl | 60px | 60px | H1 |
| 7xl | 72px | 72px | Display |

### Step 4: Hierarchy Definition

Define styles for each text role:

```
Display
  Font: [Primary], 72px, 700
  Letter-spacing: -0.02em
  Color: Neutral 900

H1
  Font: [Primary], 48px, 700
  Letter-spacing: -0.01em
  Color: Neutral 900

H2
  Font: [Primary], 36px, 600
  Letter-spacing: -0.01em
  Color: Neutral 900

Body
  Font: [Secondary], 16px, 400
  Letter-spacing: 0
  Line-height: 1.5
  Color: Neutral 700
```

### Step 5: Web Font Implementation

**Loading strategy:**
- Use `font-display: swap` for critical fonts
- Subset fonts for performance
- Provide system font fallbacks

**CSS custom properties:**
```css
:root {
  --font-primary: '[Primary]', [fallback-stack];
  --font-secondary: '[Secondary]', [fallback-stack];
}
```

## Output Schema

```json
{
    "skill": "typography",
    "cluster": "identity",
    "wave": 3,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "rationale": {
            "brand_personality": "string",
            "type_direction": "string",
            "pairing_logic": "string"
        },
        "typefaces": {
            "primary": {
                "name": "string",
                "foundry": "string",
                "style": "string (geometric, humanist, etc.)",
                "weights": ["number"],
                "use_for": "string",
                "source": "string (Google Fonts, Adobe, etc.)",
                "fallback_stack": "string"
            },
            "secondary": {
                "name": "string",
                "foundry": "string",
                "style": "string",
                "weights": ["number"],
                "use_for": "string",
                "source": "string",
                "fallback_stack": "string"
            }
        },
        "type_scale": {
            "ratio": "number (e.g., 1.25)",
            "base_size": "number (e.g., 16)",
            "sizes": {
                "xs": { "size": "string", "line_height": "string" },
                "sm": { "size": "string", "line_height": "string" },
                "base": { "size": "string", "line_height": "string" },
                "lg": { "size": "string", "line_height": "string" },
                "xl": { "size": "string", "line_height": "string" },
                "2xl": { "size": "string", "line_height": "string" },
                "3xl": { "size": "string", "line_height": "string" },
                "4xl": { "size": "string", "line_height": "string" },
                "5xl": { "size": "string", "line_height": "string" },
                "6xl": { "size": "string", "line_height": "string" },
                "7xl": { "size": "string", "line_height": "string" }
            }
        },
        "hierarchy": {
            "display": {
                "font": "string",
                "size": "string",
                "weight": "string",
                "letter_spacing": "string",
                "line_height": "string",
                "color": "string"
            },
            "h1": {},
            "h2": {},
            "h3": {},
            "h4": {},
            "h5": {},
            "h6": {},
            "body": {},
            "body_small": {},
            "caption": {},
            "label": {}
        },
        "implementation": {
            "css_variables": "string (CSS code)",
            "loading_strategy": "string",
            "font_display": "string"
        }
    }
}
```

## Quality Checklist

- [ ] Primary typeface reflects brand personality
- [ ] Typefaces pair well together
- [ ] Both typefaces have sufficient weights
- [ ] Type scale uses consistent ratio
- [ ] All hierarchy levels defined
- [ ] Fallback fonts specified
- [ ] Web font loading strategy defined
