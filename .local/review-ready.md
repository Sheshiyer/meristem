# Meristem source integration — ready for review

Date: 2026-09-27
Branch: `codex/reconcile-meristem-20260927`
Base: `origin/main` at `e95a8f2`
Runtime implementation commit: `bce27dd`
Status: local source implementation and verification complete. Parent owns curated PR/exact-head review and remote release; none was performed by this worktree task.

## Integrated scope

Both preserved checkpoint tips (`c46bda5` and `e3c92fd`) are ancestors. Identical Fitcheck/Iverif input files were deduplicated, both dated metric histories retained, FR-enriched spoke variants preserved, and upstream sourceable runner/directory-test behavior restored. Historical Cambium assets/report/audio/decks remain unmodified and explicitly qualified as an earlier exploration; the newer reviewed eleven-organ guide is a separate artifact.

Iverif's complete merged package includes config/brief, evidence ledger, draft channel plan, 36 historical wave receipts, three manifested assets and bilingual content. It is not missing its seed files. Draft channel evidence and proof-required public claims do not confer launch approval. The wiki is content/specification, without a package.json or Astro application config to build. Fixed the draft channel plan's actual landing.md source path. CEE-specific persona/competitor guidance now depends on evidenced domain, not French locale alone.

## Runtime symbols and behavior

- `execute_wave`: missing/empty required clusters fail; tracer and later failures propagate; reruns clear obsolete wave completion; content precedes social-growth in wave 6. The loop variable is local and array collection works on macOS Bash 3.2.
- `execute_spoke`, `generate_spoke_prompt`, `validate_spoke_output`: source-read, directory, wait and state failures propagate; only exactly one JSON object with matching skill and complete status can complete a spoke. Skipped/partial/missing/mismatched/malformed outputs fail.
- `json_update`, `state_update`, skill and wave state helpers: same-directory atomic replacement; failed jq or rename returns failure while preserving prior bytes and cleaning temporary output. Successful retries avoid duplicate entries and clear their own stale failure.
- `main`, `run_checkpoint`: wave/checkpoint errors propagate even in conditional calls; generated wave plans include both wave-6 clusters. No provider or brand run was executed.

## Observed validation

| Check | Result |
|---|---|
| `tests/runner-launch-directories.test.sh` | PASS under Bash 5.3 and `/bin/bash` 3.2 |
| `tests/runner-correctness.test.sh` | PASS under both; wave success/order, absent/empty clusters, tracer/later failure, six invalid-output variants, retries, failed reruns, prompt/state errors |
| `tests/runner-review-regressions.test.sh` | PASS under both; six additional scenarios: rename exit71+preservation+cleanup, real missing config, multi-document JSON, main exit72, single-spoke/local-variable scope, checkpoint exit73 |
| Shell syntax | Each runner, common, test and planning shell file checked individually with both interpreters |
| Brand JSON | 173 tracked files parsed; zero errors |
| Cambium manifest | 12/12 paths and SHA-256 hashes verified |
| Fitcheck manifest | 4/4 paths and SHA-256 hashes verified |
| Iverif manifest | 3/3 paths and SHA-256 hashes verified |
| Thoughtseed manifest | 44 references exist on this host; 24 external references and no supplied hashes, so not a portable verified release bundle |
| Whitespace | New runtime/tests/reconciliation docs clean against base; inherited archived artifact whitespace retained byte-for-byte |

All tests are synthetic and use temporary directories/stubbed waits and vault writes. No live models, NotebookLM generation, campaign sends, deployments or organ activation were exercised by tests. ShellCheck is unavailable. Checks validate coordinator semantics and package integrity, not all brand claims or generated content quality.

## Routing evidence

Heavy implementation was dispatched through `temperance-phase-dispatch.sh Build` on this sole-owned checkout. The selected seat was `cx/gpt-5.6-terra-max`; the terminal receipt reported `UNRESOLVED` / `missing-session-attribution`. Actual provider/model attribution is therefore unverified. Local code changes and independently rerun tests are the acceptance evidence. Raw routing logs/prompts stay ignored locally.

## Remaining gates and limitations

- Parent: curated final-tree PR commit, final secret/exact-head review, then authorized remote merge. Preserve checkpoint branches locally.
- Brand use: refresh mutable claim evidence and obtain owner approval before public campaign, regulated/commercial claims, canonical visual promotion, paid generation, NotebookLM publication or deployment.
- Iverif wiki: buildable application and deployment are future work, separate from its retained bilingual source content.
- Thoughtseed assets: 24 host-external references need an owner-approved portable packaging plan before claiming a fresh-clone release bundle.
- Stored Cambium package contains ~49 MiB audio plus ~14–15 MiB decks. Storage policy may need review; originals have not been deleted or silently excluded.
- Host-private `.superset/`, `.temperance/`, dynamic planner state and new execution traces are ignored. No host/private routing artifact is part of this review commit.
