# Foundation Cluster Specification

## Constitution

### Core Principles
1. **Truth over aspiration** — Foundation outputs describe reality, not wishful thinking
2. **Buyer-first** — Every output serves understanding the customer
3. **Evidence-based** — Claims backed by research or explicit assumptions
4. **Actionable outputs** — Every output enables downstream decisions

### Quality Standards
- All personas must have pain points AND goals
- Competitor analysis must include weaknesses
- Value propositions must be testable

### Constraints
- No visual generation in this wave
- Outputs are JSON + prose, not images
- Must complete before Wave 2 can start

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| brand-foundation | Brand identity fundamentals | JSON |
| buyer-persona | Target customer profiles | JSON |
| competitor-analysis | Competitive landscape | JSON |
| value-proposition | Core value statements | JSON |

### Output Dependencies

```
brand-foundation ──┬──▶ buyer-persona
                   │
                   ├──▶ competitor-analysis
                   │
                   └──▶ value-proposition
```

### Success Criteria
- [ ] Brand foundation defines: category, market, problem, solution
- [ ] At least 1 primary + 1 secondary persona defined
- [ ] At least 2 direct competitors analyzed
- [ ] Value proposition follows "For X who Y, we are Z" format

## Plan

### Implementation Approach

1. **brand-foundation** (first)
   - Extract from brand-config.yaml
   - Validate completeness
   - Generate brand attributes

2. **buyer-persona** (depends on foundation)
   - Use audience section from config
   - Expand with psychographics
   - Define jobs-to-be-done

3. **competitor-analysis** (depends on foundation)
   - Use competitors section from config
   - Analyze positioning
   - Identify whitespace

4. **value-proposition** (depends on all above)
   - Synthesize unique position
   - Generate positioning statement
   - Create elevator pitches

### Tracer Pattern
Run brand-foundation first as tracer to validate config completeness.

## Tasks

### Pre-flight
- [ ] Validate brand-config.yaml exists
- [ ] Check required fields present
- [ ] Create `.brandmint/outputs/` directory

### Execution
- [ ] Execute brand-foundation spoke
- [ ] Validate brand-foundation.json output
- [ ] Execute buyer-persona spoke
- [ ] Validate buyer-persona.json output
- [ ] Execute competitor-analysis spoke
- [ ] Validate competitor-analysis.json output
- [ ] Execute value-proposition spoke
- [ ] Validate value-proposition.json output

### Post-flight
- [ ] Update state.json with wave completion
- [ ] Log metrics to orchestrator vault
- [ ] Signal Wave 2 ready
