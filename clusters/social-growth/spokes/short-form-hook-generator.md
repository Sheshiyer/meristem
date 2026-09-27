---
name: short-form-hook-generator
description: "Generate 15-second viral hooks for short-form video (TikTok/Reels/Shorts) based on Thoughtseed delivery-loop content. Ported from brandmint-oracle-aleph and adapted for service studios."
cluster: brandmint-social-growth
wave: 6
dependencies:
  - voice-and-tone
  - messaging-framework
triggers:
  - "TikTok hooks"
  - "Reels hooks"
  - "Shorts"
  - "viral hooks"
  - "scroll-stopping"
---

# Short-Form Hook Generator

Generate scroll-stopping 15-second hooks that ground in Thoughtseed's delivery loop narrative.

## Process

### Step 1: Soundbyte Extraction

Pull punchy sentences from existing content (messaging framework, landing page copy, social calendar) that fit under 5 seconds when read aloud.

### Step 2: Visual Pairing

For each hook, describe the visual action that happens immediately (the "pattern interrupt").

### Step 3: Hook Categories

Generate hooks across four buckets:

| Category | Pattern | Service-studio adaptation |
|----------|---------|---------------------------|
| Negative/Warning | "Stop doing X..." | "Stop splitting your requirement across five vendors..." |
| Curiosity/Secret | "The #1 reason..." | "The #1 reason systems break at handoff..." |
| Outcome/Benefit | "How I got X in Y" | "How we ship a coherent system in 4 stages..." |
| Visual Oddity | "What is this thing?" | "What is the Digital Wilderness concept..." |

### Step 4: Script Construction

Write the first 15 seconds for each hook:
- 0:00-0:03 — Hook (3-second pattern interrupt)
- 0:03-0:08 — Setup (5-second context)
- 0:08-0:15 — Payoff (7-second reveal + CTA)

## Output Schema

```json
{
    "skill": "short-form-hook-generator",
    "cluster": "social-growth",
    "wave": 6,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "hooks": [
            {
                "id": "number",
                "category": "negative|curiosity|outcome|visual_oddity",
                "hook_text": "string (≤5 sec spoken)",
                "visual_action": "string",
                "script": [
                    {"timestamp": "0:00-0:03", "voiceover": "string", "on_screen": "string"},
                    {"timestamp": "0:03-0:08", "voiceover": "string", "on_screen": "string"},
                    {"timestamp": "0:08-0:15", "voiceover": "string", "on_screen": "string"}
                ],
                "cta": "string",
                "platform_fit": ["tiktok", "reels", "shorts"]
            }
        ],
        "voice_compliance": "PASS"
    }
}
```

## Quality Checklist

- [ ] 10-15 hooks generated across all 4 categories
- [ ] Each hook fits within 15 seconds total
- [ ] Hook text is under 5 seconds spoken
- [ ] Visual action is specific (not "person doing something")
- [ ] All scripts ground in delivery loop vocabulary
- [ ] No prohibited terms