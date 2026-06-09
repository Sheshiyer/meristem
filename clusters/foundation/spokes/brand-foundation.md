---
name: brand-foundation
description: "Define core brand identity elements — mission, vision, values, brand essence, and personality traits. The foundational document that all other brand work builds upon."
cluster: brandmint-foundation
wave: 1
dependencies: []
triggers:
  - "brand foundation"
  - "mission vision values"
  - "brand identity"
  - "who are we"
---

# Brand Foundation Skill

Create the foundational brand identity document that establishes who the brand is at its core.

## Prerequisites

Load brand config:
- `brand-config.yaml` — for product name, category, description

## Process

### Step 1: Mission Statement

**What is a mission?**
The mission is WHY the brand exists — the problem it solves and for whom.

**Format:** One sentence, present tense, action-oriented.

**Template:**
```
[Brand] exists to [action verb] [target audience] [achieve outcome] by [how we do it differently].
```

**Examples:**
- "Tesla's mission is to accelerate the world's transition to sustainable energy."
- "Patagonia exists to save our home planet."
- "GameGuardian exists to enhance the gaming experience by providing secure, stylish solutions for board game transportation."

**Quality check:**
- Is it one sentence?
- Does it include an action verb?
- Is it specific enough to guide decisions?
- Is it inspiring without being generic?

### Step 2: Vision Statement

**What is a vision?**
The vision is WHERE the brand is going — the future state it's working toward.

**Format:** One sentence, future-oriented, aspirational but achievable.

**Template:**
```
A world where [target audience] [experience/achieve] [ideal outcome].
```

**Examples:**
- "A world where every gamer can transport their collection with pride and confidence."
- "A future where sustainable fashion is the only fashion."

### Step 3: Core Values (3-5)

**What are values?**
Values are HOW the brand operates — the non-negotiable principles that guide behavior.

**Requirements:**
- 3-5 values (not more)
- Each value must be actionable (not generic like "quality" or "excellence")
- Each value needs a definition and behavioral example

**Format per value:**
```
**[Value Name]**
Definition: [What this means to us]
In practice: [How this shows up in our work]
```

**Bad values (too generic):**
- Quality, Excellence, Integrity, Innovation, Customer-first

**Good values (specific and actionable):**
- "Obsessive organization" — We believe every game piece deserves a dedicated home
- "Built by gamers" — We only make products we'd use ourselves
- "Function over flash" — We prioritize utility, but never sacrifice style

### Step 4: Brand Essence

**What is brand essence?**
The single word or short phrase that captures the brand's soul.

**Format:** 1-3 words maximum.

**Examples:**
- Nike: "Authentic athletic performance"
- Disney: "Magical family entertainment"
- GameGuardian: "Gaming preparedness"

**Process:**
1. List 10 words that describe the brand
2. Group into themes
3. Find the intersection of themes
4. Distill to essence

### Step 5: Brand Personality Traits

Define the brand as if it were a person:

**Trait categories:**
- **Archetype**: Which of the 12 brand archetypes? (Hero, Outlaw, Magician, Everyman, Lover, Jester, Caregiver, Ruler, Creator, Innocent, Sage, Explorer)
- **If the brand were a person**: Age, occupation, hobbies, communication style
- **Adjectives**: 5 words that describe the brand's personality

## Output Schema

```json
{
    "skill": "brand-foundation",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "mission": {
            "statement": "string (one sentence)",
            "breakdown": {
                "action": "string",
                "audience": "string",
                "outcome": "string",
                "differentiator": "string"
            }
        },
        "vision": {
            "statement": "string (one sentence)",
            "time_horizon": "string (e.g., '5 years', '10 years')"
        },
        "values": [
            {
                "name": "string",
                "definition": "string",
                "in_practice": "string"
            }
        ],
        "brand_essence": "string (1-3 words)",
        "personality": {
            "archetype": "string",
            "if_a_person": {
                "age": "string",
                "occupation": "string",
                "hobbies": ["string"],
                "communication_style": "string"
            },
            "adjectives": ["string"]
        }
    }
}
```

## Quality Checklist

- [ ] Mission is one sentence with action verb
- [ ] Vision is future-oriented and aspirational
- [ ] 3-5 values, each with definition and practice example
- [ ] No generic values (quality, excellence, integrity)
- [ ] Brand essence is 1-3 words
- [ ] Archetype selected with rationale
- [ ] 5 personality adjectives listed
