---
name: lifestyle-photography
description: "Generate lifestyle photography prompts showing the product in real-world context with target personas. Uses GPT-Image-2 for generation."
cluster: brandmint-photography
wave: 4
dependencies:
  - visual-language
  - buyer-persona
triggers:
  - "lifestyle photos"
  - "people using product"
  - "context shots"
  - "in-use photography"
---

# Lifestyle Photography Skill

Generate lifestyle photography that shows the product in authentic, aspirational contexts.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for photography style direction
- `buyer-persona.json` — for demographic and psychographic details
- `color-palette.json` — for color coordination

## Process

### Step 1: Scene Planning

Define 5-8 lifestyle scenarios based on buyer persona:

| Scenario | Setting | Activity | Mood | Key Message |
|----------|---------|----------|------|-------------|
| [name] | [location] | [what they're doing] | [emotional tone] | [what this conveys] |

**Scenario types:**
- **Hero moment** — The peak experience
- **Daily use** — Routine integration
- **Social context** — With friends/family
- **Problem/solution** — Before/after feeling
- **Aspirational** — The lifestyle they want

### Step 2: Subject Direction

Based on buyer persona, specify:

**Demographics to show:**
- Age range
- Style/aesthetic
- Diversity considerations

**Expression/body language:**
- Engaged, not posed
- Authentic, not stock-photo perfect
- Emotions that match the scenario

### Step 3: Generate Prompts

For each scenario, create a detailed GPT-Image-2 prompt:

**Template:**
```
Lifestyle photography of [subject description: age, gender, style] 
[activity with product] in [setting].

Setting details: [environment description, time of day, weather if outdoor]
Product placement: [how product appears in scene]
Subject expression: [emotional state, body language]

Photography style:
- Lighting: [from visual-language]
- Composition: [from visual-language]
- Color treatment: [from visual-language]
- Mood: [from visual-language]

High quality, editorial photography, authentic moment, not staged.
Aspect ratio: [16:9 for hero, 4:5 for social, 1:1 for square]
```

### Step 4: Shot List

Create the full shot list with variations:

| Shot ID | Scenario | Angle | Crop | Aspect | Priority |
|---------|----------|-------|------|--------|----------|
| LS-01 | [name] | [wide/medium/close] | [full/waist/detail] | [ratio] | [high/med] |

### Step 5: Generate Images

For each prompt, call GPT-Image-2:

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/lifestyle-[id].txt)" \
    --out "$brand_dir/generated/lifestyle-[id].png" \
    --aspect [ratio]
```

## Output Schema

```json
{
    "skill": "lifestyle-photography",
    "cluster": "photography",
    "wave": 4,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "scenarios": [
            {
                "id": "string (e.g., LS-01)",
                "name": "string",
                "setting": "string",
                "activity": "string",
                "mood": "string",
                "key_message": "string"
            }
        ],
        "subject_direction": {
            "demographics": "string",
            "style": "string",
            "expression": "string",
            "diversity_notes": "string"
        },
        "shot_list": [
            {
                "id": "string",
                "scenario": "string",
                "angle": "string",
                "crop": "string",
                "aspect_ratio": "string",
                "priority": "high|medium|low",
                "generation_prompt": "string",
                "generated_path": "string (output file path)"
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

- [ ] 5-8 scenarios defined
- [ ] Scenarios reflect buyer persona lifestyle
- [ ] Subject direction matches target demographic
- [ ] All prompts include photography style from visual-language
- [ ] Aspect ratios appropriate for intended use
- [ ] Priority levels assigned to all shots
