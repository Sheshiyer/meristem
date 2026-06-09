# Brandmint v2 — Agent Execution Guide

## The Golden Rule

**Use the shell runner, not individual skill files.**

```bash
./runner/bm.sh launch --config <path>/brand-config.yaml --waves 1-7 --non-interactive
```

## Architecture

Brandmint v2 is a **skill-cluster-based** brand generation pipeline:

- **7 waves** (foundation → strategy → identity → photography → illustration → content → synthesis)
- **Each wave = one skill cluster** (orchestrator + core + spokes)
- **Shell-first execution** (deterministic, no Python async issues)
- **Conducty-style orchestration** (Obsidian vault as context engine)

## Wave Reference

| Wave | Cluster | What It Produces |
|------|---------|------------------|
| 1 | `foundation` | Brand identity, buyer persona, competitor analysis, value proposition |
| 2 | `strategy` | Voice and tone, product positioning, messaging framework, brand story |
| 3 | `identity` | Logo concept, color palette, typography, visual language |
| 4 | `photography` | Lifestyle shots, product photography, hero images |
| 5 | `illustration` | Brand illustrations, icon system, pattern library |
| 6 | `content` | Landing page copy, email sequences, ad creative, press release |
| 7 | `synthesis` | NotebookLM publishing, brand docs, wiki site |

## How to Run

### Full Pipeline

```bash
./runner/bm.sh launch \
    --config /path/to/brand-config.yaml \
    --waves 1-7 \
    --non-interactive
```

### Specific Waves

```bash
# Just foundation and strategy
./runner/bm.sh launch --config ./brand-config.yaml --waves 1-2

# Resume from wave 4
./runner/bm.sh launch --config ./brand-config.yaml --resume-from 4
```

### Check Status

```bash
./runner/bm.sh status --config ./brand-config.yaml
```

### Dry Run (Show Plan)

```bash
./runner/bm.sh launch --config ./brand-config.yaml --waves 1-7 --dry-run
```

## How It Works

1. **Plan Generation**: Runner reads brand-config.yaml and creates execution plan
2. **Per-Wave Execution**:
   - Load cluster orchestrator
   - Run tracer spoke first (validates assumptions)
   - Execute remaining spokes in dependency order
   - Write outputs to `.brandmint/outputs/{skill}.json`
3. **Checkpoint**: Between waves, health metrics are logged to vault
4. **Visual Pipeline**: Waves 3-5 use `gpt-image-2` for images
5. **Synthesis**: Wave 7 publishes to NotebookLM (with asset manifest validation)

## Visual Pipeline

**Images only**: GPT Image 2 (via ChatGPT subscription)

```bash
# From within a spoke, generate image:
bash visual/gpt-image-2/scripts/gen.sh \
    --prompt "$(cat prompts/logo-concept.txt)" \
    --out "$brand_dir/generated/logo-v1.png"
```

**Videos**: Arcplume (via Grok/X session)

```bash
bash visual/arcplume/scripts/gen-video.sh \
    "Create a 30-second brand intro video..." \
    "$brand_dir/generated/intro.mp4" \
    30
```

---

## Wave 7: Synthesis — Critical Lessons Learned

**Source**: Lessons from `brandmint-oracle-aleph` NotebookLM phase.

### The Core Problem

In v1, Wave 7 had these issues:
1. Sources auto-generated without curation
2. Visual assets could be hallucinated (paths that don't exist)
3. No separation of branding docs from product docs from campaign docs
4. User-provided assets (logos, screenshots) not properly integrated
5. NVIDIA embedding service built but underused

### The Solution: Asset Manifest + 3-Stage Pipeline

#### Step 1: Generate Asset Manifest (MANDATORY)

Before ANY synthesis spoke runs:

```bash
./runner/bm.sh generate-manifest --config brand-config.yaml
./runner/bm.sh validate-manifest --config brand-config.yaml
```

This creates `.brandmint/asset-manifest.json`:

```json
{
  "user_provided_assets": [
    {
      "id": "logo-primary",
      "path": "./assets/logo.png",
      "exists": true,
      "deterministic": true,
      "required": true
    }
  ],
  "generated_assets": [
    {
      "id": "hero-image-v1",
      "path": "./generated/hero-v1.png",
      "exists": true,
      "wave": 4,
      "skill": "hero-images"
    }
  ],
  "validation": {
    "all_paths_exist": true,
    "missing_paths": []
  }
}
```

**Critical**: If `all_paths_exist: false`, synthesis FAILS.

#### Step 2: 3-Stage Source Processing (NotebookLM)

```
TRANSFORM → CURATE → ASSEMBLE
```

1. **Transform**: Skill outputs → categorized prose (brand, product, campaign)
2. **Curate**: Select sources by artifact type (mind-map, slides, report)
3. **Assemble**: Combine with validated user-provided assets

#### Step 3: Origin Tracking

Every asset gets marked:
- `user_provided` — From user (logos, screenshots)
- `generated` — Created by AI
- `deterministic: true` — Not AI-generated

The deliverables package includes `ASSET-ORIGINS.md` documenting this.

### User-Provided Assets Configuration

In `brand-config.yaml`:

```yaml
user_provided_assets:
  logo:
    path: ./assets/logo.png
    type: logo
    required: true
    
  app_screenshots:
    - path: ./assets/screenshot-home.png
      type: screenshot
      deterministic: true
```

### NVIDIA Embedding Integration (Optional)

If `DESIGN_MEMORY_WORKER_URL` is configured, the pipeline can use NVIDIA NIM embeddings to:
- Match visual assets to prose sources
- Verify asset relevance to brand

This is **optional** — falls back to keyword matching if not configured.

---

## Key Paths

| Path | Purpose |
|------|---------|
| `brand-config.yaml` | Brand configuration input |
| `.brandmint/prompts/` | Generated skill prompts |
| `.brandmint/outputs/` | Skill output JSON files |
| `.brandmint/state.json` | Pipeline state (resume capability) |
| `.brandmint/asset-manifest.json` | **Validated asset inventory** |
| `orchestrator/vault/` | Obsidian vault (plans, metrics, failures) |
| `clusters/<wave>/` | Skill clusters |

## Skill Execution Protocol

When a skill prompt is written to `.brandmint/prompts/{skill}.md`:

1. **Read the prompt** — contains skill instructions + brand context + upstream outputs
2. **Execute the skill** — follow the instructions
3. **Write output** — valid JSON to `.brandmint/outputs/{skill}.json`
4. **Runner continues** — once output file exists, runner proceeds

### Output Schema (Required)

```json
{
    "skill": "buyer-persona",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": { /* skill-specific */ }
}
```

## What NOT To Do

- **Do NOT** read individual SKILL.md files and execute outside the runner
- **Do NOT** skip the tracer spoke — it validates plan assumptions
- **Do NOT** use interactive prompts — everything is `--non-interactive`
- **Do NOT** use FAL, Replicate, or other image providers — only `gpt-image-2`
- **Do NOT** modify state.json manually
- **Do NOT** skip asset manifest validation in Wave 7
- **Do NOT** include paths without verifying they exist
- **Do NOT** hallucinate visual assets — every path must be validated

## Cluster Structure

Each cluster follows the skill-clusters pattern:

```
clusters/{wave}/
├── brandmint-{wave}-orchestrator.md   # Routes intent to spokes
├── brandmint-{wave}-core.md           # Shared rules and schemas
└── spokes/
    ├── skill-1.md
    ├── skill-2.md
    └── skill-3.md
```

**Orchestrator**: Routes fuzzy intent to correct spoke(s)
**Core**: Decision rules, output schemas, quality gates
**Spokes**: Individual skill implementations

## spec-kit Integration

Each cluster was developed via spec-driven development:

```bash
specify init clusters/foundation --integration codex --integration-options="--skills"
/speckit.constitution   # Cluster principles
/speckit.specify        # What this cluster produces
/speckit.plan           # Implementation approach
/speckit.tasks          # Actionable breakdown
/speckit.implement      # Build it
```

## Conducty Patterns

The orchestrator uses conducty-style patterns:

- **Tracer-first**: First spoke validates assumptions before full execution
- **Checkpoints**: Health metrics between waves
- **Vault as context**: Plans, failures, improvements stored in Obsidian-format notes
- **Improve loop**: After runs, learnings extracted to improve future plans

## Wave 7 Quality Gates

| Gate | Requirement | Failure Action |
|------|-------------|----------------|
| Asset manifest exists | `.brandmint/asset-manifest.json` present | FAIL |
| All paths valid | Every path in manifest exists | FAIL |
| No hallucinations | Zero non-existent paths referenced | FAIL |
| Origins tracked | User vs generated marked | Required |
| Sources are prose | Not raw JSON (or fallback) | FAIL or fallback |
| Wiki builds | `npm run build` passes | FAIL |
| Package verified | Checksums match | FAIL |
