---
name: voice-and-tone
description: "Define brand voice characteristics and tone variations for different contexts. Creates a voice prompt template that can be used across all marketing materials."
cluster: brandmint-strategy
wave: 2
dependencies:
  - buyer-persona
  - product-positioning
triggers:
  - "voice and tone"
  - "brand voice"
  - "how should we speak"
  - "messaging tone"
---

# Voice and Tone Skill

Create a comprehensive voice and tone guide based on the buyer persona and product positioning.

## Prerequisites

Load upstream outputs:
- `buyer-persona.json` — for emotional drivers and psychographics
- `product-positioning.json` — for brand values and resonance

## Process

### Step 1: Extract Voice Attributes

From the buyer persona and positioning, identify three core voice attributes:

**Tone Selection Criteria:**
- Tone should match how the target persona communicates
- Tone should reflect the brand's values
- Tone should differentiate from competitors

Common tone combinations by category:
| Category | Typical Tones |
|----------|---------------|
| B2B Tech | Professional, Knowledgeable, Confident |
| Consumer Lifestyle | Friendly, Enthusiastic, Relatable |
| Premium/Luxury | Sophisticated, Authoritative, Refined |
| Health/Wellness | Empathetic, Trustworthy, Encouraging |
| Gaming/Hobby | Enthusiastic, Knowledgeable, Playful |

### Step 2: Define Voice Character

Answer these questions:
1. **Who is the brand speaking as?** (fellow enthusiast, expert advisor, trusted friend, professional guide)
2. **What relationship do we have with the customer?** (peer, mentor, partner, service provider)
3. **What language register?** (casual, conversational, formal, technical)

### Step 3: Create Voice Prompt Template

Generate a reusable voice prompt using this structure:

```
Please craft marketing copy that uses a [tone1], [tone2], and [tone3] tone, 
echoing the voice of a fellow [identity]. 

This voice should reflect a deep understanding of the [culture/community] culture, 
use [domain-specific] language, and convey genuine excitement about [topic/interest]. 

It should also display empathy towards the unique challenges [audience] face, 
offering solutions that resonate with their specific needs and aspirations. 

The copy should engage emotionally, acknowledging the sense of [emotion1], [emotion2], 
[emotion3], and [emotion4] a dedicated [audience type] seeks. 

Remember to make it sound like a conversation between friends, highlighting that 
our brand shares their interests, understands their struggles, and is committed 
to enhancing their [experience type] experience.
```

### Step 4: Define Tone Variations

Create context-specific tone adjustments:

| Context | Tone Adjustment | Example |
|---------|-----------------|---------|
| **Announcement** | More excited, celebratory | "We're thrilled to introduce..." |
| **Support** | More empathetic, patient | "We understand how frustrating..." |
| **Education** | More authoritative, clear | "Here's exactly how it works..." |
| **Crisis** | More serious, reassuring | "We take this seriously and..." |
| **Sales** | More confident, benefit-focused | "Transform your experience with..." |

### Step 5: Language Guidelines

Document specific language preferences:

**Use:**
- Active voice
- Second person ("you", "your")
- Concrete, specific language
- [Domain-specific terminology]

**Avoid:**
- Passive voice
- Corporate jargon
- Superlatives without proof
- Generic phrases ("best-in-class", "world-leading")

**Vocabulary Bank:**
- Words to use: [list 10-15 on-brand words]
- Words to avoid: [list 5-10 off-brand words]

## Output Schema

```json
{
    "skill": "voice-and-tone",
    "cluster": "strategy",
    "wave": 2,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "voice_attributes": {
            "tone1": "string",
            "tone2": "string", 
            "tone3": "string"
        },
        "voice_character": {
            "speaking_as": "string",
            "relationship": "string",
            "language_register": "string"
        },
        "voice_prompt_template": "string",
        "tone_variations": {
            "announcement": {
                "adjustment": "string",
                "example": "string"
            },
            "support": {
                "adjustment": "string",
                "example": "string"
            },
            "education": {
                "adjustment": "string",
                "example": "string"
            },
            "crisis": {
                "adjustment": "string",
                "example": "string"
            },
            "sales": {
                "adjustment": "string",
                "example": "string"
            }
        },
        "language_guidelines": {
            "use": ["string"],
            "avoid": ["string"],
            "vocabulary_bank": {
                "preferred": ["string"],
                "prohibited": ["string"]
            }
        }
    }
}
```

## Quality Checklist

- [ ] Three distinct, non-overlapping tones selected
- [ ] Voice character clearly defined
- [ ] Voice prompt template is reusable across contexts
- [ ] At least 5 tone variations documented
- [ ] Language guidelines are specific and actionable
- [ ] Vocabulary bank reflects buyer persona language
- [ ] Examples demonstrate voice in action
