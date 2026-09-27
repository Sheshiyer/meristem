# Meristem reconciliation state

Updated: 2026-09-27
Branch: `codex/reconcile-meristem-20260927`
Base: `origin/main` at `e95a8f2`

## Current position

Both preserved branch histories are integrated: `codex/checkpoint-meristem-20260927` and `codex/iverif-fr-gtm-20260911`. Duplicate Fitcheck/Iverif files were identical; FR-enriched spoke variants and both dated metric append histories are retained. The upstream output-directory regression test remains present.

Status: source implementation and local verification complete; ready for parent review of a curated PR. All three runner test suites passed under Bash 5.3 and macOS Bash 3.2; shell syntax, brand JSON and available asset checksums verified. Do not launch generation from this state file.

## Readiness boundaries

- The current task tests only local deterministic behavior; it does not run providers, NotebookLM, campaigns, deployments or live organs.
- Cambium's generated Infinite Game package is a historical exploration, not canonical product identity. See its `PROVENANCE.md`.
- Iverif has a root brand config/brief, evidence ledger, draft channel plan, 36 historical wave receipts, three manifested assets and bilingual wiki content. Founder review of claim-bearing output, evidence freshness and a buildable wiki application remain outstanding. See `brands/iverif/README.md`.
- Thoughtseed's manifest depends on 24 external host asset references. They exist on this host; a fresh clone is not a self-contained brand release bundle.
- The parent integration review owns push/PR/main-merge decisions. No remote update is claimed here.

## Next action

Parent workflow: review the final-tree diff and `.local/review-ready.md`, repeat secret/exact-head checks on the curated PR commit, then follow the authorized PR/merge gate. No implementation test remains pending in this checkout. Any subsequent public brand use still requires its specific claim, source-freshness and owner review gates.
