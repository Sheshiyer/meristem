---
name: hero-images
description: "Generate dramatic, campaign-ready hero visuals for landing pages, ads, and key brand moments. Uses GPT-Image-2 for generation."
cluster: brandmint-photography
wave: 4
dependencies:
  - visual-language
  - product-photography
  - lifestyle-photography
triggers:
  - "hero image"
  - "key visual"
  - "campaign image"
  - "banner image"
---

# Hero Images Skill

Generate dramatic, high-impact visuals for campaigns, landing pages, and brand moments.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for photography style direction
- `product-photography.json` — for product visual reference
- `lifestyle-photography.json` — for lifestyle direction
- `messaging-framework.json` — for key messages to visualize

## Process

### Step 1: Hero Image Requirements

Define hero image needs by placement:

| Placement | Aspect Ratio | Purpose | Copy Overlay? |
|-----------|--------------|---------|---------------|
| Landing page hero | 16:9 | First impression | Yes |
| Email header | 3:1 | Drive clicks | Yes |
| Social cover | 16:9 / 2.7:1 | Brand presence | Minimal |
| Ad creative | 1:1 / 4:5 / 9:16 | Conversion | Yes |
| Press kit | 16:9 | Media use | No |

### Step 2: Concept Development

For each hero image, define:

**Concept name:** [e.g., "The Prepared Gamer"]
**Message:** [What story does this tell?]
**Emotional impact:** [What should the viewer feel?]
**Visual approach:** [Lifestyle / Product-centric / Abstract / Composite]

### Step 3: Composition Planning

**Text-safe zones:**
For images with copy overlay, ensure:
- Clear area for headline (usually left or center)
- Adequate contrast for text readability
- Product/subject doesn't compete with text

**Focal point:**
- Where should the eye go first?
- What's the hero element?

### Step 4: Generate Prompts

**Template for hero images:**
```
Dramatic [lifestyle/product] photography for [brand name] campaign.

Scene: [detailed description of the hero moment]
Subject: [product and/or person]
Composition: [rule of thirds, centered, dynamic angle]
Focal point: [what draws the eye]

Mood: [aspirational/powerful/warm/energetic]
Lighting: [dramatic/cinematic/golden hour/studio]
Color palette: [reference brand colors]

Style: High-end advertising photography, campaign quality
[If text overlay needed]: Leave [left/right/top] third clear for headline

Cinematic quality, 8K, professional advertising photography.
Aspect ratio: [16:9 for web hero, 1:1 for social, 9:16 for stories]
```

### Step 5: Shot List

| Shot ID | Concept | Placement | Aspect | Text Zone | Priority |
|---------|---------|-----------|--------|-----------|----------|
| HI-01 | [name] | Landing hero | 16:9 | Left | High |
| HI-02 | [name] | Social | 1:1 | Bottom | High |
| HI-03 | [name] | Ad | 4:5 | Top | Medium |

### Step 6: Generate Images

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/hero-[id].txt)" \
    --out "$brand_dir/generated/hero-[id].png" \
    --aspect 16:9
```

## Output Schema

```json
{
    "skill": "hero-images",
    "cluster": "photography",
    "wave": 4,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "requirements": [
            {
                "placement": "string",
                "aspect_ratio": "string",
                "purpose": "string",
                "needs_text_zone": "boolean"
            }
        ],
        "concepts": [
            {
                "name": "string",
                "message": "string",
                "emotional_impact": "string",
                "visual_approach": "string"
            }
        ],
        "shot_list": [
            {
                "id": "string",
                "concept": "string",
                "placement": "string",
                "aspect_ratio": "string",
                "text_zone": "string",
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

- [ ] Hero images defined for all key placements
- [ ] Each concept has clear message and emotional intent
- [ ] Text-safe zones specified where needed
- [ ] Aspect ratios match intended platforms
- [ ] Prompts specify cinematic/campaign quality
- [ ] Primary landing page hero is highest priority
