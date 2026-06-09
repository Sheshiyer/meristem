---
name: brandmint-content-core
description: "Shared reference for the content cluster: copy frameworks, landing page structure, email sequence patterns, ad copy formulas, and content voice application."
cluster: brandmint-content
wave: 6
version: 1.0.0
---

# Brandmint Content Core

Shared reference for all content spokes. Wave 6 generates written content for all channels.

## The One Rule Everything Turns On

**Apply the voice matrix to everything.** Every piece of content must:
1. Reference `voice_and_tone.json` 
2. Apply context modifiers appropriately
3. Use the messaging framework pillars

## Inputs from Prior Waves

| Input | From | Used By |
|-------|------|---------|
| `voice_and_tone.json` | W2 | All content spokes |
| `messaging_framework.json` | W2 | All content spokes |
| `brand_story.json` | W2 | landing-page, brand-story-content |
| `buyer_persona.json` | W1 | Audience targeting |
| `product_positioning.json` | W2 | Value prop statements |

## Voice Application Rules

### Base Voice (from voice_and_tone.json)

```json
{
  "formality": 0.6,
  "enthusiasm": 0.7,
  "technicality": 0.5,
  "warmth": 0.6,
  "authority": 0.7
}
```

### Context Modifiers by Content Type

| Content Type | Formality | Enthusiasm | Technicality | Warmth |
|--------------|-----------|------------|--------------|--------|
| Homepage Hero | -0.1 | +0.2 | -0.1 | +0.1 |
| Feature Description | +0.0 | +0.0 | +0.2 | +0.0 |
| Testimonial | -0.2 | +0.1 | -0.2 | +0.2 |
| Email Welcome | -0.1 | +0.2 | -0.1 | +0.2 |
| Email Nurture | +0.0 | +0.1 | +0.1 | +0.1 |
| Ad Copy | -0.1 | +0.3 | -0.2 | +0.0 |
| Press Release | +0.3 | -0.1 | +0.1 | -0.2 |
| Legal/Compliance | +0.4 | -0.3 | +0.2 | -0.3 |

## Copy Frameworks

### PAS (Problem-Agitate-Solve)

```
PROBLEM: State the pain point
AGITATE: Amplify the consequences
SOLVE: Present your solution
```

Best for: Landing pages, emails, ads

### AIDA (Attention-Interest-Desire-Action)

```
ATTENTION: Hook with headline
INTEREST: Engage with benefits
DESIRE: Create want with proof
ACTION: Clear CTA
```

Best for: Landing pages, sales pages

### BAB (Before-After-Bridge)

```
BEFORE: Current painful state
AFTER: Desired future state
BRIDGE: Your product is the bridge
```

Best for: Email sequences, case studies

### 4Ps (Promise-Picture-Proof-Push)

```
PROMISE: Big claim/benefit
PICTURE: Paint the outcome
PROOF: Evidence/testimonials
PUSH: Urgency + CTA
```

Best for: Sales pages, ads

## Landing Page Structure

### Above the Fold (Hero Section)

```markdown
## [Headline - Primary benefit or transformation]

[Subheadline - How you deliver that benefit]

[CTA Button - Action-oriented, specific]

[Social Proof - Logos, stats, or testimonial snippet]
```

### Standard Page Flow

```
1. HERO
   - Headline (value prop)
   - Subheadline (how)
   - Primary CTA
   - Social proof bar

2. PROBLEM
   - Pain point statements
   - "Sound familiar?" validation

3. SOLUTION
   - Your approach
   - Key differentiators

4. FEATURES/BENEFITS
   - 3-6 key features
   - Benefit-focused headlines
   - Supporting details

5. SOCIAL PROOF
   - Testimonials (with photos)
   - Case study snippets
   - Metrics/results

6. HOW IT WORKS
   - 3-step process
   - Simple, clear

7. PRICING (if applicable)
   - Clear tiers
   - Feature comparison
   - Recommended tier highlighted

8. FAQ
   - Objection handling
   - Technical questions

9. FINAL CTA
   - Restate value
   - Urgency element
   - Clear action
```

## Email Sequence Patterns

### Welcome Sequence (5-7 emails)

| Email | Timing | Purpose | Framework |
|-------|--------|---------|-----------|
| 1 | Immediate | Welcome + Quick Win | Give value immediately |
| 2 | Day 1 | Story + Mission | Why you exist |
| 3 | Day 3 | Problem Deep-dive | PAS |
| 4 | Day 5 | Solution Overview | BAB |
| 5 | Day 7 | Social Proof | Case study |
| 6 | Day 10 | Soft CTA | Invitation |
| 7 | Day 14 | Direct CTA | Limited offer |

### Nurture Sequence (Ongoing)

```
Pattern: Value, Value, Value, Soft Ask

Email 1: Educational content
Email 2: Industry insight
Email 3: Tool/resource
Email 4: Soft product mention
[Repeat]
```

### Subject Line Formulas

| Type | Formula | Example |
|------|---------|---------|
| Question | "Are you still [struggling with X]?" | "Are you still losing leads?" |
| Number | "[Number] ways to [achieve X]" | "5 ways to close more deals" |
| How-to | "How to [achieve X] without [pain]" | "How to scale without burnout" |
| Curiosity | "The [X] mistake everyone makes" | "The pricing mistake everyone makes" |
| Personal | "Quick question about [X]" | "Quick question about your workflow" |

## Ad Copy Formulas

### Google Ads (Character Limits)

```
Headline 1 (30 chars): [Primary Keyword + Benefit]
Headline 2 (30 chars): [Differentiator or CTA]
Headline 3 (30 chars): [Social Proof or Urgency]
Description 1 (90 chars): [Expand on benefit + feature]
Description 2 (90 chars): [Address objection + CTA]
```

### LinkedIn Ads

```
Intro Text (150 chars for mobile):
[Hook - Pain point or question]
[Solution teaser]
[CTA]

Headline (70 chars):
[Benefit-focused, specific]
```

### Meta Ads (Facebook/Instagram)

```
Primary Text (125 chars visible):
[Hook in first line]
[Benefit]
[CTA]

Headline (40 chars):
[Clear value prop]
```

## Output Schemas

### landing-page-copy.json

```json
{
  "skill": "landing-page-copy",
  "cluster": "content",
  "wave": 6,
  "data": {
    "page_type": "homepage",
    "sections": {
      "hero": {
        "headline": "...",
        "subheadline": "...",
        "cta_text": "...",
        "cta_url": "/signup"
      },
      "problem": {
        "headline": "...",
        "pain_points": ["...", "..."]
      },
      "solution": { ... },
      "features": [ ... ],
      "testimonials": [ ... ],
      "faq": [ ... ],
      "final_cta": { ... }
    },
    "meta": {
      "title": "...",
      "description": "...",
      "og_title": "...",
      "og_description": "..."
    }
  }
}
```

### email-sequences.json

```json
{
  "skill": "email-sequences",
  "cluster": "content",
  "wave": 6,
  "data": {
    "sequences": {
      "welcome": {
        "emails": [
          {
            "number": 1,
            "subject": "...",
            "preview_text": "...",
            "body": "...",
            "cta": { ... },
            "send_delay": "immediate"
          }
        ]
      },
      "nurture": { ... },
      "onboarding": { ... }
    }
  }
}
```

### ad-copy.json

```json
{
  "skill": "ad-copy",
  "cluster": "content",
  "wave": 6,
  "data": {
    "platforms": {
      "google": {
        "campaigns": [
          {
            "name": "Brand Awareness",
            "ad_groups": [
              {
                "name": "Main Keywords",
                "ads": [
                  {
                    "headlines": ["...", "...", "..."],
                    "descriptions": ["...", "..."]
                  }
                ]
              }
            ]
          }
        ]
      },
      "linkedin": { ... },
      "meta": { ... }
    }
  }
}
```

## Quality Gates

| Check | Requirement |
|-------|-------------|
| Voice applied | Matches voice_and_tone.json |
| Messaging used | References framework pillars |
| Character limits | Ad copy within limits |
| CTAs clear | Every section has next step |
| SEO meta | Title/description present |

## Content Variants

Each content piece should have variants for:

| Variant | Purpose |
|---------|---------|
| A/B versions | Testing different approaches |
| Persona-specific | Tailored to buyer type |
| Funnel stage | TOFU/MOFU/BOFU appropriate |

## Dependencies for Wave 7

Content cluster outputs feed directly into synthesis:

| Output | Used By (Wave 7) |
|--------|------------------|
| landing-page-copy | wiki-site-generator |
| email-sequences | brand-documentation |
| ad-copy | deliverables-package |
| press-release | notebooklm-publishing |
