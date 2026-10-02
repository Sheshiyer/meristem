#!/usr/bin/env python3
"""Meristem OmniRoute External Executor.

Bounded executor that launches canonical ./runner/bm.sh launch, polls generated
spoke prompts, executes a single OmniRoute model call per spoke, validates
envelope and content against research dossiers and quality gates, atomically
writes output JSON, and records audit receipts.
"""

import argparse
import datetime
import fcntl
import hashlib
import json
import os
import re
import signal
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Tuple, Set

try:
    import yaml
except ImportError:
    yaml = None


DEFAULT_GATEWAY = "http://127.0.0.1:20128"
DEFAULT_MODEL = "noesis-research"
DEFAULT_TIMEOUT = 180
DEFAULT_MAX_OUTPUT_TOKENS = 7000
MAX_DOSSIER_BYTES = 64 * 1024
MAX_PROMPT_BYTES = 128 * 1024
MAX_CONFIG_BYTES = 64 * 1024
MAX_EXECUTOR_WALL_TIME_SEC = 3600

PLACEHOLDER_STRINGS = {
    "tbd",
    "todo",
    "placeholder",
    "placeholder text",
    "n/a",
    "none",
    "undefined",
    "null",
    "lorem ipsum",
}


def validate_and_normalize_gateway(gateway_url: str) -> str:
    """Validate that gateway URL uses loopback interface and normalize path."""
    parsed = urllib.parse.urlparse(gateway_url)
    hostname = parsed.hostname or ""
    if hostname.lower() not in ("127.0.0.1", "localhost", "::1", "[::1]"):
        raise ValueError(
            f"Gateway must be loopback only (127.0.0.1 or localhost); rejected host: '{hostname}'"
        )
    # Normalize path: remove trailing slash and trailing /v1
    path = parsed.path.rstrip("/")
    if path.endswith("/v1"):
        path = path[:-3].rstrip("/")
    normalized = f"{parsed.scheme}://{parsed.netloc.rstrip('/')}{path}"
    return normalized


def resolve_api_key(
    env_override: Optional[str] = None,
    db_path_override: Optional[str] = None,
) -> str:
    """Resolve API key from environment or local read-only SQLite database."""
    if env_override and env_override.strip():
        return env_override.strip()

    env_key = os.environ.get("OMNIROUTE_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip()

    db_path = db_path_override or os.path.expanduser("~/.omniroute/storage.sqlite")
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT key FROM api_keys WHERE name = 'Temperance Engine' AND is_active = 1 LIMIT 1;"
            )
            row = cursor.fetchone()
            conn.close()
            if row and row[0] and row[0].strip():
                return row[0].strip()
        except Exception as exc:
            raise RuntimeError(f"Unable to read API key from database: {exc}") from exc

    raise RuntimeError(
        "Missing required OmniRoute API key. Set OMNIROUTE_API_KEY in environment or configure active 'Temperance Engine' key in ~/.omniroute/storage.sqlite"
    )


def compute_str_sha256(content: str) -> str:
    """Return hex SHA256 digest of string."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def compute_file_sha256(filepath: str) -> str:
    """Return hex SHA256 digest of file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def load_brand_config(config_path: str) -> Tuple[Dict[str, Any], str]:
    """Read brand config YAML/JSON and return parsed dict and raw content."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Brand config not found: {config_path}")

    file_size = os.path.getsize(config_path)
    if file_size > MAX_CONFIG_BYTES:
        raise ValueError(
            f"Brand config exceeds maximum allowed size of {MAX_CONFIG_BYTES} bytes: {file_size}"
        )

    with open(config_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Try PyYAML safe_load first if available
    if yaml is not None:
        try:
            data = yaml.safe_load(raw_text)
            if isinstance(data, dict):
                return data, raw_text
        except Exception as exc:
            raise ValueError(f"Malformed YAML in brand config {config_path}: {exc}") from exc

    # Fallback to JSON
    try:
        data = json.loads(raw_text)
        if isinstance(data, dict):
            return data, raw_text
    except Exception as exc:
        raise ValueError(f"Malformed brand config at {config_path}: {exc}") from exc

    raise ValueError(f"Brand config root must be a dictionary/object: {config_path}")


def extract_urls(data: Any) -> List[str]:
    """Recursively find URLs within a data structure or text."""
    urls = []
    if isinstance(data, str):
        found = re.findall(r"https?://[^\s\"'>]+", data)
        urls.extend(found)
    elif isinstance(data, dict):
        for v in data.values():
            urls.extend(extract_urls(v))
    elif isinstance(data, list):
        for item in data:
            urls.extend(extract_urls(item))
    return list(set(urls))


def read_dossier_context(
    brand_dir: str, brand_config: Dict[str, Any]
) -> Tuple[str, str, List[str]]:
    """Load research dossier and evidence ledger referenced in config or brand dir.

    Returns (dossier_text, dossier_sha256, allowed_urls).
    """
    pieces: List[str] = []
    allowed_urls: List[str] = []
    research_cfg = brand_config.get("research", {})

    if isinstance(research_cfg, dict):
        dossier_rel = research_cfg.get("dossier")
        if dossier_rel:
            p = os.path.join(brand_dir, dossier_rel) if not os.path.isabs(dossier_rel) else dossier_rel
            if not os.path.exists(p):
                raise FileNotFoundError(f"Configured research dossier not found: {p}")
            size = os.path.getsize(p)
            if size == 0:
                raise ValueError(f"Configured research dossier is empty: {p}")
            if size > MAX_DOSSIER_BYTES:
                raise ValueError(
                    f"Configured research dossier exceeds {MAX_DOSSIER_BYTES} bytes limit: {size}"
                )
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            pieces.append(f"### Research Dossier ({dossier_rel}):\n" + content)
            allowed_urls.extend(extract_urls(content))

        sources_rel = research_cfg.get("sources")
        if sources_rel:
            p = os.path.join(brand_dir, sources_rel) if not os.path.isabs(sources_rel) else sources_rel
            if not os.path.exists(p):
                raise FileNotFoundError(f"Configured research sources file not found: {p}")
            size = os.path.getsize(p)
            if size == 0:
                raise ValueError(f"Configured research sources file is empty: {p}")
            if size > MAX_DOSSIER_BYTES:
                raise ValueError(
                    f"Configured research sources file exceeds {MAX_DOSSIER_BYTES} bytes limit: {size}"
                )
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            pieces.append(f"### Research Sources ({sources_rel}):\n" + content)
            allowed_urls.extend(extract_urls(content))

    # Standard fallback files if present and no explicit config
    if not pieces:
        for default_name in [
            "research/DOSSIER.md",
            "research/EVIDENCE-LEDGER.md",
            "research/evidence.json",
        ]:
            p = os.path.join(brand_dir, default_name)
            if os.path.exists(p):
                size = os.path.getsize(p)
                if 0 < size <= MAX_DOSSIER_BYTES:
                    with open(p, "r", encoding="utf-8") as f:
                        content = f.read()
                    pieces.append(f"### Research File ({default_name}):\n" + content)
                    allowed_urls.extend(extract_urls(content))

    dossier_text = "\n\n".join(pieces)
    dossier_sha256 = compute_str_sha256(dossier_text) if dossier_text else ""
    return dossier_text, dossier_sha256, list(set(allowed_urls))


def is_valid_iso_timestamp(ts: Any) -> bool:
    """Validate strict ISO-8601 timestamp string."""
    if not isinstance(ts, str) or not ts.strip():
        return False
    # Standard ISO-8601 regex check: YYYY-MM-DDTHH:MM:SS(Z|+HH:MM)
    pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
    if not re.match(pattern, ts):
        return False
    try:
        # Check standard datetime parsing
        clean_ts = ts.replace("Z", "+00:00")
        datetime.datetime.fromisoformat(clean_ts)
        return True
    except Exception:
        return False


def is_placeholder(val: Any) -> bool:
    """Check if value is empty or a common placeholder string."""
    if val is None or val is False:
        return True
    if isinstance(val, str):
        cleaned = val.strip().lower()
        if not cleaned or cleaned in PLACEHOLDER_STRINGS:
            return True
    return False


def strip_json_fence(raw_content: str) -> str:
    """Strip enclosing ```json ... ``` or ``` ... ``` fence if present."""
    text = raw_content.strip()
    match = re.match(r"^```(?:json)?\s*\n([\s\S]*?)\n```$", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text


def validate_output_envelope(
    output_obj: Any,
    expected_spoke: str,
    expected_cluster: Optional[str] = None,
    expected_wave: Optional[int] = None,
) -> Tuple[bool, List[str]]:
    """Validate JSON output envelope required fields."""
    errors = []
    if not isinstance(output_obj, dict):
        return False, ["Output must be a JSON object"]

    # Version check
    version = output_obj.get("version")
    if not version or not isinstance(version, str) or not version.strip():
        errors.append("Field 'version' is missing or not a valid non-empty string")

    # Timestamp check
    timestamp = output_obj.get("timestamp")
    if not is_valid_iso_timestamp(timestamp):
        errors.append(f"Field 'timestamp' is missing or not a valid ISO-8601 string: '{timestamp}'")

    # Wave check
    wave = output_obj.get("wave")
    if wave is None or isinstance(wave, bool) or not isinstance(wave, int):
        errors.append(f"Field 'wave' must be an integer, got: {type(wave).__name__}")
    elif expected_wave is not None and wave != expected_wave:
        errors.append(f"Field 'wave' ({wave}) does not match expected '{expected_wave}'")

    # Identifiers check
    skill = output_obj.get("skill")
    if skill != expected_spoke:
        errors.append(f"Field 'skill' ({skill}) does not match expected '{expected_spoke}'")

    if expected_cluster:
        cluster = output_obj.get("cluster")
        if cluster != expected_cluster:
            errors.append(f"Field 'cluster' ({cluster}) does not match expected '{expected_cluster}'")

    status = output_obj.get("status")
    if status not in ("complete", "partial"):
        errors.append(f"Field 'status' must be 'complete' or 'partial', got '{status}'")

    data = output_obj.get("data")
    if not isinstance(data, dict):
        errors.append("Field 'data' must be a JSON object")
    elif status == "complete" and not data:
        errors.append("Field 'data' cannot be empty when status is 'complete'")

    return len(errors) == 0, errors


def validate_output_details(
    output_obj: Dict[str, Any],
    brand_config: Dict[str, Any],
    allowed_dossier_urls: Optional[List[str]] = None,
) -> Tuple[bool, List[str]]:
    """Perform domain- and skill-specific semantic validation."""
    errors = []
    if not isinstance(output_obj, dict):
        return False, ["Output must be a dictionary"]

    status = output_obj.get("status")
    skill = output_obj.get("skill")
    data = output_obj.get("data")

    if not isinstance(data, dict):
        return False, ["Field 'data' must be a JSON object"]

    # Enforce draft_only: true
    if data.get("draft_only") is not True:
        errors.append("Field 'data.draft_only' must be boolean true")

    # Enforce uncertainties list presence
    uncertainties = data.get("uncertainties")
    if uncertainties is None or not isinstance(uncertainties, list):
        errors.append("Field 'data.uncertainties' must be a list")

    # Enforce no live external actions
    for forbidden in ["live_action", "publish_live", "ad_spend_active", "campaign_broadcast"]:
        if data.get(forbidden) is True:
            errors.append(f"Prohibited external action field detected: '{forbidden}'")

    # Enforce evidence / source pointers
    if status == "complete":
        has_evidence = (
            bool(data.get("evidence"))
            or bool(data.get("sources"))
            or bool(data.get("source_pointers"))
            or bool(data.get("evidence_ledger"))
            or bool(extract_urls(data))
        )
        if not has_evidence:
            errors.append("Complete output must include evidence pointers, sources, or cited URLs")

        # Skill-specific validations
        if skill == "competitor-analysis":
            competitors = data.get("competitors")
            if not isinstance(competitors, list) or len(competitors) < 2:
                errors.append(
                    "competitor-analysis must include at least 2 competitors in 'competitors' list"
                )
            else:
                names = set()
                for i, comp in enumerate(competitors):
                    if not isinstance(comp, dict):
                        errors.append(f"Competitor #{i+1} must be an object")
                        continue
                    c_name = comp.get("name")
                    if not c_name or is_placeholder(c_name):
                        errors.append(f"Competitor #{i+1} missing valid distinct name")
                    else:
                        names.add(c_name.strip().lower())

                    # Check for cited source URL within competitor object
                    c_url = comp.get("url") or comp.get("source") or comp.get("source_url") or comp.get("link")
                    if not c_url or not isinstance(c_url, str) or not c_url.startswith("http"):
                        errors.append(f"Competitor '{c_name or i+1}' missing valid cited source URL")
                    elif allowed_dossier_urls:
                        # Ensure cited URL is grounded in allowed dossier sources
                        url_matched = any(
                            c_url.rstrip("/") == u.rstrip("/") or u.rstrip("/").startswith(c_url.rstrip("/"))
                            for u in allowed_dossier_urls
                        )
                        if not url_matched:
                            errors.append(
                                f"Competitor '{c_name}' cited URL '{c_url}' is not present in grounded research dossier sources"
                            )

                if len(names) < 2:
                    errors.append("competitor-analysis requires at least 2 distinct named competitors")

        elif skill == "buyer-persona":
            personas = data.get("personas") or data.get("buyer_personas") or data.get("profiles")
            if not isinstance(personas, list) or len(personas) == 0:
                # Check if single persona object is provided with structured fields
                if not any(k in data for k in ("demographics", "psychographics", "challenges", "cbbe")):
                    errors.append(
                        "buyer-persona must provide a structured array of personas or CBBE object schema, not flat text"
                    )
            else:
                for i, persona in enumerate(personas):
                    if not isinstance(persona, dict):
                        errors.append(f"Persona #{i+1} must be a JSON object")
                    elif not persona.get("name") and not persona.get("id") and not persona.get("label"):
                        errors.append(f"Persona #{i+1} missing identifier/name")

        elif skill == "brand-foundation":
            mission = data.get("mission")
            if is_placeholder(mission):
                errors.append("brand-foundation missing or placeholder 'mission' statement")

            vision = data.get("vision")
            if is_placeholder(vision):
                errors.append("brand-foundation missing or placeholder 'vision' statement")

            essence = data.get("essence") or data.get("brand_essence")
            if is_placeholder(essence):
                errors.append("brand-foundation missing or placeholder 'essence'")

            values = data.get("values")
            if not isinstance(values, list) or len(values) < 3:
                errors.append("brand-foundation must define at least 3 core values in 'values' list")
            else:
                for i, val in enumerate(values):
                    if is_placeholder(val):
                        errors.append(f"brand-foundation value #{i+1} is empty or placeholder")

    return len(errors) == 0, errors


def build_prompt_messages(
    prompt_text: str,
    brand_config: Dict[str, Any],
    dossier_text: str = "",
) -> List[Dict[str, str]]:
    """Construct structured chat prompt enforcing strict JSON schema and evidence grounding."""
    brand_name = brand_config.get("name") or brand_config.get("brand", {}).get("name", "Target Brand")
    system_instructions = (
        "You are an expert brand strategy model generating structured JSON artifacts for Brandmint.\n"
        f"Brand context: {brand_name}.\n"
        "Rules:\n"
        "1. Output valid JSON matching the exact schema requested by the prompt envelope (version, timestamp, wave, skill, cluster, status, data).\n"
        "2. Ground all claims strictly in the provided research dossier. Do not fabricate unverifiable pricing, metrics, or geographic coverage.\n"
        "3. If product identity or domain is missing/unreachable, return status 'partial' with explicit blockers and uncertainties.\n"
        "4. For competitor-analysis complete outputs, cite at least 2 distinct competitors with real URLs from the dossier.\n"
        "5. Include evidence pointers, uncertainties (as a list), and enforce draft_only: true.\n"
        "6. Do not include or trigger any live external actions (no publishing, no video generation, no live CRM mutations).\n"
        "7. Output ONLY the raw JSON object. Do not output conversational markdown prose outside the JSON.\n"
    )

    user_content = prompt_text
    if dossier_text:
        user_content += "\n\n## Grounded Research Dossier & Sources\n" + dossier_text
    user_content += (
        "\n\n## Completion transport override\n"
        "This is a text completion request. The executor owns file writes. "
        "Return the complete JSON artifact now; do not announce work, inspect files, "
        "call tools, or attempt to write the path shown above. All required source "
        "context is included in this request. Return ONLY one JSON object. "
        "Use current UTC time for timestamp; include data.draft_only=true, "
        "data.evidence and data.uncertainties. Unknown claims remain explicit unknowns."
    )

    total_bytes = len(system_instructions.encode("utf-8")) + len(user_content.encode("utf-8"))
    if total_bytes > MAX_PROMPT_BYTES:
        raise ValueError(
            f"Total prompt size ({total_bytes} bytes) exceeds maximum allowed bound of {MAX_PROMPT_BYTES} bytes"
        )

    return [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": user_content},
    ]


def call_omniroute_chat(
    gateway_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    max_tokens: int,
    timeout_sec: int,
) -> Tuple[int, Dict[str, Any], int]:
    """Execute chat completion request to OmniRoute gateway."""
    normalized_gateway = validate_and_normalize_gateway(gateway_url)
    url = f"{normalized_gateway}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.2,
        "stream": False,
    }
    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            status_code = resp.getcode()
            body_bytes = resp.read()
            timing_ms = int((time.time() - t0) * 1000)
    except urllib.error.HTTPError as exc:
        timing_ms = int((time.time() - t0) * 1000)
        # Never dump raw response body or headers which may leak credentials
        raise RuntimeError(f"OmniRoute HTTP {exc.code} error: {exc.reason}") from exc
    except Exception as exc:
        timing_ms = int((time.time() - t0) * 1000)
        raise RuntimeError(f"OmniRoute connection failure: {exc}") from exc

    raw_text = body_bytes.decode("utf-8", errors="replace").strip()

    # Reject empty responses or HTML login / auth error pages
    if not raw_text or "<!DOCTYPE html>" in raw_text or "<html" in raw_text:
        raise RuntimeError("OmniRoute returned non-JSON/HTML login page response")

    try:
        resp_json = json.loads(raw_text)
    except Exception as exc:
        raise RuntimeError(f"OmniRoute response was not valid JSON: {exc}") from exc

    # Check for finish_reason: length (truncation rejection)
    choices = resp_json.get("choices", [])
    if choices and isinstance(choices, list):
        finish_reason = choices[0].get("finish_reason")
        if finish_reason == "length":
            raise RuntimeError("OmniRoute response was truncated by max_tokens (finish_reason: length)")

    return status_code, resp_json, timing_ms


def extract_model_reply_text(resp_json: Dict[str, Any]) -> str:
    """Extract message content string from chat completion response."""
    choices = resp_json.get("choices")
    if not choices or not isinstance(choices, list) or len(choices) == 0:
        raise RuntimeError("OmniRoute response missing 'choices' array")
    message = choices[0].get("message", {})
    content = message.get("content")
    if not content or not isinstance(content, str):
        raise RuntimeError("OmniRoute response message content is empty")
    return content


def write_atomic_file(filepath: str, content: str) -> None:
    """Atomically write text content to a file via tempfile in same directory."""
    dir_name = os.path.dirname(filepath)
    os.makedirs(dir_name, exist_ok=True)
    temp_path = f"{filepath}.tmp.{os.getpid()}_{int(time.time()*1000)}"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp_path, filepath)


def write_execution_receipt(
    cache_dir: str,
    spoke: str,
    receipt_data: Dict[str, Any],
) -> str:
    """Atomically write execution receipt JSON into cache dir without raw prompt/secrets."""
    os.makedirs(cache_dir, exist_ok=True)
    receipt_file = os.path.join(cache_dir, f"{spoke}-receipt.json")
    write_atomic_file(receipt_file, json.dumps(receipt_data, indent=2))
    return receipt_file


def is_prompt_stable(prompt_path: str, wait_interval: float = 0.25) -> bool:
    """Check if prompt file exists, is non-empty, and stopped writing."""
    if not os.path.exists(prompt_path):
        return False
    try:
        s1 = os.stat(prompt_path)
        if s1.st_size == 0:
            return False
        time.sleep(wait_interval)
        s2 = os.stat(prompt_path)
        return s1.st_size == s2.st_size and s1.st_mtime == s2.st_mtime
    except OSError:
        return False


def parse_prompt_metadata(prompt_text: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract spoke and cluster from prompt text."""
    spoke = None
    cluster = None
    spoke_match = re.search(r"#\s*Brandmint Skill Execution:\s*([\w-]+)", prompt_text)
    if spoke_match:
        spoke = spoke_match.group(1).strip()
    cluster_match = re.search(r"##\s*Cluster:\s*([\w-]+)", prompt_text)
    if cluster_match:
        cluster = cluster_match.group(1).strip()
    return spoke, cluster


def get_wave_for_cluster(cluster_name: str) -> int:
    """Resolve wave number for canonical cluster name."""
    mapping = {
        "foundation": 1,
        "strategy": 2,
        "identity": 3,
        "photography": 4,
        "illustration": 5,
        "content": 6,
        "social-growth": 6,
        "synthesis": 7,
    }
    return mapping.get(cluster_name, 1)

def parse_wave_range_py(range_str: str) -> Set[int]:
    """Parse comma-separated wave range string into sorted set of ints 1..7.

    Supports: "1", "1-3", "1-2,6", "6,2,1-3".
    Rejects: reverse ranges, out-of-bounds, empty segments, non-numeric.
    """
    result: Set[int] = set()
    for segment in range_str.split(","):
        segment = segment.replace(" ", "").replace("\t", "")
        if not segment:
            raise ValueError(f"Invalid wave range: empty segment in '{range_str}'")
        m = re.match(r"^(\d+)-(\d+)$", segment)
        if m:
            start, end = int(m.group(1)), int(m.group(2))
            if start > end:
                raise ValueError(f"Invalid wave range: reverse range '{segment}' in '{range_str}'")
            if start < 1 or end > 7:
                raise ValueError(f"Wave range out of bounds: '{segment}' (must be 1..7)")
            result.update(range(start, end + 1))
        elif re.match(r"^\d+$", segment):
            n = int(segment)
            if n < 1 or n > 7:
                raise ValueError(f"Wave number out of bounds: '{segment}' (must be 1..7)")
            result.add(n)
        else:
            raise ValueError(f"Invalid wave range: '{segment}' in '{range_str}' (expected N or N-M)")
    if not result:
        raise ValueError(f"Wave range produced no valid waves from '{range_str}'")
    return result


class MeristemExternalExecutor:
    """Coordinator that launches runner and executes spoke prompts via OmniRoute."""

    def __init__(
        self,
        config_path: str,
        waves: str = "1-7",
        model: str = DEFAULT_MODEL,
        timeout: int = DEFAULT_TIMEOUT,
        max_output_tokens: int = DEFAULT_MAX_OUTPUT_TOKENS,
        gateway: Optional[str] = None,
        api_key: Optional[str] = None,
        resume: bool = False,
    ):
        if resume:
            raise RuntimeError(
                "--resume is currently unsupported; clean fresh execution required for selected waves."
            )

        self.config_path = os.path.abspath(config_path)
        self.brand_dir = os.path.dirname(self.config_path)
        self.waves = waves
        self.requested_waves = parse_wave_range_py(waves)
        self.model = model
        self.timeout = timeout
        self.max_output_tokens = max_output_tokens
        raw_gateway = gateway or os.environ.get("OMNIROUTE_BASE_URL") or DEFAULT_GATEWAY
        self.gateway = validate_and_normalize_gateway(raw_gateway)
        self.api_key = api_key or resolve_api_key()
        self.resume = resume

        self.prompts_dir = os.path.join(self.brand_dir, ".brandmint", "prompts")
        self.outputs_dir = os.path.join(self.brand_dir, ".brandmint", "outputs")
        self.cache_dir = os.path.join(self.brand_dir, ".brandmint", "cache")
        self.lock_file = os.path.join(self.brand_dir, ".brandmint", "executor.lock")

        self.brand_config, self.raw_config = load_brand_config(self.config_path)
        self.config_sha256 = compute_str_sha256(self.raw_config)
        self.dossier_text, self.dossier_sha256, self.allowed_dossier_urls = read_dossier_context(
            self.brand_dir, self.brand_config
        )

        self._lock_fd: Optional[int] = None
        self.runner_proc: Optional[subprocess.Popen] = None
        self.processed_spokes: Set[str] = set()

    def check_clean_state(self) -> None:
        """Reject pre-existing output JSON or prompts before launching runner."""
        if os.path.isdir(self.outputs_dir):
            existing_outputs = [f for f in os.listdir(self.outputs_dir) if f.endswith(".json")]
            if existing_outputs:
                raise RuntimeError(
                    f"Fresh execution requires a clean output state, but found pre-existing outputs in {self.outputs_dir}: {existing_outputs}"
                )
        if os.path.isdir(self.prompts_dir):
            existing_prompts = [f for f in os.listdir(self.prompts_dir) if f.endswith(".md")]
            if existing_prompts:
                raise RuntimeError(
                    f"Fresh execution requires a clean prompt state, but found pre-existing prompts in {self.prompts_dir}: {existing_prompts}"
                )

    def acquire_lock(self) -> None:
        """Acquire non-blocking single-writer lock for brand directory."""
        os.makedirs(os.path.dirname(self.lock_file), exist_ok=True)
        self._lock_fd = os.open(self.lock_file, os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(self._lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (BlockingIOError, IOError) as exc:
            os.close(self._lock_fd)
            self._lock_fd = None
            raise RuntimeError(
                f"Another executor is already running for brand directory: {self.brand_dir}"
            ) from exc

    def release_lock(self) -> None:
        """Release brand lock."""
        if self._lock_fd is not None:
            try:
                fcntl.flock(self._lock_fd, fcntl.LOCK_UN)
                os.close(self._lock_fd)
            except Exception:
                pass
            self._lock_fd = None

    def terminate_runner(self) -> None:
        """Terminate the launched runner subprocess and its process group."""
        if self.runner_proc and self.runner_proc.poll() is None:
            try:
                pgid = os.getpgid(self.runner_proc.pid)
                os.killpg(pgid, signal.SIGTERM)
            except (ProcessLookupError, OSError):
                pass
            try:
                self.runner_proc.wait(timeout=3)
            except Exception:
                try:
                    self.runner_proc.kill()
                    self.runner_proc.wait(timeout=2)
                except Exception:
                    pass

    def handle_spoke(self, prompt_file: str) -> bool:
        """Process a stable prompt file, call model, validate, and write output."""
        spoke_name = os.path.basename(prompt_file)
        if spoke_name.endswith(".md"):
            spoke_name = spoke_name[:-3]

        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt_content = f.read()

        prompt_sha256 = compute_str_sha256(prompt_content)
        parsed_spoke, parsed_cluster = parse_prompt_metadata(prompt_content)
        spoke = parsed_spoke or spoke_name
        cluster = parsed_cluster or "foundation"
        wave = get_wave_for_cluster(cluster)

        output_file = os.path.join(self.outputs_dir, f"{spoke}.json")

        # Check for unresolvable domain / unknown brand gate
        gates = self.brand_config.get("gates", {})
        if gates.get("symphonics_identity_unknown") is True:
            print(f"[EXECUTOR] Blocked identity detected for {spoke}; writing honest partial output")
            partial_obj = {
                "skill": spoke,
                "cluster": cluster,
                "wave": wave,
                "status": "partial",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "version": "1.0.0",
                "data": {
                    "blockers": [
                        "Missing product/source identity: domain unresolvable, offering unknown"
                    ],
                    "uncertainties": [
                        "Domain http://symphonics.heyzack.ai/ did not resolve; no product facts available"
                    ],
                    "draft_only": True,
                },
            }
            output_content = json.dumps(partial_obj, indent=2)
            write_atomic_file(output_file, output_content)
            receipt = {
                "spoke": spoke,
                "cluster": cluster,
                "wave": wave,
                "prompt_sha256": prompt_sha256,
                "config_sha256": self.config_sha256,
                "dossier_sha256": self.dossier_sha256,
                "output_sha256": compute_str_sha256(output_content),
                "requested_model": self.model,
                "response_model": None,
                "response_id": None,
                "http_status": None,
                "network_call": False,
                "gate_rejected": True,
                "status": "partial",
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                "timing_ms": 0,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "validation_result": {"valid": False, "errors": ["Blocked identity gate active"]},
                "provider_uncertainty": "Execution blocked before external gateway call.",
            }
            write_execution_receipt(self.cache_dir, spoke, receipt)
            self.processed_spokes.add(spoke)
            return False

        # Build prompt messages BEFORE network call (prompt-build failure: no network call)
        print(f"[EXECUTOR] Calling OmniRoute ({self.model}) for spoke: {spoke}")
        try:
            messages = build_prompt_messages(prompt_content, self.brand_config, self.dossier_text)
        except Exception as exc:
            print(f"[EXECUTOR ERROR] Prompt build failed for {spoke}: {exc}", file=sys.stderr)
            failure_obj = {
                "skill": spoke,
                "cluster": cluster,
                "wave": wave,
                "status": "partial",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "version": "1.0.0",
                "data": {
                    "blockers": [f"Prompt build error: {exc}"],
                    "uncertainties": ["Prompt construction failed before network call"],
                    "draft_only": True,
                },
            }
            failure_content = json.dumps(failure_obj, indent=2)
            write_atomic_file(output_file, failure_content)
            receipt = {
                "spoke": spoke,
                "cluster": cluster,
                "wave": wave,
                "prompt_sha256": prompt_sha256,
                "config_sha256": self.config_sha256,
                "dossier_sha256": self.dossier_sha256,
                "output_sha256": compute_str_sha256(failure_content),
                "requested_model": self.model,
                "response_model": None,
                "response_id": None,
                "http_status": None,
                "network_call": False,
                "gate_rejected": False,
                "status": "failed",
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                "timing_ms": 0,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "validation_result": {"valid": False, "errors": [str(exc)]},
                "provider_uncertainty": "Prompt build failed before external gateway call.",
            }
            write_execution_receipt(self.cache_dir, spoke, receipt)
            self.processed_spokes.add(spoke)
            return False

        # Network call
        try:
            status_code, resp_json, timing_ms = call_omniroute_chat(
                gateway_url=self.gateway,
                api_key=self.api_key,
                model=self.model,
                messages=messages,
                max_tokens=self.max_output_tokens,
                timeout_sec=self.timeout,
            )
        except Exception as exc:
            print(f"[EXECUTOR ERROR] Model call failed for {spoke}: {exc}", file=sys.stderr)
            failure_obj = {
                "skill": spoke,
                "cluster": cluster,
                "wave": wave,
                "status": "partial",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "version": "1.0.0",
                "data": {
                    "blockers": [f"Model execution error: {exc}"],
                    "uncertainties": ["OmniRoute model execution failed"],
                    "draft_only": True,
                },
            }
            failure_content = json.dumps(failure_obj, indent=2)
            write_atomic_file(output_file, failure_content)
            receipt = {
                "spoke": spoke,
                "cluster": cluster,
                "wave": wave,
                "prompt_sha256": prompt_sha256,
                "config_sha256": self.config_sha256,
                "dossier_sha256": self.dossier_sha256,
                "output_sha256": compute_str_sha256(failure_content),
                "requested_model": self.model,
                "response_model": None,
                "response_id": None,
                "http_status": None,
                "network_call": True,
                "gate_rejected": False,
                "status": "failed",
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                "timing_ms": 0,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "validation_result": {"valid": False, "errors": [str(exc)]},
                "provider_uncertainty": "Provider call threw exception before valid response.",
            }
            write_execution_receipt(self.cache_dir, spoke, receipt)
            self.processed_spokes.add(spoke)
            return False

        # Extract reply and parse JSON in the same validation path
        reply_text = ""
        try:
            reply_text = extract_model_reply_text(resp_json)
            cleaned_json_text = strip_json_fence(reply_text)
            output_obj = json.loads(cleaned_json_text)
        except Exception as exc:
            print(f"[EXECUTOR ERROR] Response processing failed for {spoke}: {exc}", file=sys.stderr)
            failure_obj = {
                "skill": spoke,
                "cluster": cluster,
                "wave": wave,
                "status": "partial",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "version": "1.0.0",
                "data": {
                    "blockers": [f"Response processing error: {exc}"],
                    "uncertainties": ["Model response could not be extracted or parsed as JSON"],
                    "draft_only": True,
                },
            }
            failure_content = json.dumps(failure_obj, indent=2)
            write_atomic_file(output_file, failure_content)
            receipt = {
                "spoke": spoke,
                "cluster": cluster,
                "wave": wave,
                "prompt_sha256": prompt_sha256,
                "config_sha256": self.config_sha256,
                "dossier_sha256": self.dossier_sha256,
                "output_sha256": compute_str_sha256(failure_content),
                "requested_model": self.model,
                "response_model": resp_json.get("model"),
                "response_id": resp_json.get("id"),
                "http_status": status_code,
                "network_call": True,
                "gate_rejected": False,
                "status": "failed",
                "usage": resp_json.get("usage", {}),
                "timing_ms": timing_ms,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "validation_result": {"valid": False, "errors": [str(exc)]},
                "response_excerpt": re.sub(r"(?:sk[-_]|Bearer\s+)[A-Za-z0-9_-]{12,}", "[REDACTED]", reply_text.replace(self.api_key, "[REDACTED]"))[:512],
                "provider_uncertainty": "Provider backend identity inferred from gateway response metadata; physical model routing unverified.",
            }
            write_execution_receipt(self.cache_dir, spoke, receipt)
            self.processed_spokes.add(spoke)
            return False

        env_ok, env_errors = validate_output_envelope(
            output_obj,
            expected_spoke=spoke,
            expected_cluster=cluster,
            expected_wave=wave,
        )
        det_ok, det_errors = validate_output_details(
            output_obj, self.brand_config, self.allowed_dossier_urls
        )
        all_errors = env_errors + det_errors
        is_valid = env_ok and det_ok

        if not is_valid:
            print(f"[EXECUTOR] Output validation failed for {spoke}: {', '.join(all_errors)}")
            partial_obj = {
                "skill": spoke,
                "cluster": cluster,
                "wave": wave,
                "status": "partial",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "version": "1.0.0",
                "data": {
                    "blockers": all_errors,
                    "uncertainties": ["Validation rejected candidate output"],
                    "draft_only": True,
                },
            }
            partial_content = json.dumps(partial_obj, indent=2)
            write_atomic_file(output_file, partial_content)
            receipt = {
                "spoke": spoke,
                "cluster": cluster,
                "wave": wave,
                "prompt_sha256": prompt_sha256,
                "config_sha256": self.config_sha256,
                "dossier_sha256": self.dossier_sha256,
                "output_sha256": compute_str_sha256(partial_content),
                "requested_model": self.model,
                "response_model": resp_json.get("model"),
                "response_id": resp_json.get("id"),
                "http_status": status_code,
                "network_call": True,
                "gate_rejected": False,
                "status": "rejected",
                "usage": resp_json.get("usage", {}),
                "timing_ms": timing_ms,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "validation_result": {"valid": False, "errors": all_errors},
                "provider_uncertainty": "Provider backend identity inferred from gateway response metadata; physical model routing unverified.",
            }
            write_execution_receipt(self.cache_dir, spoke, receipt)
            self.processed_spokes.add(spoke)
            return False

        output_content = json.dumps(output_obj, indent=2)
        write_atomic_file(output_file, output_content)
        receipt = {
            "spoke": spoke,
            "cluster": cluster,
            "wave": wave,
            "prompt_sha256": prompt_sha256,
            "config_sha256": self.config_sha256,
            "dossier_sha256": self.dossier_sha256,
            "output_sha256": compute_str_sha256(output_content),
            "requested_model": self.model,
            "response_model": resp_json.get("model"),
            "response_id": resp_json.get("id"),
            "http_status": status_code,
            "network_call": True,
            "gate_rejected": False,
            "status": output_obj.get("status", "complete"),
            "usage": resp_json.get("usage", {}),
            "timing_ms": timing_ms,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "validation_result": {"valid": True, "errors": []},
            "provider_uncertainty": "Provider backend identity inferred from gateway response metadata; physical model routing unverified.",
        }
        write_execution_receipt(self.cache_dir, spoke, receipt)
        print(f"[EXECUTOR] Successfully authored {output_file}")
        self.processed_spokes.add(spoke)
        return True

    def run(self) -> int:
        """Run the end-to-end execution loop."""
        self.check_clean_state()
        self.acquire_lock()
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        bm_script = os.path.join(repo_root, "runner", "bm.sh")

        cmd = [
            bm_script,
            "launch",
            "--config",
            self.config_path,
            "--waves",
            self.waves,
            "--non-interactive",
        ]

        print(f"[EXECUTOR] Starting runner: {' '.join(cmd)}")
        self.runner_proc = subprocess.Popen(
            cmd,
            cwd=repo_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            start_new_session=True,
        )

        if self.runner_proc.stdout:
            try:
                os.set_blocking(self.runner_proc.stdout.fileno(), False)
            except Exception:
                pass

        start_time = time.time()
        last_progress_log = start_time
        had_spoke_failure = False

        try:
            while True:
                # Check wall clock bounds
                if time.time() - start_time > MAX_EXECUTOR_WALL_TIME_SEC:
                    print(
                        f"[EXECUTOR ERROR] Executor wall-clock timeout exceeded ({MAX_EXECUTOR_WALL_TIME_SEC}s)",
                        file=sys.stderr,
                    )
                    return 1

                # Check runner status
                ret = self.runner_proc.poll()

                # Poll prompts if no failure has halted further prompts
                if ret is None and not had_spoke_failure and os.path.isdir(self.prompts_dir):
                    prompt_files = sorted(
                        [
                            os.path.join(self.prompts_dir, f)
                            for f in os.listdir(self.prompts_dir)
                            if f.endswith(".md")
                        ]
                    )
                    for pf in prompt_files:
                        spoke_name = os.path.basename(pf)[:-3]
                        if spoke_name in self.processed_spokes:
                            continue
                        if not is_prompt_stable(pf):
                            continue
                        # Wave filter: resolve spoke wave and skip if not requested
                        with open(pf, "r", encoding="utf-8") as prompt_handle:
                            _meta_spoke, _meta_cluster = parse_prompt_metadata(prompt_handle.read())
                        _resolved_cluster = _meta_cluster or "foundation"
                        _resolved_wave = get_wave_for_cluster(_resolved_cluster)
                        if _resolved_wave not in self.requested_waves:
                            continue
                        success = self.handle_spoke(pf)
                        if not success:
                            print(f"[EXECUTOR] Spoke {spoke_name} ended with failure/partial")
                            had_spoke_failure = True
                            break

                # Print runner stdout lines
                if self.runner_proc.stdout:
                    try:
                        while True:
                            chunk = self.runner_proc.stdout.read(2048)
                            if not chunk:
                                break
                            sys.stdout.write(chunk)
                            sys.stdout.flush()
                    except (BlockingIOError, IOError):
                        pass

                if ret is not None:
                    print(f"[EXECUTOR] Runner finished with exit code {ret}")
                    if had_spoke_failure and ret == 0:
                        return 1
                    return ret

                # Periodic progress logging
                now = time.time()
                if now - last_progress_log > 30.0:
                    print(
                        f"[EXECUTOR] Progress check: {len(self.processed_spokes)} spokes processed, runner active"
                    )
                    last_progress_log = now

                time.sleep(0.3)

        finally:
            self.terminate_runner()
            self.release_lock()


def main() -> None:
    parser = argparse.ArgumentParser(description="Meristem OmniRoute external executor")
    parser.add_argument("--config", required=True, help="Path to brand-config.yaml")
    parser.add_argument("--waves", default="1-7", help="Wave ranges to execute (e.g. 1-2,6 or 1-7)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model name for OmniRoute")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="HTTP timeout in seconds")
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=DEFAULT_MAX_OUTPUT_TOKENS,
        help="Max completion tokens",
    )
    parser.add_argument("--gateway", default=None, help="OmniRoute gateway URL override")
    parser.add_argument("--resume", action="store_true", help="Resume flag (unsupported)")

    args = parser.parse_args()

    executor = MeristemExternalExecutor(
        config_path=args.config,
        waves=args.waves,
        model=args.model,
        timeout=args.timeout,
        max_output_tokens=args.max_output_tokens,
        gateway=args.gateway,
        resume=args.resume,
    )

    def signal_handler(signum, frame):
        print(f"\n[EXECUTOR] Received signal {signum}, shutting down...")
        executor.terminate_runner()
        executor.release_lock()
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        code = executor.run()
        sys.exit(code)
    except Exception as exc:
        print(f"[EXECUTOR ERROR] {exc}", file=sys.stderr)
        executor.terminate_runner()
        executor.release_lock()
        sys.exit(1)


if __name__ == "__main__":
    main()
