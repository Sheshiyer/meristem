---
name: brand-story
description: "Craft the brand narrative — origin story, founder's journey, brand mythology, and customer transformation story. Provides emotional foundation for all storytelling."
cluster: brandmint-strategy
wave: 2
dependencies:
  - brand-foundation
  - buyer-persona
  - product-positioning
  - voice-and-tone
triggers:
  - "brand story"
  - "origin story"
  - "our story"
  - "why we started"
  - "brand narrative"
---

# Brand Story Skill

Craft the brand narrative that creates emotional connection and provides storytelling foundation.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for mission, vision, values
- `buyer-persona.json` — for customer journey
- `product-positioning.json` — for resonance section
- `voice-and-tone.json` — for narrative voice

## Process

### Step 1: Origin Story

**The Founder's Journey**

Every brand has an origin. Craft the story of how and why the brand came to be.

**Story arc:**
1. **The Before** — What was life like before? What problem did the founder experience?
2. **The Inciting Incident** — What moment sparked the idea?
3. **The Struggle** — What obstacles were overcome?
4. **The Breakthrough** — How was the solution discovered?
5. **The Mission** — What drives the brand today?

**Guidelines:**
- Be specific (dates, places, details)
- Show vulnerability (struggles humanize)
- Connect founder's problem to customer's problem
- End with forward momentum

### Step 2: Brand Mythology

**The Deeper Meaning**

Beyond the literal origin, what archetypal story does the brand embody?

**Common brand archetypes:**
| Archetype | Story Pattern | Example |
|-----------|---------------|---------|
| Hero | Overcoming obstacles | Nike |
| Outlaw | Breaking rules | Harley-Davidson |
| Magician | Transformation | Disney |
| Everyman | Belonging | IKEA |
| Caregiver | Nurturing | Johnson & Johnson |
| Creator | Innovation | Apple |
| Sage | Wisdom | Google |
| Explorer | Discovery | Patagonia |

**Questions:**
- What is the brand's "enemy" or antagonist?
- What is the "promised land" the brand leads customers to?
- What transformation does the brand enable?

### Step 3: Customer Transformation Story

**The Hero's Journey (Customer Version)**

The customer is the hero. The brand is the guide.

**Structure (StoryBrand framework):**
1. **A character** — The customer (from buyer persona)
2. **Has a problem** — External, internal, and philosophical
3. **Meets a guide** — The brand (with empathy + authority)
4. **Who gives them a plan** — Simple steps to success
5. **Calls them to action** — Clear CTA
6. **That helps them avoid failure** — Stakes of inaction
7. **And ends in success** — The transformation achieved

### Step 4: Key Story Moments

**Moments to script:**
- **The Ah-Ha Moment** — When the customer realizes they need this
- **The First Experience** — Unboxing, first use, first win
- **The Transformation** — Before/after comparison
- **The Advocacy** — Why they tell others

### Step 5: Story Formats

Package the narrative for different uses:

| Format | Length | Use Case |
|--------|--------|----------|
| One-liner | 15 words | Social bio, elevator intro |
| Paragraph | 50-75 words | About page intro |
| Short story | 150-200 words | Press kit, investor deck |
| Full narrative | 500+ words | Blog post, video script |

## Output Schema

```json
{
    "skill": "brand-story",
    "cluster": "strategy",
    "wave": 2,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "origin_story": {
            "the_before": "string",
            "inciting_incident": "string",
            "the_struggle": "string",
            "the_breakthrough": "string",
            "the_mission": "string",
            "full_narrative": "string (500+ words)"
        },
        "brand_mythology": {
            "archetype": "string",
            "enemy": "string",
            "promised_land": "string",
            "transformation_enabled": "string"
        },
        "customer_transformation": {
            "character": "string (from persona)",
            "problem": {
                "external": "string",
                "internal": "string",
                "philosophical": "string"
            },
            "guide": {
                "empathy_statement": "string",
                "authority_statement": "string"
            },
            "plan": ["string (3 steps)"],
            "call_to_action": "string",
            "failure_avoided": "string",
            "success_achieved": "string"
        },
        "key_moments": {
            "ah_ha_moment": "string",
            "first_experience": "string",
            "transformation": "string",
            "advocacy": "string"
        },
        "story_formats": {
            "one_liner": "string (15 words)",
            "paragraph": "string (50-75 words)",
            "short_story": "string (150-200 words)",
            "full_narrative": "string (500+ words)"
        }
    }
}
```

## Quality Checklist

- [ ] Origin story has specific details (not generic)
- [ ] Brand archetype selected with rationale
- [ ] Customer transformation follows StoryBrand 7-step framework
- [ ] Problem has external, internal, AND philosophical dimensions
- [ ] All 4 story formats created
- [ ] Stories align with voice-and-tone
- [ ] Customer is the hero, brand is the guide
