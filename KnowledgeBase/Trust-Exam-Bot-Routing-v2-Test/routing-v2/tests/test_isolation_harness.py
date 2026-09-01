import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "isolation_harness.py"
SPEC = importlib.util.spec_from_file_location("trust_isolation_harness", SCRIPT)
assert SPEC and SPEC.loader
harness = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(harness)


class IsolationHarnessFailClosedTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.run_dir = Path(self.temporary.name) / "run"
        self.candidate = "candidateA"
        self.paths = harness.run_paths(self.run_dir, self.candidate)
        self.paths["manifest"].parent.mkdir(parents=True)
        self.paths["output"].mkdir(parents=True)
        harness.write_json(
            self.paths["manifest"],
            {"candidate_id": self.candidate, "files": []},
        )
        harness.write_json(
            self.paths["events"],
            {"candidate_id": self.candidate, "events": []},
        )

    def add_failure(self, reason="test_failure"):
        harness.append_event(
            self.paths,
            {
                "type": "hard_isolation_failure",
                "requested_path": "/forbidden",
                "permitted": False,
                "reason": reason,
            },
        )

    def test_run_answer_denial_fails_after_event_is_recorded(self):
        completed = subprocess.CompletedProcess(
            args=["answer"],
            returncode=0,
            stdout="caught permission error\n",
            stderr="",
        )
        denials = [{"operation": "file-read-data", "path": "/forbidden/answer"}]
        with mock.patch.object(harness, "sandbox_command", return_value=(completed, denials)):
            with self.assertRaisesRegex(harness.HarnessError, "sandbox denial"):
                harness.run_answer(self.run_dir, self.candidate, ["answer"], [])

        ledger = json.loads(self.paths["events"].read_text(encoding="utf-8"))
        self.assertEqual([event["sequence"] for event in ledger["events"]], [1, 2])
        self.assertEqual(ledger["events"][0]["type"], "answer_command")
        failure = ledger["events"][1]
        self.assertEqual(failure["type"], "hard_isolation_failure")
        self.assertEqual(failure["reason"], "sandbox_denial_during_answer")
        self.assertEqual(failure["denied_operations"], ["file-read-data"])
        self.assertTrue((self.paths["output"] / "answer.stdout").is_file())

    def test_lock_refuses_candidate_with_failure_ledger(self):
        self.add_failure()
        with self.assertRaisesRegex(harness.HarnessError, "cannot be locked"):
            harness.lock_answers(self.run_dir, [self.candidate])
        self.assertFalse((self.run_dir / "answer-lock.json").exists())

    def test_evaluator_refuses_failed_isolation_even_with_stale_lock(self):
        self.add_failure()
        harness.write_json(
            self.run_dir / "answer-lock.json",
            {
                "harness_version": harness.HARNESS_VERSION,
                "state": "LOCKED",
                "candidates": [],
            },
        )
        with self.assertRaisesRegex(harness.HarnessError, "failed isolation report"):
            harness.prepare_evaluator_inputs(self.run_dir, Path(self.temporary.name), [])
        self.assertFalse((self.run_dir / "evaluator-inputs").exists())


if __name__ == "__main__":
    unittest.main()
