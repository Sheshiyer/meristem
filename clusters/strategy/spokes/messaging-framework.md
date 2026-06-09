---
name: messaging-framework
description: "Create hierarchical messaging structure — tagline, elevator pitch, value pillars, and proof points. Provides copy building blocks for all marketing materials."
cluster: brandmint-strategy
wave: 2
dependencies:
  - voice-and-tone
  - product-positioning
  - value-proposition
triggers:
  - "messaging framework"
  - "tagline"
  - "elevator pitch"
  - "value pillars"
  - "key messages"
---

# Messaging Framework Skill

Create a structured messaging hierarchy that provides copy building blocks for all marketing materials.

## Prerequisites

Load upstream outputs:
- `voice-and-tone.json` — for tone and language guidelines
- `product-positioning.json` — for CBBE framework answers
- `value-proposition.json` — for value hierarchy

## Process

### Step 1: Tagline

**What is a tagline?**
The shortest possible expression of the brand promise. Memorable, distinctive, timeless.

**Guidelines:**
- 2-7 words
- No product features
- Emotionally resonant
- Works across all contexts

**Types of taglines:**
| Type | Example |
|------|---------|
| Imperative | "Just Do It" (Nike) |
| Descriptive | "The Ultimate Driving Machine" (BMW) |
| Provocative | "Think Different" (Apple) |
| Superlative | "The Best a Man Can Get" (Gillette) |
| Clever | "Every Kiss Begins with Kay" (Kay Jewelers) |

**Generate 5 options, select 1.**

### Step 2: Elevator Pitch

**What is an elevator pitch?**
30-second explanation of what you do and why it matters.

**Structure:**
```
[Target audience] struggle with [problem].
[Product name] is a [category] that [key benefit].
Unlike [alternatives], we [differentiator].
[Proof point or credential].
```

**Word count:** 50-75 words

### Step 3: Value Pillars (3-5)

**What are value pillars?**
The core themes that all messaging ladders up to. Each pillar represents a key reason to believe.

**Structure per pillar:**
```
Pillar Name: [2-4 words]
Headline: [8-12 words]
Supporting copy: [25-40 words]
Proof points: [2-3 specific claims]
```

**Guidelines:**
- 3-5 pillars total
- Each pillar should be distinct (no overlap)
- Each pillar must have proof
- Pillars should map to buyer persona needs

### Step 4: Message Matrix

Create variations for different contexts:

| Context | Primary Message | Tone Adjustment |
|---------|-----------------|-----------------|
| Social media | Short, punchy | Casual |
| Email subject | Curiosity-driven | Direct |
| Landing page | Benefit-focused | Confident |
| Press release | Newsworthy | Professional |
| Sales conversation | Problem-solution | Consultative |

### Step 5: Proof Points Bank

Compile all provable claims:

**Types of proof:**
- Statistics (numbers, percentages)
- Testimonials (customer quotes)
- Credentials (awards, certifications)
- Demonstrations (before/after, comparisons)
- Guarantees (warranties, promises)

## Output Schema

```json
{
    "skill": "messaging-framework",
    "cluster": "strategy",
    "wave": 2,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "tagline": {
            "selected": "string (2-7 words)",
            "type": "imperative|descriptive|provocative|superlative|clever",
            "alternatives": ["string (4 more options)"]
        },
        "elevator_pitch": {
            "full": "string (50-75 words)",
            "components": {
                "problem": "string",
                "solution": "string",
                "differentiator": "string",
                "proof": "string"
            }
        },
        "value_pillars": [
            {
                "name": "string (2-4 words)",
                "headline": "string (8-12 words)",
                "supporting_copy": "string (25-40 words)",
                "proof_points": ["string"]
            }
        ],
        "message_matrix": {
            "social_media": {
                "message": "string",
                "tone": "string"
            },
            "email_subject": {
                "message": "string",
                "tone": "string"
            },
            "landing_page": {
                "message": "string",
                "tone": "string"
            },
            "press_release": {
                "message": "string",
                "tone": "string"
            },
            "sales": {
                "message": "string",
                "tone": "string"
            }
        },
        "proof_points": {
            "statistics": ["string"],
            "testimonials": ["string"],
            "credentials": ["string"],
            "demonstrations": ["string"],
            "guarantees": ["string"]
        }
    }
}
```

## Quality Checklist

- [ ] Tagline is 2-7 words
- [ ] Elevator pitch is 50-75 words
- [ ] 3-5 value pillars, each with proof points
- [ ] No overlap between pillars
- [ ] Message matrix covers all 5 contexts
- [ ] At least 2 proof points per category
- [ ] All messages align with voice-and-tone
