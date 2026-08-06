# Brandmint Skill Execution: icon-system

## Cluster: illustration

## Core Reference

---
name: brandmint-illustration-core
description: "Shared reference for the illustration cluster: GPT-Image-2 illustration prompting, icon systems, pattern libraries, and brand illustration guidelines."
cluster: brandmint-illustration
wave: 5
version: 1.0.0
---

# Brandmint Illustration Core

Shared reference for all illustration spokes. Wave 5 generates illustrative assets.

## The One Rule Everything Turns On

**Consistency is everything.** All illustrations must share:
- Same style
- Same stroke weight
- Same color usage
- Same level of detail

## Visual Generation Constraint

**GPT-Image-2 only.** No FAL, no Replicate, no Midjourney.

```bash
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$prompt" \
    --out "$brand_dir/generated/$filename"
```

## Inputs from Prior Waves

| Input | From | Used By |
|-------|------|---------|
| `visual_language.json` | W3 | All illustration spokes |
| `color_palette.json` | W3 | Color usage |
| `brand_foundation.json` | W1 | Subject matter |

## Illustration Style Framework

### Style Categories

| Style | Characteristics | Best For |
|-------|-----------------|----------|
| Flat | Solid colors, no gradients, minimal shadows | Tech, Modern |
| Line Art | Outlines only, varying stroke weights | Minimal, Editorial |
| 3D | Depth, shadows, perspective | Playful, Premium |
| Hand-drawn | Organic, imperfect, sketchy | Creative, Approachable |
| Geometric | Shapes, patterns, mathematical | Abstract, Tech |
| Isometric | 3D perspective, consistent angle | Data, Process |

### Style Consistency Rules

Once a style is chosen, ALL illustrations must:

```yaml
line_art_rules:
  stroke_weight: "2px standard, 1px details"
  corners: "rounded (2px radius)"
  fills: "optional, brand colors only"
  shadows: "none"
  
flat_rules:
  fills: "solid colors from palette"
  outlines: "none or 1px darker shade"
  shadows: "flat offset shadow only"
  gradients: "none"
  
geometric_rules:
  shapes: "circles, squares, triangles only"
  angles: "45° or 90° only"
  colors: "max 3 from palette"
```

## GPT-Image-2 Illustration Prompts

### Prompt Structure

```
[STYLE] illustration of [SUBJECT], [COLOR SCHEME], [COMPOSITION],
[DETAIL LEVEL], [BACKGROUND], vector style, clean lines
```

### Style Keywords by Category

| Style | Prompt Keywords |
|-------|-----------------|
| Flat | "flat design, solid colors, no gradients, minimal, vector" |
| Line Art | "line art, outline illustration, single weight stroke, minimal" |
| 3D | "3D illustration, soft shadows, depth, modern 3D render" |
| Hand-drawn | "hand-drawn style, sketch, organic lines, imperfect" |
| Geometric | "geometric shapes, abstract, mathematical, pattern-based" |
| Isometric | "isometric illustration, 30-degree angle, technical" |

### Color Instructions

```
# Limited palette (recommended)
"using only [primary], [secondary], and [accent] colors"

# Monochrome
"monochromatic [color] illustration with tints and shades"

# Full palette
"brand color palette with [primary] as dominant color"
```

## Icon System Guidelines

### Grid System

```
Base: 24x24px
Scales: 16, 24, 32, 48, 64

┌──────────────────────┐
│  ┌──────────────┐   │  2px padding
│  │              │   │
│  │    ICON      │   │  20x20 live area
│  │    AREA      │   │
│  │              │   │
│  └──────────────┘   │
└──────────────────────┘
```

### Icon Categories

| Category | Examples | Style Notes |
|----------|----------|-------------|
| Navigation | Home, Menu, Back | Simple, recognizable |
| Actions | Edit, Delete, Add | Clear affordance |
| Objects | File, Folder, User | Consistent metaphors |
| Status | Success, Warning, Info | Color-coded |
| Social | Share, Like, Comment | Platform-neutral |

### Icon Prompt Template

```
Simple [style] icon of [object/concept],
[stroke weight]px stroke, [corner style] corners,
[color] on transparent background,
24x24 pixel grid, centered, minimal detail
```

## Pattern Library

### Pattern Types

| Type | Use Case | Prompt Keywords |
|------|----------|-----------------|
| Geometric | Backgrounds, cards | "repeating geometric pattern" |
| Organic | Textures, overlays | "organic flowing pattern" |
| Abstract | Hero sections | "abstract brand pattern" |
| Illustrative | Feature sections | "illustrated scene pattern" |

### Pattern Rules

```yaml
pattern_guidelines:
  seamless: true  # Must tile seamlessly
  scale: "works at 50% and 200%"
  color_variants:
    - "primary on white"
    - "white on primary"
    - "accent on dark"
  opacity: "10-20% for backgrounds"
```

## Output Schemas

### brand-illustrations.json

```json
{
  "skill": "brand-illustrations",
  "cluster": "illustration",
  "wave": 5,
  "data": {
    "style_guide": {
      "style": "flat",
      "stroke_weight": null,
      "corner_radius": null,
      "shadow_style": "flat-offset",
      "color_usage": "limited-palette"
    },
    "illustrations": [
      {
        "id": "illust-hero-01",
        "concept": "Team collaboration",
        "prompt_used": "...",
        "generated_path": "./generated/illust-hero-01.png",
        "usage": ["homepage-hero", "about-section"],
        "dimensions": "1200x800"
      }
    ]
  }
}
```

### icon-system.json

```json
{
  "skill": "icon-system",
  "cluster": "illustration",
  "wave": 5,
  "data": {
    "style": {
      "type": "line-art",
      "stroke_weight": "2px",
      "corners": "rounded-2px",
      "grid": "24x24"
    },
    "icons": [
      {
        "id": "icon-dashboard",
        "name": "Dashboard",
        "category": "navigation",
        "prompt_used": "...",
        "generated_path": "./generated/icons/dashboard.png",
        "sizes": [16, 24, 32]
      }
    ],
    "icon_font": {
      "generated": false,
      "format": "svg-sprite"
    }
  }
}
```

### pattern-library.json

```json
{
  "skill": "pattern-library",
  "cluster": "illustration",
  "wave": 5,
  "data": {
    "patterns": [
      {
        "id": "pattern-geo-01",
        "name": "Geometric Grid",
        "type": "geometric",
        "prompt_used": "...",
        "generated_path": "./generated/patterns/geo-01.png",
        "seamless": true,
        "color_variants": [
          "./generated/patterns/geo-01-light.png",
          "./generated/patterns/geo-01-dark.png"
        ],
        "usage": ["card-backgrounds", "section-dividers"]
      }
    ]
  }
}
```

## Generated Assets (Wave 5)

| Asset | Count | Path Pattern |
|-------|-------|--------------|
| Brand illustrations | 3-5 | `generated/illust-*.png` |
| Icons | 10-20 | `generated/icons/*.png` |
| Patterns | 2-3 | `generated/patterns/*.png` |

## Quality Gates

| Check | Requirement |
|-------|-------------|
| Style consistency | All same style/weight |
| Color compliance | Only palette colors used |
| Grid alignment | Icons on 24px grid |
| Pattern seamless | Tiles without visible seams |

## Asset Manifest Integration

Every generated illustration must be registered:

```json
{
  "id": "illust-hero-01",
  "path": "./generated/illust-hero-01.png",
  "type": "illustration",
  "exists": true,
  "deterministic": false,
  "wave": 5,
  "skill": "brand-illustrations",
  "model": "gpt-image-2",
  "style": "flat"
}
```

## Common Illustration Mistakes

| Mistake | Fix |
|---------|-----|
| Inconsistent style | Lock style before generating |
| Too much detail | Simplify, match brand complexity |
| Wrong colors | Always reference palette explicitly |
| Icons not centered | Specify "centered in frame" |
| Patterns don't tile | Add "seamless, tileable" to prompt |

## Skill Instructions

---
name: icon-system
description: "Generate brand icon system — UI icons, feature icons, category icons. Consistent style across all iconography."
cluster: brandmint-illustration
wave: 5
dependencies:
  - visual-language
  - color-palette
triggers:
  - "icons"
  - "icon set"
  - "feature icons"
  - "UI icons"
---

# Icon System Skill

Create a comprehensive, consistent icon system for the brand.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for iconography specifications
- `color-palette.json` — for icon colors

## Process

### Step 1: Icon Style Definition

From visual-language, establish icon rules:

| Parameter | Specification |
|-----------|---------------|
| **Style** | Line / Filled / Duotone |
| **Stroke weight** | Xpx |
| **Corner radius** | Sharp / Xpx radius |
| **Grid size** | Xpx base grid |
| **Padding** | X% of canvas |
| **Line caps** | Round / Square / Butt |
| **Line joins** | Round / Miter / Bevel |

### Step 2: Icon Categories

Define icons needed by category:

**UI Icons (Navigation/Actions):**
- Menu, Close, Search, Settings
- Arrow variants (up, down, left, right)
- Plus, Minus, Check, X
- User, Cart, Heart, Share

**Feature Icons (Product Benefits):**
- [Feature 1 icon]
- [Feature 2 icon]
- [Feature 3 icon]
- [Feature 4 icon]

**Category Icons (Sections/Topics):**
- [Category 1]
- [Category 2]
- [Category 3]

### Step 3: Icon Inventory

| ID | Category | Name | Concept | Priority |
|----|----------|------|---------|----------|
| IC-01 | Feature | [name] | [what it represents] | High |
| IC-02 | Feature | [name] | [what it represents] | High |
| IC-03 | UI | [name] | [standard meaning] | Medium |

### Step 4: Generate Prompts

**Template for icons:**
```
Minimalist icon representing [concept] for [brand name].

Style: [Line/Filled/Duotone] icon
Stroke: [X]px weight, [round/square] caps
Corners: [sharp/rounded]
Colors: [primary color] on transparent background
[For duotone]: Primary [color 1], secondary [color 2]

Simple, recognizable, scalable from 16px to 96px.
Single concept, no text, centered on canvas.
Vector-style, clean geometry.
Square format, icon only.
```

### Step 5: Size Variants

For each icon, generate at standard sizes:
- 16px — Inline, small UI
- 24px — Default UI
- 32px — Medium emphasis
- 48px — Feature sections
- 64px — Large feature
- 96px — Hero/decorative

### Step 6: Export Specifications

**Formats needed:**
- SVG (scalable, web)
- PNG @1x, @2x, @3x (apps)
- Icon font (if applicable)

## Output Schema

```json
{
    "skill": "icon-system",
    "cluster": "illustration",
    "wave": 5,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "style_definition": {
            "type": "line|filled|duotone",
            "stroke_weight": "string",
            "corner_radius": "string",
            "grid_size": "string",
            "padding": "string",
            "line_caps": "string",
            "line_joins": "string",
            "colors": {
                "primary": "string",
                "secondary": "string"
            }
        },
        "categories": {
            "ui": ["string (icon names)"],
            "feature": ["string (icon names)"],
            "category": ["string (icon names)"]
        },
        "icons": [
            {
                "id": "string",
                "category": "string",
                "name": "string",
                "concept": "string",
                "priority": "high|medium|low",
                "generation_prompt": "string",
                "generated_path": "string",
                "sizes": ["16", "24", "32", "48", "64", "96"]
            }
        ],
        "export_formats": ["svg", "png"],
        "generation_summary": {
            "total_icons": "number",
            "generated": "number",
            "pending": "number"
        }
    }
}
```

## Quality Checklist

- [ ] Style definition matches visual-language specs
- [ ] All feature icons defined
- [ ] Common UI icons included
- [ ] Consistent style across all icons
- [ ] All icons work at 16px (legibility check)
- [ ] Colors limited to brand palette
- [ ] Export formats specified

## Brand Context

```yaml
# Brandmint v2 — Thoughtseed brand configuration
# Source corpus: website/thoughtseed-2026/.planning/ (brand-source, brief, logos, generated-assets)
# Studio: founder-led systems studio, requirement-to-handoff delivery.
# NOTE: The Krebs Cycle of Creativity / consciousness layer is BACKSTAGE only — never public copy.

brand:
  name: "Thoughtseed"
  slug: "thoughtseed"
  tagline: "We plant ideas. They grow wild."
  category: "technology" # founder-led systems studio / creative technology
  market:
    b2b: true
    b2c: false
    enterprise: true   # mid-market & innovation teams, not heavy procurement
    smb: true          # funded startups to scaleups

company:
  description: |
    Thoughtseed is a founder-led systems studio that turns complex requirements into
    coherent technology systems by aligning user psychology, founder operating logic,
    interface design, engineering delivery, and structured handoff inside one delivery
    loop. It carries framing, behavior, product, execution, and ownership transfer
    together instead of splitting them across disconnected vendors.
  founding_year: 2020
  stage: "growth"
  problem: |
    Important work gets split across strategy, design, engineering, and operations
    vendors who do not share one model of the problem. That fragmentation destroys
    coherence before the work ships and makes ownership harder after delivery. The
    founder becomes the full-time translator between five specialists.
  solution: |
    One studio that studies the requirement, the user, and the founder's operating
    reality, then designs, builds, and hands back a system the client can run, extend,
    and inherit. Psychology-aware framing stays grounded in engineering; handoff is a
    first-class output, not post-project admin.

audience:
  primary:
    title: "The System-Carrying Founder (founder / CTO / innovation lead / product strategist)"
    company_size: "Lean senior teams; funded startups through scaleups"
    industry: "AI & automation, product, web/mobile, IoT, creative technology"
    pain_points:
      - "Too many vendors each understand only one slice of the problem"
      - "Strategy decks get disconnected from shipped product reality"
      - "AI proposals are technically shallow or operationally naive"
      - "The system works on launch day but falls apart at ownership transfer"
    goals:
      - "Solve an important problem without becoming the full-time vendor translator"
      - "One studio that understands requirement, user, and operating reality"
      - "Receive a system that can be run internally after delivery"
  secondary:
    title: "Innovation team / technical operator needing one coherent partner"
    company_size: "Scaleup to enterprise innovation units"
    pain_points:
      - "Orchestrating separate strategy, design, engineering, and handoff vendors"
      - "Coherence and accountability lost across handoffs"

competitors:
  direct:
    - name: "Large innovation consultancies"
      positioning: "Process packaging, enterprise credibility, procurement comfort"
      weakness: "Weak on intimacy, velocity, and ownership clarity from concept to handoff"
    - name: "Premium product design agencies"
      positioning: "Polish, interface craft, presentation quality"
      weakness: "Weaker on engineering ownership, AI integration, operational handoff rigor"
    - name: "AI integration consultancies"
      positioning: "Current tooling and efficiency narratives"
      weakness: "Weak on narrative, product experience, founder workflow, durable brand memory"
  indirect:
    - name: "Specialized engineering vendors"
      positioning: "Narrow technical execution"
      weakness: "Weak when requirement, behavior, interface, and system must align"
    - name: "Freelancer swarms"
      positioning: "Flexibility, low overhead"
      weakness: "Client becomes the integrator; accountability and coherence break down"

personality:
  traits:
    - "cross-disciplinary"
    - "founder-led"
    - "precise"
    - "editorial"
    - "grounded"
  voice:
    formality: 0.55      # crafted, not stiff
    enthusiasm: 0.4      # calm over loud
    technicality: 0.6    # real systems language, no jargon theater
    warmth: 0.5          # human, founder-close, not salesy
  archetypes:
    primary: "sage"      # clarity, truth, coherence
    secondary: "creator" # builds systems that can be inherited

visual_preferences:
  color_mood: "cool"               # deep blue-black anchor, teal signal, warm orange ignition
  photography_style: "editorial"   # editorial-documentary, tactile materials, prototyping spaces
  illustration_style: "geometric"  # geometric systems diagrams blended with organic signal patterns
  preferred_colors:
    - "#1A237E"  # Deep Quantum Blue — anchor, long-horizon trust
    - "#00897B"  # Consciousness Teal — primary accent, directional signal
    - "#F57C00"  # Energetic Orange — CTA, ignition, launch
    - "#37474F"  # Mindful Gray — metadata, scaffolding, secondary text
    - "#B8E986"  # Growth Light — positive signal, emergence
  avoid_colors:
    - "#7C3AED"  # generic SaaS purple — avoid purple-on-white sameness

user_provided_assets:
  logo:
    primary:
      path: ./assets/thoughtseed-horizontal-wordmark-3x.png
      type: logo
      required: true
    icon:
      path: ./assets/thoughtseed-tree-mark-black-3x.png
      type: logo-icon
      required: false
  existing:
    - path: ./assets/thoughtseed-logo-reference-01.jpg
      type: reference
      note: "Canonical logo reference (do not regenerate)"
    - path: ./assets/thoughtseed-logo-reference-02.jpg
      type: reference
      note: "Canonical logo reference (do not regenerate)"

content:
  landing_page:
    sections:
      - hero               # Digital Wilderness stage
      - delivery-loop      # requirement -> handoff motion/state system
      - work               # project records + service modules
      - proof              # shipped systems, technical range, handoff artifacts
      - handoff            # ownership transfer as value
      - cta                # Bring the requirement.
  email:
    welcome_series: true
    launch_series: true
    prelaunch_series: true
  ads:
    platforms:
      - linkedin
      - x
    formats:
      - text
      - image

publishing:
  notebooklm:
    enabled: true
    artifacts:
      - mind_map
      - slides
      - brand_report
  wiki:
    enabled: true
    theme: "editorial"   # matte, signal-rich; NOT glossy/glassmorphism
  deliverables:
    formats:
      - zip
      - pdf
    include_origins: true

synthesis:
  synthesize_prose: true
  synthesis_model: "anthropic/claude-3.5-haiku"
  embedding_integration:
    enabled: false
    worker_url: ""

execution:
  depth: "comprehensive"
  waves: "1-7"
  max_cost: 25.00
  non_interactive: true

validation:
  require_user_assets: true
  warn_missing_optional: true
  fail_on_hallucination: true
```

## Upstream Outputs

### ad-creative-copy
```json
{
  "skill": "ad-creative-copy",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "strategy": {
      "phases": ["pre-launch", "launch", "mid-campaign", "end-campaign"],
      "platforms": ["linkedin", "x"],
      "formats": ["text", "image"],
      "audience": "The System-Carrying Founder: founder, CTO, innovation lead, or product strategist running a lean senior team.",
      "objective": "Reach founders who are tired of being the translator between disconnected vendors and route them to bring one requirement to one studio.",
      "voice_note": "Calm over loud. Short declarative lines. Evidence next to the claim. No hype, no superlatives, no internal methodology, no avoided terms.",
      "primary_cta": "Bring the requirement."
    },
    "hooks": {
      "problem_aware": [
        "You did not start the company to translate between five vendors.",
        "Strategy went to one vendor. Design to another. Nobody shares one model of the problem.",
        "The system worked on launch day. Then ownership transfer broke it.",
        "When a problem is too entangled to split, splitting it makes things worse."
      ],
      "solution_aware": [
        "One studio carries the whole requirement, from framing to handoff.",
        "A founder-led systems studio for problems that cannot be split across vendors.",
        "The people who frame the requirement are the people who ship the system.",
        "User behavior treated as part of the system, not a layer added after the build."
      ],
      "social_proof": [
        "Shipped systems across AI, IoT, web, mobile, and creative technology.",
        "Live client delivery paired with reusable product IP.",
        "Handoff documents that prove the delivery loop is real.",
        "Fewer engagements, deeper integration, a real handoff at the end."
      ],
      "urgency": [
        "We take a limited number of builds at a time. That is the point.",
        "Studio capacity for the next quarter is filling.",
        "Scoped delivery, not an open-ended retainer. Start with the requirement.",
        "Bring the requirement while there is room on the build calendar."
      ]
    },
    "linkedin_ads": [
      {
        "id": "li-pre-01",
        "name": "Problem Agitation",
        "phase": "pre-launch",
        "angle": "problem_aware",
        "urgency_level": "low",
        "intro_text": "You did not start the company to translate between vendors. Strategy goes to one. Design to another. Engineering to a third. None of them share one model of the problem, so coherence leaks at every handoff. There is a calmer way to carry the work.",
        "headline": "One studio, from requirement to handoff",
        "body": "Thoughtseed is a founder-led systems studio. We study the requirement, build the system, and hand it back in a form you can run.",
        "cta": "Bring the requirement."
      },
      {
        "id": "li-pre-02",
        "name": "Curiosity / Studio Shape",
        "phase": "pre-launch",
        "angle": "solution_aware",
        "urgency_level": "low",
        "intro_text": "Most studios pass your problem between specialists and lose coherence at every seam. We hold it in one motion. The same senior people frame the requirement, design the system, ship it, and hand it back.",
        "headline": "Build the system, not just the story",
        "body": "A founder-led systems studio for problems too entangled to split across vendors. One delivery loop. Senior judgment at every stage.",
        "cta": "See how the loop works"
      },
      {
        "id": "li-launch-01",
        "name": "Studio Live",
        "phase": "launch",
        "angle": "solution_aware",
        "urgency_level": "medium",
        "intro_text": "Thoughtseed Studio is open for new requirements. One team carries framing, user behavior, product, engineering, and handoff inside a single delivery loop, so coherence holds from the first decision to the running system.",
        "headline": "Thoughtseed Studio: one coherent delivery loop",
        "body": "Start with a System Sprint to frame and de-risk the requirement, or scope a Requirement-to-Handoff Build for full delivery. You talk to the operators doing the work.",
        "cta": "Bring the requirement."
      },
      {
        "id": "li-mid-01",
        "name": "Behavior In The System",
        "phase": "mid-campaign",
        "angle": "solution_aware",
        "urgency_level": "medium",
        "intro_text": "Adoption is an engineering concern, not post-launch polish. We map how people will actually use the system, design for it, then test it against the build. The work holds up in the real operating environment.",
        "headline": "User behavior, designed into the system",
        "body": "Web, mobile, AI, automation, and connected products, shipped with adoption logic grounded in build reality. What we framed is what we ship.",
        "cta": "Bring the requirement."
      },
      {
        "id": "li-mid-02",
        "name": "Handoff Proof",
        "phase": "mid-campaign",
        "angle": "social_proof",
        "urgency_level": "medium",
        "intro_text": "A system that works on launch day but breaks at ownership transfer is not finished. We treat that transfer as the deliverable. Documentation, training, and control surfaces ship with the build.",
        "headline": "Ownership transfer is the output, not the afterthought",
        "body": "You inherit a system you can run, extend, and own without us. Shipped across AI, IoT, web, mobile, and creative technology.",
        "cta": "Bring the requirement."
      },
      {
        "id": "li-end-01",
        "name": "Capacity Close",
        "phase": "end-campaign",
        "angle": "urgency",
        "urgency_level": "high",
        "intro_text": "We take a limited number of builds at a time, on purpose. Fewer engagements, deeper integration, a real handoff at the end. Studio capacity for the next quarter is filling.",
        "headline": "Scoped delivery, not an open-ended retainer",
        "body": "If the problem is too entangled to split across vendors, bring it here while there is room on the build calendar.",
        "cta": "Bring the requirement."
      }
    ],
    "x_ads": [
      {
        "id": "x-pre-01",
        "name": "Problem Agitation",
        "phase": "pre-launch",
        "angle": "problem_aware",
        "urgency_level": "low",
        "headline": "You did not start the company to translate between vendors.",
        "body": "Strategy, design, engineering, ops. Five teams, no shared model of the problem. Coherence leaks at every handoff. One studio can carry the whole thing instead.",
        "cta": "Bring the requirement."
      },
      {
        "id": "x-pre-02",
        "name": "Curiosity",
        "phase": "pre-launch",
        "angle": "solution_aware",
        "urgency_level": "low",
        "headline": "Build the system, not just the story.",
        "body": "A founder-led systems studio for problems too entangled to split across vendors. Requirement to handoff, one delivery loop.",
        "cta": "See how the loop works"
      },
      {
        "id": "x-launch-01",
        "name": "Studio Live",
        "phase": "launch",
        "angle": "solution_aware",
        "urgency_level": "medium",
        "headline": "Thoughtseed Studio is open for requirements.",
        "body": "One team carries framing, behavior, product, engineering, and handoff in a single loop. Start with a System Sprint or scope a Requirement-to-Handoff Build.",
        "cta": "Bring the requirement."
      },
      {
        "id": "x-mid-01",
        "name": "Behavior In The System",
        "phase": "mid-campaign",
        "angle": "solution_aware",
        "urgency_level": "medium",
        "headline": "We treat user behavior as part of the system.",
        "body": "Not a layer added after the build. Web, mobile, AI, automation, connected products, shipped to be used, not just launched.",
        "cta": "Bring the requirement."
      },
      {
        "id": "x-mid-02",
        "name": "Handoff Proof",
        "phase": "mid-campaign",
        "angle": "social_proof",
        "urgency_level": "medium",
        "headline": "Ownership transfer is the deliverable.",
        "body": "Documentation, training, and control surfaces ship with the build. You inherit a system you can run without us. From requirement to handoff.",
        "cta": "Bring the requirement."
      },
      {
        "id": "x-end-01",
        "name": "Capacity Close",
        "phase": "end-campaign",
        "angle": "urgency",
        "urgency_level": "high",
        "headline": "Fewer projects, deeper integration, real handoff.",
        "body": "We take a limited number of builds at a time, on purpose. Capacity for next quarter is filling. Bring the entangled problem here.",
        "cta": "Bring the requirement."
      }
    ],
    "platform_notes": {
      "linkedin": "Intro text leads with the founder's lived problem, then resolves to the studio shape. Headline stays factual and benefit-led. No superlatives.",
      "x": "Tighter. One declarative hook, one supporting line, the CTA. Atmosphere from phrasing, never volume.",
      "image_direction": "Pair copy with editorial-documentary imagery: prototyping spaces, worktables, tactile materials, architectural crops. No text baked into the image, no purple-on-white SaaS gradients, no stock startup team photos."
    }
  }
}
```

### brand-documentation
```json
{
  "skill": "brand-documentation",
  "cluster": "synthesis",
  "wave": 7,
  "timestamp": "2026-06-08T06:10:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "brand": "Thoughtseed",
    "document_separation_rationale": "Per the synthesis core (Lesson 4), a single monolithic brand book serves no audience well. The Thoughtseed package ships as three separated documents, each scoped to one reader and one decision context: Brand Identity for designers and production, Product Positioning for product and sales, and Campaign Guidelines for marketing and content. Internal-only material — the Krebs Cycle of Creativity, requirement-to-handoff loop internals, and the internal color labels — never appears in any document body; only its visible effects do.",
    "documents": {
      "brand_identity": {
        "title": "Thoughtseed — Brand Identity Guidelines",
        "audience": "Designers, production, and marketing operators producing branded surfaces.",
        "purpose": "Codify the logo system, color palette, typography, and visual language so every surface reads as one coherent, founder-led editorial system.",
        "page_count_estimate": 26,
        "sections_total": 5,
        "sections_complete": 5,
        "sections": [
          {
            "number": "01",
            "name": "Brand Overview",
            "source_skills": ["brand-foundation"],
            "prose": "Thoughtseed is a founder-led systems studio. Its essence is coherent systems, cultivated: disciplined engineering held against organic emergence. The brand reads as Sage with a Creator's hands — it earns trust through clarity and coherence, then ships and hands back what it frames. Five values govern every surface: clarity over theater, cross-disciplinary rigor, delivery integrity, accountable handoff, and selective focus. Personality is coherent, founder-led, precise, grounded, and intentional. In any identity surface, this means restraint over decoration, evidence over adjectives, and one calm signal over visual noise.",
            "assets_referenced": []
          },
          {
            "number": "02",
            "name": "Logo System",
            "source_skills": ["logo-concept"],
            "prose": "Thoughtseed uses two canonical marks as a system, not a single locked lockup. The horizontal wordmark is the primary mark for headers, mastheads, decks, and signatures wherever there is horizontal room. The tree mark is the standalone symbol for square and compact contexts — app icons, avatars, favicons, watermarks, embossed cover details. The marks are monochrome by rule: black on light surfaces, reversed to white on the deep-blue or dark canvas. Accent colors are never applied to the mark; they belong to the surrounding system. Clear space for the wordmark equals the cap-height of the T on all sides; for the tree mark, a quarter of its height minimum, half preferred. Minimum sizes: wordmark 120px / 28mm wide, tree mark 24px / 8mm tall (16px favicon floor only when the silhouette still reads). When the wordmark cannot meet its minimum, substitute the tree mark rather than shrinking it. Do not generate, redraw, recolor, skew, or add effects to the marks; any embossed seal or poster artwork in the reference set is art-direction mood only and is never a replacement mark.",
            "assets_referenced": [
              { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided", "deterministic": true, "role": "primary mark" },
              { "id": "logo-tree-mark", "path": "./assets/thoughtseed-tree-mark-black-3x.png", "origin": "user_provided", "deterministic": true, "role": "standalone symbol" },
              { "id": "logo-reference-01", "path": "./assets/thoughtseed-logo-reference-01.jpg", "origin": "user_provided", "deterministic": true, "role": "mark reference, not a lockup" },
              { "id": "logo-reference-02", "path": "./assets/thoughtseed-logo-reference-02.jpg", "origin": "user_provided", "deterministic": true, "role": "mark reference, not a lockup" }
            ]
          },
          {
            "number": "03",
            "name": "Color Palette",
            "source_skills": ["color-palette"],
            "prose": "The system is dark-first and cool-anchored, distributed roughly 60 / 25 / 10 / 5 to stay editorial rather than loud. A deep indigo-blue (#1A237E) and a cool near-black (#0A0E14) form the dominant dark field and carry long-horizon trust. A cool blue-gray (#37474F) supplies scaffolding, metadata, borders, and secondary text. A teal (#00897B) is the working signal for links, active states, focus, and data emphasis, at roughly ten percent. A single warm orange (#F57C00) is reserved almost entirely for the primary call-to-action; its scarcity is what makes it read as ignition. A soft green (#B8E986) marks positive emergence and validation. Accessibility is non-negotiable: orange CTAs MUST carry deep-blue (#1A237E) label text at 4.90:1 — white on orange fails at 2.70:1 and is forbidden. White on teal is large-text and UI only; darken to teal 600 (#007065) or add weight for fine text. The palette deliberately avoids the generic purple-on-white SaaS gradient. Color names are internal working labels for designers and tooling only; they never appear in any client-visible string, UI, or document body.",
            "assets_referenced": []
          },
          {
            "number": "04",
            "name": "Typography",
            "source_skills": ["typography"],
            "prose": "Type is a three-role system, not a two-font pairing, so the page reads as an editorial publication built by engineers. Tyros Pro is the display face for hero thresholds and ceremonial headings — the Digital Wilderness line, section thresholds, covers — used sparingly, never for body or UI. SubjectivitySerif is the primary reading voice for narrative and case-study copy at 16px / 1.625. Fira Code is the load-bearing data layer: metadata, captions, diagram and section labels, numbering, and eyebrow kickers, so the system always shows its engineering substrate. The scale is a 1.25 ratio on a 16px base. Contrast comes from role separation, not from piling on weights: one display moment per view, body measure of roughly 60–75 characters, the mono used to signal precision in labels and numbers rather than sprinkled through prose. Self-host the licensed display and serif webfonts with font-display: swap and editorial fallbacks; load Fira Code from Google Fonts or self-host. Never reach for a default SaaS stack as a primary face.",
            "assets_referenced": []
          },
          {
            "number": "05",
            "name": "Visual Language",
            "source_skills": ["visual-language"],
            "prose": "The visual territory is Digital Wilderness: architectural precision held against cultivated texture, structured layouts against alive surfaces, with neither side winning. Five principles govern it — architectural precision against cultivated texture, signal over noise, negative space as structure, material truth over gloss, and show the system. Materials run matte paper, black ink, glass, brushed aluminium, oxidized copper, weathered stone, living moss, screen glow, and architectural shadow. Photography is editorial documentary: natural directional light, architectural crops, intentional negative space, real materials and prototyping spaces over staged people, a cool desaturated cast with at most one restrained signal accent. Illustration is geometric systems diagrams blended with organic signal and cultivated-landscape motifs, in brand colors only. Icons share one single-weight, near-sharp 24px grid construction. Patterns are a quiet systems grid interwoven with contour and root-and-branch motifs. Forbidden across every image: purple-on-white SaaS gradients, stock startup team photos, empty futurism, mystical wellness fog, glossy plastic, cartoon iconography, and any text, lettering, or logos baked into generated imagery.",
            "assets_referenced": [
              { "id": "visual-language-board", "path": "./generated/visual-language-board.png", "origin": "generated", "deterministic": false, "role": "moodboard reference, direction not deliverable" },
              { "id": "icons-01-sheet", "path": "./generated/icons-01-sheet.png", "origin": "generated", "deterministic": false, "role": "icon construction reference" },
              { "id": "pattern-01-dark", "path": "./generated/pattern-01-dark.png", "origin": "generated", "deterministic": false, "role": "pattern, dark field" },
              { "id": "pattern-02-light", "path": "./generated/pattern-02-light.png", "origin": "generated", "deterministic": false, "role": "pattern, light field" },
              { "id": "illus-01-systems-organism", "path": "./generated/illus-01-systems-organism.png", "origin": "generated", "deterministic": false, "role": "illustration style example" },
              { "id": "illus-02-delivery-loop", "path": "./generated/illus-02-delivery-loop.png", "origin": "generated", "deterministic": false, "role": "illustration style example" }
            ]
          }
        ]
      },
      "product_positioning": {
        "title": "Thoughtseed — Product Positioning",
        "audience": "Product team and sales operators framing and selling Thoughtseed Studio.",
        "purpose": "Codify the value proposition, positioning, target buyer, and competitive frame so every conversation lands on coherence, ownership, and evidence.",
        "page_count_estimate": 14,
        "sections_total": 4,
        "sections_complete": 4,
        "sections": [
          {
            "number": "01",
            "name": "Value Proposition",
            "source_skills": ["value-proposition"],
            "prose": "One studio carries the requirement all the way to a system you own. The primary value is a single accountable owner of coherence from requirement to handoff — it ends the founder's exhausting role as the full-time translator between five specialists and stops coherence leaking at every seam. Secondary values follow: ownership over dependency, a system the team can run and extend; user behavior kept grounded in engineering reality so adoption survives launch; and AI and automation built into product logic rather than bolted on as a demo. The pain-to-gain motion is concrete — too many single-slice vendors become one delivery loop; decks disconnected from shipped reality become what-we-framed-is-what-we-ship; launch-day systems that break at handoff become documentation, training, and control surfaces that ship with the build. Table stakes — senior craft, modern engineering, professional discovery — are assumed, not sold.",
            "assets_referenced": [
              { "id": "product-01-system-artifacts", "path": "./generated/product-01-system-artifacts.png", "origin": "generated", "deterministic": false, "role": "system-artifacts visual for handoff value" },
              { "id": "product-02-screen-surface", "path": "./generated/product-02-screen-surface.png", "origin": "generated", "deterministic": false, "role": "product surface visual" }
            ]
          },
          {
            "number": "02",
            "name": "Positioning & Category",
            "source_skills": ["product-positioning"],
            "prose": "Thoughtseed defines the founder-led systems studio: the studio that carries a complex requirement all the way to a system the client can own, instead of selling a single slice of strategy, design, or engineering. The frame of reference is deliberate — not a single-slice design agency, not an enterprise consultancy that packages process, not an AI integrator chasing tooling. Points of difference: one integrated studio logic where requirement, behavior, interface, and engineering stay in one loop; founder-led judgment with less translation loss than layered account management; and handoff treated as part of the system. Points of parity — senior craft, modern engineering across web, mobile, AI, automation, and connected products, professional discovery — are met, then moved past. The positioning statement: for the system-carrying founder who needs to solve a problem too entangled to split across vendors, Thoughtseed aligns user psychology, founder operating logic, interface design, engineering delivery, and structured handoff into one coherent system from requirement to handoff.",
            "assets_referenced": []
          },
          {
            "number": "03",
            "name": "Target Customer",
            "source_skills": ["buyer-persona"],
            "prose": "The primary buyer is Mira, the System-Carrying Founder — a founder, CTO, innovation lead, or product strategist running a lean senior team at a funded startup through scaleup, controlling a project budget of roughly $150k–$600k per engagement, based in a major innovation hub. She sees herself as the only person currently holding the whole system in her head and resents being the permanent translator between vendors. She values coherence over performative specialization, ownership over dependency, taste with restraint, and evidence of shipping over polished promises. Her jobs to be done: frame a problem too entangled to split; ship a product real users adopt; add AI without it being a demo that never matures; own and run the system after the engagement; and stop being the integrator. She is skeptical of buzzwords and pitch theater, reads founder memos and technical walkthroughs over marketing content, and pays for competence once trust is earned through specificity.",
            "assets_referenced": []
          },
          {
            "number": "04",
            "name": "Competitive Positioning",
            "source_skills": ["competitor-analysis"],
            "prose": "Thoughtseed sits against five alternatives, each owning one slice and structurally dependent on translation loss. Large innovation consultancies package process and clear board approval but rarely ship and dilute coherence across big teams. Premium product design agencies produce exceptional craft but hand off before the system runs and carry thin engineering ownership. AI integration consultancies reach a fast demo but bolt AI on rather than building it into product logic. Specialized engineering vendors execute a clean spec but build mistakes as handed over with no requirement shaping. Freelancer swarms offer flexibility but make the founder the integrator. The ownable territory is editorial precision with operating clarity — the one founder-led studio that turns a single requirement into a coherent system you can own, framed in calm, signal-rich, technically grounded language no competitor category can credibly claim. The unfair advantage is structural: the same senior operators frame, design for adoption, ship the engineering, and build the handoff, removing the translation loss every single-slice competitor depends on.",
            "assets_referenced": []
          }
        ]
      },
      "campaign_content": {
        "title": "Thoughtseed — Campaign & Content Guidelines",
        "audience": "Marketing and content operators producing public-facing campaigns and copy.",
        "purpose": "Codify voice, messaging, story, and copy patterns so every campaign sounds like the founder-side systems translator and respects layer discipline.",
        "page_count_estimate": 18,
        "sections_total": 4,
        "sections_complete": 4,
        "sections": [
          {
            "number": "01",
            "name": "Brand Voice",
            "source_skills": ["voice-and-tone"],
            "prose": "Write as the founder-side systems translator: an operator who has built systems and lived with ambiguity, speaking peer to peer with the founder, never an account manager. The voice is clear, grounded, and crafted, in short declarative sentences with evidence close to every claim. Use requirement, operating logic, user behavior, founder context, systems, signal, coherence, intentional, crafted, shipped, legible, inherited, handoff, cross-disciplinary, and delivery loop. Describe the downstream effects of how the work is done — clearer requirements, calmer execution, stronger trust and adoption, cleaner ownership transfer — rather than the internal method behind them. Never use any term on the prohibited vocabulary list (see voice-and-tone, language_guidelines.vocabulary_bank.prohibited); the layer discipline is absolute, and any phrasing that reaches for hype, mystical, or generic-agency language must be translated back into visible effects. Do not describe Thoughtseed as an always-on retainer agency; the model is scoped delivery with strong handoff.",
            "prohibited_vocabulary_ref": "voice-and-tone.data.language_guidelines.vocabulary_bank.prohibited",
            "assets_referenced": []
          },
          {
            "number": "02",
            "name": "Messaging Framework",
            "source_skills": ["messaging-framework"],
            "prose": "The brand promise is one coherent system from requirement to handoff. The public headline is Digital Wilderness; the tagline is We plant ideas. They grow wild. Four message pillars carry every campaign: One coherent loop — one studio carries the whole requirement, framing to handoff; Founder-led judgment — senior operators do the work, so less is lost in translation; Behavior as part of the system — user psychology grounded in what actually ships; and Handoff you can run — ownership transfer is the output, not the afterthought. Approved phrases for verbatim use: Digital Wilderness; We plant ideas. They grow wild.; Build the system, not just the story.; From requirement to handoff.; One coherent delivery loop.; Cross-disciplinary rigor.; Bring the requirement. Objections have set responses — breadth is a deliberate studio shape, the difference from an agency is the delivery loop, psychology means trust and adoption grounded in engineering, and premium framing is backed by shipped evidence. Until verified client quotes exist, lead with shipped work and handoff artifacts rather than unattributed praise.",
            "assets_referenced": [
              { "id": "social-og", "path": "./generated/social-og.png", "origin": "generated", "deterministic": false, "role": "open-graph share card" },
              { "id": "social-x-header", "path": "./generated/social-x-header.png", "origin": "generated", "deterministic": false, "role": "social profile header" },
              { "id": "social-ig-story", "path": "./generated/social-ig-story.png", "origin": "generated", "deterministic": false, "role": "story-format social asset" }
            ]
          },
          {
            "number": "03",
            "name": "Brand Story",
            "source_skills": ["brand-story"],
            "prose": "Thoughtseed was planted in 2020 from one observation that would not go away: the problems worth solving were never single-discipline problems. They lived between a founder's operating logic, the user's behavior, the interface, and the engineering underneath — and the market split them across a consultancy, an agency, an engineering vendor, and whichever AI shop had the newest demo. The founder became the integrator by default, the full-time translator between five specialists who shared no model of the problem, and coherence leaked at every handoff. The answer was a single delivery loop: the same senior operators frame the requirement, design for adoption, ship the engineering, and build the handoff. Nothing is thrown over a wall, because there is no wall. This is Digital Wilderness — disciplined engineering meets organic emergence, structured systems still alive enough to grow once the client owns them. We plant ideas, and they grow wild, because we hand back something legible and inheritable, designed from the first day to be run by the team that keeps it. The enemy is fragmentation; the promised land is a coherent system the founder owns and the team can run. Build the system, not just the story. Bring the requirement.",
            "assets_referenced": [
              { "id": "hero-01-digital-wilderness", "path": "./generated/hero-01-digital-wilderness.png", "origin": "generated", "deterministic": false, "role": "primary hero, Digital Wilderness" }
            ]
          },
          {
            "number": "04",
            "name": "Copy Guidelines & Campaign Assets",
            "source_skills": ["landing-page-copy", "product-description", "ad-creative-copy", "press-release", "launch-email-sequence", "prelaunch-email-sequence", "welcome-email-sequence"],
            "prose": "Headlines stay spare and atmospheric; atmosphere comes from phrasing and image choice, not volume. Body copy is short, declarative, and editorial, with evidence next to the claim. CTAs default to Bring the requirement. and route to /start. The homepage runs as a numbered editorial sequence — Hero (00), Delivery Loop (01), Work (02), Proof (03), Handoff (04), Start (05) — with the four delivery-loop stages Requirement, System, Build, Handoff. Product copy describes Thoughtseed Studio in micro through extended lengths, always landing on one coherent system from requirement to handoff and ownership over dependency. Email sequences (pre-launch, launch, welcome) and ad creative carry the same pillars and approved phrases; the press release stays factual, restrained, and newsworthy. Campaign imagery draws from the validated hero, lifestyle, and social assets below — all generated, none containing baked-in text or logos. Place the wordmark or tree mark as a real asset over imagery; never rely on text rendered inside a generated image.",
            "assets_referenced": [
              { "id": "hero-01-digital-wilderness", "path": "./generated/hero-01-digital-wilderness.png", "origin": "generated", "deterministic": false, "role": "homepage hero" },
              { "id": "hero-02-establishing", "path": "./generated/hero-02-establishing.png", "origin": "generated", "deterministic": false, "role": "establishing / section hero" },
              { "id": "hero-03-mobile", "path": "./generated/hero-03-mobile.png", "origin": "generated", "deterministic": false, "role": "mobile hero crop" },
              { "id": "lifestyle-01-worktable", "path": "./generated/lifestyle-01-worktable.png", "origin": "generated", "deterministic": false, "role": "worktable lifestyle, proof/about" },
              { "id": "lifestyle-02-studio", "path": "./generated/lifestyle-02-studio.png", "origin": "generated", "deterministic": false, "role": "studio lifestyle, about" },
              { "id": "social-og", "path": "./generated/social-og.png", "origin": "generated", "deterministic": false, "role": "open-graph card" },
              { "id": "social-x-header", "path": "./generated/social-x-header.png", "origin": "generated", "deterministic": false, "role": "profile header" },
              { "id": "social-ig-story", "path": "./generated/social-ig-story.png", "origin": "generated", "deterministic": false, "role": "story asset" }
            ]
          }
        ]
      }
    },
    "asset_validation": {
      "manifest_source": ".brandmint/asset-manifest.json",
      "total_assets_referenced": 20,
      "assets_validated": 20,
      "assets_missing": 0,
      "assets_with_warnings": 0,
      "user_provided_count": 4,
      "generated_count": 16,
      "deterministic_count": 4,
      "unique_asset_ids_referenced": [
        "logo-wordmark", "logo-tree-mark", "logo-reference-01", "logo-reference-02",
        "visual-language-board", "icons-01-sheet", "pattern-01-dark", "pattern-02-light",
        "illus-01-systems-organism", "illus-02-delivery-loop", "product-01-system-artifacts",
        "product-02-screen-surface", "hero-01-digital-wilderness", "hero-02-establishing",
        "hero-03-mobile", "lifestyle-01-worktable", "lifestyle-02-studio",
        "social-og", "social-x-header", "social-ig-story"
      ]
    },
    "layer_discipline_check": {
      "avoided_terms_in_document_bodies": 0,
      "krebs_or_consciousness_as_public_claim": false,
      "internal_color_labels_surfaced_in_bodies": false,
      "note": "Internal color names (Deep Quantum Blue, Consciousness Teal, Energetic Orange, Mindful Gray, Growth Light) are intentionally NOT used in any prose body; only hex values and functional roles appear. Krebs Cycle and consciousness research are referenced only as backstage context in the separation rationale, never as a public category claim."
    },
    "outputs": {
      "intended_formats": ["markdown", "pdf"],
      "markdown": {
        "brand_identity": "deliverables/docs/thoughtseed-brand-identity.md",
        "product_positioning": "deliverables/docs/thoughtseed-product-positioning.md",
        "campaign_content": "deliverables/docs/thoughtseed-campaign-guidelines.md"
      },
      "pdf": {
        "brand_identity": "deliverables/docs/thoughtseed-brand-identity-guidelines.pdf",
        "product_positioning": "deliverables/docs/thoughtseed-product-positioning.pdf",
        "campaign_content": "deliverables/docs/thoughtseed-campaign-guidelines.pdf"
      }
    },
    "validation_report": {
      "all_assets_exist": true,
      "all_assets_in_manifest": true,
      "hallucinated_paths": 0,
      "documents_separated": true,
      "warnings": []
    }
  }
}
```

### brand-foundation
```json
{
  "skill": "brand-foundation",
  "cluster": "foundation",
  "wave": 1,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "name_rationale": "Thoughtseed names the studio's core motion: a requirement is planted as a single clear idea and grown into a coherent, living system the client can run. It carries the brand's two truths at once — disciplined cultivation and organic emergence — which surface publicly as the Digital Wilderness territory and the line 'We plant ideas. They grow wild.'",
    "mission": {
      "statement": "Thoughtseed exists to help system-carrying founders turn complex requirements into coherent technology systems by carrying framing, user behavior, product, engineering, and handoff inside one delivery loop instead of splitting them across disconnected vendors.",
      "breakdown": {
        "action": "turn complex requirements into coherent technology systems",
        "audience": "system-carrying founders, CTOs, innovation leads, and product strategists with lean senior teams",
        "outcome": "a coherent system the client can run, extend, and inherit after delivery",
        "differentiator": "one founder-led delivery loop from requirement to handoff, instead of stitching together five single-slice vendors"
      }
    },
    "vision": {
      "statement": "A world where important, cross-disciplinary problems are no longer fractured across disconnected vendors — where founders bring one requirement to one studio and receive a coherent system they can own and run.",
      "time_horizon": "10 years"
    },
    "values": [
      {
        "name": "Clarity over theater",
        "definition": "We say what is true and keep evidence next to every claim, removing inflated language before any work begins.",
        "in_practice": "We frame the requirement and surface constraints and tradeoffs first, so a founder sees the real problem and the real decision pressure before a single screen or model is built."
      },
      {
        "name": "Cross-disciplinary rigor",
        "definition": "We think across research, user behavior, product, engineering, and communication as one connected problem, not as separate handoffs.",
        "in_practice": "The same team that frames the requirement designs the interface and ships the engineering, so adoption logic and build reality stay aligned instead of drifting apart between specialists."
      },
      {
        "name": "Delivery integrity",
        "definition": "Design decisions must survive implementation, and implementation must stay legible to the client.",
        "in_practice": "We treat a strategy that cannot ship as a failed strategy; what we present in framing is what we hand back as a working system, not a deck disconnected from shipped reality."
      },
      {
        "name": "Accountable handoff",
        "definition": "Work is not complete until the system can be owned and run by the client without us.",
        "in_practice": "Documentation, training, and control surfaces are first-class outputs delivered with the build, so the system does not fall apart at ownership transfer."
      },
      {
        "name": "Selective focus",
        "definition": "We take on fewer, higher-leverage engagements where integrated thinking actually matters.",
        "in_practice": "We decline generic single-slice work and commit deeply to problems that cross product, interface, and technical delivery, rather than farming open-ended retainers."
      }
    ],
    "brand_essence": "Coherent systems, cultivated",
    "personality": {
      "archetype": "Sage (primary) / Creator (secondary)",
      "archetype_rationale": "Sage leads because the brand earns trust through clarity, truth, and coherence — calm judgment over loud claims. Creator follows because the studio does not just advise; it builds systems engineered to be inherited and run. The pairing keeps ambition grounded in shipped reality.",
      "if_a_person": {
        "age": "39",
        "occupation": "founder-side systems translator — an operator who has built and shipped real systems and lived with ambiguity across research, product, and engineering",
        "hobbies": ["editorial and longform writing", "architecture and industrial design", "prototyping with hardware and AI", "field photography of built and natural spaces"],
        "communication_style": "clear, calm, technically precise, and editorially restrained — speaks in short declarative sentences, keeps evidence close to the claim, and lets shipped work carry the weight rather than adjectives"
      },
      "adjectives": ["coherent", "founder-led", "precise", "grounded", "intentional"]
    }
  }
}
```

### brand-illustrations
```json
{
  "skill": "brand-illustrations",
  "cluster": "illustration",
  "wave": 5,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "Brand illustrations express the core duality literally: precise geometric node-and-line systems that grow organically into root, branch, and canopy forms — a seed becoming a structured system. Drawn in luminous teal line work on a deep blue-black field with exactly one orange node as the single highlighted element, they read as engineered yet alive. The set stays geometric-meets-organic, moderate complexity, legible not busy, and visualizes Thoughtseed's backstage-translated ideas (growth, the requirement-to-handoff loop) as frontstage-safe abstract motifs with no baked text or named-cycle labels.",
      "model": "gemini-3-pro-image-preview"
    },
    "style_codification": {
      "line_work": {
        "weight": "precise, mostly uniform technical line with selective organic variation where growth motifs enter",
        "style": "luminous geometric line / vector-style, clean edges",
        "color": "teal (#00897B) signal line as the dominant stroke"
      },
      "fill_style": "line-dominant, minimal fill; dark-first field rather than solid color blocks",
      "color_palette": ["#0A0E14", "#1A237E", "#00897B", "#F57C00", "#B8E986", "#37474F"],
      "color_rule": "Brand palette only. Teal signal lines on a Deep Quantum Blue / near-black field; Growth Light reserved for emergent notes; at most ONE Energetic Orange highlight per illustration. Never purple, never a rainbow palette.",
      "detail_level": "moderate — legible structure, not busy",
      "perspective": "flat / 2D diagrammatic, non-figurative",
      "motif": "engineered grid/diagram structure overgrown and interwoven with organic signal patterns and cultivated-landscape forms (roots, branches, contour lines)"
    },
    "assets": [
      {
        "id": "illus-01-systems-organism",
        "path": "./generated/illus-01-systems-organism.png",
        "aspect_ratio": "16:9",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "type": "hero",
        "concept": "A planted idea growing into a coherent system — the Digital Wilderness duality of disciplined engineering and organic emergence, expressed as a seed becoming a structured canopy.",
        "description": "Brand illustration: a precise geometric node-and-line system diagram that grows organically into fine root and branch forms, like a seed becoming a structured canopy, drawn in luminous teal line work with one orange node on a deep blue-black field, engineered yet alive.",
        "prompt": "A brand illustration: a precise geometric node-and-line system diagram that grows organically into fine root and branch forms, like a seed becoming a structured canopy, drawn in luminous teal line work with one orange node on a deep blue-black field, engineered yet alive.",
        "usage": ["homepage-hero-illustration", "about-section", "conceptual-divider", "deck"]
      },
      {
        "id": "illus-02-delivery-loop",
        "path": "./generated/illus-02-delivery-loop.png",
        "aspect_ratio": "1:1",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "type": "conceptual",
        "concept": "The requirement-to-handoff delivery loop as one continuous, coherent cycle — a frontstage-safe abstraction of the internal loop, shown as geometric flow transitioning into organic growth. No named cycle, no labels.",
        "description": "Brand illustration of a continuous loop: an abstract requirement-to-handoff cycle as a circular geometric flow that subtly transitions into organic growth motifs, with four implied stages marked only by node clusters, in teal on blue-black with a single orange accent.",
        "prompt": "A brand illustration of a continuous loop: an abstract requirement-to-handoff cycle as a circular geometric flow that subtly transitions into organic growth motifs, with four implied stages marked only by node clusters, in teal on blue-black with a single orange accent.",
        "usage": ["delivery-loop-section", "process-diagram", "feature-spot", "deck"]
      }
    ],
    "consistency_verified": true,
    "consistency_checks": {
      "same_line_weight": true,
      "brand_colors_only": true,
      "same_perspective_system": true,
      "consistent_detail_level": true,
      "same_brand_personality": true
    },
    "quality_gates": {
      "style_codification_matches_visual_language": true,
      "brand_colors_only": true,
      "hero_illustration_defined": "illus-01-systems-organism",
      "vector_style_output": true,
      "no_baked_text_or_logos": true,
      "no_cartoon_iconography": true,
      "backstage_layer_protected": "No named Krebs cycle / consciousness labels; loop shown as abstract effect only.",
      "forbidden_visuals_avoided": true,
      "all_images_generated": true,
      "prompts_documented": true
    },
    "generation_summary": { "total": 2, "generated": 2, "pending": 0, "model": "gemini-3-pro-image-preview" }
  }
}
```

### brand-story
```json
{
  "skill": "brand-story",
  "cluster": "strategy",
  "wave": 2,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "tagline": "We plant ideas. They grow wild.",
    "headline": "Digital Wilderness",
    "call_to_action": "Bring the requirement.",
    "origin_story": {
      "the_before": "Important work kept getting split across strategy, design, engineering, and operations vendors who shared no model of the problem. Founders carried the gap. They became the full-time translator between five specialists, watching coherence leak at every handoff.",
      "inciting_incident": "Planted in 2020, Thoughtseed started from a simple observation: the hardest problems were not single-discipline problems. They sat between product, user behavior, interface, and engineering, and no single-slice vendor could hold them whole.",
      "the_struggle": "Cross-disciplinary curiosity led the founders to work across fields most studios keep separate. The hard part was discipline. Range only matters if it stays grounded in what ships, so the studio built one operating logic instead of a menu of services.",
      "the_breakthrough": "The answer was a single delivery loop. One founder-led studio that studies the requirement, designs for adoption, ships the engineering, and builds the handoff, so coherence is never handed between disconnected parts.",
      "the_mission": "Thoughtseed exists to carry a complex requirement all the way to a coherent system the client can run, extend, and inherit. We build the system, not just the story.",
      "full_narrative": "Thoughtseed was planted in 2020 from one observation that would not go away: the problems worth solving were never single-discipline problems. They lived in the space between a founder's operating logic, the user's behavior, the interface, and the engineering underneath, and the way the market was organized made that space impossible to hold. Strategy went to a consultancy. Design went to an agency. Engineering went to a vendor. AI went to whichever shop had the newest demo. Each one understood a slice. None of them understood the whole. And so the founder became the integrator by default, the full-time translator carrying meaning between five specialists who shared no model of the problem. Coherence leaked at every handoff. The deck stopped matching the product. The system that worked on launch day fell apart when it was time to hand it over. The founders behind Thoughtseed came to this from cross-disciplinary curiosity, a habit of working across fields that most studios keep firmly apart. That breadth was the start, but breadth alone is a liability. Range only earns its keep when it stays grounded in what actually ships. So the discipline came next: not a wider menu of services, but a single operating logic that could carry one problem from framing to ownership without losing its shape. That is the delivery loop. The same senior operators frame the requirement, design for adoption, build the engineering, and write the handoff. Nothing is thrown over a wall, because there is no wall. This is what we mean by Digital Wilderness. Disciplined engineering meets organic emergence: structured systems that are still alive enough to grow once the client owns them. We plant ideas, and they grow wild, not because we walk away, but because we hand back something legible and inheritable, designed from the first day to be run by the team that keeps it. The mission has stayed the same since 2020. Hold the whole problem. Keep evidence next to every claim. Hand back a coherent system the client can run, extend, and inherit, instead of a stack of disconnected deliverables and a new dependency. Bring the requirement. We study it, build the system, and give it back in a form you can actually run."
    },
    "brand_mythology": {
      "archetype": "Sage with a Creator's hands — clarity and coherence that also ships and is inherited.",
      "enemy": "Fragmentation. The single-slice model that splits one problem across disconnected vendors and forces the founder to become the integrator.",
      "promised_land": "A coherent system the founder owns and the team can run, where execution stays whole from requirement to handoff and ownership never breaks at launch.",
      "transformation_enabled": "The founder stops translating between specialists and starts owning a legible, inheritable system, calm in the knowledge that coherence held all the way through."
    },
    "customer_transformation": {
      "character": "Mira, the System-Carrying Founder — founder, CTO, innovation lead, or product strategist with a lean senior team, carrying a problem too entangled to split.",
      "problem": {
        "external": "A complex requirement is fragmented across strategy, design, engineering, and AI vendors who share no model of the problem, so coherence breaks before launch and ownership breaks after it.",
        "internal": "She is exhausted from being the full-time translator and distrustful of decks that never match shipped reality.",
        "philosophical": "Work this important should be owned, not outsourced in disconnected slices, and a founder should be able to inherit the result instead of depending on a vendor."
      },
      "guide": {
        "empathy_statement": "We have built systems and lived with the ambiguity. We know what it costs to be the only person holding the whole problem together.",
        "authority_statement": "We carry framing, behavior, product, engineering, and handoff in one founder-led delivery loop, with shipped systems across AI, IoT, web, mobile, and creative technology to show for it."
      },
      "plan": [
        "Bring the requirement. We study it and frame the problem, the user, and your operating reality before anything is built.",
        "We design and build the system in one delivery loop, with user behavior treated as part of the system and grounded in engineering.",
        "We hand it back legible, with documentation, training, and control surfaces, so your team can run, extend, and inherit it."
      ],
      "call_to_action": "Bring the requirement.",
      "failure_avoided": "She avoids going back to being the full-time translator between five specialists, watching coherence leak at every handoff and the system break at ownership transfer.",
      "success_achieved": "She owns a coherent system her team can run and extend, built once, handed back clean, with the calm confidence that nothing essential was lost between vendors."
    },
    "key_moments": {
      "ah_ha_moment": "The moment she realizes the problem is not a design problem or an engineering problem but a coherence problem, and that no single-slice vendor can own it.",
      "first_experience": "The first framing session, where the requirement, the user, and her operating reality are mapped into one model before anyone proposes a build.",
      "transformation": "Before: five vendors, one exhausted translator, coherence leaking at every seam. After: one delivery loop, one accountable owner, a system her team can run.",
      "advocacy": "She tells other founders that for once she got a system she could actually run, not a beautiful deck or a demo that died at implementation."
    },
    "story_formats": {
      "one_liner": "We plant ideas. They grow wild. One studio carries your requirement to a system you own.",
      "paragraph": "Thoughtseed is a founder-led systems studio, planted in 2020 from one observation: the problems worth solving live between disciplines, where single-slice vendors cannot hold them. We carry framing, user behavior, product, engineering, and handoff in one delivery loop, then hand back a coherent system your team can run, extend, and inherit. Build the system, not just the story.",
      "short_story": "Thoughtseed was planted in 2020 from a problem the founders kept watching repeat. Important work was split across strategy, design, engineering, and AI vendors who shared no model of the problem, so the founder became the full-time translator and coherence leaked at every handoff. The studio grew from cross-disciplinary curiosity, a habit of working across fields most studios keep apart, but breadth only mattered once it was disciplined into one operating logic. That logic is the delivery loop: the same senior operators frame the requirement, design for adoption, ship the engineering, and build the handoff. We call the result Digital Wilderness, where structured systems stay alive enough to grow once the client owns them. We plant ideas, and they grow wild, because we hand back something legible and inheritable. Bring the requirement. We study it, build the system, and give it back in a form you can run.",
      "full_narrative": "Thoughtseed was planted in 2020 from one observation that would not go away: the problems worth solving were never single-discipline problems. They lived in the space between a founder's operating logic, the user's behavior, the interface, and the engineering underneath, and the way the market was organized made that space impossible to hold. Strategy went to a consultancy. Design went to an agency. Engineering went to a vendor. AI went to whichever shop had the newest demo. Each one understood a slice. None understood the whole. So the founder became the integrator by default, the full-time translator carrying meaning between five specialists who shared no model of the problem. Coherence leaked at every handoff. The deck stopped matching the product. The system that worked on launch day fell apart when it was time to hand it over. Thoughtseed came at this from cross-disciplinary curiosity, a habit of working across fields most studios keep firmly apart. That breadth was the start, but breadth alone is a liability. Range only earns its keep when it stays grounded in what actually ships, so the discipline came next: not a wider menu of services, but a single operating logic that carries one problem from framing to ownership without losing its shape. That is the delivery loop. The same senior operators frame the requirement, design for adoption, build the engineering, and write the handoff. Nothing is thrown over a wall, because there is no wall. This is what we mean by Digital Wilderness. Disciplined engineering meets organic emergence: structured systems still alive enough to grow once the client owns them. We plant ideas, and they grow wild, not because we walk away, but because we hand back something legible and inheritable, designed from the first day to be run by the team that keeps it. The mission has stayed the same since 2020. Hold the whole problem. Keep evidence next to every claim. Hand back a coherent system the client can run, extend, and inherit, instead of a stack of disconnected deliverables and a new dependency. Bring the requirement. We study it, build the system, and give it back in a form you can actually run."
    }
  }
}
```

### buyer-persona
```json
{
  "skill": "buyer-persona",
  "cluster": "foundation",
  "wave": 1,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "persona_name": "Mira, the System-Carrying Founder",
    "demographics": {
      "age": 41,
      "gender": null,
      "education": "Master's degree in a technical or design discipline (e.g., computer science, HCI, or product design)",
      "income": "$220,000 base plus equity; controls a project or innovation budget of $150,000–$600,000 per engagement",
      "location": "Major innovation hub — urban core of a city like London, Berlin, Singapore, or Bangalore",
      "occupation": "Founder / CTO / innovation lead / product strategist at a funded startup or scaleup with a lean senior team"
    },
    "psychographics": {
      "identity": "Sees herself as the person who carries the whole system in her head — the only one who currently understands how requirement, user, product, and operations connect — and resents that this makes her the permanent translator between vendors.",
      "values": ["coherence over performative specialization", "ownership over dependency", "competence and taste with restraint", "evidence of shipping over polished promises", "clarity about tradeoffs"],
      "lifestyle": "Operates with a small senior team and a long task list; reads founder memos and technical walkthroughs over marketing content; protects focus time; deeply skeptical of buzzwords and pitch theater.",
      "aspirations": "Solve an important, cross-disciplinary problem well, then hand it to her team to run — so she can step out of the translator role and back into building the company.",
      "community": "Other founders, CTOs, and innovation leads; technical operators; angel and seed investors; design- and engineering-literate peers who trade case studies and handoff notes."
    },
    "challenges": [
      {
        "challenge": "Every vendor only understands one slice of the problem, so she becomes the full-time translator stitching strategy, design, and engineering together.",
        "current_solution": "A roster of single-slice vendors — a strategy shop, a design agency, an engineering firm — coordinated by her.",
        "why_it_fails": "No vendor shares one model of the problem, so coherence is destroyed in the gaps between them and accountability has no single owner.",
        "quote": "I'm spending more time translating between five vendors than actually building the company."
      },
      {
        "challenge": "Strategy decks arrive beautiful and then drift completely from the product that actually ships.",
        "current_solution": "A separate strategy or branding engagement that produces a deck, handed to a different team to build.",
        "why_it_fails": "Decisions made in the deck never survive implementation, so the shipped product quietly contradicts the strategy it was supposed to express.",
        "quote": "The strategy looked great on slide 12, but nothing in the product we shipped actually reflects it."
      },
      {
        "challenge": "AI proposals are either technically shallow demos or operationally naive — bolted on, not integrated into the product's real logic.",
        "current_solution": "An AI integration consultancy pitching current tooling and efficiency narratives.",
        "why_it_fails": "The work stops at a demo layer and ignores product experience, user behavior, and how the system has to actually run day to day.",
        "quote": "Everyone's selling me an AI demo. Nobody's shown me how it survives contact with real users and real operations."
      },
      {
        "challenge": "The system works on launch day and then falls apart at ownership transfer.",
        "current_solution": "A build vendor that ships the product and treats documentation and handoff as a closing footnote.",
        "why_it_fails": "Without real documentation, training, and control surfaces, her team can't run or extend the system, so she stays dependent on the vendor forever.",
        "quote": "It launched fine. Two months later my team couldn't change a thing without going back to the vendor."
      },
      {
        "challenge": "Studios that lead with human or psychology language can sound soft, and premium studios can be beautiful but slow.",
        "current_solution": "Premium design studios with strong taste but weaker engineering ownership and velocity.",
        "why_it_fails": "She can't tell whether the atmosphere hides shallow delivery, and she can't afford a partner that is elegant but cannot ship on a real timeline.",
        "quote": "I need depth and a system I can run — not a gorgeous narrative that takes a year and breaks when I touch it."
      }
    ],
    "emotional_drivers": {
      "positive": [
        "Relief at finally having one accountable partner who holds the whole problem",
        "Confidence that what was framed is what will actually ship",
        "Pride in a coherent, well-crafted system that reflects real taste and rigor",
        "Ownership and autonomy — her team can run and extend the system without her",
        "Trust earned through specificity and evidence of shipping rather than promises"
      ],
      "negative": [
        "Frustration and fatigue from being the permanent translator between vendors",
        "Anxiety that the polished pitch hides shallow or naive delivery",
        "Regret over money and months lost to work that drifted from reality",
        "Fear of dependency — being locked to a vendor she can never run the system without",
        "Embarrassment of championing a partner internally who then ships incoherent, broken-at-handoff work"
      ]
    },
    "cbbe": {
      "salience": {
        "product_category": "Founder-led systems studio for requirement-to-handoff delivery",
        "problem_solved": "Important, cross-disciplinary work gets fractured across disconnected vendors who do not share one model of the problem, which destroys coherence before launch and makes ownership harder after it.",
        "one_sentence": "Thoughtseed is the one studio that studies the requirement, the user, and the founder's operating reality, then designs, builds, and hands back a coherent system the client can run."
      },
      "performance": {
        "points_of_difference": [
          "One integrated studio logic across requirement, behavior, product, and delivery — not five vendors to coordinate",
          "Founder-led judgment with fewer translation layers, instead of account-management mediation",
          "User-behavior-aware framing that stays grounded in engineering and build reality",
          "Handoff treated as a first-class output — documentation, training, and control surfaces shipped with the system",
          "Studio-plus-IP posture with reusable product IP, not pure service-vendor billing"
        ],
        "points_of_parity": [
          "Premium product and interface craft",
          "Real engineering and AI/automation capability across web, mobile, and connected devices",
          "Professional discovery, scoping, and project delivery",
          "A clear engagement and pricing structure for serious budgets"
        ],
        "core_features": [
          "Requirement Architecture: problem framing, behavior mapping, operating constraints, and decision logic before implementation",
          "Product and Interface Systems: web, mobile, AI, automation, and connected-product execution with user behavior treated as part of the system",
          "Handoff and Decision Systems: documentation, training, control surfaces, and operational artifacts that make the work inheritable",
          "Engagement models: System Sprint for fast framing and de-risking, and Requirement-to-Handoff Build for scoped delivery through ownership transfer"
        ]
      },
      "imagery": {
        "associated_brands": [
          "IDEO (integrated, research-led problem framing) — but with deeper engineering ownership",
          "Pentagram (editorial taste and a distinct point of view) — but extended through to shipped technical systems",
          "Thoughtworks / Palantir Foundry (serious technical delivery) — but founder-close and design-literate, not enterprise-distant"
        ],
        "usage_locations": [
          "Founder and innovation-team strategy sessions where the requirement is first framed",
          "Live product, AI, and connected-device builds across web and mobile",
          "Ownership-transfer moments where the running system moves to the client's internal team"
        ],
        "usage_methods": [
          "Engaged as the single accountable partner for a cross-disciplinary problem",
          "Brought in early for a System Sprint to clarify and de-risk the next build decision",
          "Retained for a scoped Requirement-to-Handoff Build that ends in a runnable, documented system"
        ]
      },
      "judgments": {
        "positive": [
          "Finally, one partner who holds the whole problem instead of one slice",
          "The language is intelligent without becoming abstract or salesy",
          "There is real evidence of shipped systems, not just decks",
          "Handoff and operational clarity are treated as part of the value"
        ],
        "concerns": [
          "This sounds broad — is it a generalist-for-hire rather than a focused studio?",
          "Is this just another agency with nicer words?",
          "Will the human and behavior language come at the expense of technical depth?",
          "Premium studios can be beautiful but slow — can they ship on a real timeline?"
        ],
        "credibility": "Established founder-led systems studio (founded 2020) with shipped work across AI and automation, web, mobile, and connected devices; live client delivery plus reusable internal product IP; service surfaces that already span framing, design, engineering, and handoff; and decision artifacts and handoff documents that prove the model in practice."
      },
      "feelings": {
        "desired_feelings": [
          "Relieved to have handed the whole problem to one accountable partner",
          "Confident the system will ship coherent and run after delivery",
          "Respected as a technical, skeptical buyer rather than pitched at",
          "In control — owning the system rather than depending on a vendor"
        ],
        "voice": "The founder-side systems translator — a peer operator who has built and shipped systems and lived with ambiguity, not an account manager or a guru.",
        "tone": "Clear, calm, technically precise, human, and editorially restrained — ambitious ideas kept grounded, with evidence close to every claim."
      },
      "resonance": {
        "why_missed": "Without Thoughtseed, this founder goes back to being the full-time translator between single-slice vendors, watching coherence leak away between handoffs and carrying a system no one else can run.",
        "mission_alignment": "Her mission is to solve an important problem and hand a runnable system to her team; Thoughtseed's mission is to deliver exactly that coherent, inheritable system — so the studio's success is measured by her independence, not her dependency.",
        "core_values": ["coherence", "ownership over dependency", "evidence over theater", "cross-disciplinary rigor", "taste with restraint"],
        "why_choose_us": "Because no other partner carries framing, user behavior, product, engineering, and handoff in one founder-led loop — so she gets one accountable studio, a system that ships coherent, and a clean transfer to ownership instead of a vendor she can never leave."
      }
    }
  }
}
```

### color-palette
```json
{
  "skill": "color-palette",
  "cluster": "identity",
  "wave": 3,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "rationale": {
      "brand_attributes": [
        "cross-disciplinary",
        "founder-led",
        "precise",
        "editorial",
        "grounded"
      ],
      "color_psychology": "The system is dark-first and cool-anchored: a deep blue-black carries long-horizon trust and serious depth, a teal signal directs attention and reads as interface energy, a single warm orange marks ignition and launch moments, a cool blue-gray provides scaffolding and quiet metadata, and a soft green confirms positive emergence. The pairing of a disciplined cool base with one warm accent is the chromatic form of the brand duality — architectural precision against cultivated emergence. Color names are internal working labels only and are never surfaced in public copy.",
      "competitor_differentiation": "Deliberately avoids the generic purple-on-white SaaS gradient (#7C3AED and its family). Where innovation consultancies and AI vendors default to bright purple and high-saturation light UIs, Thoughtseed anchors on a deep indigo-blue near-black with a single restrained warm accent, signalling an editorial, founder-led studio rather than another agency template."
    },
    "color_naming_note": "Palette color names (Deep Quantum Blue, Consciousness Teal, Energetic Orange, Mindful Gray, Growth Light) are INTERNAL labels for designers and tooling. They must never appear in public-facing copy, UI strings, or client-visible artifacts. In particular 'Consciousness Teal' references backstage research origins and is forbidden in any frontstage surface.",
    "palette": {
      "primary": {
        "hex": "#1A237E",
        "rgb": "rgb(26, 35, 126)",
        "hsl": "hsl(235, 66%, 30%)",
        "name": "Deep Quantum Blue",
        "role": "anchor",
        "usage": "Anchor backgrounds, long-horizon trust, serious depth, primary headings on light surfaces, dark sectional fields, the visual spine of the system.",
        "variations": {
          "50": "#EDEDF5",
          "100": "#D6D7E8",
          "200": "#ADB0D1",
          "300": "#8388B9",
          "400": "#51589D",
          "500": "#1A237E",
          "600": "#151D67",
          "700": "#111753",
          "800": "#0D123F",
          "900": "#090C2B"
        }
      },
      "secondary": {
        "hex": "#37474F",
        "rgb": "rgb(55, 71, 79)",
        "hsl": "hsl(200, 18%, 26%)",
        "name": "Mindful Gray",
        "role": "scaffolding / secondary text",
        "usage": "Metadata, borders, dividers, scaffolding, secondary and tertiary text, table rules, system chrome. The quiet structural layer that lets signal colors carry meaning.",
        "variations": {
          "50": "#F8F9F9",
          "100": "#EDEEEF",
          "200": "#D7DADC",
          "300": "#B3B9BC",
          "400": "#879195",
          "500": "#5B686F",
          "600": "#37474F",
          "700": "#1F2730",
          "800": "#161B22",
          "900": "#0A0E14"
        }
      },
      "accent": {
        "primary_signal": {
          "hex": "#00897B",
          "rgb": "rgb(0, 137, 123)",
          "hsl": "hsl(174, 100%, 27%)",
          "name": "Consciousness Teal",
          "role": "primary accent / directional signal",
          "usage": "Primary accent, directional signal, interface energy, links, active states, focus rings, key data emphasis, diagram signal lines. The teal is the brand's working signal color, not the launch trigger.",
          "variations": {
            "50": "#EBF6F4",
            "100": "#D1EAE7",
            "200": "#A3D5CF",
            "300": "#75BFB8",
            "400": "#3DA59B",
            "500": "#00897B",
            "600": "#007065",
            "700": "#005A51",
            "800": "#00443E",
            "900": "#002F2A"
          }
        },
        "ignition": {
          "hex": "#F57C00",
          "rgb": "rgb(245, 124, 0)",
          "hsl": "hsl(30, 100%, 48%)",
          "name": "Energetic Orange",
          "role": "CTA / ignition",
          "usage": "Reserved almost entirely for the primary call-to-action, ignition, and launch moments ('Bring the requirement.'). The single warm note in a cool system — its scarcity is what makes it read as ignition. Never use as a background field or for body text.",
          "variations": {
            "50": "#FEF5EB",
            "100": "#FDE7D1",
            "200": "#FBD0A3",
            "300": "#FAB875",
            "400": "#F79B3D",
            "500": "#F57C00",
            "600": "#C96600",
            "700": "#A25200",
            "800": "#7A3E00",
            "900": "#532A00"
          }
        },
        "positive_signal": {
          "hex": "#B8E986",
          "rgb": "rgb(184, 233, 134)",
          "hsl": "hsl(90, 69%, 72%)",
          "name": "Growth Light",
          "role": "positive signal / emergence",
          "usage": "Positive signal, emergence, subtle validation, success ticks, progress confirmation, the 'grows wild' organic note. Most effective as a small bright accent on the deep blue or near-black anchor.",
          "variations": {
            "50": "#F9FDF5",
            "100": "#F2FBE9",
            "200": "#E5F7D3",
            "300": "#D9F3BE",
            "400": "#C9EEA3",
            "500": "#B8E986",
            "600": "#97BF6E",
            "700": "#799A58",
            "800": "#5C7443",
            "900": "#3F4F2E"
          }
        }
      },
      "semantic": {
        "success": "#B8E986",
        "warning": "#F57C00",
        "error": "#C0392B",
        "info": "#00897B",
        "note": "Semantic states reuse the brand palette wherever it stays legible — Growth Light for success, the ignition orange for warning, teal for info. Error introduces a controlled muted red (#C0392B) because no brand hue should carry destructive meaning; keep it rare and never decorative."
      },
      "neutrals": {
        "900": "#0A0E14",
        "800": "#161B22",
        "700": "#1F2730",
        "600": "#37474F",
        "500": "#5B686F",
        "400": "#879195",
        "300": "#B3B9BC",
        "200": "#D7DADC",
        "100": "#EDEEEF",
        "50": "#F8F9F9",
        "white": "#FFFFFF",
        "note": "Cool blue-gray neutral ramp anchored on Mindful Gray (#37474F at 600). Neutral 900 (#0A0E14) is the dark-first canvas ink; it is a cool near-black, not pure #000, to sit naturally beside the deep blue anchor."
      }
    },
    "usage_ratios": {
      "model": "Disciplined 60 / 25 / 10 / 5 distribution keeps the system editorial rather than loud.",
      "anchor_and_neutral_dark": "~60% — Deep Quantum Blue and the dark cool neutrals (900/800/700) form the dominant dark-first field.",
      "neutral_light_and_paper": "~25% — white, Neutral 50/100 and Mindful Gray scaffolding for light editorial surfaces and text.",
      "teal_signal": "~10% — Consciousness Teal for directional signal, links, active states, and data emphasis.",
      "ignition_and_growth": "~5% combined — Energetic Orange strictly for the primary CTA/ignition, Growth Light for small positive-signal accents. Scarcity is intentional; if orange or green covers large areas the system loses its signal logic."
    },
    "dark_first_guidance": {
      "default_canvas": "#0A0E14 (Neutral 900) and #1A237E (Deep Quantum Blue) are the default canvases. Light surfaces are the secondary mode, used for long-form editorial reading and print.",
      "text_on_dark": "Primary text on dark = #FFFFFF or Neutral 50 (#F8F9F9). Secondary/metadata on dark = Neutral 300 (#B3B9BC) which holds 9.41:1 on Neutral 900. Avoid Mindful Gray (#37474F) as text directly on the dark canvas — it is a structural/scaffolding tone there, not a text tone.",
      "signal_on_dark": "Teal, Growth Light, and Orange all read as bright signal on the dark anchor. Growth Light (13.85:1 on #0A0E14) and Teal are the workhorses; reserve Orange for the single ignition action.",
      "surfaces_and_elevation": "Build elevation with the neutral dark ramp (900 base, 800 raised, 700 cards/borders) rather than with shadows alone — material and contrast over glossy depth."
    },
    "accessibility": {
      "standard": "WCAG 2.1 — AA target for all text and UI; AAA noted where achieved.",
      "critical_rules": [
        "Energetic Orange (#F57C00) CTAs MUST use Deep Quantum Blue (#1A237E) label text (4.90:1, AA), NOT white — white on orange is only 2.70:1 and fails. This is the single most important contrast rule in the system.",
        "Consciousness Teal (#00897B) with white text is 4.32:1 — passes AA for large text (18px+/14px bold) and UI components, but NOT for normal body text. Use teal-on-white or teal-on-dark for fine text, or restrict white-on-teal to large/bold labels.",
        "Teal-on-blue (#00897B on #1A237E) is 3.07:1 — large text and UI/graphical elements only, never small body text."
      ],
      "contrast_checks": [
        { "foreground": "#FFFFFF", "background": "#1A237E", "ratio": "13.24:1", "wcag_aa": true, "wcag_aaa": true, "use": "Primary text on the deep-blue anchor — excellent." },
        { "foreground": "#FFFFFF", "background": "#0A0E14", "ratio": "19.34:1", "wcag_aa": true, "wcag_aaa": true, "use": "Primary text on the dark-first canvas — excellent." },
        { "foreground": "#B8E986", "background": "#1A237E", "ratio": "9.48:1", "wcag_aa": true, "wcag_aaa": true, "use": "Growth Light positive signal on anchor blue." },
        { "foreground": "#B8E986", "background": "#0A0E14", "ratio": "13.85:1", "wcag_aa": true, "wcag_aaa": true, "use": "Growth Light signal on dark canvas." },
        { "foreground": "#B3B9BC", "background": "#0A0E14", "ratio": "9.41:1", "wcag_aa": true, "wcag_aaa": true, "use": "Neutral 300 metadata/secondary text on dark canvas." },
        { "foreground": "#1A237E", "background": "#FFFFFF", "ratio": "13.24:1", "wcag_aa": true, "wcag_aaa": true, "use": "Deep-blue headings on white editorial surface." },
        { "foreground": "#37474F", "background": "#FFFFFF", "ratio": "9.65:1", "wcag_aa": true, "wcag_aaa": true, "use": "Mindful Gray body/secondary text on white." },
        { "foreground": "#FFFFFF", "background": "#37474F", "ratio": "9.65:1", "wcag_aa": true, "wcag_aaa": true, "use": "White text on Mindful Gray surface." },
        { "foreground": "#1A237E", "background": "#F57C00", "ratio": "4.90:1", "wcag_aa": true, "wcag_aaa": false, "use": "REQUIRED CTA pairing — deep-blue label on Energetic Orange button." },
        { "foreground": "#1A237E", "background": "#B8E986", "ratio": "9.48:1", "wcag_aa": true, "wcag_aaa": true, "use": "Deep-blue text on a Growth Light chip/badge." },
        { "foreground": "#37474F", "background": "#B8E986", "ratio": "6.91:1", "wcag_aa": true, "wcag_aaa": false, "use": "Mindful Gray text on Growth Light." },
        { "foreground": "#FFFFFF", "background": "#00897B", "ratio": "4.32:1", "wcag_aa": false, "wcag_aaa": false, "use": "White on teal — AA Large / UI ONLY (passes 3:1); fails for normal body text." },
        { "foreground": "#00897B", "background": "#FFFFFF", "ratio": "4.32:1", "wcag_aa": false, "wcag_aaa": false, "use": "Teal on white — AA Large / UI / links with non-color affordance; pair fine teal text with a heavier weight or darken to Teal 600 (#007065) for AA body." },
        { "foreground": "#00897B", "background": "#1A237E", "ratio": "3.07:1", "wcag_aa": false, "wcag_aaa": false, "use": "Teal on blue — large text & UI components only." },
        { "foreground": "#FFFFFF", "background": "#F57C00", "ratio": "2.70:1", "wcag_aa": false, "wcag_aaa": false, "use": "FORBIDDEN for text — documented as the trap to avoid; never put white text on orange." }
      ]
    },
    "usage_guidelines": {
      "primary": {
        "do": [
          "Use Deep Quantum Blue as the anchor field and as primary heading color on light surfaces.",
          "Pair it with white or Neutral 50 text for high-contrast, trustworthy reading.",
          "Let it dominate the dark-first system alongside the cool dark neutrals."
        ],
        "dont": [
          "Don't use it for long body text on dark canvases (use white/Neutral 50 instead).",
          "Don't dilute it with purple — never blend toward the avoided SaaS purple family.",
          "Don't apply gradients from blue to purple/magenta."
        ]
      },
      "secondary": {
        "do": [
          "Use Mindful Gray for metadata, borders, dividers, and scaffolding.",
          "Use it for secondary text on light surfaces (9.65:1 on white).",
          "Use its neutral ramp for elevation and card surfaces in dark mode."
        ],
        "dont": [
          "Don't use Mindful Gray as primary text directly on the dark canvas — it reads as structure there, not text.",
          "Don't let scaffolding gray compete with the teal signal for attention."
        ]
      },
      "accent": {
        "do": [
          "Reserve Energetic Orange for the single most important action (the CTA / ignition) and always label it with Deep Quantum Blue text.",
          "Use Consciousness Teal as the working signal color for links, active states, focus, and data emphasis.",
          "Use Growth Light as a small bright positive-signal accent on dark fields."
        ],
        "dont": [
          "Don't put white text on Energetic Orange (2.70:1 — fails).",
          "Don't spread orange across large areas or use it as a background — it stops reading as ignition.",
          "Don't use teal for fine body text on white without darkening to Teal 600 or adding weight."
        ]
      }
    },
    "avoid_list": {
      "colors": [
        "#7C3AED — generic SaaS purple (and the whole bright-purple family); avoid purple-on-white sameness entirely.",
        "High-saturation magenta/violet gradients.",
        "Pure #000000 as the dark canvas — use the cool near-black Neutral 900 (#0A0E14) instead so it harmonizes with the deep blue anchor.",
        "Warm beige/cream paper tones that fight the cool system."
      ],
      "patterns": [
        "Purple-to-blue or purple-to-pink gradients (reads as default startup).",
        "White text on the orange CTA.",
        "Large orange or large Growth Light fields (signal colors must stay scarce).",
        "Rainbow / multi-hue data palettes — keep data viz to teal + Growth Light + neutral ramp, with orange only for the single highlighted series."
      ]
    }
  }
}
```

### competitor-analysis
```json
{
  "skill": "competitor-analysis",
  "cluster": "foundation",
  "wave": 1,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "competitors": [
      {
        "name": "Large innovation consultancies",
        "type": "direct",
        "price": "Premium — six- to seven-figure engagements with multi-layer teams and long procurement cycles",
        "value_proposition": "De-risked innovation for the enterprise through proven process, scale, and institutional credibility.",
        "target_audience": "Enterprise transformation, R&D, and innovation units inside large organizations with heavy procurement.",
        "key_features": ["Process frameworks and playbooks", "Enterprise credibility and references", "Large multidisciplinary benches", "Procurement and compliance comfort"],
        "positioning": {
          "headline": "Enterprise innovation, de-risked at scale",
          "category_claimed": "Innovation and transformation consultancy"
        },
        "strengths": ["Strong process packaging and repeatable methodology", "Enterprise credibility that clears internal approval", "Comfort with large-organization procurement and risk", "Deep benches across many disciplines"],
        "weaknesses": ["Weak intimacy — founders rarely touch the senior people they bought", "Slow velocity from layered account management", "Unclear ownership and accountability from concept to handoff", "Coherence diluted as work passes between large teams"],
        "customer_sentiment": {
          "praise_points": ["Safe, defensible choice for a board", "Comprehensive frameworks and documentation", "Brand-name credibility"],
          "complaints": ["Expensive and slow", "Junior staff doing the actual work", "Strategy that never connects to anything shipped"]
        }
      },
      {
        "name": "Premium product design agencies",
        "type": "direct",
        "price": "Premium — high day-rates and polished project fees focused on design deliverables",
        "value_proposition": "Beautiful, best-in-class product and interface craft with presentation-grade polish.",
        "target_audience": "Funded startups and brand-led teams that want standout interface design and presentation quality.",
        "key_features": ["High-craft interface and visual design", "Strong presentation and storytelling", "Design systems and brand expression", "Portfolio of awarded work"],
        "positioning": {
          "headline": "World-class product design and craft",
          "category_claimed": "Premium product / experience design agency"
        },
        "strengths": ["Exceptional interface craft and visual polish", "Strong narrative and presentation quality", "Mature design-systems thinking", "Distinct aesthetic reputation"],
        "weaknesses": ["Weaker engineering ownership — designs handed off, not shipped end to end", "Limited real AI and automation integration", "Thin operational tooling and handoff rigor", "Can be beautiful but slow, with work that breaks at implementation"],
        "customer_sentiment": {
          "praise_points": ["Stunning visual output", "Great to show investors", "Strong design taste"],
          "complaints": ["Designs that engineering couldn't ship as drawn", "Slow timelines", "Hands off and disappears before the system actually runs"]
        }
      },
      {
        "name": "AI integration consultancies",
        "type": "direct",
        "price": "Mid-market to premium — scoped AI implementation and tooling engagements",
        "value_proposition": "Faster, more efficient operations by integrating current AI tooling into your stack.",
        "target_audience": "Operators chasing efficiency gains and teams under pressure to 'add AI' quickly.",
        "key_features": ["Current model and tooling expertise", "Efficiency and automation narratives", "Rapid proof-of-concept demos", "Integration with existing data and APIs"],
        "positioning": {
          "headline": "Put AI to work across your business",
          "category_claimed": "AI integration / implementation consultancy"
        },
        "strengths": ["Up-to-date on current tooling and models", "Fast to a working demo", "Clear efficiency and cost narratives", "Comfortable with technical integration"],
        "weaknesses": ["Weak product experience and user-behavior thinking", "AI bolted on as a demo layer, not built into product logic", "Little attention to founder workflow or narrative", "No durable brand or system memory after the engagement"],
        "customer_sentiment": {
          "praise_points": ["Impressive early demos", "Knows the latest tools", "Quick to start"],
          "complaints": ["Demo that never matured into a real product", "Operationally naive about how teams actually work", "No design or experience depth"]
        }
      },
      {
        "name": "Specialized engineering vendors",
        "type": "indirect",
        "price": "Mid-market — scoped build contracts or staff-augmentation rates",
        "value_proposition": "Reliable, focused technical execution for a defined build.",
        "target_audience": "Teams with an already-specified product who need engineering capacity to build it.",
        "key_features": ["Narrow, deep technical execution", "Defined-scope delivery", "Engineering capacity on demand", "Stack-specific expertise"],
        "positioning": {
          "headline": "Engineering that ships your spec",
          "category_claimed": "Software engineering / development vendor"
        },
        "strengths": ["Strong, focused technical execution", "Predictable delivery against a clear spec", "Deep expertise in chosen stacks", "Cost-efficient for well-defined builds"],
        "weaknesses": ["Weak when requirement, user behavior, interface, and system all must align", "No requirement shaping — builds the spec it's handed, even if flawed", "Little product or design judgment", "Founder still owns coherence across the whole problem"],
        "customer_sentiment": {
          "praise_points": ["Got the build done", "Solid engineers", "Did what was asked"],
          "complaints": ["Built exactly what we specified, including our mistakes", "No push-back on the wrong requirement", "Needed someone else to own the experience"]
        }
      },
      {
        "name": "Freelancer swarms",
        "type": "indirect",
        "price": "Budget to mid-market — assembled per-hour from multiple independent contractors",
        "value_proposition": "Flexible, low-overhead access to specialists, assembled on demand.",
        "target_audience": "Cost-sensitive founders piecing together a team without committing to one firm.",
        "key_features": ["Flexible specialist access", "Low fixed overhead", "Scales up and down quickly", "Wide skill coverage on paper"],
        "positioning": {
          "headline": "On-demand specialists, assembled your way",
          "category_claimed": "Freelance / talent-marketplace network"
        },
        "strengths": ["Maximum flexibility and low overhead", "Quick to spin specialists up or down", "Cost control for small budgets", "Broad nominal skill coverage"],
        "weaknesses": ["Client becomes the integrator and single point of coherence", "Accountability fragments across many independents", "No shared model of the problem", "Quality and continuity vary engagement to engagement"],
        "customer_sentiment": {
          "praise_points": ["Affordable and flexible", "Found niche skills fast", "No long contracts"],
          "complaints": ["I became the project manager and integrator", "Nobody owned the whole thing", "Coherence and quality fell apart across people"]
        }
      }
    ],
    "feature_matrix": {
      "features": [
        "Requirement framing before build",
        "User-behavior / adoption design",
        "End-to-end engineering ownership",
        "Integrated (not bolted-on) AI and automation",
        "Handoff as a first-class output (docs, training, control surfaces)",
        "Single accountable owner of coherence",
        "Founder-led / low translation loss",
        "Editorial / distinct visual-verbal territory"
      ],
      "comparison": {
        "our_product": [true, true, true, true, true, true, true, true],
        "competitors": {
          "Large innovation consultancies": [true, true, false, false, false, false, false, false],
          "Premium product design agencies": [false, true, false, false, false, false, false, true],
          "AI integration consultancies": [false, false, true, true, false, false, false, false],
          "Specialized engineering vendors": [false, false, true, false, false, false, false, false],
          "Freelancer swarms": [false, false, false, false, false, false, false, false]
        }
      }
    },
    "whitespace": {
      "unmet_needs": [
        "One studio that owns narrative framing and technical delivery together, so coherence survives all the way to launch",
        "AI built into the product's real logic and user experience rather than bolted on as a demo layer",
        "A premium visual and verbal identity that does not come at the cost of technical seriousness",
        "Ownership transfer designed in from the start, so the system can be run by the client's team rather than locking them to a vendor"
      ],
      "missing_features": [
        "Handoff and decision systems (documentation, training, control surfaces) delivered as part of the build, not as post-project admin",
        "Requirement architecture that reshapes a flawed spec before engineering, instead of building it as handed over",
        "A single accountable owner of coherence across requirement, behavior, product, and delivery"
      ],
      "underserved_segments": [
        "System-carrying founders who need fewer vendors and sharper accountability, not more specialists to coordinate",
        "Innovation and technical teams who want integrated thinking over performative specialization",
        "Buyers who are skeptical of buzzwords and pay for competence once trust is earned through evidence of shipping"
      ]
    },
    "differentiation": {
      "genuine_differences": [
        "Carries framing, user behavior, product, engineering, and handoff in one founder-led delivery loop, so coherence is never lost between vendors",
        "Treats handoff as a first-class output — the engagement ends in a system the client can run, extend, and inherit, not a dependency",
        "Keeps user-behavior and adoption thinking grounded in real engineering, so the experience survives implementation",
        "Operates as a studio-plus-IP, with reusable product IP and a distinct visual-verbal territory beyond generic agency sameness"
      ],
      "ownable_territory": "Editorial precision with operating clarity — the one founder-led studio that turns a single requirement into a coherent system you can own, framed in calm, signal-rich, technically grounded Digital Wilderness language no competitor category can credibly claim.",
      "unfair_advantage": "Founder-led, cross-disciplinary judgment under one roof: the same senior operators frame the requirement, design for adoption, ship the engineering, and build the handoff — removing the translation loss that every single-slice competitor structurally depends on."
    },
    "positioning_statement": "Unlike single-slice vendors — consultancies that package process but never ship, design agencies that hand off before the system runs, AI shops that stop at a demo, engineering vendors that build the spec as handed over, and freelancer swarms that make the founder the integrator — Thoughtseed carries the requirement, the user, the product, the engineering, and the handoff in one founder-led delivery loop, because coherence and ownership cannot be assembled from disconnected parts after the fact."
  }
}
```

### deliverables-package
```json
{
  "skill": "deliverables-package",
  "cluster": "synthesis",
  "wave": 7,
  "timestamp": "2026-06-08T06:10:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "package_info": {
      "name": "thoughtseed-brand-package",
      "path": "deliverables/thoughtseed-brand-package/",
      "brand": "Thoughtseed",
      "created": "2026-06-08T06:10:00Z",
      "brandmint_version": "2.0.0",
      "package_version": "1.0.0"
    },
    "asset_manifest": {
      "loaded": true,
      "valid": true,
      "manifest_source": ".brandmint/asset-manifest.json",
      "user_provided_assets": 4,
      "generated_assets": 16,
      "all_paths_verified": true
    },
    "formats": ["folder", "zip", "pdf"],
    "folder_structure": [
      "thoughtseed-brand-package/README.md",
      "thoughtseed-brand-package/MANIFEST.json",
      "thoughtseed-brand-package/ASSET-ORIGINS.md",
      "thoughtseed-brand-package/01-Brand-Guidelines/",
      "thoughtseed-brand-package/02-Logo/user-provided/",
      "thoughtseed-brand-package/03-Colors/",
      "thoughtseed-brand-package/04-Typography/",
      "thoughtseed-brand-package/05-Photography/generated/",
      "thoughtseed-brand-package/06-Product/generated/",
      "thoughtseed-brand-package/07-Illustrations/generated/",
      "thoughtseed-brand-package/08-Patterns/generated/",
      "thoughtseed-brand-package/09-Copy/",
      "thoughtseed-brand-package/10-Social-Media/generated/",
      "thoughtseed-brand-package/11-NotebookLM/",
      "thoughtseed-brand-package/12-Wiki/",
      "thoughtseed-brand-package/_source/outputs/"
    ],
    "contents": {
      "documents": {
        "count": 11,
        "origin": "deterministic",
        "origin_note": "Generated deterministically from validated skill outputs; no AI image generation involved in these artifacts.",
        "items": [
          { "path": "01-Brand-Guidelines/thoughtseed-brand-identity.pdf", "type": "pdf", "source_skills": ["brand-documentation"], "origin": "deterministic" },
          { "path": "01-Brand-Guidelines/thoughtseed-product-positioning.pdf", "type": "pdf", "source_skills": ["brand-documentation"], "origin": "deterministic" },
          { "path": "01-Brand-Guidelines/thoughtseed-campaign-guidelines.pdf", "type": "pdf", "source_skills": ["brand-documentation"], "origin": "deterministic" },
          { "path": "03-Colors/palette.css", "type": "css", "source_skills": ["color-palette"], "origin": "deterministic" },
          { "path": "03-Colors/palette.json", "type": "json", "source_skills": ["color-palette"], "origin": "deterministic" },
          { "path": "04-Typography/typography-guide.md", "type": "markdown", "source_skills": ["typography"], "origin": "deterministic" },
          { "path": "09-Copy/landing-page-copy.md", "type": "markdown", "source_skills": ["landing-page-copy"], "origin": "deterministic" },
          { "path": "09-Copy/product-description.md", "type": "markdown", "source_skills": ["product-description"], "origin": "deterministic" },
          { "path": "09-Copy/ad-creative-copy.md", "type": "markdown", "source_skills": ["ad-creative-copy"], "origin": "deterministic" },
          { "path": "09-Copy/press-release.md", "type": "markdown", "source_skills": ["press-release"], "origin": "deterministic" },
          { "path": "09-Copy/email-sequences.md", "type": "markdown", "source_skills": ["launch-email-sequence", "prelaunch-email-sequence", "welcome-email-sequence"], "origin": "deterministic" }
        ]
      },
      "user_provided_assets": {
        "count": 4,
        "origin": "user_provided",
        "category": "02-Logo",
        "items": [
          { "id": "logo-wordmark", "manifest_path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "package_path": "02-Logo/user-provided/thoughtseed-horizontal-wordmark-3x.png", "type": "logo", "deterministic": true, "required": true },
          { "id": "logo-tree-mark", "manifest_path": "./assets/thoughtseed-tree-mark-black-3x.png", "package_path": "02-Logo/user-provided/thoughtseed-tree-mark-black-3x.png", "type": "logo-icon", "deterministic": true, "required": false },
          { "id": "logo-reference-01", "manifest_path": "./assets/thoughtseed-logo-reference-01.jpg", "package_path": "02-Logo/user-provided/thoughtseed-logo-reference-01.jpg", "type": "reference", "deterministic": true, "required": false },
          { "id": "logo-reference-02", "manifest_path": "./assets/thoughtseed-logo-reference-02.jpg", "package_path": "02-Logo/user-provided/thoughtseed-logo-reference-02.jpg", "type": "reference", "deterministic": true, "required": false }
        ]
      },
      "generated_assets": {
        "count": 16,
        "origin": "generated",
        "model": "gemini-3-pro-image-preview",
        "items": [
          { "id": "hero-01-digital-wilderness", "manifest_path": "./generated/hero-01-digital-wilderness.png", "package_path": "05-Photography/generated/hero-01-digital-wilderness.png", "type": "hero", "deterministic": false, "wave": 4, "skill": "hero-images" },
          { "id": "hero-02-establishing", "manifest_path": "./generated/hero-02-establishing.png", "package_path": "05-Photography/generated/hero-02-establishing.png", "type": "hero", "deterministic": false, "wave": 4, "skill": "hero-images" },
          { "id": "hero-03-mobile", "manifest_path": "./generated/hero-03-mobile.png", "package_path": "05-Photography/generated/hero-03-mobile.png", "type": "hero", "deterministic": false, "wave": 4, "skill": "hero-images" },
          { "id": "lifestyle-01-worktable", "manifest_path": "./generated/lifestyle-01-worktable.png", "package_path": "05-Photography/generated/lifestyle-01-worktable.png", "type": "lifestyle", "deterministic": false, "wave": 4, "skill": "lifestyle-photography" },
          { "id": "lifestyle-02-studio", "manifest_path": "./generated/lifestyle-02-studio.png", "package_path": "05-Photography/generated/lifestyle-02-studio.png", "type": "lifestyle", "deterministic": false, "wave": 4, "skill": "lifestyle-photography" },
          { "id": "product-01-system-artifacts", "manifest_path": "./generated/product-01-system-artifacts.png", "package_path": "06-Product/generated/product-01-system-artifacts.png", "type": "product", "deterministic": false, "wave": 4, "skill": "product-photography" },
          { "id": "product-02-screen-surface", "manifest_path": "./generated/product-02-screen-surface.png", "package_path": "06-Product/generated/product-02-screen-surface.png", "type": "product", "deterministic": false, "wave": 4, "skill": "product-photography" },
          { "id": "illus-01-systems-organism", "manifest_path": "./generated/illus-01-systems-organism.png", "package_path": "07-Illustrations/generated/illus-01-systems-organism.png", "type": "illustration", "deterministic": false, "wave": 5, "skill": "brand-illustrations" },
          { "id": "illus-02-delivery-loop", "manifest_path": "./generated/illus-02-delivery-loop.png", "package_path": "07-Illustrations/generated/illus-02-delivery-loop.png", "type": "illustration", "deterministic": false, "wave": 5, "skill": "brand-illustrations" },
          { "id": "icons-01-sheet", "manifest_path": "./generated/icons-01-sheet.png", "package_path": "07-Illustrations/generated/icons-01-sheet.png", "type": "icons", "deterministic": false, "wave": 5, "skill": "icon-system" },
          { "id": "pattern-01-dark", "manifest_path": "./generated/pattern-01-dark.png", "package_path": "08-Patterns/generated/pattern-01-dark.png", "type": "pattern", "deterministic": false, "wave": 5, "skill": "pattern-library" },
          { "id": "pattern-02-light", "manifest_path": "./generated/pattern-02-light.png", "package_path": "08-Patterns/generated/pattern-02-light.png", "type": "pattern", "deterministic": false, "wave": 5, "skill": "pattern-library" },
          { "id": "social-ig-story", "manifest_path": "./generated/social-ig-story.png", "package_path": "10-Social-Media/generated/social-ig-story.png", "type": "social", "deterministic": false, "wave": 4, "skill": "social-media-assets" },
          { "id": "social-og", "manifest_path": "./generated/social-og.png", "package_path": "10-Social-Media/generated/social-og.png", "type": "social", "deterministic": false, "wave": 4, "skill": "social-media-assets" },
          { "id": "social-x-header", "manifest_path": "./generated/social-x-header.png", "package_path": "10-Social-Media/generated/social-x-header.png", "type": "social", "deterministic": false, "wave": 4, "skill": "social-media-assets" },
          { "id": "visual-language-board", "manifest_path": "./generated/visual-language-board.png", "package_path": "07-Illustrations/generated/visual-language-board.png", "type": "moodboard", "deterministic": false, "wave": 3, "skill": "visual-language" }
        ]
      },
      "data": {
        "count": 28,
        "origin": "deterministic",
        "items": [
          { "path": "_source/outputs/", "type": "directory", "description": "All 26 prior spoke JSON outputs plus the 4 synthesis outputs", "origin": "deterministic" },
          { "path": "_source/asset-manifest.json", "type": "json", "description": "Validated asset manifest, copied", "origin": "deterministic" },
          { "path": "MANIFEST.json", "type": "json", "description": "Package inventory with validation", "origin": "deterministic" }
        ]
      }
    },
    "origin_tracking": {
      "asset_origins_generated": true,
      "user_provided_clearly_marked": true,
      "generated_clearly_marked": true,
      "deterministic_assets_identified": 4,
      "folder_convention": "Image categories split into user-provided/ and generated/ subfolders; documents and data are deterministic, generated from validated skill JSON without AI image synthesis.",
      "asset_origins_summary": {
        "user_provided": {
          "count": 4,
          "deterministic": true,
          "description": "Provided by the brand owner, exactly as supplied, not modified or AI-generated. The two canonical logo marks plus two mark reference images.",
          "ids": ["logo-wordmark", "logo-tree-mark", "logo-reference-01", "logo-reference-02"]
        },
        "generated": {
          "count": 16,
          "deterministic": false,
          "model": "gemini-3-pro-image-preview",
          "description": "Created by AI image generation during waves 3-5. Hero, lifestyle, product, illustration, icon, pattern, social, and moodboard assets. Art direction and creative suggestions that may warrant human review; none contain baked-in text or logos.",
          "by_skill": {
            "hero-images": 3,
            "lifestyle-photography": 2,
            "product-photography": 2,
            "brand-illustrations": 2,
            "icon-system": 1,
            "pattern-library": 2,
            "social-media-assets": 3,
            "visual-language": 1
          }
        },
        "deterministic_documents_and_data": {
          "description": "PDF guidelines, copy markdown, color/type tokens, JSON outputs, and the manifest are produced deterministically from validated skill outputs. Always accurate, never AI-image-generated.",
          "document_count": 11,
          "data_artifacts": ["all spoke JSON outputs", "asset-manifest.json", "MANIFEST.json", "ASSET-ORIGINS.md", "README.md"]
        }
      }
    },
    "totals": {
      "folders": 13,
      "documents": 11,
      "user_provided_images": 4,
      "generated_images": 16,
      "total_image_assets": 20
    },
    "outputs": {
      "manifest_path": "MANIFEST.json",
      "readme_path": "README.md",
      "asset_origins_path": "ASSET-ORIGINS.md"
    },
    "exports": {
      "folder": {
        "path": "deliverables/thoughtseed-brand-package/",
        "created": true,
        "verified": true
      },
      "zip": {
        "path": "deliverables/thoughtseed-brand-package.zip",
        "created": true,
        "contains_only_manifest_assets": true
      },
      "pdf": {
        "documents": [
          "deliverables/thoughtseed-brand-package/01-Brand-Guidelines/thoughtseed-brand-identity.pdf",
          "deliverables/thoughtseed-brand-package/01-Brand-Guidelines/thoughtseed-product-positioning.pdf",
          "deliverables/thoughtseed-brand-package/01-Brand-Guidelines/thoughtseed-campaign-guidelines.pdf"
        ]
      }
    },
    "validation": {
      "all_paths_exist": true,
      "all_referenced_assets_in_manifest": true,
      "hallucinated_paths": 0,
      "missing_required": 0,
      "missing_paths": [],
      "warnings": []
    }
  }
}
```

### hero-images
```json
{
  "skill": "hero-images",
  "cluster": "photography",
  "wave": 4,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "Hero stages render the Digital Wilderness duality at campaign scale: a dark-first, cool-anchored field where architectural precision (concrete, glass, brushed aluminium, structured crops) is held against cultivated, living texture (weathered stone, living moss, oxidized copper). Each frame carries one teal signal network and at most one warm golden-orange ignition point so the signal stays legible. Compositions are editorial-documentary stills with controlled hard shadow, intentional negative space, and architectural crops. The negative space is deliberate so headline copy can be overlaid later in layout — never baked into the image.",
      "model": "gemini-3-pro-image-preview",
      "lighting": "A single shaft of cool screen-glow light, controlled architectural shadow, clean high contrast, shallow depth of field; never flat or over-lit.",
      "color_treatment": "Cool cast anchored to Deep Quantum Blue (#1A237E) shading toward near-black (#0A0E14), with restrained teal (#00897B) signal lines and a single Energetic Orange (#F57C00) ignition accent. Desaturated, not candy-bright.",
      "composition": "Architectural crops, asymmetric framing, generous intentional negative space sized for downstream headline overlay; strong horizon/vertical lines; one signal moment per frame.",
      "mood": "Calm, intentional, grounded, signal-rich; founder-led and technically precise, not aspirational-glossy."
    },
    "text_overlay_policy": "Hero frames are built with deliberate dark negative space (left or low in frame) for headline/CTA overlay applied in layout. NO text, lettering, words, or logos are baked into any generated image. Approved overlay copy from the brief: headline 'Digital Wilderness'; tagline 'We plant ideas. They grow wild.'; CTA 'Bring the requirement.'",
    "assets": [
      {
        "id": "hero-01-digital-wilderness",
        "path": "./generated/hero-01-digital-wilderness.png",
        "aspect_ratio": "16:9",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "description": "Primary landing-page hero. Full-bleed cinematic Digital Wilderness stage: a deep quantum blue-black field shading to near-black, architectural shadow, a single shaft of cool screen-glow light. Foreground tactile material study where matte black paper and a brushed-aluminium panel meet weathered stone and a small patch of living moss; fine teal signal lines and a faint node network trace the surfaces with one warm golden-orange ignition point. Disciplined engineering precision meeting organic emergence.",
        "prompt": "Editorial brand hero image, \"Digital Wilderness\" art direction for a founder-led engineering systems studio. Full-bleed cinematic stage: deep quantum blue-black background shading toward near-black, architectural shadow, a single shaft of cool screen-glow light. Foreground is a tactile material study where matte black paper and a brushed-aluminum panel meet weathered stone and a small patch of living moss; fine teal signal lines and a faint network of directional nodes trace across the surfaces, with one warm golden-orange ignition point. Disciplined engineering precision meeting organic emergence. Editorial, signal-rich, premium, restrained, with intentional negative space and an architectural crop, shot like an editorial-documentary still, clean high contrast, shallow depth of field. Absolutely no text, no words, no letters, no logos anywhere. No purple gradients, no stock people, no glossy plastic, no sci-fi cliche, no mystical fog.",
        "text_safe_zones": { "left": true, "center": false, "right": false, "bottom": true },
        "cta_placement": "bottom-left",
        "priority": "high",
        "usage": ["landing-page-hero", "press-kit", "campaign-key-visual"]
      },
      {
        "id": "hero-02-establishing",
        "path": "./generated/hero-02-establishing.png",
        "aspect_ratio": "16:9",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "description": "Wide establishing brand stage: an architectural interior corner where a structured concrete-and-glass surface meets a cultivated patch of moss and stone on a matte work surface; a single shaft of cool light falls across it; a faint network of teal nodes drifts through the empty negative space on the left, sized for headline overlay.",
        "prompt": "A wide establishing brand stage: an architectural interior corner where a structured concrete-and-glass surface meets a cultivated patch of moss and stone on a matte work surface; a single shaft of cool light falls across it; a faint network of teal nodes drifts through the empty negative space on the left.",
        "text_safe_zones": { "left": true, "center": false, "right": false, "bottom": false },
        "cta_placement": "left",
        "priority": "high",
        "usage": ["secondary-hero", "section-header", "social-cover", "press-kit"]
      },
      {
        "id": "hero-03-mobile",
        "path": "./generated/hero-03-mobile.png",
        "aspect_ratio": "9:16",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "description": "Tall vertical brand hero stage for mobile: a shaft of cool light falling onto a rolled matte-paper scroll and a brushed-aluminium edge meeting weathered stone and moss at the base; fine teal signal lines rise upward through deep dark negative space, with one small golden-orange ignition point low in the frame and calm empty space for top-aligned headline overlay.",
        "prompt": "A tall vertical brand hero stage for mobile: a shaft of cool light falling onto a rolled matte-paper scroll and a brushed-aluminum edge meeting weathered stone and moss at the base, fine teal signal lines rising upward through deep dark negative space, one small golden-orange ignition point low in the frame.",
        "text_safe_zones": { "top": true, "center": false, "bottom": false },
        "cta_placement": "top",
        "priority": "high",
        "usage": ["mobile-hero", "instagram-story-cover", "vertical-ad"]
      }
    ],
    "requirements": [
      { "placement": "Landing page hero", "aspect_ratio": "16:9", "purpose": "First impression / primary brand stage", "needs_text_zone": true },
      { "placement": "Establishing / section header", "aspect_ratio": "16:9", "purpose": "Brand presence, secondary scenes, press use", "needs_text_zone": true },
      { "placement": "Mobile / vertical hero", "aspect_ratio": "9:16", "purpose": "Mobile-first hero and story-format brand stage", "needs_text_zone": true }
    ],
    "quality_gates": {
      "all_images_generated": true,
      "prompts_documented": true,
      "brand_alignment": "Colors and editorial-documentary style match the Digital Wilderness visual language; dark-first cool field with single teal/orange signal.",
      "technical_quality": "2K resolution, shallow depth of field, clean high contrast.",
      "text_safe_zones_specified": true,
      "no_baked_text_or_logos": true,
      "forbidden_visuals_avoided": true
    },
    "generation_summary": { "total_shots": 3, "generated": 3, "pending": 0, "model": "gemini-3-pro-image-preview" }
  }
}
```

### icon-system
```json
{
  "skill": "icon-system",
  "cluster": "illustration",
  "wave": 5,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "The icon system is one cohesive sheet of about twelve minimal geometric line icons sharing a single thin teal stroke and one construction logic on a deep blue-black field. Marks are abstract and engineered — seed-and-growth, a loop, a node network, a layered system, framing/requirement, and handoff — never cartoonish and never lettered. The set reads as a system built by people who think in systems: precise, legible, palette-disciplined. This sheet is the reference set; production icons are cut to a 24x24 grid from this construction.",
      "model": "gemini-3-pro-image-preview"
    },
    "style_definition": {
      "type": "line",
      "stroke_weight": "2px standard, 1.5px at small sizes — uniform across the set",
      "corner_radius": "2px (near-sharp) — precise and engineered, lightly softened",
      "grid_size": "24x24 base, scaled to 16 / 32 / 48",
      "padding": "2px (20x20 live area on the 24px grid)",
      "line_caps": "round",
      "line_joins": "round",
      "optical_adjustments": "yes — weight balanced optically across the set",
      "colors": {
        "primary": "#00897B",
        "secondary": "#37474F",
        "field": "#0A0E14",
        "active_signal": "#00897B",
        "rule": "Neutral gray by default; teal for active/signal. Never the ignition orange except on a true primary action; never recolored into gradients."
      }
    },
    "categories": {
      "ui": ["menu", "close", "search", "settings", "arrow", "check", "share", "user"],
      "feature": ["requirement-architecture (framing)", "product-and-interface-systems (layered system)", "handoff-and-decision-systems (handoff)", "node-network", "delivery-loop"],
      "category": ["seed-and-growth", "document/diagram type", "system map"]
    },
    "assets": [
      {
        "id": "icons-01-sheet",
        "path": "./generated/icons-01-sheet.png",
        "aspect_ratio": "1:1",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "type": "icon-sheet",
        "description": "A cohesive system of about twelve minimal geometric line icons on a tidy grid: abstract marks for seed-and-growth, a loop, a node network, a layered system, framing or requirement, and handoff, all drawn with one consistent thin teal stroke on deep blue-black, precise and engineered, never cartoonish.",
        "prompt": "A cohesive system of about twelve minimal geometric line icons on a tidy grid: abstract marks for seed-and-growth, a loop, a node network, a layered system, framing or requirement, and handoff, all drawn with one consistent thin teal stroke on deep blue-black, precise and engineered, never cartoonish.",
        "contains_icon_concepts": ["seed-and-growth", "loop", "node-network", "layered-system", "framing/requirement", "handoff", "and additional system marks to ~12 total"],
        "usage": ["icon-reference-sheet", "feature-section-icons", "ui-icons", "diagram-legends", "deck"]
      }
    ],
    "export_formats": ["svg", "png"],
    "export_note": "The generated sheet is a single 1:1 reference grid. Production cuts each mark to its own SVG on the 24x24 grid and exports PNG at 16/24/32/48/64/96; no text is ever baked into any icon.",
    "size_variants": ["16", "24", "32", "48", "64", "96"],
    "quality_gates": {
      "style_definition_matches_visual_language": true,
      "feature_icons_defined": "requirement architecture, product & interface systems, handoff & decision systems present as abstract marks.",
      "common_ui_icons_included": true,
      "consistent_style_across_set": "Single thin teal stroke, one construction logic, one grid.",
      "legible_at_16px": "Near-sharp 2px construction holds at small sizes; 1.5px variant for 16px.",
      "colors_limited_to_palette": true,
      "no_cartoon_iconography": true,
      "no_baked_text_or_logos": true,
      "export_formats_specified": true,
      "all_images_generated": true,
      "prompts_documented": true
    },
    "generation_summary": { "total_icons": 1, "generated": 1, "pending": 0, "icon_concepts_on_sheet": 12, "model": "gemini-3-pro-image-preview" }
  }
}
```

### landing-page-copy
```json
{
  "skill": "landing-page-copy",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "page_type": "homepage",
    "hero": {
      "section_label": "00 / Digital Wilderness",
      "headline": "Digital Wilderness",
      "subhead": "Build the system, not just the story.",
      "product_pitch": "Thoughtseed is a founder-led systems studio. We turn complex requirements into coherent systems by aligning user behavior, founder operating logic, interface design, and technical delivery. One loop, from requirement to handoff.",
      "supporting_line": "We plant ideas. They grow wild.",
      "cta_button": "Bring the requirement.",
      "cta_url": "/start",
      "metadata_strip": [
        "studio / founder-led",
        "scope / requirement → handoff",
        "range / web · mobile · AI · automation · connected products"
      ]
    },
    "delivery_loop": {
      "section_label": "01 / Delivery Loop",
      "headline": "One coherent delivery loop.",
      "subhead": "Requirement to handoff, carried by one team that shares a single model of the problem.",
      "intro": "Most studios pass your problem between specialists and lose coherence at every seam. We hold it in one motion. Each stage feeds the next, and the same people who frame the requirement ship the system and hand it back.",
      "stages": [
        {
          "step": "01",
          "name": "Requirement",
          "annotation": "in: the entangled problem",
          "body": "We study the requirement, the people who will use it, and the way you want to run it. Constraints and tradeoffs surface before anything is built."
        },
        {
          "step": "02",
          "name": "System",
          "annotation": "design + behavior",
          "body": "We design the interface and the operating logic together. User behavior is treated as part of the system, not a layer added later."
        },
        {
          "step": "03",
          "name": "Build",
          "annotation": "engineering delivery",
          "body": "Senior engineers ship the system. What we framed is what we build, so the work stays legible from the first decision to the running product."
        },
        {
          "step": "04",
          "name": "Handoff",
          "annotation": "out: a system you can run",
          "body": "Documentation, training, and control surfaces ship with the build. You inherit a system you can run, extend, and own without us."
        }
      ],
      "closing_line": "From requirement to handoff. Nothing gets lost between vendors, because there are no vendors in between."
    },
    "work": {
      "section_label": "02 / Work",
      "headline": "What we carry.",
      "subhead": "Three service modules under one operating logic. Engaged together, not stitched from separate teams.",
      "services": [
        {
          "module_id": "M-01",
          "name": "Requirement Architecture",
          "headline": "Frame it before you build it.",
          "body": "Problem framing, psychology mapping, operating constraints, and decision logic, settled before implementation. You see the real problem and the real decision pressure first.",
          "template_used": "3"
        },
        {
          "module_id": "M-02",
          "name": "Product & Interface Systems",
          "headline": "Build it so it gets used.",
          "body": "Web, mobile, AI, automation, and connected-product execution, with user behavior treated as part of the system. Adoption logic and build reality stay aligned.",
          "template_used": "2"
        },
        {
          "module_id": "M-03",
          "name": "Handoff & Decision Systems",
          "headline": "Hand it back so you can run it.",
          "body": "Documentation, training, control surfaces, and operational artifacts that make the delivered work inheritable. Handoff is a first-class output, not post-project admin.",
          "template_used": "1"
        }
      ],
      "engagement_models": [
        {
          "name": "System Sprint",
          "summary": "A short, high-leverage framing or prototype cycle that clarifies the requirement and de-risks the next build decision."
        },
        {
          "name": "Requirement-to-Handoff Build",
          "summary": "Scoped delivery from framing through implementation and ownership transfer. Fewer projects, deeper integration, a real handoff at the end."
        }
      ]
    },
    "proof": {
      "section_label": "03 / Proof",
      "headline": "Evidence stays close to the claim.",
      "subhead": "We pair atmosphere with proof: shipped systems, technical range, and the artifacts a client can actually run.",
      "proof_points": [
        "Shipped work across AI, IoT, web, mobile, and creative technology.",
        "Live client delivery paired with reusable internal product IP.",
        "Service surfaces that already span framing, design, engineering, and handoff.",
        "Decision artifacts and handoff documents that prove the loop is real."
      ],
      "case_record_template": {
        "note": "Records render in mono with legible metadata.",
        "fields": [
          "client",
          "year",
          "tags",
          "tech",
          "proof",
          "handoff"
        ]
      },
      "testimonials": [
        "[Founder testimonial placeholder — relief that one partner finally held the whole problem.]",
        "[CTO testimonial placeholder — coherence held from framing through the running system.]",
        "[Innovation lead testimonial placeholder — ownership transfer that actually worked.]"
      ],
      "trust_badges": [
        "[Client logo placeholder]",
        "[Client logo placeholder]",
        "[Client logo placeholder]"
      ],
      "media_mentions": [
        "[Press / feature placeholder]"
      ]
    },
    "handoff": {
      "section_label": "04 / Handoff",
      "headline": "The work is yours to run.",
      "subhead": "A system that works on launch day but breaks at ownership transfer is not finished. We treat that transfer as the deliverable.",
      "body": "We ship the documentation, the training, and the control surfaces with the build. You get a system you can operate, extend, and inherit, not a dependency on the people who built it. Ownership over dependency, every time.",
      "what_you_inherit": [
        "A running system, not a deck disconnected from shipped reality.",
        "Documentation written to be read by the team that will run it.",
        "Control surfaces and operational artifacts that keep the system legible.",
        "A model of the problem you can carry forward without us."
      ]
    },
    "cta": {
      "section_label": "05 / Start",
      "headline": "Bring the requirement.",
      "subhead": "If the problem is too entangled to split across vendors, bring it here. We will study it, build the system, and hand it back in a form you can run.",
      "body": "Start with a System Sprint to frame and de-risk the requirement, or scope a Requirement-to-Handoff Build for full delivery. Either way, you talk to the operators doing the work.",
      "button": "Bring the requirement.",
      "button_url": "/start",
      "secondary_link": {
        "text": "See how the delivery loop works",
        "url": "/delivery-loop"
      }
    },
    "faq": [
      {
        "question": "This sounds broad. What exactly do you do?",
        "answer": "The breadth is a deliberate studio shape for problems that cross product, interface, and technical delivery. We take fewer engagements and go deeper, carrying one requirement from framing to a system you can run, rather than staffing every slice."
      },
      {
        "question": "How is this different from an agency?",
        "answer": "The delivery loop. Fewer projects, deeper integration, and a real handoff instead of open-ended account farming. We are not an always-on retainer. We frame the requirement, build the system, and transfer ownership."
      },
      {
        "question": "What does \"user psychology\" mean here? It sounds soft.",
        "answer": "It means trust, adoption, founder workflow, and user behavior grounded in engineering reality. We treat behavior as part of the system, then test it against what ships."
      },
      {
        "question": "How do I know premium framing is not hiding shallow delivery?",
        "answer": "Evidence sits next to the claim. Shipped systems, technical range across AI, IoT, web, and mobile, concrete project surfaces, and the handoff artifacts you can actually run."
      },
      {
        "question": "How do we start?",
        "answer": "Bring the requirement. We usually begin with a System Sprint to frame and de-risk it, then scope a Requirement-to-Handoff Build if the path is clear."
      }
    ],
    "final_cta": {
      "headline": "Bring the requirement.",
      "body": "One studio carries framing, behavior, product, execution, and handoff inside a single loop. You get a coherent system you can own, not a stack of disconnected deliverables.",
      "button": "Bring the requirement."
    },
    "meta": {
      "title": "Thoughtseed — Founder-led systems studio, from requirement to handoff",
      "description": "Thoughtseed turns complex requirements into coherent systems by aligning user behavior, founder operating logic, interface design, and technical delivery. One delivery loop, from requirement to handoff. Bring the requirement.",
      "og_title": "Thoughtseed — Build the system, not just the story.",
      "og_description": "A founder-led systems studio for problems that cannot be split across disconnected vendors. We study the requirement, build the system, and hand it back in a form you can run."
    }
  }
}
```

### launch-email-sequence
```json
{
  "skill": "launch-email-sequence",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "sequence_strategy": {
      "context": "Sent during the open window when Thoughtseed Studio is taking new requirements for a build round. Drives founders to bring a requirement before the limited capacity fills.",
      "campaign_length": "Open window, roughly 14 days from open to close",
      "total_emails": 6,
      "goals": [
        "Open the window with a clear, calm announcement",
        "Show the studio shape and the two ways to engage",
        "Use real proof, not pressure, to build confidence",
        "Make the requirement-gathering step easy",
        "Communicate genuine capacity limits as the window narrows",
        "Close the window cleanly without manufactured panic"
      ],
      "voice_note": "Urgency comes from real, limited build capacity, never manufactured scarcity. Calm confidence over celebration. Short declarative sentences. No FOMO theater, no superlatives, no avoided terms."
    },
    "emails": [
      {
        "number": 1,
        "name": "Window Open",
        "send_timing": "Day 1",
        "primary_lever": "Clarity",
        "urgency_level": "medium",
        "subject_lines": {
          "primary": "Thoughtseed Studio is open. Bring the requirement.",
          "variation_a": "The door is open for new builds",
          "variation_b": "One studio, from requirement to handoff, now taking work"
        },
        "preview_text": "Limited builds this round. The list goes first.",
        "body": "It is open.\n\nThoughtseed Studio is taking new requirements for this build round, starting today.\n\nHere is the short version. Thoughtseed is a founder-led systems studio. One team carries framing, user behavior, product, engineering, and handoff inside a single delivery loop. We study the requirement, build the system, and hand it back in a form your team can run.\n\nTwo ways to start:\n\n- System Sprint: a short framing or prototype cycle that clarifies the requirement and de-risks the next build decision.\n- Requirement-to-Handoff Build: scoped delivery from framing through implementation and ownership transfer.\n\nWe take a limited number of builds at a time, on purpose. If you have a problem too entangled to split across vendors, bring it now.",
        "cta": {
          "text": "Bring the requirement.",
          "url_placeholder": "{{start_url}}"
        },
        "ps": "P.S. You talk to the operators doing the work, from the first conversation onward."
      },
      {
        "number": 2,
        "name": "How It Runs",
        "send_timing": "Day 3",
        "primary_lever": "Studio shape",
        "urgency_level": "low",
        "subject_lines": {
          "primary": "What carrying it whole actually looks like",
          "variation_a": "Requirement, system, build, handoff",
          "variation_b": "Where each decision gets made"
        },
        "preview_text": "Four stages, one motion, nothing lost between vendors.",
        "body": "If you are weighing whether to bring a requirement this round, here is how the work runs.\n\nFour stages, one continuous loop.\n\n1. Requirement. We study the problem, the people who will use the system, and how you want to run it. Constraints surface before anything is built.\n2. System. We design the interface and the operating logic together. User behavior is treated as part of the system, not a layer added later.\n3. Build. Senior engineers ship it. What we framed is what we build, so the work stays legible the whole way.\n4. Handoff. Documentation, training, and control surfaces ship with the build. You inherit a system you can run, extend, and own without us.\n\nThe same people carry it from the first decision to the running product. That is the difference between one studio and a stack of vendors.",
        "cta": {
          "text": "See the delivery loop in detail",
          "url_placeholder": "{{delivery_loop_url}}"
        },
        "ps": "P.S. Not sure which engagement fits? Bring the requirement and we will tell you whether a System Sprint or a full build is the right first move."
      },
      {
        "number": 3,
        "name": "Proof, Not Pressure",
        "send_timing": "Day 6",
        "primary_lever": "Evidence",
        "urgency_level": "low",
        "subject_lines": {
          "primary": "Evidence sits next to the claim",
          "variation_a": "Shipped work, real range, real handoff",
          "variation_b": "How to tell framing from delivery"
        },
        "preview_text": "Shipped across AI, IoT, web, mobile, and creative technology.",
        "body": "Premium language can hide shallow delivery. So instead of pressure, here is proof.\n\nShipped work across AI, IoT, web, mobile, and creative technology. Live client delivery paired with reusable internal product IP. Service surfaces that already span framing, design, engineering, and handoff. Decision artifacts and handoff documents that prove the loop is real.\n\nThe part most studios skip is the part we treat as the deliverable: ownership transfer. When we hand back the work, your team inherits documentation written to be read, control surfaces that keep the system legible, and a model of the problem you can carry forward without us.\n\nThat is what you are buying. Not a deck. A coherent system you can run.",
        "cta": {
          "text": "See shipped work and handoff artifacts",
          "url_placeholder": "{{proof_url}}"
        },
        "ps": "P.S. The build calendar for this round is filling. Bringing the requirement now keeps your spot open while we scope it."
      },
      {
        "number": 4,
        "name": "Bring The Messy Version",
        "send_timing": "Day 9",
        "primary_lever": "Lower the barrier",
        "urgency_level": "medium",
        "subject_lines": {
          "primary": "You do not need it polished to bring it",
          "variation_a": "Half-formed requirements are welcome",
          "variation_b": "Framing the problem is part of the work"
        },
        "preview_text": "We are built for entangled problems. Bring the tangle.",
        "body": "A reason founders wait: the requirement is not clean yet.\n\nIt does not need to be. Framing the requirement is the first part of the work, not a prerequisite for starting. We are built for problems that are too entangled to split, so the messy version is exactly what we want to see.\n\nIf you have them, it helps to bring the problem in your own words, who will use the system, how you want to own the result, any hard constraints, and what a good outcome looks like to you. If you only have some of that, bring what you have.\n\nThe window for this round is open now and capacity is limited. Bringing the requirement does not commit you to a full build. It starts the conversation with the people who would do the work.",
        "cta": {
          "text": "Bring the requirement.",
          "url_placeholder": "{{start_url}}"
        },
        "ps": "P.S. Start with a System Sprint if you want to de-risk the hard decision before committing to a full build."
      },
      {
        "number": 5,
        "name": "Capacity Narrowing",
        "send_timing": "Day 12",
        "primary_lever": "Real scarcity",
        "urgency_level": "high",
        "subject_lines": {
          "primary": "Capacity for this round is nearly full",
          "variation_a": "A few build slots left this round",
          "variation_b": "The window closes in two days"
        },
        "preview_text": "We take a limited number of builds at a time.",
        "body": "A straight update, because we would want one.\n\nCapacity for this build round is nearly full. We take a limited number of builds at a time, on purpose, so when the slots are gone, they are gone until the next round.\n\nThe window closes in two days. If you have been waiting for the requirement to feel ready, bring it as it is. We will frame it with you. If a System Sprint is the right first step, we will say so. If the timing is wrong, we will tell you that too.\n\nThis is scoped delivery with a real handoff, not an open-ended retainer. The point of carrying fewer projects is that the ones we take get our full attention.",
        "cta": {
          "text": "Bring the requirement.",
          "url_placeholder": "{{start_url}}"
        },
        "ps": "P.S. If now is not the time, reply and we will hold a place for you on the list for the next round."
      },
      {
        "number": 6,
        "name": "Window Closing",
        "send_timing": "Day 14",
        "primary_lever": "Clean close",
        "urgency_level": "high",
        "subject_lines": {
          "primary": "Last day to bring a requirement this round",
          "variation_a": "The window closes tonight",
          "variation_b": "Final call for this build round"
        },
        "preview_text": "After today, the next opening is a future round.",
        "body": "Today is the last day to bring a requirement for this round.\n\nNo pressure tactics here, just the facts. After today, this build round closes and the remaining slots are filled. The next chance to start is a future round, and the list will hear about it first.\n\nIf you have a problem that is too entangled to split across vendors, and you want one studio to carry it from framing to a system you can own, bring it before the window closes. The messy version is fine. You will talk to the operators doing the work.\n\nWe frame the requirement, build the system, and hand it back in a form you can run. Build the system, not just the story.",
        "cta": {
          "text": "Bring the requirement.",
          "url_placeholder": "{{start_url}}"
        },
        "ps": "P.S. Not ready this round? Reply and stay on the list. We would rather start at the right time than the rushed one."
      }
    ]
  }
}
```

### lifestyle-photography
```json
{
  "skill": "lifestyle-photography",
  "cluster": "photography",
  "wave": 4,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "Lifestyle frames document the founder-operator's working reality rather than staging people. They show the environment and objects of a systems studio — worktables carrying matte-paper schematics, brushed-metal tools, devices turned to abstract interface glow, and a single cultivated stone-and-moss detail. Editorial-documentary treatment: architectural daylight mixed with screen glow, clean contrast, intentional arrangement. Every scene reads as built by people who think in systems and ship them, with no faces and no stock-startup perfection.",
      "model": "gemini-3-pro-image-preview",
      "lighting": "Natural, directional architectural daylight mixed with screen glow; controlled clean shadow for depth; never flat or over-lit.",
      "color_treatment": "Cool cast anchored to deep blue-black and cool grays; desaturated, with restrained teal signal accents occurring naturally in interfaces and equipment.",
      "composition": "Low three-quarter and interior establishing crops, asymmetric, structure-forward, intentional negative space.",
      "mood": "Calm, intentional, grounded, founder-led and technical, not aspirational-glossy."
    },
    "subject_direction": {
      "demographics": "No people / no faces shown. Brand presence is carried by environment, working surfaces, and objects — the founder-operator implied, never posed.",
      "style": "Editorial-documentary; tactile real materials (matte paper, brushed metal, weathered stone, living moss, screen glow); intentional arrangement over incidental clutter.",
      "expression": "N/A — environment-and-object storytelling rather than human expression.",
      "diversity_notes": "By deliberately avoiding figures, the frames sidestep stock-photo casting clichés; representation is handled elsewhere in the brand system, not through staged lifestyle people."
    },
    "scenarios": [
      { "id": "lifestyle-01-worktable", "name": "Founder-operator worktable", "setting": "A founder-operator's worktable seen from a low three-quarter angle", "activity": "System schematics, precise tools, and a device in active working context; a stone-and-moss paperweight grounding the scene", "mood": "Focused, grounded, technically precise", "key_message": "Real systems work happens here — requirement made tangible on the table." },
      { "id": "lifestyle-02-studio", "name": "Quiet systems studio interior", "setting": "A quiet systems studio: structured shelving and a long worktable", "activity": "Architectural daylight mixed with screen glow over intentional, arranged materials and a single cultivated plant detail", "mood": "Calm, ordered, intentional", "key_message": "A studio built like a system: structured, alive, and deliberate." }
    ],
    "assets": [
      {
        "id": "lifestyle-01-worktable",
        "path": "./generated/lifestyle-01-worktable.png",
        "aspect_ratio": "3:2",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "scenario": "Founder-operator worktable",
        "angle": "low three-quarter",
        "crop": "detail / tabletop",
        "description": "Editorial-documentary still of a founder-operator's worktable from a low three-quarter angle: matte-paper system schematics carrying faint abstract geometric diagrams, a brushed-metal rule and precise tools, a laptop turned away showing only an abstract dark interface glow, and a small stone-and-moss object used as a paperweight. No faces, no people.",
        "prompt": "An editorial-documentary still of a founder-operator's worktable seen from a low three-quarter angle: matte-paper system schematics carrying faint abstract geometric diagrams, a brushed-metal rule and precise tools, a laptop turned away showing only an abstract dark interface glow, and a small stone-and-moss object used as a paperweight. No faces, no people.",
        "priority": "high",
        "usage": ["about-page", "process-section", "case-study", "social"]
      },
      {
        "id": "lifestyle-02-studio",
        "path": "./generated/lifestyle-02-studio.png",
        "aspect_ratio": "3:2",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "scenario": "Quiet systems studio interior",
        "angle": "interior establishing",
        "crop": "wide / environmental",
        "description": "Editorial-documentary interior of a quiet systems studio: structured shelving and a long worktable, architectural daylight mixed with screen glow, tactile materials and a single cultivated plant detail, everything arranged and intentional rather than incidental. No people.",
        "prompt": "An editorial-documentary interior of a quiet systems studio: structured shelving and a long worktable, architectural daylight mixed with screen glow, tactile materials and a single cultivated plant detail, everything arranged and intentional rather than incidental. No people.",
        "priority": "high",
        "usage": ["about-page", "studio-section", "press-kit", "background"]
      }
    ],
    "quality_gates": {
      "scenarios_reflect_persona": "Frames reflect the System-Carrying Founder's working reality — systems on the table, ownership of the build — without staged people.",
      "style_matches_visual_language": true,
      "aspect_ratios_appropriate": "3:2 editorial format for hero/about/case-study placements.",
      "no_stock_photo_cliches": true,
      "no_baked_text_or_logos": true,
      "forbidden_visuals_avoided": true,
      "all_images_generated": true,
      "prompts_documented": true
    },
    "generation_summary": { "total_shots": 2, "generated": 2, "pending": 0, "model": "gemini-3-pro-image-preview" }
  }
}
```

### logo-concept
```json
{
  "skill": "logo-concept",
  "cluster": "identity",
  "wave": 3,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "mode": "codify-existing",
    "codification_note": "This spoke does NOT invent or generate a new logo. Thoughtseed's marks already exist and are canonical. This file codifies correct usage of the two existing marks. Any generated emboss, seal, or poster imagery in the generated/ directory is art-direction reference only and is NEVER a replacement mark, an alternate logo, or a logo lockup. Use only the canonical asset files below as the actual logo.",
    "canonical_marks": {
      "wordmark": {
        "name": "Horizontal wordmark",
        "asset": "assets/thoughtseed-horizontal-wordmark-3x.png",
        "type": "wordmark",
        "role": "primary",
        "description": "The full Thoughtseed name set horizontally. This is the default mark for most surfaces: site headers, document mastheads, decks, signatures, and any context with adequate horizontal room.",
        "use_when": "There is enough horizontal space and the brand must be named in full, e.g. page headers, footers, title slides, letterheads, email signatures, proposal and contract mastheads."
      },
      "tree_mark": {
        "name": "Tree mark (black)",
        "asset": "assets/thoughtseed-tree-mark-black-3x.png",
        "type": "symbol",
        "role": "secondary / standalone symbol",
        "description": "The standalone tree symbol. Carries the 'Digital Wilderness — we plant ideas, they grow wild' idea as a compact, recognizable mark. Used where the wordmark will not fit or where a square/compact mark is required.",
        "use_when": "Square or compact contexts: app icons, avatars, favicons, social profile marks, watermarks, loading states, embossed cover details, or as a quiet repeating motif on collateral."
      },
      "reference_assets": {
        "note": "Canonical visual references for the marks. Do not regenerate, redraw, or vectorize these into a 'new' logo — they document the existing mark.",
        "files": [
          "assets/thoughtseed-logo-reference-01.jpg",
          "assets/thoughtseed-logo-reference-02.jpg"
        ]
      }
    },
    "logo_type": {
      "primary": "wordmark + standalone symbol (two canonical marks, used as a system rather than a single locked combination)",
      "rationale": "The name 'Thoughtseed' is distinctive enough to carry a wordmark, while the tree symbol gives a compact, ownable mark for square and small contexts. Keeping them as two deliberate marks — rather than one fixed lockup — fits a founder-led systems studio that values restraint and legibility over decorative branding."
    },
    "symbolism": {
      "brand_attributes": [
        "cross-disciplinary",
        "founder-led",
        "precise",
        "editorial",
        "grounded"
      ],
      "visual_concepts": [
        "a planted idea that grows into a structured system",
        "architectural precision meeting cultivated, living growth",
        "from requirement to handoff as a single rooted, branching form"
      ],
      "symbol_meaning": "The tree mark reads as a seed that has grown structure: roots (the requirement and operating reality), trunk (the delivery loop), and branches (the shipped, inheritable system). It states the Digital Wilderness duality — disciplined engineering and organic emergence — without any literal text or slogan baked into the mark."
    },
    "style_direction": {
      "complexity": "simple — reductive, single-weight, no gradients or ornament",
      "weight": "medium — confident strokes that hold at small sizes",
      "shape": "balanced — geometric structure carrying an organic, grown silhouette",
      "style": "modern-editorial — restrained, founder-led, not decorative",
      "mood": "serious and calm — grounded, intentional, signal over noise"
    },
    "color_treatment": {
      "default": "Monochrome. The tree mark ships black (#0A0E14 cool near-black) on light surfaces and reversed to white (#FFFFFF) on dark/anchor surfaces.",
      "anchor_surface": "On the Deep Quantum Blue (#1A237E) or dark canvas (#0A0E14), use the white/reversed mark.",
      "light_surface": "On white or Neutral 50 (#F8F9F9) paper, use the black mark.",
      "accent_rule": "Do not recolor the mark into teal, orange, or green. Brand accent colors (#00897B teal signal, #F57C00 ignition, #B8E986 growth) belong to the surrounding system — links, CTAs, signal — not to the logo itself. The mark stays monochrome so it reads as a stable identity anchor while the accents do the signalling.",
      "single_exception": "If a single-color reproduction must carry brand color (e.g. a one-ink emboss), Deep Quantum Blue (#1A237E) is the only permitted non-neutral, and only for the full mark in isolation — never mid-layout beside live teal/orange signal."
    },
    "clear_space": {
      "wordmark": "Minimum clear space on all four sides equal to the cap-height of the 'T' in the wordmark. Nothing — text, image edge, fold, or other mark — may enter this zone.",
      "tree_mark": "Minimum clear space on all four sides equal to one quarter of the mark's height (0.25x). Prefer 0.5x where layout allows for a calmer, more editorial frame.",
      "principle": "Negative space is part of the identity. When in doubt, give the mark more room, not less."
    },
    "minimum_sizes": {
      "wordmark_digital": "Minimum 120px wide on screen so the wordmark stays legible. Below this, switch to the tree mark.",
      "wordmark_print": "Minimum 28mm wide in print.",
      "tree_mark_digital": "Minimum 24px height on screen (favicon/app contexts may go to 16px only when no smaller-legible alternative exists and the silhouette still reads).",
      "tree_mark_print": "Minimum 8mm height in print.",
      "rule": "If the wordmark cannot meet its minimum, do not shrink it — substitute the tree mark."
    },
    "surface_treatments": {
      "matte_paper": "Black ink on matte uncoated stock is the signature print treatment — editorial, tactile, no gloss. Use the black wordmark or tree mark. A blind or single-ink deboss of the tree mark is encouraged for covers and closeout documents.",
      "brushed_metal": "On brushed aluminium or oxidized-copper surfaces, use a clean reversed (etched/engraved) tree mark. Let the material's grain and patina supply texture; keep the mark itself crisp and unembellished.",
      "dark_textured": "On dark textured fields (architectural shadow, weathered stone, screen-glow darks), use the white/reversed mark with generous clear space so it holds against the texture. Never drop a busy texture inside the mark's clear-space zone.",
      "glass_and_screen": "On glass or live screen surfaces, the reversed mark sits on the dark-first canvas (#0A0E14); maintain full clear space and never place it over high-frequency imagery."
    },
    "generated_art_disclaimer": "Generated emboss, seal, and poster artwork (e.g. anything under generated/) are mood and art-direction references that show how the mark might feel on a surface. They are NOT the logo, NOT approved lockups, and must never be exported, traced, or shipped as the mark. Production always uses the canonical asset files named in canonical_marks.",
    "usage_specs": {
      "minimum_size": "Wordmark 120px / 28mm wide; tree mark 24px / 8mm tall (16px favicon floor only when silhouette still reads).",
      "clear_space": "Wordmark: 1x cap-height of 'T' on all sides. Tree mark: 0.25x height minimum (0.5x preferred).",
      "color_variations": [
        "black_on_light",
        "white_reversed_on_dark",
        "single_ink_deep_quantum_blue_for_isolated_emboss_only"
      ],
      "color_locked": "Monochrome only in layout; accent colors never applied to the mark.",
      "do": [
        "Use the canonical asset files as the only real logo.",
        "Give the mark its full clear space and keep it monochrome.",
        "Switch from wordmark to tree mark when space is tight rather than shrinking below minimum size.",
        "Reverse to white on dark/anchor surfaces; keep black on light paper.",
        "Let surface material (matte paper, brushed metal, dark texture) carry the texture while the mark stays crisp."
      ],
      "dont_do": [
        "Do not generate, redraw, or substitute a new logo or alternate mark.",
        "Do not treat generated emboss/seal/poster art as a replacement or approved lockup.",
        "Do not recolor the mark into teal, orange, green, or any gradient.",
        "Do not stretch, skew, rotate, add shadows, outlines, or glows to the mark.",
        "Do not place the mark on a busy texture or image without preserving full clear space.",
        "Do not shrink the wordmark below its legibility minimum — use the tree mark instead.",
        "Do not bake the tagline or any text into the symbol; the tree mark stands alone.",
        "Do not put the mark inside a colored badge that competes with the system's teal/orange signal."
      ]
    }
  }
}
```

### messaging-framework
```json
{
  "skill": "messaging-framework",
  "cluster": "strategy",
  "wave": 2,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "brand_promise": "One coherent system from requirement to handoff.",
    "value_proposition": "Thoughtseed turns complex requirements into coherent systems by aligning user psychology, founder operating logic, interface design, and technical delivery, then hands back a system the client can run.",
    "headline": "Digital Wilderness",
    "tagline": {
      "selected": "We plant ideas. They grow wild.",
      "type": "imperative",
      "alternatives": [
        "Build the system, not just the story.",
        "From requirement to handoff.",
        "One coherent delivery loop.",
        "Bring the requirement."
      ]
    },
    "elevator_pitch": {
      "full": "Founders carry important work that gets split across strategy, design, engineering, and operations vendors who never share one model of the problem. Thoughtseed is a founder-led systems studio that carries the whole requirement instead. We study the requirement, the user, and how you want to run the result, then design, build, and hand back a coherent system you can own. Unlike single-slice agencies, we keep it in one delivery loop with senior judgment. Bring the requirement.",
      "components": {
        "problem": "Important work gets split across vendors who do not share one model of the problem, so coherence breaks before launch and ownership breaks after it.",
        "solution": "A founder-led systems studio that carries requirement, behavior, product, engineering, and handoff in one delivery loop.",
        "differentiator": "One integrated studio logic with founder-led judgment, and handoff treated as part of the system.",
        "proof": "Shipped systems across AI, IoT, web, mobile, and creative technology, delivered with the artifacts a client needs to run them."
      }
    },
    "elevator_pitches": {
      "10_second": "Thoughtseed is a founder-led systems studio. We turn a complex requirement into a coherent system you can run, from framing to handoff.",
      "30_second": "Founders end up as the full-time translator between strategy, design, engineering, and operations vendors who never share one model of the problem. Thoughtseed carries the whole requirement instead. We study the requirement, the user, and your operating reality, then design, build, and hand back a coherent system you can own. One delivery loop, senior judgment, real handoff.",
      "60_second": "In view of how most important work gets built, the founder becomes the integrator. Strategy goes to one vendor, design to another, engineering to a third, operations to a fourth, and none of them share one model of the problem. Coherence leaks at every handoff, and the system that worked on launch day falls apart at ownership transfer. Thoughtseed is a founder-led systems studio built for problems that cannot be split this way. We align user psychology, founder operating logic, interface design, and engineering delivery inside one loop, and we treat handoff as a first-class output. You get a coherent system, documented and operable, that your team can run, extend, and inherit. We ship across AI, IoT, web, mobile, and creative technology. Bring the requirement."
    },
    "one_liner": "A founder-led systems studio that turns complex requirements into coherent systems you can own.",
    "key_messages": [
      {
        "pillar": "One coherent loop",
        "headline": "One studio carries the whole requirement, framing to handoff",
        "supporting_copy": "Most work fragments across vendors who never share one model of the problem. Thoughtseed keeps requirement, behavior, interface, and engineering in a single delivery loop, so coherence survives all the way to launch.",
        "proof_points": [
          "Requirement, design, engineering, and handoff happen under one operating logic",
          "Service surfaces already span framing, design, engineering, and delivery",
          "Fewer engagements, deeper integration, no vendor stack for the founder to manage"
        ]
      },
      {
        "pillar": "Founder-led judgment",
        "headline": "Senior operators do the work, so less is lost in translation",
        "supporting_copy": "The people framing the requirement are the people building it. Founder-led judgment replaces layered account management, which means decisions stay close to the work and to the founder's operating reality.",
        "proof_points": [
          "Senior team engaged directly, not mediated through account managers",
          "Decisions documented as artifacts you can trace",
          "Built by operators who have shipped systems and lived with ambiguity"
        ]
      },
      {
        "pillar": "Behavior as part of the system",
        "headline": "User psychology grounded in what actually ships",
        "supporting_copy": "Trust and adoption are treated as engineering concerns, not afterthoughts. We map how people will use the system and design for that, then test it against the build, so the work holds up in the real operating environment.",
        "proof_points": [
          "Psychology mapping and operating constraints set before implementation",
          "Adoption and trust treated as part of the system, not post-launch polish",
          "Behavioral framing stays grounded in build reality"
        ]
      },
      {
        "pillar": "Handoff you can run",
        "headline": "Ownership transfer is the output, not the afterthought",
        "supporting_copy": "A system that works on launch day but breaks at handoff has not been delivered. Documentation, training, and control surfaces ship with the build, so your team can run, extend, and inherit the work without us.",
        "proof_points": [
          "Documentation, training, and control surfaces ship with the system",
          "Handoff and decision artifacts make delivered work inheritable",
          "Scoped delivery with real ownership transfer, not an open-ended retainer"
        ]
      }
    ],
    "value_pillars": [
      {
        "name": "One coherent loop",
        "headline": "One studio carries the whole requirement, framing to handoff",
        "supporting_copy": "Most work fragments across vendors who never share one model of the problem. Thoughtseed keeps requirement, behavior, interface, and engineering in a single delivery loop, so coherence survives all the way to launch.",
        "proof_points": [
          "Requirement, design, engineering, and handoff happen under one operating logic",
          "Service surfaces already span framing, design, engineering, and delivery",
          "Fewer engagements, deeper integration, no vendor stack to manage"
        ]
      },
      {
        "name": "Founder-led judgment",
        "headline": "Senior operators do the work, so less is lost in translation",
        "supporting_copy": "The people framing the requirement are the people building it. Founder-led judgment replaces layered account management, so decisions stay close to the work and to the founder's operating reality.",
        "proof_points": [
          "Senior team engaged directly, not mediated through account managers",
          "Decisions documented as artifacts you can trace",
          "Built by operators who have shipped systems"
        ]
      },
      {
        "name": "Behavior in the system",
        "headline": "User psychology grounded in what actually ships",
        "supporting_copy": "Trust and adoption are engineering concerns. We map how people will use the system, design for it, and test it against the build so the work holds in the real operating environment.",
        "proof_points": [
          "Psychology mapping and operating constraints set before implementation",
          "Adoption and trust treated as part of the system",
          "Behavioral framing stays grounded in build reality"
        ]
      },
      {
        "name": "Handoff you can run",
        "headline": "Ownership transfer is the output, not the afterthought",
        "supporting_copy": "A system that breaks at handoff has not been delivered. Documentation, training, and control surfaces ship with the build, so your team can run, extend, and inherit the work.",
        "proof_points": [
          "Documentation, training, and control surfaces ship with the system",
          "Handoff and decision artifacts make delivered work inheritable",
          "Scoped delivery with real ownership transfer"
        ]
      }
    ],
    "message_matrix": {
      "social_media": {
        "message": "Important work shouldn't be split across five vendors who never share one model of the problem. One studio, one delivery loop, a system you can own. Bring the requirement.",
        "tone": "Short, declarative, grounded"
      },
      "email_subject": {
        "message": "From requirement to handoff, in one loop",
        "tone": "Direct, concrete"
      },
      "landing_page": {
        "message": "Digital Wilderness. Thoughtseed turns complex requirements into coherent systems by aligning user psychology, founder operating logic, interface design, and technical delivery. Bring the requirement.",
        "tone": "Spare, atmospheric, confident"
      },
      "press_release": {
        "message": "Thoughtseed is a founder-led systems studio that carries complex requirements from framing through implementation to a handoff the client can run, across AI, IoT, web, mobile, and creative technology.",
        "tone": "Factual, restrained, newsworthy"
      },
      "sales": {
        "message": "Tell us the requirement. We'll study it, frame it, build the system, and hand it back in a form your team can run, extend, and inherit, without you becoming the translator between vendors.",
        "tone": "Consultative, confident, concrete"
      }
    },
    "objection_responses": {
      "This sounds broad.": "The breadth is a deliberate studio shape for problems that cross product, interface, and technical delivery. We take fewer engagements and go deeper, rather than staffing every slice.",
      "This sounds like an agency.": "The difference is the delivery loop. Fewer projects, deeper integration, and a real handoff instead of open-ended account farming. We are not an always-on retainer.",
      "Psychology language can feel fuzzy.": "Here it means trust, adoption, founder workflow, and user behavior grounded in engineering reality. We treat behavior as part of the system, then test it against what ships.",
      "Premium language can hide shallow delivery.": "We pair atmosphere with evidence: shipped systems, technical range, concrete project surfaces, and the handoff artifacts your team can actually run."
    },
    "proof_points": {
      "statistics": [
        "Thoughtseed was planted in 2020 and has grown across multiple technology disciplines since",
        "One delivery loop replaces a stack of four or more disconnected vendors"
      ],
      "testimonials": [
        "Reserve for verified client quotes. Until populated, lead with shipped work and handoff artifacts rather than unattributed praise.",
        "Founder-side reference quotes about reduced translation burden and clean ownership transfer, once cleared for use."
      ],
      "credentials": [
        "Shipped systems across AI, IoT, web, mobile, and creative technology",
        "Live client delivery paired with reusable internal product IP",
        "Public service surfaces spanning framing, design, engineering, and handoff"
      ],
      "demonstrations": [
        "Before: the founder translates between strategy, design, engineering, and operations vendors. After: one studio holds the whole requirement",
        "Decision artifacts and handoff documents that show the delivery loop is real",
        "Systems that remain operable by the client's own team after delivery"
      ],
      "guarantees": [
        "Handoff is a first-class output: documentation, training, and control surfaces ship with the system",
        "Scoped delivery with explicit ownership transfer, not an open-ended retainer"
      ]
    }
  }
}
```

### notebooklm-publishing
```json
{
  "skill": "notebooklm-publishing",
  "cluster": "synthesis",
  "wave": 7,
  "timestamp": "2026-06-08T06:10:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "brand": "Thoughtseed",
    "manifest_source": ".brandmint/asset-manifest.json",
    "pipeline": {
      "stage1_transform": {
        "description": "Skill outputs transformed into categorized narrative prose, written as the brand. Sources are PROSE summaries, never raw JSON. Voice follows voice-and-tone: clear, grounded, crafted, with evidence next to the claim and no avoided terms.",
        "synthesis_voice": "founder-side systems translator",
        "categories_processed": ["brand-identity", "product-strategy", "voice-messaging", "campaign-content", "visual-catalog"],
        "sources_generated": 5,
        "fallback_used": false,
        "sources": [
          {
            "category": "brand-identity",
            "source_skills": ["brand-foundation", "color-palette", "typography", "logo-concept"],
            "source_doc": ".brandmint/sources/brand-identity/thoughtseed-brand-identity.md",
            "format": "prose",
            "prose": "Thoughtseed is a founder-led systems studio whose essence is coherent systems, cultivated. The identity reads as Sage with a Creator's hands: it earns trust through clarity and coherence, then ships what it frames. Its visible system is built for restraint. Two canonical marks work together rather than as a single lockup: a horizontal wordmark for headers and mastheads, and a standalone tree mark for square and compact contexts. The marks stay monochrome — black on light, reversed white on the dark or deep-blue field — and never take accent color. The palette is dark-first and cool-anchored: a deep indigo-blue and a cool near-black carry long-horizon trust, a blue-gray supplies scaffolding and metadata, a teal is the working signal, a single warm orange is reserved for the primary call-to-action so its scarcity reads as ignition, and a soft green marks positive emergence. Type is a three-role system — a display face for hero thresholds, an editorial serif as the reading voice, and a monospace as the load-bearing data layer of labels and numbering — so the page reads as an editorial publication built by engineers. Across all of it, one calm signal beats visual noise.",
            "word_count": 198,
            "path_validated": true
          },
          {
            "category": "product-strategy",
            "source_skills": ["product-positioning", "value-proposition", "buyer-persona", "competitor-analysis"],
            "source_doc": ".brandmint/sources/product-strategy/thoughtseed-product-strategy.md",
            "format": "prose",
            "prose": "Thoughtseed defines the founder-led systems studio: the studio that carries a complex requirement all the way to a system the client can own, instead of selling a single slice of strategy, design, or engineering. Its primary value is a single accountable owner of coherence from requirement to handoff, which ends the founder's exhausting role as the full-time translator between five specialists. The buyer is Mira, the System-Carrying Founder — a founder, CTO, innovation lead, or product strategist running a lean senior team, controlling a six-figure project budget, skeptical of buzzwords and pitch theater, who pays for competence once trust is earned through specificity. Her jobs to be done: frame a problem too entangled to split, ship a product real users adopt, add AI without it being a demo that never matures, and own the system after the engagement. The competitive field is five single-slice alternatives, each structurally dependent on translation loss — consultancies that package process but rarely ship, design agencies that hand off before the system runs, AI shops that stop at a demo, engineering vendors that build the spec as handed over, and freelancer swarms that make the founder the integrator. The ownable territory is editorial precision with operating clarity, and the unfair advantage is that the same senior operators frame, design for adoption, ship the engineering, and build the handoff.",
            "word_count": 226,
            "path_validated": true
          },
          {
            "category": "voice-messaging",
            "source_skills": ["voice-and-tone", "messaging-framework", "brand-story"],
            "source_doc": ".brandmint/sources/voice-messaging/thoughtseed-voice-messaging.md",
            "format": "prose",
            "prose": "Thoughtseed speaks as the founder-side systems translator: an operator who has built systems and lived with ambiguity, peer to peer with the founder, in short declarative sentences with evidence close to every claim. The voice is clear, grounded, and crafted, and it describes the downstream effects of the work — clearer requirements, calmer execution, stronger trust and adoption, cleaner ownership transfer — rather than the internal method behind them. The brand promise is one coherent system from requirement to handoff. The public headline is Digital Wilderness and the tagline is We plant ideas. They grow wild. Four message pillars carry everything: one coherent loop, founder-led judgment, behavior as part of the system, and handoff you can run. The origin story holds the whole arc: planted in 2020 from the observation that the problems worth solving were never single-discipline problems, Thoughtseed answered fragmentation with a single delivery loop where the same senior operators frame the requirement, design for adoption, ship the engineering, and build the handoff. Nothing is thrown over a wall, because there is no wall. The enemy is fragmentation; the promised land is a coherent system the founder owns and the team can run. Build the system, not just the story. Bring the requirement.",
            "word_count": 206,
            "path_validated": true
          },
          {
            "category": "campaign-content",
            "source_skills": ["landing-page-copy", "product-description", "ad-creative-copy", "press-release", "launch-email-sequence", "prelaunch-email-sequence", "welcome-email-sequence"],
            "source_doc": ".brandmint/sources/campaign-content/thoughtseed-campaign-content.md",
            "format": "prose",
            "prose": "Thoughtseed's campaign surfaces run as a calm editorial sequence. The homepage moves through a numbered arc — Hero, Delivery Loop, Work, Proof, Handoff, Start — opening on Digital Wilderness with the line Build the system, not just the story, and the supporting note We plant ideas. They grow wild. The delivery loop is told in four stages: Requirement, where the entangled problem and its constraints surface before anything is built; System, where interface and operating logic are designed together with user behavior treated as part of the system; Build, where senior engineers ship what was framed; and Handoff, where documentation, training, and control surfaces ship with the build so the client inherits a system they can run. Product copy describes Thoughtseed Studio from a twenty-two-word micro line up to a full narrative, always landing on one coherent system from requirement to handoff and ownership over dependency. Two engagement models recur: a System Sprint to frame and de-risk the next decision, and a Requirement-to-Handoff Build for scoped delivery through ownership transfer. Email sequences and ad creative carry the same pillars and approved phrases; the press release stays factual, restrained, and newsworthy. Every call to action resolves to: Bring the requirement.",
            "word_count": 201,
            "path_validated": true
          },
          {
            "category": "visual-catalog",
            "source_skills": ["visual-language", "hero-images", "lifestyle-photography", "product-photography", "brand-illustrations", "icon-system", "pattern-library", "social-media-assets"],
            "source_doc": ".brandmint/sources/visual-catalog/thoughtseed-visual-catalog.md",
            "format": "prose",
            "prose": "Thoughtseed's visual territory is Digital Wilderness: architectural precision held against cultivated texture, structured layouts against alive surfaces, with neither side winning. Five principles govern the work — architectural precision against cultivated texture, signal over noise, negative space as structure, material truth over gloss, and show the system. Materials run matte paper, black ink, glass, brushed aluminium, oxidized copper, weathered stone, living moss, screen glow, and architectural shadow. The visual catalog comprises a moodboard that fixes the mood and material range; three hero compositions including the primary Digital Wilderness hero, an establishing crop, and a mobile crop; two lifestyle scenes of a worktable and a studio; two product compositions of system artifacts and a screen surface; two illustrations rendering a systems-organism and the delivery loop; an icon construction sheet; and two patterns for dark and light fields, plus social cards for open-graph, profile header, and story formats. Photography is editorial documentary with a cool desaturated cast and at most one signal accent; illustration is geometric systems diagrams blended with organic motifs in brand colors only. No generated image contains baked-in text or logos — the real marks are always placed as assets over imagery.",
            "word_count": 197,
            "path_validated": true,
            "catalog_assets": [
              { "id": "visual-language-board", "path": "./generated/visual-language-board.png" },
              { "id": "hero-01-digital-wilderness", "path": "./generated/hero-01-digital-wilderness.png" },
              { "id": "hero-02-establishing", "path": "./generated/hero-02-establishing.png" },
              { "id": "hero-03-mobile", "path": "./generated/hero-03-mobile.png" },
              { "id": "lifestyle-01-worktable", "path": "./generated/lifestyle-01-worktable.png" },
              { "id": "lifestyle-02-studio", "path": "./generated/lifestyle-02-studio.png" },
              { "id": "product-01-system-artifacts", "path": "./generated/product-01-system-artifacts.png" },
              { "id": "product-02-screen-surface", "path": "./generated/product-02-screen-surface.png" },
              { "id": "illus-01-systems-organism", "path": "./generated/illus-01-systems-organism.png" },
              { "id": "illus-02-delivery-loop", "path": "./generated/illus-02-delivery-loop.png" },
              { "id": "icons-01-sheet", "path": "./generated/icons-01-sheet.png" },
              { "id": "pattern-01-dark", "path": "./generated/pattern-01-dark.png" },
              { "id": "pattern-02-light", "path": "./generated/pattern-02-light.png" },
              { "id": "social-og", "path": "./generated/social-og.png" },
              { "id": "social-x-header", "path": "./generated/social-x-header.png" },
              { "id": "social-ig-story", "path": "./generated/social-ig-story.png" }
            ]
          }
        ]
      },
      "stage2_curate": {
        "description": "Sources selected per target artifact and priority. User-provided assets always included; deterministic logo marks prioritized; generated assets selected by relevance. Source budget is the NotebookLM Standard limit of 50; prose sources count toward the budget, plus the validated image assets attached.",
        "source_budget_total": 50,
        "priority_order": ["user_provided", "brand-identity", "product-strategy", "voice-messaging", "campaign-content", "visual-catalog"],
        "artifacts": [
          {
            "artifact": "mind-map",
            "required_sources": ["brand-identity", "product-strategy"],
            "optional_sources": ["voice-messaging"],
            "prose_sources_selected": ["brand-identity", "product-strategy", "voice-messaging"],
            "assets_selected": [
              { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided", "deterministic": true },
              { "id": "illus-02-delivery-loop", "path": "./generated/illus-02-delivery-loop.png", "origin": "generated", "deterministic": false }
            ],
            "budget_used": 5,
            "budget_total": 10
          },
          {
            "artifact": "brand-slides",
            "required_sources": ["brand-identity", "voice-messaging"],
            "optional_sources": ["visual-catalog"],
            "prose_sources_selected": ["brand-identity", "voice-messaging", "visual-catalog"],
            "assets_selected": [
              { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided", "deterministic": true },
              { "id": "logo-tree-mark", "path": "./assets/thoughtseed-tree-mark-black-3x.png", "origin": "user_provided", "deterministic": true },
              { "id": "hero-01-digital-wilderness", "path": "./generated/hero-01-digital-wilderness.png", "origin": "generated", "deterministic": false },
              { "id": "visual-language-board", "path": "./generated/visual-language-board.png", "origin": "generated", "deterministic": false },
              { "id": "pattern-01-dark", "path": "./generated/pattern-01-dark.png", "origin": "generated", "deterministic": false }
            ],
            "budget_used": 8,
            "budget_total": 15
          },
          {
            "artifact": "brand-report",
            "required_sources": ["brand-identity", "product-strategy", "voice-messaging", "campaign-content", "visual-catalog"],
            "optional_sources": [],
            "prose_sources_selected": ["brand-identity", "product-strategy", "voice-messaging", "campaign-content", "visual-catalog"],
            "assets_selected": [
              { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided", "deterministic": true },
              { "id": "logo-tree-mark", "path": "./assets/thoughtseed-tree-mark-black-3x.png", "origin": "user_provided", "deterministic": true },
              { "id": "logo-reference-01", "path": "./assets/thoughtseed-logo-reference-01.jpg", "origin": "user_provided", "deterministic": true },
              { "id": "logo-reference-02", "path": "./assets/thoughtseed-logo-reference-02.jpg", "origin": "user_provided", "deterministic": true },
              { "id": "hero-01-digital-wilderness", "path": "./generated/hero-01-digital-wilderness.png", "origin": "generated", "deterministic": false },
              { "id": "hero-02-establishing", "path": "./generated/hero-02-establishing.png", "origin": "generated", "deterministic": false },
              { "id": "hero-03-mobile", "path": "./generated/hero-03-mobile.png", "origin": "generated", "deterministic": false },
              { "id": "lifestyle-01-worktable", "path": "./generated/lifestyle-01-worktable.png", "origin": "generated", "deterministic": false },
              { "id": "lifestyle-02-studio", "path": "./generated/lifestyle-02-studio.png", "origin": "generated", "deterministic": false },
              { "id": "product-01-system-artifacts", "path": "./generated/product-01-system-artifacts.png", "origin": "generated", "deterministic": false },
              { "id": "product-02-screen-surface", "path": "./generated/product-02-screen-surface.png", "origin": "generated", "deterministic": false },
              { "id": "illus-01-systems-organism", "path": "./generated/illus-01-systems-organism.png", "origin": "generated", "deterministic": false },
              { "id": "illus-02-delivery-loop", "path": "./generated/illus-02-delivery-loop.png", "origin": "generated", "deterministic": false },
              { "id": "icons-01-sheet", "path": "./generated/icons-01-sheet.png", "origin": "generated", "deterministic": false },
              { "id": "pattern-01-dark", "path": "./generated/pattern-01-dark.png", "origin": "generated", "deterministic": false },
              { "id": "pattern-02-light", "path": "./generated/pattern-02-light.png", "origin": "generated", "deterministic": false },
              { "id": "social-og", "path": "./generated/social-og.png", "origin": "generated", "deterministic": false },
              { "id": "social-x-header", "path": "./generated/social-x-header.png", "origin": "generated", "deterministic": false },
              { "id": "social-ig-story", "path": "./generated/social-ig-story.png", "origin": "generated", "deterministic": false }
            ],
            "budget_used": 24,
            "budget_total": 50
          }
        ]
      },
      "stage3_assemble": {
        "description": "Prose sources combined with validated user and generated assets into source routing. Every asset path checked against the manifest before inclusion; none reference a non-manifest path.",
        "all_paths_validated": true,
        "prose_docs": 5,
        "user_provided_assets": 4,
        "generated_assets": 16,
        "source_routing": {
          "brand-overview-artifacts": {
            "prose_sources": [
              ".brandmint/sources/brand-identity/thoughtseed-brand-identity.md",
              ".brandmint/sources/product-strategy/thoughtseed-product-strategy.md",
              ".brandmint/sources/voice-messaging/thoughtseed-voice-messaging.md"
            ],
            "assets": [
              "./assets/thoughtseed-horizontal-wordmark-3x.png",
              "./assets/thoughtseed-tree-mark-black-3x.png",
              "./generated/hero-01-digital-wilderness.png",
              "./generated/visual-language-board.png",
              "./generated/illus-02-delivery-loop.png"
            ]
          },
          "product-artifacts": {
            "prose_sources": [
              ".brandmint/sources/product-strategy/thoughtseed-product-strategy.md",
              ".brandmint/sources/campaign-content/thoughtseed-campaign-content.md"
            ],
            "assets": [
              "./generated/product-01-system-artifacts.png",
              "./generated/product-02-screen-surface.png",
              "./generated/illus-01-systems-organism.png"
            ]
          },
          "campaign-artifacts": {
            "prose_sources": [
              ".brandmint/sources/campaign-content/thoughtseed-campaign-content.md",
              ".brandmint/sources/voice-messaging/thoughtseed-voice-messaging.md"
            ],
            "assets": [
              "./generated/hero-02-establishing.png",
              "./generated/hero-03-mobile.png",
              "./generated/lifestyle-01-worktable.png",
              "./generated/lifestyle-02-studio.png",
              "./generated/social-og.png",
              "./generated/social-x-header.png",
              "./generated/social-ig-story.png"
            ]
          },
          "visual-artifacts": {
            "prose_sources": [
              ".brandmint/sources/visual-catalog/thoughtseed-visual-catalog.md",
              ".brandmint/sources/brand-identity/thoughtseed-brand-identity.md"
            ],
            "assets": [
              "./assets/thoughtseed-logo-reference-01.jpg",
              "./assets/thoughtseed-logo-reference-02.jpg",
              "./generated/icons-01-sheet.png",
              "./generated/pattern-01-dark.png",
              "./generated/pattern-02-light.png"
            ]
          }
        }
      }
    },
    "notebook": {
      "name": "Thoughtseed — Brand System",
      "planned": true,
      "source_count_planned": 25,
      "note": "Notebook spec: 5 prose category documents plus up to 20 validated image assets. Created on upload; sources are prose, assets are manifest-validated."
    },
    "sources_uploaded": {
      "prose_documents": [
        { "name": "thoughtseed-brand-identity.md", "category": "brand-identity", "source_skills": ["brand-foundation", "color-palette", "typography", "logo-concept"], "word_count": 198, "path_validated": true },
        { "name": "thoughtseed-product-strategy.md", "category": "product-strategy", "source_skills": ["product-positioning", "value-proposition", "buyer-persona", "competitor-analysis"], "word_count": 226, "path_validated": true },
        { "name": "thoughtseed-voice-messaging.md", "category": "voice-messaging", "source_skills": ["voice-and-tone", "messaging-framework", "brand-story"], "word_count": 206, "path_validated": true },
        { "name": "thoughtseed-campaign-content.md", "category": "campaign-content", "source_skills": ["landing-page-copy", "product-description", "ad-creative-copy", "press-release", "launch-email-sequence", "prelaunch-email-sequence", "welcome-email-sequence"], "word_count": 201, "path_validated": true },
        { "name": "thoughtseed-visual-catalog.md", "category": "visual-catalog", "source_skills": ["visual-language", "hero-images", "lifestyle-photography", "product-photography", "brand-illustrations", "icon-system", "pattern-library", "social-media-assets"], "word_count": 197, "path_validated": true }
      ],
      "assets": [
        { "id": "logo-wordmark", "type": "logo", "origin": "user_provided", "deterministic": true, "path_validated": true },
        { "id": "logo-tree-mark", "type": "logo-icon", "origin": "user_provided", "deterministic": true, "path_validated": true },
        { "id": "logo-reference-01", "type": "reference", "origin": "user_provided", "deterministic": true, "path_validated": true },
        { "id": "logo-reference-02", "type": "reference", "origin": "user_provided", "deterministic": true, "path_validated": true },
        { "id": "hero-01-digital-wilderness", "type": "hero", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "hero-02-establishing", "type": "hero", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "hero-03-mobile", "type": "hero", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "lifestyle-01-worktable", "type": "lifestyle", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "lifestyle-02-studio", "type": "lifestyle", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "product-01-system-artifacts", "type": "product", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "product-02-screen-surface", "type": "product", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "illus-01-systems-organism", "type": "illustration", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "illus-02-delivery-loop", "type": "illustration", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "icons-01-sheet", "type": "icons", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "pattern-01-dark", "type": "pattern", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "pattern-02-light", "type": "pattern", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "social-og", "type": "social", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "social-x-header", "type": "social", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "social-ig-story", "type": "social", "origin": "generated", "deterministic": false, "path_validated": true },
        { "id": "visual-language-board", "type": "moodboard", "origin": "generated", "deterministic": false, "path_validated": true }
      ]
    },
    "artifacts_planned": {
      "mind_map": { "planned": true, "path": "deliverables/notebooklm/mind-map.png" },
      "brand_slides": { "planned": true, "path": "deliverables/notebooklm/brand-slides.pdf" },
      "brand_report": { "planned": true, "path": "deliverables/notebooklm/brand-report.pdf" }
    },
    "layer_discipline_check": {
      "avoided_terms_in_prose": 0,
      "krebs_or_consciousness_as_public_claim": false,
      "internal_color_labels_in_prose": false,
      "note": "All five prose sources describe visible effects only; internal color names and backstage methodology are excluded from every source document."
    },
    "validation": {
      "sources_are_prose": true,
      "all_paths_exist": true,
      "all_referenced_assets_in_manifest": true,
      "missing_paths": [],
      "hallucinated_paths": 0
    }
  }
}
```

### pattern-library
```json
{
  "skill": "pattern-library",
  "cluster": "illustration",
  "wave": 5,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "Two seamless, tileable patterns extend the brand as quiet texture rather than focal decoration: a fine geometric systems grid interwoven with organic node-and-branch signal motifs. The dark variant sits on the deep quantum blue-black field in teal and muted gray for behind-content use; the light variant carries the same motif system on warm matte paper in muted teal, slate gray, and soft growth-green. Both are low-contrast and restrained so they read as watermark-scale ground — never large fills of orange or green, never a busy rainbow tile.",
      "model": "gemini-3-pro-image-preview"
    },
    "strategy": {
      "usage_types": [
        { "usage": "Hero / section backgrounds", "pattern_type": "geometric-plus-organic signal grid", "scale": "medium", "density": "low" },
        { "usage": "Section dividers", "pattern_type": "geometric-plus-organic signal grid", "scale": "medium", "density": "medium" },
        { "usage": "Card / document-cover backgrounds", "pattern_type": "geometric-plus-organic signal grid", "scale": "small-medium", "density": "low" },
        { "usage": "Closeout collateral & data-viz grounds", "pattern_type": "geometric-plus-organic signal grid", "scale": "variable", "density": "low" }
      ]
    },
    "color_combinations": [
      { "name": "Signal on dark", "foreground": "#00897B teal + #37474F muted gray", "background": "#0A0E14 / #1A237E deep quantum blue-black", "usage": "Default dark-mode ground behind content" },
      { "name": "Motif on matte light", "foreground": "muted #00897B teal + #37474F slate gray + #B8E986 soft growth-green", "background": "warm matte-paper light", "usage": "Editorial light surfaces, document covers, print" }
    ],
    "assets": [
      {
        "id": "pattern-01-dark",
        "path": "./generated/pattern-01-dark.png",
        "aspect_ratio": "1:1",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "name": "Signal Grid — Dark",
        "type": "geometric",
        "colors": { "foreground": "#00897B teal + #37474F muted gray", "background": "#0A0E14 / #1A237E deep quantum blue-black" },
        "tile_size": "2K seamless tile",
        "tiling_verified": true,
        "description": "Seamless tileable background pattern of fine geometric signal lines interwoven with organic node and branch motifs, in teal and muted gray on a deep quantum blue-black field, subtle and low-contrast for use behind content.",
        "prompt": "A seamless tileable background pattern of fine geometric signal lines interwoven with organic node and branch motifs, in teal and muted gray on a deep quantum blue-black field, subtle and low-contrast for use behind content.",
        "usage": ["dark-section-backgrounds", "hero-grounds", "watermark-texture", "data-viz-ground", "dark-document-covers"]
      },
      {
        "id": "pattern-02-light",
        "path": "./generated/pattern-02-light.png",
        "aspect_ratio": "1:1",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "name": "Signal Grid — Light",
        "type": "geometric",
        "colors": { "foreground": "muted #00897B teal + #37474F slate gray + #B8E986 soft growth-green", "background": "warm matte-paper light" },
        "tile_size": "2K seamless tile",
        "tiling_verified": true,
        "description": "Seamless tileable pattern of the same geometric-plus-organic signal motif system on a warm matte-paper light background, drawn in muted teal, slate gray and soft growth-green line work, restrained and editorial.",
        "prompt": "A seamless tileable pattern of the same geometric-plus-organic signal motif system on a warm matte-paper light background, drawn in muted teal, slate gray and soft growth-green line work, restrained and editorial.",
        "usage": ["light-section-backgrounds", "document-covers", "closeout-collateral", "print", "card-backgrounds"]
      }
    ],
    "textures": [],
    "usage_guidelines": {
      "opacity": "10-20% behind content so the pattern stays quiet texture, not focal.",
      "scale": "Works at 50% and 200% of native tile; keep medium scale for dividers, smaller for cards.",
      "signal_scarcity": "Never large fills of orange or green; signal color stays sparse so it reads as signal.",
      "pairing": "Dark variant on the cool anchor field; light variant on matte paper. Do not mix orange ignition into the pattern itself."
    },
    "quality_gates": {
      "pattern_types_align_with_personality": "Geometric-meets-organic matches the Digital Wilderness duality.",
      "brand_colors_only": true,
      "multiple_scale_options": "50%-200% range documented; dark + light variants.",
      "color_combinations_defined": true,
      "seamlessly_tileable": true,
      "low_contrast_for_background_use": true,
      "no_baked_text_or_logos": true,
      "forbidden_visuals_avoided": true,
      "all_images_generated": true,
      "prompts_documented": true
    },
    "generation_summary": { "total": 2, "generated": 2, "verified_tileable": 2, "model": "gemini-3-pro-image-preview" }
  }
}
```

### prelaunch-email-sequence
```json
{
  "skill": "prelaunch-email-sequence",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "sequence_strategy": {
      "context": "Sent to founders on the list before Thoughtseed Studio opens a new round of build capacity. Builds the case for one coherent studio and primes them to bring a requirement when capacity opens.",
      "goals": [
        "Confirm the signup and set expectations",
        "Name the fragmentation problem and validate it",
        "Reveal the studio approach without overclaiming",
        "Establish credibility with shipped work and the handoff model",
        "Prime founders to bring a requirement the day capacity opens"
      ],
      "timing": "Email 1 immediately after signup; Email 2 day 2; Email 3 day 5; Email 4 day 8; Email 5 the day before capacity opens",
      "total_emails": 5,
      "voice_note": "Calm anticipation, not hype. Short declarative sentences. Evidence next to the claim. No countdown theater, no superlatives, no avoided terms."
    },
    "emails": [
      {
        "number": 1,
        "name": "Welcome + Promise",
        "send_timing": "Immediate",
        "goal": "Confirm signup and set expectations for what is coming",
        "subject_lines": {
          "primary": "You're on the list. Here is what we'll send.",
          "curiosity": "A different way to carry the hard problem",
          "benefit": "One studio, from requirement to handoff",
          "urgency": "Capacity opens soon. First, the context."
        },
        "preview_text": "No noise. A few notes, then the door opens.",
        "hook": "You signed up because the usual way of building is not working.",
        "body": "Thanks for joining the list.\n\nHere is what to expect. Over the next week or so, a few short notes. No noise. Each one makes the case for carrying a complex requirement in one place instead of splitting it across vendors.\n\nThoughtseed is a founder-led systems studio. We turn complex requirements into coherent systems by aligning user behavior, founder operating logic, interface design, and technical delivery. One delivery loop, from requirement to handoff.\n\nWhen we open the next round of build capacity, you will hear it here first. Until then, read on, and start thinking about the requirement you would bring.",
        "cta": {
          "text": "See how the delivery loop works",
          "url_placeholder": "{{delivery_loop_url}}"
        },
        "ps": "P.S. We take a limited number of builds at a time. That is deliberate, and it is why the list matters."
      },
      {
        "number": 2,
        "name": "Problem Agitation",
        "send_timing": "Day 2",
        "goal": "Name and validate the fragmentation problem",
        "subject_lines": {
          "primary": "You did not start the company to translate",
          "curiosity": "The seam where coherence leaks",
          "benefit": "Stop being the integrator between vendors",
          "urgency": "Before capacity opens, name the real problem"
        },
        "preview_text": "Five vendors, no shared model of the problem.",
        "hook": "Strategy goes to one vendor. Design to another. Engineering to a third. Operations to a fourth.",
        "body": "Here is the pattern most founders know too well.\n\nImportant work gets split across strategy, design, engineering, and operations vendors who never share one model of the problem. Each one understands a single slice. You become the integrator, holding the whole thing in your head and re-explaining it at every handoff.\n\nCoherence leaks at every seam. The strategy deck drifts from the shipped product. The engineering ignores how people will actually adopt it. And the system that worked on launch day falls apart at ownership transfer, because the team that now owns it was never handed a way to run it.\n\nIf that sounds familiar, it is not a vendor-management problem you can solve with better project management. It is a structural problem. The work was split when it should have been carried whole.",
        "cta": {
          "text": "Read how we keep it whole",
          "url_placeholder": "{{approach_url}}"
        },
        "ps": "P.S. The next note is about what carrying it whole actually looks like."
      },
      {
        "number": 3,
        "name": "Solution Tease",
        "send_timing": "Day 5",
        "goal": "Reveal the studio approach without a full pitch",
        "subject_lines": {
          "primary": "One team carries the whole requirement",
          "curiosity": "What a single delivery loop changes",
          "benefit": "From requirement to handoff, no vendors in between",
          "urgency": "Capacity is close. Here is the approach."
        },
        "preview_text": "The same people frame it, build it, and hand it back.",
        "hook": "When a problem is too entangled to split, the answer is not a better vendor stack.",
        "body": "Here is how we hold the work in one motion.\n\nThoughtseed keeps requirement, behavior, interface, and engineering in a single delivery loop. The same senior people who frame the requirement design the system, ship it, and prepare the handoff. Nothing gets passed between teams who never shared the problem, because there are no teams in between.\n\nIt runs in three modules under one operating logic. Requirement Architecture frames the problem and the tradeoffs before anything is built. Product & Interface Systems delivers the web, mobile, AI, automation, or connected-product work, with user behavior treated as part of the system. Handoff & Decision Systems ships the documentation, training, and control surfaces that make the work inheritable.\n\nThe result is one coherent system from requirement to handoff. Build the system, not just the story.",
        "cta": {
          "text": "Explore the three modules",
          "url_placeholder": "{{services_url}}"
        },
        "ps": "P.S. There are two ways to engage when capacity opens: a System Sprint, or a full Requirement-to-Handoff Build. More on that soon."
      },
      {
        "number": 4,
        "name": "Credibility",
        "send_timing": "Day 8",
        "goal": "Establish authority with shipped work and the handoff model",
        "subject_lines": {
          "primary": "Evidence sits next to the claim",
          "curiosity": "How to tell premium framing from shallow delivery",
          "benefit": "Shipped systems, real range, real handoff",
          "urgency": "One more note before the door opens"
        },
        "preview_text": "Shipped across AI, IoT, web, mobile, and creative technology.",
        "hook": "Premium language can hide shallow delivery. So here is the evidence.",
        "body": "Before capacity opens, the part that matters: proof.\n\nWe pair atmosphere with evidence. Shipped work across AI, IoT, web, mobile, and creative technology. Live client delivery paired with reusable internal product IP. Service surfaces that already span framing, design, engineering, and handoff. Decision artifacts and handoff documents that prove the loop is real.\n\nThe handoff is the part most studios skip, and the part we treat as the deliverable. A system that works on launch day but breaks at ownership transfer has not been delivered. When we hand back the work, your team inherits documentation written to be read, control surfaces that keep the system legible, and a model of the problem you can carry forward without us.\n\nFounder-led judgment, less lost in translation, and a handoff that holds. That is the whole case.",
        "cta": {
          "text": "See shipped work and handoff artifacts",
          "url_placeholder": "{{proof_url}}"
        },
        "ps": "P.S. Next time you hear from us, capacity will be open."
      },
      {
        "number": 5,
        "name": "Capacity Opens",
        "send_timing": "Day before capacity opens",
        "goal": "Prime founders to bring a requirement when the round opens",
        "subject_lines": {
          "primary": "Tomorrow: bring the requirement",
          "curiosity": "The door opens in the morning",
          "benefit": "A spot to carry your hard problem whole",
          "urgency": "Limited builds. The list goes first."
        },
        "preview_text": "We take a limited number of builds at a time.",
        "hook": "Tomorrow, the next round of build capacity opens, and the list goes first.",
        "body": "This is the note you have been waiting for.\n\nTomorrow we open the next round of build capacity at Thoughtseed Studio. We take a limited number of builds at a time, on purpose. Fewer engagements, deeper integration, a real handoff at the end. Because the list went deep on the why, you go first.\n\nWhen the door opens, here is how it works:\n\n- Start with a System Sprint, a short framing or prototype cycle that clarifies the requirement and de-risks the next build decision.\n- Or scope a Requirement-to-Handoff Build, full delivery from framing through implementation and ownership transfer.\n\nEither way, you talk to the operators doing the work, and the requirement you bring stays whole the entire way.\n\nHave the requirement ready. The messy version is fine. Bring it tomorrow.",
        "cta": {
          "text": "Bring the requirement.",
          "url_placeholder": "{{start_url}}"
        },
        "ps": "P.S. If the problem is too entangled to split across vendors, it is exactly the kind we are built to carry."
      }
    ]
  }
}
```

### press-release
```json
{
  "skill": "press-release",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "release_type": "FOR IMMEDIATE RELEASE",
    "headline": "Thoughtseed Launches Thoughtseed Studio, Carrying Complex Requirements From Framing to Handoff in One Delivery Loop",
    "subheadline": "The founder-led systems studio takes work that founders usually split across strategy, design, engineering, and operations vendors and carries it whole, across AI, IoT, web, mobile, and creative technology.",
    "dateline": {
      "city": "[CITY]",
      "date": "June 8, 2026"
    },
    "lead_paragraph": "Thoughtseed, a founder-led systems studio founded in 2020, today opened Thoughtseed Studio, an engagement model that carries a complex requirement from framing through implementation to a handoff the client can run. The studio is built for founders and technical leaders who would otherwise split important work across strategy, design, engineering, and operations vendors who never share one model of the problem. Thoughtseed keeps requirement, user behavior, interface design, and engineering delivery in a single loop, and treats ownership transfer as a first-class output.",
    "body_paragraphs": [
      {
        "topic": "The problem",
        "content": "Important work commonly gets divided among separate strategy, design, engineering, and operations vendors. Each understands a single slice, and the founder becomes the full-time translator between them. Coherence breaks before the work ships, and ownership breaks after it, because the system that launched cleanly cannot be run by the team that now owns it. Thoughtseed Studio is built to remove that fragmentation."
      },
      {
        "topic": "How the studio works",
        "content": "Thoughtseed Studio runs as one delivery loop carried by the same senior operators from start to finish. The work is organized into three modules under one operating logic. Requirement Architecture settles problem framing, operating constraints, and decision logic before implementation. Product and Interface Systems delivers web, mobile, AI, automation, and connected-product execution, with user behavior treated as part of the system rather than a layer added later. Handoff and Decision Systems ships the documentation, training, control surfaces, and operational artifacts that make the delivered work inheritable."
      },
      {
        "topic": "Who it is for",
        "content": "The studio is designed for founders, CTOs, innovation leads, and product strategists running lean senior teams who need one partner that understands the requirement, the user, and the operating reality together. Engagements take one of two forms: a System Sprint, a short framing or prototype cycle that clarifies the requirement and de-risks the next build decision, or a Requirement-to-Handoff Build, scoped delivery from framing through implementation and ownership transfer. Thoughtseed takes a limited number of builds at a time and is not structured as an always-on retainer."
      },
      {
        "topic": "Differentiation",
        "content": "Where large consultancies offer process and procurement comfort, premium design agencies offer interface polish, and AI integration firms offer current tooling, Thoughtseed pairs founder-led judgment with build reality across all of these surfaces. The same people who frame a requirement design and ship the system, which reduces translation loss and keeps decisions documented as artifacts the client can trace. Handoff is part of the system, not post-project administration."
      },
      {
        "topic": "Availability",
        "content": "Thoughtseed Studio is open now and accepting requirements for the current build round. Engagements are scoped per project rather than priced as a subscription. Founders can begin by bringing a requirement, including early or unresolved ones, for framing. More information is available at [WEBSITE URL]."
      }
    ],
    "quotes": [
      {
        "speaker": "[FOUNDER NAME]",
        "title": "Founder, Thoughtseed",
        "quote": "Founders keep getting handed five vendors and a translation job. We built Thoughtseed Studio so one team can carry the whole requirement, from framing to a system the client can actually run. We study the requirement, build the system, and hand it back. The handoff is not the afterthought. It is the point."
      },
      {
        "speaker": "[FOUNDER NAME OR SECOND PRINCIPAL]",
        "title": "[TITLE], Thoughtseed",
        "quote": "A system that works on launch day but breaks at ownership transfer has not been delivered. We treat user behavior as part of the system and ship the documentation, training, and control surfaces with the build, so the work is legible and the client can run it without us."
      }
    ],
    "product_details": {
      "availability": "Open now, accepting requirements for the current build round; limited number of builds taken at a time",
      "pricing": "Scoped per engagement (System Sprint or Requirement-to-Handoff Build); not a subscription or retainer",
      "launch_date": "June 8, 2026",
      "where_to_buy": "Bring a requirement at [WEBSITE URL]"
    },
    "boilerplate": "About Thoughtseed. Thoughtseed is a founder-led systems studio that turns complex requirements into coherent technology systems. Founded in 2020, it aligns user behavior, founder operating logic, interface design, engineering delivery, and structured handoff inside one delivery loop, carrying work from requirement to handoff instead of splitting it across disconnected vendors. Thoughtseed ships across AI, automation, web, mobile, IoT, and creative technology, and treats ownership transfer as a first-class deliverable so clients can run, extend, and inherit the systems it builds. Learn more at [WEBSITE URL].",
    "media_contact": {
      "name": "[CONTACT NAME]",
      "title": "[CONTACT TITLE]",
      "email": "[CONTACT EMAIL]",
      "phone": "[CONTACT PHONE]"
    },
    "full_release": "FOR IMMEDIATE RELEASE\n\nThoughtseed Launches Thoughtseed Studio, Carrying Complex Requirements From Framing to Handoff in One Delivery Loop\n\nThe founder-led systems studio takes work that founders usually split across strategy, design, engineering, and operations vendors and carries it whole, across AI, IoT, web, mobile, and creative technology.\n\n[CITY] — June 8, 2026 — Thoughtseed, a founder-led systems studio founded in 2020, today opened Thoughtseed Studio, an engagement model that carries a complex requirement from framing through implementation to a handoff the client can run. The studio is built for founders and technical leaders who would otherwise split important work across strategy, design, engineering, and operations vendors who never share one model of the problem. Thoughtseed keeps requirement, user behavior, interface design, and engineering delivery in a single loop, and treats ownership transfer as a first-class output.\n\nImportant work commonly gets divided among separate strategy, design, engineering, and operations vendors. Each understands a single slice, and the founder becomes the full-time translator between them. Coherence breaks before the work ships, and ownership breaks after it, because the system that launched cleanly cannot be run by the team that now owns it. Thoughtseed Studio is built to remove that fragmentation.\n\nThoughtseed Studio runs as one delivery loop carried by the same senior operators from start to finish. The work is organized into three modules under one operating logic. Requirement Architecture settles problem framing, operating constraints, and decision logic before implementation. Product and Interface Systems delivers web, mobile, AI, automation, and connected-product execution, with user behavior treated as part of the system rather than a layer added later. Handoff and Decision Systems ships the documentation, training, control surfaces, and operational artifacts that make the delivered work inheritable.\n\nThe studio is designed for founders, CTOs, innovation leads, and product strategists running lean senior teams who need one partner that understands the requirement, the user, and the operating reality together. Engagements take one of two forms: a System Sprint, a short framing or prototype cycle that clarifies the requirement and de-risks the next build decision, or a Requirement-to-Handoff Build, scoped delivery from framing through implementation and ownership transfer. Thoughtseed takes a limited number of builds at a time and is not structured as an always-on retainer.\n\n\"Founders keep getting handed five vendors and a translation job,\" said [FOUNDER NAME], Founder of Thoughtseed. \"We built Thoughtseed Studio so one team can carry the whole requirement, from framing to a system the client can actually run. We study the requirement, build the system, and hand it back. The handoff is not the afterthought. It is the point.\"\n\nWhere large consultancies offer process and procurement comfort, premium design agencies offer interface polish, and AI integration firms offer current tooling, Thoughtseed pairs founder-led judgment with build reality across all of these surfaces. The same people who frame a requirement design and ship the system, which reduces translation loss and keeps decisions documented as artifacts the client can trace. Handoff is part of the system, not post-project administration.\n\n\"A system that works on launch day but breaks at ownership transfer has not been delivered,\" said [FOUNDER NAME OR SECOND PRINCIPAL], [TITLE] at Thoughtseed. \"We treat user behavior as part of the system and ship the documentation, training, and control surfaces with the build, so the work is legible and the client can run it without us.\"\n\nThoughtseed Studio is open now and accepting requirements for the current build round. Engagements are scoped per project rather than priced as a subscription. Founders can begin by bringing a requirement, including early or unresolved ones, for framing. More information is available at [WEBSITE URL].\n\nAbout Thoughtseed\n\nThoughtseed is a founder-led systems studio that turns complex requirements into coherent technology systems. Founded in 2020, it aligns user behavior, founder operating logic, interface design, engineering delivery, and structured handoff inside one delivery loop, carrying work from requirement to handoff instead of splitting it across disconnected vendors. Thoughtseed ships across AI, automation, web, mobile, IoT, and creative technology, and treats ownership transfer as a first-class deliverable so clients can run, extend, and inherit the systems it builds. Learn more at [WEBSITE URL].\n\nMedia Contact\n[CONTACT NAME]\n[CONTACT TITLE], Thoughtseed\n[CONTACT EMAIL]\n[CONTACT PHONE]\n\n###"
  }
}
```

### product-description
```json
{
  "skill": "product-description",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "core_info": {
      "product_name": "Thoughtseed Studio",
      "category": "Founder-led systems studio",
      "price": "Scoped per engagement (System Sprint or Requirement-to-Handoff Build)",
      "key_specs": [
        "Scope: requirement to handoff, one delivery loop",
        "Range: web, mobile, AI, automation, connected products",
        "Team: senior, cross-disciplinary, founder-led",
        "Engagement models: System Sprint; Requirement-to-Handoff Build",
        "Output: a running system plus the artifacts to own it"
      ]
    },
    "benefits_hierarchy": {
      "primary": "One coherent system from requirement to handoff, carried by one team instead of split across disconnected vendors.",
      "secondary": [
        "Less translation loss: senior operators do the work directly, so coherence holds from framing to the running product.",
        "Adoption built in: user behavior is treated as part of the system, not a layer added after the build.",
        "Real ownership: documentation, training, and control surfaces ship with the build, so you can run it without us."
      ],
      "features": [
        "Requirement Architecture: problem framing, psychology mapping, operating constraints, and decision logic before implementation",
        "Product & Interface Systems: web, mobile, AI, automation, and connected-product execution",
        "Handoff & Decision Systems: documentation, training, control surfaces, and operational artifacts"
      ]
    },
    "descriptions": {
      "micro": {
        "word_count": 22,
        "copy": "Thoughtseed Studio is a founder-led systems studio that turns complex requirements into coherent systems you can run. From requirement to handoff."
      },
      "short": {
        "word_count": 64,
        "copy": "Thoughtseed Studio is a founder-led systems studio. We turn complex requirements into coherent systems by aligning user behavior, founder operating logic, interface design, and technical delivery. One team carries framing, build, and handoff in a single delivery loop, so coherence holds from the first decision to the running product. You inherit a system you can run, extend, and own. Bring the requirement."
      },
      "medium": {
        "word_count": 132,
        "copy": "Important work gets split across strategy, design, engineering, and operations vendors who do not share one model of the problem. Coherence breaks before launch, and ownership breaks after it. Thoughtseed Studio holds the whole problem in one delivery loop. We study the requirement, the people who will use the system, and the way you want to run it. Then we design the interface, build the engineering, and hand it back. User behavior is treated as part of the system. Documentation, training, and control surfaces ship with the build. The result is one coherent system from requirement to handoff, carried by senior operators with less translation loss, and a handoff you can actually run. Fewer projects, deeper integration, real ownership. Bring the requirement."
      },
      "full": {
        "word_count": 268,
        "copy": "When a problem is too entangled to split, splitting it makes things worse. You hire a strategy vendor, a design agency, an engineering shop, and someone for handoff, and you become the full-time translator between five teams who never shared one model of the problem. Coherence leaks at every seam. The system works on launch day and falls apart at ownership transfer.\n\nThoughtseed Studio is built for exactly this. It is a founder-led systems studio that carries one requirement all the way to a system you can own. We hold framing, user behavior, product design, engineering delivery, and handoff inside a single loop, with the same senior people from start to finish.\n\nIt works in three modules under one operating logic. Requirement Architecture settles problem framing, psychology mapping, operating constraints, and decision logic before anything is built. Product & Interface Systems delivers web, mobile, AI, automation, and connected-product execution, with user behavior treated as part of the system rather than a layer added later. Handoff & Decision Systems ships the documentation, training, control surfaces, and operational artifacts that make the work inheritable.\n\nYou can start small with a System Sprint, a short cycle that clarifies the requirement and de-risks the next build decision, or scope a Requirement-to-Handoff Build for full delivery through ownership transfer. Either way, you talk to the operators doing the work.\n\nWhat you get is one coherent system from requirement to handoff: technically serious, grounded in adoption, and legible enough to run without us. Fewer projects, deeper integration, and a handoff that holds. Build the system, not just the story. Bring the requirement."
      },
      "extended": {
        "word_count": 438,
        "copy": "Thoughtseed Studio is the founder-led systems studio for problems that cannot be split across disconnected vendors.\n\nThe core problem is fragmentation. Important work gets passed between strategy, design, engineering, and operations vendors who do not share one model of the problem. Each one understands a single slice. The founder becomes the integrator, holding the whole thing in their head and re-explaining it at every handoff. Coherence breaks before the work ships. Ownership breaks after it, because the system that launched cleanly cannot be run by the people who now own it.\n\nThoughtseed Studio is the alternative. One team carries the requirement from framing to a running system, in a single delivery loop, with senior judgment at every stage. We study the requirement, the people who will use the system, and the way you want to operate it. Then we design, build, and hand it back in a form you can run.\n\nThe work is organized into three modules under one operating logic.\n\nRequirement Architecture comes first: problem framing, psychology mapping, operating constraints, and decision logic, settled before implementation. You see the real problem and the real decision pressure before a single screen or model is built.\n\nProduct & Interface Systems is the build: web, mobile, AI, automation, and connected-product execution. User behavior is treated as part of the system, so adoption logic and build reality stay aligned instead of drifting apart between specialists. What we framed is what we ship.\n\nHandoff & Decision Systems closes the loop: documentation, training, control surfaces, and operational artifacts delivered with the build. Handoff is a first-class output, not post-project admin. The system does not fall apart at ownership transfer.\n\nThere are two ways to engage. A System Sprint is a short, high-leverage framing or prototype cycle that clarifies the requirement and de-risks the next build decision. A Requirement-to-Handoff Build is scoped delivery from framing through implementation and ownership transfer. We take fewer engagements and go deeper. This is not an always-on retainer.\n\nThe evidence sits close to the claim: shipped work across AI, IoT, web, mobile, and creative technology, live client delivery paired with reusable internal product IP, and handoff documents that prove the loop is real.\n\nWhat you get is one coherent system from requirement to handoff. Technically serious. Grounded in how people actually adopt and trust software. Legible enough to run, extend, and inherit without us. Ownership over dependency.\n\nBuild the system, not just the story. Bring the requirement."
      }
    },
    "feature_benefit_map": [
      {
        "feature": "Requirement Architecture",
        "benefit": "You see the real problem and the real tradeoffs before anything is built",
        "copy_snippet": "We frame the requirement and surface constraints first, so you decide with the real picture in front of you."
      },
      {
        "feature": "Product & Interface Systems",
        "benefit": "The system gets adopted because behavior was designed in, not bolted on",
        "copy_snippet": "We treat user behavior as part of the system, so what ships is built to be used, not just launched."
      },
      {
        "feature": "Handoff & Decision Systems",
        "benefit": "You can run, extend, and own the system after delivery",
        "copy_snippet": "Documentation, training, and control surfaces ship with the build, so the work is yours to run."
      },
      {
        "feature": "One delivery loop, one senior team",
        "benefit": "Coherence holds from framing to the running product",
        "copy_snippet": "The same operators frame, design, build, and hand back, so nothing gets lost between vendors."
      },
      {
        "feature": "System Sprint engagement model",
        "benefit": "You de-risk the hard decision before committing to a full build",
        "copy_snippet": "Start with a short framing cycle that clarifies the requirement and de-risks what comes next."
      }
    ],
    "bullet_points": [
      "Founder-led systems studio: senior operators carry the work directly, with less translation loss.",
      "One delivery loop from requirement to handoff, instead of five disconnected vendors.",
      "Requirement Architecture frames the problem and the tradeoffs before anything is built.",
      "Product & Interface Systems ships web, mobile, AI, automation, and connected products.",
      "User behavior is treated as part of the system, so the work gets adopted.",
      "Handoff ships with documentation, training, and control surfaces you can run.",
      "Two ways to engage: System Sprint, or full Requirement-to-Handoff Build."
    ],
    "seo_keywords": [
      "founder-led systems studio",
      "requirement to handoff",
      "product and engineering studio",
      "AI and automation delivery",
      "systems design studio",
      "product handoff and ownership transfer",
      "cross-disciplinary product studio"
    ]
  }
}
```

### product-photography
```json
{
  "skill": "product-photography",
  "cluster": "photography",
  "wave": 4,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "Thoughtseed's 'product' is a delivered system, so product photography treats the system as a physical and on-screen artifact rather than a retail object on white. One frame is a premium flat-lay of documentation and control-surface sheets — the inheritable handoff — bound and arranged on weathered stone with a connecting teal signal line. The other is a close on-device shot of an abstract systems interface. Both use brushed metal, architectural shadow, shallow depth of field, and a single orange status accent. No pure-white e-commerce backgrounds; depth comes from material and contrast, not gloss.",
      "model": "gemini-3-pro-image-preview",
      "lighting": "Studio-controlled directional light with architectural shadow; shallow depth of field; clean contrast, no flat even fill, no glossy hotspots.",
      "color_treatment": "Deep blue-black and cool gray base; teal (#00897B) signal lines connecting elements; a single Energetic Orange (#F57C00) status point.",
      "composition": "Premium flat-lay (4:5) and close product crop (4:3); architectural shadow; intentional negative space; one signal moment per frame."
    },
    "product_description": "The Thoughtseed delivered system rendered as an artifact: handoff documentation and control surfaces as physical sheets, and the working systems interface on a device screen. This represents the brand promise — one coherent system from requirement to handoff — made tangible, not a conventional retail product.",
    "key_features_to_highlight": [
      "Handoff as a first-class, physical, inheritable artifact (documentation + control surfaces)",
      "Systems thinking made visible (geometric diagrams, node maps printed as abstract marks)",
      "On-screen systems interface: teal signal lines, node graph, single orange status point",
      "Material truth — brushed metal, weathered stone, architectural shadow over gloss"
    ],
    "shot_types": [
      { "type": "Flat-lay / artifact", "purpose": "Show the delivered system as a physical, inheritable handoff", "background": "weathered stone", "lighting": "directional studio light, architectural shadow" },
      { "type": "Close product / screen", "purpose": "Show the working systems interface as the on-screen product surface", "background": "brushed-metal stand, dark field", "lighting": "controlled, shallow depth of field" }
    ],
    "assets": [
      {
        "id": "product-01-system-artifacts",
        "path": "./generated/product-01-system-artifacts.png",
        "aspect_ratio": "4:5",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "type": "flat-lay / artifact",
        "angle": "top-down flat-lay",
        "background": "weathered stone",
        "feature_focus": "Handoff documentation and control-surface sheets as a delivered physical system",
        "description": "Premium flat-lay of a delivered system as a physical artifact: a stack of matte-paper documentation and control-surface sheets bound with a brushed-metal clip, faint geometric diagrams and node maps printed as abstract marks, arranged on weathered stone with a thin teal signal line connecting the pieces.",
        "prompt": "A premium flat-lay of a delivered system as a physical artifact: a stack of matte-paper documentation and control-surface sheets bound with a brushed-metal clip, faint geometric diagrams and node maps printed as abstract marks, arranged on weathered stone with a thin teal signal line connecting the pieces.",
        "priority": "high",
        "usage": ["work-section", "handoff-section", "proof", "social", "deck"]
      },
      {
        "id": "product-02-screen-surface",
        "path": "./generated/product-02-screen-surface.png",
        "aspect_ratio": "4:3",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "type": "close product / screen",
        "angle": "close three-quarter",
        "background": "brushed-metal stand on a dark field",
        "feature_focus": "Working systems interface — teal signal lines, node graph, one orange status point",
        "description": "Close premium product shot of a single dark device screen on a brushed-metal stand, displaying an abstract systems interface of teal signal lines, a node graph and one orange status point on a deep blue-black UI, with architectural shadow and shallow depth of field.",
        "prompt": "A close premium product shot of a single dark device screen on a brushed-metal stand, displaying an abstract systems interface of teal signal lines, a node graph and one orange status point on a deep blue-black UI, with architectural shadow and shallow depth of field.",
        "priority": "high",
        "usage": ["product-section", "interface-systems-module", "proof", "deck"]
      }
    ],
    "quality_gates": {
      "hero_shot_defined": "product-01-system-artifacts is the primary artifact frame.",
      "angles_covered": "Top-down flat-lay and close three-quarter screen crop.",
      "feature_detail_shots": "Screen surface shot serves as the interface detail.",
      "background_treatment": "Material-truth backgrounds (weathered stone, brushed metal, dark field) instead of pure-white e-commerce — intentional per Digital Wilderness direction.",
      "lighting_direction_included": true,
      "no_glossy_plastic": true,
      "no_baked_text_or_logos": true,
      "forbidden_visuals_avoided": true,
      "all_images_generated": true,
      "prompts_documented": true
    },
    "generation_summary": { "total_shots": 2, "generated": 2, "pending": 0, "model": "gemini-3-pro-image-preview" }
  }
}
```

### product-positioning
```json
{
  "skill": "product-positioning",
  "cluster": "strategy",
  "wave": 2,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "cbbe": {
      "salience": {
        "product_category": "Founder-led systems studio for requirement-to-handoff delivery",
        "problem_solved": "Important work gets split across strategy, design, engineering, and operations vendors who do not share one model of the problem. Coherence breaks before launch, and ownership breaks after it.",
        "one_sentence": "Thoughtseed is the founder-led systems studio that studies the requirement, builds the system, and hands it back in a form the client can run."
      },
      "performance": {
        "points_of_difference": [
          "One integrated studio logic: requirement, user behavior, interface, and engineering stay in one delivery loop instead of being passed between vendors.",
          "Founder-led judgment: senior operators do the work directly, so less is lost in account-management translation.",
          "Handoff is part of the system: documentation, training, and control surfaces ship with the build so the client can run it without us."
        ],
        "points_of_parity": [
          "Senior product design and interface craft",
          "Modern engineering across web, mobile, AI, automation, and connected products",
          "Project framing, discovery, and scoping",
          "Professional delivery artifacts and structured decks"
        ],
        "core_features": [
          { "feature": "Requirement Architecture: problem framing, psychology mapping, operating constraints, and decision logic before implementation", "value_level": "high" },
          { "feature": "Product & Interface Systems: web, mobile, AI, automation, and connected-product execution with user behavior treated as part of the system", "value_level": "high" },
          { "feature": "Handoff & Decision Systems: documentation, training, control surfaces, and operational artifacts that make delivered work inheritable", "value_level": "high" },
          { "feature": "System Sprint: short framing or prototype cycle that clarifies the requirement and de-risks the next build decision", "value_level": "medium" },
          { "feature": "Requirement-to-Handoff Build: scoped delivery from framing through implementation and ownership transfer", "value_level": "high" },
          { "feature": "Cross-disciplinary team under one operating logic", "value_level": "high" },
          { "feature": "Reusable product IP alongside client services", "value_level": "medium" }
        ]
      },
      "imagery": {
        "brand_associations": [
          "A serious architecture practice that also engineers the building, not just the renders",
          "An editorial studio with the rigor of an engineering firm",
          "A founder-side operator who has shipped real systems and lived with the ambiguity"
        ],
        "usage_locations": [
          "Inside lean senior teams at funded startups through scaleups",
          "Innovation units that need one coherent partner, not a vendor stack",
          "Founder and CTO desks where the requirement is too entangled to split"
        ],
        "usage_methods": [
          "Engaged for a System Sprint to frame and de-risk a hard requirement",
          "Engaged for a Requirement-to-Handoff Build to design, build, and transfer ownership of a system",
          "Brought in when a problem crosses product, interface, AI, and operating reality at once"
        ]
      },
      "judgments": {
        "positive_judgments": [
          "Technically serious; the work ships and runs",
          "Coherent; one model of the problem carries from framing to handoff",
          "Honest and specific; claims sit close to evidence",
          "Restrained; taste without theater"
        ],
        "concerns_doubts": [
          "The studio's range can read as broad or unfocused",
          "It can sound like a full-service agency",
          "Psychology language can feel fuzzy or soft",
          "Premium framing can hide shallow delivery"
        ],
        "credibility": "Shipped work across AI, IoT, web, mobile, and creative technology; live client delivery paired with reusable internal IP; service surfaces that already span framing, design, engineering, and handoff; decision artifacts and handoff documents that prove the loop is real.",
        "concern_responses": [
          { "concern": "This sounds broad.", "response": "The breadth is a deliberate studio shape for problems that cross product, interface, and technical delivery. We take fewer engagements and go deeper, rather than staffing every slice." },
          { "concern": "This sounds like an agency.", "response": "The difference is the delivery loop. Fewer projects, deeper integration, and a real handoff instead of open-ended account farming. We are not an always-on retainer." },
          { "concern": "Psychology language can feel fuzzy.", "response": "Here it means trust, adoption, founder workflow, and user behavior grounded in engineering reality. We treat behavior as part of the system, then test it against what ships." },
          { "concern": "Premium language can hide shallow delivery.", "response": "We pair atmosphere with evidence: shipped systems, technical range, concrete project surfaces, and the handoff artifacts a client can actually run." }
        ]
      },
      "feelings": {
        "desired_feelings": [
          "Relief that one partner finally holds the whole problem",
          "Trust earned through specificity and shipped evidence",
          "Calm confidence that execution will stay coherent",
          "Ownership: the sense that the delivered system is theirs to run"
        ],
        "voice": "The founder-side systems translator. An operator who has built systems and lived with ambiguity, speaking peer to peer with the founder.",
        "tone": "Clear, calm, technically precise, human, founder-led, editorially restrained."
      },
      "resonance": {
        "why_missed": "Without Thoughtseed, the founder goes back to being the full-time translator between five specialists, watching coherence leak at every handoff and ownership break after launch.",
        "mission_alignment": "The founder wants to solve an important problem and own the result, not manage vendors. Thoughtseed exists to carry the requirement and hand back a system they can run, extend, and inherit.",
        "core_values": [
          "Cross-disciplinary rigor",
          "Coherence from requirement to handoff",
          "Founder-led accountability",
          "Ownership over dependency",
          "Evidence kept close to the claim"
        ],
        "why_choose_us": "One studio carries framing, behavior, product, execution, and handoff inside a single loop with senior judgment, so the founder gets a coherent system they can own instead of a stack of disconnected deliverables."
      }
    },
    "positioning_statement": "For the system-carrying founder who needs to solve a problem too entangled to split across vendors, Thoughtseed is the founder-led systems studio that aligns user psychology, founder operating logic, interface design, engineering delivery, and structured handoff into one coherent system from requirement to handoff. Unlike single-slice agencies and consultancies, Thoughtseed carries the whole loop with senior judgment and hands back a system the client can actually run.",
    "frame_of_reference": "Not a single-slice design agency, not an enterprise consultancy that packages process, and not an AI integrator chasing tooling. A founder-led systems studio that holds requirement, behavior, product, engineering, and handoff in one delivery loop.",
    "competitive_frame": "niche-specialist",
    "points_of_parity": [
      "Senior product design and interface craft",
      "Modern engineering across web, mobile, AI, automation, and connected products",
      "Professional discovery, scoping, and delivery artifacts"
    ],
    "points_of_difference": [
      "One coherent delivery loop: requirement, behavior, interface, and engineering never get handed between disconnected vendors.",
      "Founder-led judgment with less translation loss than layered account management.",
      "Handoff treated as part of the system, so the client can run and inherit the work after delivery."
    ],
    "category_design": "Defines the founder-led systems studio: the studio that carries a complex requirement all the way to a system the client can own, instead of selling a single slice of strategy, design, or engineering."
  }
}
```

### social-media-assets
```json
{
  "skill": "social-media-assets",
  "cluster": "photography",
  "wave": 4,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "art_direction": {
      "theme": "Digital Wilderness",
      "summary": "Social assets carry the Digital Wilderness atmosphere into platform formats while leaving deliberate dark negative space for overlay applied in the layout layer. Each format places a tactile material vignette (matte paper, brushed metal, weathered stone, moss) and a teal signal network against a deep blue-black field, with a single orange ignition accent. The OG and X header bias content to one side / one sweep so headline copy, the canonical wordmark, or profile elements can be composited over clean space — never baked in. Restraint keeps the brand reading as founder-led and editorial across the feed.",
      "model": "gemini-3-pro-image-preview",
      "lighting": "Cool screen-glow shaft and controlled architectural shadow; clean contrast.",
      "color_treatment": "Deep Quantum Blue / near-black field, teal (#00897B) signal nodes, single Energetic Orange (#F57C00) accent; desaturated.",
      "composition": "Format-specific: right-two-thirds vignette with empty left (OG), left-to-right material sweep (X header), low vignette with calm top/bottom (IG story)."
    },
    "platforms": ["linkedin", "x", "instagram", "facebook", "youtube"],
    "profile_strategy": {
      "approach": "Use the existing canonical Thoughtseed marks as the profile image — the black tree mark on light, or the white/reversed tree mark on the dark anchor field. No new profile mark is generated; the logo-concept spoke governs usage. Generated imagery is never used as the avatar mark.",
      "background": "Deep Quantum Blue (#1A237E) or dark canvas (#0A0E14) for reversed mark; Neutral 50 (#F8F9F9) for black mark.",
      "note": "Per logo-concept: switch to the tree mark in square/compact contexts; keep it monochrome and give full clear space.",
      "prompt": "N/A — profile mark uses canonical asset files (assets/thoughtseed-tree-mark-black-3x.png), not generated imagery."
    },
    "cover_strategy": {
      "approach": "Atmospheric Digital Wilderness vignettes with composed empty space for text/profile/wordmark overlay added in layout.",
      "safe_zones": "OG keeps the left third empty; X header keeps the left clear and accounts for the centered profile-photo crop; IG story keeps top and bottom calm. Account for platform UI cropping on each.",
      "seasonal_updates": false
    },
    "assets": [
      {
        "id": "social-og",
        "path": "./generated/social-og.png",
        "aspect_ratio": "16:9",
        "platform": "open-graph / linkedin / facebook / x-post",
        "type": "share / OG card",
        "dimensions": "1200x675 (16:9)",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "description": "Balanced social share image: an atmospheric Digital Wilderness material vignette occupying the right two-thirds with teal signal nodes and one orange accent, and deliberate empty dark negative space on the left for later overlay (headline + wordmark).",
        "prompt": "A balanced social share image: an atmospheric Digital Wilderness material vignette occupying the right two-thirds with teal signal nodes and one orange accent, and deliberate empty dark negative space on the left for later overlay.",
        "text_safe_zone": "left third",
        "priority": "high",
        "usage": ["open-graph-card", "linkedin-post", "facebook-post", "x-post-image", "link-preview"]
      },
      {
        "id": "social-x-header",
        "path": "./generated/social-x-header.png",
        "aspect_ratio": "21:9",
        "platform": "x / twitter",
        "type": "profile header / banner",
        "dimensions": "1500x500 (~21:9 ultra-wide)",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "description": "Ultra-wide banner: a horizontal sweep from architectural shadow on the left into a tactile material study on the right of matte paper, brushed metal, stone and moss, connected by a single long faint teal signal line across deep blue-black with generous negative space for the profile-photo crop and overlay.",
        "prompt": "An ultra-wide banner: a horizontal sweep from architectural shadow on the left into a tactile material study on the right of matte paper, brushed metal, stone and moss, connected by a single long faint teal signal line across deep blue-black with generous negative space.",
        "text_safe_zone": "left and lower-center (profile-photo crop zone)",
        "priority": "high",
        "usage": ["x-profile-header", "linkedin-cover", "wide-banner"]
      },
      {
        "id": "social-ig-story",
        "path": "./generated/social-ig-story.png",
        "aspect_ratio": "9:16",
        "platform": "instagram / stories / reels",
        "type": "story / vertical",
        "dimensions": "1080x1920 (9:16)",
        "model": "gemini-3-pro-image-preview",
        "source": "generated",
        "user_provided": false,
        "description": "Vertical story-format brand stage: a tall dark composition with a shaft of cool light, a single material vignette of brushed metal meeting moss and stone low in the frame, teal nodes rising through empty space and one small orange ignition accent, with calm empty space at top and bottom for sticker/headline overlay.",
        "prompt": "A vertical story-format brand stage: a tall dark composition with a shaft of cool light, a single material vignette of brushed metal meeting moss and stone low in the frame, teal nodes rising through empty space and one small orange ignition accent, with calm empty space at top and bottom.",
        "text_safe_zone": "top and bottom",
        "priority": "high",
        "usage": ["instagram-story", "reel-cover", "vertical-ad", "story-ad"]
      }
    ],
    "post_templates": [
      { "name": "Quote / phrase card", "purpose": "Engagement", "elements": ["approved brand phrase as overlay text", "social-og vignette ground", "wordmark"], "prompt": "Overlay an approved brand phrase (e.g. 'Build the system, not just the story.' or 'From requirement to handoff.') in the left safe zone of social-og.png; apply text in layout, never bake into the generated image." },
      { "name": "Announcement", "purpose": "News / launch", "elements": ["bold headline overlay", "single orange ignition accent visible", "wordmark"], "prompt": "Use social-og.png or social-ig-story.png with headline overlaid in the safe zone; reserve the orange accent moment for launch energy." },
      { "name": "Work / proof", "purpose": "Credibility", "elements": ["product-photography artifact frame", "short caption overlay"], "prompt": "Pair product-01-system-artifacts.png with a restrained caption in layout to show shipped, inheritable work." }
    ],
    "quality_gates": {
      "profile_images_defined": "Profile marks use canonical logo assets (not generated) per logo-concept.",
      "cover_safe_zones_specified": true,
      "dimensions_match_platforms": true,
      "post_templates_cover_key_types": true,
      "brand_consistency": "All assets hold the Digital Wilderness dark-first field with single teal/orange signal.",
      "small_size_legibility": "Profile legibility handled by the canonical tree mark per logo-concept minimum sizes.",
      "no_baked_text_or_logos": true,
      "forbidden_visuals_avoided": true,
      "all_images_generated": true,
      "prompts_documented": true
    },
    "generation_summary": { "total_assets": 3, "generated": 3, "pending": 0, "model": "gemini-3-pro-image-preview" }
  }
}
```

### typography
```json
{
  "skill": "typography",
  "cluster": "identity",
  "wave": 3,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "rationale": {
      "brand_personality": "Cross-disciplinary, founder-led, precise, editorial, grounded. A systems studio that ships, with taste held under restraint. The type system has to read as an editorial publication built by engineers — never a default SaaS stack.",
      "type_direction": "A three-role system rather than a two-font pairing: a distinctive display face for ceremonial thresholds, a readable serif for narrative and case-study reading, and a monospace for the data, labels, and section numbering that signal real systems work. The split mirrors the brand duality — architectural precision (mono) against cultivated, human narrative (serif), with the display face marking the thresholds between them.",
      "pairing_logic": "Display + Serif gives editorial contrast and gravity; Serif + Mono gives the 'built by people who ship' tension. The monospace is load-bearing brand signal, not decoration — it carries metadata, diagram labels, and numbering so the system always shows its engineering substrate. Restraint is the rule: display type appears at thresholds only, the serif carries reading, and the mono stays in the data layer."
    },
    "typefaces": {
      "display": {
        "name": "Tyros Pro",
        "foundry": "Licensed display face (brand-provided)",
        "role": "display",
        "style": "distinctive editorial display",
        "weights": [400, 500, 700],
        "use_for": "Hero lines, section thresholds, ceremonial headings, the 'Digital Wilderness' headline, title slides, document covers. Used sparingly to mark thresholds, never for body or UI.",
        "source": "Brand-licensed (self-host the licensed webfont; not a default Google stack)",
        "fallback_stack": "'Tyros Pro', 'Tiempos Headline', Georgia, 'Times New Roman', serif"
      },
      "body": {
        "name": "SubjectivitySerif",
        "foundry": "Licensed editorial serif (brand-provided)",
        "role": "body / editorial",
        "style": "contemporary editorial serif",
        "weights": [400, 500, 600, 700],
        "use_for": "Narrative text, case-study and project-record copy, long-form editorial reading, memos, body paragraphs, pull quotes, lead text. The primary reading voice of the brand.",
        "source": "Brand-licensed (self-host the licensed webfont)",
        "fallback_stack": "'SubjectivitySerif', 'Source Serif Pro', Georgia, 'Times New Roman', serif"
      },
      "data_ops": {
        "name": "Fira Code",
        "foundry": "Mozilla / Nikita Prokopov (open source, SIL OFL)",
        "role": "data / ops / mono",
        "style": "monospace",
        "weights": [400, 500, 600],
        "use_for": "Technical labels, metadata, captions, diagram and system-map labels, section numbering, code and config, tabular figures, UI chrome where a systems-signal is wanted, eyebrow/kicker labels.",
        "source": "Google Fonts / GitHub (open source)",
        "fallback_stack": "'Fira Code', 'SFMono-Regular', 'JetBrains Mono', 'Menlo', 'Consolas', monospace"
      }
    },
    "type_scale": {
      "ratio": 1.25,
      "base_size": 16,
      "sizes": {
        "xs": { "size": "12px", "line_height": "16px", "use": "Captions, fine metadata, mono labels" },
        "sm": { "size": "14px", "line_height": "20px", "use": "Secondary text, mono section numbering" },
        "base": { "size": "16px", "line_height": "26px", "use": "Body / editorial reading (SubjectivitySerif)" },
        "lg": { "size": "18px", "line_height": "30px", "use": "Lead paragraphs, intro text" },
        "xl": { "size": "20px", "line_height": "28px", "use": "H6 / small headings" },
        "2xl": { "size": "24px", "line_height": "32px", "use": "H5" },
        "3xl": { "size": "30px", "line_height": "38px", "use": "H4" },
        "4xl": { "size": "36px", "line_height": "42px", "use": "H3" },
        "5xl": { "size": "48px", "line_height": "52px", "use": "H2 / section thresholds (Tyros Pro)" },
        "6xl": { "size": "60px", "line_height": "62px", "use": "H1 (Tyros Pro)" },
        "7xl": { "size": "72px", "line_height": "74px", "use": "Display / hero (Tyros Pro)" }
      }
    },
    "hierarchy": {
      "display": {
        "font": "Tyros Pro",
        "size": "72px",
        "weight": "700",
        "letter_spacing": "-0.02em",
        "line_height": "1.03",
        "color": "#0A0E14 on light / #FFFFFF on dark",
        "use": "Hero threshold lines such as the 'Digital Wilderness' headline."
      },
      "h1": {
        "font": "Tyros Pro",
        "size": "60px",
        "weight": "700",
        "letter_spacing": "-0.02em",
        "line_height": "1.03",
        "color": "#1A237E on light / #FFFFFF on dark"
      },
      "h2": {
        "font": "Tyros Pro",
        "size": "48px",
        "weight": "500",
        "letter_spacing": "-0.01em",
        "line_height": "1.08",
        "color": "#1A237E on light / #FFFFFF on dark"
      },
      "h3": {
        "font": "Tyros Pro",
        "size": "36px",
        "weight": "500",
        "letter_spacing": "-0.01em",
        "line_height": "1.15",
        "color": "#1A237E on light / #F8F9F9 on dark"
      },
      "h4": {
        "font": "SubjectivitySerif",
        "size": "24px",
        "weight": "600",
        "letter_spacing": "0",
        "line_height": "1.3",
        "color": "#1A237E on light / #F8F9F9 on dark"
      },
      "h5": {
        "font": "SubjectivitySerif",
        "size": "20px",
        "weight": "600",
        "letter_spacing": "0",
        "line_height": "1.4",
        "color": "#1A237E on light / #F8F9F9 on dark"
      },
      "h6": {
        "font": "Fira Code",
        "size": "14px",
        "weight": "500",
        "letter_spacing": "0.08em",
        "line_height": "1.4",
        "text_transform": "uppercase",
        "color": "#00897B signal / #37474F on light",
        "use": "Eyebrow / kicker labels and section signposts in the mono data voice."
      },
      "body": {
        "font": "SubjectivitySerif",
        "size": "16px",
        "weight": "400",
        "letter_spacing": "0",
        "line_height": "1.625",
        "color": "#37474F on light / #F8F9F9 on dark"
      },
      "body_small": {
        "font": "SubjectivitySerif",
        "size": "14px",
        "weight": "400",
        "letter_spacing": "0",
        "line_height": "1.5",
        "color": "#37474F on light / #B3B9BC on dark"
      },
      "caption": {
        "font": "Fira Code",
        "size": "12px",
        "weight": "400",
        "letter_spacing": "0.02em",
        "line_height": "1.4",
        "color": "#5B686F on light / #B3B9BC on dark",
        "use": "Image captions, fine print, timestamps."
      },
      "label": {
        "font": "Fira Code",
        "size": "12px",
        "weight": "500",
        "letter_spacing": "0.08em",
        "line_height": "1.3",
        "text_transform": "uppercase",
        "color": "#00897B on dark / #37474F on light",
        "use": "Metadata labels, diagram labels, section numbering, data keys."
      }
    },
    "pairing_rules": {
      "do": [
        "Set hero lines and section thresholds in Tyros Pro, and reserve it for those threshold moments only.",
        "Carry all narrative and case-study reading in SubjectivitySerif at 16px/1.625 for calm editorial rhythm.",
        "Use Fira Code for every metadata, label, caption, diagram-label, and section-number role so the system always shows its engineering substrate.",
        "Pair Tyros Pro display directly above SubjectivitySerif body for the editorial-gravity contrast.",
        "Keep generous line-height on serif body and tight, slightly negative tracking on large display."
      ],
      "dont": [
        "Don't use Tyros Pro for body text, UI, or anything below ~30px — it is a threshold face, not a workhorse.",
        "Don't set long-form reading in Fira Code; the mono is a data/label voice, not a paragraph voice.",
        "Don't reach for a default SaaS stack (Inter/Roboto/system-ui) as a primary face — only as deep fallback.",
        "Don't apply display type everywhere; if every heading shouts, nothing reads as a threshold.",
        "Don't mix more than these three families; restraint is the system."
      ]
    },
    "contrast_and_restraint": {
      "principle": "Contrast comes from role separation, not from piling on weights and sizes. Three voices — ceremonial (Tyros Pro), narrative (SubjectivitySerif), and data (Fira Code) — each stay in their lane. The page should feel like an engineering-grade editorial publication: lots of quiet serif reading, occasional display thresholds, and a precise mono layer of labels and numbers.",
      "rules": [
        "One display moment per view in most cases; let negative space do the amplifying.",
        "Set body measure to roughly 60–75 characters per line for editorial readability.",
        "Use the mono layer to signal precision sparingly — labels, numbers, captions — not as decoration sprinkled through prose.",
        "Prefer weight and space over color for emphasis in text; reserve teal/orange/green for true signal moments per the color system.",
        "Let the type sit on the dark-first canvas comfortably: white / Neutral 50 for primary, Neutral 300 for secondary on dark."
      ]
    },
    "implementation": {
      "css_variables": ":root {\n  --font-display: 'Tyros Pro', 'Tiempos Headline', Georgia, 'Times New Roman', serif;\n  --font-body: 'SubjectivitySerif', 'Source Serif Pro', Georgia, 'Times New Roman', serif;\n  --font-mono: 'Fira Code', 'SFMono-Regular', 'JetBrains Mono', Menlo, Consolas, monospace;\n  --type-base: 16px;\n  --type-ratio: 1.25;\n  --leading-tight: 1.08;\n  --leading-normal: 1.5;\n  --leading-relaxed: 1.625;\n  --tracking-display: -0.02em;\n  --tracking-label: 0.08em;\n}",
      "loading_strategy": "Self-host the licensed Tyros Pro and SubjectivitySerif webfonts (woff2, subset to required character sets); load Fira Code from Google Fonts or self-host. Use font-display: swap so the editorial fallbacks (Georgia / serif and Menlo / monospace) render immediately and reflow gracefully. Preload the display and body woff2 used above the fold.",
      "font_display": "swap"
    }
  }
}
```

### value-proposition
```json
{
  "skill": "value-proposition",
  "cluster": "foundation",
  "wave": 1,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "buyer_persona_reference": "Mira, the System-Carrying Founder — founder / CTO / innovation lead / product strategist running a lean senior team at a funded startup through scaleup.",
    "pain_gain_map": {
      "pains": {
        "functional": [
          "Too many vendors each understand only one slice of the problem, so Mira has to assemble coherence herself.",
          "AI proposals arrive technically shallow or operationally naive, demos that never mature into product.",
          "The system works on launch day but falls apart at ownership transfer, leaving the team unable to run it.",
          "Engineering vendors build the spec as handed over, mistakes included, with no push-back on a flawed requirement."
        ],
        "emotional": [
          "Exhaustion from becoming the full-time translator between five specialists who share no model of the problem.",
          "Distrust earned from glossy decks that get disconnected from shipped product reality.",
          "Anxiety that coherence is leaking at every handoff and that nobody owns the whole problem."
        ],
        "social": [
          "Looking like the bottleneck because the project's coherence depends entirely on the founder.",
          "Carrying the blame when a launched system breaks at handoff and the internal team cannot extend it.",
          "Being sold buzzwords by partners who notice neither specificity nor evidence of shipping."
        ]
      },
      "gains": {
        "functional": [
          "Solve an important problem with one studio that understands requirement, user, and operating reality at once.",
          "Receive a coherent system that the internal team can run, extend, and inherit after delivery.",
          "Get the requirement reshaped before the build, not built blindly as handed over."
        ],
        "emotional": [
          "Relief that one partner finally holds the whole problem instead of five disconnected vendors.",
          "Calm confidence that execution stays coherent from framing to handoff.",
          "Trust earned through specificity and shipped evidence rather than premium atmosphere."
        ],
        "social": [
          "Stop being the full-time vendor translator and reclaim time for founder work.",
          "Own the result rather than manage a stack of suppliers.",
          "Hand the internal team a legible system they can stand behind."
        ]
      }
    },
    "value_canvas": [
      {
        "customer_job": "Frame a problem too entangled to split across vendors.",
        "pain_point": "Too many vendors each understand only one slice of the problem.",
        "solution": "Requirement Architecture: problem framing, psychology mapping, operating constraints, and decision logic before implementation.",
        "gain_created": "One model of the problem carries from framing forward, so coherence is set before any code is written."
      },
      {
        "customer_job": "Ship a product that real users adopt and trust.",
        "pain_point": "Strategy decks get disconnected from shipped product reality.",
        "solution": "Product & Interface Systems where user behavior is treated as part of the system and stays grounded in engineering.",
        "gain_created": "Stronger trust and adoption because the experience survives implementation instead of breaking at the build."
      },
      {
        "customer_job": "Add AI without it being a demo that never matures.",
        "pain_point": "AI proposals are technically shallow or operationally naive.",
        "solution": "AI and automation built into the product's real logic and operating reality, not bolted on as a demo layer.",
        "gain_created": "Capability that runs in production and holds up against how the team actually works."
      },
      {
        "customer_job": "Own and run the system after the engagement ends.",
        "pain_point": "The system works on launch day but falls apart at ownership transfer.",
        "solution": "Handoff & Decision Systems: documentation, training, control surfaces, and operational artifacts shipped with the build.",
        "gain_created": "Cleaner ownership transfer, so the internal team can run, extend, and inherit the system without the studio."
      },
      {
        "customer_job": "Stop being the integrator between specialists.",
        "pain_point": "The founder becomes the full-time translator between five specialists.",
        "solution": "One founder-led delivery loop that carries framing, behavior, product, engineering, and handoff together.",
        "gain_created": "A single accountable owner of coherence, so the founder reclaims time and the project stops depending on her translation."
      }
    ],
    "differentiation": {
      "against_competitors": [
        "Unlike large innovation consultancies that package process but never ship, Thoughtseed carries the requirement all the way into a running system.",
        "Unlike premium product design agencies that hand off polished designs before the system runs, Thoughtseed owns engineering and ships the experience end to end.",
        "Unlike AI integration consultancies that stop at an impressive demo, Thoughtseed builds AI into the product's real logic and operating reality.",
        "Unlike specialized engineering vendors that build the spec as handed over, Thoughtseed reshapes a flawed requirement before the build.",
        "Unlike freelancer swarms that make the founder the integrator, Thoughtseed is one accountable owner of coherence across the whole problem."
      ],
      "ownable_territory": "Editorial precision with operating clarity — the one founder-led studio that turns a single requirement into a coherent system the client can own.",
      "unfair_advantage": "The same senior operators frame the requirement, design for adoption, ship the engineering, and build the handoff, removing the translation loss every single-slice competitor structurally depends on."
    },
    "statements": {
      "classic": "For the system-carrying founder, who is tired of being the full-time translator between vendors who each understand only one slice of the problem, Thoughtseed is the founder-led systems studio that frames the requirement, builds the system, and hands back a system the team can run. Unlike single-slice consultancies, design agencies, AI shops, engineering vendors, and freelancer swarms, we carry framing, behavior, product, engineering, and handoff in one delivery loop with senior judgment.",
      "one_sentence": "Thoughtseed helps the system-carrying founder turn one entangled requirement into a coherent system the team can run, by carrying framing, behavior, product, engineering, and handoff in a single founder-led delivery loop, unlike single-slice vendors who break coherence at every handoff.",
      "core": "One coherent system from requirement to handoff, owned by you.",
      "headlines": {
        "primary": "One studio carries the requirement all the way to a system you own.",
        "subheadline": "Thoughtseed frames the problem, builds the system, and hands it back legible, so your team can run and extend it without us.",
        "proof_point": "Shipped systems across AI, IoT, web, mobile, and creative technology, each delivered with the handoff artifacts a client can actually run."
      }
    },
    "headline_value_prop": "One studio carries the requirement all the way to a system you own.",
    "proof_points": [
      "Shipped systems across AI, IoT, web, mobile, and creative technology, paired with reusable internal product IP.",
      "Service surfaces that already span framing, design, engineering, and handoff under one operating logic.",
      "Decision artifacts and handoff documents that let the client's team run the system after delivery.",
      "Senior operators do the work directly, so less is lost in account-management translation."
    ],
    "differentiators": [
      "One coherent delivery loop: requirement, behavior, interface, and engineering are never handed between disconnected vendors.",
      "Founder-led judgment with less translation loss than layered account management.",
      "Handoff treated as a first-class output, so the client inherits a system instead of a dependency.",
      "User behavior kept grounded in real engineering, so adoption survives launch.",
      "Studio-plus-IP with a distinct visual and verbal territory beyond generic agency sameness."
    ],
    "value_hierarchy": {
      "primary": {
        "value": "One accountable owner of coherence from requirement to handoff.",
        "why_it_matters": "It ends Mira's exhausting role as the full-time translator between five specialists and stops coherence leaking at every handoff.",
        "proof": "A single founder-led delivery loop where the same senior operators frame, design, build, and hand off, evidenced by shipped systems and the handoff artifacts that ship with them."
      },
      "secondary": [
        {
          "value": "Ownership over dependency: a system the team can run, extend, and inherit.",
          "why_it_matters": "It removes the fear that the system breaks at handoff and locks the team to a vendor."
        },
        {
          "value": "User behavior grounded in engineering reality.",
          "why_it_matters": "It means adoption and trust hold after launch instead of degrading at implementation."
        },
        {
          "value": "AI and automation built into product logic, not bolted on.",
          "why_it_matters": "It answers the founder's distrust of shallow demos that never mature into product."
        }
      ],
      "table_stakes": [
        "Senior product design and interface craft",
        "Modern engineering across web, mobile, AI, automation, and connected products",
        "Professional discovery, scoping, and delivery artifacts"
      ]
    }
  }
}
```

### visual-language
```json
{
  "skill": "visual-language",
  "cluster": "identity",
  "wave": 3,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "theme": "Digital Wilderness",
    "essence": "Disciplined engineering meets organic emergence. Architectural precision held against cultivated texture; structured layouts against alive surfaces. Editorial, signal-rich, tactile, intentional, founder-led, technically grounded.",
    "reference_assets": {
      "moodboard": "generated/visual-language-board.png",
      "note": "The moodboard is a generated reference that captures the Digital Wilderness mood and material range. It is direction, not a deliverable, and contains no baked-in text or logos."
    },
    "visual_principles": [
      {
        "name": "Architectural precision against cultivated texture",
        "description": "Every composition holds an engineered structure (grids, crops, system diagrams, clean type) in tension with something grown and tactile (moss, oxidized copper, weathered stone, screen glow). Neither side wins; the duality is the brand."
      },
      {
        "name": "Signal over noise",
        "description": "A dark-first, cool-anchored field where a single warm or teal signal carries meaning. Restraint makes the signal legible. If everything is highlighted, nothing reads."
      },
      {
        "name": "Negative space as structure",
        "description": "Space is composed, not leftover. Architectural crops and intentional emptiness give the work editorial calm and let materials and type breathe."
      },
      {
        "name": "Material truth over gloss",
        "description": "Depth comes from real material and contrast — matte paper, brushed aluminium, architectural shadow — not from glossy plastic, drop-shadows, or glassmorphism. Tactile and grounded, like something that ships."
      },
      {
        "name": "Show the system",
        "description": "Geometric systems diagrams, labels, and numbering are part of the aesthetic. The work looks like it was built by people who think in systems and ship them."
      }
    ],
    "materials": [
      "matte paper",
      "black ink",
      "glass",
      "brushed aluminium",
      "oxidized copper",
      "weathered stone",
      "living moss",
      "screen glow",
      "architectural shadow"
    ],
    "photography": {
      "style": {
        "approach": "editorial documentary",
        "lighting": "natural, directional, clean contrast; controlled hard shadow for architectural depth — never flat or over-lit",
        "composition": "architectural crops, asymmetric framing, intentional negative space; structure-forward",
        "color_treatment": "cool cast anchored to the deep blue / near-black system, with restrained warm or teal signal accents from the real scene — desaturated rather than candy-bright",
        "subject_focus": "materials, prototyping spaces, worktables, structured interiors, hands building, devices and screens in context; environment and object over staged people",
        "mood": "calm, intentional, grounded, signal-rich; founder-led and technical, not aspirational-glossy",
        "context": "studio, workshop, structured interior, architectural exterior; real working surfaces"
      },
      "references": [
        "A matte-paper worktable shot from directly above: prototypes, system sketches, a device, raking natural light and clean shadow.",
        "An architectural interior crop — concrete, glass, steel — with deep negative space and a single screen-glow accent in the frame.",
        "A close, tactile macro of oxidized copper or living moss against a machined aluminium edge: precision meeting growth.",
        "A structured workshop scene, cool light, desaturated palette, a small teal or warm signal occurring naturally in the equipment."
      ],
      "prompt_template": "[Scene: prototyping space / worktable / structured interior / architectural crop] in an editorial-documentary photography style. Lighting: natural, directional, clean contrast with controlled architectural shadow. Mood: calm, intentional, grounded, technically precise. Color palette: cool, anchored to deep blue-black and cool grays with a single restrained teal or warm signal accent; desaturated, not candy-bright. Composition: architectural crop, asymmetric, generous intentional negative space. Materials in frame: matte paper, brushed aluminium, glass, weathered stone, oxidized copper, or living moss. High-quality professional photography. No text, no lettering, no logos anywhere in the image. Avoid: purple-on-white SaaS gradients, stock startup team photos, empty futurism, wellness or mystical fog, glossy plastic, cartoon elements."
    },
    "illustration": {
      "style": {
        "type": "geometric systems diagrams blended with organic signal patterns and cultivated-landscape motifs",
        "complexity": "moderate — legible structure, not busy",
        "line_weight": "precise, mostly uniform technical line with selective organic variation where growth motifs enter",
        "color_approach": "brand palette only — Mindful Gray / neutral structure with teal signal lines, Growth Light for positive/emergent notes, Deep Quantum Blue fields, and Energetic Orange reserved for a single highlighted element",
        "character_style": "non-figurative by default; if any figure appears, geometric and simplified, never cartoonish",
        "motif": "the Digital Wilderness duality — engineered grid/diagram structure overgrown or interwoven with organic signal patterns and cultivated-landscape forms (roots, branches, contour lines)"
      },
      "prompt_template": "[Subject: systems diagram / signal pattern / cultivated-landscape motif] as a geometric technical illustration blended with organic growth forms. Line work: precise, mostly uniform, with selective organic variation. Colors: brand palette only — neutral gray structure, teal (#00897B) signal lines, Growth Light (#B8E986) emergent accents, deep blue (#1A237E) fields, with at most one Energetic Orange (#F57C00) highlight. Style: geometric meets organic, moderate complexity, legible not busy. Background: dark-first canvas (#0A0E14) or matte light. Vector-style, clean edges. No text, no lettering, no logos in the artwork. Avoid: purple SaaS gradients, glossy 3D plastic, cartoon iconography, mystical fog."
    },
    "iconography": {
      "style": "line, single-weight, with optional duotone using a neutral plus one signal color",
      "stroke_weight": "2px standard, 1.5px at small sizes",
      "corner_radius": "2px (near-sharp) — precise and engineered, lightly softened",
      "grid_size": "24x24 base, scaled to 16 / 32 / 48",
      "optical_adjustments": "yes — balance weight optically across the set",
      "categories": [
        "UI icons (navigation, actions, states)",
        "feature icons (service modules: requirement architecture, product & interface systems, handoff & decision systems)",
        "category icons (sections, document and diagram types)"
      ],
      "note": "Icons share one weight and one geometric construction logic so the set reads as a system. Color follows the palette: neutral by default, teal for active/signal, never the ignition orange except on a true primary action."
    },
    "patterns": {
      "type": "geometric systems grid interwoven with organic signal / contour motifs",
      "scale": "medium — present but quiet; used as texture, not focal",
      "usage": [
        "section dividers and backgrounds",
        "document covers and closeout collateral",
        "quiet watermark-scale texture behind dark fields",
        "data-viz framing and diagram grounds"
      ],
      "colors": "brand palette only — neutral structure on the dark-first canvas with sparse teal or Growth Light signal; never large fills of orange or green",
      "prompt_template": "Seamless tileable pattern: a fine geometric systems grid interwoven with organic contour and root/branch signal motifs. Style: geometric meets organic, minimal and quiet. Colors: neutral gray structure on a dark canvas (#0A0E14) or matte light, with sparse teal (#00897B) or Growth Light (#B8E986) signal lines only. Suitable as a subtle background texture. No text, no lettering, no logos. Avoid: purple gradients, glossy plastic, busy rainbow palettes."
    },
    "composition_bias": {
      "principles": [
        "Architectural crops: frame tight on structure and let edges run; favor strong horizon/vertical lines.",
        "Intentional negative space: compose emptiness deliberately for editorial calm.",
        "Asymmetric, grid-aware layouts over centered symmetry.",
        "Dark-first fields with a single signal moment per composition.",
        "Build depth with material and contrast (matte paper, brushed metal, architectural shadow), not gloss or drop-shadows."
      ]
    },
    "forbidden_visuals": [
      "generic purple-on-white SaaS gradients",
      "stock startup team photography",
      "empty futurism / sci-fi cliché",
      "wellness clichés or mystical fog without structure",
      "glossy plastic surfaces",
      "cartoon iconography",
      "ANY text, lettering, words, or logos baked permanently into generated imagery"
    ],
    "guidelines": {
      "do": [
        "Hold architectural precision against cultivated, tactile texture in every composition.",
        "Anchor on the dark-first cool field and let one teal or warm signal carry meaning.",
        "Use editorial-documentary photography of real materials, prototyping spaces, and structured interiors.",
        "Compose with architectural crops and intentional negative space.",
        "Keep illustration to geometric systems diagrams blended with organic signal motifs, in brand colors only.",
        "Build depth from material and contrast; reference the moodboard at generated/visual-language-board.png for mood."
      ],
      "dont": [
        "Don't use purple-on-white SaaS gradients or any avoided-startup look.",
        "Don't use stock startup team photography or staged perfection.",
        "Don't drift into empty futurism, sci-fi cliché, or mystical wellness fog without structure.",
        "Don't use glossy plastic surfaces, glassmorphism, or gloss-based depth.",
        "Don't use cartoon iconography.",
        "Don't bake any text, lettering, words, or logos into generated imagery.",
        "Don't flood compositions with signal color — scarcity is what makes teal/orange/green read as signal."
      ]
    }
  }
}
```

### voice-and-tone
```json
{
  "skill": "voice-and-tone",
  "cluster": "strategy",
  "wave": 2,
  "timestamp": "2026-06-07T10:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "voice_matrix": {
      "formality": 0.55,
      "enthusiasm": 0.4,
      "technicality": 0.6,
      "warmth": 0.5,
      "authority": 0.7
    },
    "context_modifiers": {
      "website_hero": { "enthusiasm": 0.45, "warmth": 0.55, "note": "Spare, memorable, atmospheric. Atmosphere comes from phrasing and restraint, not volume." },
      "proposal": { "formality": 0.6, "authority": 0.75, "note": "Confident, concrete, disciplined. Lead with the requirement and the plan, not the pitch." },
      "documentation": { "formality": 0.6, "enthusiasm": 0.3, "technicality": 0.75, "note": "Explicit, structured, low-drama. Optimized for someone inheriting the system." },
      "case_study": { "warmth": 0.55, "authority": 0.7, "note": "Reflective, specific, quietly proud. Evidence sits next to every claim." },
      "founder_note": { "formality": 0.45, "warmth": 0.6, "note": "Grounded, exact, slightly poetic only when earned. Peer to peer with the founder." }
    },
    "voice_attributes": {
      "tone1": "Clear",
      "tone2": "Grounded",
      "tone3": "Crafted"
    },
    "voice_character": {
      "speaking_as": "The founder-side systems translator: an operator who has built systems and lived with ambiguity, not an abstract strategist, growth marketer, or inflated agency.",
      "relationship": "Peer to the founder. A senior partner who carries the requirement and hands back something the client can own, not a vendor managing an account.",
      "language_register": "Clear, calm, technically precise, human, founder-led, editorially restrained. Short declarative sentences with evidence close to the claim."
    },
    "voice_prompt_template": "Please write as the founder-side systems translator for Thoughtseed, a founder-led systems studio. Use a clear, grounded, and crafted tone, speaking as an operator who has built real systems and lived with ambiguity. Write in short declarative sentences and keep evidence close to every claim. Use real product, systems, and delivery language when it improves understanding, never as jargon theater. Prefer requirement, operating logic, user behavior, founder context, systems, signal, coherence, intentional, crafted, shipped, legible, inherited, handoff, cross-disciplinary, and delivery loop. Describe the downstream effects of how the work is done, such as clearer requirements, calmer execution, stronger trust and adoption, and cleaner ownership transfer, rather than the internal method or metaphor behind it. Never use consciousness-aligned, conscious growth, consciousness technology, organic growth operations, disruptive, revolutionary, synergy, best-in-class, future-proof, cutting-edge, guru, healing journey, vibration, AMC, or full-service agency. Do not name internal methodology in public copy and do not describe Thoughtseed as an always-on retainer agency. Keep ambitious ideas calm, let atmosphere come from phrasing and image choice, and write like someone who ships.",
    "tone_variations": {
      "announcement": {
        "adjustment": "Calm confidence over celebration. State what shipped and what it does, then stop.",
        "example": "We shipped the system. It frames the requirement, runs in production, and the team can extend it without us."
      },
      "support": {
        "adjustment": "Steady and exact. Acknowledge the situation plainly and point to the next concrete step.",
        "example": "Here is exactly what changed and what it means for your system. Nothing in production is at risk while we resolve it."
      },
      "education": {
        "adjustment": "Explicit, structured, low-drama. Explain the system as if briefing the person who will inherit it.",
        "example": "Here is how the delivery loop works, step by step, and where each decision gets made."
      },
      "crisis": {
        "adjustment": "Serious and grounded. Keep claims close to evidence and say what is being done.",
        "example": "We take this seriously. Here is what happened, what we know, and the next action with a timestamp."
      },
      "sales": {
        "adjustment": "Confident and concrete. Lead with the requirement and the coherent system, not pressure.",
        "example": "Bring the requirement. We study it, build the system, and hand it back in a form you can run."
      }
    },
    "channel_calibration": {
      "website_hero": "Spare, memorable, atmospheric. Use the approved messaging hierarchy verbatim where copy is needed.",
      "proposal_opener": "Confident, concrete, disciplined. Name the requirement and the plan before the credentials.",
      "technical_documentation": "Explicit, structured, low-drama. Written for the operator who inherits the system.",
      "case_study": "Reflective, specific, quietly proud. Pair every outcome with the evidence behind it.",
      "founder_note": "Grounded, exact, slightly poetic only when earned. Sound close to the people doing the work."
    },
    "language_guidelines": {
      "use": [
        "Short declarative sentences",
        "Second person when addressing the founder; first person plural for the studio",
        "Concrete, specific, shippable language",
        "Evidence placed immediately next to the claim",
        "Real systems, product, and delivery terminology when it improves understanding",
        "Downstream effects of the process: clearer requirements, calmer execution, stronger trust and adoption, cleaner ownership transfer, more coherent systems"
      ],
      "avoid": [
        "Naming the internal methodology or its metaphors in public copy",
        "Framing Thoughtseed as an always-on retainer or full-service agency",
        "Mystical, juvenile, or enterprise-bureaucratic phrasing",
        "Superlatives or premium atmosphere without evidence",
        "Jargon used as theater",
        "Overexplaining ambitious ideas instead of keeping them calm"
      ],
      "vocabulary_bank": {
        "preferred": [
          "requirement",
          "operating logic",
          "user behavior",
          "founder context",
          "systems",
          "signal",
          "coherence",
          "intentional",
          "crafted",
          "shipped",
          "legible",
          "inherited",
          "handoff",
          "cross-disciplinary",
          "delivery loop"
        ],
        "prohibited": [
          "consciousness-aligned",
          "conscious growth",
          "consciousness technology",
          "organic growth operations",
          "disruptive",
          "revolutionary",
          "synergy",
          "best-in-class",
          "future-proof",
          "cutting-edge",
          "guru",
          "healing journey",
          "vibration",
          "AMC",
          "full-service agency"
        ]
      }
    },
    "approved_brand_phrases": [
      "Digital Wilderness",
      "We plant ideas. They grow wild.",
      "Build the system, not just the story.",
      "From requirement to handoff.",
      "One coherent delivery loop.",
      "Cross-disciplinary rigor.",
      "Bring the requirement."
    ],
    "do": [
      "Say the thing directly; prefer plain statements over padded agency prose.",
      "Keep evidence next to the claim: shipped systems, technical range, handoff artifacts.",
      "Tie psychology and behavior back to system design, adoption, and operating reality.",
      "Translate internal methodology into its visible effects for any public audience.",
      "Write like someone who has shipped things."
    ],
    "dont": [
      "Don't use any avoided term in public copy: consciousness-aligned, conscious growth, consciousness technology, organic growth operations, disruptive, revolutionary, synergy, best-in-class, future-proof, cutting-edge, guru, healing journey, vibration, AMC, full-service agency.",
      "Don't make the Krebs cycle, the requirement-to-handoff loop internals, or consciousness research a public headline or category claim.",
      "Don't describe Thoughtseed as an always-on retainer agency; the model is scoped delivery with strong handoff.",
      "Don't sound mystical, juvenile, or enterprise-bureaucratic.",
      "Don't reach for atmosphere through abstraction; let it come from phrasing and image choice."
    ],
    "layer_discipline": {
      "backstage_internal": "Inside team operations, research, and delivery management, Thoughtseed can name the Krebs Cycle of Creativity, the requirement-to-handoff loop internals, and the cross-disciplinary research origins that shaped its sensitivity to behavior and trust.",
      "frontstage_public": "Public copy foregrounds only the visible effects: clearer requirements, calmer execution, stronger trust and adoption, cleaner ownership transfer, and more coherent systems.",
      "rule": "If public copy contains any avoided term, or names the Krebs cycle or consciousness as a category claim, it is wrong. Translate it into effects instead."
    },
    "tone_words": [
      "clear",
      "calm",
      "precise",
      "grounded",
      "crafted",
      "founder-led",
      "coherent"
    ],
    "example_phrases": [
      { "instead_of": "We're a full-service agency delivering revolutionary, future-proof solutions.", "use": "We're a founder-led systems studio. We study the requirement, build the system, and hand it back." },
      { "instead_of": "Our consciousness-aligned process unlocks organic growth and synergy.", "use": "Our delivery loop keeps the work coherent from requirement to handoff, so adoption holds after launch." },
      { "instead_of": "A best-in-class, cutting-edge, disruptive platform.", "use": "A coherent system you can run, extend, and inherit." },
      { "instead_of": "We partner with you on an ongoing growth journey.", "use": "We frame the requirement, ship the system, and transfer ownership so you can run it yourself." }
    ]
  }
}
```

### welcome-email-sequence
```json
{
  "skill": "welcome-email-sequence",
  "cluster": "content",
  "wave": 6,
  "timestamp": "2026-06-08T06:00:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "sequence_strategy": {
      "context": "Sent after a founder brings a requirement and begins an engagement with Thoughtseed Studio, typically a System Sprint or a Requirement-to-Handoff Build.",
      "goals": [
        "Confirm the engagement and set a calm, concrete tone",
        "Introduce the studio and the operators who will do the work",
        "Explain how the delivery loop runs, stage by stage",
        "Make the requirement-gathering step easy and clear",
        "Set expectations for handoff from the very first email"
      ],
      "timing": "Email 1 immediately after kickoff is scheduled; Email 2 day 1; Email 3 day 3; Email 4 day 5; Email 5 day 8",
      "total_emails": 5,
      "voice_note": "Peer to the founder. Short declarative sentences. No celebration theater, no superlatives, no internal methodology, no avoided terms."
    },
    "emails": [
      {
        "number": 1,
        "name": "Kickoff Confirmation",
        "send_timing": "Immediate",
        "goal": "Confirm the engagement and state what happens next",
        "tone": "Grounded, warm, exact",
        "subject_lines": {
          "primary": "We have the requirement. Here is what happens next.",
          "variation_a": "Your build is on the calendar",
          "variation_b": "From requirement to handoff: where we start"
        },
        "preview_text": "One team, one delivery loop, a system you can run.",
        "body": "Thanks for bringing the requirement to us.\n\nHere is the short version of what you have signed up for. Thoughtseed is a founder-led systems studio. One team carries framing, user behavior, product, engineering, and handoff inside a single delivery loop. The people who frame the requirement are the people who build it, so coherence holds from the first decision to the running system.\n\nWhat happens next:\n\n1. We confirm the kickoff time and who joins from your side.\n2. We open with the requirement: the problem, the people who will use the system, and the way you want to run it.\n3. From there we design, build, and hand it back in a form your team can own.\n\nYou will always talk to the operators doing the work, not an account layer. If anything is unclear before kickoff, reply to this email and ask.",
        "cta": {
          "text": "Confirm your kickoff details",
          "action": "schedule_kickoff"
        },
        "ps": "P.S. Handoff is not the last step we think about. It is the first. We will tell you what you inherit before we build it."
      },
      {
        "number": 2,
        "name": "Who Does The Work",
        "send_timing": "Day 1",
        "goal": "Introduce the studio and the founder-led model",
        "tone": "Personal, founder-close, restrained",
        "subject_lines": {
          "primary": "The people who will frame and build your system",
          "variation_a": "No translators in between",
          "variation_b": "Why one studio instead of five vendors"
        },
        "preview_text": "Senior operators, engaged directly, less lost in translation.",
        "body": "A quick note on who you are working with, and why the studio is shaped this way.\n\nMost important work gets split across strategy, design, engineering, and operations vendors who never share one model of the problem. The founder ends up as the full-time translator between them. Coherence breaks before launch. Ownership breaks after it.\n\nWe built Thoughtseed so that does not happen. Senior operators do the work directly. The same people frame the requirement, design the interface and the operating logic, ship the engineering, and prepare the handoff. Decisions stay close to the work and to your operating reality, and they get written down as artifacts you can trace.\n\nWe take fewer engagements and go deeper. That is deliberate. It is how the work stays coherent.",
        "cta": {
          "text": "Meet the team before kickoff",
          "action": "view_team"
        },
        "ps": "P.S. We are not an always-on retainer. This is scoped delivery with a real handoff at the end."
      },
      {
        "number": 3,
        "name": "How The Delivery Loop Runs",
        "send_timing": "Day 3",
        "goal": "Explain the four stages so the founder knows what to expect",
        "tone": "Explicit, structured, low-drama",
        "subject_lines": {
          "primary": "How the delivery loop works, stage by stage",
          "variation_a": "Requirement, system, build, handoff",
          "variation_b": "Where each decision gets made"
        },
        "preview_text": "Four stages, one motion, nothing lost between vendors.",
        "body": "Here is how your engagement runs. Four stages, one continuous loop.\n\n1. Requirement. We study the requirement, the people who will use the system, and the way you want to run it. Constraints and tradeoffs surface before anything is built.\n\n2. System. We design the interface and the operating logic together. User behavior is treated as part of the system, not a layer added later.\n\n3. Build. Senior engineers ship the system. What we framed is what we build, so the work stays legible from the first decision to the running product.\n\n4. Handoff. Documentation, training, and control surfaces ship with the build. You inherit a system you can run, extend, and own without us.\n\nEach stage feeds the next. The same team carries it the whole way.",
        "cta": {
          "text": "See the delivery loop in detail",
          "action": "view_delivery_loop"
        },
        "ps": "P.S. If you want to know where a specific decision gets made, ask. The loop is meant to be legible, not mysterious."
      },
      {
        "number": 4,
        "name": "Bring The Full Requirement",
        "send_timing": "Day 5",
        "goal": "Make it easy to share the context the studio needs",
        "tone": "Practical, direct, collaborative",
        "subject_lines": {
          "primary": "What to bring to the requirement session",
          "variation_a": "The more context, the cleaner the system",
          "variation_b": "Quick prep before we frame the work"
        },
        "preview_text": "Bring the messy version. We are built for entangled problems.",
        "body": "Before we frame the work, it helps to gather what you already know. You do not need it polished. The messy version is fine. We are built for problems that are too entangled to split.\n\nIf you have them, bring:\n\n- The problem in your own words, including the parts that feel unresolved.\n- Who will use the system, and what would make them trust and adopt it.\n- How you want to run and own the result after delivery.\n- Any constraints: timelines, existing systems, team capacity.\n- What a good outcome looks like to you.\n\nWe will take it from there, surface the real decision pressure, and frame the requirement with you. The clearer the input, the more coherent the system we hand back.",
        "cta": {
          "text": "Add your context to the brief",
          "action": "open_requirement_brief"
        },
        "ps": "P.S. Half-formed is welcome. Framing the requirement is part of the work, not a prerequisite for starting."
      },
      {
        "number": 5,
        "name": "What You Will Inherit",
        "send_timing": "Day 8",
        "goal": "Reinforce handoff as the deliverable and open the line for questions",
        "tone": "Reflective, confident, grounded",
        "subject_lines": {
          "primary": "The work will be yours to run",
          "variation_a": "What ownership transfer looks like here",
          "variation_b": "A system you can run, extend, and inherit"
        },
        "preview_text": "Ownership over dependency, every time.",
        "body": "One last note as we get going, and it is the one we care about most.\n\nA system that works on launch day but breaks at ownership transfer is not finished. So we treat that transfer as the deliverable, not post-project admin.\n\nWhen we hand back the work, you inherit:\n\n- A running system, not a deck disconnected from shipped reality.\n- Documentation written to be read by the team that will run it.\n- Control surfaces and operational artifacts that keep the system legible.\n- A model of the problem you can carry forward without us.\n\nThat is the whole point of the loop. We frame the requirement, build the system, and hand it back in a form you can actually run. If a question comes up at any stage, reply here. You are talking to the people doing the work.",
        "cta": {
          "text": "Ask us anything before kickoff",
          "action": "reply_to_team"
        },
        "ps": "P.S. We plant ideas. They grow wild. The version you inherit should keep growing after we step back."
      }
    ]
  }
}
```

### wiki-site-generator
```json
{
  "skill": "wiki-site-generator",
  "cluster": "synthesis",
  "wave": 7,
  "timestamp": "2026-06-08T06:10:00Z",
  "status": "complete",
  "version": "1.0.0",
  "data": {
    "artifact_kind": "specification",
    "brand": "Thoughtseed",
    "manifest_source": ".brandmint/asset-manifest.json",
    "site_config": {
      "framework": "astro",
      "template": "starlight",
      "theme": "editorial",
      "theme_description": "A matte, signal-rich editorial documentation theme — NOT glossy. Dark-first cool canvas (#0A0E14) with the deep-blue anchor (#1A237E), cool blue-gray scaffolding (#37474F), a teal (#00897B) working signal, and the orange (#F57C00) reserved for the single primary action. Depth comes from material, contrast, and negative space, never from gloss, glassmorphism, or drop-shadows. Reads like an engineering-grade publication.",
      "theme_tokens": {
        "canvas_dark": "#0A0E14",
        "anchor": "#1A237E",
        "scaffolding": "#37474F",
        "signal_teal": "#00897B",
        "ignition_orange_cta_only": "#F57C00",
        "positive_green": "#B8E986",
        "cta_label_rule": "Orange CTA buttons MUST use deep-blue (#1A237E) label text, never white (white-on-orange fails at 2.70:1).",
        "font_display": "Tyros Pro (thresholds only)",
        "font_body": "SubjectivitySerif (reading voice, 16px/1.625)",
        "font_mono": "Fira Code (labels, metadata, section numbering)",
        "color_label_rule": "Internal palette names are never surfaced in any page text, nav label, or UI string."
      },
      "appearance_rules": [
        "Dark-first by default; light surfaces only for long-form reading pages and print.",
        "One display moment per view; let negative space amplify.",
        "Mono layer carries section numbering and metadata so the system always shows its engineering substrate.",
        "Signal colors stay scarce; never flood teal, orange, or green.",
        "No gloss, no glassmorphism, no drop-shadow depth — material and contrast only."
      ]
    },
    "asset_handling": {
      "manifest_loaded": true,
      "manifest_valid": true,
      "copy_policy": "Only assets present in asset-manifest.json are copied to /public/images/; every source path is verified to exist before copy. No blind cp.",
      "assets_to_copy": {
        "total": 20,
        "user_provided": 4,
        "generated": 16,
        "deterministic": 4
      },
      "image_destination_mapping": {
        "logo": "/images/logo/",
        "logo-icon": "/images/logo/",
        "reference": "/images/logo/reference/",
        "hero": "/images/hero/",
        "lifestyle": "/images/photography/",
        "product": "/images/product/",
        "illustration": "/images/illustrations/",
        "icons": "/images/illustrations/",
        "moodboard": "/images/illustrations/",
        "pattern": "/images/patterns/",
        "social": "/images/social/"
      },
      "copy_verification": {
        "all_sources_exist": true,
        "all_copies_planned": true,
        "missing_sources": []
      }
    },
    "site_structure": {
      "nav": [
        {
          "group": "About",
          "items": [
            { "label": "Overview", "path": "/about" },
            { "label": "Story", "path": "/about/story" },
            { "label": "Values", "path": "/about/values" }
          ]
        },
        {
          "group": "Identity",
          "items": [
            { "label": "Logo", "path": "/identity/logo" },
            { "label": "Colors", "path": "/identity/colors" },
            { "label": "Typography", "path": "/identity/typography" },
            { "label": "Visual Style", "path": "/identity/visual-style" }
          ]
        },
        {
          "group": "Positioning",
          "items": [
            { "label": "Value Proposition", "path": "/positioning/value" },
            { "label": "Audience", "path": "/positioning/audience" },
            { "label": "Competitive Frame", "path": "/positioning/competitive" }
          ]
        },
        {
          "group": "Voice & Messaging",
          "items": [
            { "label": "Voice Guidelines", "path": "/voice/guidelines" },
            { "label": "Messaging Pillars", "path": "/messaging/pillars" }
          ]
        },
        {
          "group": "Product",
          "items": [
            { "label": "Thoughtseed Studio", "path": "/product/overview" }
          ]
        },
        {
          "group": "Assets",
          "items": [
            { "label": "Asset Inventory", "path": "/assets/inventory" },
            { "label": "Downloads", "path": "/assets/downloads" }
          ]
        }
      ],
      "pages": [
        {
          "path": "/about",
          "title": "Overview",
          "source_skills": ["brand-foundation"],
          "content_summary": "Founder-led systems studio; essence coherent systems, cultivated; mission, vision, and the Sage-with-a-Creator's-hands personality. Visible effects only.",
          "assets_referenced": [
            { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided" },
            { "id": "hero-02-establishing", "path": "./generated/hero-02-establishing.png", "origin": "generated" }
          ]
        },
        {
          "path": "/about/story",
          "title": "Story",
          "source_skills": ["brand-story"],
          "content_summary": "Planted in 2020 from the observation that the problems worth solving were never single-discipline problems; fragmentation answered by one delivery loop; Digital Wilderness.",
          "assets_referenced": [
            { "id": "hero-01-digital-wilderness", "path": "./generated/hero-01-digital-wilderness.png", "origin": "generated" },
            { "id": "lifestyle-02-studio", "path": "./generated/lifestyle-02-studio.png", "origin": "generated" }
          ]
        },
        {
          "path": "/about/values",
          "title": "Values",
          "source_skills": ["brand-foundation"],
          "content_summary": "Clarity over theater, cross-disciplinary rigor, delivery integrity, accountable handoff, selective focus — each with what it looks like in practice.",
          "assets_referenced": []
        },
        {
          "path": "/identity/logo",
          "title": "Logo",
          "source_skills": ["logo-concept"],
          "content_summary": "Two canonical marks used as a system; monochrome rule; clear space; minimum sizes; substitution rule; generated seal art is reference only, never a mark.",
          "assets_referenced": [
            { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided" },
            { "id": "logo-tree-mark", "path": "./assets/thoughtseed-tree-mark-black-3x.png", "origin": "user_provided" },
            { "id": "logo-reference-01", "path": "./assets/thoughtseed-logo-reference-01.jpg", "origin": "user_provided" },
            { "id": "logo-reference-02", "path": "./assets/thoughtseed-logo-reference-02.jpg", "origin": "user_provided" }
          ]
        },
        {
          "path": "/identity/colors",
          "title": "Colors",
          "source_skills": ["color-palette"],
          "content_summary": "Dark-first cool palette by hex and role; 60/25/10/5 distribution; the deep-blue-on-orange CTA contrast rule; purple-SaaS avoid. Internal color names omitted from page text.",
          "assets_referenced": [
            { "id": "pattern-01-dark", "path": "./generated/pattern-01-dark.png", "origin": "generated" },
            { "id": "pattern-02-light", "path": "./generated/pattern-02-light.png", "origin": "generated" }
          ]
        },
        {
          "path": "/identity/typography",
          "title": "Typography",
          "source_skills": ["typography"],
          "content_summary": "Three-role system: Tyros Pro display, SubjectivitySerif body, Fira Code data layer; 1.25 scale; restraint by role separation; self-host strategy.",
          "assets_referenced": []
        },
        {
          "path": "/identity/visual-style",
          "title": "Visual Style",
          "source_skills": ["visual-language"],
          "content_summary": "Digital Wilderness principles; materials; editorial-documentary photography; geometric-organic illustration; icons, patterns; forbidden visuals.",
          "assets_referenced": [
            { "id": "visual-language-board", "path": "./generated/visual-language-board.png", "origin": "generated" },
            { "id": "illus-01-systems-organism", "path": "./generated/illus-01-systems-organism.png", "origin": "generated" },
            { "id": "illus-02-delivery-loop", "path": "./generated/illus-02-delivery-loop.png", "origin": "generated" },
            { "id": "icons-01-sheet", "path": "./generated/icons-01-sheet.png", "origin": "generated" },
            { "id": "lifestyle-01-worktable", "path": "./generated/lifestyle-01-worktable.png", "origin": "generated" }
          ]
        },
        {
          "path": "/positioning/value",
          "title": "Value Proposition",
          "source_skills": ["value-proposition"],
          "content_summary": "One studio carries the requirement to a system you own; primary value of a single accountable owner of coherence; pain-to-gain motion; table stakes assumed.",
          "assets_referenced": [
            { "id": "product-01-system-artifacts", "path": "./generated/product-01-system-artifacts.png", "origin": "generated" }
          ]
        },
        {
          "path": "/positioning/audience",
          "title": "Audience",
          "source_skills": ["buyer-persona"],
          "content_summary": "Mira, the System-Carrying Founder — profile, values, jobs to be done, and what she notices and respects.",
          "assets_referenced": []
        },
        {
          "path": "/positioning/competitive",
          "title": "Competitive Frame",
          "source_skills": ["competitor-analysis", "product-positioning"],
          "content_summary": "Five single-slice alternatives and their translation-loss dependency; the ownable territory of editorial precision with operating clarity; the founder-led unfair advantage.",
          "assets_referenced": []
        },
        {
          "path": "/voice/guidelines",
          "title": "Voice Guidelines",
          "source_skills": ["voice-and-tone"],
          "content_summary": "Founder-side systems translator voice; preferred vocabulary; prohibited terms; layer discipline; do/don't examples.",
          "assets_referenced": []
        },
        {
          "path": "/messaging/pillars",
          "title": "Messaging Pillars",
          "source_skills": ["messaging-framework"],
          "content_summary": "Brand promise; Digital Wilderness headline and tagline; four pillars with proof points; approved phrases; objection responses.",
          "assets_referenced": [
            { "id": "social-og", "path": "./generated/social-og.png", "origin": "generated" },
            { "id": "social-x-header", "path": "./generated/social-x-header.png", "origin": "generated" },
            { "id": "social-ig-story", "path": "./generated/social-ig-story.png", "origin": "generated" }
          ]
        },
        {
          "path": "/product/overview",
          "title": "Thoughtseed Studio",
          "source_skills": ["product-description", "landing-page-copy"],
          "content_summary": "Thoughtseed Studio described across lengths; three service modules; System Sprint and Requirement-to-Handoff Build; the numbered homepage delivery-loop arc.",
          "assets_referenced": [
            { "id": "hero-03-mobile", "path": "./generated/hero-03-mobile.png", "origin": "generated" },
            { "id": "product-02-screen-surface", "path": "./generated/product-02-screen-surface.png", "origin": "generated" }
          ]
        },
        {
          "path": "/assets/inventory",
          "title": "Asset Inventory",
          "source_skills": [],
          "content_summary": "Auto-generated from the asset manifest: user-provided (deterministic) assets and generated assets with wave, skill, and location. Mirrors the manifest exactly.",
          "assets_referenced": [
            { "id": "logo-wordmark", "path": "./assets/thoughtseed-horizontal-wordmark-3x.png", "origin": "user_provided" },
            { "id": "logo-tree-mark", "path": "./assets/thoughtseed-tree-mark-black-3x.png", "origin": "user_provided" }
          ]
        },
        {
          "path": "/assets/downloads",
          "title": "Downloads",
          "source_skills": [],
          "content_summary": "Links to the deliverables package and per-category asset downloads; documents the user-provided vs generated split.",
          "assets_referenced": []
        }
      ]
    },
    "per_page_asset_summary": {
      "total_unique_assets_referenced": 20,
      "user_provided_referenced": 4,
      "generated_referenced": 16,
      "all_in_manifest": true,
      "unique_asset_ids": [
        "logo-wordmark", "logo-tree-mark", "logo-reference-01", "logo-reference-02",
        "hero-01-digital-wilderness", "hero-02-establishing", "hero-03-mobile",
        "lifestyle-01-worktable", "lifestyle-02-studio",
        "product-01-system-artifacts", "product-02-screen-surface",
        "illus-01-systems-organism", "illus-02-delivery-loop",
        "icons-01-sheet", "pattern-01-dark", "pattern-02-light",
        "visual-language-board", "social-og", "social-x-header", "social-ig-story"
      ]
    },
    "build_stack_recommendation": {
      "framework": "Astro",
      "docs_template": "Starlight",
      "styling": "Astro/Starlight custom CSS with the editorial theme tokens; self-hosted Tyros Pro + SubjectivitySerif woff2, Fira Code from Google Fonts or self-host; font-display: swap.",
      "search": "Starlight built-in (Pagefind) indexing all content",
      "image_handling": "astro:assets for optimization; copy only manifest-validated assets into /public/images/ via a validated copy step",
      "deploy_target": "Vercel (static build of dist/)",
      "node": "Node 18+ / npm",
      "build_verification": "Parse built HTML/MD for image references and fail the build if any referenced path is missing from dist/."
    },
    "layer_discipline_check": {
      "avoided_terms_in_page_content": 0,
      "krebs_or_consciousness_as_public_claim": false,
      "internal_color_labels_in_page_text": false,
      "note": "Page content surfaces visible effects only; internal color names and backstage methodology never appear in nav labels, page bodies, or UI strings."
    },
    "build_ready": true,
    "build_ready_notes": [
      "Specification only — no site is built by this spoke; the spec is complete and consistent enough to scaffold and build.",
      "All 20 referenced assets exist in asset-manifest.json; zero hallucinated paths.",
      "Theme is editorial (matte, signal-rich), not glossy, per the spoke requirement.",
      "Logo pages use only the canonical user-provided marks; generated seal/poster art is never presented as a mark.",
      "Copy placeholders in landing-page-copy and proof sections (testimonials, client logos, media mentions) remain placeholders until verified; the wiki should render them as explicit placeholders, not invent content.",
      "Licensed display/body webfonts (Tyros Pro, SubjectivitySerif) must be present in the build environment for production parity; Fira Code is open source."
    ],
    "validation": {
      "spec_complete": true,
      "all_referenced_assets_in_manifest": true,
      "all_paths_exist": true,
      "missing_paths": [],
      "hallucinated_paths": 0,
      "broken_references_expected": 0
    }
  }
}
```

## Output Requirements

Write your output as valid JSON to:
`/Volumes/madara/2026/Projects/thoughtseed/brandmint-v2/brands/thoughtseed/.brandmint/outputs/icon-system.json`

The output must include:
- `skill`: "icon-system"
- `cluster`: "illustration"
- `timestamp`: ISO 8601 timestamp
- `status`: "complete" or "partial"
- `data`: skill-specific output data
