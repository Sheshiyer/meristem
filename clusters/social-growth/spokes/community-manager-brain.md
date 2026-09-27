---
name: community-manager-brain
description: "Generate community engagement plans for Thoughtseed's audience (founders, CTOs, design circles). Tiered response templates, voice discipline, and engagement tactics. Ported from brandmint-oracle-aleph."
cluster: brandmint-social-growth
wave: 6
dependencies:
  - voice-and-tone
  - buyer-persona
triggers:
  - "community engagement"
  - "Discord"
  - "Slack community"
  - "comment response"
  - "engagement plan"
---

# Community Manager Brain

Generate a community engagement strategy for Thoughtseed's audience.

## Audience Context

Thoughtseed's community (per `buyer-persona.json`):
- Founders, CTOs, innovation leads, product strategists
- Lean senior teams at funded startups through scaleups
- Skeptical of buzzwords, attracted to integrated thinking
- Reads founder memos and technical walkthroughs over marketing content

## Engagement Tiers

| Tier | Audience | Response Time | Voice | When |
|------|----------|---------------|-------|------|
| 1 | Founder inquiry | < 2 hours | Direct, founder-to-founder | DM with "Bring the requirement" or scoped conversation |
| 2 | Operator inquiry | < 8 hours | Technical, specific | Detailed explanation of delivery loop, ownership transfer |
| 3 | General follower | < 24 hours | Restrained, illustrative | Quote a delivery-loop principle, link to relevant content |
| 4 | Industry observer | < 48 hours | Editorial, grounded | Deeper essay-style response if appropriate |

## Response Templates

### Tier 1 — Founder inquiry

```
[Brief acknowledgment of what they brought]

The short version: one team carries framing, behavior, product, execution,
and handoff inside a single delivery loop. The people who frame the
requirement are the people who build it.

If the problem is too entangled to split across vendors, bring it here.
We study it, build the system, and hand it back in a form you can run.

[Link to /start or specific entry point]
```

### Tier 2 — Operator inquiry

```
[Specific technical acknowledgment]

Here's how the loop runs in your case:
- Requirement: [specific framing of their question]
- System: [specific design decision]
- Build: [specific engineering approach]
- Handoff: [specific deliverable]

[Detail or link to case study showing this approach]
```

### Tier 3 — General follower

```
[Restrained acknowledgment]

The loop is the studio. Four stages, one team, one handoff.
Here's [link to relevant content].
```

### Tier 4 — Industry observer

```
[Editorial, grounded response]

[Longer reflection if appropriate, drawing on delivery-loop principles]
[Link to relevant deeper content]
```

## Output Schema

```json
{
    "skill": "community-manager-brain",
    "cluster": "social-growth",
    "wave": 6,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "engagement_tiers": [
            {"tier": 1, "audience": "founder inquiry", "response_time": "< 2 hours", "voice": "direct", "template": "string"}
        ],
        "engagement_tactics": [
            {"tactic": "string", "purpose": "string", "frequency": "string"}
        ],
        "voice_discipline": "PASS — uses preferred vocabulary, no prohibited terms",
        "response_do": ["string"],
        "response_dont": ["string"]
    }
}
```

## Quality Checklist

- [ ] All 4 tiers defined
- [ ] Templates grounded in delivery-loop vocabulary
- [ ] Response times are realistic
- [ ] No prohibited terms
- [ ] Engagement tactics are sustainable (not burnout-inducing)