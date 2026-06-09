---
name: social-media-assets
description: "Generate platform-specific visual assets for social media — profile images, covers, post templates, story formats. Uses GPT-Image-2 for generation."
cluster: brandmint-photography
wave: 4
dependencies:
  - visual-language
  - logo-concept
  - hero-images
triggers:
  - "social media assets"
  - "Instagram"
  - "Facebook cover"
  - "social graphics"
---

# Social Media Assets Skill

Generate optimized visual assets for all social media platforms.

## Prerequisites

Load upstream outputs:
- `visual-language.json` — for visual style
- `logo-concept.json` — for profile images
- `hero-images.json` — for cover/header reference
- `color-palette.json` — for brand colors

## Process

### Step 1: Platform Requirements

Define assets needed per platform:

| Platform | Asset Type | Dimensions | Format |
|----------|------------|------------|--------|
| **Instagram** | Profile | 320x320 | Square |
| | Post | 1080x1080 | Square |
| | Landscape | 1080x566 | 1.91:1 |
| | Portrait | 1080x1350 | 4:5 |
| | Story/Reel | 1080x1920 | 9:16 |
| **Facebook** | Profile | 170x170 | Square |
| | Cover | 820x312 | 2.63:1 |
| | Post | 1200x630 | 1.91:1 |
| **Twitter/X** | Profile | 400x400 | Square |
| | Header | 1500x500 | 3:1 |
| | Post | 1200x675 | 16:9 |
| **LinkedIn** | Profile | 400x400 | Square |
| | Cover | 1584x396 | 4:1 |
| | Post | 1200x627 | 1.91:1 |
| **YouTube** | Profile | 800x800 | Square |
| | Banner | 2560x1440 | 16:9 |
| | Thumbnail | 1280x720 | 16:9 |

### Step 2: Profile Image Strategy

For profile images across platforms:

**Options:**
- Logo mark only (if strong symbol)
- Lettermark
- Simplified logo
- Branded graphic element

**Considerations:**
- Must be recognizable at small sizes
- Should work on various backgrounds
- Consistent across all platforms

### Step 3: Cover/Banner Strategy

For cover images:

**Safe zones:** Account for cropping on different devices
**Content:** Support brand messaging without competing with UI elements
**Variants:** May need seasonal or campaign updates

### Step 4: Post Template System

Create template styles for:

| Template | Purpose | Elements |
|----------|---------|----------|
| **Quote** | Engagement | Text on brand background |
| **Product** | Sales | Product + headline |
| **Lifestyle** | Aspiration | Photo + subtle branding |
| **Announcement** | News | Bold text + graphic |
| **Carousel** | Education | Consistent header/footer |

### Step 5: Generate Prompts

**Profile image prompt:**
```
Brand profile image for [brand name].
Featuring: [logo mark / lettermark / symbol]
Background: [brand primary color]
Style: Clean, modern, recognizable at small sizes
Square format, 400x400px equivalent.
```

**Cover image prompt:**
```
Social media cover/banner for [brand name].
Scene: [key brand visual or product lifestyle]
Composition: Safe zone in center for text/profile overlay
Colors: [brand palette]
Mood: [from visual-language]
Style: Professional, brand-aligned
Dimensions: [platform-specific]
```

### Step 6: Generate Assets

```bash
# Profile images
for platform in instagram facebook twitter linkedin youtube; do
    bash visual/gpt-image-2/scripts/gen.sh \
        --prompt "$(cat prompts/profile-$platform.txt)" \
        --out "$brand_dir/generated/social/$platform-profile.png" \
        --aspect 1:1
done

# Cover images
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/cover-facebook.txt)" \
    --out "$brand_dir/generated/social/facebook-cover.png" \
    --aspect 2.63:1
```

## Output Schema

```json
{
    "skill": "social-media-assets",
    "cluster": "photography",
    "wave": 4,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "platforms": ["instagram", "facebook", "twitter", "linkedin", "youtube"],
        "profile_strategy": {
            "approach": "string (logo mark, lettermark, etc.)",
            "background": "string",
            "prompt": "string"
        },
        "cover_strategy": {
            "approach": "string",
            "safe_zones": "string",
            "seasonal_updates": "boolean"
        },
        "assets": [
            {
                "platform": "string",
                "type": "string (profile, cover, post)",
                "dimensions": "string",
                "aspect_ratio": "string",
                "generation_prompt": "string",
                "generated_path": "string"
            }
        ],
        "post_templates": [
            {
                "name": "string",
                "purpose": "string",
                "elements": ["string"],
                "prompt": "string"
            }
        ],
        "generation_summary": {
            "total_assets": "number",
            "generated": "number",
            "pending": "number"
        }
    }
}
```

## Quality Checklist

- [ ] Profile images defined for all major platforms
- [ ] Cover images account for safe zones
- [ ] All dimensions match current platform specs
- [ ] Post templates cover key content types
- [ ] Assets maintain brand consistency
- [ ] Small-size legibility verified for profiles
