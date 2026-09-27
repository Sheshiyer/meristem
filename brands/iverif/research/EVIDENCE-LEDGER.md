# iverif evidence ledger

**Prepared:** 2026-09-11  
**Purpose:** bounded input to Meristem Wave 1; not public-facing copy.  
**Method:** synthesis of `brands/iverif/inputs/v1/**` plus public FR primary pages
for CEE / Primes Énergie and named market actors. Claim classes below separate
facts, observations, hypotheses, and prohibited public claims.

## Rules for all downstream work

- A source supports only the precise claim written below.
- Do not convert a category, programme, or competitor claim into an iverif
  outcome claim.
- Internal targets from v1 inputs (e.g. “<2% rejection”, “30 seconds”) are
  product aspirations until iverif-specific, dated receipts exist.
- FR GTM copy must keep **obligé** vs **délégataire** roles accurate.
- Approved public domains: brand **iverif.fr**, wiki **iverif.io**.

## Claim classes

| Class | Meaning | Downstream use |
| --- | --- | --- |
| `fact` | Dated public or first-party observation as written | Safe with cited limit |
| `observation` | Competitor / market signal without iverif proof | Context only |
| `hypothesis` | Working assumption to test | Label explicitly |
| `prohibited` | Must not appear in public copy until proved | Block |

## Public-source facts — CEE

| ID | Finding | Evidence | Safe use | Limits | Class |
| --- | --- | --- | --- | --- | --- |
| P1 | France’s CEE (certificats d’économies d’énergie) scheme obliges energy suppliers to promote energy-saving actions; consumers may receive a CEE-related prime for eligible works. | [Service-Public — Certificats d’économie d’énergie (CEE)](https://www.service-public.fr/particuliers/vosdroits/F35584), verified note dated 2026-06-26; [Ministère — Dispositif des CEE](https://www.ecologie.gouv.fr/politiques-publiques/dispositif-certificats-deconomies-denergie). | Explain that CEE is a statutory FR obligation scheme with documented eligibility rules. | Not an iverif product claim; page details change. | fact |
| P2 | Standardised CEE operations are defined in official fiches (catalogue of opérations standardisées) that set technical criteria and forfait savings. | [Opérations standardisées d’économies d’énergie](https://www.ecologie.gouv.fr/politiques-publiques/operations-standardisees-deconomies-denergie) (ministry page; catalogue size and fiche content are live fields). | Programme-rule language may refer to “fiches d’opérations standardisées” as the regulatory reference shape. | Do not invent fiche IDs, forfaits, or catalogue counts in public copy without a fresh fetch. | fact |
| P3 | Sixth CEE period materials and délégataire-related texts are published by the ministry for 2026–2030. | Same ministry CEE dispositif page, section on sixième période (2026–2030). | FR GTM may assume operators work under period-6 obligation rules; confirm dates before publication. | Period texts and délégataire lists are mutable; re-fetch before citing counts. | fact |

## Public-source facts — Primes Énergie

| ID | Finding | Evidence | Safe use | Limits | Class |
| --- | --- | --- | --- | --- | --- |
| P4 | “Prime énergie” / “primes économies d’énergie” is the consumer-facing aid label commonly used for CEE-funded support on eligible renovation works. | [Hellio — Primes économies d’énergie](https://particulier.hellio.com/blog/financement/primes-economies-energie); [Effy — Certificat d’économies d’énergie / Prime Effy](https://www.effy.fr/renovation-energetique/certificat-economie-energie). | Pair “Primes Énergie” with CEE in FR messaging as the market label operators and households recognise. | Competitor pages are commercial; do not reuse their euro amounts or “jusqu’à X%” claims as iverif facts. | fact |
| P5 | Market explainers distinguish **obligés** (energy sellers with CEE obligation), **délégataires** / intermediaries that collect CEE on behalf of obligés, and end beneficiaries (households, entreprises, collectivités). | [Effy pro — Comprendre le marché des primes énergies](https://www.effy.fr/pro/accompagnement-client/comprendre-le-marche-des-primes-energies); [Hellio — dispositif CEE (délégataires)](https://www.hellio.com/aides-financements/certificats-economies-energie). | Keep Marie Durand / ICP copy accurate on obligé vs délégataire. | Roles and accreditation lists change; do not claim iverif is itself an obligé or délégataire. | fact |

## First-party product facts

| ID | Finding | Evidence | Safe use | Limits | Class |
| --- | --- | --- | --- | --- | --- |
| F1 | Brand name is iverif; brand domain iverif.fr; wiki domain iverif.io; GTM region FR / language fr-FR. | `brands/iverif/brand-config.yaml`; v1 source URI `https://iverif.fr/` in `inputs/v1/brand-config.yaml`. | Use these names and domains consistently. | Domain DNS/live site content must be re-checked before launch copy. | fact |
| F2 | Stated programme coverage in v1 materials: CEE, Primes Énergie, Conto Termico, BEG, ECO4, MOVES III. | `inputs/v1/brand-config.yaml` programme capsule; buyer-persona / competitor artifacts. | List programmes as product scope intent. | “Pre-configured” depth per programme is not independently audited in this ledger. | fact |
| F3 | Existing user assets present: `logo-icon.png`, `og-image.png`, `screenshot-hero.png`. | `brands/iverif/assets/`; origins in `assets/ASSET-ORIGINS.md`. | Assess and extend identity; do not regenerate blindly. | Asset presence ≠ legal clearance. | fact |
| F4 | Personality lock from v1: precise / authoritative / no-hype; aspirational craft refs Stripe, Notion, Vercel, Linear. | `inputs/v1/brand-config.yaml`; `product-positioning-summary.json`. | Voice and visual craft guidance for waves. | Aspirational refs are not partnerships. | fact |

## FR competitor observations

| ID | Observation | Evidence | Interpretation boundary | Class |
| --- | --- | --- | --- | --- |
| C1 | Hellio markets itself as a long-standing CEE / energy-efficiency actor and délégataire-style accompaniment for obligés and end customers, including primes énergie content. | [hellio.com CEE](https://www.hellio.com/aides-financements/certificats-economies-energie); [particulier.hellio.com primes](https://particulier.hellio.com/solutions/prime-energie). | Market operator / primes distributor — not evidence that Hellio ships AI cross-document dossier validation equivalent to iverif. | observation |
| C2 | Effy markets renovation énergétique journeys and a branded “Prime Effy” under the CEE mechanism for households and pros. | [effy.fr](https://www.effy.fr/); [Effy CEE page](https://www.effy.fr/renovation-energetique/certificat-economie-energie). | Consumer/pro renovation + primes brand; do not treat Effy euro amounts as category benchmarks for iverif. | observation |
| C3 | Économie d’Énergie SAS and GEO PLC are named direct competitive context for FR/EU obligation-scheme GTM in this seed (operator / market-participant class). | Founder / Phase 1 intake directive for Meristem iverif FR GTM (2026-09-11); secondary confirmation pending live primary-page fetch in a later evidence run. | Treat as named peers for differentiation rules; do not invent product feature comparisons until primary pages are fetched and dated. | observation |
| C4 | v1 competitor artifacts framed indirect competition as generic OCR, legacy DMS, and single-market CEE tools — not the named FR primes operators above. | `inputs/v1/brandmint-outputs/competitor-analysis.json`. | Both frames are useful: named FR actors (Hellio, Effy, …) vs tooling substitutes (OCR/DMS). | observation |

## Working hypotheses to test

1. FR operators (Marie Durand archetype) will respond to dossier-validation messaging that leads with CEE / Primes Énergie accuracy and audit trails rather than multi-country programme breadth. (`hypothesis`)
2. Clear obligé vs délégataire language reduces mistrust in outbound and landing copy. (`hypothesis`)
3. Differentiation against Hellio/Effy succeeds when iverif is framed as pre-submission validation software, not as a primes distributor or renovation marketplace. (`hypothesis`)

## Prohibited public claims until proved

- Specific rejection-rate reduction, “up to 90% fewer errors”, “30 seconds per dossier”, or “go-live in 5–7 days” as guaranteed outcomes. (`prohibited`)
- Any claim that iverif is an accredited obligé, délégataire, or government-affiliated body. (`prohibited`)
- Reuse of competitor euro primes amounts, Trustpilot scores, or “jusqu’à X% d’aides” language. (`prohibited`)
- Market-size figures from v1 wiki (~2M CEE operations/year, 15–20% rejection) until backed by a dated primary source in this ledger. (`prohibited`)
- Privacy / GDPR / “EU-hosted” assurances beyond an audited implementation receipt. (`prohibited`)
