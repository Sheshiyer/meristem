# Synthesis Cluster Specification

## Constitution

### Core Principles
1. **No hallucinated paths** — Every path validated before use
2. **Origin tracking** — User-provided vs generated marked
3. **3-stage pipeline** — Transform → Curate → Assemble
4. **Build verification** — Wiki must compile

### Quality Standards
- Asset manifest exists and validates
- All paths verified before inclusion
- Sources are prose (not raw JSON)
- Deliverables package is complete

### Constraints
- MUST generate asset manifest first
- MUST validate all paths exist
- NotebookLM requires OPENROUTER_API_KEY for synthesis
- Wiki requires npm build to pass

## Specify

### What This Cluster Produces

| Spoke | Output | Format |
|-------|--------|--------|
| notebooklm-publishing | AI notebook artifacts | JSON + downloaded files |
| brand-documentation | Structured brand docs | Markdown + PDF |
| wiki-site-generator | Astro documentation site | Built site |
| deliverables-package | Final package | ZIP + manifest |

### Success Criteria
- [ ] Asset manifest generated and valid
- [ ] NotebookLM artifacts downloaded
- [ ] Brand documentation in 3 categories
- [ ] Wiki site builds without errors
- [ ] Deliverables package complete with origins

## Plan

### Implementation Approach

1. **Generate Asset Manifest** (PRE-REQUISITE)
   - Scan user_provided_assets from config
   - Scan generated/ directory
   - Validate all paths exist
   - FAIL if any missing

2. **notebooklm-publishing** (first)
   - Transform: skill outputs → prose
   - Curate: select by artifact type
   - Assemble: combine with validated assets
   - Upload and generate artifacts

3. **brand-documentation** (parallel)
   - Brand Identity document
   - Product Positioning document
   - Campaign Guidelines document

4. **wiki-site-generator** (after docs)
   - Convert markdown to Astro
   - Copy validated assets
   - Build and verify

5. **deliverables-package** (last)
   - Collect all artifacts
   - Generate checksums
   - Create ASSET-ORIGINS.md
   - Package as ZIP

### Tracer Pattern
Asset manifest generation is the tracer — if it fails, synthesis cannot proceed.

## Tasks

### Pre-flight
- [ ] Verify Waves 1-6 complete
- [ ] Check user_provided_assets in config
- [ ] Check OPENROUTER_API_KEY (optional)

### Asset Manifest (MANDATORY)
- [ ] Generate .brandmint/asset-manifest.json
- [ ] Validate all user_provided paths exist
- [ ] Validate all generated paths exist
- [ ] FAIL if any missing required assets

### Execution
- [ ] Execute notebooklm-publishing spoke
  - [ ] Transform skill outputs to prose
  - [ ] Curate sources by artifact
  - [ ] Upload to NotebookLM
  - [ ] Download artifacts
- [ ] Execute brand-documentation spoke
  - [ ] Generate brand-identity.md
  - [ ] Generate product-positioning.md
  - [ ] Generate campaign-guidelines.md
- [ ] Execute wiki-site-generator spoke
  - [ ] Process markdown files
  - [ ] Copy validated assets
  - [ ] Run npm build
  - [ ] Verify no errors
- [ ] Execute deliverables-package spoke
  - [ ] Collect all artifacts
  - [ ] Generate checksums
  - [ ] Create ASSET-ORIGINS.md
  - [ ] Create ZIP package

### Post-flight
- [ ] Verify deliverables complete
- [ ] Update state.json with completion
- [ ] Log final metrics
- [ ] Report success

## Error Recovery

| Error | Action |
|-------|--------|
| Missing required asset | FAIL, report which |
| Missing optional asset | WARN, continue |
| NotebookLM synthesis fails | Fallback to mechanical |
| Wiki build fails | FAIL, show error |
| Package verification fails | FAIL, investigate |
