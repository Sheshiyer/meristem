---
name: value-proposition
description: "Synthesize brand foundation, buyer persona, and competitor analysis into a clear, compelling value proposition statement."
cluster: brandmint-foundation
wave: 1
dependencies:
  - brand-foundation
  - buyer-persona
  - competitor-analysis
triggers:
  - "value proposition"
  - "why should they buy"
  - "unique value"
  - "what makes us different"
---

# Value Proposition Skill

Create the core value proposition that answers "Why should our target customer choose us?"

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for mission, values, essence
- `buyer-persona.json` — for pain points and emotional drivers
- `competitor-analysis.json` — for differentiation and whitespace

## Process

### Step 1: Pain-Gain Mapping

From buyer persona, list:

**Pains (problems to solve):**
- Functional pains (what doesn't work)
- Emotional pains (how it makes them feel)
- Social pains (how others perceive them)

**Gains (outcomes desired):**
- Functional gains (what they want to achieve)
- Emotional gains (how they want to feel)
- Social gains (how they want to be perceived)

### Step 2: Value Proposition Canvas

Map product features to customer jobs:

| Customer Job | Pain Point | Our Solution | Gain Created |
|--------------|------------|--------------|--------------|
| [task] | [frustration] | [feature] | [outcome] |

### Step 3: Differentiation Check

For each value we claim, verify:
- Is this genuinely different from competitors?
- Can we prove this claim?
- Does the customer actually care about this?

**The value proposition should NOT include:**
- Claims competitors can also make
- Features without benefits
- Benefits without proof

### Step 4: Value Proposition Statement

**Format 1: Classic Template**
```
For [target customer]
Who [has this problem/need]
Our [product] is a [category]
That [key benefit]
Unlike [competitors]
We [key differentiator]
```

**Format 2: One-Sentence**
```
[Product] helps [target customer] [achieve outcome] by [unique mechanism], 
unlike [alternatives] which [limitation].
```

**Format 3: Headlines (for marketing)**
- Primary headline (8-14 words)
- Supporting subheadline (15-25 words)
- Proof point (one specific claim)

### Step 5: Value Hierarchy

Rank value propositions by importance:

1. **Primary value** — The #1 reason to buy
2. **Secondary values** — Supporting reasons (2-3)
3. **Table stakes** — Expected but not differentiating

## Output Schema

```json
{
    "skill": "value-proposition",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "pain_gain_map": {
            "pains": {
                "functional": ["string"],
                "emotional": ["string"],
                "social": ["string"]
            },
            "gains": {
                "functional": ["string"],
                "emotional": ["string"],
                "social": ["string"]
            }
        },
        "value_canvas": [
            {
                "customer_job": "string",
                "pain_point": "string",
                "solution": "string",
                "gain_created": "string"
            }
        ],
        "statements": {
            "classic": "string (full template)",
            "one_sentence": "string",
            "headlines": {
                "primary": "string (8-14 words)",
                "subheadline": "string (15-25 words)",
                "proof_point": "string"
            }
        },
        "value_hierarchy": {
            "primary": {
                "value": "string",
                "why_it_matters": "string",
                "proof": "string"
            },
            "secondary": [
                {
                    "value": "string",
                    "why_it_matters": "string"
                }
            ],
            "table_stakes": ["string"]
        }
    }
}
```

## Quality Checklist

- [ ] Pain points reference buyer persona challenges by name
- [ ] Value proposition differentiates from competitors explicitly
- [ ] One-sentence statement is under 30 words
- [ ] Primary headline is 8-14 words
- [ ] Primary value is genuinely unique (not "better quality")
- [ ] All claims have proof points or can be demonstrated
- [ ] Table stakes are identified (not claimed as differentiators)
