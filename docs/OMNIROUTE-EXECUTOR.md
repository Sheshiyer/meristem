# Meristem OmniRoute External Executor

The Meristem OmniRoute External Executor (`runner/omniroute-executor.py`) is a deterministic, standard-library Python coordinator that launches Meristem's canonical shell runner (`./runner/bm.sh launch`) and executes single bounded OmniRoute model calls for each generated spoke prompt.

## Architectural Boundaries & Separation of Concerns

To prevent over-claiming, ensure safety, and maintain auditability, Meristem explicitly separates research grounding, draft authoring, and external integrations:

```
┌────────────────────────────────────────────────────────┐
│ 1. Canonical State & Execution Coordination            │
│    - bm.sh / launch.sh: wave checkpoints, prompts.     │
│    - omniroute-executor.py: directory flock locking,   │
│      fresh state validation, strict bounds & receipts. │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. Grounded Model Authoring (omniroute-executor.py)    │
│    Single bounded model call per prompt, temperature   │
│    discipline, strict JSON fence extraction.           │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. Independently Validated Research Drafts             │
│    - Envelope schema checks (version, ISO timestamp).  │
│    - Dossier grounding (competitor URLs from dossier). │
│    - Quality gates (draft_only: true, uncertainties).  │
│    - Missing/unreachable domains produce honest partial│
└───────────────────────────┬────────────────────────────┘
                            │ (STOPS HERE — No Live Actions)
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. External Live Connected Systems (OUT OF SCOPE)      │
│    Live video rendering, social publishing/broadcast,  │
│    live ad spend, public website hosting mutations,    │
│    or production CRM/ERP mutations.                    │
└────────────────────────────────────────────────────────┘
```

> **Source Validation vs Authored Drafts vs Live Systems**:
> 1. **Source Evidence**: Grounded truth files (such as `research/DOSSIER.md` or `EVIDENCE-LEDGER.md`) provide boundary constraints and source URLs.
> 2. **Authored Drafts**: Model-generated outputs in `.brandmint/outputs/*.json` are research drafts marked with `draft_only: true`. They are proposals, not verified corporate facts or active campaigns.
> 3. **Integration Receipts**: Execution receipts in `.brandmint/cache/*-receipt.json` certify only that the local loopback gateway answered the completion request and recorded byte/token metrics. They do not certify remote provider infrastructure or external system execution.
> 4. **Future ERP Integration**: Custom ERP via Model Context Protocol (MCP) on the local host is the canonical future connection architecture. Legacy ERPNext/Zoho connectors are unselected historical exploratory code.

---

## Brand Directory File Locking

The Python executor (`runner/omniroute-executor.py`) acquires an exclusive, non-blocking file lock on `<brand_dir>/.brandmint/executor.lock` via `fcntl.flock` before starting the runner subprocess. This guarantees single-writer safety and prevents concurrent executor runs from colliding or corrupting output files.

---

## Authentication and Gateway Resolution

The executor communicates strictly over loopback interfaces (`127.0.0.1` or `localhost`) to prevent remote key exfiltration. Remote gateway URLs are rejected immediately.

### API Key Resolution Order

1. **Environment Variable**: `OMNIROUTE_API_KEY`
2. **Local SQLite Store**: Active key named `Temperance Engine` from `~/.omniroute/storage.sqlite` (read-only mode).

### Provider Authentication vs Gateway Reachability

- Reaching the local gateway (`127.0.0.1:20128`) confirms local daemon connectivity.
- Upstream provider authentication errors (e.g. HTTP 401 or provider quota exhaustion) are captured cleanly, with HTTP status categories recorded while completely redacting secret keys and request headers from logs and receipts.

---

## Freshness and `--resume` Policy

- **Fresh Clean State**: Fresh execution requires that `.brandmint/outputs/` and `.brandmint/prompts/` contain no pre-existing files for the target brand run. If pre-existing files exist, the executor halts immediately to prevent `bm.sh` from silently reusing stale outputs.
- **`--resume` Flag**: `--resume` is currently unsupported and safely rejected with a clear error message, ensuring uninterrupted clean runs across selected waves.

---

## Command Reference

### Standard Execution

```bash
# Run Wave 1 for a brand portfolio
python3 runner/omniroute-executor.py \
    --config brands/axtech-portfolio-20261002/axtech/brand-config.yaml \
    --waves 1 \
    --model noesis-research \
    --timeout 180 \
    --max-output-tokens 7000

# Run waves 1, 2, and 6 only (text strategy + content drafts)
python3 runner/omniroute-executor.py \
    --config brands/axtech-portfolio-20261002/axtech/brand-config.yaml \
    --waves 1-2,6 \
    --model noesis-research
```

### Options

| Flag | Default | Description |
|---|---|---|
| `--config <path>` | *(required)* | Path to `brand-config.yaml` |
| `--waves <range>` | `1-7` | Waves to execute (e.g. `1`, `1-2`, `1-2,6`, `1-7`) |
| `--model <name>` | `noesis-research` | OmniRoute model target |
| `--timeout <sec>` | `180` | HTTP timeout per spoke model call |
| `--max-output-tokens <n>` | `7000` | Max completion tokens |
| `--gateway <url>` | `http://127.0.0.1:20128` | Loopback OmniRoute gateway URL |
| `--resume` | `false` | Resume flag (unsupported; clean state required) |

---

## Wave Range Format

The `--waves` flag accepts comma-separated ranges and singles:

| Format | Example | Result |
|--------|---------|--------|
| Single | `1` | Wave 1 |
| Range | `1-3` | Waves 1, 2, 3 |
| Mixed | `1-2,6` | Waves 1, 2, 6 |
| Complex | `6,2,1-3` | Waves 1, 2, 3, 6 (sorted, deduplicated) |

Validation rules:
- Each segment must be an integer 1..7
- Reverse ranges (e.g. `5-2`) are rejected
- Empty segments (e.g. `1,,3`) are rejected
- Non-numeric input is rejected
- Output is sorted unique in dependency order

The executor parses waves into `requested_waves` and filters polled prompts to only process spokes whose resolved wave number is in the requested set.

---

## Error Path Architecture

The executor separates failures into three distinct receipt-writing paths:

1. **Prompt-build failure** (`network_call: false`): Prompt exceeds `MAX_PROMPT_BYTES` (128KB) or other construction error. No network call is made. Receipt records `response_model: null`, zero usage.

2. **Network call failure** (`network_call: true`): HTTP error, connection failure, or timeout from the OmniRoute gateway. Receipt records `response_model: null`, zero usage, and the HTTP status if available.

3. **Response processing failure** (`network_call: true`): HTTP 200 received but response lacks `choices`, has empty content, or model output is not valid JSON. Receipt records `response_model` from the actual response metadata (null if absent), and actual usage/timing from the response.

In all cases, a truthful partial/failure output JSON is written to the outputs directory, and the spoke is marked processed. A failure in any spoke stops further spoke processing for that run.

---

## Process Management

The runner subprocess is launched with `start_new_session=True` (POSIX `setsid`), creating its own process group. On termination, `SIGTERM` is sent to the entire process group via `os.killpg()`, ensuring clean cleanup of the runner and its children without affecting the executor process.

---

## `response_model` Policy

`response_model` in audit receipts reflects only what the gateway response actually contains:
- Present in response: recorded as-is (e.g. `"deepseek/deepseek-v4-pro"`)
- Absent from response: recorded as `null` (not defaulted to the requested model)

This ensures receipts truthfully report what the backend claimed, not what was requested.

---
---

## Audit Receipts and Caching

For each executed spoke, the executor writes an audit receipt to `<brand_dir>/.brandmint/cache/<spoke>-receipt.json`.

### Successful Completion Receipt

```json
{
  "spoke": "competitor-analysis",
  "cluster": "foundation",
  "wave": 1,
  "prompt_sha256": "8a7c2f...",
  "config_sha256": "4e1b0d...",
  "dossier_sha256": "3c9b1a...",
  "output_sha256": "9f2e4a...",
  "requested_model": "noesis-research",
  "response_model": "deepseek/deepseek-v4-pro",
  "response_id": "chatcmpl-12345",
  "http_status": 200,
  "network_call": true,
  "gate_rejected": false,
  "status": "complete",
  "usage": {
    "prompt_tokens": 1200,
    "completion_tokens": 650,
    "total_tokens": 1850
  },
  "timing_ms": 3250,
  "timestamp": "2026-10-02T12:30:00Z",
  "validation_result": {
    "valid": true,
    "errors": []
  },
  "provider_uncertainty": "Provider backend identity inferred from gateway response metadata; physical model routing unverified."
}
```

### Symbolic Blocked Gate Receipt

When an unknown identity or unresolvable brand domain blocks external calls:

```json
{
  "spoke": "brand-foundation",
  "cluster": "foundation",
  "wave": 1,
  "prompt_sha256": "8a7c2f...",
  "config_sha256": "4e1b0d...",
  "dossier_sha256": "3c9b1a...",
  "output_sha256": "6b4d1e...",
  "requested_model": "noesis-research",
  "response_model": null,
  "response_id": null,
  "http_status": null,
  "network_call": false,
  "gate_rejected": true,
  "status": "partial",
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
  },
  "timing_ms": 0,
  "timestamp": "2026-10-02T12:30:00Z",
  "validation_result": {
    "valid": false,
    "errors": ["Blocked identity gate active"]
  },
  "provider_uncertainty": "Execution blocked before external gateway call."
}
```

---

## Canonical Prompt Dependency Assembly

To prevent prompt bloat exceeding the 128 KiB guard (`MAX_PROMPT_BYTES = 128 * 1024`) during multi-wave pipeline runs, `runner/launch.sh` (`generate_spoke_prompt`) selectively injects only declared upstream dependencies from the spoke's YAML frontmatter (`dependencies: [...]`).

### Assembly Rules

1. **Selective Frontmatter Ingestion**: Only outputs declared in the spoke's `dependencies` list are read and embedded in `## Upstream Outputs`. Unrelated upstream outputs and self-references are excluded.
2. **Deterministic Deduplication**: Dependency names are validated with strict identifier syntax (`^[a-zA-Z0-9_-]+$`) and deduplicated while preserving declaration order. Malformed frontmatter or syntax is rejected with a non-zero exit status.
3. **Shared Context for Content & Social-Growth**: For spokes in `content` and `social-growth` clusters, shared core dependencies (`voice-and-tone`, `messaging-framework`, `buyer-persona`, `product-positioning`) are automatically included if not already declared.
4. **Explicit Missing Dependency Notices**: If a declared upstream output file is not present in `.brandmint/outputs/`, an explicit missing notice is emitted (`Dependency output missing: required upstream source outputs/<dep>.json not available`) rather than hallucinating content or failing silently.
5. **No Compression or Truncation**: Declared dependencies, core cluster instructions, brand configuration, and output contracts are retained in full without truncating claims or raising the 128 KiB bound.
