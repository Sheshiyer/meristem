---
name: prelaunch-email-sequence
description: "Create pre-campaign email sequence to build anticipation and collect leads before launch. 3-5 emails for the pre-launch phase."
cluster: brandmint-content
wave: 6
dependencies:
  - voice-and-tone
  - product-positioning
  - buyer-persona
  - brand-story
triggers:
  - "prelaunch emails"
  - "pre-campaign emails"
  - "build anticipation"
  - "lead nurture"
---

# Prelaunch Email Sequence Skill

Create an email sequence that builds anticipation before product launch.

## Prerequisites

Load upstream outputs:
- `voice-and-tone.json` — for email voice
- `product-positioning.json` — for key messages
- `buyer-persona.json` — for pain points to address
- `brand-story.json` — for narrative elements

## Process

### Step 1: Sequence Strategy

**Goals of prelaunch sequence:**
1. Build email list
2. Create anticipation
3. Educate about the problem
4. Establish credibility
5. Prime for launch day action

**Timing:**
- Email 1: Immediately after signup
- Email 2: 2-3 days later
- Email 3: 5-7 days later
- Email 4: 1-2 days before launch
- Email 5: Launch day countdown

### Step 2: Email Framework

Each email follows this structure:

| Element | Purpose | Guidelines |
|---------|---------|------------|
| **Subject** | Open the email | Under 50 chars, curiosity/benefit |
| **Preview** | Support subject | 35-90 chars, adds context |
| **Hook** | Keep reading | First line captures attention |
| **Body** | Deliver value | One main idea per email |
| **CTA** | Drive action | Single, clear next step |
| **P.S.** | Second chance | Restate offer or add urgency |

### Step 3: Email Sequence Outline

**Email 1: Welcome + Promise**
- Subject: [Curiosity about what's coming]
- Goal: Confirm signup, set expectations
- Content: What they'll get, when to expect launch

**Email 2: Problem Agitation**
- Subject: [Relate to their pain]
- Goal: Connect with their frustration
- Content: Deep dive into the problem, validate their struggle

**Email 3: Solution Tease**
- Subject: [Hint at the solution]
- Goal: Build curiosity about the product
- Content: Reveal the approach without full product reveal

**Email 4: Social Proof / Credibility**
- Subject: [Why trust us]
- Goal: Establish authority
- Content: Founder story, testimonials, credentials

**Email 5: Launch Countdown**
- Subject: [Urgency + specific timing]
- Goal: Create anticipation for launch
- Content: Exact launch time, what to expect, early-bird teaser

### Step 4: Write Each Email

Apply voice-and-tone template to all copy:
- Use the brand voice consistently
- Match the emotional tone to the email purpose
- Use buyer persona language

### Step 5: Subject Line Variations

For each email, create 3 subject line options:
- Option A: Curiosity-based
- Option B: Benefit-based
- Option C: Urgency/FOMO-based

## Output Schema

```json
{
    "skill": "prelaunch-email-sequence",
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
                "name": "string (e.g., 'Welcome + Promise')",
                "send_timing": "string",
                "goal": "string",
                "subject_lines": {
                    "primary": "string",
                    "curiosity": "string",
                    "benefit": "string",
                    "urgency": "string"
                },
                "preview_text": "string",
                "hook": "string (first line)",
                "body": "string (full email body)",
                "cta": {
                    "text": "string",
                    "url_placeholder": "string"
                },
                "ps": "string"
            }
        ]
    }
}
```

## Quality Checklist

- [ ] 3-5 emails in sequence
- [ ] Each email has single clear goal
- [ ] Subject lines under 50 characters
- [ ] 3+ subject line variations per email
- [ ] Voice matches brand tone
- [ ] Clear CTA in each email
- [ ] Sequence builds logically to launch
