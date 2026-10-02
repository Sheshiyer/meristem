# Axtech integration source audit — 2 October 2026

Status: **source review complete; connected-system acceptance not established**.
Scope: existing HeyZack estimate applications and configured research agents/transport.
This audit made no provider calls, credential reads, application changes, external writes or runtime changes.
The only deliverable mutation is this document. Existing dirty application files were preserved.

## Evidence and authority

- Source inspected: `heyzack/esitmate-backend`, `heyzack/estimate-lite`, `heyzack/heyzack-estimate/estimate-web`; indexed research skill paths, configured researcher definitions and the OmniRoute evidence helper.
- Source existence does not demonstrate a deployed route, provider authentication, delivered email, completed call or ERP record.
- Synthetic and historical checks below are attributed to repository documents; they were not rerun in this audit.
- Current Meristem acceptance belongs to [ISA.md](/Volumes/madara/2026/Projects/thoughtseed/meristem/ISA.md); continuation belongs to `.planning/STATE.md`, per [AGENTS.md:330](/Volumes/madara/2026/Projects/thoughtseed/meristem/AGENTS.md:330).
- Per-brand execution must use the shell runner and its wave receipts. This audit does not claim any brand's Meristem run complete. See [AGENTS.md:3](/Volumes/madara/2026/Projects/thoughtseed/meristem/AGENTS.md:3).

## Six-brand identity boundary

These six URLs were supplied by the operator. They are research slots, not proof of legal ownership, current service coverage, product readiness or an authorized sender.

| Slot | Supplied domain | Identity evidence still required |
| --- | --- | --- |
| HeyZack | `https://heyzack.ai/` | Legal entity, Axtech relationship, B2B offer, service areas and approved claims |
| Kartezzi | `https://www.kartezzi.com/` | Legal entity, Axtech relationship, offer, audience and sender |
| ECOLED Europe | `https://ecoled-europe.com/` | Legal entity, Axtech relationship, catalogue, service areas and sender |
| Wave Concept | `https://www.wave-concept.com/` | Legal entity, Axtech relationship, offer, audience and sender |
| Axtech | `https://www.axtech.fr/` | Group/legal-entity map, SIREN/SIRET, contracting entity and portfolio scope |
| Symphonics URL slot | `http://symphonics.heyzack.ai/` | Current domain content, offer identity, legal entity and relationship to HeyZack |

The supplied ESAC/Airbnb package is a proposed offer requiring its own evidence; this audit does not map ESAC to a legal entity or domain by inference.
The current campaign priority is B2B MEP: electricians, plumbers, HVAC/climatisation, architects, fluid-engineering bureaux d'études and construction-engineering bureaux d'études.
Use independent trade tags; a plumbing/HVAC common group is justified only when the same legal entity demonstrably performs both. Retain artisans, sole traders and all company sizes.

## Current source flow versus historical paths

The authoritative current product map is [product-map.md:1](/Volumes/madara/2026/Projects/thoughtseed/heyzack/estimate-lite/docs/product-map.md:1).

| Path | Implemented behavior | Readiness conclusion |
| --- | --- | --- |
| Lite `pdf_only`, default | Same-origin `POST /api/lite/intake` renders an unpriced French/English PDF locally; no saved lead, email or call | Implemented source; deployed mode not probed |
| Lite development `pack_v3` | Proxy forwards v3 to shared backend; Shopify FR/EUR snapshot, private S3 PDF, PostgreSQL lead/snapshot, signed download | Implemented source; live dependency/configuration acceptance absent from this audit |
| Historical Lite `priced` | Proxy to `estimate-web`; ERP pricing policy and Customer Lead, private R2 PDF | Current documents classify this as inactive |
| Historical Lite callback | Saved ERP lead/PDF verification, durable R2 callback claim, outbound Vapi call | Real dispatch code; only enabled by inactive `priced` mode |
| Full estimator | Long wizard to shared backend `POST /api/estimate`; legacy persistence/PDF/Brevo path | Separate from Lite; no live round-trip verified here |

Current mode separation: [integrations.md:3](/Volumes/madara/2026/Projects/thoughtseed/heyzack/estimate-lite/docs/integrations.md:3).
The Lite intake mode branch is [route.ts:77](/Volumes/madara/2026/Projects/thoughtseed/heyzack/estimate-lite/app/api/lite/intake/route.ts:77).
The Lite callback mode gate is [route.ts:74](/Volumes/madara/2026/Projects/thoughtseed/heyzack/estimate-lite/app/api/lite/callback/route.ts:74).

### Development pack contract

- Browser request: `heyzack.lite.preliminary-estimate.v3`, source `estimate-lite`, locale, customer name/email/address and validated residential answers; UUID `Idempotency-Key`.
- BFF forwards to `POST /api/lite/preliminary-estimates` with a server-only bearer token. Backend route validates authentication, JSON, UUID and submission; new result 201, replay 200.
- Public response: estimate UUID, `preliminary_estimate`, locale, policy and Shopify snapshot references, EUR integer-cent pack total and tax status, one gateway plus opening sensors, unpriced suggestions and private PDF download expiring within 15 minutes.
- No per-item money fields, ERP, checkout or Vapi in this pack contract. Opening quantity is one assumed entrance plus submitted opening counts.
- PostgreSQL transaction/advisory lock serializes environment/request key, rejects changed-body reuse, and atomically writes lead plus immutable audit snapshot.
- Public pack amounts require real TTC verification/approval; `pdf_only` remains the documented release fallback until acceptance.

Pointers: [contract.ts:3](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/lite/contract.ts:3), [routes.ts:14](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/lite/routes.ts:14), [service.ts:57](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/lite/service.ts:57), [repository.ts:26](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/lite/repository.ts:26), [pack-v3.md:9](/Volumes/madara/2026/Projects/thoughtseed/heyzack/estimate-lite/docs/pack-v3.md:9).

### ERP and CRM source contracts

- Historical ERP pricing defaults to `POST /api/method/heyzack.lite.resolve_preliminary_estimate`; request includes policy key, contract version, catalog snapshot, service areas, opening quantity, locale and answers.
- ERP pricing response is validated against the catalogue and customer locale. Lead lookup/upsert uses `/api/resource/Customer%20Lead`; metadata defaults to `lite_estimate_metadata`.
- Separate `POST /api/erp` maps full-estimate fields to `/api/resource/Customer Lead`. It reads `ZOHO_CLIENT_ID` and `ZOHO_CLIENT_SECRET` as ERP Basic-auth credentials despite its error naming ERP credentials. Reconcile this binding before reuse.
- Separate `POST /api/zoho/add-lead` refreshes OAuth and posts name/email/phone/company/source/address to `${ZOHO_API_DOMAIN}/crm/v2/Leads`.
- No canonical ERP-versus-Zoho ownership, synchronization or campaign-event mapping was established by these separate routes.

Pointers: [erp.ts:71](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/lib/lite-estimate/erp.ts:71), [ERP config:89](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/lib/lite-estimate/config.ts:89), [legacy ERP route:4](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/app/api/erp/route.ts:4), [Zoho route:38](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/app/api/zoho/add-lead/route.ts:38).

### Vapi source behavior and blockers

- Shared backend mounts `/api/vapi`: webhook, knowledge-base search, session management and tool routes.
- `scheduleCallback` returns `scheduled:true` without scheduling; `sendBrochure` stores an email and returns `sent:true` without sending.
- Conversation state is an in-memory `Map` with six-hour TTL; durability across restarts/replicas is not provided by this implementation.
- `verifyVapiBearerToken` skips authentication if its configured token is absent. Middleware covers webhook and KB search; generic/action tool routes and session routes do not use it.
- Distinct historical callback contract is `heyzack.lite.callback.v2`: estimate UUID, `+33` phone, explicit true consent, `estimate-call-v1`, locale. It verifies saved lead/PDF before durable claim and `POST https://api.vapi.ai/call`.
- Timeout/malformed dispatch remains pending to prevent duplicate dialing. Returned `queued`/call ID does not demonstrate completion, terminal call-event reconciliation or CRM writeback.

Pointers: [stub handlers:1094](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/vapi/vapiController.ts:1094), [session state:35](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/vapi/vapiController.ts:35), [auth bypass:13](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/vapi/vapiAuth.ts:13), [routes:22](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/vapi/vapiRoutes.ts:22), [callback contract:4](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/lib/lite-callback/contracts.ts:4), [callback service:40](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/lib/lite-callback/service.ts:40), [outbound dispatch:31](/Volumes/madara/2026/Projects/thoughtseed/heyzack/heyzack-estimate/estimate-web/lib/lite-callback/vapi.ts:31).

## Research agents and OmniRoute transport

Configured `PerplexityResearcher` definitions exist for Codex and Claude. Their named mandatory startup-context and Perplexity workflow files were absent at all four referenced paths during this audit.

- Codex references: [PerplexityResearcher.toml:49](/Users/sheshnarayaniyer/.codex/agents/PerplexityResearcher.toml:49) and [workflow:143](/Users/sheshnarayaniyer/.codex/agents/PerplexityResearcher.toml:143).
- Claude references: [PerplexityResearcher.md:77](/Users/sheshnarayaniyer/.claude/agents/PerplexityResearcher.md:77) and [workflow:171](/Users/sheshnarayaniyer/.claude/agents/PerplexityResearcher.md:171).
- Canonical indexed Research spoke also lacks `Workflows/PerplexityResearch.md`; default StandardResearch dispatches Claude/Gemini, not Perplexity: [workflow:35](/Users/sheshnarayaniyer/.agents/skill-clusters/skills/research/Workflows/StandardResearch.md:35).
- Active `exa-search` and `deep-research` spokes describe MCP tools, so installation alone does not prove OmniRoute-backed calls: [Exa requirements:26](/Users/sheshnarayaniyer/.agents/skill-clusters/skills/exa-search/SKILL.md:26), [Deep Research requirements:25](/Users/sheshnarayaniyer/.agents/skill-clusters/skills/deep-research/SKILL.md:25).
- Exposed tool metadata includes Firecrawl connector tools; no exposed Exa or Perplexity MCP tools were found. This does not determine gateway availability.
- CodeGraph was queried first for `.agents` structure. Returned loader paths were missing on disk; the graph's structural results do not override current file evidence.

The host source declares the requested evidence transport in [phase-combo-map.json:368](/Users/sheshnarayaniyer/.temperance_engine/router/phase-combo-map.json:368):

| Capability | Declared route/provider |
| --- | --- |
| Search | `POST http://127.0.0.1:20128/v1/search`; `brave-search`, `exa-search` |
| Source fetch | `POST http://127.0.0.1:20128/v1/web/fetch`; `firecrawl`, `jina-reader` |
| Grounded chat | `perplexity-web/pplx-sonar` or `openrouter/perplexity/sonar-pro`; combo `noesis-research` |
| Separate Perplexity search | Explicitly marked missing/broken; Search API key differs from web session |

Helper source: [temperance-search-evidence.sh:1](/Users/sheshnarayaniyer/.temperance_engine/router/temperance-search-evidence.sh:1).
The helper tries Brave first and Exa on failure; a generic successful search is not evidence that Exa ran. Fetch tries Firecrawl then Jina.
Required research receipts must identify requested and resolved provider, model where applicable, query/source URL, timestamp, artifact hash, citations and failures/fallbacks.
No provider availability or resolved model was tested by this audit.

## Missing durable acquisition and event contracts

Literal API/identity searches found no Explee API, campaign ID mapping, campaign webhook handling or social publishing endpoints in the scoped application sources.
The current lead schema and hardcoded Lite source do not establish the following shared records:

| Required record | Missing contract/evidence |
| --- | --- |
| Brand/legal entity | Brand ID, domain, contracting entity, SIREN/SIRET and verified parent relationship; approved offer/sender version |
| Prospect organization | Durable SIREN/entity ID, SIRET establishment IDs, corroborated multi-trade tags, business size and legal form, region/departement and source provenance |
| Contact | Durable contact ID, organization/role/channel binding, address evidence, provenance and eligibility; deduplication across brands/trades |
| Campaign | Brand + offer + MEP segment + region + language, draft/version/approval, external Explee project/campaign IDs |
| Suppression | Contact/channel/global-or-brand scope, reason/source/time, opt-out/bounce state, pre-send check and propagation to every channel |
| Event envelope | Stable event ID/type/schema version, source/time, correlation/idempotency key, brand/org/contact/campaign IDs, external references, sanitized payload and replay state |
| Delivery lifecycle | Discovery/import → qualified → approved → dispatched → delivered/bounced/replied → qualified handoff → ERP/call/advisor outcome |
| Social lifecycle | Approved Meristem asset/version → destination account/platform adapter → queued/published receipt → attributable response |

Schema pointers: [lead table:116](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/db/schema.ts:116), [Lite source literal:57](/Volumes/madara/2026/Projects/thoughtseed/heyzack/esitmate-backend/src/lite/contract.ts:57).
These are required design records, not a claim that the ERP can accept them unchanged.

## Synthetic and historical evidence status

[pack-v3.md:implementation verification](/Volumes/madara/2026/Projects/thoughtseed/heyzack/estimate-lite/docs/pack-v3.md:49) records unit/browser fixtures, disposable local PostgreSQL concurrency/rollback tests and private synthetic S3 PDFs.
Those checks establish their bounded fixtures/storage behavior, not live Shopify prices, an accepted deployed pack, a delivered campaign or a Vapi conversation.
The same document's September 26/29 notes record database-host/configuration problems and possible route 404 pending deployment. They are historical observations, not freshly confirmed failures.
The current source still documents public Lite as unpriced until development/TTC acceptance. This audit did not inspect hosting secrets or verify current deployed settings.

## Required acceptance probes before connected-system claims

| Lane | Probe and required evidence |
| --- | --- |
| Research | Explicitly resolve Perplexity, Exa and Firecrawl through the intended OmniRoute paths; save citations and honest failure/fallback receipts for each brand |
| Brand research | Validate domain/legal identity, offers, assets, service regions and claim evidence; retain unresolved facts and approved source boundaries in separate per-brand Meristem inputs |
| Meristem | Runner status, per-wave output/schema receipts, tracer assumptions, source origins, manifest existence/path validation and current ISA acceptance; generated copy remains a draft until approved |
| Pack backend | Health configured with variable names only; unauthenticated estimate POST 401; isolated FR/EN real pricing/persistence/download, changed-key/racing-key rejection, S3 unsigned denial/expiry and actual TTC approval |
| ERP/CRM | Select exact non-production target/doctype; verify schema and credentials binding; one idempotent contact/organization upsert, brand/trade/region attribution, replay and fail-visible behavior |
| Explee | Verify documented API compatibility, exact account/project/campaign bindings and budget/autopilot state; test duplicate prevention, suppression and reply event ingestion in an isolated authorized lane |
| Vapi | Reject missing/invalid auth; persist session and consent; verify call dispatch, terminal event, conversation summary, single CRM writeback and timeout/replay without a second call |
| Social | Verify account identity, approved asset/version and destination contract; validate draft/preview before a separately authorized publication receipt |
| Complete flow | One attributable test record through research → segment → draft → approval → campaign event → ERP → consented call/advisor → durable outcome; capture all correlated receipts and failure paths |

No campaign activation, social publication, outbound call or bulk contact action is authorized by completion of this source audit.

## Preserved local source state at audit

- `esitmate-backend`: `feat/lite-brand-pdf`, HEAD `25e1f33e8ca7ab2bf71b9cfbdcfd069152990191`; pre-existing modified brand PDF/pack proposal/recommendations/two tests, untracked `output/`.
- `estimate-lite`: `main`, HEAD `75cbb3ade4a574d09e422557770f4169cf6e4565`; pre-existing modified brand PDF, untracked `.codex/` and `.planning/HANDOFF.json`.
- `heyzack-estimate/estimate-web`: Git did not find a repository at this path or its ancestors before the mount boundary.
- No application edits or state cleanup were performed. Integration completion remains unproven.
