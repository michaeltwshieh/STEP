from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "routing-v2/scripts"
FIXTURES = ROOT / "routing-v2/tests/fixtures"
VALIDATOR = SCRIPTS / "validate_route_plan.py"

sys.path.insert(0, str(SCRIPTS))
from validate_route_plan import DEFAULT_SCHEMA, validate  # noqa: E402


EXPECTED_FAILURES = {
    "action-notice.missing-operatives.fail.json": "ACTION_NOTICE_COMPONENTS",
    "managed-borrowing.missing-upstream.fail.json": "CORPORATE_ACTOR_AUTHORITY",
    "managed-borrowing.missing-bill-of-sale.fail.json": "COMPLEX_TRANSACTION_DOCUMENTS",
    "managed-borrowing.missing-complex-attachment.fail.json": "COMPLEX_TRANSACTION_DOCUMENTS",
    "managed-borrowing.missing-charge-register.fail.json": "COMPLEX_TRANSACTION_DOCUMENTS",
    "transfer-unresolved.hard-approval.fail.json": "BRANCH_DECIDING_FACT",
    "final-completion.cumulative.fail.json": "XOR_SELECTION",
    "final-completion.unselected-incorporated.fail.json": "XOR_SELECTION",
    "source-access.forbidden-open.fail.json": "FORBIDDEN_SOURCE_ACCESS",
    "source-access.incorporated-not-opened.fail.json": "SOURCE_ALLOWLIST",
    "source-access.prior-answer-open.fail.json": "FORBIDDEN_SOURCE_ACCESS",
    "source-access.role-mismatch.fail.json": "SOURCE_ALLOWLIST",
    "entity-count.unsupported.fail.json": "ENTITY_COUNT_SUPPORT",
    "materials-gap.unconditional.fail.json": "MATERIALS_GAP_PRESERVATION",
}


class RoutePlanValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(DEFAULT_SCHEMA.read_text(encoding="utf-8"))

    def test_every_clean_fixture_passes(self) -> None:
        clean = sorted(FIXTURES.glob("*.clean.json"))
        self.assertGreaterEqual(len(clean), 7)
        for path in clean:
            with self.subTest(path=path.name):
                plan = json.loads(path.read_text(encoding="utf-8"))
                report, exit_code = validate(plan, self.schema)
                self.assertEqual(0, exit_code, report)
                self.assertEqual("VALID", report["status"])
                self.assertEqual([], report["issues"])

    def test_every_targeted_failure_is_rejected_by_named_invariant(self) -> None:
        for name, expected_code in EXPECTED_FAILURES.items():
            with self.subTest(path=name):
                plan = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
                report, exit_code = validate(plan, self.schema)
                codes = {item["code"] for item in report["issues"]}
                self.assertEqual(1, exit_code, report)
                self.assertEqual("INVALID", report["status"])
                self.assertIn(expected_code, codes)

    def test_report_is_byte_deterministic_and_exit_codes_are_stable(self) -> None:
        fixture = FIXTURES / "action-notice.missing-operatives.fail.json"
        first = subprocess.run(
            [sys.executable, str(VALIDATOR), str(fixture), "--compact"],
            text=True,
            capture_output=True,
            check=False,
        )
        second = subprocess.run(
            [sys.executable, str(VALIDATOR), str(fixture), "--compact"],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(1, first.returncode)
        self.assertEqual(first.returncode, second.returncode)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual("", first.stderr)
        self.assertEqual("", second.stderr)

        clean = subprocess.run(
            [sys.executable, str(VALIDATOR), str(FIXTURES / "action-notice.clean.json"), "--compact"],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, clean.returncode)
        self.assertEqual("VALID", json.loads(clean.stdout)["status"])

    def test_invalid_json_is_tool_error_exit_two(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), str(path), "--compact"],
                text=True,
                capture_output=True,
                check=False,
            )
        report = json.loads(completed.stdout)
        self.assertEqual(2, completed.returncode)
        self.assertEqual("ERROR", report["status"])
        self.assertEqual(2, report["exit_code"])

    def test_schema_rejects_orphan_mcq_option(self) -> None:
        plan = json.loads((FIXTURES / "source-access.clean.json").read_text(encoding="utf-8"))
        plan["claims"].pop()
        report, exit_code = validate(plan, self.schema)
        self.assertEqual(1, exit_code)
        self.assertIn("FACT_CLAIM_DISPOSITIONS", {item["code"] for item in report["issues"]})

    def test_allowlist_cannot_change_after_its_hash_is_frozen(self) -> None:
        plan = json.loads((FIXTURES / "source-access.clean.json").read_text(encoding="utf-8"))
        plan["source_access"]["allowlist"].pop()
        report, exit_code = validate(plan, self.schema)
        self.assertEqual(1, exit_code)
        self.assertIn("SOURCE_ALLOWLIST", {item["code"] for item in report["issues"]})

    def test_every_route_verdict_remains_visible_in_final_trace(self) -> None:
        plan = json.loads((FIXTURES / "source-access.clean.json").read_text(encoding="utf-8"))
        plan["final_trace"] = [
            item for item in plan["final_trace"]
            if item["route_id"] != "R_forbidden"
        ]
        report, exit_code = validate(plan, self.schema)
        self.assertEqual(1, exit_code)
        self.assertIn("FINAL_ROUTE_TRACE", {item["code"] for item in report["issues"]})


if __name__ == "__main__":
    unittest.main()
