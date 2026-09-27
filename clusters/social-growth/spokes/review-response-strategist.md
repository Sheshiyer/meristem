---
name: review-response-strategist
description: "Generate review-response playbooks for testimonial replies across platforms (G2, Capterra, LinkedIn recommendations, design circles). Ported from brandmint-oracle-aleph and adapted for service studios."
cluster: brandmint-social-growth
wave: 6
dependencies:
  - voice-and-tone
  - buyer-persona
triggers:
  - "review response"
  - "testimonial reply"
  - "customer feedback response"
---

# Review Response Strategist

Generate a playbook for responding to founder/operator testimonials and reviews across platforms.

## Review Tone Principles

Per `voice-and-tone.json`:
- **Steady and exact** — Acknowledge the situation plainly
- **Point to the next concrete step** — not celebration theater
- **Evidence close to the claim** — never inflate
- **Maintain calm confidence** — not loud luxury
- **Short declarative sentences** — peer to the founder

## Response Patterns

### Pattern 1: Specific Outcome Acknowledged

```
Thank you for the observation.

The point you raise — [specific outcome] — is exactly what the
delivery loop is shaped to produce. One team carries the requirement
from framing to handoff so the system ships coherent.

If you want to talk specifics about your situation, we're here.
[Link or contact]
```

### Pattern 2: Concern Raised

```
That concern is fair. [Acknowledge specifically]

In practice, [specific evidence or method that addresses it].

[Specific next step if applicable]
```

### Pattern 3: Praise + Use Case

```
Thank you. [Specific element of the observation].

The work you saw was the loop running as designed. If your situation
has a similar shape, the same loop applies.
```

### Pattern 4: Disagreement / Critical

```
We hear you. [Specific acknowledgment].

Where we differ: [honest, restrained explanation of approach].

The studio is not for every engagement. If the problem is too entangled
to split, we study it; if it needs a different shape, we say so.
```

## Output Schema

```json
{
    "skill": "review-response-strategist",
    "cluster": "social-growth",
    "wave": 6,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "tone_principles": ["string"],
        "response_patterns": [
            {
                "pattern_name": "string",
                "trigger": "string",
                "template": "string",
                "example_response": "string"
            }
        ],
        "platform_specific": [
            {"platform": "string", "response_length": "string", "tone_adjustment": "string"}
        ],
        "do": ["string"],
        "dont": ["string"],
        "voice_compliance": "PASS"
    }
}
```

## Quality Checklist

- [ ] All 4 response patterns defined
- [ ] Templates grounded in delivery-loop vocabulary
- [ ] No prohibited terms
- [ ] No superlatives or celebration theater
- [ ] Platform-specific adjustments documented