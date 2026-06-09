# Photography Cluster Specification

## Constitution

### Core Principles
1. **Brand-aligned** — All photos reflect visual language
2. **Purposeful** — Every image has a defined use case
3. **Consistent treatment** — Same color treatment across all
4. **Prompt-documented** — Full prompts saved with each image

### Quality Standards
- Lifestyle shots: authentic, diverse representation
- Product shots: clear, well-lit, on-brand background
- Hero images: text-safe zones defined

### Constraints
- GPT-Image-2 only
- Must reference visual_language.json
- Must reference color_palette.json

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| lifestyle-shots | Contextual photography | JSON + images |
| product-photography | Product-focused shots | JSON + images |
| hero-images | Large header images | JSON + images |

### Generated Assets

```
generated/
├── lifestyle-01.png
├── lifestyle-02.png
├── lifestyle-03.png
├── product-hero-01.png
├── product-detail-01.png
├── hero-homepage.png
└── hero-about.png
```

### Success Criteria
- [ ] 3-5 lifestyle shots generated
- [ ] 3-5 product shots generated
- [ ] 2-3 hero images generated
- [ ] All prompts documented
- [ ] Text-safe zones defined for heroes

## Plan

### Implementation Approach

1. **lifestyle-shots** (first)
   - Reference buyer persona for subjects
   - Apply photography direction
   - Generate 3-5 images

2. **product-photography** (parallel)
   - Use brand colors for backgrounds
   - Multiple angles/contexts
   - Generate 3-5 images

3. **hero-images** (last)
   - Combine lifestyle + product themes
   - Define text overlay zones
   - Generate 2-3 images

### Tracer Pattern
Run lifestyle-shots first — tests GPT-Image-2 pipeline and style.

## Tasks

### Pre-flight
- [ ] Verify Wave 3 outputs exist
- [ ] Load visual_language.json
- [ ] Load color_palette.json
- [ ] Load buyer_persona.json (for subjects)

### Execution
- [ ] Execute lifestyle-shots spoke
- [ ] Verify images generated
- [ ] Execute product-photography spoke
- [ ] Verify images generated
- [ ] Execute hero-images spoke
- [ ] Verify images generated

### Post-flight
- [ ] Add all images to asset manifest
- [ ] Verify prompts documented
- [ ] Update state.json
- [ ] Signal Wave 5 ready
