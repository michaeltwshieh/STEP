from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "routing-v2/scripts"
sys.path.insert(0, str(SCRIPTS))

from run_focused_behavioral import run  # noqa: E402


class FocusedBehavioralTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("sandbox-exec"), "macOS sandbox-exec required")
    def test_two_isolated_candidates_validate_and_fix_every_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first_root = Path(directory) / "first"
            second_root = Path(directory) / "second"
            first_root.mkdir()
            second_root.mkdir()
            first = run(first_root)
            second = run(second_root)
            first_report = (first_root / "report.json").read_bytes()
            second_report = (second_root / "report.json").read_bytes()

        self.assertEqual("PASS", first["status"])
        self.assertEqual(2, first["candidate_count"])
        self.assertEqual("PASS", first["isolation"]["status"])
        self.assertEqual(0, first["isolation"]["hard_isolation_failure_count"])
        self.assertEqual(first_report, second_report)
        for candidate in first["candidates"]:
            self.assertTrue(all(candidate["target_checks"].values()))
            self.assertEqual(5, len(candidate["validations"]))
            self.assertTrue(all(item["status"] == "VALID" for item in candidate["validations"]))
        self.assertEqual("EVALUATOR_READY_AFTER_LOCK", first["evaluator_release"]["state"])
        self.assertEqual(first["answer_lock_sha256"], first["evaluator_release"]["answer_lock_sha256"])
        self.assertEqual(second["answer_lock_sha256"], second["evaluator_release"]["answer_lock_sha256"])


if __name__ == "__main__":
    unittest.main()
