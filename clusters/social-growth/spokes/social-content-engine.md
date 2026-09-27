---
name: social-content-engine
description: "Generate a 30-day content calendar with weekly themes, platform-specific posts, and content mix (value/connection/engagement/promotion). Ported from brandmint-oracle-aleph and adapted for service studios."
cluster: brandmint-social-growth
wave: 6
dependencies:
  - voice-and-tone
  - messaging-framework
  - buyer-persona
triggers:
  - "content calendar"
  - "30-day plan"
  - "weekly themes"
  - "social media schedule"
---

# Social Content Engine Skill

Generate a strategic 30-day content calendar that builds audience around the Thoughtseed delivery loop.

## Prerequisites

- `voice-and-tone.json` — vocabulary, prohibited terms
- `messaging-framework.json` — key messages and value pillars
- `buyer-persona.json` — audience targeting
- `product-positioning.json` — differentiators

## Process

### Step 1: Weekly Themes

Assign a theme to each of 4 weeks:

| Week | Theme | Focus |
|------|-------|-------|
| 1 | Pain Awareness | The fragmentation problem, what the founder carries, why it breaks |
| 2 | Solution Education | The delivery loop, what each stage does, how it holds together |
| 3 | Studio Story | Who does the work, how decisions are made, what handoff means |
| 4 | Call to Engage | Bring the requirement, scoped delivery, ownership transfer |

### Step 2: Platform Adaptation

For each post, generate platform-specific versions:

| Platform | Format | Voice |
|----------|--------|-------|
| Instagram | Reel ideas, carousel posts, single image with caption | Visual-first, restrained text |
| LinkedIn | Long-form text, document posts, articles | Professional, evidence-led |
| X/Twitter | Threads, single tweets, quote cards | Concise, declarative, evidence-close |

### Step 3: Content Mix

Distribute posts across categories:
- 40% Value (delivery loop stages, design principles, founder operating logic)
- 30% Connection (founder-led, behind-the-scenes, who's doing the work)
- 20% Engagement (polls, questions, founder challenge probes)
- 10% Promotion (Bring the requirement, link to delivery loop)

### Step 4: Daily Plan

Generate 30 days of specific post ideas. For each day:
- Date
- Platform
- Post type
- Hook (first line for visual, headline for text)
- Body (1-2 sentences for short-form, 100-200 words for long-form)
- Visual description (if applicable)
- CTA (if applicable)

## Output Schema

```json
{
    "skill": "social-content-engine",
    "cluster": "social-growth",
    "wave": 6,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "weekly_themes": [
            {"week": 1, "theme": "string", "focus": "string", "post_count": "number"}
        ],
        "platform_strategy": {
            "instagram": {"format": "string", "voice": "string", "post_count": "number"},
            "linkedin": {"format": "string", "voice": "string", "post_count": "number"},
            "x": {"format": "string", "voice": "string", "post_count": "number"}
        },
        "content_mix": {
            "value": {"percentage": 40, "topic_examples": ["string"]},
            "connection": {"percentage": 30, "topic_examples": ["string"]},
            "engagement": {"percentage": 20, "topic_examples": ["string"]},
            "promotion": {"percentage": 10, "topic_examples": ["string"]}
        },
        "calendar": [
            {
                "day": "number",
                "date": "ISO date",
                "platform": "string",
                "post_type": "string",
                "category": "value|connection|engagement|promotion",
                "hook": "string",
                "body": "string",
                "visual_description": "string",
                "cta": "string"
            }
        ],
        "voice_compliance": "PASS — no prohibited terms"
    }
}
```

## Quality Checklist

- [ ] 30 days, sequential, no gaps
- [ ] Content mix follows 40/30/20/10 distribution
- [ ] All hooks reference delivery loop or its vocabulary
- [ ] No prohibited terms (conscious-aligned, disruptive, etc.)
- [ ] CTAs are restrained (Bring the requirement, not BUY NOW)
- [ ] Visual descriptions are specific, not generic