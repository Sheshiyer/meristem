---
name: brandmint-synthesis-orchestrator
description: "Route synthesis and publishing tasks to the right spoke — NotebookLM publishing, brand documentation, wiki site generation. Asset manifest validation required. USE WHEN packaging deliverables, creating documentation, or publishing brand assets."
cluster: brandmint-synthesis
wave: 7
version: 2.0.0
---

# Brandmint Synthesis Orchestrator

The entry skill for Wave 7: Synthesis. Routes publishing and documentation intents to the appropriate spoke.

## Critical Principle: Asset Manifest is Mandatory

**Before ANY synthesis spoke runs, the asset manifest MUST be generated and validated.**

```bash
# REQUIRED: Generate and validate asset manifest first
bm generate-manifest --config brand-config.yaml
bm validate-manifest --config brand-config.yaml
```

The asset manifest ensures:
- NO hallucinated paths (every path verified to exist)
- Clear distinction: user-provided vs generated assets
- Deterministic assets identified (screenshots, logos from user)
- Required assets present before packaging

## Prerequisites

1. All prior waves (1-6) must be complete
2. `.brandmint/outputs/` contains all skill outputs
3. `.brandmint/asset-manifest.json` generated and valid
4. User-provided assets (if any) configured and present

## Cluster Map (Routing Targets)

| Spoke | Purpose | Key Lesson Applied |
|-------|---------|-------------------|
| `brandmint-synthesis-core` | Shared reference: output formats, quality gates | - |
| `notebooklm-publishing` | Upload to NotebookLM, generate artifacts | 3-stage source pipeline, path validation |
| `brand-documentation` | Comprehensive brand guidelines PDF/doc | Document type separation, asset validation |
| `wiki-site-generator` | Astro-based documentation site | Asset copy validation, origin tracking |
| `deliverables-package` | Organize and zip final deliverables | Asset manifest, origin markers |

## Routing Rules by Intent

| Intent | Target Spoke | Pre-Validation |
|--------|--------------|----------------|
| "NotebookLM", "notebook", "mind map", "audio overview" | `notebooklm-publishing` | Asset manifest + sources |
| "brand guidelines", "brand book", "documentation" | `brand-documentation` | Asset manifest + outputs |
| "wiki", "documentation site", "Astro site" | `wiki-site-generator` | Asset manifest + docs |
| "package", "zip", "deliverables", "final export" | `deliverables-package` | Asset manifest + all prior |
| "full synthesis" | Run all spokes in order | Full validation |

## Execution Order (With Validation Gates)

```
┌─────────────────────────────────────────────────────────────┐
│ GATE 0: Asset Manifest Generation & Validation              │
│ - Generate .brandmint/asset-manifest.json                   │
│ - Validate ALL paths exist                                  │
│ - Identify user-provided vs generated                       │
│ - Mark deterministic assets                                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ SPOKE 1: brand-documentation                                │
│ - Separate documents: brand, product, campaign              │
│ - Validate asset paths before embedding                     │
│ - Generate PDFs with verified images                        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ SPOKE 2: wiki-site-generator                                │
│ - Copy assets with validation                               │
│ - Track origins in generated pages                          │
│ - Verify ALL image references resolve                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ SPOKE 3: notebooklm-publishing                              │
│ - 3-stage pipeline: Transform → Curate → Assemble           │
│ - Validate ALL source paths before upload                   │
│ - No hallucinated visuals                                   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ SPOKE 4: deliverables-package                               │
│ - Package with origin markers                               │
│ - Generate ASSET-ORIGINS.md                                 │
│ - Final validation before ZIP                               │
└─────────────────────────────────────────────────────────────┘
```

## Lessons Learned (from brandmint-oracle-aleph)

### 1. Source Processing Pipeline (NotebookLM)

**Problem solved:** Sources were auto-generated without proper curation.

**Solution:** 3-stage pipeline in `notebooklm-publishing`:
1. **Transform** — Skill outputs → categorized prose (brand, product, campaign)
2. **Curate** — Select sources by target artifact type
3. **Assemble** — Combine with validated user-provided assets

### 2. Asset Path Validation

**Problem solved:** Paths could be hallucinated or non-existent.

**Solution:** Asset manifest system:
- Generate manifest before synthesis
- Verify EVERY path exists on disk
- Fail fast if required assets missing
- Warn on optional missing assets

### 3. User-Provided vs Generated Distinction

**Problem solved:** No clear tracking of asset origins.

**Solution:** Origin tracking in all spokes:
- `user_provided` — Assets from user (logos, screenshots)
- `generated` — AI-generated assets
- `deterministic: true` — Not AI-generated, always include

### 4. Document Type Separation

**Problem solved:** Single monolithic brand doc.

**Solution:** Three separate documents in `brand-documentation`:
- Brand Identity Guidelines (for designers)
- Product Positioning (for product/sales)
- Campaign Guidelines (for marketing)

### 5. NVIDIA Embedding Integration (Optional)

**Available but optional:** Design Memory Worker with NVIDIA NIM embeddings.

**Use cases:**
- Match visual assets to prose sources
- Verify asset relevance to brand
- Reference image selection for generation

**Configured via:**
```yaml
embedding_integration:
  enabled: true
  worker_url: "https://design-memory.your-domain.workers.dev"
```

## Asset Manifest Schema

```json
{
    "generated_at": "ISO-8601",
    "validation": {
        "all_paths_exist": true,
        "required_assets_present": true,
        "missing_paths": []
    },
    "user_provided_assets": [
        {
            "id": "logo-primary",
            "path": "./assets/logo.png",
            "type": "logo",
            "exists": true,
            "deterministic": true,
            "required": true
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
            "skill": "hero-images"
        }
    ]
}
```

## Quality Gates (Updated)

| Gate | Requirement | Enforced By |
|------|-------------|-------------|
| Asset manifest valid | All paths exist | All spokes |
| No hallucinated paths | Path verification | All spokes |
| User assets marked | Origin tracking | deliverables-package |
| Sources are prose | Not raw JSON | notebooklm-publishing |
| Docs separated by type | 3 documents | brand-documentation |
| Wiki builds | `npm run build` passes | wiki-site-generator |
| All images resolve | Reference check | wiki-site-generator |
| Package verified | Checksum validation | deliverables-package |

## Error Handling

| Error | Spoke | Action |
|-------|-------|--------|
| Required user asset missing | All | **FAIL** |
| Optional asset missing | All | WARN, skip asset |
| Path not in manifest | All | WARN, exclude |
| Hallucinated path | All | **FAIL** |
| Synthesis failed | notebooklm | FALLBACK to mechanical |
| Build failed | wiki-site | **FAIL** |
| Checksum mismatch | deliverables | **FAIL** |

## Loading Spokes On Demand

Spokes are loaded by reading:

```
clusters/synthesis/spokes/<spoke-name>.md
```

Available spokes:
- `notebooklm-publishing.md` — v2.0.0, 3-stage pipeline
- `brand-documentation.md` — v2.0.0, separated documents
- `wiki-site-generator.md` — v2.0.0, validated assets
- `deliverables-package.md` — v2.0.0, origin tracking
