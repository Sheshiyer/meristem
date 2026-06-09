---
name: brandmint-illustration-core
description: "Shared reference for the illustration cluster: GPT-Image-2 illustration prompting, icon systems, pattern libraries, and brand illustration guidelines."
cluster: brandmint-illustration
wave: 5
version: 1.0.0
---

# Brandmint Illustration Core

Shared reference for all illustration spokes. Wave 5 generates illustrative assets.

## The One Rule Everything Turns On

**Consistency is everything.** All illustrations must share:
- Same style
- Same stroke weight
- Same color usage
- Same level of detail

## Visual Generation Constraint

**GPT-Image-2 only.** No FAL, no Replicate, no Midjourney.

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$prompt" \
    --out "$brand_dir/generated/$filename"
```

## Inputs from Prior Waves

| Input | From | Used By |
|-------|------|---------|
| `visual_language.json` | W3 | All illustration spokes |
| `color_palette.json` | W3 | Color usage |
| `brand_foundation.json` | W1 | Subject matter |

## Illustration Style Framework

### Style Categories

| Style | Characteristics | Best For |
|-------|-----------------|----------|
| Flat | Solid colors, no gradients, minimal shadows | Tech, Modern |
| Line Art | Outlines only, varying stroke weights | Minimal, Editorial |
| 3D | Depth, shadows, perspective | Playful, Premium |
| Hand-drawn | Organic, imperfect, sketchy | Creative, Approachable |
| Geometric | Shapes, patterns, mathematical | Abstract, Tech |
| Isometric | 3D perspective, consistent angle | Data, Process |

### Style Consistency Rules

Once a style is chosen, ALL illustrations must:

```yaml
line_art_rules:
  stroke_weight: "2px standard, 1px details"
  corners: "rounded (2px radius)"
  fills: "optional, brand colors only"
  shadows: "none"
  
flat_rules:
  fills: "solid colors from palette"
  outlines: "none or 1px darker shade"
  shadows: "flat offset shadow only"
  gradients: "none"
  
geometric_rules:
  shapes: "circles, squares, triangles only"
  angles: "45° or 90° only"
  colors: "max 3 from palette"
```

## GPT-Image-2 Illustration Prompts

### Prompt Structure

```
[STYLE] illustration of [SUBJECT], [COLOR SCHEME], [COMPOSITION],
[DETAIL LEVEL], [BACKGROUND], vector style, clean lines
```

### Style Keywords by Category

| Style | Prompt Keywords |
|-------|-----------------|
| Flat | "flat design, solid colors, no gradients, minimal, vector" |
| Line Art | "line art, outline illustration, single weight stroke, minimal" |
| 3D | "3D illustration, soft shadows, depth, modern 3D render" |
| Hand-drawn | "hand-drawn style, sketch, organic lines, imperfect" |
| Geometric | "geometric shapes, abstract, mathematical, pattern-based" |
| Isometric | "isometric illustration, 30-degree angle, technical" |

### Color Instructions

```
# Limited palette (recommended)
"using only [primary], [secondary], and [accent] colors"

# Monochrome
"monochromatic [color] illustration with tints and shades"

# Full palette
"brand color palette with [primary] as dominant color"
```

## Icon System Guidelines

### Grid System

```
Base: 24x24px
Scales: 16, 24, 32, 48, 64

┌──────────────────────┐
│  ┌──────────────┐   │  2px padding
│  │              │   │
│  │    ICON      │   │  20x20 live area
│  │    AREA      │   │
│  │              │   │
│  └──────────────┘   │
└──────────────────────┘
```

### Icon Categories

| Category | Examples | Style Notes |
|----------|----------|-------------|
| Navigation | Home, Menu, Back | Simple, recognizable |
| Actions | Edit, Delete, Add | Clear affordance |
| Objects | File, Folder, User | Consistent metaphors |
| Status | Success, Warning, Info | Color-coded |
| Social | Share, Like, Comment | Platform-neutral |

### Icon Prompt Template

```
Simple [style] icon of [object/concept],
[stroke weight]px stroke, [corner style] corners,
[color] on transparent background,
24x24 pixel grid, centered, minimal detail
```

## Pattern Library

### Pattern Types

| Type | Use Case | Prompt Keywords |
|------|----------|-----------------|
| Geometric | Backgrounds, cards | "repeating geometric pattern" |
| Organic | Textures, overlays | "organic flowing pattern" |
| Abstract | Hero sections | "abstract brand pattern" |
| Illustrative | Feature sections | "illustrated scene pattern" |

### Pattern Rules

```yaml
pattern_guidelines:
  seamless: true  # Must tile seamlessly
  scale: "works at 50% and 200%"
  color_variants:
    - "primary on white"
    - "white on primary"
    - "accent on dark"
  opacity: "10-20% for backgrounds"
```

## Output Schemas

### brand-illustrations.json

```json
{
  "skill": "brand-illustrations",
  "cluster": "illustration",
  "wave": 5,
  "data": {
    "style_guide": {
      "style": "flat",
      "stroke_weight": null,
      "corner_radius": null,
      "shadow_style": "flat-offset",
      "color_usage": "limited-palette"
    },
    "illustrations": [
      {
        "id": "illust-hero-01",
        "concept": "Team collaboration",
        "prompt_used": "...",
        "generated_path": "./generated/illust-hero-01.png",
        "usage": ["homepage-hero", "about-section"],
        "dimensions": "1200x800"
      }
    ]
  }
}
```

### icon-system.json

```json
{
  "skill": "icon-system",
  "cluster": "illustration",
  "wave": 5,
  "data": {
    "style": {
      "type": "line-art",
      "stroke_weight": "2px",
      "corners": "rounded-2px",
      "grid": "24x24"
    },
    "icons": [
      {
        "id": "icon-dashboard",
        "name": "Dashboard",
        "category": "navigation",
        "prompt_used": "...",
        "generated_path": "./generated/icons/dashboard.png",
        "sizes": [16, 24, 32]
      }
    ],
    "icon_font": {
      "generated": false,
      "format": "svg-sprite"
    }
  }
}
```

### pattern-library.json

```json
{
  "skill": "pattern-library",
  "cluster": "illustration",
  "wave": 5,
  "data": {
    "patterns": [
      {
        "id": "pattern-geo-01",
        "name": "Geometric Grid",
        "type": "geometric",
        "prompt_used": "...",
        "generated_path": "./generated/patterns/geo-01.png",
        "seamless": true,
        "color_variants": [
          "./generated/patterns/geo-01-light.png",
          "./generated/patterns/geo-01-dark.png"
        ],
        "usage": ["card-backgrounds", "section-dividers"]
      }
    ]
  }
}
```

## Generated Assets (Wave 5)

| Asset | Count | Path Pattern |
|-------|-------|--------------|
| Brand illustrations | 3-5 | `generated/illust-*.png` |
| Icons | 10-20 | `generated/icons/*.png` |
| Patterns | 2-3 | `generated/patterns/*.png` |

## Quality Gates

| Check | Requirement |
|-------|-------------|
| Style consistency | All same style/weight |
| Color compliance | Only palette colors used |
| Grid alignment | Icons on 24px grid |
| Pattern seamless | Tiles without visible seams |

## Asset Manifest Integration

Every generated illustration must be registered:

```json
{
  "id": "illust-hero-01",
  "path": "./generated/illust-hero-01.png",
  "type": "illustration",
  "exists": true,
  "deterministic": false,
  "wave": 5,
  "skill": "brand-illustrations",
  "model": "gpt-image-2",
  "style": "flat"
}
```

## Common Illustration Mistakes

| Mistake | Fix |
|---------|-----|
| Inconsistent style | Lock style before generating |
| Too much detail | Simplify, match brand complexity |
| Wrong colors | Always reference palette explicitly |
| Icons not centered | Specify "centered in frame" |
| Patterns don't tile | Add "seamless, tileable" to prompt |
