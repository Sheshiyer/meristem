# Axtech / Snow Gloves intake reconciliation

Reviewed 5 October 2026. This is a read-only reconciliation of the ongoing Claude Code intake with the Meristem research and campaign preparation. It does not provision tenants, ingest data, accept marketing copy, or authorize delivery.

## Finding

Reuse the Snow Gloves founder intake and portfolio records for operating structure. Reuse the existing Meristem evidence dossiers for domain research. Keep the custom ERP as the selected business record reference, currently read-only. The six-domain Meristem package is a scoped research package within the broader portfolio; it is not a second portfolio registry.

Snow Gloves source was clean at commit `006ec915aeadaa6ba80aca6c6b7e85f40fdbf1e7` during the review. The portfolio intake landed in `6f8afea`; the current fleet session handoff landed in `006ec91`. These local commits do not establish deployment or live marketing acceptance.

## Current source authority

| Concern | Reuse this source | What it establishes |
|---|---|---|
| Founder business descriptions | `snow-gloves-os/specs/006-editorial-steward-integration/founder-intake-2026-10-05.md` | The founder's corrected operating map, installation/sales distinction, retired SaveWatt and open questions |
| Branch/project structure | `snow-gloves-os/specs/006-editorial-steward-integration/portfolio-map-proposal.json` and `docs/PORTFOLIO-ORG-MAP.md` | Named operating branches, projects, parents and proposed sharing rules; legal ownership remains unbound |
| Tenant context | `snow-gloves-os/tenants/<slug>/context/`, `MANIFEST.yaml` | Existing facts and FILL gaps; folder status does not prove a provisioned identity |
| Intake/apply/render process | `snow-gloves-os/docs/onboarding.md`, `scripts/onboard.py`, `prompts/onboard-interview.md` | Existing interview/harvest, module validation and adapter rendering workflow |
| Interpretation / GTM | `snow-gloves-os/specs/004-brand-enriched-autogtm/`, `scripts/lib/gtm.py`, `workflows/skill-hooks.yaml` | Approved-brief derivation, injectable company/people search and fit ranking; current Axtech live adapter acceptance remains unproved |
| Current public-domain research | `meristem/brands/axtech-portfolio-20261002/<slug>/research/{DOSSIER.md,evidence.json}` | Six completed evidence dossiers, including honest provider and identity failures |
| Marketing draft execution | Meristem canonical runner and preserved `.local/axtech-portfolio-20261002/authoring-*` attempts | Actual per-spoke/wave results; failed or partial runs remain failed or partial |
| Editorial derivatives | `meristem/brands/axtech-portfolio-20261002/campaign-drafts-index.md` | 33 proposed emails and 15 proposed LinkedIn posts, held for editorial/owner/sender acceptance; no claim of runner completion |
| ERP references | `heyzack/axtech-campaign-agent/docs/AXTECH-ERP-READONLY-AUDIT.md`, `config/integration-bindings.json` | Actual dated read-only schema/reference evidence, separate from unbound writes and business ownership |
| France MEP normalization | `heyzack/axtech-campaign-agent/src/` | Existing nine-segment classifier, SIREN/SIRET preservation and held export; one headquarters-flag provenance defect remains open |
| Current Explee state | `heyzack/axtech-campaign-agent/receipts/explee-20261005.json` | Current GET snapshot, distinct from historical archived campaigns and optional catalog modules |

Paths above are relative to `/Volumes/madara/2026/Projects/thoughtseed/`. The sibling Snow Gloves files remain owned by the Claude Code work; this review changed none of them.

## Portfolio crosswalk

The proposal contains **nine direct branch tenants beneath Axtech and AXIO beneath Metagration**: ten branch records excluding the Axtech root. Some fleet prose uses an ambiguous count; use the actual parent fields.

| Existing Meristem scope | Snow Gloves identity | Reconciliation |
|---|---|---|
| `axtech` | Axtech portfolio/root tenant | Existing group draft covers HeyZack/Ecoled MEP and separate Kartezzi interior intake only; it is not a complete group offer |
| `heyzack` | `heyzack`, parent `axtech` | Reuse building-automation research and actual brand assets; no repeat identity interview for established facts |
| `ecoled-europe` | `ecoled`, parent `axtech` | Explicit slug alias for the current package; do not create a duplicate `ecoled-europe` tenant or infer a separate legal entity |
| `kartezzi` | `kartezzi`, parent `axtech` | Preserve joinery/furniture/kitchens/doors/decorative/integrated-lighting offer evidence |
| `wave-concept` | `wave-concept`, parent `axtech` | Founder confirms mobile-accessory B2B. Keep the reseller lane separate from MEP |
| `symphonics` | No confirmed tenant; sketch says “Symphonie Électricité?” under HeyZack | No automatic alias or new brand admission. Name, relationship and unavailable-domain identity remain unresolved |
| No current Meristem brand package | `sunfeed`, parent `axtech` | Founder confirms renovation/construction and electrical/plumbing/heat-pump installation. Sunfeed installs; it does not sell the products |
| No current Meristem brand package | `cee-management`, parent `axtech` | CEE eligibility/processing business. `iverif` is its document-processing project, not a parallel brand tenant |
| No current Meristem brand package | `china-sourcing`, parent `axtech` | Existing vendor-network and purchase-intent routing intake. Sensitive network/margin records stay in their own scope |
| No current Meristem brand package | `metagration`, parent `axtech`; `axio`, parent `metagration` | Hospitality/service-business websites and inbound AI answering; AXIO is the B2B training wing. The older AXIO/getleads description conflict is already recorded in `tenants/axio/context/open-questions.md` |
| No current Meristem brand package | `izzimo`, parent `axtech` | Parent established; actual offer remains a source gap |
| Separate future product-sale lane | `axtech-shop` project under `axtech` | Existing group storefront concept; no replacement marketplace/catalog subsystem should be designed before reconciling this project |
| Separate future B2B channel | `safvr-channel` project under `axtech` | Safety/video-intelligence channel recorded. It does not extend the present six-domain MEP campaign package automatically |
| No package | `savewatt`, retired | Do not recreate; explicitly dropped by the founder |

Founder descriptions are attributable founder statements. They do not establish current stock, pricing, operational capacity, quantified proof, legal ownership or approved advertising claims.

## What is already done, and what is still missing

The corrected operating map, tenant scaffolding, reusable control roles, onboarding process, module catalog, approved-brief gate and fleet/onboarding roadmap already exist. Do not recreate them.

In the ten inspected tenants (`axtech`, `heyzack`, `ecoled`, `kartezzi`, `wave-concept`, `sunfeed`, `cee-management`, `china-sourcing`, `metagration`, `axio`), each of the seven context files still contains at least one FILL marker. No `ingest-plan.json` or `vector-index.jsonl` was present in these tenant roots. HeyZack has `enabled.yaml` with selected modules and no agents; that is module selection, not an authenticated running desk or proof of connector readiness. Other checked tenants have no enabled-module record. The existing founder intake is therefore useful source context, while completed Axtech data ingestion/indexing is not demonstrated in this checkout.

The Meristem six-domain dossiers and existing HeyZack content audit already answer some “gather project sources” work in the Snow Gloves editorial handoff. Link and review that evidence rather than running the same domain crawl again. The Snow Gloves legal/company/source fields and the ERP business-unit references still require a reviewed identity binding; neither portfolio position nor a matching business-unit label supplies that binding.

## Concrete duplicate-work risks

1. **Replaying an older harvest overwrites newer facts.** `scripts/onboard.py:368–436` writes context, open questions, raw harvest, enabled modules and runtime files. Existing `sources.yaml` is left unchanged. Do not apply a stale harvest over the 5 October founder edits. Reconcile a field-level delta against current context first; merely rerunning apply is not a merge.
2. **Two competing brand registries.** Use the Snow Gloves parent/project IDs for operating structure and a typed alias for Meristem `ecoled-europe` → Snow Gloves `ecoled`. Retain the six research package IDs and their history without adding duplicate tenants.
3. **Rebuilding an existing GTM pipeline.** Existing Snow Gloves approved-brief derivation and search/fit module is the integration starting point. The campaign CLI supplies the France trade/establishment/provenance requirements that are missing from that generic path. A future adapter must reconcile these contracts, not become another coordinator or sender.
4. **Treating scaffolding or task checks as runtime acceptance.** Spec 006 still holds tenant/caller/module admission, local dispatch and implementation approval. Its `readiness.json` still lists only the initial three branches; the editorial handoff/plan still says to gather HeyZack/Ecoled/Kartezzi sources. These are stale planning references relative to the broader founder map and our completed research. Report the delta to the owner of that work; do not rewrite their concurrent state here.
5. **Assuming documented source isolation is enforced.** `docs/architecture/knowledge-ingest.md` says ingest paths must be tenant-contained, but `scripts/ingest.py:39–53` accepts existing absolute source paths without tenant-root containment. HeyZack's current `sources.yaml` points at an external brand-PDF skill. This is a source-admission gap to reconcile before private data ingestion; no ingest or embedding command was run in this review.
6. **Recreating infrastructure already handled by the fleet session.** Reuse `docs/fleet/HANDOFF-2026-10-05.md` for bootstrap/cutover/node tasks. Its gateway-topology conflict is recorded evidence, not a reason to launch another gateway from the campaign work. No live fleet probing or change occurred here.
7. **Duplicating or prematurely implementing sharing.** The heat-pump chain, shop catalog sharing and China Sourcing intent routing already have named proposed records. Preserve `proposed_not_approved`; participants, fields and authority are not yet accepted integration contracts.

## Public code / private operating data

The current Claude session contains the founder's decision to keep Snow Gloves code public and put operating data into a private ops repository. That split is owned by the ongoing Claude work. No local `/Volumes/madara/2026/Projects/thoughtseed/snow-gloves-ops` checkout was present at review; this does not assert that a remote repository is absent. Do not copy founder/customer/vendor/ERP data, secrets, raw sessions or private receipts into the public-code checkout. This reconciliation stores reference paths and hashes, not private records or raw session contents.

## Continuation order

1. Reuse the current Snow Gloves founder map and preserve its unresolved questions. Stop further brand-structure invention and repeated domain research.
2. Carry forward our current dossiers and unapproved draft package as references. Review the Axtech group draft against the broader operating map before accepting it as group-wide copy.
3. Have the Snow Gloves intake owner reconcile source/context deltas and finish the public/private data boundary before an actual import. No stale-harvest replay or blanket cross-tenant source access.
4. Extend the existing brief/connector path with the campaign CLI's France MEP semantics after tenant, legal sender, ERP and provider contracts are bound. Current ERP MCP access stays read-only.
5. Complete the pending provenance correction and independent editorial checks locally. Delivery remains held until the actual sender, suppression, contact relevance, event/writeback and Vapi/social contracts are accepted.

No new crawl, paid lead operation, tenant ingestion, embedding, ERP query/write, Explee mutation, Vapi call, publishing, infrastructure change or message to another external thread was made by this review. Existing authoring launched before the steering was left intact and its results remain separately attributed.

## Review evidence

The bounded receipt `.planning/AXTECH-SNOWGLOVES-INTAKE-RECONCILIATION-20261005.json` contains 32 source-file SHA-256 values, the inspected ten-tenant artifact matrix and the two Claude Code session references. All 32 source hashes were read back and matched. No raw session messages or credentials are copied. The existing integration audit agent completed an independent read-only review and concurred on portfolio ownership, intake gaps, existing GTM reuse, pending dispatch and source-admission drift. Its informal Wave alias was reconciled to the actual Meristem package slug `wave-concept`. The existing GTM spec's initial Tryambakam Noesis scope and proxy transport are distinct from the current Axtech/public-key API use; adapter compatibility is unverified. Advisor invocation timed out after 30 seconds; no advisor acceptance is claimed.
