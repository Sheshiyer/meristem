# Fitcheck evidence ledger

**Prepared:** 2026-08-10  
**Purpose:** bounded input to Meristem Wave 1; not public-facing copy.  
**Method:** deterministic OmniRoute evidence search (Brave/Exa) and primary-page
fetch (Firecrawl/Jina Reader), plus first-party Fitcheck artifacts and internal
campaign analytics already supplied to this project. The source records below
name the provider and retrieval time where the live run supplied them.

## Rules for all downstream work

- A source supports only the precise claim written below.
- Do not convert a category or competitor claim into a Fitcheck outcome claim.
- Internal campaign labels are operational signals, not customer proof.
- Any merchant performance language requires a Fitcheck-specific, dated receipt.
- Approved pricing is **$99 monthly / $799 yearly**. No retired pricing belongs
  in this system.

## Public-source facts

| ID | Finding | Evidence | Safe use | Limits |
| --- | --- | --- | --- | --- |
| P1 | Shopify’s virtual-try-on category shows 297 apps. | [Shopify category](https://apps.shopify.com/categories/store-design-images-and-media-3d-ar-vr/all?feature_handles%5B%5D=cf.3d_ar_vr.visualization.virtual_try_on&page=11&st_source=gadget&surface_detail=slash-ar-virtual-try-on&surface_type=app_details), accessed 2026-08-10. | The category is crowded; discoverability needs a deliberate distribution plan. | A directory count is not market size or demand. |
| P2 | Synthenova’s FitCheck listing has a free plan and usage-based paid plans; the listing showed 0 reviews when accessed. | [Synthenova listing](https://apps.shopify.com/fitcheck-1), accessed 2026-08-10. | Name collision is real; differentiate descriptor, language, and visual identity. | Live App Store data changes; do not infer installs or revenue. |
| P3 | Shopify’s requirements require secure, truthful, privacy-safe apps, accurate sync, necessary access scopes, and merchant access to collected data. | [Shopify App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements), accessed 2026-08-10. | Product and brand work must not overclaim capabilities or hide data practices. | This is platform guidance, not legal advice. |
| P4 | Shopify requires public apps to respond to compliance-webhook privacy requests; its guidance also requires minimization and transparency for protected customer data. | [Privacy compliance](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance); [protected customer data](https://shopify.dev/docs/apps/launch/protected-customer-data), accessed 2026-08-10. | Any shopper-photo or customer-data flow needs a specific privacy and retention review. | The ledger does not determine Fitcheck’s actual data classification. |
| P5 | Shopify states apparel and footwear commonly have above-average return rates because fit and sizing are difficult to judge online. | [Shopify returns guide](https://www.shopify.com/uk/enterprise/blog/eCommerce-returns), accessed 2026-08-10. | Fit uncertainty is a credible merchant problem to explore. | Do not claim Fitcheck reduces returns without Fitcheck-specific measurement. |

## First-party product facts

| ID | Finding | Evidence | Safe use | Limits |
| --- | --- | --- | --- | --- |
| F1 | Fitcheck is a Shopify App Store app by Thoughtseed, launched July 23, 2026, with 0 reviews at retrieval. | Firecrawl fetch of [Fitcheck Shopify listing](https://apps.shopify.com/fitcheck-try-on), 2026-08-10 10:42 IST. | Reference the verified distribution presence. | Reviews, listing copy, and pricing are live fields that must be re-checked before publication. |
| F2 | The approved Fitcheck offer is $99 monthly / $799 yearly. | Current Fitcheck landing configuration and founder direction, 2026-08-10. | Use those prices consistently. | No promised outcome is embedded in the price. |
| F3 | Existing identity assets are orange/navy/tech-blue logo, mark, landing hero, and social asset. | `brands/fitcheck/assets/` checksums recorded in this repository. | Assess and extend, rather than regenerate the identity blindly. | Asset presence does not establish legal clearance. |

## Internal operating observations

| ID | Observation | Evidence | Interpretation boundary |
| --- | --- | --- | --- |
| I1 | Outbound baseline: 1,241 sends; 18 replies; 5 provider-labelled hot leads; $37.23. | Existing Explee campaign analytics supplied to project, accessed 2026-08-10. | A small signal for continued outbound learning, not revenue or product-market-fit evidence. |
| I2 | Fashion Marketplaces had the best reply-rate cohort (3.0%); Retail Tech Teams and Shopify Fashion Brands each supplied two hot labels. | Existing Explee cohort analytics supplied to project. | Prioritization hypothesis for a new pilot, not a statistically conclusive ICP finding. |

## Deterministic evidence run — 2026-08-10

| Step | Result | Receipt / limit |
| --- | --- | --- |
| Provider health | Brave and Exa are configured; Firecrawl and Jina Reader both returned HTTP 200 fetch probes. | `temperance-search-evidence.sh --providers` |
| Category/name search | Brave returned HTTP 429; the helper fell through to Exa. Exa returned the Fitcheck and Synthenova listing URLs, plus category peers. | Exa `search-bef05874-cb12-4f53-8e79-9a551f646876`, 2026-08-10T09:41:49Z. |
| Shopify privacy search | Brave returned Shopify’s protected-data, App Store, privacy, and access-scope documentation. | Brave `search-8d25d078-3290-4fcb-82da-5fc176403723`, 2026-08-10T09:41:48Z. |
| Fitcheck listing fetch | Firecrawl returned the live Thoughtseed listing, including its developer, launch date, review count, live price display, and public copy. | `web/fetch` Firecrawl, 2026-08-10 10:42 IST. |
| Shopify privacy fetch | Firecrawl returned Shopify’s requirement to link a privacy policy and explain data collection, use, retention, and contact route. | `web/fetch` Firecrawl, 2026-08-10 10:42 IST. |
| Competitor fetch | The helper’s fetch attempt returned 504 for the Synthenova URL. | Search evidence is retained; do not state current competitor details beyond the earlier dated observation until a later fetch succeeds. |

## Live-listing reconciliation flag

The live Fitcheck listing fetched on 2026-08-10 displayed **Free** and included
legacy claims about return reduction, add-to-cart rates, a 48-hour launch, and
under-15-second renders. This conflicts with this system’s approved commercial
source of truth ($99 monthly / $799 yearly) and its no-unverified-outcomes rule.

- Keep $99 monthly / $799 yearly as the brand-system commercial source of truth.
- Treat the live Shopify listing as an external reconciliation item until its
  current display is independently re-fetched with aligned pricing and claims.
- Do not use the fetched performance/return claims in brand, agency, wiki, or
  campaign materials.

## Working hypotheses to test

1. A descriptor-led identity—**AI Fit Confidence for Shopify**—can distinguish
   Fitcheck from Synthenova while retaining the existing name.
2. Guided setup and a measurement plan may reduce perceived adoption risk for
   emerging and mid-market Shopify fashion merchants.
3. Distribution-led outreach is the appropriate early channel; App Store search
   should be measured, not presumed.

## Prohibited public claims until proved

- Conversion lift, revenue lift, return reduction, adoption volume, or customer
  satisfaction.
- Claims that a try-on result guarantees size, fit, appearance, or purchase
  suitability.
- Any privacy, security, or retention claim beyond an audited implementation.
