---
title: "Paysage concurrentiel"
description: "Pairs marché FR/UE et substituts outillage pour différencier iverif."
locale: fr
category: market
status: evidence-bounded
claim_class: observation
sources:
  - .brandmint/outputs/competitor-analysis.json
  - research/EVIDENCE-LEDGER.md
  - brand-config.yaml
last_updated: "2026-09-11"
---

# Paysage concurrentiel

**Cadre :** les acteurs nommés ci-dessous sont surtout des **opérateurs de marché / distributeurs de primes**, pas la preuve qu’ils livrent un logiciel AI de validation cross-document équivalent. Les substituts outillage forment un second cadre.

## Contexte FR / UE nommé (observation)

| Nom | Classe | Règle de différenciation |
| --- | --- | --- |
| **Hellio** | Accompagnement CEE / primes FR (C1) | iverif valide des dossiers ; Hellio opère des services CEE / primes. Aucune affiliation. |
| **Effy** | Parcours rénovation + Prime Effy sous CEE (C2) | Effy vend primes et parcours ; iverif vend la validation documentaire pré-dépôt. Ne jamais réutiliser les montants euros. |
| **Économie d'Énergie SAS** | Acteur FR économies d’énergie / marché CEE (C3) | Opérateur / participant de marché — pas un logiciel AI de validation de dossiers. Matrice features en attente de fetch de pages primaires datées. |
| **GEO PLC** | Participant de dispositifs d’obligation UE (C3) | Différenciation soft : validation logicielle vs opérateur de dispositif. Pas de parité features inventée. |

## Substituts outillage indirects

- **OCR / IDP génériques** — extraction sans règles programme CEE embarquées
- **DMS legacy** (SharePoint, DocuSign, etc.) — stockent et routent ; ne valident pas contre les fiches
- **Outils CEE mono-marché** — couverture multi-programme limitée / charge de règles self-serve

## Écart de marché (hypothèse)

Peu d’outils se positionnent explicitement comme **validation AI pré-dépôt pour back-offices CEE / délégataires**. Traiter comme hypothèse de catégorie — pas une claim de monopole.

## Confusion acheteur à lever

Les opérateurs qui comparent des parcours type Hellio/Effy peuvent confondre **distribution de primes** et **logiciel de validation**. Le messaging doit séparer les deux clairement.
