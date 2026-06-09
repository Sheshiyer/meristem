---
name: wiki-site-generator
description: "Generate Astro-based documentation wiki from brand outputs. Asset manifest validation, user-provided asset handling, path verification."
cluster: brandmint-synthesis
wave: 7
dependencies:
  - brand-documentation
  - all-generated-assets
triggers:
  - "wiki"
  - "documentation site"
  - "Astro site"
  - "brand wiki"
---

# Wiki Site Generator Skill

Transform brand outputs into a browsable Astro documentation site with validated assets.

## Critical Lesson: Asset Manifest Integration

**NEVER copy assets without validation.** Every asset included in the wiki must:
1. Exist in the asset manifest
2. Have its path verified before copy
3. Be categorized as user-provided or generated

## Prerequisites

- `brand-documentation` complete (markdown content)
- `.brandmint/asset-manifest.json` validated
- Node.js environment
- All asset paths verified to exist

## Process

### Step 1: Load and Validate Asset Manifest

```bash
# Load asset manifest
bm wiki-validate --config brand-config.yaml

# Output:
# ✓ Asset manifest loaded: 15 assets
# ✓ User-provided: 4 assets (all exist)
# ✓ Generated: 11 assets (all exist)
# ✓ Ready to build wiki
```

**Validation checks:**
- [ ] Asset manifest exists at `.brandmint/asset-manifest.json`
- [ ] All `user_provided` asset paths exist
- [ ] All `generated` asset paths exist
- [ ] No duplicate asset IDs

**Asset categories in wiki:**

| Category | Source | Wiki Location | Priority |
|----------|--------|---------------|----------|
| Logo | user-provided OR generated | /images/logo/ | High |
| Screenshots | user-provided, deterministic | /images/product/ | High |
| Hero images | generated | /images/hero/ | Medium |
| Photography | generated | /images/photography/ | Medium |
| Illustrations | generated | /images/illustrations/ | Medium |
| Icons | generated | /images/icons/ | Low |
| Patterns | generated | /images/patterns/ | Low |

### Step 2: Content Transformation

Transform `.brandmint/outputs/*.json` into structured markdown with **validated image references**:

**Transformation mapping:**
| Skill Output | Wiki Page(s) | Assets Referenced |
|--------------|--------------|-------------------|
| brand-foundation | /about, /mission, /values | - |
| buyer-persona | /audience/persona | - |
| product-positioning | /positioning | app screenshots (if provided) |
| voice-and-tone | /voice/guidelines | - |
| messaging-framework | /messaging/pillars | - |
| color-palette | /identity/colors | color swatches |
| typography | /identity/typography | type samples |
| logo-concept | /identity/logo | logo files (validated) |
| visual-language | /identity/visual-style | photography, illustration examples |

**Image reference format:**

```markdown
<!-- CORRECT: Reference validated asset -->
![Primary Logo](/images/logo/logo-primary.png)
<!-- Asset validated: exists=true, origin=user_provided -->

<!-- INCORRECT: Never reference unvalidated paths -->
![Logo](/images/logo/some-logo.png)
<!-- ERROR: Path not in asset manifest -->
```

### Step 3: Site Structure with Asset Organization

```
wiki/
├── src/
│   ├── content/
│   │   ├── docs/
│   │   │   ├── about/
│   │   │   │   ├── mission.md
│   │   │   │   ├── values.md
│   │   │   │   └── story.md
│   │   │   ├── identity/
│   │   │   │   ├── logo.md         # References /images/logo/*
│   │   │   │   ├── colors.md
│   │   │   │   ├── typography.md
│   │   │   │   └── visual-style.md # References /images/photography/*
│   │   │   ├── voice/
│   │   │   │   ├── guidelines.md
│   │   │   │   └── examples.md
│   │   │   ├── messaging/
│   │   │   │   ├── pillars.md
│   │   │   │   └── copy.md
│   │   │   ├── product/
│   │   │   │   └── overview.md     # References /images/product/*
│   │   │   └── assets/
│   │   │       ├── downloads.md
│   │   │       └── inventory.md    # Auto-generated from manifest
│   ├── pages/
│   └── styles/
├── public/
│   └── images/
│       ├── logo/                    # Validated assets only
│       │   ├── logo-primary.png     # [user_provided]
│       │   └── logo-dark.png        # [generated]
│       ├── product/                 # User-provided screenshots
│       │   ├── screenshot-home.png  # [user_provided, deterministic]
│       │   └── screenshot-dash.png  # [user_provided, deterministic]
│       ├── hero/                    # Generated hero images
│       ├── photography/             # Generated photography
│       └── illustrations/           # Generated illustrations
├── asset-manifest.json              # Copy of validated manifest
├── astro.config.mjs
└── package.json
```

### Step 4: Asset Copy with Validation

**NEVER use blind `cp` commands.** Use validated asset copy:

```bash
# CORRECT: Copy with validation
bm wiki-copy-assets --config brand-config.yaml --dest wiki/public/images/

# This script:
# 1. Reads asset manifest
# 2. Validates each source path exists
# 3. Copies to organized destination
# 4. Logs each copy with origin (user_provided/generated)
# 5. Fails if any source path missing
```

**Copy script logic:**

```python
def copy_assets_to_wiki(manifest_path: Path, dest_dir: Path) -> CopyResult:
    """
    Copy validated assets to wiki public folder.
    """
    manifest = json.loads(manifest_path.read_text())
    results = []
    
    for asset in manifest['assets']['user_provided'] + manifest['assets']['generated']:
        source = Path(asset['path'])
        
        # CRITICAL: Validate source exists
        if not source.exists():
            raise AssetNotFoundError(f"Asset missing: {source}")
        
        # Determine destination based on type
        asset_type = asset['type']  # logo, screenshot, hero, etc.
        dest_subdir = ASSET_TYPE_MAPPING.get(asset_type, 'other')
        dest_path = dest_dir / dest_subdir / source.name
        
        # Copy file
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest_path)
        
        results.append({
            'source': str(source),
            'dest': str(dest_path),
            'origin': asset.get('origin'),
            'deterministic': asset.get('deterministic', False)
        })
    
    return CopyResult(copied=len(results), results=results)
```

### Step 5: Generate Asset Inventory Page

Auto-generate `/assets/inventory.md` from manifest:

```markdown
---
title: Asset Inventory
description: Complete list of brand assets
---

# Brand Asset Inventory

Generated from asset manifest on [date].

## User-Provided Assets

These assets were provided by the brand owner and are deterministic (not AI-generated).

| Asset | Type | Location |
|-------|------|----------|
| Primary Logo | logo | /images/logo/logo-primary.png |
| Home Screenshot | screenshot | /images/product/screenshot-home.png |
| Dashboard Screenshot | screenshot | /images/product/screenshot-dash.png |

## Generated Assets

These assets were generated by AI during the brand pipeline.

| Asset | Type | Wave | Skill | Location |
|-------|------|------|-------|----------|
| Hero Image v1 | hero | 4 | hero-images | /images/hero/hero-v1.png |
| Lifestyle Photo 1 | photography | 4 | lifestyle-photography | /images/photography/lifestyle-1.png |

## Download All Assets

[Download ZIP](/downloads/all-assets.zip)
```

### Step 6: Build and Verify

```bash
cd wiki
npm install
npm run build

# Verify all image references resolve
bm wiki-verify-images --dir dist/

# Output:
# ✓ 47 image references found
# ✓ 47 images exist
# ✓ 0 broken references
```

**Verification script:**
- Parse all HTML/MD files for image references
- Check each referenced path exists in `dist/`
- Report any broken references
- **FAIL build if any broken references**

### Step 7: Deploy with Confidence

```bash
# Deploy only after verification passes
bm wiki-deploy --platform vercel --config brand-config.yaml

# Or manual deploy
cd wiki
npm run build
# Deploy dist/ to your platform
```

## Handling Missing User-Provided Assets

```yaml
# In brand-config.yaml
wiki:
  missing_asset_handling:
    user_provided:
      logo:
        required: true
        action: fail  # Stop build if missing
        
      screenshots:
        required: false
        action: placeholder
        placeholder_text: "[Screenshot coming soon]"
        
    generated:
      hero_images:
        required: false
        action: skip  # Don't include section if missing
```

## Output Schema

```json
{
    "skill": "wiki-site-generator",
    "cluster": "synthesis",
    "wave": 7,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "2.0.0",
    "data": {
        "site_config": {
            "framework": "astro",
            "template": "starlight",
            "theme": "brand-custom"
        },
        "asset_handling": {
            "manifest_loaded": true,
            "manifest_valid": true,
            "assets_copied": {
                "total": 15,
                "user_provided": 4,
                "generated": 11,
                "deterministic": 4
            },
            "copy_verification": {
                "all_sources_exist": true,
                "all_copies_verified": true,
                "missing_sources": []
            }
        },
        "pages_generated": [
            {
                "path": "/identity/logo",
                "source_skill": "logo-concept",
                "title": "Logo Guidelines",
                "assets_referenced": [
                    {
                        "path": "/images/logo/logo-primary.png",
                        "validated": true,
                        "origin": "user_provided"
                    }
                ]
            }
        ],
        "image_verification": {
            "total_references": 47,
            "references_resolved": 47,
            "broken_references": 0
        },
        "build": {
            "success": true,
            "output_path": "wiki/dist/",
            "page_count": 18,
            "asset_count": 15
        },
        "deployment": {
            "platform": "vercel",
            "url": "https://brand-wiki.vercel.app",
            "deployed": true
        }
    }
}
```

## Quality Checklist

### Asset Validation
- [ ] Asset manifest loaded and valid
- [ ] ALL source paths verified to exist
- [ ] ALL assets copied successfully
- [ ] User-provided vs generated distinguished
- [ ] Deterministic assets marked correctly

### Image References
- [ ] All markdown image references valid
- [ ] All HTML img src attributes valid
- [ ] Zero broken image references
- [ ] Build verification passes

### Content Completeness
- [ ] All skill outputs transformed to pages
- [ ] Navigation structure logical
- [ ] Search indexes all content
- [ ] Asset inventory page generated

### Deployment
- [ ] Site builds without errors
- [ ] All images load correctly
- [ ] Responsive on mobile
- [ ] Dark mode works (if applicable)
