---
name: icon-system
description: "Generate brand icon system — UI icons, feature icons, category icons. Consistent style across all iconography."
cluster: brandmint-illustration
wave: 5
dependencies:
  - visual-language
  - color-palette
triggers:
  - "icons"
  - "icon set"
  - "feature icons"
  - "UI icons"
---

# Icon System Skill

Create a comprehensive, consistent icon system for the brand.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for iconography specifications
- `color-palette.json` — for icon colors

## Process

### Step 1: Icon Style Definition

From visual-language, establish icon rules:

| Parameter | Specification |
|-----------|---------------|
| **Style** | Line / Filled / Duotone |
| **Stroke weight** | Xpx |
| **Corner radius** | Sharp / Xpx radius |
| **Grid size** | Xpx base grid |
| **Padding** | X% of canvas |
| **Line caps** | Round / Square / Butt |
| **Line joins** | Round / Miter / Bevel |

### Step 2: Icon Categories

Define icons needed by category:

**UI Icons (Navigation/Actions):**
- Menu, Close, Search, Settings
- Arrow variants (up, down, left, right)
- Plus, Minus, Check, X
- User, Cart, Heart, Share

**Feature Icons (Product Benefits):**
- [Feature 1 icon]
- [Feature 2 icon]
- [Feature 3 icon]
- [Feature 4 icon]

**Category Icons (Sections/Topics):**
- [Category 1]
- [Category 2]
- [Category 3]

### Step 3: Icon Inventory

| ID | Category | Name | Concept | Priority |
|----|----------|------|---------|----------|
| IC-01 | Feature | [name] | [what it represents] | High |
| IC-02 | Feature | [name] | [what it represents] | High |
| IC-03 | UI | [name] | [standard meaning] | Medium |

### Step 4: Generate Prompts

**Template for icons:**
```
Minimalist icon representing [concept] for [brand name].

Style: [Line/Filled/Duotone] icon
Stroke: [X]px weight, [round/square] caps
Corners: [sharp/rounded]
Colors: [primary color] on transparent background
[For duotone]: Primary [color 1], secondary [color 2]

Simple, recognizable, scalable from 16px to 96px.
Single concept, no text, centered on canvas.
Vector-style, clean geometry.
Square format, icon only.
```

### Step 5: Size Variants

For each icon, generate at standard sizes:
- 16px — Inline, small UI
- 24px — Default UI
- 32px — Medium emphasis
- 48px — Feature sections
- 64px — Large feature
- 96px — Hero/decorative

### Step 6: Export Specifications

**Formats needed:**
- SVG (scalable, web)
- PNG @1x, @2x, @3x (apps)
- Icon font (if applicable)

## Output Schema

```json
{
    "skill": "icon-system",
    "cluster": "illustration",
    "wave": 5,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "style_definition": {
            "type": "line|filled|duotone",
            "stroke_weight": "string",
            "corner_radius": "string",
            "grid_size": "string",
            "padding": "string",
            "line_caps": "string",
            "line_joins": "string",
            "colors": {
                "primary": "string",
                "secondary": "string"
            }
        },
        "categories": {
            "ui": ["string (icon names)"],
            "feature": ["string (icon names)"],
            "category": ["string (icon names)"]
        },
        "icons": [
            {
                "id": "string",
                "category": "string",
                "name": "string",
                "concept": "string",
                "priority": "high|medium|low",
                "generation_prompt": "string",
                "generated_path": "string",
                "sizes": ["16", "24", "32", "48", "64", "96"]
            }
        ],
        "export_formats": ["svg", "png"],
        "generation_summary": {
            "total_icons": "number",
            "generated": "number",
            "pending": "number"
        }
    }
}
```

## Quality Checklist

- [ ] Style definition matches visual-language specs
- [ ] All feature icons defined
- [ ] Common UI icons included
- [ ] Consistent style across all icons
- [ ] All icons work at 16px (legibility check)
- [ ] Colors limited to brand palette
- [ ] Export formats specified
