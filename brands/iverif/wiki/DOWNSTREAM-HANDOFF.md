---
brand: iverif
source_pages:
  - wiki/MDS.md
  - wiki/docs/product/claims.md
  - wiki/src/content/docs/fr/product/claims.md
  - wiki/src/content/docs/en/product/claims.md
  - wiki/docs/operations/evidence-protocol.md
  - wiki/docs/operations/campaign-learning.md
  - research/EVIDENCE-LEDGER.md
  - research/channel-plan.md
  - BRAND-BRIEF.md
  - brand-config.yaml
claim_class: proof-required
evidence_receipt: "research/EVIDENCE-LEDGER.md"
reviewed_at: "2026-09-11"
owner: "iverif-founder"
---

# iverif → Cambium downstream handoff

## Purpose

This handoff turns the iverif FR GTM brand system into a governed input for
Cambium / Fitcheck-style downstream flows. It transfers decision-ready context,
not deployment authority, production state, customer data, or provider credentials.

## Mandated fields (carry on every generated artifact)

```yaml
brand: iverif
source_pages: []
claim_class: supported|proof-required|prohibited
evidence_receipt: ""
reviewed_at: "YYYY-MM-DD"
owner: ""
```

Current handoff defaults:

| Field | Value |
| --- | --- |
| `brand` | `iverif` |
| `source_pages` | see frontmatter list |
| `claim_class` | `proof-required` (default until a page cites a ledger `fact`) |
| `evidence_receipt` | `research/EVIDENCE-LEDGER.md` |
| `reviewed_at` | `2026-09-11` |
| `owner` | `iverif-founder` |

## Canonical Cambium inputs

| Input | Purpose | Consumer rule |
| --- | --- | --- |
| `wiki/MDS.md` | Positioning and messaging decisions | Treat as the default copy spine. |
| `wiki/docs/product/claims.md` | Claim classification (compat path) | Block unsupported / prohibited claims. |
| `wiki/src/content/docs/{fr,en}/product/claims.md` | Locale claim mirrors | Prefer locale matching the artifact. |
| `research/EVIDENCE-LEDGER.md` | Source evidence and claim classes | Runtime source observations outrank stale prose. |
| `wiki/docs/operations/evidence-protocol.md` | Evidence receipt shape | Require provenance for factual outputs. |
| `wiki/docs/operations/campaign-learning.md` | Internal outbound / channel learnings | Do not convert signals into customer proof. |
| `research/channel-plan.md` | FR GTM channel set | Tag orchestration `FR GTM`; no live media authority. |
| `brand-config.yaml` / `BRAND-BRIEF.md` | Brand lock + region | `market.region: FR`, domains iverif.fr / iverif.io. |
| `inputs/v1/**` | Prior BrandMint / wiki seed | Historical context; ledger + wave outputs outrank on conflict. |
| `.brandmint/asset-manifest.json` | Asset provenance | Only package paths that exist and are listed. |

## GTM lock

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

## Stop conditions

- Artifact claims rejection-rate reduction, processing-time guarantees, go-live SLAs, market-size figures, or GDPR/EU-hosting assurances without an iverif-specific dated receipt.
- Artifact claims iverif is an obligé, délégataire, PNCEE partner, or government-affiliated body.
- Artifact reuses Hellio / Effy euro amounts, Trustpilot scores, or “jusqu’à X% d’aides” language.
- Artifact treats Explee drafts or channel-plan rows as live media buys.
- Artifact mutates Cambium runtime state from this Meristem worktree task.

## Handoff state

Waves 1–6 outputs exist under `.brandmint/outputs/`. Wave 7 synthesis receipts
and bilingual wiki scaffolds are complete. This wiki enables founder-reviewed
refinement; it does **not** authorize deployment or public publishing.
Coordinator may run `bm.sh` launch 1–7 next. Do not touch Cambium from this task.
