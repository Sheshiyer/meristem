# Identity Cluster Specification

## Constitution

### Core Principles
1. **Systematic** — Every element has rationale, rules, and restrictions
2. **Consistent** — All visuals share the same design language
3. **Accessible** — Color combinations meet WCAG AA
4. **Generative** — All images via GPT-Image-2 only

### Quality Standards
- Logo concepts: minimum 2 options
- Colors: all pairs checked for contrast
- Typography: display + body fonts defined
- Visual language: photo + illustration direction set

### Constraints
- GPT-Image-2 only (no FAL, Replicate, Midjourney)
- Must reference color preferences from config
- Typography must use web-safe or Google Fonts

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| logo-concept | Logo design concepts | JSON + images |
| color-palette | Brand color system | JSON + swatch image |
| typography | Type system | JSON + specimen image |
| visual-language | Photo/illustration direction | JSON + moodboard |

### Generated Assets

```
generated/
├── logo-concept-1.png
├── logo-concept-2.png
├── color-swatches.png
├── type-specimen.png
└── moodboard.png
```

### Success Criteria
- [ ] 2+ logo concepts generated
- [ ] Primary + secondary + accent colors defined
- [ ] Display + body typography defined
- [ ] Photography direction documented
- [ ] Illustration direction documented

## Plan

### Implementation Approach

1. **color-palette** (first)
   - Reference visual preferences in config
   - Generate systematic palette
   - Check accessibility
   - Generate swatch image

2. **typography** (parallel)
   - Select font pairing
   - Define type scale
   - Generate specimen

3. **logo-concept** (after colors)
   - Use color palette
   - Generate 2+ concepts
   - Document rationale

4. **visual-language** (last)
   - Synthesize all identity decisions
   - Define photo direction
   - Define illustration direction
   - Generate moodboard

### Tracer Pattern
Run color-palette first — all other elements depend on it.

## Tasks

### Pre-flight
- [ ] Verify Wave 2 outputs exist
- [ ] Load visual_preferences from config
- [ ] Check GPT-Image-2 availability

### Execution
- [ ] Execute color-palette spoke
- [ ] Generate color-swatches.png
- [ ] Execute typography spoke
- [ ] Generate type-specimen.png
- [ ] Execute logo-concept spoke
- [ ] Generate logo concepts (2+)
- [ ] Execute visual-language spoke
- [ ] Generate moodboard.png

### Post-flight
- [ ] Verify all images generated
- [ ] Add to asset manifest
- [ ] Update state.json
- [ ] Signal Wave 4 ready
