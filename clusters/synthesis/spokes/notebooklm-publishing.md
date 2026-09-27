---
name: notebooklm-publishing
description: "Publish brand outputs to NotebookLM — 3-stage source pipeline (transform, curate, assemble), asset manifest validation, artifact generation."
cluster: brandmint-synthesis
wave: 7
dependencies:
  - all-prior-waves
triggers:
  - "NotebookLM"
  - "notebook"
  - "mind map"
  - "audio overview"
  - "AI notebook"
---

# NotebookLM Publishing Skill

Upload brand outputs to Google NotebookLM using a validated 3-stage source pipeline.

## Critical Lesson: No Auto-Generated Sources

**NEVER auto-generate or hallucinate sources.** Every source must:
1. Be explicitly transformed from a real skill output
2. Have its path validated before upload
3. Be categorized by document type and target artifact

## Prerequisites

- All Wave 1-6 outputs complete in `.brandmint/outputs/`
- `OPENROUTER_API_KEY` environment variable (for prose synthesis)
- NotebookLM access (Google account)
- Asset manifest generated and validated

## 3-Stage Source Processing Pipeline

### Stage 1: TRANSFORM — Skill Outputs → Categorized Prose

Transform JSON outputs into narrative prose, organized by **document category**:

| Category | Source Skills | Target Use |
|----------|---------------|------------|
| **brand-identity** | brand-foundation, color-palette, typography, logo-concept | Brand overview artifacts |
| **product-strategy** | product-positioning, value-proposition, buyer-persona | Positioning artifacts |
| **voice-messaging** | voice-and-tone, messaging-framework, brand-story | Communication artifacts |
| **campaign-content** | landing-page-copy, email-sequences, ad-copy, press-release | Campaign artifacts |
| **visual-catalog** | visual-language, photography metadata, illustration metadata | Visual artifacts |

**Transformation approach:**
```
For each skill output:
1. Read JSON from .brandmint/outputs/{skill-id}.json
2. Verify JSON is valid and non-empty
3. Transform to prose using voice-and-tone output
4. Write to .brandmint/sources/{category}/{skill-id}.md
5. Record in source-manifest.json
```

### Bilingual sources (additive)

When `market.region: FR` or `locales` includes `fr`, write transformed prose under locale trees:

```
.brandmint/sources/en/{category}/{skill-id}.md
.brandmint/sources/fr/{category}/{skill-id}.md
```

Also accept brand-local publish mirrors such as `brands/{slug}/publish/notebooklm/sources/{en,fr}/` when the brand uses that layout. Single-locale brands keep the existing `.brandmint/sources/{category}/` paths unchanged.

Prefer FR prose as primary when `defaultLocale: fr`. Record locale on each `source-manifest.json` entry (`locale: en|fr`).
**Prose synthesis (if OPENROUTER_API_KEY set):**
- Use LLM to transform JSON → narrative
- Write *as* the brand using voice-and-tone
- Include all key information in readable format

**Mechanical fallback (if no key):**
- JSON → formatted markdown
- Less effective but functional

### Stage 2: CURATE — Select Sources by Target Artifact

Select sources based on what artifact you're generating:

| Artifact Type | Required Sources | Optional Sources |
|---------------|------------------|------------------|
| **mind-map** | brand-identity, product-strategy | voice-messaging |
| **brand-slides** | brand-identity, voice-messaging | visual-catalog |
| **campaign-slides** | campaign-content, voice-messaging | product-strategy |
| **audio-overview** | brand-identity, product-strategy, voice-messaging | campaign-content |
| **brand-report** | ALL categories | - |

**Curation rules:**
```yaml
source_budget: 50  # NotebookLM Standard limit
priority_order:
  - user-provided (always include)
  - brand-identity (core)
  - product-strategy (core)
  - voice-messaging (high value)
  - campaign-content (if relevant)
  - visual-catalog (last)
```

### Stage 3: ASSEMBLE — Combine with Validated Assets

**Asset Manifest Structure:**
```json
{
  "generated_at": "ISO-8601",
  "assets": {
    "user_provided": [
      {
        "id": "logo-primary",
        "path": "./assets/logo.png",
        "type": "logo",
        "exists": true,
        "include_in_notebooklm": true
      },
      {
        "id": "app-screenshot-1",
        "path": "./assets/screenshot-home.png",
        "type": "screenshot",
        "exists": true,
        "deterministic": true
      }
    ],
    "generated": [
      {
        "id": "hero-image-v1",
        "path": "./generated/hero-image-v1.png",
        "type": "hero",
        "exists": true,
        "wave": 4,
        "skill": "hero-images"
      }
    ]
  },
  "validation": {
    "all_paths_exist": true,
    "missing_paths": [],
    "total_assets": 15
  }
}
```

**Assembly rules:**
1. **ALWAYS** validate every path exists before upload
2. **User-provided assets** get highest priority
3. **Deterministic assets** (screenshots, logos) always included
4. **Generated assets** selected by relevance and quality
5. **NEVER** include paths that don't exist on disk

## Source-to-Artifact Routing

```yaml
artifact_routing:
  brand-overview-artifacts:
    sources:
      - brand-identity/*
      - product-strategy/product-positioning.md
      - voice-messaging/voice-and-tone.md
    assets:
      - user_provided/logo-*
      - generated/brand-seal-*
      - generated/bento-grid-*
    
  campaign-artifacts:
    sources:
      - campaign-content/*
      - voice-messaging/messaging-framework.md
    assets:
      - generated/hero-images-*
      - generated/social-*
      
  product-artifacts:
    sources:
      - product-strategy/*
      - campaign-content/product-description.md
    assets:
      - user_provided/app-screenshot-*  # Deterministic, user-provided
      - user_provided/product-photo-*
      - generated/product-photography-*
```

## User-Provided Assets Configuration

In `brand-config.yaml`:

```yaml
user_provided_assets:
  logo:
    path: ./assets/logo.png
    type: logo
    include_in_notebooklm: true
    required: true  # Fail if missing
    
  app_screenshots:
    - path: ./assets/screenshot-home.png
      type: screenshot
      deterministic: true  # Not AI-generated
    - path: ./assets/screenshot-dashboard.png
      type: screenshot
      deterministic: true
      
  product_photos:
    - path: ./assets/product-front.jpg
      type: product
      include_in_notebooklm: true

# Validation at launch
validation:
  require_user_assets: true  # Fail if any required asset missing
  warn_missing_optional: true
```

## Process

### Step 1: Validate Asset Manifest

```bash
# Generate and validate asset manifest
bm validate-assets --config brand-config.yaml

# Output: .brandmint/asset-manifest.json
# Must pass before proceeding
```

**Validation checks:**
- [ ] All user-provided asset paths exist
- [ ] All generated asset paths exist
- [ ] No duplicate asset IDs
- [ ] Required assets present

### Step 2: Transform Sources (Stage 1)

```bash
# Transform skill outputs to categorized prose
bm transform-sources --config brand-config.yaml

# Output: .brandmint/sources/{category}/*.md
# Output: .brandmint/source-manifest.json
```

### Step 3: Curate Sources (Stage 2)

```bash
# Select sources for target artifact focus
bm curate-sources --config brand-config.yaml --focus brand-overview

# Output: .brandmint/curated-sources.json
```

### Step 4: Assemble Upload (Stage 3)

```bash
# Assemble final upload set with validated assets
bm assemble-upload --config brand-config.yaml

# Output: .brandmint/upload-manifest.json
# Contains: prose docs + validated asset paths
```

### Step 5: Upload to NotebookLM

```bash
# Upload to NotebookLM (only validated sources)
bm notebooklm-upload --config brand-config.yaml

# Creates notebook, uploads sources, waits for indexing
```

### Step 6: Generate Artifacts

```bash
# Generate artifacts
bm notebooklm-artifacts --config brand-config.yaml

# Generates: mind-map, slides, report, audio
```

### Step 7: Download Artifacts

```bash
# Download all generated artifacts
bm notebooklm-download --config brand-config.yaml

# Output: deliverables/notebooklm/
```

## Output Schema

```json
{
    "skill": "notebooklm-publishing",
    "cluster": "synthesis",
    "wave": 7,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "2.0.0",
    "data": {
        "pipeline": {
            "transform": {
                "categories_processed": ["brand-identity", "product-strategy", "..."],
                "sources_generated": 12,
                "synthesis_model": "anthropic/claude-3.5-haiku",
                "fallback_used": false
            },
            "curate": {
                "focus": "brand-overview",
                "sources_selected": 8,
                "sources_excluded": 4,
                "budget_used": 8,
                "budget_total": 50
            },
            "assemble": {
                "prose_docs": 8,
                "user_provided_assets": 3,
                "generated_assets": 5,
                "all_paths_validated": true
            }
        },
        "notebook": {
            "id": "string",
            "name": "string",
            "url": "string",
            "created_at": "string"
        },
        "sources_uploaded": {
            "prose_documents": [
                {
                    "name": "string",
                    "category": "brand-identity|product-strategy|...",
                    "source_skill": "string",
                    "word_count": 0,
                    "path_validated": true,
                    "indexed": true
                }
            ],
            "assets": [
                {
                    "id": "string",
                    "type": "logo|screenshot|hero|...",
                    "origin": "user_provided|generated",
                    "deterministic": true,
                    "path_validated": true,
                    "indexed": true
                }
            ]
        },
        "artifacts_generated": {
            "mind_map": {
                "generated": true,
                "path": "deliverables/notebooklm/mind-map.png"
            },
            "slides": {
                "generated": true,
                "path": "deliverables/notebooklm/slides.pdf"
            },
            "report": {
                "generated": true,
                "path": "deliverables/notebooklm/brand-report.pdf"
            },
            "audio": {
                "generated": true,
                "path": "deliverables/notebooklm/audio-overview.mp3",
                "duration": "8:32"
            }
        },
        "validation": {
            "all_paths_exist": true,
            "missing_paths": [],
            "hallucinated_paths": 0
        }
    }
}
```

## Quality Checklist

### Pipeline Validation
- [ ] Asset manifest generated and validated
- [ ] ALL paths verified to exist before upload
- [ ] Zero hallucinated/non-existent paths
- [ ] User-provided assets included (if configured)
- [ ] Deterministic assets marked correctly

### Source Processing
- [ ] Transform: All skill outputs processed
- [ ] Transform: Prose written as the brand voice
- [ ] Curate: Sources selected by artifact focus
- [ ] Curate: Budget not exceeded (max 50)
- [ ] Assemble: Final manifest validated
- [ ] If bilingual/FR: sources emitted under `sources/{en,fr}/` (or `.brandmint/sources/{en,fr}/...`)
### NotebookLM
- [ ] Notebook created successfully
- [ ] All sources uploaded
- [ ] All sources indexed
- [ ] Artifacts generated
- [ ] Artifacts downloaded

## Error Handling

```yaml
errors:
  missing_required_asset:
    action: FAIL
    message: "Required user-provided asset not found: {path}"
    
  missing_optional_asset:
    action: WARN
    message: "Optional asset not found, excluding: {path}"
    
  hallucinated_path:
    action: FAIL
    message: "Path does not exist, cannot upload: {path}"
    
  synthesis_failed:
    action: FALLBACK
    message: "Prose synthesis failed, using mechanical rendering"
    
  budget_exceeded:
    action: TRUNCATE
    message: "Source budget exceeded, excluding lowest priority sources"
```

## NVIDIA Embedding Integration (Optional)

If `DESIGN_MEMORY_WORKER_URL` is configured:

```yaml
embedding_integration:
  enabled: true
  worker_url: "https://design-memory.your-domain.workers.dev"
  
  use_cases:
    - match_assets_to_sources:
        description: "Find best visual assets for each prose source"
        query: "brand identity visual representation"
        
    - verify_asset_relevance:
        description: "Verify generated assets match brand"
        threshold: 0.7
```

This is **optional enhancement** — the pipeline works without it using keyword matching.
