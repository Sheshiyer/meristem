# Strategy Cluster Specification

## Constitution

### Core Principles
1. **Actionable over abstract** — Every output tells you what to DO
2. **Consistent voice** — Voice matrix applies everywhere
3. **CBBE-grounded** — Positioning follows brand equity framework
4. **Story-driven** — Brand story uses StoryBrand structure

### Quality Standards
- Voice matrix must have all 5 dimensions
- Positioning must address all CBBE levels
- Messaging framework must have proof points
- Brand story must define stakes (failure state)

### Constraints
- Must use outputs from Wave 1
- No visual generation
- Voice decisions lock content tone for Wave 6

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| voice-and-tone | Voice calibration matrix | JSON |
| product-positioning | CBBE-based positioning | JSON |
| messaging-framework | Hierarchy of messages | JSON |
| brand-story | StoryBrand narrative | JSON |

### Output Dependencies

```
brand-foundation ──┬──▶ voice-and-tone ──────┐
                   │                         │
buyer-persona ─────┼──▶ messaging-framework ─┼──▶ (Wave 6)
                   │                         │
competitor-analysis┼──▶ product-positioning ─┤
                   │                         │
value-proposition ─┴──▶ brand-story ─────────┘
```

### Success Criteria
- [ ] Voice matrix: all 5 dimensions scored 0-1
- [ ] Positioning statement follows template
- [ ] 3-5 key message pillars with proof points
- [ ] Brand story has all 7 StoryBrand elements

## Plan

### Implementation Approach

1. **voice-and-tone** (first)
   - Analyze brand personality from config
   - Generate base voice matrix
   - Define context modifiers

2. **product-positioning** (parallel)
   - Apply CBBE framework
   - Define points of parity/difference
   - Generate positioning statement

3. **messaging-framework** (after voice)
   - Build on voice-and-tone
   - Create message hierarchy
   - Define audience variants

4. **brand-story** (last)
   - Apply StoryBrand framework
   - Connect to positioning
   - Define transformation arc

### Tracer Pattern
Run voice-and-tone first — it sets the tone for everything else.

## Tasks

### Pre-flight
- [ ] Verify Wave 1 outputs exist
- [ ] Load brand-foundation.json
- [ ] Load buyer-persona.json
- [ ] Load competitor-analysis.json
- [ ] Load value-proposition.json

### Execution
- [ ] Execute voice-and-tone spoke
- [ ] Validate voice matrix completeness
- [ ] Execute product-positioning spoke
- [ ] Validate CBBE coverage
- [ ] Execute messaging-framework spoke
- [ ] Validate proof points exist
- [ ] Execute brand-story spoke
- [ ] Validate StoryBrand elements

### Post-flight
- [ ] Update state.json
- [ ] Log metrics
- [ ] Signal Wave 3 ready
