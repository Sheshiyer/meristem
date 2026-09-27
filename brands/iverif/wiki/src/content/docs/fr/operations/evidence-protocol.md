---
title: "Protocole de preuve"
description: "Classification des claims et reçus pour les outputs iverif."
locale: fr
category: operations
status: active
sources:
  - research/EVIDENCE-LEDGER.md
  - wiki/DOWNSTREAM-HANDOFF.md
last_updated: "2026-09-11"
---

# Protocole de preuve

## Classes de claim

| Classe | Sens | Usage aval |
| --- | --- | --- |
| `fact` | Observation publique ou first-party datée, telle qu’écrite | Sûr avec limite citée |
| `observation` | Signal concurrent / marché sans preuve iverif | Contexte seul |
| `hypothesis` | Hypothèse de travail | Étiqueter explicitement |
| `prohibited` | Interdit en copy publique jusqu’à preuve | Bloquer |

## Forme minimale du reçu

```yaml
brand: iverif
source_pages: []
claim_class: supported|proof-required|prohibited
evidence_receipt: ""
reviewed_at: "YYYY-MM-DD"
owner: ""
```

## Règles

1. Une source ne soutient que le claim précis écrit dans le ledger.
2. Ne pas convertir un fait concurrent ou programme en outcome iverif.
3. Re-fetcher les pages ministère / Service-Public avant de citer des effectifs de catalogue live.
4. Les métriques internes de campagne ≠ preuve client.
