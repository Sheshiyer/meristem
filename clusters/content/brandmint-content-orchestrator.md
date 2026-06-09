---
name: brandmint-content-orchestrator
description: "Route content creation tasks to the right spoke — landing page copy, email sequences, ad creative, press release, product descriptions. USE WHEN creating marketing content, writing copy, drafting emails, or producing ad variations."
cluster: brandmint-content
wave: 6
version: 1.0.0
---

# Brandmint Content Orchestrator

The entry skill for Wave 6: Content. Routes content creation intents to the appropriate spoke.

## Prerequisites

All prior waves must be complete:
- Wave 1: Foundation (buyer-persona, value-proposition)
- Wave 2: Strategy (voice-and-tone, product-positioning, messaging-framework)
- Wave 3-5: Visual identity (for image references)

## Cluster Map (Routing Targets)

- `brandmint-content-core` — shared reference: copy frameworks, quality gates, word counts
- `landing-page-copy` — hero section, features, benefits, CTAs, social proof structure
- `prelaunch-email-sequence` — pre-campaign nurture emails (3-5 emails)
- `launch-email-sequence` — campaign launch emails (5-7 emails)
- `welcome-email-sequence` — post-purchase onboarding (3-5 emails)
- `ad-creative-copy` — pre-campaign and live campaign ad variations
- `press-release` — media-ready announcement copy
- `product-description` — concise product copy for listings

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "landing page", "homepage", "sales page" | `landing-page-copy` |
| "prelaunch emails", "pre-campaign", "build anticipation" | `prelaunch-email-sequence` |
| "launch emails", "campaign emails", "crowdfunding emails" | `launch-email-sequence` |
| "welcome emails", "onboarding", "post-purchase" | `welcome-email-sequence` |
| "ads", "ad copy", "Facebook ads", "paid media" | `ad-creative-copy` |
| "press release", "media announcement", "PR" | `press-release` |
| "product description", "listing copy", "Amazon copy" | `product-description` |
| "full content suite" | Run all spokes in order |

## Execution Order

Content spokes have dependencies on strategy outputs but are largely parallelizable:

```
          ┌─► landing-page-copy
          │
          ├─► prelaunch-email-sequence
          │
voice ────┼─► launch-email-sequence
 and      │
tone      ├─► welcome-email-sequence
          │
          ├─► ad-creative-copy
          │
          └─► press-release
```

Exception: `product-description` is a dependency for `landing-page-copy` (hero section references it).

Recommended order:
1. `product-description` (standalone)
2. `landing-page-copy` (references product-description)
3. Parallel: `prelaunch-email-sequence`, `launch-email-sequence`, `welcome-email-sequence`
4. `ad-creative-copy` (can reference landing page headlines)
5. `press-release` (final synthesis)

## Quality Gates

From `brandmint-content-core`:
- All copy must use voice-and-tone prompt template
- Headlines must be 8-14 words
- Feature descriptions must be 42 words or less
- Email subject lines must be under 50 characters
- CTAs must be action-oriented verbs
- No generic superlatives without proof

## Loading Spokes On Demand

Spokes are not enumerated at startup. Load by reading:

`clusters/content/spokes/<spoke-name>.md`
