---
name: campaign-orchestrator
description: "Orchestrate the full campaign workflow phase-by-phase, ensuring each skill runs in sequence with proper handoffs and validation gates. Ported from brandmint-oracle-aleph and adapted for service-based B2B studios."
cluster: brandmint-synthesis
wave: 7
dependencies:
  - all-upstream
triggers:
  - "campaign orchestration"
  - "full campaign workflow"
  - "multi-phase campaign"
---

# Campaign Orchestrator

Coordinate all skill outputs into a structured, sequenced campaign from market understanding to continual interest.

## When to Use

Use this when launching or running a full campaign that requires coordinated execution across multiple skill outputs.

## Inputs (Required Upstream Outputs)

- `buyer-persona.json` — audience foundation
- `competitor-analysis.json` — market positioning
- `messaging-framework.json` — key messages
- `voice-and-tone.json` — vocabulary discipline
- `landing-page-copy.json` — homepage copy
- `email-sequence outputs` — lifecycle emails
- `ad-creative-copy.json` — ad variants
- `social-media-assets.json` — platform assets

## Global Conventions

- All outputs must include the canonical JSON schema with `skill`, `cluster`, `wave`, `timestamp`, `status`, `data` fields
- Output paths follow `.brandmint/outputs/{skill}.json` convention
- The `templates/` directories in oracle-aleph are NOT used — meristem is JSON-only

### Market region → GTM tag (additive)

Read `market.region` from `brand-config.yaml` (or equivalent execution context):

| `market.region` | GTM tag | Effects |
|-----------------|---------|---------|
| `FR` | `FR GTM` | Force bilingual FR+EN content/synthesis; `defaultLocale: fr`; require FR competitor set + Marie Durand depth; load `brands/iverif/research/channel-plan.md` when brand is iverif |
| other / unset | (none) | Existing single-locale behaviour |

Emit on orchestrator output:

```json
"gtm": {
  "region": "FR",
  "tag": "FR GTM",
  "locales": ["fr", "en"],
  "defaultLocale": "fr",
  "channel_plan_path": "brands/iverif/research/channel-plan.md"
}
```

Other brands without FR region omit `gtm` or set `tag` null.
## Campaign Phases for Service Studios

### Phase 1: Foundation
1. **buyer-persona** — audience and pain points
2. **competitor-analysis** — market gaps
3. **voice-and-tone** — vocabulary and prohibited terms

### Phase 2: Strategy
4. **messaging-framework** — key messages, value pillars
5. **product-positioning** — differentiators, observable outcome
6. **brand-story** — narrative thread

### Phase 3: Identity + Visual Language
7. **color-palette** — palette + treatment rules
8. **typography** — typefaces + hierarchy
9. **logo-concept** — logo system + usage
10. **visual-language** — visual principles, photography, illustration

### Phase 4: Photography
11. **hero-images** — homepage hero
12. **lifestyle-photography** — about-page lifestyle
13. **product-photography** — services-page artifacts
14. **social-media-assets** — platform-formatted assets

### Phase 5: Illustration
15. **brand-illustrations** — diagrams
16. **icon-system** — service-module icons
17. **pattern-library** — background patterns

### Phase 6: Content + Social Growth
18. **landing-page-copy** — homepage
19. **email-sequences** — welcome/prelaunch/launch
20. **ad-creative-copy** — ad variants
21. **press-release** — press kit announcement
22. **product-description** — services descriptions
23. **social-content-engine** — 30-day calendar (NEW)
24. **short-form-hook-generator** — viral hooks (NEW)
25. **update-strategy-sequencer** — campaign updates (NEW)
26. **community-manager-brain** — engagement plan (NEW)
27. **review-response-strategist** — testimonial playbook (NEW)

### Phase 7: Synthesis
28. **brand-documentation** — three separated docs
29. **notebooklm-publishing** — NotebookLM sources
30. **wiki-site-generator** — wiki navigation
31. **deliverables-package** — final package
32. **visual-content-bridge** — copy↔visual mapping (NEW)
33. **campaign-orchestrator** — this skill — final coordination

## Validation Gates

Per phase:
- Phase 1: persona has ≥5 challenges, competitor has ≥3 competitors
- Phase 2: voice matrix defined, prohibited terms listed, messaging has value pillars
- Phase 3: palette + typography + visual-language complete, all paths exist
- Phase 4: hero/lifestyle/product/social-media assets exist
- Phase 5: illustrations + icons + patterns complete
- Phase 6: all copy outputs complete, voice-discipline check PASS, social-growth spokes complete
- Phase 7: documentation + notebooklm + wiki + deliverables complete

## Output Schema

```json
{
    "skill": "campaign-orchestrator",
    "cluster": "synthesis",
    "wave": 7,
    "timestamp": "ISO 8601",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "campaign_id": "string",
        "phases": [
            {
                "phase": "number",
                "name": "string",
                "skills": [
                    {"skill": "string", "status": "PASS|FAIL|PARTIAL", "output_path": "string"}
                ]
            }
        ],
        "validation_gates": [
            {"gate": "string", "requirement": "string", "status": "PASS|FAIL"}
        ],
        "missing_outputs": ["string"],
        "ready_for_launch": "boolean",
        "gtm": {
            "region": "string|null",
            "tag": "FR GTM|null",
            "locales": ["fr", "en"],
            "defaultLocale": "fr",
            "channel_plan_path": "string|null"
        }
    }
}
```

## Quality Checklist

- [ ] All 33+ skills accounted for in phases
- [ ] Validation gates run for each phase
- [ ] Missing outputs flagged
- [ ] ready_for_launch boolean accurate
- [ ] Output paths verified to exist
- [ ] If `market.region=FR`: `gtm.tag` is `FR GTM` and bilingual gates acknowledged