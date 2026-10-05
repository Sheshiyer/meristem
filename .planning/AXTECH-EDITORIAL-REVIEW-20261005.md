# Axtech portfolio — editorial review, 5 October 2026

Verdict: **revise before using these upstream drafts in prospect content**. The actual coordinator completed foundation and strategy draft waves for four brands; this is execution evidence, not editorial or launch acceptance. Kartezzi has only two completed foundation outputs. No completed wave 6 content package exists in the inspected attempt.

This was a bounded, read-only audit of the five current v4 draft folders against each brand's `research/DOSSIER.md` and `research/evidence.json`. No provider, external application, private ERP record, campaign, publication or runtime-state mutation was used. The reviewer writes only this report. Other shared edits are preserved.

## Inspected sources and actual state

Repository root: `/Volumes/madara/2026/Projects/thoughtseed/meristem`.

Draft root: `.local/axtech-portfolio-20261002/authoring-v4-20261005/<brand>/.brandmint/outputs/`.

Research root: `brands/axtech-portfolio-20261002/<brand>/research/`.

| Brand | Completed JSON drafts inspected | Actual state | Content status |
|---|---:|---|---|
| HeyZack | 8 | Waves 1 and 2 complete; `product-description` failed in wave 6 | No completed content/social package |
| Axtech | 8 | Waves 1 and 2 complete; `product-description` failed in wave 6 | No completed content/social package |
| Ecoled Europe | 8 | Waves 1 and 2 complete; `product-description` failed in wave 6 | No completed content/social package |
| Wave Concept | 8 | Waves 1 and 2 complete; `product-description` failed in wave 6 | No completed content/social package |
| Kartezzi | 2 | Foundation and persona complete; competitor-analysis failed; no wave complete | No complete strategy/content package |

The four wave 6 product-description files and Kartezzi competitor-analysis file are partial envelopes. They are not missing silently and are not accepted deliverables. Symphonics is outside this draft audit and remains an essential-identity/source hold; no counterpart domain is substituted.

Findings below use brand, file and JSON pointer relative to the draft root. They concern generated wording, not modifications to accepted source identities.

## Required edits

### 1. Operational audit language has become prospect-facing positioning

The source dossiers correctly keep provenance and launch gaps explicit. Several generated fields transplant that internal audit into the customer's message, or turn the project's caution into the brand's principal benefit.

| Brand/file | Pointer and concrete example | Required change |
|---|---|---|
| HeyZack `brand-story.json` | `/data/story_formats/paragraph`: “Pas de ROI ni conformité CEE promis ici ; brouillon interne, activation tenue.” | Keep this in review metadata. A prospect paragraph should describe relevant building-control needs and propose a technical exchange. |
| HeyZack `voice-and-tone.json` | `/data/example_phrases/3/use`: “la couverture de prestation terrain n'est pas établie dans ce dossier” | Ask for the project department and confirm service feasibility individually. Do not put a dossier-status explanation in the message. |
| HeyZack `messaging-framework.json` | `/data/elevator_pitch/full`: “nous séparons déclarations du site et capacités à confirmer” and “le catalogue reste à rapprocher” | Lead with lighting, heating/climate, energy or access needs. Compatibility confirmation is a concrete scoping step, not a claim that internal integration work is a differentiated product. |
| Axtech `messaging-framework.json` | `/data/elevator_pitch/full`: “l'offre documentée correspond” and “marque routée” | Use plain customer language: understand the professional's requirement and put them in contact with the relevant team. The software routing model remains internal. |
| Ecoled `brand-story.json` | `/data/story_formats/paragraph`: “hypothèse interne alignée sur l’offre officielle” and “brouillon interne uniquement” | Describe professional LED lighting and lighting studies; ask for usage and plans. Keep the strategic hypothesis and public-claim approval in separate metadata. |
| Ecoled `messaging-framework.json` | `/data/elevator_pitch/components/proof`: `approved_for_public_claim=false` | This is an approval field, not a proof sentence for a reader. Preserve it in evidence metadata only. |
| Wave `voice-and-tone.json` | `/data/example_phrases/2/use`: “fiches et conditions alignées à votre ERP avant diffusion”; `/data/example_phrases/3/use`: “tout flux automatisé ou marketplace reste à prouver” | Lead with the reseller's mobile-accessory assortment. Do not imply a customer ERP reconciliation or marketplace connector. Confirm product references and commercial conditions only when relevant. |
| Wave `messaging-framework.json` | `/data/value_pillars/3/supporting_copy`: “hors activation MEP courante” and “CHR hérité”; pillar 4 references reconciliation ERP | Keep category exclusions and stale-metadata diagnostics in the internal brief. A retail buyer needs the actual mobile-accessory scope. |

Do not repair this by deleting caveats from the evidence record or by promoting unsupported claims. Separate `prospect_copy` from `review_notes`, `claim_refs`, `uncertainties`, `operational_readiness` and `approval_status`. Copy may be internally complete while launch remains held. Essential missing identity, relevant sources or actual required content remains partial.

### 2. Competitor absence-of-evidence has become a negative comparative claim

The research labels the named companies comparison candidates, with competitive overlap and weaknesses unproved. The generated contrasts overstate what limited pages establish.

| Brand/file | Pointer and concrete example | Required change |
|---|---|---|
| HeyZack `value-proposition.json` | `/data/statements/one_sentence`: “contrairement aux intégrateurs Loxone qui promettent l'expertise avant la compatibilité” | Remove this assertion. No reviewed evidence establishes the order of another company's qualification, or that it promises expertise irresponsibly. |
| HeyZack `competitor-analysis.json` | `/data/positioning_statement`: contrasts integrators anchored on Loxone or one product pillar with HeyZack qualification | Retain factual descriptions as internal comparisons with exact source attribution. Qualification is a proposed HeyZack approach, not an evidenced exclusive advantage. |
| Axtech `value-proposition.json` | `/data/statements/one_sentence`: “Rexel ou Sonepar qui vendent un catalogue MEP indifférencié” | Remove the characterization. The dossiers document suppliers' categories and technical accompaniment, not an undifferentiated customer service. |
| Axtech `competitor-analysis.json` | `/data/positioning_statement`: “aucun comparateur du dossier ne couvre de bout en bout” | A missing full-portfolio comparison cannot prove market whitespace. State only Axtech's published brand portfolio and the proposed intake approach. |
| Ecoled `messaging-framework.json` | `/data/elevator_pitch/full`: “Contrairement aux portails catalogue des grands fabricants” | Remove the general contrast. TRILUX, Signify and GOSPI may offer project support; the dossier does not prove Ecoled alone starts from a specification. |
| Wave `value-proposition.json` | `/data/statements/one_sentence`: “Bigben et Hama sans preuve catalogue alignée ERP” | The audit did not inspect the companies' operating systems. Remove this claim entirely. |
| Wave `brand-story.json` | `/data/origin_story/full_narrative`: “peu offrent une lecture assortiment aussi explicitement découpée” | Remove the market-wide generalization. The existence of Wave's category navigation is a first-party fact, not unique superiority. |
| Wave `competitor-analysis.json` | `/data/competitors/0/type` and `/1/type`: `direct` | Change to comparison candidate or a clearly marked proposed relationship. Current sources establish relevant category overlap; they do not establish direct competition. |

Do not place unknowns in `weaknesses` or `complaints` as if they were findings. A missing review corpus belongs in `unknowns`. Do not manufacture criticisms to satisfy a template that asks for weaknesses.

### 3. New taglines, brand essence and values are proposals

`messaging-framework.json` selects new taglines: HeyZack “Qualifiez avant de promettre”, Axtech “Qualifiez avant le catalogue”, Ecoled “Lumière ingéniérée, projet par projet”, Wave “Assortir par univers”. Foundation also creates brand essence and named values; Kartezzi uses “Matières sur plan”. These are authored proposals rather than source-confirmed or owner-approved identity.

The draft-only envelope does not establish approval for each selected phrase. Future content must preserve existing brand identities and label proposed taglines as `proposed`, with approval pending. Do not replace an accepted slogan/logo/system with these variants. Several proposals also encode internal review policy rather than a customer benefit. Ecoled's “ingéniérée” is awkward French; use natural lighting vocabulary in body copy without silently adopting a replacement slogan.

No invented founding date or named founder is asserted in the inspected origin metadata. However, fictional customer scenes and invented persona biography are not historical origin evidence. Keep them labelled illustrative and avoid presenting them as actual clients or case studies.

### 4. Canonical evidence references resolve, but reference namespaces are mixed

The inspected canonical claim and source identifiers resolve against each current evidence ledger. A second check of every explicit `source_ids`, `claim_ids` and `evidence_ids` array found noncanonical addresses mixed into the source-ID field:

| Brand | Canonical reference occurrences | Noncanonical reference occurrences |
|---|---:|---:|
| HeyZack | 68 | 28 |
| Axtech | 89 | 27 |
| Ecoled | 88 | 37 |
| Wave | 120 | 21 |
| Kartezzi | 8 | 0 |

These are occurrence counts, not distinct-source counts. The 113 noncanonical occurrences include real upstream/local concepts, not necessarily invented publications; they simply do not resolve as ledger IDs.

Examples: HeyZack foundation `/data/evidence/5/source_ids/0` is `evidence.json:positioning`; HeyZack value proposition includes `competitor-analysis:COMP-01`; Axtech foundation includes `segmentation_hypotheses`; Ecoled messaging includes `value-proposition.json`; Wave story includes `upstream:buyer-persona.json`.

Use only registered source IDs in `source_ids`, registered claim IDs in `claim_ids`, and separately typed upstream references containing an actual artifact path, JSON pointer and content hash. A generated upstream opinion is not a public source or independent corroboration. Preserve `strategic_hypothesis` classification through downstream use; do not cite HZ-H1, AX-H1, EL-H1, WV-H1 or KZ-H1 as proof of operational service.

### 5. Brand and trade fit is mostly preserved but the group pitch is too broad

HeyZack's relevant electrical, HVAC and fluid/electrical prescription roles are recognizable. Plumbing-only and structural BET need a documented control/coordination need. Ecoled correctly centers professional LED and lighting studies: fluid BET is relevant only with lighting/electrical or evidenced coordination responsibility, not simply because it is MEP. Kartezzi correctly addresses architects/interior specifiers, joinery and fitout; LED integrated into furniture is not general electrical contracting.

Wave is correctly framed as mobile accessories rather than MEP or inherited CHR. However, Axtech's shared pitch groups “électriciens et prescripteurs” with mobile accessories and routes to Wave in the same list. Produce separate, explicit group variants: MEP routes to relevant HeyZack/Ecoled needs; architecture/interior fitout may route to Kartezzi; mobile retail is its own future B2B lane. Symphonics remains excluded pending identity.

One fictional buyer persona per brand does not establish exhaustive coverage of all trades or company sizes. Wave's two-shop buyer and Kartezzi's Paris architect are examples only. Do not use their employee counts, income, gender or locations as exclusion filters.

### 6. Regional detail describes prospects, not proven service coverage

No inspected ledger establishes a national or regional installation/service promise. The drafts usually preserve this distinction. HeyZack's persona is in department 31/Occitanie; Kartezzi's is in Paris/Île-de-France; Wave's is in a French metropolitan town. These are authored scenarios, not region evidence.

Kartezzi `buyer-persona.json` `/data/demographics/income` states an estimated €72,000 gross income and `/location` specifies Paris/Île-de-France; HeyZack gives a €42,000–58,000 illustrative income band. Neither is a researched market statistic. Wave labels its €38,500 income illustrative explicitly. Mark every persona demographic and imagined quote illustrative consistently, or omit irrelevant numeric biography. Do not recast it as a lead, interview, testimonial or confirmed client.

Ask for actual project commune/department, preserve SIREN and establishment SIRET separately, and confirm feasibility before a proposal. The legal Paris address and Courtry establishment do not prove coverage. Do not borrow WEAV's stated Île-de-France coverage.

### 7. French prospect address is usable; operator metadata needs a separate English layer

Voice guidelines and inspected direct-address examples use French `vous`/`votre`. No concrete tutoiement issue was established; occurrences of `ton` describe tone and are not the possessive pronoun. Do not mechanically reject them.

Many operational notes, proof labels, uncertainty fields and prompt templates remain French. The owner requested English operator communication; future review/readiness documents should be English while prospect email, landing and social copy remains natural fr-FR/vous. English ERP vocabulary and identifiers should not leak into French customer body text. Keep bilingual hooks only as a deliberate content requirement, with the French set primary and English companion clearly identified.

## Direction for the future wave 6 run

Generate body copy from current offer facts and relevant role needs. Require evidence/approval metadata alongside the copy, never as customer paragraphs. These short internal wording examples illustrate the intended separation; they are proposed copy, not approved outreach or operating promises:

- HeyZack: “Votre prochain chantier prévoit-il le pilotage de l’éclairage, du chauffage ou des accès ? Indiquez-nous les équipements existants et le département du projet pour examiner les besoins et les contraintes de compatibilité avec vous.”
- Ecoled: “Vous préparez un lot éclairage ? Partagez l’usage des locaux et les plans disponibles pour cadrer le besoin en éclairage LED et en étude photométrique.”
- Axtech, MEP intake: “Votre besoin porte-t-il sur l’éclairage LED ou le pilotage du bâtiment ? Décrivez le projet et votre métier pour identifier l’interlocuteur adapté au sein des marques Axtech.”
- Kartezzi: “Vous travaillez sur un projet d’agencement ou de revêtement mural ? Présentez-nous vos plans, dimensions et finitions recherchées pour préparer un échange sur les matières et le sur-mesure.”
- Wave, separate reseller draft: “Vous préparez l’assortiment accessoires de votre boutique téléphonie ? Précisez les familles recherchées — charge, audio ou support — et les références à examiner pour votre rayon.”

These examples omit unproved performance, stock, price, deadline, connector, coverage and competitive claims. They do not imply that ERP/Vapi/Explee/social is operational. The user-facing offer and CTA must still receive brand/sender review before any actual use.

The wave 6 acceptance check must inspect actual landing/email/social deliverables, required sequence and calendar counts, brand/trade variants, French language, evidence linkage and clean separation of metadata. It must also confirm that Thoughtseed service-studio template language has not carried into these product brands. A complete JSON envelope, a source-backed draft and authority to send or publish are separate states. This review provides no sending, publishing, ERP-writing or Vapi-calling authority.
