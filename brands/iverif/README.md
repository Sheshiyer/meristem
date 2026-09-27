# Iverif FR GTM package and readiness

The merged tree contains both the imported `inputs/v1/` archive and the later September 11 brand package: root config/brief, evidence ledger, draft channel plan, three source assets with a manifest, 36 wave output receipts, and bilingual FR/EN wiki content.

`inputs/v1/` remains historical source material. Its machine-generated approval labels are provenance, not current founder approval. The later evidence ledger and explicit claim boundaries take precedence for downstream copy.

## What exists

- `brand-config.yaml` and `BRAND-BRIEF.md`: France/FR language and product positioning inputs.
- `research/EVIDENCE-LEDGER.md`: dated observations, hypotheses and prohibited claims; several competitor confirmations and public outcome claims remain unproved.
- `research/channel-plan.md`: draft research, explicitly not a live media plan or budget authority.
- `.brandmint/outputs/`: 36 historical generation receipts; state records waves 1–7 complete. Reconciliation does not rerun or semantically reapprove every output.
- `.brandmint/asset-manifest.json`: three existing product-owned source assets with SHA-256 hashes.
- `wiki/src/content/docs/{fr,en}/` and `wiki/DOWNSTREAM-HANDOFF.md`: bilingual content/specification package. No `package.json` or Astro configuration exists here, so this is not a verified buildable/deployed site.

## Remaining boundaries

Fresh source verification and founder review are required before public use of mutable regulatory, competitor, operational or commercial claims. The channel plan is draft; an existing path is not an approval receipt. A future wiki application build is separate from the retained content package. Paid generation, NotebookLM publication, campaign sends, deployment and runtime admission require their own explicit authority.

No new brand generation or live operation was performed by reconciliation. The runner tests use synthetic fixtures only.
