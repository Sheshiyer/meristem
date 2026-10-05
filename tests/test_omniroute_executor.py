#!/usr/bin/env python3
"""Synthetic unit and integration tests for Meristem OmniRoute executor.

Tests authentication resolution, loopback gateway validation, prompt stability,
JSON fence stripping, envelope and semantic validation, quality gates,
dossier grounding, error secret redaction, atomic writes, cache receipts with
exact hashes, brand locking, clean state enforcement, and end-to-end runner execution.
"""

import datetime
import importlib.util
import json
import os
import shutil
import sqlite3
import tempfile
import unittest
import urllib.error
from unittest.mock import MagicMock, patch

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXECUTOR_SCRIPT = os.path.join(REPO_ROOT, "runner", "omniroute-executor.py")
spec = importlib.util.spec_from_file_location("omniroute_executor", EXECUTOR_SCRIPT)
executor_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(executor_mod)


class TestOmniRouteExecutor(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="meristem_test_")
        self.vault_dir = os.path.join(self.test_dir, "isolated_vault")
        os.makedirs(self.vault_dir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_resolve_api_key_from_env(self):
        with patch.dict(os.environ, {"OMNIROUTE_API_KEY": "env-secret-123"}):
            key = executor_mod.resolve_api_key()
            self.assertEqual(key, "env-secret-123")

    def test_resolve_api_key_from_sqlite(self):
        db_path = os.path.join(self.test_dir, "test_storage.sqlite")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE api_keys (id TEXT PRIMARY KEY, name TEXT, key TEXT, is_active INTEGER);"
        )
        cursor.execute(
            "INSERT INTO api_keys (id, name, key, is_active) VALUES ('1', 'Temperance Engine', 'db-secret-456', 1);"
        )
        conn.commit()
        conn.close()

        with patch.dict(os.environ, {}, clear=True):
            key = executor_mod.resolve_api_key(db_path_override=db_path)
            self.assertEqual(key, "db-secret-456")

    def test_resolve_api_key_missing_fails(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(RuntimeError) as ctx:
                executor_mod.resolve_api_key(db_path_override=os.path.join(self.test_dir, "missing.sqlite"))
            self.assertIn("Missing required OmniRoute API key", str(ctx.exception))

    def test_gateway_loopback_validation(self):
        # Valid loopback URLs
        self.assertEqual(
            executor_mod.validate_and_normalize_gateway("http://127.0.0.1:20128"),
            "http://127.0.0.1:20128",
        )
        self.assertEqual(
            executor_mod.validate_and_normalize_gateway("http://localhost:20128/v1/"),
            "http://localhost:20128",
        )
        self.assertEqual(
            executor_mod.validate_and_normalize_gateway("http://127.0.0.1:20128/v1"),
            "http://127.0.0.1:20128",
        )

        # Rejected non-loopback URLs
        with self.assertRaises(ValueError) as ctx:
            executor_mod.validate_and_normalize_gateway("https://api.openai.com")
        self.assertIn("Gateway must be loopback only", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            executor_mod.validate_and_normalize_gateway("http://remote.host.internal:20128")
        self.assertIn("Gateway must be loopback only", str(ctx.exception))

    def test_strip_json_fence(self):
        raw = "```json\n{\"skill\": \"buyer-persona\", \"status\": \"complete\"}\n```"
        cleaned = executor_mod.strip_json_fence(raw)
        self.assertEqual(cleaned, '{"skill": "buyer-persona", "status": "complete"}')

        raw_no_fence = '{"skill": "buyer-persona", "status": "complete"}'
        self.assertEqual(executor_mod.strip_json_fence(raw_no_fence), raw_no_fence)

    def test_validate_output_envelope_valid(self):
        valid_obj = {
            "skill": "buyer-persona",
            "cluster": "foundation",
            "wave": 1,
            "status": "complete",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {"personas": [{"id": "electrician"}]},
        }
        ok, errors = executor_mod.validate_output_envelope(
            valid_obj, expected_spoke="buyer-persona", expected_cluster="foundation", expected_wave=1
        )
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_validate_output_envelope_invalid_fields(self):
        base_obj = {
            "skill": "buyer-persona",
            "cluster": "foundation",
            "wave": 1,
            "status": "complete",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {"personas": [{"id": "user1"}]},
        }

        # Missing / invalid version
        bad_ver = dict(base_obj, version="")
        ok, errors = executor_mod.validate_output_envelope(bad_ver, expected_spoke="buyer-persona")
        self.assertFalse(ok)
        self.assertTrue(any("version" in e for e in errors))

        # Invalid timestamp
        bad_ts = dict(base_obj, timestamp="invalid-date")
        ok, errors = executor_mod.validate_output_envelope(bad_ts, expected_spoke="buyer-persona")
        self.assertFalse(ok)
        self.assertTrue(any("timestamp" in e for e in errors))

        # Invalid wave type
        bad_wave = dict(base_obj, wave="1")
        ok, errors = executor_mod.validate_output_envelope(bad_wave, expected_spoke="buyer-persona")
        self.assertFalse(ok)
        self.assertTrue(any("wave" in e for e in errors))

        # Mismatched wave int
        mismatched_wave = dict(base_obj, wave=2)
        ok, errors = executor_mod.validate_output_envelope(mismatched_wave, expected_spoke="buyer-persona", expected_wave=1)
        self.assertFalse(ok)
        self.assertTrue(any("wave" in e for e in errors))

        # Non-dict data
        bad_data = dict(base_obj, data="not-a-dict")
        ok, errors = executor_mod.validate_output_envelope(bad_data, expected_spoke="buyer-persona")
        self.assertFalse(ok)
        self.assertTrue(any("data" in e for e in errors))

    def test_draft_only_and_source_gate_enforcement(self):
        brand_cfg = {"name": "TestBrand"}

        # Missing draft_only
        obj_no_draft = {
            "skill": "value-proposition",
            "status": "complete",
            "data": {"value": "High quality", "uncertainties": []},
        }
        ok, errors = executor_mod.validate_output_details(obj_no_draft, brand_cfg)
        self.assertFalse(ok)
        self.assertTrue(any("draft_only" in e for e in errors))

        # Missing uncertainties list
        obj_no_unc = {
            "skill": "value-proposition",
            "status": "complete",
            "data": {"value": "High quality", "draft_only": True, "operational_readiness": "held"},
        }
        ok, errors = executor_mod.validate_output_details(obj_no_unc, brand_cfg)
        self.assertFalse(ok)
        self.assertTrue(any("uncertainties" in e for e in errors))

        # Prohibited live external action
        obj_live_action = {
            "skill": "value-proposition",
            "status": "complete",
            "data": {
                "value": "High quality",
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
                "live_action": True,
            },
        }
        ok, errors = executor_mod.validate_output_details(obj_live_action, brand_cfg)
        self.assertFalse(ok)
        self.assertTrue(any("Prohibited external action" in e for e in errors))

    def test_competitor_analysis_validation_and_dossier_grounding(self):
        brand_cfg = {"name": "TestBrand"}
        allowed_urls = ["https://comp1.test/about", "https://comp2.test/pricing"]

        # Less than 2 competitors
        insufficient = {
            "skill": "competitor-analysis",
            "status": "complete",
            "data": {
                "competitors": [{"name": "Comp1", "url": "https://comp1.test/about"}],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
            },
        }
        ok, errors = executor_mod.validate_output_details(insufficient, brand_cfg, allowed_urls)
        self.assertFalse(ok)
        self.assertTrue(any("at least 2 competitors" in e for e in errors))

        # Competitors missing distinct names
        duplicate_names = {
            "skill": "competitor-analysis",
            "status": "complete",
            "data": {
                "competitors": [
                    {"name": "Comp1", "url": "https://comp1.test/about"},
                    {"name": "Comp1", "url": "https://comp2.test/pricing"},
                ],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
            },
        }
        ok, errors = executor_mod.validate_output_details(duplicate_names, brand_cfg, allowed_urls)
        self.assertFalse(ok)
        self.assertTrue(any("distinct named competitors" in e for e in errors))

        # Competitor cited URL not in allowed dossier sources
        ungrounded_url = {
            "skill": "competitor-analysis",
            "status": "complete",
            "data": {
                "competitors": [
                    {"name": "Comp1", "url": "https://comp1.test/about"},
                    {"name": "Comp2", "url": "https://fabricated-unverified.com"},
                ],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
            },
        }
        ok, errors = executor_mod.validate_output_details(ungrounded_url, brand_cfg, allowed_urls)
        self.assertFalse(ok)
        self.assertTrue(any("not present in grounded research dossier" in e for e in errors))

        # Fully valid and grounded competitor analysis
        valid_comp = {
            "skill": "competitor-analysis",
            "status": "complete",
            "data": {
                "competitors": [
                    {"name": "Comp1", "url": "https://comp1.test/about"},
                    {"name": "Comp2", "url": "https://comp2.test/pricing"},
                ],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
                "evidence": ["Direct review of verified competitors"],
            },
        }
        ok, errors = executor_mod.validate_output_details(valid_comp, brand_cfg, allowed_urls)
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_buyer_persona_validation(self):
        brand_cfg = {"name": "TestBrand"}

        # Flat string instead of structured object/array
        bad_persona = {
            "skill": "buyer-persona",
            "status": "complete",
            "data": {
                "personas": "Marie Durand is an operations manager",
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
                "evidence": ["Interview notes"],
            },
        }
        ok, errors = executor_mod.validate_output_details(bad_persona, brand_cfg)
        self.assertFalse(ok)
        self.assertTrue(any("buyer-persona must provide a structured array" in e for e in errors))

        # Valid structured persona list
        valid_persona = {
            "skill": "buyer-persona",
            "status": "complete",
            "data": {
                "personas": [
                    {
                        "id": "persona-1",
                        "name": "Marie Durand",
                        "role": "Operations Manager",
                        "challenges": ["Dossier audit compliance"],
                    }
                ],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": ["Needs field interview validation"],
                "evidence": ["CEE regulatory documentation"],
            },
        }
        ok, errors = executor_mod.validate_output_details(valid_persona, brand_cfg)
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_brand_foundation_validation(self):
        brand_cfg = {"name": "TestBrand"}

        # Placeholder values rejected
        placeholder_foundation = {
            "skill": "brand-foundation",
            "status": "complete",
            "data": {
                "mission": "TBD",
                "vision": "TODO",
                "essence": "Placeholder",
                "values": ["Innovation", "Quality"],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
                "evidence": ["Founding brief"],
            },
        }
        ok, errors = executor_mod.validate_output_details(placeholder_foundation, brand_cfg)
        self.assertFalse(ok)
        self.assertTrue(any("mission" in e for e in errors))
        self.assertTrue(any("vision" in e for e in errors))
        self.assertTrue(any("at least 3 core values" in e for e in errors))

        # Valid brand foundation
        valid_foundation = {
            "skill": "brand-foundation",
            "status": "complete",
            "data": {
                "mission": "Enable French energy auditors to automate CEE compliance checks.",
                "vision": "Become the standard operating system for energy transition audits.",
                "essence": "Deterministic audit integrity.",
                "values": ["Precision", "Transparency", "Rigor"],
                "draft_only": True, "operational_readiness": "held",
                "uncertainties": [],
                "evidence": ["Founding brief"],
            },
        }
        ok, errors = executor_mod.validate_output_details(valid_foundation, brand_cfg)
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_dossier_loading_bounds_and_missing_files(self):
        brand_dir = os.path.join(self.test_dir, "dossier_brand")
        os.makedirs(brand_dir, exist_ok=True)

        # Configured missing dossier raises FileNotFoundError
        cfg_missing = {"research": {"dossier": "missing_dossier.md"}}
        with self.assertRaises(FileNotFoundError):
            executor_mod.read_dossier_context(brand_dir, cfg_missing)

        # Configured empty dossier raises ValueError
        empty_dossier_file = os.path.join(brand_dir, "empty_dossier.md")
        with open(empty_dossier_file, "w") as f:
            pass
        cfg_empty = {"research": {"dossier": "empty_dossier.md"}}
        with self.assertRaises(ValueError) as ctx:
            executor_mod.read_dossier_context(brand_dir, cfg_empty)
        self.assertIn("empty", str(ctx.exception).lower())

        # Configured oversized dossier raises ValueError
        oversized_file = os.path.join(brand_dir, "large_dossier.md")
        with open(oversized_file, "w") as f:
            f.write("A" * (executor_mod.MAX_DOSSIER_BYTES + 100))
        cfg_large = {"research": {"dossier": "large_dossier.md"}}
        with self.assertRaises(ValueError) as ctx:
            executor_mod.read_dossier_context(brand_dir, cfg_large)
        self.assertIn("exceeds", str(ctx.exception).lower())

    def test_clean_state_and_resume_rejection(self):
        brand_dir = os.path.join(self.test_dir, "fresh_brand")
        os.makedirs(os.path.join(brand_dir, ".brandmint", "outputs"), exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write("name: FreshBrand\n")

        # Resume flag unsupported rejection
        with self.assertRaises(RuntimeError) as ctx:
            executor_mod.MeristemExternalExecutor(
                config_path=config_path, api_key="test-key", resume=True
            )
        self.assertIn("--resume is currently unsupported", str(ctx.exception))

        # Pre-existing output rejection in fresh run
        existing_output_file = os.path.join(brand_dir, ".brandmint", "outputs", "brand-foundation.json")
        with open(existing_output_file, "w") as f:
            f.write('{"status": "complete"}')

        ex = executor_mod.MeristemExternalExecutor(
            config_path=config_path, api_key="test-key", resume=False
        )
        with self.assertRaises(RuntimeError) as ctx:
            ex.check_clean_state()
        self.assertIn("Fresh execution requires a clean output state", str(ctx.exception))

    def test_http_error_secret_redaction(self):
        secret_api_key = "super-secret-key-9999"
        mock_http_err = urllib.error.HTTPError(
            url="http://127.0.0.1:20128/v1/chat/completions",
            code=401,
            msg="Unauthorized",
            hdrs={"Authorization": f"Bearer {secret_api_key}"},
            fp=MagicMock(),
        )

        with patch("urllib.request.urlopen", side_effect=mock_http_err):
            with self.assertRaises(RuntimeError) as ctx:
                executor_mod.call_omniroute_chat(
                    gateway_url="http://127.0.0.1:20128",
                    api_key=secret_api_key,
                    model="test-model",
                    messages=[],
                    max_tokens=1000,
                    timeout_sec=5,
                )
            err_msg = str(ctx.exception)
            self.assertIn("HTTP 401 error: Unauthorized", err_msg)
            self.assertNotIn(secret_api_key, err_msg)

    def test_finish_reason_length_rejection(self):
        mock_resp = MagicMock()
        mock_resp.getcode.return_value = 200
        mock_resp.read.return_value = json.dumps(
            {
                "id": "chat-123",
                "choices": [
                    {
                        "finish_reason": "length",
                        "message": {"role": "assistant", "content": '{"partial": "json'},
                    }
                ],
            }
        ).encode("utf-8")
        mock_resp.__enter__.return_value = mock_resp

        with patch("urllib.request.urlopen", return_value=mock_resp):
            with self.assertRaises(RuntimeError) as ctx:
                executor_mod.call_omniroute_chat(
                    gateway_url="http://127.0.0.1:20128",
                    api_key="key",
                    model="test-model",
                    messages=[],
                    max_tokens=1000,
                    timeout_sec=5,
                )
            self.assertIn("truncated", str(ctx.exception).lower())

    def test_symbolic_unknown_identity_gate_receipt(self):
        brand_dir = os.path.join(self.test_dir, "gate_brand")
        os.makedirs(os.path.join(brand_dir, ".brandmint", "prompts"), exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(
                json.dumps(
                    {
                        "name": "Symphonics",
                        "gates": {"symphonics_identity_unknown": True},
                    }
                )
            )

        prompt_file = os.path.join(brand_dir, ".brandmint", "prompts", "brand-foundation.md")
        with open(prompt_file, "w") as f:
            f.write("# Brandmint Skill Execution: brand-foundation\n## Cluster: foundation\n")

        ex = executor_mod.MeristemExternalExecutor(
            config_path=config_path, api_key="test-key"
        )
        success = ex.handle_spoke(prompt_file)
        self.assertFalse(success)

        receipt_file = os.path.join(brand_dir, ".brandmint", "cache", "brand-foundation-receipt.json")
        self.assertTrue(os.path.exists(receipt_file))
        with open(receipt_file, "r") as f:
            receipt = json.load(f)

        self.assertIsNone(receipt["http_status"])
        self.assertFalse(receipt["network_call"])
        self.assertIsNone(receipt["response_model"])
        self.assertIsNone(receipt["response_id"])
        self.assertTrue(receipt["gate_rejected"])
        self.assertEqual(receipt["status"], "partial")
        self.assertIn("output_sha256", receipt)
        self.assertIn("dossier_sha256", receipt)
        with open(os.path.join(brand_dir, ".brandmint", "outputs", "brand-foundation.json")) as f:
            output = json.load(f)
        self.assertEqual(output["status"], "partial")
        self.assertEqual(output["data"]["operational_readiness"], "held")

    def test_end_to_end_synthetic_execution_wave1_isolated_vault(self):
        brand_dir = os.path.join(self.test_dir, "e2e_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(
                json.dumps(
                    {
                        "name": "SyntheticBrand",
                        "brand": {"name": "SyntheticBrand"},
                        "execution": {"research_only": True},
                    }
                )
            )

        def mock_call_omniroute(gateway_url, api_key, model, messages, max_tokens, timeout_sec):
            user_msg = messages[-1]["content"] if messages else ""
            spoke, cluster = executor_mod.parse_prompt_metadata(user_msg)
            spoke = spoke or "test-spoke"
            cluster = cluster or "foundation"
            wave = executor_mod.get_wave_for_cluster(cluster)

            if spoke == "brand-foundation":
                data = {
                    "mission": "Provide synthetic brand foundation for testing.",
                    "vision": "Scale automated brand verification.",
                    "essence": "Synthetic precision.",
                    "values": ["Speed", "Accuracy", "Quality"],
                    "draft_only": True, "operational_readiness": "held",
                    "uncertainties": [],
                    "evidence": ["Synthetic test suite"],
                }
            elif spoke == "buyer-persona":
                data = {
                    "personas": [
                        {
                            "id": "user1",
                            "name": "Auditor Alex",
                            "role": "Lead Auditor",
                            "challenges": ["Compliance accuracy"],
                        }
                    ],
                    "draft_only": True, "operational_readiness": "held",
                    "uncertainties": [],
                    "evidence": ["Synthetic test suite"],
                }
            elif spoke == "competitor-analysis":
                data = {
                    "competitors": [
                        {"name": "Competitor Alpha", "url": "https://alpha.test/pricing"},
                        {"name": "Competitor Beta", "url": "https://beta.test/features"},
                    ],
                    "draft_only": True, "operational_readiness": "held",
                    "uncertainties": [],
                    "evidence": ["Synthetic test suite"],
                }
            else:
                data = {
                    "value_props": ["High efficiency", "Deterministic reliability"],
                    "draft_only": True, "operational_readiness": "held",
                    "uncertainties": [],
                    "evidence": ["Synthetic test suite"],
                }

            out_obj = {
                "skill": spoke,
                "cluster": cluster,
                "wave": wave,
                "status": "complete",
                "timestamp": "2026-10-02T12:00:00Z",
                "version": "1.0.0",
                "data": data,
            }
            resp_payload = {
                "id": f"chatcmpl-{spoke}",
                "model": "mock/deepseek-v4-pro",
                "choices": [{"message": {"role": "assistant", "content": json.dumps(out_obj)}}],
                "usage": {"prompt_tokens": 50, "completion_tokens": 50, "total_tokens": 100},
            }
            return 200, resp_payload, 120

        with patch.dict(os.environ, {"BRANDMINT_VAULT": self.vault_dir}):
            with patch.object(executor_mod, "call_omniroute_chat", side_effect=mock_call_omniroute):
                executor = executor_mod.MeristemExternalExecutor(
                    config_path=config_path,
                    waves="1",
                    api_key="mock-test-key",
                )
                exit_code = executor.run()
                self.assertEqual(exit_code, 0)

                outputs_dir = os.path.join(brand_dir, ".brandmint", "outputs")
                cache_dir = os.path.join(brand_dir, ".brandmint", "cache")

                self.assertTrue(os.path.exists(os.path.join(outputs_dir, "brand-foundation.json")))
                self.assertTrue(os.path.exists(os.path.join(outputs_dir, "buyer-persona.json")))
                self.assertTrue(os.path.exists(os.path.join(outputs_dir, "competitor-analysis.json")))
                self.assertTrue(os.path.exists(os.path.join(outputs_dir, "value-proposition.json")))

                receipt_file = os.path.join(cache_dir, "brand-foundation-receipt.json")
                self.assertTrue(os.path.exists(receipt_file))
                with open(receipt_file) as f:
                    r_json = json.load(f)
                self.assertEqual(r_json["status"], "complete")
                self.assertEqual(r_json["response_model"], "mock/deepseek-v4-pro")
                self.assertTrue(r_json["network_call"])
                self.assertFalse(r_json["gate_rejected"])
                self.assertIn("prompt_sha256", r_json)
                self.assertIn("output_sha256", r_json)
                self.assertIn("dossier_sha256", r_json)

    # ------------------------------------------------------------------
    # parse_wave_range_py tests
    # ------------------------------------------------------------------

    def test_parse_wave_range_py_single(self):
        self.assertEqual(executor_mod.parse_wave_range_py("5"), {5})

    def test_parse_wave_range_py_range(self):
        self.assertEqual(executor_mod.parse_wave_range_py("1-3"), {1, 2, 3})

    def test_parse_wave_range_py_comma_separated(self):
        self.assertEqual(executor_mod.parse_wave_range_py("1-2,6"), {1, 2, 6})

    def test_parse_wave_range_py_mixed_sorted_dedup(self):
        self.assertEqual(executor_mod.parse_wave_range_py("6,2,1-3,2"), {1, 2, 3, 6})

    def test_parse_wave_range_py_all_waves(self):
        self.assertEqual(executor_mod.parse_wave_range_py("1-7"), {1, 2, 3, 4, 5, 6, 7})

    def test_parse_wave_range_py_reverse_range_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            executor_mod.parse_wave_range_py("5-2")
        self.assertIn("reverse", str(ctx.exception))

    def test_parse_wave_range_py_out_of_bounds_rejected(self):
        with self.assertRaises(ValueError):
            executor_mod.parse_wave_range_py("0")
        with self.assertRaises(ValueError):
            executor_mod.parse_wave_range_py("8")

    def test_parse_wave_range_py_empty_segment_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            executor_mod.parse_wave_range_py("1,,3")
        self.assertIn("empty", str(ctx.exception))

    def test_parse_wave_range_py_injection_rejected(self):
        with self.assertRaises(ValueError):
            executor_mod.parse_wave_range_py("1;rm -rf /")

    def test_parse_wave_range_py_whitespace_tolerant(self):
        self.assertEqual(executor_mod.parse_wave_range_py(" 1 - 2 , 6 "), {1, 2, 6})

    # ------------------------------------------------------------------
    # Prompt-build failure: network_call must be False
    # ------------------------------------------------------------------

    def test_prompt_build_failure_network_call_false(self):
        brand_dir = os.path.join(self.test_dir, "prompt_fail_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(json.dumps({"name": "PFBrand", "brand": {"name": "PFBrand"}}))

        # Write a prompt that will cause build_prompt_messages to exceed MAX_PROMPT_BYTES
        prompts_dir = os.path.join(brand_dir, ".brandmint", "prompts")
        os.makedirs(prompts_dir, exist_ok=True)
        huge_content = "# Brandmint Skill Execution: test-spoke\n## Cluster: foundation\n" + "X" * (executor_mod.MAX_PROMPT_BYTES + 1000)
        with open(os.path.join(prompts_dir, "test-spoke.md"), "w") as f:
            f.write(huge_content)

        with patch.dict(os.environ, {"BRANDMINT_VAULT": self.vault_dir}):
            executor = executor_mod.MeristemExternalExecutor(
                config_path=config_path,
                waves="1",
                api_key="mock-key",
            )
            prompt_file = os.path.join(prompts_dir, "test-spoke.md")
            result = executor.handle_spoke(prompt_file)
            self.assertFalse(result)

            cache_dir = os.path.join(brand_dir, ".brandmint", "cache")
            receipt_file = os.path.join(cache_dir, "test-spoke-receipt.json")
            self.assertTrue(os.path.exists(receipt_file))
            with open(receipt_file) as f:
                r = json.load(f)
            self.assertFalse(r["network_call"])
            self.assertIsNone(r["response_model"])
            self.assertEqual(r["status"], "failed")
            self.assertEqual(r["usage"], {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0})

    # ------------------------------------------------------------------
    # Response processing failure (empty choices): receipt written
    # ------------------------------------------------------------------

    def test_response_processing_failure_empty_choices_receipt(self):
        brand_dir = os.path.join(self.test_dir, "empty_choices_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(json.dumps({"name": "ECBrand", "brand": {"name": "ECBrand"}}))

        prompts_dir = os.path.join(brand_dir, ".brandmint", "prompts")
        os.makedirs(prompts_dir, exist_ok=True)
        with open(os.path.join(prompts_dir, "test-spoke.md"), "w") as f:
            f.write("# Brandmint Skill Execution: test-spoke\n## Cluster: foundation\n")

        # Mock: HTTP 200 but empty choices
        def mock_call_empty_choices(*args, **kwargs):
            return 200, {"id": "chatcmpl-empty", "choices": [], "usage": {}}, 50

        with patch.dict(os.environ, {"BRANDMINT_VAULT": self.vault_dir}):
            with patch.object(executor_mod, "call_omniroute_chat", side_effect=mock_call_empty_choices):
                executor = executor_mod.MeristemExternalExecutor(
                    config_path=config_path,
                    waves="1",
                    api_key="mock-key",
                )
                prompt_file = os.path.join(prompts_dir, "test-spoke.md")
                result = executor.handle_spoke(prompt_file)
                self.assertFalse(result)

                cache_dir = os.path.join(brand_dir, ".brandmint", "cache")
                receipt_file = os.path.join(cache_dir, "test-spoke-receipt.json")
                self.assertTrue(os.path.exists(receipt_file))
                with open(receipt_file) as f:
                    r = json.load(f)
                self.assertTrue(r["network_call"])
                self.assertIsNone(r["response_model"])  # no model field in response
                self.assertEqual(r["http_status"], 200)
                self.assertEqual(r["status"], "failed")

    # ------------------------------------------------------------------
    # response_model is null when model field absent from response
    # ------------------------------------------------------------------

    def test_response_model_null_when_absent(self):
        brand_dir = os.path.join(self.test_dir, "no_model_field_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(json.dumps({"name": "NMBrand", "brand": {"name": "NMBrand"}}))

        prompts_dir = os.path.join(brand_dir, ".brandmint", "prompts")
        os.makedirs(prompts_dir, exist_ok=True)
        with open(os.path.join(prompts_dir, "test-spoke.md"), "w") as f:
            f.write("# Brandmint Skill Execution: test-spoke\n## Cluster: foundation\n")

        def mock_call_no_model(*args, **kwargs):
            # Response without "model" field
            out_obj = {
                "skill": "test-spoke", "cluster": "foundation", "wave": 1,
                "status": "complete", "timestamp": "2026-10-02T12:00:00Z",
                "version": "1.0.0", "data": {"value_props": ["A", "B"], "draft_only": True, "operational_readiness": "held", "uncertainties": [], "evidence": ["test"]},
            }
            resp = {
                "id": "chatcmpl-nomodel",
                # no "model" key
                "choices": [{"message": {"role": "assistant", "content": json.dumps(out_obj)}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 10, "total_tokens": 20},
            }
            return 200, resp, 80

        with patch.dict(os.environ, {"BRANDMINT_VAULT": self.vault_dir}):
            with patch.object(executor_mod, "call_omniroute_chat", side_effect=mock_call_no_model):
                executor = executor_mod.MeristemExternalExecutor(
                    config_path=config_path,
                    waves="1",
                    api_key="mock-key",
                )
                prompt_file = os.path.join(prompts_dir, "test-spoke.md")
                result = executor.handle_spoke(prompt_file)
                self.assertTrue(result)

                cache_dir = os.path.join(brand_dir, ".brandmint", "cache")
                receipt_file = os.path.join(cache_dir, "test-spoke-receipt.json")
                with open(receipt_file) as f:
                    r = json.load(f)
                self.assertIsNone(r["response_model"])  # null, not self.model

    # ------------------------------------------------------------------
    # requested_waves set is populated correctly
    # ------------------------------------------------------------------

    def test_requested_waves_parsed(self):
        brand_dir = os.path.join(self.test_dir, "wave_parse_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(json.dumps({"name": "WPBrand", "brand": {"name": "WPBrand"}}))

        executor = executor_mod.MeristemExternalExecutor(
            config_path=config_path, waves="1-2,6", api_key="mock-key"
        )
        self.assertEqual(executor.requested_waves, {1, 2, 6})

    def test_requested_waves_single(self):
        brand_dir = os.path.join(self.test_dir, "wave_single_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(json.dumps({"name": "WSBrand", "brand": {"name": "WSBrand"}}))

        executor = executor_mod.MeristemExternalExecutor(
            config_path=config_path, waves="3", api_key="mock-key"
        )
        self.assertEqual(executor.requested_waves, {3})

    def test_requested_waves_invalid_rejected(self):
        brand_dir = os.path.join(self.test_dir, "wave_invalid_brand")
        os.makedirs(brand_dir, exist_ok=True)
        config_path = os.path.join(brand_dir, "brand-config.yaml")
        with open(config_path, "w") as f:
            f.write(json.dumps({"name": "WIBrand", "brand": {"name": "WIBrand"}}))

        with self.assertRaises(ValueError):
            executor_mod.MeristemExternalExecutor(
                config_path=config_path, waves="5-2", api_key="mock-key"
            )



    # ------------------------------------------------------------------
    # operational_readiness='held' enforcement
    # ------------------------------------------------------------------

    def test_operational_readiness_required(self):
        """Validate that missing operational_readiness='held' is rejected."""
        obj = {
            "skill": "buyer-persona",
            "cluster": "foundation",
            "wave": 1,
            "status": "complete",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "personas": [{"id": "user1"}],
                "draft_only": True,
                "operational_readiness": "held",
                "uncertainties": [],
                "evidence": ["test"],
            },
        }
        ok, errors = executor_mod.validate_output_details(obj, {"name": "TestBrand"})
        self.assertTrue(ok, f"Unexpected errors: {errors}")

    def test_operational_readiness_missing_rejected(self):
        """Validate that missing operational_readiness is caught."""
        obj = {
            "skill": "buyer-persona",
            "cluster": "foundation",
            "wave": 1,
            "status": "complete",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "personas": [{"id": "user1"}],
                "draft_only": True,
                "uncertainties": [],
                "evidence": ["test"],
            },
        }
        ok, errors = executor_mod.validate_output_details(obj, {"name": "TestBrand"})
        self.assertFalse(ok)
        self.assertTrue(any("operational_readiness" in e for e in errors))

    def test_operational_readiness_wrong_value_rejected(self):
        """Validate that operational_readiness != 'held' is caught."""
        obj = {
            "skill": "buyer-persona",
            "cluster": "foundation",
            "wave": 1,
            "status": "complete",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "personas": [{"id": "user1"}],
                "draft_only": True,
                "operational_readiness": "approved",
                "uncertainties": [],
                "evidence": ["test"],
            },
        }
        ok, errors = executor_mod.validate_output_details(obj, {"name": "TestBrand"})
        self.assertFalse(ok)
        self.assertTrue(any("operational_readiness" in e for e in errors))

    # ------------------------------------------------------------------
    # Draft vs launch distinction — status=complete is internal draft only
    # ------------------------------------------------------------------

    def test_status_complete_is_draft_not_launch(self):
        """status=complete with operational_readiness='held' passes — it means draft, not launch."""
        obj = {
            "skill": "product-positioning",
            "cluster": "strategy",
            "wave": 2,
            "status": "complete",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "cbbe": {"salience": {"product_category": "test"}},
                "positioning_summary": "A summary",
                "draft_only": True,
                "operational_readiness": "held",
                "uncertainties": ["Pricing not confirmed"],
                "evidence": ["dossier-ref"],
            },
        }
        ok, errors = executor_mod.validate_output_details(obj, {"name": "TestBrand"})
        self.assertTrue(ok, f"Draft complete should pass: {errors}")

    def test_missing_identity_yields_partial_not_complete(self):
        """When brand identity is missing, status must be partial, not complete."""
        obj = {
            "skill": "brand-foundation",
            "cluster": "foundation",
            "wave": 1,
            "status": "partial",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "blockers": ["Domain unreachable; product identity unknown"],
                "uncertainties": ["Brand identity could not be verified"],
                "draft_only": True,
                "operational_readiness": "held",
            },
        }
        ok, errors = executor_mod.validate_output_details(obj, {"name": "TestBrand"})
        self.assertTrue(ok, f"Partial with blockers should pass: {errors}")

    def test_partial_with_blockers_passes_envelope(self):
        """Partial status with blockers and operational_readiness='held' is valid."""
        obj = {
            "skill": "brand-foundation",
            "cluster": "foundation",
            "wave": 1,
            "status": "partial",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "blockers": ["Domain unreachable"],
                "uncertainties": ["Identity unknown"],
                "draft_only": True,
                "operational_readiness": "held",
            },
        }
        env_ok, env_errors = executor_mod.validate_output_envelope(
            obj, expected_spoke="brand-foundation", expected_cluster="foundation", expected_wave=1
        )
        self.assertTrue(env_ok, f"Envelope should pass: {env_errors}")
        det_ok, det_errors = executor_mod.validate_output_details(obj, {"name": "TestBrand"})
        self.assertTrue(det_ok, f"Details should pass: {det_errors}")

    # ------------------------------------------------------------------
    # Completion prompt content — verifies draft/launch instructions
    # ------------------------------------------------------------------

    def test_completion_prompt_contains_status_complete_clarification(self):
        """build_prompt_messages system instructions clarify status=complete semantics."""
        messages = executor_mod.build_prompt_messages(
            "# Test prompt\n", {"name": "TestBrand"}, ""
        )
        system_msg = messages[0]["content"]
        self.assertIn("status='complete' means", system_msg)
        self.assertIn("NEVER means founder approval", system_msg)
        self.assertIn("operational_readiness", system_msg)

    def test_completion_prompt_contains_timestamp_instruction(self):
        """build_prompt_messages user content includes request timestamp."""
        messages = executor_mod.build_prompt_messages(
            "# Test prompt\n", {"name": "TestBrand"}, "",
            request_timestamp="2026-10-02T15:30:00Z"
        )
        user_msg = messages[1]["content"]
        self.assertIn("2026-10-02T15:30:00Z", user_msg)
        self.assertIn("request timestamp", user_msg)

    def test_completion_prompt_uses_executor_timestamp_when_empty(self):
        """When request_timestamp is empty, executor provides its own timestamp."""
        messages = executor_mod.build_prompt_messages(
            "# Test prompt\n", {"name": "TestBrand"}, ""
        )
        user_msg = messages[1]["content"]
        # Should contain a valid ISO timestamp from the executor
        self.assertRegex(user_msg, r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

    def test_completion_prompt_no_current_utc_instruction(self):
        """Completion prompt no longer says 'Use current UTC time'."""
        messages = executor_mod.build_prompt_messages(
            "# Test prompt\n", {"name": "TestBrand"}, ""
        )
        user_msg = messages[1]["content"]
        self.assertNotIn("Use current UTC time", user_msg)


    # ------------------------------------------------------------------
    # Upstream Run Import / Checkpoint Continuation Tests (Wave 6)
    # ------------------------------------------------------------------

    def _create_valid_upstream_fixture(self, brand_name="SynthetixBrand", domain="https://synthetix.example"):
        """Helper to create a fully valid upstream W1+W2 brand run fixture."""
        src_dir = os.path.join(self.test_dir, f"upstream_{brand_name.lower()}")
        os.makedirs(os.path.join(src_dir, ".brandmint", "outputs"), exist_ok=True)
        os.makedirs(os.path.join(src_dir, ".brandmint", "cache"), exist_ok=True)
        os.makedirs(os.path.join(src_dir, "research"), exist_ok=True)

        dossier_text = "Dossier content with competitor: https://comp-a.com/overview and https://comp-b.com/profile"
        with open(os.path.join(src_dir, "research", "DOSSIER.md"), "w", encoding="utf-8") as f:
            f.write(dossier_text)
        dossier_sha = executor_mod.compute_str_sha256(f"### Research File (research/DOSSIER.md):\n{dossier_text}")

        cfg_content = f"name: {brand_name}\ndomain: {domain}\nindustry: AI Tech\ngates:\n  research_complete: true\n"
        with open(os.path.join(src_dir, "brand-config.yaml"), "w", encoding="utf-8") as f:
            f.write(cfg_content)
        cfg_sha = executor_mod.compute_str_sha256(cfg_content)

        state_data = {
            "version": "2.0.0",
            "current_wave": 2,
            "completed_waves": [1, 2],
            "completed_skills": list(executor_mod.UPSTREAM_W1_W2_SKILLS.keys()),
            "failed_skills": [],
            "status": "complete",
        }
        with open(os.path.join(src_dir, ".brandmint", "state.json"), "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2)

        # Generate 8 valid outputs and receipts
        for skill, (cluster, wave) in executor_mod.UPSTREAM_W1_W2_SKILLS.items():
            if skill == "brand-foundation":
                data = {
                    "mission": "Deliver deterministic brand architecture",
                    "vision": "Autonomous precision branding systems",
                    "essence": "Pure Determinism",
                    "values": ["rigor", "clarity", "verifiability"],
                    "draft_only": True,
                    "operational_readiness": "held",
                    "uncertainties": ["Long-term market expansion"],
                    "evidence": ["dossier-ref"],
                }
            elif skill == "competitor-analysis":
                data = {
                    "competitors": [
                        {"name": "Comp Alpha", "source_url": "https://comp-a.com/overview"},
                        {"name": "Comp Beta", "source_url": "https://comp-b.com/profile"},
                    ],
                    "draft_only": True,
                    "operational_readiness": "held",
                    "uncertainties": ["Pricing tiers unverified"],
                    "evidence": ["dossier-ref"],
                }
            elif skill == "buyer-persona":
                data = {
                    "personas": [{"name": "Lead Architect", "id": "arch-1"}],
                    "draft_only": True,
                    "operational_readiness": "held",
                    "uncertainties": ["Enterprise budget cycles"],
                    "evidence": ["dossier-ref"],
                }
            else:
                data = {
                    "summary": f"Artifact for {skill}",
                    "draft_only": True,
                    "operational_readiness": "held",
                    "uncertainties": ["Refinements pending review"],
                    "evidence": ["dossier-ref"],
                }

            out_obj = {
                "skill": skill,
                "cluster": cluster,
                "wave": wave,
                "status": "complete",
                "timestamp": "2026-10-02T12:00:00Z",
                "version": "1.0.0",
                "data": data,
            }
            out_raw = json.dumps(out_obj, indent=2)
            out_sha = executor_mod.compute_str_sha256(out_raw)
            out_file = os.path.join(src_dir, ".brandmint", "outputs", f"{skill}.json")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(out_raw)

            rec_obj = {
                "spoke": skill,
                "cluster": cluster,
                "wave": wave,
                "prompt_sha256": "fake_prompt_sha",
                "config_sha256": cfg_sha,
                "dossier_sha256": dossier_sha,
                "output_sha256": out_sha,
                "requested_model": "noesis-research",
                "response_model": "deepseek/deepseek-v4-pro",
                "response_id": f"chatcmpl-{skill}",
                "http_status": 200,
                "network_call": True,
                "gate_rejected": False,
                "status": "complete",
                "usage": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150},
                "timing_ms": 1200,
                "timestamp": "2026-10-02T12:00:00Z",
                "validation_result": {"valid": True, "errors": []},
                "provider_uncertainty": "Provider backend identity inferred from gateway response metadata; physical model routing unverified.",
            }
            rec_file = os.path.join(src_dir, ".brandmint", "cache", f"{skill}-receipt.json")
            with open(rec_file, "w", encoding="utf-8") as f:
                json.dump(rec_obj, f, indent=2)

        return src_dir

    def _create_target_brand(self, brand_name="SynthetixBrand", domain="https://synthetix.example"):
        """Helper to create a fresh target brand directory."""
        tgt_dir = os.path.join(self.test_dir, f"target_{brand_name.lower()}")
        os.makedirs(os.path.join(tgt_dir, "research"), exist_ok=True)

        dossier_text = "Dossier content with competitor: https://comp-a.com/overview and https://comp-b.com/profile"
        with open(os.path.join(tgt_dir, "research", "DOSSIER.md"), "w", encoding="utf-8") as f:
            f.write(dossier_text)

        cfg_content = f"name: {brand_name}\ndomain: {domain}\nindustry: AI Tech\ngates:\n  research_complete: true\n"
        cfg_path = os.path.join(tgt_dir, "brand-config.yaml")
        with open(cfg_path, "w", encoding="utf-8") as f:
            f.write(cfg_content)

        return tgt_dir, cfg_path

    def test_upstream_run_valid_continuation(self):
        """Valid upstream W1+W2 outputs and receipts are imported cleanly under target lock."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        executor.acquire_lock()
        try:
            executor.check_clean_state()
            executor.validate_and_import_upstream()
        finally:
            executor.release_lock()

        # Check that all 8 outputs were imported into target
        for skill in executor_mod.UPSTREAM_W1_W2_SKILLS:
            imported_out = os.path.join(tgt_dir, ".brandmint", "outputs", f"{skill}.json")
            self.assertTrue(os.path.exists(imported_out), f"Imported output missing: {skill}")

        # Check that upstream-import manifest was written
        manifest_path = os.path.join(tgt_dir, ".brandmint", "cache", "upstream-import.json")
        self.assertTrue(os.path.exists(manifest_path))
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        self.assertEqual(manifest["imported_count"], 8)
        self.assertEqual(manifest["brand_name"], "SynthetixBrand")
        self.assertIn("brand-foundation", manifest["imported_skills"])

        # Verify target state.json is untouched / not faked
        tgt_state = os.path.join(tgt_dir, ".brandmint", "state.json")
        self.assertFalse(os.path.exists(tgt_state))

    def test_upstream_run_changed_source_output_fails(self):
        """If source output file was altered after receipt was written, validation fails."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Tamper with buyer-persona.json with valid structure but changed content (hash mismatch)
        bp_path = os.path.join(src_dir, ".brandmint", "outputs", "buyer-persona.json")
        with open(bp_path, "r", encoding="utf-8") as f:
            bp_obj = json.load(f)
        bp_obj["data"]["personas"][0]["name"] = "Tampered Persona Name"
        with open(bp_path, "w", encoding="utf-8") as f:
            json.dump(bp_obj, f, indent=2)

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("Upstream output SHA256 mismatch in receipt", str(ctx.exception))

    def test_upstream_run_changed_source_config_fails(self):
        """If source brand-config was altered after receipt, config hash mismatch rejects continuation."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Tamper with upstream brand config
        with open(os.path.join(src_dir, "brand-config.yaml"), "a", encoding="utf-8") as f:
            f.write("tampered_extra_field: true\n")

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("config SHA256 mismatch", str(ctx.exception))

    def test_upstream_run_changed_source_dossier_fails(self):
        """If target dossier does not match upstream dossier hash, continuation fails."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Change target dossier content
        with open(os.path.join(tgt_dir, "research", "DOSSIER.md"), "w", encoding="utf-8") as f:
            f.write("Completely different dossier content")

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("research dossier SHA256", str(ctx.exception))

    def test_upstream_run_crossbrand_fails(self):
        """If upstream brand name differs from target brand name, continuation is rejected."""
        src_dir = self._create_valid_upstream_fixture(brand_name="OriginalBrand")
        tgt_dir, tgt_cfg = self._create_target_brand(brand_name="DifferentBrand")

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("Cross-brand upstream continuation rejected", str(ctx.exception))

    def test_upstream_run_partial_status_fails(self):
        """If any upstream output has status != complete, continuation fails."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Overwrite value-proposition with partial status output and matching receipt
        vp_out = os.path.join(src_dir, ".brandmint", "outputs", "value-proposition.json")
        vp_obj = {
            "skill": "value-proposition",
            "cluster": "foundation",
            "wave": 1,
            "status": "partial",
            "timestamp": "2026-10-02T12:00:00Z",
            "version": "1.0.0",
            "data": {
                "blockers": ["Missing input"],
                "draft_only": True,
                "operational_readiness": "held",
            },
        }
        raw_vp = json.dumps(vp_obj, indent=2)
        with open(vp_out, "w", encoding="utf-8") as f:
            f.write(raw_vp)

        rec_file = os.path.join(src_dir, ".brandmint", "cache", "value-proposition-receipt.json")
        with open(rec_file, "r", encoding="utf-8") as f:
            rec_obj = json.load(f)
        rec_obj["output_sha256"] = executor_mod.compute_str_sha256(raw_vp)
        rec_obj["status"] = "partial"
        with open(rec_file, "w", encoding="utf-8") as f:
            json.dump(rec_obj, f, indent=2)

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("expected 'complete'", str(ctx.exception))

    def test_upstream_run_missing_wave_in_state_fails(self):
        """If upstream state.json is missing wave 2 in completed_waves, continuation is rejected."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        state_file = os.path.join(src_dir, ".brandmint", "state.json")
        with open(state_file, "r", encoding="utf-8") as f:
            state_data = json.load(f)
        state_data["completed_waves"] = [1]  # missing wave 2
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2)

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("missing completed waves 1 and 2", str(ctx.exception))

    def test_upstream_run_preexisting_target_fails(self):
        """If target has pre-existing outputs, check_clean_state rejects execution before import."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Pre-create output in target
        tgt_outputs = os.path.join(tgt_dir, ".brandmint", "outputs")
        os.makedirs(tgt_outputs, exist_ok=True)
        with open(os.path.join(tgt_outputs, "existing.json"), "w", encoding="utf-8") as f:
            f.write("{}")

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(RuntimeError) as ctx:
            executor.check_clean_state()
        self.assertIn("Fresh execution requires a clean output state", str(ctx.exception))

    def test_upstream_run_unsupported_waves_fails(self):
        """Continuation with --upstream-run is rejected if waves != 6."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        with self.assertRaises(ValueError) as ctx:
            executor_mod.MeristemExternalExecutor(
                config_path=tgt_cfg,
                waves="1-7",
                upstream_run=src_dir,
                api_key="test-key",
            )
        self.assertIn("--upstream-run is only supported for waves=6", str(ctx.exception))

    def test_upstream_run_missing_receipt_fails(self):
        """If any upstream receipt is missing, continuation fails."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Delete brand-story receipt
        os.remove(os.path.join(src_dir, ".brandmint", "cache", "brand-story-receipt.json"))

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        with self.assertRaises(FileNotFoundError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("Missing upstream receipt file", str(ctx.exception))

    def test_upstream_run_same_path_fails(self):
        """Upstream run path cannot be the same as target brand dir."""
        tgt_dir, tgt_cfg = self._create_target_brand()

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=tgt_dir,
            api_key="test-key",
        )
        with self.assertRaises(ValueError) as ctx:
            executor.validate_and_import_upstream()
        self.assertIn("cannot be the same as target brand directory", str(ctx.exception))

    def test_upstream_run_source_w6_failure_allowed_if_w1_w2_valid(self):
        """A source that experienced a W6 failure is accepted if W1+W2 are complete and valid."""
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()

        # Add failed W6 spoke to source state and outputs
        state_file = os.path.join(src_dir, ".brandmint", "state.json")
        with open(state_file, "r", encoding="utf-8") as f:
            state_data = json.load(f)
        state_data["failed_skills"] = ["product-description"]
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2)

        # Write partial W6 output to source
        with open(os.path.join(src_dir, ".brandmint", "outputs", "product-description.json"), "w", encoding="utf-8") as f:
            f.write('{"skill": "product-description", "status": "partial"}')

        executor = executor_mod.MeristemExternalExecutor(
            config_path=tgt_cfg,
            waves="6",
            upstream_run=src_dir,
            api_key="test-key",
        )
        executor.validate_and_import_upstream()

        # Verify only 8 W1/W2 outputs were imported (no product-description imported)
        self.assertFalse(os.path.exists(os.path.join(tgt_dir, ".brandmint", "outputs", "product-description.json")))
        for skill in executor_mod.UPSTREAM_W1_W2_SKILLS:
            self.assertTrue(os.path.exists(os.path.join(tgt_dir, ".brandmint", "outputs", f"{skill}.json")))

    def test_competitor_analysis_source_url_prompt_clarification(self):
        """Prompt instructions explicitly mention source_url for competitor-analysis."""
        messages = executor_mod.build_prompt_messages(
            "# Spoke prompt\n", {"name": "TestBrand"}, ""
        )
        system_msg = messages[0]["content"]
        user_msg = messages[1]["content"]
        self.assertIn("source_url", system_msg)
        self.assertIn("at least 2 distinct", system_msg)
        self.assertIn("source_url", user_msg)


    def test_research_json_compaction_preserves_value_and_markdown(self):
        source = {"label": "Étude française", "text": "line one\nline two  with spaces", "list": [1, 2, {"quoted": 'a "quote"'}]}
        prefix = "### Research Dossier (DOSSIER.md):\nSource  prose stays.\n\n"
        header = "### Research Sources (evidence.json):\n"
        original = prefix + header + json.dumps(source, indent=4) + "\n\n"
        result = executor_mod.compact_research_json_for_prompt(original)
        self.assertTrue(result.startswith(prefix + header))
        self.assertEqual(json.loads(result.split(header)[1]), source)
        self.assertLess(len(result.encode()), len(original.encode()))
        self.assertEqual(executor_mod.compact_research_json_for_prompt(prefix), prefix)
        with self.assertRaisesRegex(ValueError, "Malformed JSON research"):
            executor_mod.compact_research_json_for_prompt(header + "{invalid}")

    def test_continuation_checks_nested_company_website(self):
        src_dir = self._create_valid_upstream_fixture()
        tgt_dir, tgt_cfg = self._create_target_brand()
        with open(tgt_cfg, "a", encoding="utf-8") as handle:
            handle.write("company:\n  website: https://different-brand.example\n")
        ex = executor_mod.MeristemExternalExecutor(tgt_cfg, waves="6", upstream_run=src_dir, api_key="fixture")
        with self.assertRaisesRegex(ValueError, "company.website"):
            ex.validate_and_import_upstream()
        self.assertFalse(os.path.exists(ex.outputs_dir))

    def test_continuation_rejects_running_or_failed_upstream_skill(self):
        src_dir = self._create_valid_upstream_fixture()
        _tgt_dir, tgt_cfg = self._create_target_brand()
        path = os.path.join(src_dir, ".brandmint", "state.json")
        with open(path, encoding="utf-8") as handle:
            original = json.load(handle)
        for mutation in [{"status": "running"}, {"failed_skills": ["voice-and-tone"]}]:
            with self.subTest(mutation=mutation):
                with open(path, "w", encoding="utf-8") as handle:
                    json.dump(dict(original, **mutation), handle)
                ex = executor_mod.MeristemExternalExecutor(tgt_cfg, waves="6", upstream_run=src_dir, api_key="fixture")
                with self.assertRaises(ValueError):
                    ex.validate_and_import_upstream()
                self.assertFalse(os.path.exists(ex.outputs_dir))

    def test_continuation_detects_late_checkpoint_mutation(self):
        src_dir = self._create_valid_upstream_fixture()
        _tgt_dir, tgt_cfg = self._create_target_brand()
        ex = executor_mod.MeristemExternalExecutor(tgt_cfg, waves="6", upstream_run=src_dir, api_key="fixture")
        original_validator = executor_mod.validate_output_details
        calls = []
        def mutate_after_validation(*args, **kwargs):
            result = original_validator(*args, **kwargs)
            calls.append(1)
            if len(calls) == 8:
                with open(os.path.join(src_dir, ".brandmint", "state.json"), "a", encoding="utf-8") as handle:
                    handle.write("\n ")
            return result
        with patch.object(executor_mod, "validate_output_details", side_effect=mutate_after_validation):
            with self.assertRaisesRegex(ValueError, "Concurrent mutation"):
                ex.validate_and_import_upstream()
        self.assertFalse(os.path.exists(ex.outputs_dir))


if __name__ == "__main__":
    unittest.main()
