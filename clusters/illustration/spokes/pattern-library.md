---
name: pattern-library
description: "Generate brand patterns and textures — repeatable patterns, background textures, decorative elements."
cluster: brandmint-illustration
wave: 5
dependencies:
  - visual-language
  - color-palette
triggers:
  - "patterns"
  - "textures"
  - "backgrounds"
  - "decorative elements"
---

# Pattern Library Skill

Create seamless patterns and textures that extend the brand visual system.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for pattern direction
- `color-palette.json` — for color restrictions

## Process

### Step 1: Pattern Strategy

Define pattern needs:

| Usage | Pattern Type | Scale | Density |
|-------|--------------|-------|---------|
| **Hero backgrounds** | [type] | Large | Low |
| **Section dividers** | [type] | Medium | Medium |
| **Card backgrounds** | [type] | Small | Low |
| **Accent elements** | [type] | Variable | Medium |
| **Print/packaging** | [type] | Variable | Variable |

### Step 2: Pattern Types

Select pattern approaches that fit brand:

| Type | Description | Brand Fit |
|------|-------------|-----------|
| **Geometric** | Shapes, grids, lines | Modern, tech, minimal |
| **Organic** | Flowing, natural forms | Friendly, natural, creative |
| **Abstract** | Non-representational | Unique, artistic |
| **Illustrative** | Brand elements repeated | Playful, recognizable |
| **Textural** | Subtle surface quality | Premium, tactile |

### Step 3: Color Combinations

Define allowed color combinations for patterns:

| Combination | Foreground | Background | Usage |
|-------------|------------|------------|-------|
| Primary on light | [primary] | [neutral-100] | Default |
| Primary on dark | [primary] | [neutral-900] | Dark mode |
| Neutral subtle | [neutral-300] | [neutral-100] | Subtle texture |
| Accent | [accent] | [white] | Emphasis |

### Step 4: Pattern Inventory

| ID | Name | Type | Colors | Usage | Tile Size |
|----|------|------|--------|-------|-----------|
| PT-01 | [name] | [type] | [combo] | Backgrounds | 200x200 |
| PT-02 | [name] | [type] | [combo] | Sections | 100x100 |

### Step 5: Generate Prompts

**Template for seamless patterns:**
```
Seamless repeating pattern for [brand name].

Pattern type: [geometric/organic/abstract/illustrative]
Elements: [describe the repeating elements]
Scale: [small/medium/large] elements

Colors: 
- Foreground: [color/hex]
- Background: [color/hex]
- [Additional colors if needed]

Style: [minimal/detailed], [modern/classic]
Mood: [aligned with brand personality]

IMPORTANT: Pattern must tile seamlessly in all directions.
No visible seams when repeated.
Square format for tiling.
```

**Template for textures:**
```
Subtle texture/grain for [brand name] backgrounds.

Type: [paper/fabric/noise/gradient]
Color: [base color]
Intensity: [subtle/medium/strong]

Style: [organic/digital]
Usage: Background texture, overlay

Seamless, tileable, high resolution.
```

### Step 6: Generate Patterns

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/pattern-[id].txt)" \
    --out "$brand_dir/generated/patterns/[id].png" \
    --aspect 1:1
```

### Step 7: Tiling Test

After generation, verify patterns tile correctly:
- No visible seams
- Elements don't cluster at edges
- Density is consistent

## Output Schema

```json
{
    "skill": "pattern-library",
    "cluster": "illustration",
    "wave": 5,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "strategy": {
            "usage_types": [
                {
                    "usage": "string",
                    "pattern_type": "string",
                    "scale": "string",
                    "density": "string"
                }
            ]
        },
        "color_combinations": [
            {
                "name": "string",
                "foreground": "string",
                "background": "string",
                "usage": "string"
            }
        ],
        "patterns": [
            {
                "id": "string",
                "name": "string",
                "type": "geometric|organic|abstract|illustrative|textural",
                "colors": {
                    "foreground": "string",
                    "background": "string"
                },
                "usage": "string",
                "tile_size": "string",
                "generation_prompt": "string",
                "generated_path": "string",
                "tiling_verified": "boolean"
            }
        ],
        "textures": [
            {
                "id": "string",
                "name": "string",
                "type": "string",
                "base_color": "string",
                "intensity": "string",
                "generation_prompt": "string",
                "generated_path": "string"
            }
        ],
        "generation_summary": {
            "total": "number",
            "generated": "number",
            "verified_tileable": "number"
        }
    }
}
```

## Quality Checklist

- [ ] Pattern types align with brand personality
- [ ] All patterns use brand colors only
- [ ] Multiple scale options available
- [ ] Color combinations defined for each pattern
- [ ] All patterns verified as seamlessly tileable
- [ ] Usage guidelines provided for each pattern
