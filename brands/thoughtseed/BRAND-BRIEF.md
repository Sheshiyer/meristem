# Thoughtseed — Brand Brief

*Minted by brandmint-v2 · waves 1–7 · 2026-06-08*
*Source corpus: `website/thoughtseed-2026/.planning/`*

---

## At a glance

- **Name:** Thoughtseed
- **Headline:** Digital Wilderness
- **Tagline:** We plant ideas. They grow wild.
- **Promise:** One coherent system from requirement to handoff.
- **CTA:** Bring the requirement.
- **Category:** Founder-led systems studio for requirement-to-handoff delivery.

> A founder-led systems studio that turns complex requirements into coherent products by
> aligning user psychology, founder operating logic, interface design, engineering delivery,
> and structured handoff — inside one delivery loop.

---

## Positioning

The market splits important work across strategy, design, engineering, and ops vendors who
don't share one model of the problem. That fragmentation destroys coherence before the work
ships and makes ownership harder afterward. Thoughtseed carries framing, behavior, product,
execution, and handoff together so the founder stops being the full-time translator.

**Differentiators:** one integrated studio logic · founder-led judgment (less translation
loss) · psychology-aware framing grounded in build reality · handoff as a first-class output ·
studio-plus-IP (reusable product IP, not pure services) · a distinct visual/verbal territory.

**Service modules:** Requirement Architecture · Product & Interface Systems · Handoff &
Decision Systems. **Engagement models:** System Sprint · Requirement-to-Handoff Build.

---

## Audience — "Mira, the System-Carrying Founder"

Founder / CTO / innovation lead / product strategist with a lean senior team. Wants one studio
that understands the requirement, the user, and the operating reality — and a system they can
run after delivery. Skeptical of buzzwords, attracted to integrated thinking, prefers ownership
over dependency. Notices specificity, coherent language, taste with restraint, evidence of shipping.

---

## Voice & tone

Founder-side systems translator: clear, calm, technically precise, human, editorially restrained.
Short declarative sentences; evidence close to the claim; write like someone who ships.

- **Preferred:** requirement, operating logic, user behavior, founder context, systems, signal,
  coherence, intentional, crafted, shipped, legible, inherited, handoff, delivery loop.
- **Avoided (never public):** consciousness-aligned, disruptive, revolutionary, synergy,
  best-in-class, future-proof, cutting-edge, guru, healing journey, vibration, full-service agency.
- **Layer discipline:** the Krebs Cycle / research origins are **backstage only**. Public copy
  speaks in effects — clearer requirements, calmer execution, stronger adoption, cleaner ownership.

---

## Identity

**Palette** (internal labels — never surfaced publicly):

| Hex | Internal label | Role |
|---|---|---|
| `#1A237E` | Deep Quantum Blue | anchor backgrounds, long-horizon trust |
| `#00897B` | (teal) | primary accent, directional signal |
| `#F57C00` | Energetic Orange | CTA, ignition, launch |
| `#37474F` | Mindful Gray | scaffolding, secondary text |
| `#B8E986` | Growth Light | positive signal, emergence |

**Typography:** Tyros Pro (display) · SubjectivitySerif (editorial body) · Fira Code (data/ops).

**Logo:** existing canonical wordmark + tree mark (in `assets/`) — codified, not regenerated.
Generated emboss/seal/poster imagery are art-direction references, never replacement marks.

**Visual system — Digital Wilderness:** disciplined engineering meets organic emergence.
Architectural precision against cultivated texture. Materials: matte paper, brushed aluminum,
weathered stone, living moss, oxidized copper, screen glow, architectural shadow. Editorial-
documentary photography; geometric-organic illustration. *Forbidden:* purple SaaS gradients,
stock startup photos, empty futurism, mystical fog, glossy plastic, cartoon icons, baked-in text.

---

## Asset inventory

**User-provided (4, deterministic)** — `assets/`: horizontal wordmark, black tree mark, 2 logo references.

**Generated (16, Gemini / nanobanana)** — `generated/`:
- Hero: `hero-01-digital-wilderness`, `hero-02-establishing`, `hero-03-mobile`
- Lifestyle: `lifestyle-01-worktable`, `lifestyle-02-studio`
- Product: `product-01-system-artifacts`, `product-02-screen-surface`
- Social: `social-og`, `social-x-header`, `social-ig-story`
- Illustration: `illus-01-systems-organism`, `illus-02-delivery-loop`
- Icons: `icons-01-sheet`
- Pattern: `pattern-01-dark`, `pattern-02-light`
- Moodboard: `visual-language-board`

All paths validated in `.brandmint/asset-manifest.json` (`all_paths_exist: true`).

---

## What's in this package

- **30 spoke outputs** across 7 waves → `.brandmint/outputs/*.json`
  - W1 Foundation · W2 Strategy · W3 Identity · W4 Photography · W5 Illustration · W6 Content · W7 Synthesis
- **`asset-manifest.json`** — validated, origin-tracked asset inventory
- **`brand-config.yaml`** — the run configuration
- **`.brandmint/CANONICAL-BRIEF.md`** — the single brand-truth source used by every spoke
- **This brief** + (see `brand-documentation.json`) three separated docs: Brand Identity,
  Product Positioning, Campaign Guidelines

**Regenerate / extend:** `./runner/bm.sh launch --config brands/thoughtseed/brand-config.yaml --waves <range> --non-interactive`
