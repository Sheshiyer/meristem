# Fitcheck Brandmint relocation and R2 status

## Local relocation

On 2026-08-10, two root-local Cambium drafts were moved into the Fitcheck
Meristem sidecar at `legacy-unvalidated/cambium-root-2026-08-10/`. Their
checksums and quarantine status are recorded in that directory's `README.md`.
No draft remains in Cambium's `.brandmint/` or `.brandmint-outputs/` roots.

## Canonical project map

Fitcheck is already one Thoughtseed WorkObject: `sapling:fitcheck`. Its product
source repository is `Sheshiyer/fitcheck-landing`; Meristem is the standalone
brand-system organ, not a competing Fitcheck product root.

## Existing R2 evidence

The existing immutable mapping receipt is
`pmr_9de251ce89564f07f3e4c510`, read-back verified at:

`portfolio/thoughtseed/workobjects/sapling:fitcheck/mapping/pmr_9de251ce89564f07f3e4c510.json`

It proves WorkObject-to-repository identity. It is not a bulk synchronisation
of Brandmint source files or generated NotebookLM artifacts.

## Next authorised boundary

Before a new R2 artifact-sync write, define and approve an exact manifest
(objects, checksums, retention, reader access, and immutable key prefix). Until
then, this sidecar remains the local source of record and the existing mapping
receipt remains unchanged.
