---
name: buyer-persona
description: "Create detailed buyer persona profiles using the CBBE framework. Includes demographics, psychographics, challenges, emotional drivers, and the 6 CBBE sections (Salience, Performance, Imagery, Judgments, Feelings, Resonance)."
cluster: brandmint-foundation
wave: 1
dependencies:
  - brand-foundation
triggers:
  - "buyer persona"
  - "target audience"
  - "who is the customer"
  - "ideal customer profile"
  - "ICP"
---

# Buyer Persona Skill

Create a comprehensive buyer persona using the Consumer-Based Brand Equity (CBBE) framework.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for brand context, product category, core values

## Process

### Step 1: Demographics Foundation

Define concrete demographics:
- **Name**: Give the persona a memorable name (e.g., "Boardgame Brandon")
- **Age**: Specific age, not a range
- **Gender**: If relevant to product
- **Education**: Degree level
- **Income**: Specific bracket
- **Location**: Urban/suburban/rural, region if relevant
- **Occupation**: Job title and industry

### Step 1b: FR Energy-Subsidy Depth — Marie Durand (additive)

Only when the evidenced brand domain is French CEE / energy-subsidy operations, deepen the primary persona with the following dimensions. **Marie Durand** is an illustrative persona label, not a verified customer. French locale alone does not trigger this domain-specific section. Use supplied persona evidence; do not invent interview findings.

**Market-role clarity (obligé vs délégataire):**
- Document whether Marie works for an **obligé** (energy supplier with CEE obligation) or a **délégataire** (entity that takes on / manages obligation volumes and dossier flows), or a hybrid ESCo/aggregator serving both.
- Capture how that role changes buying criteria: audit exposure, volume peaks, PNCEE rule changes, relationship to installers vs prime contractors.

**PNCEE literacy:**
- Reference the **PNCEE** (Pôle National des Certificats d'Économies d'Énergie) as the institutional context for rule interpretation, controls, and dossier scrutiny.
- Include at least one challenge tied to PNCEE/CEE documentation consistency (attestations, invoices, technical sheets, photos).

**LinkedIn FR job-title coverage:**
Include realistic French LinkedIn titles in demographics / targeting hooks, e.g.:
- Responsable Back-Office CEE
- Responsable Conformité / Compliance CEE
- Chef de projet CEE / Primes Énergie
- Responsable Opérations Dossiers
- Directeur / Directrice des Opérations (ESCO / délégataire)
- Chargé(e) de validation dossiers
- Responsable Qualité & Audit réglementaire

Emit domain-specific schema fields only when the evidenced French CEE gate fires:
- `data.fr_market_role`: `"obligé" | "délégataire" | "hybrid" | "esco_aggregator"`
- `data.pncee_context`: short string
- `data.linkedin_fr_titles`: string[]

### Step 2: Psychographics Deep Dive

Explore the inner world:
- **Identity**: How do they see themselves? What role does this product category play in their identity?
- **Values**: What do they prioritize in life?
- **Lifestyle**: How do they spend time outside work?
- **Aspirations**: What are they working toward?
- **Community**: Who do they associate with?

### Step 3: Challenges and Pain Points

Document specific frustrations with current solutions:
- List 3-5 specific challenges
- Include direct quotes (hypothetical but realistic)
- Explain why existing solutions fail them

Example format:
> "[Current solution] that [specific failure]: '[Direct quote expressing frustration]'"

### Step 4: Emotional Drivers

**Positive emotions sought** (what they want to feel):
- Pride
- Relief
- Satisfaction
- Anticipation
- Admiration from peers

**Negative emotions to avoid** (what they don't want):
- Frustration
- Embarrassment
- Anxiety
- Regret
- Wasted effort

### Step 5: CBBE Framework Application

For each section, answer the consumer's implicit question:

#### Salience ("Who are you?")
- What product category are you in?
- What problem do you solve?
- In one sentence, what is your product?

#### Performance ("What are you?")
- What makes you different from competition? (Points of Difference)
- What do you share with competition? (Points of Parity)
- What are your core features and their value?

#### Imagery ("What do I associate with you?")
- What established brands would you associate with?
- Where is the product used?
- How is the product used?

#### Judgments ("How good are you?")
- What positive judgments will people have?
- What concerns or doubts may they have?
- What credibility do you have in this market?

#### Feelings ("How do you make me feel?")
- How should people feel when using the product?
- What is the voice of your messaging? (friend, expert, teacher?)
- What is the tone? (enthusiastic, professional, playful?)

#### Resonance ("What about you and me?")
- Why would you be missed if you disappeared?
- How does your mission align with the customer's mission?
- What are your core values?
- Why will customers choose only you?

## Output Schema

```json
{
    "skill": "buyer-persona",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "persona_name": "string",
        "demographics": {
            "age": "number",
            "gender": "string|null",
            "education": "string",
            "income": "string",
            "location": "string",
            "occupation": "string"
        },
        "psychographics": {
            "identity": "string",
            "values": ["string"],
            "lifestyle": "string",
            "aspirations": "string",
            "community": "string"
        },
        "challenges": [
            {
                "challenge": "string",
                "current_solution": "string",
                "why_it_fails": "string",
                "quote": "string"
            }
        ],
        "emotional_drivers": {
            "positive": ["string"],
            "negative": ["string"]
        },
        "cbbe": {
            "salience": {
                "product_category": "string",
                "problem_solved": "string",
                "one_sentence": "string"
            },
            "performance": {
                "points_of_difference": ["string"],
                "points_of_parity": ["string"],
                "core_features": ["string"]
            },
            "imagery": {
                "associated_brands": ["string"],
                "usage_locations": ["string"],
                "usage_methods": ["string"]
            },
            "judgments": {
                "positive": ["string"],
                "concerns": ["string"],
                "credibility": "string"
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
        "fr_market_role": "obligé|délégataire|hybrid|esco_aggregator (optional; required for evidenced French CEE domain)",
        "pncee_context": "string (optional)",
        "linkedin_fr_titles": ["string (optional; FR LinkedIn titles)"]
    }
}
```

## Quality Checklist

- [ ] Persona has a memorable, specific name
- [ ] Demographics are concrete (no ranges)
- [ ] At least 3 challenges with quotes
- [ ] Both positive and negative emotional drivers included
- [ ] All 6 CBBE sections completed
- [ ] Language reflects how the persona would actually speak
- [ ] Challenges reference real pain points, not assumed ones
- [ ] If the evidenced domain is French CEE: the sourced persona (or labelled illustrative persona) covers obligé vs délégataire, PNCEE context, and LinkedIn FR titles
