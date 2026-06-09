---
name: welcome-email-sequence
description: "Create post-purchase welcome email sequence for onboarding and relationship building. 3-5 emails for new customers."
cluster: brandmint-content
wave: 6
dependencies:
  - voice-and-tone
  - brand-story
  - buyer-persona
triggers:
  - "welcome emails"
  - "onboarding emails"
  - "post-purchase"
  - "customer welcome"
---

# Welcome Email Sequence Skill

Create email sequence for new customers after purchase/backing.

## Prerequisites

Load upstream outputs:
- `voice-and-tone.json` — for email voice
- `brand-story.json` — for founder connection
- `buyer-persona.json` — for customer needs

## Process

### Step 1: Welcome Sequence Goals

**Objectives:**
1. Confirm purchase and build excitement
2. Introduce the brand/founder
3. Set expectations for next steps
4. Build community connection
5. Encourage social sharing

**Timing:**
- Email 1: Immediately after purchase
- Email 2: 2-3 days later
- Email 3: 1 week later
- Email 4: 2 weeks later (if long fulfillment)
- Email 5: Pre-delivery or delivery day

### Step 2: Email Sequence Outline

**Email 1: Thank You + Confirmation**
- Goal: Confirm purchase, express gratitude
- Content: Order details, what happens next, gratitude
- Tone: Warm, excited, appreciative

**Email 2: Meet the Founder**
- Goal: Personal connection
- Content: Founder story, why they built this, mission
- Tone: Personal, authentic, passionate

**Email 3: Community Welcome**
- Goal: Build belonging
- Content: Join social channels, community highlights, how to share
- Tone: Inclusive, welcoming

**Email 4: Behind the Scenes (if applicable)**
- Goal: Keep engaged during wait
- Content: Production updates, process insights
- Tone: Transparent, exciting

**Email 5: Delivery Excitement**
- Goal: Build anticipation for arrival
- Content: What to expect, unboxing tips, how to share
- Tone: Excited, helpful

### Step 3: Write Each Email

For each email, include:
- Subject line (+ 2 variations)
- Preview text
- Full body copy
- CTA (social, share, etc.)
- P.S. line

### Step 4: Relationship Tone

Welcome emails should feel like:
- A friend excited to share something
- Not a transaction, but a relationship
- Warm and personal, not corporate
- Grateful without being obsequious

## Output Schema

```json
{
    "skill": "welcome-email-sequence",
    "cluster": "content",
    "wave": 6,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "sequence_strategy": {
            "goals": ["string"],
            "timing": "string",
            "total_emails": "number"
        },
        "emails": [
            {
                "number": "number",
                "name": "string",
                "send_timing": "string",
                "goal": "string",
                "tone": "string",
                "subject_lines": {
                    "primary": "string",
                    "variation_a": "string",
                    "variation_b": "string"
                },
                "preview_text": "string",
                "body": "string (full email)",
                "cta": {
                    "text": "string",
                    "action": "string"
                },
                "ps": "string"
            }
        ]
    }
}
```

## Quality Checklist

- [ ] 3-5 emails in sequence
- [ ] First email sent immediately
- [ ] Founder story included
- [ ] Community/social links provided
- [ ] Tone is warm and personal
- [ ] Expectations set for delivery
- [ ] Opportunities to share/engage
