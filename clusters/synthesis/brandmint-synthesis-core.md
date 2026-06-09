---
name: brandmint-synthesis-core
description: "Shared reference for the synthesis cluster: asset manifest system, 3-stage source pipeline, origin tracking, path validation rules, and the lessons learned from brandmint-oracle-aleph."
cluster: brandmint-synthesis
wave: 7
version: 2.0.0
---

# Brandmint Synthesis Core

Shared reference for all synthesis spokes. Contains the lessons learned from brandmint-oracle-aleph and the mandatory patterns for Wave 7.

## The One Rule Everything Turns On

**NEVER include a path that doesn't exist.** Every synthesis spoke must:

1. Load the asset manifest
2. Validate every path before use
3. Fail fast on hallucinated paths
4. Track asset origins (user-provided vs generated)

## Lessons Learned from brandmint-oracle-aleph

### Lesson 1: Auto-Generated Sources Break NotebookLM

**Problem:** Sources emitted from waves were auto-synthesized without curation:
- JSON → prose transformation was one-step
- No separation by document category
- User-provided assets not integrated
- Visual assets could be hallucinated

**Solution:** 3-stage source processing pipeline:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   TRANSFORM     │ ──▶ │     CURATE      │ ──▶ │    ASSEMBLE     │
│                 │     │                 │     │                 │
│ Skill outputs   │     │ Select by       │     │ Combine with    │
│ → categorized   │     │ artifact type   │     │ validated       │
│ prose           │     │ and priority    │     │ user assets     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Lesson 2: No Visual Hallucination

**Problem:** NotebookLM flow could include paths that don't exist:
- `generated/` directory scanned without validation
- Missing assets silently included
- No distinction between user-provided and AI-generated

**Solution:** Asset manifest as source of truth:

```json
{
  "validation": {
    "all_paths_exist": true,
    "required_assets_present": true,
    "missing_paths": []
  }
}
```

### Lesson 3: NVIDIA Embeddings Available But Underused

**Available architecture:**
- `services/design-memory-worker/` — Cloudflare Worker with NVIDIA NIM
- Indexes images, returns semantic matches
- Client in `brandmint/core/design_memory.py`

**Intended uses (not fully wired):**
1. Match visual assets to prose sources
2. Verify generated assets match brand
3. Reference image selection for generation

**Integration point:** Optional enhancement for source curation.

### Lesson 4: Document Type Separation

**Problem:** Single monolithic brand document.

**Solution:** Three separate documents:
| Document | Audience | Content |
|----------|----------|---------|
| Brand Identity | Designers | Logo, colors, typography |
| Product Positioning | Product/Sales | Value prop, features |
| Campaign Guidelines | Marketing | Voice, messaging, copy |

### Lesson 5: Deterministic vs AI-Generated

**Problem:** No clear tracking of what's user-provided vs generated.

**Solution:** Origin markers:
- `user_provided` — From user (logos, screenshots, product photos)
- `generated` — Created by AI during pipeline
- `deterministic: true` — Not AI-generated, always accurate

## Asset Manifest System

### Generation

```bash
# Generate manifest from all sources
bm generate-manifest --config brand-config.yaml
```

**Sources scanned:**
1. User-provided assets from `brand-config.yaml`
2. Generated assets from `generated/` directory
3. Skill outputs from `.brandmint/outputs/`

### Schema

```json
{
    "generated_at": "2024-01-15T10:30:00Z",
    "brand_name": "Brand Name",
    "brand_slug": "brand-name",
    "version": "1.0.0",
    
    "user_provided_assets": [
        {
            "id": "logo-primary",
            "path": "./assets/logo.png",
            "type": "logo",
            "exists": true,
            "deterministic": true,
            "required": true,
            "checksum": "sha256:abc123..."
        }
    ],
    
    "generated_assets": [
        {
            "id": "hero-image-v1",
            "path": "./generated/hero-v1.png",
            "type": "hero",
            "exists": true,
            "deterministic": false,
            "wave": 4,
            "skill": "hero-images",
            "model": "gpt-image-2"
        }
    ],
    
    "validation": {
        "all_paths_exist": true,
        "required_assets_present": true,
        "missing_paths": [],
        "warnings": []
    }
}
```

### Validation Rules

| Check | Action on Failure |
|-------|-------------------|
| Required user asset missing | **FAIL** |
| Optional user asset missing | WARN, skip |
| Generated asset missing | WARN, regenerate or skip |
| Path not in manifest | WARN, exclude |
| Hallucinated path | **FAIL** |

## 3-Stage Source Pipeline (NotebookLM)

### Stage 1: Transform

Convert skill outputs to categorized prose:

| Category | Source Skills | Target Use |
|----------|---------------|------------|
| brand-identity | brand-foundation, color-palette, typography, logo-concept | Brand overview |
| product-strategy | product-positioning, value-proposition, buyer-persona | Positioning |
| voice-messaging | voice-and-tone, messaging-framework, brand-story | Communication |
| campaign-content | landing-page-copy, email-sequences, ad-copy | Campaign |
| visual-catalog | visual-language, photography, illustration metadata | Visual |

### Stage 2: Curate

Select sources by target artifact:

| Artifact | Required Sources | Budget |
|----------|------------------|--------|
| mind-map | brand-identity, product-strategy | 10 |
| brand-slides | brand-identity, voice-messaging | 15 |
| audio-overview | ALL categories | 25 |
| brand-report | ALL categories | 50 |

### Stage 3: Assemble

Combine prose with validated assets:

```yaml
source_routing:
  brand-overview-artifacts:
    sources: [brand-identity/*, product-strategy/product-positioning.md]
    assets:
      - user_provided/logo-*
      - generated/brand-seal-*
      
  product-artifacts:
    sources: [product-strategy/*, product-description.md]
    assets:
      - user_provided/app-screenshot-*  # Deterministic
      - generated/product-photography-*
```

## User-Provided Assets Configuration

```yaml
# In brand-config.yaml
user_provided_assets:
  logo:
    path: ./assets/logo.png
    type: logo
    required: true
    
  app_screenshots:
    - path: ./assets/screenshot-home.png
      type: screenshot
      deterministic: true
    - path: ./assets/screenshot-dashboard.png
      type: screenshot
      deterministic: true
      
validation:
  require_user_assets: true
  warn_missing_optional: true
```

## Path Validation Function

Every spoke must use this pattern:

```python
def validate_asset_path(path: str, manifest: dict) -> ValidationResult:
    """
    Validate asset path exists and is in manifest.
    NEVER skip this check.
    """
    # 1. Check file exists on disk
    if not Path(path).exists():
        return ValidationResult(
            valid=False,
            error="Path does not exist",
            action="FAIL"
        )
    
    # 2. Check if in asset manifest
    asset = find_in_manifest(manifest, path)
    if not asset:
        return ValidationResult(
            valid=True,
            warning="Asset not in manifest",
            action="WARN"
        )
    
    # 3. Return with origin info
    return ValidationResult(
        valid=True,
        origin=asset.get('origin'),  # user_provided | generated
        deterministic=asset.get('deterministic', False)
    )
```

## Quality Gates

| Gate | Where Enforced | Failure Action |
|------|----------------|----------------|
| Manifest exists | All spokes | FAIL |
| All paths valid | All spokes | FAIL |
| No hallucinations | All spokes | FAIL |
| Origins tracked | deliverables | Required |
| Sources are prose | notebooklm | FAIL or fallback |
| Docs separated | brand-documentation | Required |
| Wiki builds | wiki-site | FAIL |
| Package verified | deliverables | FAIL |

## Error Recovery

| Error | Spoke | Recovery |
|-------|-------|----------|
| Missing required asset | ALL | Stop, report error |
| Missing optional asset | ALL | Warn, continue without |
| Synthesis fails | notebooklm | Fallback to mechanical |
| Build fails | wiki | Stop, show error |
| Checksum mismatch | deliverables | Stop, investigate |

## NVIDIA Embedding Integration (Optional)

```yaml
# Optional configuration
embedding_integration:
  enabled: true
  worker_url: "https://design-memory.workers.dev"
  
  use_cases:
    - match_assets_to_sources
    - verify_asset_relevance
```

If not configured, falls back to keyword matching.

## Version History

| Version | Changes |
|---------|---------|
| 2.0.0 | Added 3-stage pipeline, asset manifest, origin tracking |
| 1.0.0 | Initial version (from brandmint-oracle-aleph patterns) |
