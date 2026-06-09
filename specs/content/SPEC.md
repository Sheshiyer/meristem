# Content Cluster Specification

## Constitution

### Core Principles
1. **Voice-applied** — Every piece uses voice matrix
2. **Framework-driven** — Copy uses proven frameworks
3. **Channel-appropriate** — Character limits respected
4. **CTA-focused** — Every piece has clear next step

### Quality Standards
- Voice matrix applied with context modifiers
- Messaging framework pillars referenced
- Ad copy within platform limits
- SEO meta for all pages

### Constraints
- No image generation in this wave
- Must use outputs from Waves 1-2
- Ad copy must respect character limits

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| landing-page-copy | Website copy | JSON |
| email-sequences | Email campaigns | JSON |
| ad-copy | Platform-specific ads | JSON |
| social-media-content | Social posts | JSON |
| press-release | PR copy | JSON |
| case-study-template | Success story format | JSON |
| blog-outlines | Content calendar | JSON |

### Success Criteria
- [ ] Homepage copy complete (all sections)
- [ ] Welcome email sequence (5-7 emails)
- [ ] Ad copy for 2+ platforms
- [ ] Press release template
- [ ] Voice consistently applied

## Plan

### Implementation Approach

1. **landing-page-copy** (first)
   - Apply voice matrix
   - Use messaging framework
   - Follow standard page flow

2. **email-sequences** (parallel)
   - Welcome sequence
   - Nurture sequence
   - Apply email context modifiers

3. **ad-copy** (parallel)
   - Google Ads
   - LinkedIn Ads
   - Meta Ads (if configured)

4. **social-media-content** (parallel)
   - Platform-appropriate
   - Mix of content types

5. **press-release** (parallel)
   - Formal voice modifier
   - Standard PR format

6. **case-study-template** (parallel)
   - BAB framework
   - Results-focused

7. **blog-outlines** (parallel)
   - SEO-informed topics
   - Content calendar

### Tracer Pattern
Run landing-page-copy first — it's the core content other pieces reference.

## Tasks

### Pre-flight
- [ ] Verify Wave 2 outputs exist
- [ ] Load voice_and_tone.json
- [ ] Load messaging_framework.json
- [ ] Load brand_story.json
- [ ] Load buyer_persona.json

### Execution
- [ ] Execute landing-page-copy spoke
- [ ] Validate all sections present
- [ ] Execute email-sequences spoke
- [ ] Validate sequence completeness
- [ ] Execute ad-copy spoke
- [ ] Validate character limits
- [ ] Execute social-media-content spoke
- [ ] Execute press-release spoke
- [ ] Execute case-study-template spoke
- [ ] Execute blog-outlines spoke

### Post-flight
- [ ] Verify voice consistency
- [ ] Update state.json
- [ ] Signal Wave 7 ready
