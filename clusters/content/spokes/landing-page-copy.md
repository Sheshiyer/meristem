---
name: landing-page-copy
description: "Create high-converting landing page copy including hero headline, product pitch, key features, and CTAs. Uses structured templates with emotional resonance for buyer persona."
cluster: brandmint-content
wave: 6
dependencies:
  - voice-and-tone
  - product-positioning
  - buyer-persona
  - messaging-framework
triggers:
  - "landing page"
  - "sales page"
  - "homepage copy"
  - "hero section"
---

# Landing Page Copy Skill

Create comprehensive landing page copy that makes the buyer persona feel understood.

## Prerequisites

Load upstream outputs:
- `voice-and-tone.json` — for voice prompt template
- `product-positioning.json` — for CBBE framework answers
- `buyer-persona.json` — for emotional drivers and challenges
- `messaging-framework.json` — for value pillars and tagline

## Core Principle

> The goal of great writing is for the reader to understand.  
> The goal of GREAT COPY is for the prospect to feel understood.

## Process

### Step 1: Hero Section

**Hero Headline (8-14 words)**
Formula: `[Product Name]: [Unique benefit] [How it's different]`

Example: "GameGuardian: The Ultimate, Customizable Board Game Backpack Designed for Gamers"

**Product Pitch (30-40 words)**
Include:
- Product name
- What it does
- How it does it differently
- Emotional benefit

**CTA Button**
- Action verb + benefit
- Example: "Get Your Exclusive Discount"

### Step 2: Key Features (5-8 sections)

Use ONE of these templates per feature:

**Template 1: Feature → Mechanism → Benefit → Differentiator**
```
[Feature] [How does feature work?] [What does the feature do?] [How does it do it differently?]
```
Example: "4 layers of insulation keeps the heat inside and makes sure your hands are always toasty and warm, even in the coldest climates."

**Template 2: Benefit → Differentiator → Feature → Mechanism**
```
[What does the feature do?] [How does it do it differently?] [Feature] [How does feature work?]
```
Example: "Store TONS of games and never run out of space with Odo's modular design. Start with one set of shelves then build on it as your board game collection grows!"

**Template 3: Problem → Solution**
```
[Status quo/Problem]. [Product/Feature] [Benefit].
```
Example: "Stacking games on top of each other damages the boxes. Odo Shelves is designed to store your games flat and secure."

**Template 4: Specifics → Benefit**
```
[Feature specifics] [Functional, emotional, or self-expressive benefit]
```
Example: "Lomi holds up to 2.5L of food waste which is enough for a family of four."

**Template 5: Emotional → Action**
```
[Emotional appeal]. [Self-expressive action made possible by product feature].
```
Example: "Your board games give you hours of fun and build cherished memories with friends and family. Display them proudly and protect them from wear."

### Step 3: Feature Headlines

Each feature needs:
- **Headline** (2-10 words)
- **Body** (1-2 sentences, max 42 words)

Structure each feature section:
```
#N Key Feature Headline - [Feature Name]
"[Catchy Headline]"
[Body copy using one of the templates above]
```

### Step 4: Social Proof Section

Include placeholders for:
- Customer testimonials (3-5)
- Review quotes
- Trust badges
- Media mentions

### Step 5: FAQ Section

Address potential objections from buyer persona:
- Price/value questions
- Feature comparisons
- Shipping/warranty
- Use case questions

### Step 6: Final CTA Section

Repeat the main offer with urgency:
- Restate key benefit
- Limited time/quantity (if applicable)
- Clear CTA button

## Voice Application

Apply the voice prompt template from `voice-and-tone.json` to all copy:
- Use the three tones consistently
- Echo the voice character (fellow enthusiast, expert, etc.)
- Use domain-specific language
- Engage emotional drivers

## Bilingual FR + EN (additive)

When `market.region: FR` **or** `locales` includes `fr`, emit **both** language variants. JSON remains the primary wave output; wiki markdown is a planned secondary emit for synthesis.

**Planned wiki paths (document; do not invent live site):**
- `wiki/src/content/docs/en/marketing/landing-page.md`
- `wiki/src/content/docs/fr/marketing/landing-page.md`

Rules:
- `data` holds the default/primary locale copy (prefer `fr` when `defaultLocale: fr`).
- `data.locales.en` and `data.locales.fr` each contain the full landing structure (hero, features, social_proof, faq, final_cta).
- Non-bilingual brands omit `locales` and keep the existing single-locale schema.

## Output Schema

```json
{
    "skill": "landing-page-copy",
    "cluster": "content",
    "wave": 6,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.1.0",
    "data": {
        "hero": {
            "headline": "string (8-14 words)",
            "product_pitch": "string (30-40 words)",
            "cta_button": "string"
        },
        "features": [
            {
                "name": "string",
                "headline": "string (2-10 words)",
                "body": "string (max 42 words)",
                "template_used": "1|2|3|4|5"
            }
        ],
        "social_proof": {
            "testimonials": ["string"],
            "trust_badges": ["string"],
            "media_mentions": ["string"]
        },
        "faq": [
            {
                "question": "string",
                "answer": "string"
            }
        ],
        "final_cta": {
            "headline": "string",
            "body": "string",
            "button": "string"
        },
        "locales": {
            "en": { "hero": {}, "features": [], "social_proof": {}, "faq": [], "final_cta": {} },
            "fr": { "hero": {}, "features": [], "social_proof": {}, "faq": [], "final_cta": {} }
        },
        "wiki_paths": {
            "en": "wiki/src/content/docs/en/marketing/landing-page.md",
            "fr": "wiki/src/content/docs/fr/marketing/landing-page.md"
        }
    }
}
```

## Quality Checklist

- [ ] Hero headline is 8-14 words
- [ ] Product pitch is 30-40 words
- [ ] Each feature body is max 42 words
- [ ] 5-8 features included
- [ ] Voice prompt template applied consistently
- [ ] Emotional drivers from buyer persona addressed
- [ ] At least 3 FAQs address potential objections
- [ ] CTAs use action verbs
- [ ] No generic superlatives without proof
- [ ] If bilingual: both `locales.en` and `locales.fr` complete; wiki paths documented
