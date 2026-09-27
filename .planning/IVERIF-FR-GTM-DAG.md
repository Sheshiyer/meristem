# Iverif FR GTM historical execution plan

> Status as of reconciliation, 2026-09-27: archived plan, not executable approval. Root config/brief, evidence ledger, draft channel plan, assets/manifest, 36 wave receipts and bilingual wiki content are now present alongside imported `inputs/v1/`. Public claim approval, evidence refresh and a buildable wiki application remain outstanding. The "locked decisions" below record the earlier planning session; they do not authorize generation, admitted flips, publication or sends in this reconciliation. See `brands/iverif/README.md` and current roadmap.

## Original execution DAG (2026-09-11)

## Locked decisions
- Phase 0: accept copy+checksum as done; amend MANIFEST wording only
- Wave production: full `bm.sh` launch with agent writers filling `.brandmint/outputs/*.json`
- Phase 4(c): attempt admitted flip in packet/golden-path
- Isolation: feature worktrees `codex/iverif-fr-gtm-20260911`

## Meristem ownership (this worktree)
1. Amend nothing critical in Phase 0 here (iverif worktree owns MANIFEST amend)
2. Schema: examples/brand-config.yaml += market.region/language (+ domains optional)
3. Brand seed: brands/iverif/{brand-config.yaml,BRAND-BRIEF.md,research/EVIDENCE-LEDGER.md,assets}
4. Spoke patches BEFORE waves:
   - foundation competitor-analysis + buyer-persona (FR gaps)
   - content spokes bilingual + explee format on ad-creative
   - social-growth short-form-hook-generator bilingual; add channel-plan spoke OR research/channel-plan.md
   - synthesis 5 spokes bilingual/i18n
5. Run waves 1-6 then 7 with agent writers
6. Verify cluster artifacts + DOWNSTREAM-HANDOFF

## Acceptance aliases (plan name → real artifact)
- EVIDENCE-LEDGER.md → brands/iverif/research/EVIDENCE-LEDGER.md (seeded input + W1 enrichment)
- competitive-landscape/category-map → .brandmint/outputs/competitor-analysis.json (+ wiki later)
- MDS / voice / positioning → messaging-framework.json, voice-and-tone.json, product-positioning.json + wiki/MDS.md
- logo-system/color-tokens → logo-concept.json, color-palette.json
- shotlist/system → photography/illustration spoke JSONs
