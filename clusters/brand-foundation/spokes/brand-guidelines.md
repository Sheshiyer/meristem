---
name: brand-guidelines
description: "Synthesize all brand outputs into a single source-of-truth brand guidelines document. Combines foundation, strategy, identity outputs into one navigable reference. Ported from brandmint-oracle-aleph."
cluster: brandmint-foundation
wave: 1
dependencies:
  - brand-foundation
  - voice-and-tone
  - visual-language
triggers:
  - "brand guidelines"
  - "brand bible"
  - "single source of truth"
  - "brand reference"
---

# Brand Guidelines Skill

Synthesize all brand outputs into a single source-of-truth document that the studio team, partners, and future operators can reference.

## Prerequisites

- `brand-foundation.json` — name, mission, values, personality
- `voice-and-tone.json` — vocabulary, prohibited terms, channel calibration
- `messaging-framework.json` — key messages, value pillars
- `product-positioning.json` — differentiators, CBBE
- `buyer-persona.json` — audience definition
- `visual-language.json` — visual principles, photography, illustration
- `color-palette.json` — palette + usage
- `typography.json` — typefaces + hierarchy
- `logo-concept.json` — logo system + usage specs

## Process

### Step 1: Sections to Include

A complete brand-guidelines document has these sections:

1. **Brand at a Glance** — name, headline, tagline, promise, CTA, category
2. **Mission & Values** — mission statement, 3-5 values with definitions
3. **Brand Personality** — archetype, adjectives, if-a-person description
4. **Voice & Tone** — voice matrix, tone variations by context, vocabulary bank
5. **Visual Identity** — logo system, palette, typography, photography style
6. **Messaging** — key messages, value pillars, elevator pitches
7. **Positioning** — differentiators, points of difference/parity, observable outcome
8. **Audience** — primary persona summary, secondary persona summary
9. **What We Don't Do** — prohibited terms, forbidden visual elements

### Step 2: Audience-Specific Versions

Brand guidelines can be rendered in three versions:
- **Internal operator version** — full detail, all variants, troubleshooting
- **Partner version** — focused on voice and visual rules
- **Public reference** — high-level only, no internal methodology

### Step 3: Validation

- All data points traceable to source JSON outputs
- No invented copy or claims
- Voice discipline preserved (no prohibited terms)
- Visual references point to verified asset paths

## Output Schema

```json
{
    "skill": "brand-guidelines",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "document_title": "string",
        "sections": [
            {
                "section_number": "number",
                "title": "string",
                "content": "string",
                "source_outputs": ["string"]
            }
        ],
        "render_versions": [
            {"version": "internal|partner|public", "audience": "string", "scope": "string"}
        ],
        "source_outputs_used": ["string"],
        "voice_compliance": "PASS"
    }
}
```

## Quality Checklist

- [ ] All required sections present
- [ ] Each section traces to a source JSON output
- [ ] Voice discipline preserved throughout
- [ ] Three render versions documented
- [ ] No invented content — everything grounded in source