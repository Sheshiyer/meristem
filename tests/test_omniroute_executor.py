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
            "data": {"value": "High quality", "draft_only": True},
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                "draft_only": True,
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
                    "draft_only": True,
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
                    "draft_only": True,
                    "uncertainties": [],
                    "evidence": ["Synthetic test suite"],
                }
            elif spoke == "competitor-analysis":
                data = {
                    "competitors": [
                        {"name": "Competitor Alpha", "url": "https://alpha.test/pricing"},
                        {"name": "Competitor Beta", "url": "https://beta.test/features"},
                    ],
                    "draft_only": True,
                    "uncertainties": [],
                    "evidence": ["Synthetic test suite"],
                }
            else:
                data = {
                    "value_props": ["High efficiency", "Deterministic reliability"],
                    "draft_only": True,
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
                "version": "1.0.0", "data": {"value_props": ["A", "B"], "draft_only": True, "uncertainties": [], "evidence": ["test"]},
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



if __name__ == "__main__":
    unittest.main()
