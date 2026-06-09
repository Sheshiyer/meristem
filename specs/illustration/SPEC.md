# Illustration Cluster Specification

## Constitution

### Core Principles
1. **Style consistency** — ALL illustrations same style
2. **Color compliance** — Only palette colors
3. **Grid alignment** — Icons on standard grid
4. **Seamless patterns** — Patterns must tile

### Quality Standards
- All illustrations match chosen style
- Icons: same stroke weight, corner style
- Patterns: verified seamless tiling

### Constraints
- GPT-Image-2 only
- Style locked before generation begins
- Must reference visual_language.json

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| brand-illustrations | Concept illustrations | JSON + images |
| icon-system | Iconography set | JSON + images |
| pattern-library | Repeating patterns | JSON + images |

### Generated Assets

```
generated/
├── illust-hero-01.png
├── illust-feature-01.png
├── icons/
│   ├── dashboard.png
│   ├── settings.png
│   └── ...
└── patterns/
    ├── geo-01.png
    └── geo-01-dark.png
```

### Success Criteria
- [ ] 3-5 brand illustrations generated
- [ ] 10-20 icons generated
- [ ] 2-3 patterns generated
- [ ] Style guide documented
- [ ] All same visual style

## Plan

### Implementation Approach

1. **Lock illustration style**
   - From visual_language.json
   - Define: stroke weight, corners, colors

2. **brand-illustrations** (first)
   - Apply locked style
   - Generate concept illustrations
   - Document prompts

3. **icon-system** (parallel)
   - Same style as illustrations
   - 24x24 grid
   - Generate core set

4. **pattern-library** (parallel)
   - Same color palette
   - Verify seamless
   - Generate variants

### Tracer Pattern
Run brand-illustrations first — validates style across large images.

## Tasks

### Pre-flight
- [ ] Verify Wave 4 outputs exist
- [ ] Load visual_language.json
- [ ] Load color_palette.json
- [ ] Lock illustration style

### Execution
- [ ] Execute brand-illustrations spoke
- [ ] Verify style consistency
- [ ] Execute icon-system spoke
- [ ] Verify grid alignment
- [ ] Execute pattern-library spoke
- [ ] Verify seamless tiling

### Post-flight
- [ ] Add all images to asset manifest
- [ ] Document style guide
- [ ] Update state.json
- [ ] Signal Wave 6 ready
