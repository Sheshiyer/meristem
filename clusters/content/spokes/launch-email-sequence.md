---
name: launch-email-sequence
description: "Create campaign launch email sequence for crowdfunding or product launch. 5-7 emails covering launch day through campaign end."
cluster: brandmint-content
wave: 6
dependencies:
  - voice-and-tone
  - product-positioning
  - messaging-framework
  - landing-page-copy
triggers:
  - "launch emails"
  - "campaign emails"
  - "crowdfunding emails"
  - "launch sequence"
---

# Launch Email Sequence Skill

Create email sequence for the active campaign/launch period.

## Prerequisites

Load upstream outputs:
- `voice-and-tone.json` — for email voice
- `product-positioning.json` — for key messages
- `messaging-framework.json` — for value pillars
- `landing-page-copy.json` — for consistent messaging

## Process

### Step 1: Launch Sequence Strategy

**Goals of launch sequence:**
1. Drive immediate action on launch day
2. Address objections over time
3. Create urgency at key milestones
4. Celebrate progress (social proof)
5. Close strong at campaign end

**Timing (for typical 30-day campaign):**
- Email 1: Launch day
- Email 2: Day 2-3 (momentum)
- Email 3: Day 7 (first week recap)
- Email 4: Mid-campaign (new angle)
- Email 5: 72 hours left
- Email 6: 24 hours left
- Email 7: Final hours

### Step 2: Email Purpose Map

| Email | Timing | Primary Lever | Secondary |
|-------|--------|---------------|-----------|
| Launch | Day 1 | Excitement | Early-bird |
| Momentum | Day 2-3 | Social proof | Features |
| Week 1 | Day 7 | Progress | New content |
| Mid | Day 15 | Value deeper dive | Testimonials |
| 72hr | Day 27 | Urgency | Scarcity |
| 24hr | Day 29 | FOMO | Last chance |
| Final | Day 30 | Deadline | No regrets |

### Step 3: Email Templates

**Launch Day Email:**
```
Subject: [Excitement + product name]
Preview: [The moment is here]

[Enthusiastic opening - we're live!]
[Brief reminder of what this is]
[Key benefit #1]
[Early-bird offer details]
[Clear CTA: Back now]
[P.S.: Early-bird ends in X hours]
```

**Urgency Email (72hr/24hr):**
```
Subject: [Time-based urgency]
Preview: [Specific deadline]

[Acknowledge the deadline]
[Quick recap of value]
[What they'll miss if they don't act]
[Social proof if available]
[CTA: Don't miss out]
[P.S.: Exact end time]
```

### Step 4: Write Full Sequence

For each email:
- 3 subject line variations
- Preview text
- Full body copy
- CTA button text
- P.S. line

### Step 5: Urgency Calibration

**Urgency levels by email:**
| Email | Urgency Level | Language |
|-------|---------------|----------|
| Launch | Medium | "Now available" |
| Day 2-3 | Low | "Momentum building" |
| Week 1 | Low | "Making progress" |
| Mid | Medium | "Halfway there" |
| 72hr | High | "Only 3 days left" |
| 24hr | Very High | "Ends tomorrow" |
| Final | Maximum | "Last chance - hours left" |

## Bilingual FR + EN (additive)

When `market.region: FR` **or** `locales` includes `fr`, emit both language variants. JSON remains the primary wave output.

**Planned wiki paths:**
- `wiki/src/content/docs/en/marketing/launch-email-sequence.md`
- `wiki/src/content/docs/fr/marketing/launch-email-sequence.md`

Rules:
- `data.emails` = default/primary locale sequence (prefer `fr` when `defaultLocale: fr`).
- `data.locales.en.emails` / `data.locales.fr.emails` = full parallel sequences.
- Align subjects/CTAs with `ad-creative-copy` `explee_draft.emails` when that draft is present (draft-only; no POST).

## Output Schema

```json
{
    "skill": "launch-email-sequence",
    "cluster": "content",
    "wave": 6,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.1.0",
    "data": {
        "sequence_strategy": {
            "campaign_length": "string (e.g., '30 days')",
            "total_emails": "number",
            "goals": ["string"]
        },
        "emails": [
            {
                "number": "number",
                "name": "string",
                "send_timing": "string (e.g., 'Day 1')",
                "primary_lever": "string",
                "urgency_level": "low|medium|high|maximum",
                "subject_lines": {
                    "primary": "string",
                    "variation_a": "string",
                    "variation_b": "string"
                },
                "preview_text": "string",
                "body": "string (full email)",
                "cta": {
                    "text": "string",
                    "url_placeholder": "string"
                },
                "ps": "string"
            }
        ],
        "locales": {
            "en": { "emails": [] },
            "fr": { "emails": [] }
        },
        "wiki_paths": {
            "en": "wiki/src/content/docs/en/marketing/launch-email-sequence.md",
            "fr": "wiki/src/content/docs/fr/marketing/launch-email-sequence.md"
        }
    }
}
```

## Quality Checklist

- [ ] 5-7 emails covering full campaign
- [ ] Launch day email is highest energy
- [ ] Urgency increases appropriately
- [ ] Each email has distinct purpose
- [ ] Social proof included where relevant
- [ ] Final emails have maximum urgency
- [ ] All CTAs link to campaign page
- [ ] If bilingual: both locale sequences complete; wiki paths documented
