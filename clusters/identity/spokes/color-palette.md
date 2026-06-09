---
name: color-palette
description: "Define brand color palette — primary, secondary, accent, and neutral colors with hex codes, usage rules, and accessibility guidelines."
cluster: brandmint-identity
wave: 3
dependencies:
  - brand-foundation
  - buyer-persona
triggers:
  - "color palette"
  - "brand colors"
  - "color scheme"
  - "what colors"
---

# Color Palette Skill

Define the brand color system with emotional rationale, usage rules, and accessibility compliance.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for brand personality and values
- `buyer-persona.json` — for audience preferences

## Process

### Step 1: Color Psychology Mapping

Map brand attributes to color associations:

| Brand Attribute | Color Family | Emotional Association |
|-----------------|--------------|----------------------|
| Trust | Blue | Reliability, calm, professional |
| Energy | Orange/Red | Excitement, urgency, passion |
| Growth | Green | Nature, health, prosperity |
| Premium | Black/Gold | Luxury, sophistication |
| Innovation | Purple | Creativity, imagination |
| Warmth | Yellow/Orange | Optimism, friendliness |
| Purity | White | Clean, simple, honest |

### Step 2: Primary Color Selection

**The primary color is the brand's signature.** It should:
- Reflect the core brand personality
- Differentiate from competitors
- Work across all mediums (digital + print)

**Selection criteria:**
1. Emotional alignment with brand
2. Differentiation from competition
3. Versatility (light/dark backgrounds)
4. Accessibility compliance

### Step 3: Color System Structure

**Build the full palette:**

| Role | Purpose | Example |
|------|---------|---------|
| **Primary** | Main brand color, CTAs, key elements | #2563EB |
| **Secondary** | Supporting color, sections, accents | #7C3AED |
| **Accent** | Highlights, alerts, emphasis | #F59E0B |
| **Success** | Positive states, confirmations | #10B981 |
| **Warning** | Caution states | #F59E0B |
| **Error** | Error states, destructive actions | #EF4444 |
| **Neutral 900** | Primary text | #111827 |
| **Neutral 600** | Secondary text | #4B5563 |
| **Neutral 400** | Disabled text, borders | #9CA3AF |
| **Neutral 100** | Backgrounds | #F3F4F6 |
| **White** | Cards, surfaces | #FFFFFF |

### Step 4: Accessibility Check

**WCAG 2.1 AA Requirements:**
- Normal text: 4.5:1 contrast ratio
- Large text (18px+): 3:1 contrast ratio
- UI components: 3:1 contrast ratio

**Test each combination:**
| Foreground | Background | Contrast Ratio | Pass? |
|------------|------------|----------------|-------|
| Primary | White | X.XX:1 | ✓/✗ |
| White | Primary | X.XX:1 | ✓/✗ |
| Neutral 900 | White | X.XX:1 | ✓/✗ |

### Step 5: Usage Guidelines

**Do's and Don'ts for each color:**

```
Primary Color (#XXXX)
✓ Use for: CTAs, links, key headlines, brand moments
✗ Don't use for: Large background areas, body text
```

### Step 6: Color Variations

For each primary/secondary color, define:
- **50** — Lightest tint (backgrounds)
- **100-400** — Light variations
- **500** — Base color
- **600-800** — Dark variations
- **900** — Darkest shade

## Output Schema

```json
{
    "skill": "color-palette",
    "cluster": "identity",
    "wave": 3,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "rationale": {
            "brand_attributes": ["string"],
            "color_psychology": "string",
            "competitor_differentiation": "string"
        },
        "palette": {
            "primary": {
                "hex": "string",
                "rgb": "string",
                "hsl": "string",
                "name": "string (e.g., 'Brand Blue')",
                "usage": "string",
                "variations": {
                    "50": "string",
                    "100": "string",
                    "200": "string",
                    "300": "string",
                    "400": "string",
                    "500": "string",
                    "600": "string",
                    "700": "string",
                    "800": "string",
                    "900": "string"
                }
            },
            "secondary": {
                "hex": "string",
                "name": "string",
                "usage": "string",
                "variations": {}
            },
            "accent": {
                "hex": "string",
                "name": "string",
                "usage": "string"
            },
            "semantic": {
                "success": "string",
                "warning": "string",
                "error": "string",
                "info": "string"
            },
            "neutrals": {
                "900": "string",
                "800": "string",
                "700": "string",
                "600": "string",
                "500": "string",
                "400": "string",
                "300": "string",
                "200": "string",
                "100": "string",
                "50": "string"
            }
        },
        "accessibility": {
            "contrast_checks": [
                {
                    "foreground": "string",
                    "background": "string",
                    "ratio": "string",
                    "wcag_aa": "boolean",
                    "wcag_aaa": "boolean"
                }
            ]
        },
        "usage_guidelines": {
            "primary": {
                "do": ["string"],
                "dont": ["string"]
            },
            "secondary": {
                "do": ["string"],
                "dont": ["string"]
            }
        }
    }
}
```

## Quality Checklist

- [ ] Primary color aligns with brand personality
- [ ] Color differentiates from competitors
- [ ] Full variation scale (50-900) for primary/secondary
- [ ] All text combinations pass WCAG AA
- [ ] Semantic colors defined (success, warning, error)
- [ ] Neutral scale complete
- [ ] Usage guidelines provided for each color
