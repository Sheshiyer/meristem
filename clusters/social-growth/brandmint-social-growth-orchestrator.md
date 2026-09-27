---
name: brandmint-social-growth-orchestrator
description: "Shared reference for the social-growth cluster: 30-day content calendar generation, viral hooks, community engagement, review responses, and campaign updates."
cluster: brandmint-social-growth
wave: 6
version: 1.0.0
---

# Brandmint Social Growth Orchestrator

The entry skill for the social-growth cluster. Routes social media workflow intents to the appropriate spoke.

## Cluster Map (Routing Targets)

- `brandmint-social-growth-core` — shared reference
- `social-content-engine` — 30-day content calendar
- `short-form-hook-generator` — viral hooks for TikTok/Reels/Shorts
- `community-manager-brain` — community engagement plans
- `review-response-strategist` — testimonial review responses
- `update-strategy-sequencer` — campaign update sequences

## Routing Rules by Intent

| Intent | Target Spoke |
|--------|--------------|
| "content calendar", "30-day plan", "weekly themes" | `social-content-engine` |
| "TikTok hooks", "Reels hooks", "Shorts", "viral hooks" | `short-form-hook-generator` |
| "community", "engagement plan", "Discord/Slack" | `community-manager-brain` |
| "review response", "testimonial reply", "customer feedback" | `review-response-strategist` |
| "update sequence", "campaign update", "announcement" | `update-strategy-sequencer` |
| "full social media suite" | Run all spokes in sequence |

## Service-Business Adaptation

This cluster was ported from `brandmint-oracle-aleph` and adapted for **service-based B2B studios**:

- ❌ **Skipped** (oracle-aleph originals): affiliate-program-designer, influencer-outreach-pro, niche-validator, brand-name-studio, competitive-ads-extractor
- ✓ **Adapted** (for service studio): all spokes now ground in the delivery-loop narrative (Requirement → System → Build → Handoff), not crowdfunding-stage mechanics
- ✓ **Voice discipline**: all outputs use `voice-and-tone.json` (voice_matrix + prohibited vocabulary)

## Execution Order

Recommended for a campaign:
1. `social-content-engine` — establishes 30-day calendar
2. `short-form-hook-generator` — derives hooks from calendar themes
3. `update-strategy-sequencer` — runs campaign updates
4. `community-manager-brain` — handles engagement
5. `review-response-strategist` — responds to testimonials

## Quality Gates

- All outputs use approved vocabulary from `voice-and-tone.json`
- No prohibited terms (conscious-aligned, disruptive, etc.)
- All content references the delivery loop or its vocabulary
- Calendar dates are realistic and non-overlapping