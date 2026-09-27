# Image overlay audit (Phase 6)

Date: 2026-09-11
Scope: iverif/generated/*.png + iverif/website-assets/*.png
OCR available on host: 1

## Inventory

### generated
- `generated/09-capture-compass-spec.png` (1711906 bytes)
- `generated/2A-brand-kit-bento-nanobananapro-v1.png` (1714375 bytes)
- `generated/2A-brand-kit-bento-nanobananapro-v137.png` (1846971 bytes)
- `generated/2B-brand-seal-flux2pro-v1.png` (2713207 bytes)
- `generated/2B-brand-seal-flux2pro-v137.png` (2329808 bytes)
- `generated/2C-logo-emboss-flux2pro-v1.png` (2418197 bytes)
- `generated/2C-logo-emboss-flux2pro-v137.png` (2836605 bytes)
- `generated/APP-ICON-app_icon-flux2pro-v1.png` (990172 bytes)
- `generated/APP-ICON-app_icon-flux2pro-v137.png` (1025029 bytes)
- `generated/EMAIL-HERO-email_hero-nanobananapro-v1.png` (1711906 bytes)
- `generated/EMAIL-HERO-email_hero-nanobananapro-v137.png` (1698238 bytes)
- `generated/OG-IMAGE-og_image-nanobananapro-v1.png` (1550112 bytes)
- `generated/OG-IMAGE-og_image-nanobananapro-v137.png` (1581529 bytes)
- `generated/PITCH-HERO-pitch_hero-nanobananapro-v1.png` (1755809 bytes)
- `generated/PITCH-HERO-pitch_hero-nanobananapro-v137.png` (1649134 bytes)
- `generated/TWITTER-HEADER-twitter_header-nanobananapro-v1.png` (1862248 bytes)
- `generated/TWITTER-HEADER-twitter_header-nanobananapro-v137.png` (1652853 bytes)

### website-assets
- `website-assets/favicon.png` (990172 bytes)
- `website-assets/og-image.png` (1550112 bytes)
- `website-assets/pitch-hero.png` (1755809 bytes)
- `website-assets/twitter-header.png` (1862248 bytes)

## Status
- Heuristic OCR not completed in this pass (tesseract may be absent).
- Operator must visually confirm no EN text overlays before Explee manual post.
- If EN overlays found, re-render via meristem W4/W5 prompts (FR-only text).

## OCR findings (tesseract eng, 2026-09-11)

EN text overlays detected (do not ship in FR Explee package without re-render):

| Asset | Detected EN phrases / words |
|---|---|
| `generated/PITCH-HERO-pitch_hero-nanobananapro-v137.png` | "Stop Losing subsidy Claims To Avoidable Document Errors" |
| `generated/OG-IMAGE-og_image-nanobananapro-v137.png` | "AI document validation for energy subsidy operators" |
| `generated/TWITTER-HEADER-twitter_header-nanobananapro-v1.png` | "AI document validation for energy subsidy operators" |
| `generated/TWITTER-HEADER-twitter_header-nanobananapro-v137.png` | same family |
| `website-assets/og-image.png` | "Real-time validation overview", Documents/Compliance UI chrome |
| `website-assets/twitter-header.png` | "AI document validation for energy subsidy operators" |
| `website-assets/pitch-hero.png` | EN UI chrome / integration labels |

## Packaging rule
- FR GTM draft package may reference meristem W4/W5 prompts for FR re-render.
- Until re-render, prefer non-text seal/logo assets (`2B-brand-seal*`, `APP-ICON*`, `logo-icon.png`) over EN hero copy images.
