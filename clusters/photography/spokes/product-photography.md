---
name: product-photography
description: "Generate clean product photography — pack shots, detail shots, angle variations. Uses GPT-Image-2 for generation."
cluster: brandmint-photography
wave: 4
dependencies:
  - visual-language
  - color-palette
triggers:
  - "product photos"
  - "pack shots"
  - "detail shots"
  - "product angles"
---

# Product Photography Skill

Generate clean, professional product photography for e-commerce, marketing, and documentation.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for photography style direction
- `color-palette.json` — for background and accent colors

## Process

### Step 1: Shot Type Planning

Define the required product shots:

| Type | Purpose | Background | Lighting |
|------|---------|------------|----------|
| **Hero** | Primary product image | White/gradient | Soft, even |
| **Angle 45°** | Show depth/dimension | White | 3-point lighting |
| **Side profile** | Show thickness/silhouette | White | Side-lit |
| **Top-down** | Show surface/features | White | Flat, even |
| **Detail** | Highlight specific features | Contextual | Macro |
| **Scale** | Show size reference | White | Even |
| **In-use** | Show product being used | Contextual | Natural |

### Step 2: Background Options

Define background variations:

| Background | Use Case | Prompt Addition |
|------------|----------|-----------------|
| Pure white | E-commerce, Amazon | "on pure white background, product photography" |
| Gradient | Marketing | "on soft [color] to white gradient background" |
| Brand color | Social media | "on [brand primary color] solid background" |
| Contextual | Lifestyle | "in [relevant setting]" |
| Transparent | Flexibility | "isolated product, transparent background" |

### Step 3: Generate Prompts

**Template for product photography:**
```
Professional product photography of [product name and description].

Product details: [key visual features to highlight]
Angle: [front/45-degree/side/top-down/detail]
Background: [white/gradient/colored/contextual]

Lighting: Studio lighting, [soft/dramatic], [even/directional]
Style: Clean, commercial, high-end product photography
Focus: Sharp throughout, high detail

[For detail shots]: Macro focus on [specific feature]
[For scale shots]: Include [reference object] for scale

8K quality, professional product photography, catalog style.
Aspect ratio: [1:1 for product, 4:3 for features]
```

### Step 4: Shot List

| Shot ID | Type | Angle | Background | Feature Focus | Priority |
|---------|------|-------|------------|---------------|----------|
| PP-01 | Hero | Front | White | Full product | High |
| PP-02 | Angle | 45° | White | Depth | High |
| PP-03 | Detail | Macro | Context | [Feature 1] | Medium |
| PP-04 | Detail | Macro | Context | [Feature 2] | Medium |
| PP-05 | Scale | Front | White | Size reference | Low |

### Step 5: Generate Images

For each prompt:

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/product-[id].txt)" \
    --out "$brand_dir/generated/product-[id].png" \
    --aspect 1:1
```

## Output Schema

```json
{
    "skill": "product-photography",
    "cluster": "photography",
    "wave": 4,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "product_description": "string",
        "key_features_to_highlight": ["string"],
        "shot_types": [
            {
                "type": "string",
                "purpose": "string",
                "background": "string",
                "lighting": "string"
            }
        ],
        "shot_list": [
            {
                "id": "string",
                "type": "string",
                "angle": "string",
                "background": "string",
                "feature_focus": "string",
                "priority": "high|medium|low",
                "generation_prompt": "string",
                "generated_path": "string"
            }
        ],
        "generation_summary": {
            "total_shots": "number",
            "generated": "number",
            "pending": "number"
        }
    }
}
```

## Quality Checklist

- [ ] Hero shot defined at highest priority
- [ ] Multiple angles covered (front, 45°, side, top)
- [ ] Key features have detail shots
- [ ] White background versions for e-commerce
- [ ] Prompts include lighting direction
- [ ] All prompts specify professional quality
