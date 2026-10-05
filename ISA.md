---
schema: thoughtseed.isa.v1
project: meristem
effort: E3
updated_at: 2026-10-05
phase: execute
---

## Problem

Two preserved branches contain overlapping brand packages and shared coordinator changes. The coordinator could mark a wave complete after missing clusters or failed spokes. Historical generation artifacts and unfinished Iverif planning could also be mistaken for current product or launch authority.

## Vision

A source-grounded Axtech portfolio workflow that researches each brand, produces France-specific B2B drafts by relevant trade, and verifies the actual ERP, Explee, Vapi and social contracts before activation. Historical source reconciliation and all failed attempts remain recoverable.

## Goal

Run a fresh, source-grounded Meristem research and marketing workflow for Axtech, HeyZack, Kartezzi, Ecoled Europe, Wave Concept and Symphonics using configured Perplexity, Exa and Firecrawl through OmniRoute. Preserve each brand's actual offer, qualify France/region targeting and verify ERP/Vapi/Explee/social end-to-end contracts before any activation or publication. The prior source reconciliation is closed historical work; current draft and operational criteria below govern this run.

## Principles

- Historical generated artifacts are preserved with provenance; they do not redefine product identity.
- A failed or skipped prerequisite cannot be converted to completion.
- Domain-specific research follows source evidence, not locale inference.
- Host configuration, credentials and execution traces stay local.
- Explicit return checks must remain reliable when Bash functions run in conditional contexts.

## Out of Scope

No campaign activation/import/send, budget increase, public social publication, ERP write, provider configuration migration, new identity/media generation or live calls are authorized in this preparation run. B2C marketplace and short-stay/ESAC campaigns are separate future lanes; their contract requirements may be mapped, but they do not enter the current B2B MEP target pool.

## Constraints

The connected custom Axtech ERP MCP is authorized for read-only reference use. Legal sender, brand/business-unit ownership, suppression/consent, durable event IDs, idempotency and terminal writeback require actual contracts rather than assumptions. A completed internal draft never implies operational acceptance or owner approval. NAF is a discovery hint; headquarters location does not prove service coverage.

## Historical source scope and constraints

Implementation was isolated from the primary checkout. The parent completed authorized source release through reviewed PR #2; no live generation, NotebookLM publication, delivery, deployment or organ activation is included. Substantial implementation used the Build rail, with provider attribution explicitly unresolved. The earlier August enrollment ISA is superseded for this reconciliation; no claim is made about Superset registration or current host runtime readiness.

## Criteria

- [x] ISC-1: Both checkpoint tips are ancestors of preserved `codex/reconcile-meristem-20260927`; main contains its reviewed curated tree and identical brand inputs are retained once.
- [x] ISC-2: Required missing/empty clusters and tracer/later failures return failure and cannot mark a wave complete.
- [x] ISC-3: Only existing valid JSON with matching skill and complete status can complete a spoke; skipped/partial output fails.
- [x] ISC-4: Retry completion is idempotent, stale failure clears on success, and failed reruns remove obsolete completion.
- [x] ISC-5: Existing directory regression plus synthetic failure, retry and state-write checks pass without providers or waits.
- [x] ISC-6: FR additions remain, with unreviewed or absent Iverif channel evidence blocking readiness and CEE guidance scoped to an evidenced domain.
- [x] ISC-7: Historical Cambium generation is distinct from current reviewed system/visual authority.
- [x] ISC-8: All 173 current brand JSON files parse; Cambium 12, Fitcheck 4 and Iverif 3 asset hashes match; external Thoughtseed paths are explicitly qualified.
- [x] ISC-9: Shell syntax and changed-file whitespace checks pass; exact tests/risks are recorded for review.
- [x] ISC-10: Remote source release uses a reviewed, pinned-head PR; provider generation, publication, campaign and deployment remain outside this task.

## Test Strategy

| Criterion | Verification |
|---|---|
| ISC-1 | `git merge-base --is-ancestor` for both checkpoint tips |
| ISC-2–5 | All `tests/runner-*.test.sh` with synthetic fixtures and stubbed side effects |
| ISC-6–7 | Source review of FR contracts and brand provenance/readiness documents |
| ISC-8 | Parse tracked brand JSON; recompute SHA-256 for available manifest hashes; classify absolute external refs |
| ISC-9 | `bash -n`, `git diff --check`, local review receipt |
| ISC-10 | Scoped operation record; no runtime acceptance inferred |

## Features

Source reconciliation precedes runner verification. Historical asset packages and bilingual instruction refinements are independently reviewable; neither grants execution authority. Release follows parent review rather than automatic next-wave dispatch.

## Decisions

Preserve the original brand packages without silently rewriting source claims. Record qualifications in new provenance/readiness documents. Iverif seed material exists; current claim approval, evidence refresh and wiki application packaging remain incomplete.

## Changelog

2026-09-27: Source release completed through PR #2 (`05b4853`). The prepared and merged trees match exactly; primary main was clean and synchronized. Earlier worktree-only release holds are closed, while brand/publication/runtime gates remain open.

## Verification

All three runner suites passed under Bash 5.3 and macOS Bash 3.2. Each runner/test/planning shell file passed syntax checking with both interpreters. All 173 tracked brand JSON files parse; 19 available Cambium/Fitcheck/Iverif asset hashes match. Thoughtseed has 44 existing references, including 24 external host paths without stored hashes; this remains a portability limitation. New runtime, tests and reconciliation documents pass base-to-head whitespace checks. Inherited archival generated-source whitespace is preserved intentionally. Both checkpoint tips are ancestors. See `.local/review-ready.md` for scope, route attribution and release boundaries.

## Axtech portfolio run — 2026-10-02

The user now authorizes fresh research and Meristem flow per supplied brand, with B2B MEP targeting before Explee campaigns or social publication. The historical reconciliation criteria above remain closed; this run has independent open criteria. Current identity assets remain source-authoritative.

- [x] AX-ISC-1: Canonical runner and configured research rails are traced from current source.
- [x] AX-ISC-2: Each of six domains has a fresh source/evidence research dossier with provider receipts or explicit provider/availability failure.
- [ ] AX-ISC-3: Per-brand Meristem prompts and outputs are advanced through the actual runner with honest tracer and completeness states.
- [x] AX-ISC-3.1: Six actual first-run tracer attempts have runner state and provider/gate receipts; failed and partial runs are not marked complete.
- [ ] AX-ISC-3.2: Five evidenced brands complete the scoped research, strategy and content draft waves; Symphonics remains an explicit identity hold.
- [x] AX-ISC-4: B2B MEP segmentation includes sole traders and deduplicates verified mixed activities.
- [ ] AX-ISC-4.1: One SIREN retains every establishment/location/source observation idempotently; contradictory geography is held and provenance is not mixed.
- [ ] AX-ISC-5: Per-brand marketing and social draft artifacts cite validated inputs and preserve claim boundaries.
- [x] AX-ISC-6: ERP, Vapi, Explee and social contracts are mapped; configured, source, synthetic and live evidence are distinguished.
- [ ] AX-ISC-7: Meaningful local end-to-end contract probes pass, or exact external blockers are recorded.
- [ ] AX-ISC-8: No Explee start, send, budget increase, public social publish, secret/provider migration or unapproved live-data write occurs.

### Current verification — 2 October 2026

AX-ISC-3.1: Read actual six `.brandmint/state.json` files and tracer receipts. Five first attempts failed structured-response parsing; Symphonics produced a local identity-gated partial without a provider call. Preserved fresh authoring-v2 attempts completed wave1 for HeyZack, Ecoled and Axtech, then stopped before HTTP at the128KiB context guard. Dependency-only assembly is repaired and tested. All five fresh v3 attempts stopped honestly: HeyZack/Wave foundation returned partial for operational holds; Ecoled/Kartezzi completed wave1 then voice-and-tone reported a missing positioning dependency; Axtech competitor JSON was malformed. Correct draft scope and strategy ordering remain required. No state was hand-edited; partial generation is not a finished marketing package.

AX-ISC-6: User connected the custom Axtech ERP MCP for read-only references. Fifteen bounded SELECT queries verified actual society/business-unit/brand/activity/client/lead/product schemas and aggregates. `docs/AXTECH-ERP-READONLY-AUDIT.md` and the portable integration binding distinguish verified reads from unbound writes, suppression, consent, idempotency and terminal writeback. ERPNext/Zoho remain unselected.

AX-ISC-4/7: Local CLI107tests and strict typecheck pass after residual corrections. Independent stable review passed72/73focusedstdout checks; the remaining uppercase-HTTP-scheme P2 is corrected with a regression test, final readback pending. Fresh official Annuaire shape confirmed nested headquarters geography and total_results; mapper/tests corrected. Meristem33Python tests and6shell suites pass, including dependency filtering. Actual v3 generation now exposed incorrect voice/positioning ordering and draft-versus-launch status ambiguity.

Decision: Operator communication is English; prospect copy remains French vous. The research providers remain explicitly Exa/Firecrawl via OmniRoute, with Perplexity's semantic sign-in failure recorded. Structured draft authoring uses configured noesis-write after noesis-research returned conversational announcements. Gateway response metadata reports composer-2.5; physical provider resolution is unverified. Advisor was attempted through Inference.ts and timed out after30s; no successful advisor verdict is claimed.

### Verified continuation — 5 October 2026

AX-ISC-4: Current CLI107tests and strict typecheck passed. Independent final acceptance12/12offlineprobes passed for uppercase/mixed HTTP export, real contact tuple preservation, official-shaped Annuaire headquarters/pagination mapping, NAF-only export hold, original archival receipt rejection and six brand-held plans. Earlier72/73matrix defects are resolved. A fresh official registry5company sample traversed discover→classify→export:5heldresearchcandidates,0import leads; department and region retained. No all-France coverage is claimed. See standalone agent docs/STEWARD-ACCEPTANCE.md and receipts/annuaire-electricity-20261005*.

AX-ISC-6: Current read-only ERP MCP SELECT1 succeeded again. The2October schema/aggregate audit remains dated; no individual contacts or writes were queried. Source template rationale for Kartezzi now matches furniture/joinery/decorative materials/integrated lighting, independently read back.

Refined: strategy must position before voice. Five v3attempts are terminal failed; missing dependencies, partial drafts and malformed JSON remain preserved. Current source repair is on the Build combo, and a fresh Perplexity probe is pending. No existing failed state is rewritten.

### Source repair and fresh attempts — 5 October 2026

AX-ISC-3/3.2: Source commitf75cb05 corrects positioning-before-voice and positioning's actual brand-foundation prerequisite. Parent repaired the new regression for macOSBash3.2 and checked both Bash interpreters; all6shellsuites and43Python tests pass. Complete andpartialdrafts keep operational_readinessheld, including localidentityfailure outputs. Freshv4fivebrandjobs are launched; no successful wave completion claimed yet. Buildtransport ran via noesis-build; finalphysical/sessionattribution is UNRESOLVED, not a verified vendor identity.

AX-ISC-4.1: RegionalextensionBuild18033 and parent118tests/typecheckpass, but independent15-caseprobe reported7provenance/contradiction failures. The independent report turn hit modelcapacity before delivering a durable report. Current residualBuild66317 addresses these exact defects. The extension remains unaccepted despite green fixture tests.

AX-ISC-6: Actual5OctoberExpleeGETs show project43522/heyzack.ai, dailybudget0, currentcampaigns0 and sends/replies/hotleads/spend0. Autopilot andautoreplysettingsareenabled; unchangedbyagent. Current sixbrandplans are allheld with onlyHeyZackprojectbound. Fresh PerplexityHTTP200stillSignups; fresh SymphonicsDNSfails, FirecrawlemptyHTTP200, exactExaquery0results. No providerconfigurationchange.

### Draft continuation checkpoint — 5 October 2026

AX-ISC-3/3.2: Actual v4 HeyZack state completed waves1,2 (eight validated upstream artifacts), then stopped before HTTP at content product-description:137166bytes exceeds128KiB. Kartezzi v4 stopped at competitor-analysis because each candidate lacked the required cited URL field. These failures remain intact. Axtech/Ecoled/Wave v4 are still running at the latest poll; no content completion is inferred. A scoped Build repair is implementing lossless JSON whitespace compaction and a separately attributed waves6 continuation from verified upstream outputs; the size guard, strict source validation and fresh-target guard remain mandatory.

AX-ISC-4.1: Residual regional Build66317 is still running. Earlier118fixture tests do not close the seven independent provenance/contradiction failures.

### Verified source and content attempts — 5 October 2026

AX-ISC-3/3.2: All four v4 evidenced-brand upstream runs completed waves1,2 then failed before HTTP at the unchanged128KiB guard (Hey137166,Ax145034,Eco135974,Wave152521bytes). Kartezzi v4 failed competitor URL validation. Reviewed Build33186 introduced lossless dependency/config/research JSON compaction and an opt-in separately attributed wave6 continuation. Parent strengthened nested identity, terminal-state and whole-checkpoint mutation checks, plus source state/receipt hashes;60Python tests and6shell suites pass. Four fresh v5 wave6 continuations verified/imported8sourceoutputs each under lock and launched actual inference; Kartezzi v5 starts fresh scoped waves1,2,6. Target state does not claim imported waves1,2. Build finalprovider attribution remainsUNRESOLVED.

AX-ISC-5: Independent editorial review examined34completed upstream drafts and found audit-policy language in customer pitches, unsupported competitor contrasts, unapproved identity proposals and113noncanonical source-pointer occurrences. `.planning/AXTECH-EDITORIAL-REVIEW-20261005.md` records exact pointers and required edits. V5 content direction/system prompt separates natural French customer offer/CTA from English review metadata; no editorial acceptance or finished content package is claimed yet.

AX-ISC-6: Two fresh bounded5October ERPSELECTs revalidated active ECOLED3,Wave4,Hey5,Kartezzi7 and separate test-only brand table; no private contacts or writes. Receipt in standalone campaign agent. Older2October schema/aggregates remain dated.
