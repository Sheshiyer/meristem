# Meristem reconciliation state

Updated: 2026-09-27
Branch: `codex/reconcile-meristem-20260927`
Base: `origin/main` at `e95a8f2`

## Current position

Both preserved branch histories are integrated: `codex/checkpoint-meristem-20260927` and `codex/iverif-fr-gtm-20260911`. Duplicate Fitcheck/Iverif files were identical; FR-enriched spoke variants and both dated metric append histories are retained. The upstream output-directory regression test remains present.

Status: source integration merged through PR #2 as `05b4853531b1fa1627252fe0a2ea66d347bc0845` on 2026-09-27. The merged tree exactly matches the reviewed prepared tree. All three runner test suites passed under Bash 5.3 and macOS Bash 3.2; shell syntax, brand JSON and available asset checksums verified. Do not launch generation from this state file.

## Readiness boundaries

- The current task tests only local deterministic behavior; it does not run providers, NotebookLM, campaigns, deployments or live organs.
- Cambium's generated Infinite Game package is a historical exploration, not canonical product identity. See its `PROVENANCE.md`.
- Iverif has a root brand config/brief, evidence ledger, draft channel plan, 36 historical wave receipts, three manifested assets and bilingual wiki content. Founder review of claim-bearing output, evidence freshness and a buildable wiki application remain outstanding. See `brands/iverif/README.md`.
- Thoughtseed's manifest depends on 24 external host asset references. They exist on this host; a fresh clone is not a self-contained brand release bundle.
- Source release is complete through the reviewed PR. Its merge does not confer brand publication, provider, campaign, or deployment authority.

## Next action

No source reconciliation or implementation test remains pending. Next, select a bounded brand task from roadmap step 5: claim/evidence review, Iverif wiki application packaging, or portable Thoughtseed assets. Public brand use still requires its specific claim, source-freshness and owner review gates. `.local/review-ready.md` remains the historical pre-merge source receipt.
