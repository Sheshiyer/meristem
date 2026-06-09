---
name: brand-illustrations
description: "Generate brand illustrations — hero illustrations, spot illustrations, conceptual art. Uses GPT-Image-2 for generation."
cluster: brandmint-illustration
wave: 5
dependencies:
  - visual-language
  - color-palette
triggers:
  - "illustrations"
  - "hero illustration"
  - "spot illustrations"
  - "conceptual art"
---

# Brand Illustrations Skill

Generate custom brand illustrations that extend the visual identity.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for illustration style direction
- `color-palette.json` — for color restrictions

## Process

### Step 1: Illustration Needs Assessment

Define illustration types needed:

| Type | Purpose | Size/Complexity | Quantity |
|------|---------|-----------------|----------|
| **Hero** | Landing pages, key moments | Large, detailed | 2-3 |
| **Spot** | Feature sections, benefits | Medium, focused | 5-10 |
| **Decorative** | Background, accents | Small, simple | 3-5 |
| **Mascot** | Brand character (if applicable) | Variable | 1 + poses |
| **Conceptual** | Abstract brand concepts | Variable | 2-3 |

### Step 2: Style Codification

From visual-language, extract illustration style rules:

**Style parameters:**
- Line work: [weight, style, color]
- Fill style: [flat, gradient, textured]
- Color palette: [brand colors only]
- Level of detail: [minimal, moderate, detailed]
- Perspective: [flat, isometric, 3D]
- Character style: [if applicable]

### Step 3: Subject Planning

For each illustration, define:

| ID | Type | Subject | Concept/Message | Usage |
|----|------|---------|-----------------|-------|
| IL-01 | Hero | [subject] | [what it communicates] | Landing hero |
| IL-02 | Spot | [subject] | [what it communicates] | Feature 1 |

### Step 4: Generate Prompts

**Template for brand illustrations:**
```
[Type] illustration for [brand name] in a [style] style.

Subject: [detailed description]
Concept: [what this represents/communicates]

Style specifications:
- Line work: [from visual-language]
- Colors: ONLY use these colors: [list hex codes]
- Fill: [flat/gradient/textured]
- Detail level: [minimal/moderate/detailed]
- Perspective: [flat/isometric/3D]

Background: [transparent/solid color/gradient]
Mood: [playful/professional/energetic/calm]

Vector-style illustration, clean edges, brand-consistent.
Aspect ratio: [based on usage]
```

### Step 5: Consistency Checks

For a cohesive illustration system:
- [ ] All use same line weight
- [ ] All use brand colors only
- [ ] All use same perspective system
- [ ] All have consistent level of detail
- [ ] All convey same brand personality

### Step 6: Generate Images

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/illustration-[id].txt)" \
    --out "$brand_dir/generated/illustrations/[id].png" \
    --aspect [ratio]
```

## Output Schema

```json
{
    "skill": "brand-illustrations",
    "cluster": "illustration",
    "wave": 5,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "style_codification": {
            "line_work": {
                "weight": "string",
                "style": "string",
                "color": "string"
            },
            "fill_style": "string",
            "color_palette": ["string (hex codes)"],
            "detail_level": "string",
            "perspective": "string"
        },
        "illustrations": [
            {
                "id": "string",
                "type": "hero|spot|decorative|mascot|conceptual",
                "subject": "string",
                "concept": "string",
                "usage": "string",
                "aspect_ratio": "string",
                "generation_prompt": "string",
                "generated_path": "string"
            }
        ],
        "consistency_verified": "boolean",
        "generation_summary": {
            "total": "number",
            "generated": "number",
            "pending": "number"
        }
    }
}
```

## Quality Checklist

- [ ] Style codification matches visual-language
- [ ] All illustrations use brand colors only
- [ ] Hero illustrations defined for key pages
- [ ] Spot illustrations cover all features
- [ ] Consistent style across all illustrations
- [ ] Prompts specify vector-style output
