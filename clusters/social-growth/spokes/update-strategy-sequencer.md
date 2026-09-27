---
name: update-strategy-sequencer
description: "Generate campaign-update sequences — announcement emails, progress notes, milestone communications. Ported from brandmint-oracle-aleph and adapted for service studios."
cluster: brandmint-social-growth
wave: 6
dependencies:
  - voice-and-tone
  - messaging-framework
  - landing-page-copy
triggers:
  - "campaign update"
  - "announcement"
  - "milestone communication"
  - "progress update"
---

# Update Strategy Sequencer

Generate campaign-update sequences that announce milestones, progress, and changes during an active campaign.

## Process

### Step 1: Identify Update Type

| Update Type | When | Voice |
|-------------|------|-------|
| Kickoff | Day 0 | Calm confidence, state what begins |
| Mid-engagement | Day 7-14 | Steady, exact, point to next step |
| Milestone reached | When relevant | Reflective, evidence-led |
| Handoff announcement | At end | Quietly proud, peer to the founder |

### Step 2: Channel Selection

For each update, decide channels:
- Email (welcome/launch sequences)
- LinkedIn post (long-form, professional audience)
- X/Twitter (short announcement, thread)
- Instagram (visual milestone)

### Step 3: Voice Calibration

Per `voice-and-tone.json` tone_variations:
- **announcement**: Calm confidence over celebration. State what shipped, what it does, then stop.
- **support**: Steady and exact. Acknowledge the situation plainly and point to the next concrete step.

### Step 4: Sequence Construction

For each update:
- Subject line (email) or hook (social)
- Body
- CTA (if applicable)
- Channel(s)

## Output Schema

```json
{
    "skill": "update-strategy-sequencer",
    "cluster": "social-growth",
    "wave": 6,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "update_types": [
            {"type": "string", "when": "string", "voice": "string", "frequency": "string"}
        ],
        "sequences": [
            {
                "id": "string",
                "update_type": "string",
                "subject_lines": ["string"],
                "body": "string",
                "channels": ["string"],
                "cta": "string",
                "scheduled_for": "string"
            }
        ],
        "voice_compliance": "PASS",
        "calendar": [
            {"date": "ISO date", "sequence_id": "string", "channels": ["string"]}
        ]
    }
}
```

## Quality Checklist

- [ ] All update types have at least one example
- [ ] Sequences ground in delivery-loop vocabulary
- [ ] No prohibited terms
- [ ] Calendar dates are realistic and non-overlapping
- [ ] CTAs are restrained (Bring the requirement, scoped)