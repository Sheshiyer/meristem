# iverif — France GTM Channel Plan

Research artifact for Meristem wave runs. Prefer this over adding a `social-growth` spoke so the runner need not register a new skill ID.

**Scope:** `market.region: FR` · energy-subsidy / CEE operators · bilingual FR+EN content  
**Brand:** iverif  
**Status:** draft research (not live media buys)

---

## Primary channels (required FR set)

| Channel | Role | Audience fit | Content types |
|---------|------|--------------|---------------|
| **LinkedIn FR** | Primary ABM / demand | Responsable Back-Office CEE, Compliance CEE, Ops délégataire/obligé | Thought leadership, short hooks, carousel dossier-pain, lead forms |
| **Welcome to the Jungle** | Employer + category presence | Operators hiring compliance/back-office talent; brand trust signal | Company page narrative, ops culture, product-as-tool-for-teams |
| **JDN (Journal du Net)** | Tech / SaaS press & thought | Digital decision-makers, B2B SaaS buyers | Bylines, product announce, RegTech angle |
| **PNCEE** | Institutional / regulatory adjacency | CEE programme stakeholders, rule-aware operators | Evidence-led explainers; no false affiliation claims |
| **Les Échos** | Business press | Exec / finance / energy-services leadership | Press release, funding/product milestones, market framing |

---

## Channel notes

### LinkedIn FR
- Default paid + organic surface for Marie Durand ICP.
- Job-title targeting: see `buyer-persona` FR LinkedIn titles (Responsable Back-Office CEE, Chef de projet CEE, etc.).
- Pair with `short-form-hook-generator` bilingual hooks and `ad-creative-copy` LinkedIn variants.
- Explee drafts (`ad-creative-copy.explee_draft`) may seed creatives — **draft-only, no POST**.

### Welcome to the Jungle
- Use for credibility with operators who recruit heavily; not a direct performance channel.
- Align employer story with product: fewer rejected dossiers, less peak-season burnout.

### JDN
- Pitch RegTech / AI document validation for energy subsidies; avoid unsupported accuracy claims.
- Route announce copy from bilingual `press-release` wiki paths.

### PNCEE
- Treat as **context and language source**, not a paid media buy.
- Messaging must respect institutional role; never imply endorsement.
- Useful for glossary, FAQ, and proof-required claim framing.

### Les Échos
- Primary FR business newswire target for `press-release` FR locale.
- Dateline/city and factual tone per press-release spoke FR conventions.

---

## Secondary / support

- Company website FR landing (`wiki/src/content/docs/fr/marketing/landing-page.md` → site build).
- Email sequences (`launch-email-sequence` locales fr/en).
- EN mirrors for EU desks and international investors (`wiki/src/content/docs/en/marketing/*`).

---

## GTM tag

When `market.region: FR`, campaign orchestration should tag outputs:

```yaml
gtm_tag: FR
gtm_label: "FR GTM"
locales: [fr, en]
defaultLocale: fr
channels:
  - linkedin_fr
  - welcome_to_the_jungle
  - jdn
  - pncee
  - les_echos
```

---

## Downstream consumers

- `campaign-orchestrator` — apply FR GTM tag from `market.region`
- `ad-creative-copy` / `landing-page-copy` / `launch-email-sequence` / `press-release` — bilingual wiki paths
- `short-form-hook-generator` — bilingual hooks biased to LinkedIn FR
- `wiki-site-generator` — Starlight i18n `en` + `fr`, `defaultLocale: fr`
- `deliverables-package` — zip both locales

---

## Stop conditions

- Do not claim PNCEE partnership or accreditation without evidence receipt.
- Do not POST Explee or ad-platform drafts from Meristem spokes.
- Do not treat this file as live media plan or budget authority.
