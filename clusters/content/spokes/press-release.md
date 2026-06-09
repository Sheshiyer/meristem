---
name: press-release
description: "Create media-ready press release announcing the product launch. Follows standard PR format with quotes, boilerplate, and media contact."
cluster: brandmint-content
wave: 6
dependencies:
  - brand-foundation
  - product-positioning
  - messaging-framework
  - brand-story
triggers:
  - "press release"
  - "PR"
  - "media announcement"
  - "launch announcement"
---

# Press Release Skill

Create a professional press release for product launch announcement.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for company background
- `product-positioning.json` — for key messages
- `messaging-framework.json` — for headlines and proof points
- `brand-story.json` — for founder quotes

## Process

### Step 1: Press Release Structure

Standard PR format:
1. **FOR IMMEDIATE RELEASE** (or embargo date)
2. **Headline** — Newsworthy, factual
3. **Subheadline** — Supporting detail
4. **Dateline** — City, Date
5. **Lead paragraph** — Who, What, When, Where, Why
6. **Body paragraphs** — Details, features, benefits
7. **Quote 1** — Founder/CEO perspective
8. **Supporting details** — Specs, availability, pricing
9. **Quote 2** — Industry expert or customer (if available)
10. **Boilerplate** — About the company
11. **Media contact** — Name, email, phone

### Step 2: Headline Writing

**Press release headlines should be:**
- Factual, not promotional
- Newsworthy (what's the story?)
- Include company/product name
- Active voice

**Formula:**
`[Company] Launches [Product], [Key Differentiator/Benefit]`

**Examples:**
- "GameGuardian Launches First Modular Board Game Backpack for Serious Gamers"
- "New Board Game Backpack Solves Transport Problem for Gaming Enthusiasts"

### Step 3: Lead Paragraph (5 W's)

Answer in first paragraph:
- **Who:** Company name
- **What:** Product being launched
- **When:** Launch date
- **Where:** Where available (Kickstarter, website, etc.)
- **Why:** Why this matters / problem solved

### Step 4: Body Content

**Paragraph 2:** Product details and key features
**Paragraph 3:** Target audience and use cases
**Paragraph 4:** Competitive differentiation
**Paragraph 5:** Availability, pricing, timeline

### Step 5: Quotes

**Quote 1 (Founder):**
- Personal connection to the problem
- Vision for the product
- Passion and mission

**Quote 2 (External, if available):**
- Industry validation
- Customer testimonial
- Expert endorsement

### Step 6: Boilerplate

Standard "About [Company]" paragraph:
- What the company does
- Mission/vision
- Key differentiator
- Website URL

## Output Schema

```json
{
    "skill": "press-release",
    "cluster": "content",
    "wave": 6,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "release_type": "FOR IMMEDIATE RELEASE|EMBARGOED UNTIL [date]",
        "headline": "string",
        "subheadline": "string",
        "dateline": {
            "city": "string",
            "date": "string"
        },
        "lead_paragraph": "string (answers 5 W's)",
        "body_paragraphs": [
            {
                "topic": "string",
                "content": "string"
            }
        ],
        "quotes": [
            {
                "speaker": "string",
                "title": "string",
                "quote": "string"
            }
        ],
        "product_details": {
            "availability": "string",
            "pricing": "string",
            "launch_date": "string",
            "where_to_buy": "string"
        },
        "boilerplate": "string (About [Company])",
        "media_contact": {
            "name": "string",
            "title": "string",
            "email": "string",
            "phone": "string"
        },
        "full_release": "string (complete formatted press release)"
    }
}
```

## Quality Checklist

- [ ] Headline is newsworthy, not promotional
- [ ] Lead paragraph answers all 5 W's
- [ ] At least one founder quote included
- [ ] Boilerplate is professional and concise
- [ ] Media contact information complete
- [ ] Product details clearly stated
- [ ] Follows standard PR format
- [ ] Can be sent to media as-is
