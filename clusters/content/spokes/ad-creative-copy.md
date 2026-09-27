---
name: ad-creative-copy
description: "Create ad copy variations for pre-campaign and live campaign periods. Covers Facebook, Instagram, and other paid media platforms."
cluster: brandmint-content
wave: 6
dependencies:
  - voice-and-tone
  - messaging-framework
  - buyer-persona
  - value-proposition
triggers:
  - "ad copy"
  - "Facebook ads"
  - "Instagram ads"
  - "paid media"
  - "ad creative"
---

# Ad Creative Copy Skill

Create ad copy variations for paid media campaigns.

## Prerequisites

Load upstream outputs:
- `voice-and-tone.json` — for ad voice
- `messaging-framework.json` — for headlines and pillars
- `buyer-persona.json` — for targeting hooks
- `value-proposition.json` — for key benefits

## Process

### Step 1: Ad Strategy

**Campaign phases:**
| Phase | Goal | Angle | Urgency |
|-------|------|-------|---------|
| Pre-launch | List building | Curiosity, problem | Low |
| Launch | Conversions | Solution, benefits | Medium |
| Mid-campaign | Conversions | Social proof, features | Medium |
| End-campaign | Final push | Scarcity, FOMO | High |

### Step 2: Ad Formats

Create copy for each format:

| Format | Platform | Headline | Body | CTA |
|--------|----------|----------|------|-----|
| Single image | FB/IG | 40 chars | 125 chars | Button |
| Carousel | FB/IG | Per card | 125 chars | Button |
| Video | FB/IG | 40 chars | 125 chars | Button |
| Stories | IG | Overlay | Minimal | Swipe up |

### Step 3: Hook Categories

Develop hooks for different angles:

**Problem-aware hooks:**
- "Tired of [problem]?"
- "If you've ever [frustration]..."
- "[Problem] driving you crazy?"

**Solution-aware hooks:**
- "Finally, a [category] that [benefit]"
- "Introducing [product]: [key differentiator]"
- "The [category] designed for [audience]"

**Social proof hooks:**
- "[X] [audience] already [action]"
- "See why [audience] are switching to [product]"
- "Backed by [X]+ people in [timeframe]"

**Urgency hooks:**
- "Only [X] days left"
- "Early-bird pricing ends [date]"
- "Limited quantities available"

### Step 4: Create Ad Variations

For each phase, create 3-5 variations:

**Variation structure:**
```
Hook: [Attention-grabbing opening]
Body: [Value proposition + benefit]
CTA: [Clear action]
```

### Step 5: Pre-Campaign Ads

**Ad 1: Problem Agitation**
```
Headline: [Problem question]
Body: [Elaborate on frustration + hint at solution]
CTA: Get Early Access
```

**Ad 2: Curiosity**
```
Headline: [Intriguing tease]
Body: [Build mystery + promise value]
CTA: Join the Waitlist
```

**Ad 3: Social/Community**
```
Headline: [Community angle]
Body: [Join others who understand]
CTA: Sign Up Now
```

### Step 6: Live Campaign Ads

**Ad 1: Launch Announcement**
```
Headline: [We're live + product]
Body: [Key benefit + early-bird incentive]
CTA: Back Now
```

**Ad 2: Feature Focus**
```
Headline: [Specific feature benefit]
Body: [How it works + outcome]
CTA: Learn More
```

**Ad 3: Social Proof**
```
Headline: [Funding milestone]
Body: [Community validation + FOMO]
CTA: Join [X]+ Backers
```

**Ad 4: Urgency**
```
Headline: [Time remaining]
Body: [Don't miss out + recap value]
CTA: Back Before It's Gone
```

## Bilingual FR + EN (additive)

When `market.region: FR` **or** `locales` includes `fr`, emit both language variants under `data.locales.{en,fr}`. JSON remains primary wave output.

**Planned wiki paths:**
- `wiki/src/content/docs/en/marketing/ad-creative.md`
- `wiki/src/content/docs/fr/marketing/ad-creative.md`

## Explee Draft Schema (draft-only, no POST)

Also emit an **explee-compatible draft payload** for landing/ads/emails. This is **draft-only** — never POST to Explee or any live ad/email API from this spoke.

```json
{
  "explee_draft": {
    "mode": "draft_only",
    "do_not_post": true,
    "targets": ["landing", "ads", "emails"],
    "locales": ["fr", "en"],
    "output_format": {
      "landing": {
        "headline": "string",
        "subhead": "string",
        "cta": "string",
        "body_blocks": ["string"]
      },
      "ads": [
        {
          "platform": "linkedin|meta|other",
          "locale": "fr|en",
          "headline": "string",
          "primary_text": "string",
          "cta": "string"
        }
      ],
      "emails": [
        {
          "locale": "fr|en",
          "subject": "string",
          "preview": "string",
          "body": "string",
          "cta": "string"
        }
      ]
    },
    "source_skills": ["landing-page-copy", "ad-creative-copy", "launch-email-sequence"]
  }
}
```

Place under `data.explee_draft` in this skill's JSON (and mirror references from sibling content outputs when available). Downstream tools may import the draft; this spoke must not perform network writes.

## Output Schema

```json
{
    "skill": "ad-creative-copy",
    "cluster": "content",
    "wave": 6,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.1.0",
    "data": {
        "strategy": {
            "phases": ["pre-launch", "launch", "mid-campaign", "end-campaign"],
            "platforms": ["facebook", "instagram"],
            "formats": ["single_image", "carousel", "video", "stories"]
        },
        "hooks": {
            "problem_aware": ["string"],
            "solution_aware": ["string"],
            "social_proof": ["string"],
            "urgency": ["string"]
        },
        "pre_campaign_ads": [
            {
                "id": "string",
                "name": "string",
                "angle": "string",
                "headline": "string (40 chars max)",
                "body": "string (125 chars max)",
                "cta": "string"
            }
        ],
        "live_campaign_ads": [
            {
                "id": "string",
                "name": "string",
                "phase": "string",
                "angle": "string",
                "headline": "string",
                "body": "string",
                "cta": "string"
            }
        ],
        "locales": {
            "en": { "hooks": {}, "pre_campaign_ads": [], "live_campaign_ads": [] },
            "fr": { "hooks": {}, "pre_campaign_ads": [], "live_campaign_ads": [] }
        },
        "wiki_paths": {
            "en": "wiki/src/content/docs/en/marketing/ad-creative.md",
            "fr": "wiki/src/content/docs/fr/marketing/ad-creative.md"
        },
        "explee_draft": {
            "mode": "draft_only",
            "do_not_post": true,
            "targets": ["landing", "ads", "emails"],
            "locales": ["fr", "en"],
            "output_format": {}
        }
    }
}
```

## Quality Checklist

- [ ] 3+ pre-campaign ad variations
- [ ] 4+ live campaign ad variations
- [ ] Headlines under 40 characters
- [ ] Body copy under 125 characters
- [ ] Each phase has appropriate urgency
- [ ] Multiple hook angles covered
- [ ] CTAs match campaign goals
- [ ] If bilingual: `locales.en` and `locales.fr` complete; wiki paths documented
- [ ] `explee_draft` present with `do_not_post: true` (draft-only; no POST)
