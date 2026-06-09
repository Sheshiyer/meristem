---
name: brand-documentation
description: "Create comprehensive brand guidelines document — separated by document type (brand, product, campaign), with validated asset paths."
cluster: brandmint-synthesis
wave: 7
dependencies:
  - all-identity-outputs
  - voice-and-tone
  - messaging-framework
triggers:
  - "brand guidelines"
  - "brand book"
  - "style guide"
  - "brand documentation"
---

# Brand Documentation Skill

Create comprehensive brand guidelines document from validated outputs.

## Critical Lesson: Separate Document Types

Brand documentation must be **separated by document type** to serve different audiences:

| Document Type | Audience | Content Focus |
|---------------|----------|---------------|
| **Brand Identity** | Designers, marketing | Logo, colors, typography, visual language |
| **Product & Positioning** | Product team, sales | Value proposition, positioning, features |
| **Campaign & Content** | Marketing, content | Messaging, copy guidelines, tone |
| **Internal Strategy** | Leadership, founders | Competitive analysis, market data |

## Prerequisites

All identity and strategy outputs with **validated paths**:
- `brand-foundation.json`
- `color-palette.json`
- `typography.json`
- `logo-concept.json`
- `visual-language.json`
- `voice-and-tone.json`
- `messaging-framework.json`

**Asset Manifest** (from deliverables-package or notebooklm-publishing):
- `.brandmint/asset-manifest.json` — validated asset paths

## Process

### Step 1: Load and Validate Assets

```bash
# Validate all assets before building documentation
bm validate-doc-assets --config brand-config.yaml
```

**Validation rules:**
1. Every image reference must exist on disk
2. User-provided assets marked as `deterministic: true`
3. Generated assets marked with source skill and wave
4. Missing assets → warning OR error (configurable)

**Asset categories for documentation:**

| Asset Type | Origin | Include In |
|------------|--------|------------|
| Logo (primary) | user-provided OR generated | Brand Identity doc |
| Logo (variations) | generated | Brand Identity doc |
| Color swatches | generated from palette | Brand Identity doc |
| Typography samples | generated | Brand Identity doc |
| App screenshots | user-provided, deterministic | Product doc |
| Product photos | user-provided OR generated | Product doc |
| Hero images | generated | Campaign doc |
| Social assets | generated | Campaign doc |

### Step 2: Document Structure by Type

#### Brand Identity Document (for designers)

```markdown
# [Brand] Brand Identity Guidelines

## 1. Brand Overview
   - Mission & Vision (from brand-foundation)
   - Brand Values
   - Brand Essence
   - Brand Personality

## 2. Logo System
   - Primary Logo [VALIDATED_PATH: logo-primary.png]
   - Logo Variations [VALIDATED_PATH: logo-*.png]
   - Clear Space Rules
   - Minimum Size
   - Incorrect Usage Examples

## 3. Color Palette
   - Primary Colors [HEX, RGB, CMYK]
   - Secondary Colors
   - Accessibility Contrast Ratios
   - Digital vs Print Usage

## 4. Typography
   - Primary Typeface [VALIDATED_PATH or font name]
   - Secondary Typeface
   - Type Scale
   - Web Implementation

## 5. Visual Language
   - Photography Direction
   - Illustration Style
   - Iconography Rules
   - Pattern Usage
```

#### Product & Positioning Document (for product/sales)

```markdown
# [Brand] Product Positioning

## 1. Value Proposition
   - Core Value Statement
   - Pain Points Addressed
   - Gain Creators

## 2. Target Customer
   - Primary Persona (from buyer-persona)
   - Secondary Personas
   - Jobs to Be Done

## 3. Competitive Positioning
   - Market Position
   - Differentiators
   - Competitive Advantages

## 4. Product Features
   - Feature Highlights
   - Benefits Mapping
   - [VALIDATED_PATH: app-screenshots if provided]

## 5. Pricing & Packaging
   - (if included in skill outputs)
```

#### Campaign & Content Document (for marketing)

```markdown
# [Brand] Campaign & Content Guidelines

## 1. Brand Voice
   - Voice Attributes
   - Tone Spectrum
   - Vocabulary (do/don't use)

## 2. Messaging Framework
   - Tagline
   - Elevator Pitch
   - Value Pillars
   - Proof Points

## 3. Copy Guidelines
   - Headlines Style
   - Body Copy Style
   - CTA Patterns

## 4. Campaign Assets
   - Hero Images [VALIDATED_PATH: hero-*.png]
   - Social Templates [VALIDATED_PATH: social-*.png]
   - Email Headers [VALIDATED_PATH: email-*.png]
```

### Step 3: Asset Path Validation

**Before embedding any image:**

```python
def validate_asset_path(path: str, asset_manifest: dict) -> ValidationResult:
    """
    Validate asset path exists and is in manifest.
    
    Returns:
        ValidationResult with:
        - exists: bool
        - in_manifest: bool
        - origin: 'user_provided' | 'generated' | None
        - deterministic: bool
    """
    # Check file exists on disk
    if not Path(path).exists():
        return ValidationResult(exists=False, error="Path does not exist")
    
    # Check if in asset manifest
    asset = asset_manifest.get('assets', {}).get(path)
    if not asset:
        return ValidationResult(exists=True, in_manifest=False, 
                               warning="Asset not in manifest")
    
    return ValidationResult(
        exists=True,
        in_manifest=True,
        origin=asset.get('origin'),
        deterministic=asset.get('deterministic', False)
    )
```

**Embedding rules:**
- ✅ Path exists AND in manifest → embed
- ⚠️ Path exists but NOT in manifest → warn and embed
- ❌ Path does NOT exist → **NEVER embed**, show placeholder or skip

### Step 4: Content Assembly with Validation

For each section, pull from skill outputs and validate:

| Section | Source Skill | Visual Assets | Validation |
|---------|--------------|---------------|------------|
| Brand Overview | brand-foundation | - | JSON exists |
| Logo | logo-concept | logo-*.png | All paths exist |
| Color | color-palette | - | HEX codes valid |
| Typography | typography | - | Font names valid |
| Visual | visual-language | examples | Paths exist |
| Voice | voice-and-tone | - | JSON exists |
| Messaging | messaging-framework | - | JSON exists |
| Product | product-positioning | screenshots | Paths exist |

### Step 5: Handle Missing Assets Gracefully

```yaml
missing_asset_handling:
  logo:
    required: true
    fallback: "[Logo placeholder - asset not generated]"
    action: warn
    
  app_screenshots:
    required: false
    fallback: "[No screenshots provided]"
    action: skip_section
    
  hero_images:
    required: false
    fallback: "[Hero images pending generation]"
    action: placeholder
```

### Step 6: Format Generation

Generate documentation in multiple formats with validated assets:

| Format | Tool | Asset Handling |
|--------|------|----------------|
| **Markdown** | Native | Relative paths |
| **PDF** | Pandoc/WeasyPrint | Embedded images |
| **HTML** | Static generator | Copied to assets/ |

```bash
# Generate all formats
bm generate-docs --config brand-config.yaml --format all

# Generate specific document type
bm generate-docs --config brand-config.yaml --type brand-identity
bm generate-docs --config brand-config.yaml --type product
bm generate-docs --config brand-config.yaml --type campaign
```

## Output Schema

```json
{
    "skill": "brand-documentation",
    "cluster": "synthesis",
    "wave": 7,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "2.0.0",
    "data": {
        "documents": {
            "brand_identity": {
                "title": "[Brand] Brand Identity Guidelines",
                "path": "deliverables/docs/brand-identity-guidelines.pdf",
                "page_count": 24,
                "sections_complete": 5,
                "sections_total": 5
            },
            "product_positioning": {
                "title": "[Brand] Product Positioning",
                "path": "deliverables/docs/product-positioning.pdf",
                "page_count": 12,
                "sections_complete": 4,
                "sections_total": 5
            },
            "campaign_content": {
                "title": "[Brand] Campaign Guidelines",
                "path": "deliverables/docs/campaign-guidelines.pdf",
                "page_count": 16,
                "sections_complete": 4,
                "sections_total": 4
            }
        },
        "asset_validation": {
            "total_assets_referenced": 15,
            "assets_validated": 15,
            "assets_missing": 0,
            "assets_with_warnings": 0,
            "user_provided_count": 4,
            "generated_count": 11,
            "deterministic_count": 4
        },
        "sections": [
            {
                "name": "Logo System",
                "document": "brand_identity",
                "source_skill": "logo-concept",
                "assets_embedded": [
                    {
                        "path": "generated/logo-primary-v1.png",
                        "validated": true,
                        "origin": "generated"
                    }
                ],
                "complete": true
            }
        ],
        "outputs": {
            "markdown": {
                "brand_identity": "deliverables/docs/brand-identity.md",
                "product_positioning": "deliverables/docs/product.md",
                "campaign_content": "deliverables/docs/campaign.md"
            },
            "pdf": {
                "brand_identity": "deliverables/docs/brand-identity-guidelines.pdf",
                "product_positioning": "deliverables/docs/product-positioning.pdf",
                "campaign_content": "deliverables/docs/campaign-guidelines.pdf"
            }
        },
        "validation_report": {
            "all_assets_exist": true,
            "all_assets_in_manifest": true,
            "hallucinated_paths": 0,
            "warnings": []
        }
    }
}
```

## Quality Checklist

### Asset Validation
- [ ] Asset manifest loaded and validated
- [ ] ALL image paths verified to exist
- [ ] Zero hallucinated/non-existent paths
- [ ] User-provided assets correctly identified
- [ ] Deterministic vs generated assets distinguished

### Document Separation
- [ ] Brand Identity document complete
- [ ] Product Positioning document complete
- [ ] Campaign Guidelines document complete
- [ ] Each document serves its audience

### Content Completeness
- [ ] Logo usage guidelines clear
- [ ] Color palette with accessibility notes
- [ ] Typography examples shown
- [ ] Voice guidelines actionable
- [ ] Messaging framework included

### Format Quality
- [ ] PDF exports cleanly (no broken images)
- [ ] Markdown links work
- [ ] Version and date included
- [ ] Table of contents accurate
