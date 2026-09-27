# Fitcheck → Cambium downstream handoff

## Purpose

This handoff turns the Fitcheck brand system into a governed input for Cambium
downstream flows. It transfers decision-ready context, not deployment authority,
production state, customer data, or provider credentials.

## Canonical inputs

| Input | Purpose | Consumer rule |
| --- | --- | --- |
| `wiki/MDS.md` | Positioning and messaging decisions | Treat as the default copy spine. |
| `wiki/docs/product/claims.md` | Claim classification | Block unsupported claims. |
| `research/EVIDENCE-LEDGER.md` | Source evidence and live discrepancies | Runtime source observations outrank stale prose. |
| `wiki/docs/operations/evidence-protocol.md` | Evidence receipt shape | Require provenance for factual outputs. |
| `wiki/docs/operations/campaign-learning.md` | Internal outbound learnings | Do not convert signals into customer proof. |

## Required downstream fields

Every generated downstream artifact should carry:

```yaml
brand: fitcheck
source_pages: []
claim_class: supported|proof-required|prohibited
evidence_receipt: ""
reviewed_at: "YYYY-MM-DD"
owner: ""
```

## Stop conditions

- The artifact claims fit certainty, conversion lift, return reduction, user
  volume, quality, privacy practice, or setup speed without a Fitcheck-specific
  source.
- It uses pricing other than $99 monthly / $799 yearly.
- It treats the live Shopify listing as reconciled despite the ledger flag.
- It copies or implies affiliation with Synthenova.

## Handoff state

Wave 1 is complete in canonical Meristem. Strategy, identity, and content
receipts are inherited context pending their evidence-led refresh. This wiki
enables that refinement; it does not authorize deployment or public publishing.
