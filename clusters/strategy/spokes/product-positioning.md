---
name: product-positioning
description: "Create comprehensive product positioning using the CBBE framework. Synthesizes buyer persona insights into a positioning summary for all marketing materials."
cluster: brandmint-strategy
wave: 2
dependencies:
  - brand-foundation
  - buyer-persona
  - competitor-analysis
triggers:
  - "product positioning"
  - "CBBE framework"
  - "how are we positioned"
  - "market position"
---

# Product Positioning Skill

Create a comprehensive product positioning summary using the Consumer-Based Brand Equity (CBBE) framework.

## Prerequisites

Load upstream outputs:
- `buyer-persona.json` — for CBBE framework answers
- `competitor-analysis.json` — for differentiation points
- `brand-foundation.json` — for mission and values

## Core Principle

> The underlying principle of the CBBE framework: you do not own your brand — consumers do. 
> It's a concept that lives rent-free in their minds. 
> For that reason, we approach product positioning as if we are the consumer.

## Process

### Step 1: Salience — "Who are you?"

If your brand has salience, consumers know who you are and what problem you solve.

**Questions to answer:**
1. What product category are you in?
2. What problem do you solve?
3. What is your product in one sentence?

**Guidelines:**
- Use words consumers recognize
- Associate with a category they understand
- Don't overthink — simplicity wins

**Bad:** "The quad-layer, super warm, hand insulator"
**Good:** "The best damn mittens ever"

### Step 2: Performance — "What are you?"

Where consumers understand what makes you different from competition.

**Questions to answer:**
1. What makes you different from competition? (Points of Difference)
2. What makes you similar to competition? (Points of Parity)
3. What are the core features? How valuable is each?

**Goal:** Identify 3 main points of difference.

### Step 3: Imagery — "What do I associate with you?"

When someone hears your brand name, what comes to mind?

**Questions to answer:**
1. What established brands would you associate with your product?
2. Where is your product used?
3. How is your product used?

**Example:** William Painter sunglasses → NASA association → "These NASA-Inspired Sunglasses Are Made Of Aerospace-Grade Titanium"

### Step 4: Judgments — "How good are you?"

Consumers evaluate your performance and imagery to form opinions.

**Questions to answer:**
1. What positive judgments will people have?
2. What concerns or doubts may people have?
3. What credibility do you have in the market?

**Critical:** Address concerns directly in messaging.

### Step 5: Feelings — "How do you make me feel?"

The emotional connection with your brand.

**Questions to answer:**
1. How do you want people to feel when using your product?
2. What is the voice of your message? (friend, teacher, expert?)
3. What is the tone? (funny, somber, optimistic, epic, friendly?)

### Step 6: Resonance — "What about you and me?"

Why the consumer will have a loyal, active relationship with your brand.

**Questions to answer:**
1. Why would you be missed if you disappeared?
2. How is your mission aligned with the customer's mission?
3. What are your core values?
4. Why will customers only choose you?

## Output Schema

```json
{
    "skill": "product-positioning",
    "cluster": "strategy",
    "wave": 2,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "cbbe": {
            "salience": {
                "product_category": "string",
                "problem_solved": "string",
                "one_sentence": "string"
            },
            "performance": {
                "points_of_difference": ["string (3 items)"],
                "points_of_parity": ["string"],
                "core_features": [
                    {
                        "feature": "string",
                        "value_level": "high|medium|table_stakes"
                    }
                ]
            },
            "imagery": {
                "brand_associations": ["string"],
                "usage_locations": ["string"],
                "usage_methods": ["string"]
            },
            "judgments": {
                "positive_judgments": ["string"],
                "concerns_doubts": ["string"],
                "credibility": "string",
                "concern_responses": [
                    {
                        "concern": "string",
                        "response": "string"
                    }
                ]
            },
            "feelings": {
                "desired_feelings": ["string"],
                "voice": "string",
                "tone": "string"
            },
            "resonance": {
                "why_missed": "string",
                "mission_alignment": "string",
                "core_values": ["string"],
                "why_choose_us": "string"
            }
        },
        "positioning_summary": "string (comprehensive narrative)"
    }
}
```

## Quality Checklist

- [ ] Salience uses simple, recognizable category language
- [ ] Exactly 3 points of difference identified
- [ ] Brand associations reference real, known brands
- [ ] All concerns have documented responses
- [ ] Voice and tone are specific (not generic)
- [ ] Resonance explains emotional loyalty drivers
- [ ] Summary is comprehensive enough to brief a copywriter
