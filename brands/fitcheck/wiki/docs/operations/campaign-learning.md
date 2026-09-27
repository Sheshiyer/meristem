---
title: "Campaign learning"
description: "Internal outbound baseline, test hypotheses, and measurement boundaries for Fitcheck."
sidebar:
  order: 20
status: "internal-draft"
source_artifacts:
  - "../../../research/EVIDENCE-LEDGER.md"
  - "../../../research/FOUNDATION-IMPORT.md"
claim_reviewed: true
last_reviewed: "2026-08-10"
---

# Campaign learning

This page is an internal planning record. It does not establish product-market
fit, customer outcomes, or a promised result for future outreach.

## Baseline signal

Existing Explee analytics supplied to the project recorded:

| Metric | Internal observation |
| --- | ---: |
| Sends | 1,241 |
| Replies | 18 |
| Provider-labelled hot leads | 5 |
| Recorded spend | $37.23 |

These numbers are operational signals only. A "hot" label is provider-assigned,
not Fitcheck qualification; a reply is not a meeting, install, conversion, or
revenue outcome. The governing source and its limits are in the [evidence ledger](../../../research/EVIDENCE-LEDGER.md#internal-operating-observations).

## Cohort observations

The internal dataset indicated a 3.0% reply-rate cohort for Fashion
Marketplaces. Retail Tech Teams and Shopify Fashion Brands each supplied two
provider-labelled hot leads. This is a prioritisation hypothesis, not a
statistically conclusive ICP finding.

| Test priority | Why it is worth testing | Decision boundary |
| --- | --- | --- |
| Fashion Marketplaces | Highest observed reply-rate cohort in the existing data. | Test against a narrowly specified contact and geography definition. |
| Retail Tech Teams | Two provider-labelled hot leads. | Validate whether the role can buy, refer, or partner before calling it demand. |
| Shopify Fashion Brands | Two provider-labelled hot leads and direct product relevance. | Confirm store fit, decision-maker role, and consent/compliance constraints. |

## Next-test design

Use one defined Shopify-fashion cohort per learning cycle. Before any send,
record the target geography, retailer profile, role, exclusions, source links,
message angle, reply-classification rubric, owner, and suppression rules.

Judge the cycle using deliverability, reply quality, qualified conversations,
meetings, opt-outs, and segment-level learnings. Do not use open rates as the
primary success criterion and do not represent any metric publicly without a
Fitcheck-owned, dated receipt.

## Message guardrails

- Use the descriptor **AI Fit Confidence for Shopify** and the approved offer:
  **$99 monthly / $799 yearly**.
- Describe a product-page AI try-on interaction, not a sizing guarantee,
  returns-reduction programme, or conversion engine.
- Ground personalisation in a recorded public source; never invent product,
  business, or person-specific details.
- Include a compliant opt-out path and honour suppression requests.

The [evidence protocol](evidence-protocol.md) applies to every segment and
claim. For an agency-delivered test, use the [LaCleo pilot brief](lacleo-pilot.md)
as the operating handoff.
