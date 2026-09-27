---
title: "Evidence protocol"
description: "How to classify claims and attach receipts for iverif outputs."
locale: en
category: operations
status: active
sources:
  - research/EVIDENCE-LEDGER.md
  - wiki/DOWNSTREAM-HANDOFF.md
last_updated: "2026-09-11"
---

# Evidence protocol

## Claim classes

| Class | Meaning | Downstream use |
| --- | --- | --- |
| `fact` | Dated public or first-party observation as written | Safe with cited limit |
| `observation` | Competitor / market signal without iverif proof | Context only |
| `hypothesis` | Working assumption to test | Label explicitly |
| `prohibited` | Must not appear in public copy until proved | Block |

## Receipt shape (minimum)

```yaml
brand: iverif
source_pages: []
claim_class: supported|proof-required|prohibited
evidence_receipt: ""   # path or URL + date
reviewed_at: "YYYY-MM-DD"
owner: ""
```

## Rules

1. A source supports only the precise claim written in the ledger.
2. Do not convert competitor or programme facts into iverif outcome claims.
3. Re-fetch ministry / Service-Public pages before citing live catalogue counts or period texts.
4. Internal campaign metrics ≠ customer proof (see campaign learning).
