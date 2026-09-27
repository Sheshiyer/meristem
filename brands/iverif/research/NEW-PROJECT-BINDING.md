# New Explee project binding — iverif.fr

**Bound at:** 2026-09-11T13:44:19.486579+00:00  
**New project ID:** `35674`  
**Domain:** `iverif.fr`  
**Old project:** `16763` (archived / not in active list)

## Live GET snapshot
- Spend/sends so far: **$0 / 0 emails** (clean stats denominator — good)
- Project daily budget: **$10** (operator managing in UI)
- Autopilot: **ON**
- Auto-reply: **ON** (delay 1440m)
- Campaigns present (6), all `listening` / mostly `user_pause`, **$10** daily_limit each:
  - 159032 Energy EPC Firms
  - 159033 Subsidy Aggregators
  - 159034 Energy Consultants
  - 159035 Utility Providers
  - 159036 Public Agencies
  - 159037 Energy Lenders

## Critical warning
These campaign **names match the archived money-guzzler set**. Even with zero sends, do **not** treat them as the FR CEE délégataire strategy. Prefer creating a **new FR-first campaign** (or retarget carefully) rather than restarting “Public Agencies”.

## Immediate operator checklist (UI)
1. Turn **Autopilot OFF**
2. Turn **Auto-reply OFF**
3. Keep campaigns paused / budget controlled until FR ICP is rewritten
4. Optional: archive/delete the six clone campaigns if they were only scaffolding
5. Create one campaign aimed at **FR délégataire / CEE ops (Marie Durand)**, language `fr`

## Cambium follow-ups (code, separate PR)
- Update `workers/quests/src/iverif-grounding.ts` observe binding from 16763/45711 → 35674/(new campaign id)
- Update adapter docs + draft package `project_id`
- Keep 16763 learning pack as historical corpus only

## Hot queue from old project
Dropped / do-not-send (unchanged).
