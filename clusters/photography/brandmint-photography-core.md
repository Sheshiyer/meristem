---
name: brandmint-photography-core
description: "Shared reference for the photography cluster: GPT-Image-2 prompting patterns, lifestyle vs product shots, hero image composition, and photography direction."
cluster: brandmint-photography
wave: 4
version: 1.0.0
---

# Brandmint Photography Core

Shared reference for all photography spokes. Wave 4 generates photographic assets.

## The One Rule Everything Turns On

**GPT-Image-2 only.** No FAL, no Replicate, no Midjourney, no DALL-E 3 direct.

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$prompt" \
    --out "$brand_dir/generated/$filename"
```

## Inputs from Prior Waves

| Input | From | Used By |
|-------|------|---------|
| `visual_language.json` | W3 | All photography spokes |
| `color_palette.json` | W3 | Color treatment |
| `brand_foundation.json` | W1 | Subject matter |
| `buyer_persona.json` | W1 | People representation |

## GPT-Image-2 Prompting Framework

### Prompt Structure

```
[SUBJECT] + [STYLE] + [COMPOSITION] + [LIGHTING] + [COLOR] + [MOOD] + [TECHNICAL]
```

### Subject Guidelines

| Category | Prompt Pattern |
|----------|----------------|
| People | "Professional [demographic] in [setting], [action/pose]" |
| Product | "[Product type] on [surface], [arrangement]" |
| Abstract | "[Concept] represented through [visual metaphor]" |
| Environment | "[Location type] with [key elements], [time of day]" |

### Style Keywords

| Style | Keywords |
|-------|----------|
| Corporate | "professional, clean, modern, corporate photography" |
| Lifestyle | "authentic, candid, lifestyle photography, natural" |
| Editorial | "editorial style, magazine quality, high fashion" |
| Minimal | "minimalist, clean background, simple composition" |

### Technical Specifications

```
Aspect Ratios:
- Hero: 16:9 or 3:2
- Social: 1:1 or 4:5
- Portrait: 2:3 or 3:4

Resolution: Always request "high resolution, detailed"
```

## Photography Categories

### Lifestyle Photography

**Purpose**: Show brand in context of real life

**Prompt Template**:
```
Authentic lifestyle photography of [persona description] 
[doing activity related to product/service] in [realistic setting].
Natural lighting, candid moment, [brand color] accents in environment.
High resolution, editorial quality.
```

**Dos**:
- Show real scenarios
- Diverse representation
- Natural expressions
- Environmental context

**Don'ts**:
- Overly staged poses
- Stock photo clichés
- Unrealistic perfection

### Product Photography

**Purpose**: Showcase product clearly

**Prompt Template**:
```
Professional product photography of [product description].
[Surface/background description], [lighting setup].
[Angle: front/45-degree/flat-lay], clean composition.
[Brand color] accent elements. Studio quality, high resolution.
```

**Styles**:
| Style | Use Case |
|-------|----------|
| Hero shot | Main product page |
| Detail shot | Features section |
| In-context | Lifestyle integration |
| Flat lay | Social media |

### Hero Images

**Purpose**: Large, impactful visuals for headers

**Prompt Template**:
```
Cinematic hero image for [brand type] brand.
[Visual concept description] with [brand color] color palette.
[Composition: rule of thirds / centered / asymmetric].
Dramatic lighting, [mood adjectives].
Wide format (16:9), high resolution, professional photography.
```

**Composition Rules**:
- Leave space for text overlay
- Strong focal point
- Leading lines toward CTA area
- Brand colors in key elements

## Color Treatment

Based on `visual_language.json`:

| Treatment | When to Use | Prompt Addition |
|-----------|-------------|-----------------|
| Natural | Authentic brands | "natural colors, true to life" |
| Branded tint | Strong brand color | "subtle [color] color grade" |
| High contrast | Bold brands | "high contrast, vivid colors" |
| Muted | Sophisticated brands | "muted tones, desaturated" |
| Warm | Friendly brands | "warm color temperature" |
| Cool | Tech/professional | "cool color temperature" |

## Output Schemas

### lifestyle-shots.json

```json
{
  "skill": "lifestyle-shots",
  "cluster": "photography",
  "wave": 4,
  "data": {
    "shots": [
      {
        "id": "lifestyle-01",
        "concept": "Team collaboration",
        "prompt_used": "...",
        "generated_path": "./generated/lifestyle-01.png",
        "usage": ["about-page", "social"],
        "dimensions": "1920x1080"
      }
    ],
    "direction_notes": "...",
    "styling_guide": { ... }
  }
}
```

### product-photography.json

```json
{
  "skill": "product-photography",
  "cluster": "photography",
  "wave": 4,
  "data": {
    "shots": [
      {
        "id": "product-hero-01",
        "type": "hero",
        "prompt_used": "...",
        "generated_path": "./generated/product-hero-01.png",
        "background": "gradient-blue",
        "lighting": "soft-studio"
      }
    ],
    "product_styling": { ... }
  }
}
```

### hero-images.json

```json
{
  "skill": "hero-images",
  "cluster": "photography",
  "wave": 4,
  "data": {
    "heroes": [
      {
        "id": "hero-homepage",
        "page": "homepage",
        "concept": "...",
        "prompt_used": "...",
        "generated_path": "./generated/hero-homepage.png",
        "text_safe_zones": {
          "left": true,
          "center": false,
          "right": false
        },
        "cta_placement": "bottom-left"
      }
    ]
  }
}
```

## Generated Assets (Wave 4)

| Asset | Count | Path Pattern |
|-------|-------|--------------|
| Lifestyle shots | 3-5 | `generated/lifestyle-*.png` |
| Product photos | 3-5 | `generated/product-*.png` |
| Hero images | 2-3 | `generated/hero-*.png` |

## Quality Gates

| Check | Requirement |
|-------|-------------|
| All images generated | Files exist at paths |
| Prompts documented | Full prompt saved with each |
| Brand alignment | Colors/style match identity |
| Technical quality | Resolution sufficient |

## Asset Manifest Integration

Every generated image must be added to the asset manifest:

```json
{
  "id": "lifestyle-01",
  "path": "./generated/lifestyle-01.png",
  "type": "lifestyle",
  "exists": true,
  "deterministic": false,
  "wave": 4,
  "skill": "lifestyle-shots",
  "model": "gpt-image-2"
}
```

## Common Prompt Mistakes

| Mistake | Fix |
|---------|-----|
| Too vague | Add specific details |
| Too many subjects | Focus on one main subject |
| Conflicting styles | Choose one clear direction |
| Missing technical specs | Always include resolution/format |
| Brand colors not mentioned | Explicitly reference palette |
