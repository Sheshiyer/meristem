---
title: "Apprentissage campagne"
description: "Usage interne des signaux canaux FR GTM."
locale: fr
category: operations
status: active
sources:
  - research/channel-plan.md
  - .brandmint/outputs/campaign-orchestrator.json
last_updated: "2026-09-11"
---

# Apprentissage campagne

## Objet

Capturer des signaux de priorisation pour le GTM France (LinkedIn FR, JDN, Les Échos, WTTJ, contexte PNCEE). Ces signaux guident l’itération ; ce **ne sont pas** des preuves client.

## Usages internes autorisés

- Classer hooks / créas pour tests ultérieurs
- Affiner le ciblage titres Marie Durand
- Noter quelles explications obligé vs délégataire réduisent la confusion
- Flagger la copy qui a échoué à la revue de claims

## Conversions interdites

- Taux de réponse → « les clients adorent iverif »
- Impressions → leadership de marché
- Créas Explee draft → claims de performance live
- Lignes du channel-plan → autorité budgétaire

## Tag

Tous les journaux d’apprentissage orchestrés portent `gtm_tag: FR GTM`.
