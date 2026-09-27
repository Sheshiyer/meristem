---
schema: thoughtseed.isa.seed.v1
seed: true
effort: extended
generated_by: temperance-hands ready
generated_at: 2026-08-22T10:59:02Z
project: meristem
---

## Problem

This repository is enrolled as a Temperance **Hands** execute root in Superset, but it lacked a project ISA. Acceptance was undefined, so ALGORITHM runs could not bind Ideal State Criteria.

## Vision

Operators open this repo in Superset, run Noesis ALGORITHM against a living ISA, and finish with falsifiable verification — not vibes.

## Out of Scope

Hermes/Phloem company-agent delivery. Non-git portfolio folders. Codex App as a Superset worker. Bulk-import of every Thoughtseed folder.

## Principles

- Acceptance lives in `ISA.md` (SoR); GSD `.planning/` plans work but does not replace ISC probes.
- Hands execute only on git roots via Superset + Claude (Mac plant).

## Constraints

- Execute lock: Superset + Claude via OmniRoute; never Codex App as worker.
- Do not enroll Hermes as a Hands workspace.

## Goal

Maintain a project ISA with at least Goal + Criteria (+ E3 sections) so every Hands ALGORITHM session can OBSERVE → VERIFY against named ISCs.

## Criteria

- [ ] ISC-1: `ISA.md` exists at repo root and contains `## Goal` and `## Criteria`.
- [ ] ISC-2: `.temperance/project.json` has `active_planner` set to `isa` or `gsd`.
- [ ] ISC-3: Superset local.db lists this repo path as a project with ≥1 workspace (`temperance-superset-sync --check`).
- [ ] ISC-4: Anti: no Hermes/Phloem agent job is launched from this Superset workspace.

## Test Strategy

| isc | type | check | threshold | tool |
|---|---|---|---|---|
| ISC-1 | file | ISA.md sections | present | rg/read |
| ISC-2 | file | active_planner | isa\|gsd | jq |
| ISC-3 | db | local.db project row | 1 | sqlite3 / temperance-superset-sync |
| ISC-4 | policy | hermes path absent | 0 | temperance-hands / doctor |

## Features

| name | description | satisfies | depends_on | parallelizable |
|---|---|---|---|---|
| seed-isa | Initial ISA seed for Hands readiness | [ISC-1, ISC-4] | [] | false |
| planner-pin | Pin active_planner for Manifest/GSD non-fight | [ISC-2] | [seed-isa] | false |

## Decisions

- 2026-08-22T10:59:02Z: `refined:` seeded ISA via `temperance-hands ready` — deepen via ISA Interview before treating as full E3 product doctrine.

## Changelog

- conjectured: Hands repos can run ALGORITHM without a project ISA
- refuted by: Manifest/GSD fight + missing acceptance SoR on unset planners
- learned: seed ISA + active_planner before Execute
- criterion now: ISC-1..ISC-4

## Verification

- pending: fill after first Hands ALGORITHM verify pass
