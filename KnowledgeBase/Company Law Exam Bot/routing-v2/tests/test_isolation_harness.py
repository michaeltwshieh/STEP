from __future__ import annotations

import shutil
import stat
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "routing-v2/scripts"
sys.path.insert(0, str(SCRIPTS))

from isolation_harness import (  # noqa: E402
    HarnessError,
    isolation_report,
    lock_answers,
    prepare_answer_inputs,
    prepare_evaluator_inputs,
    probe_external_path,
    request_open,
    run_answer,
    run_paths,
    SANDBOX_PYTHON,
    stage_output,
)


def make_file(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


class IsolationHarnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self._cleanup)
        self.base = Path(self.temporary.name)
        self.workspace = self.base / "workspace"
        self.run_dir = self.base / "run"
        self.question = make_file(self.workspace / "question.json", "question-only")
        self.workflow = make_file(self.workspace / "candidate-workflow.md", "workflow")
        self.course = make_file(self.workspace / "course-rule.md", "course")
        self.gold = make_file(self.workspace / "gold.json", "SECRET GOLD")
        self.kap = make_file(self.workspace / "kap.txt", "SECRET KAP")
        self.prior = make_file(self.workspace / "prior-answer.md", "SECRET PRIOR ANSWER")

    def _cleanup(self) -> None:
        # Read-only fixture trees are intentional; restore owner write before cleanup.
        for path in sorted(self.base.rglob("*"), key=lambda item: len(item.parts), reverse=True):
            try:
                if path.is_dir():
                    path.chmod(stat.S_IRWXU)
                else:
                    path.chmod(stat.S_IRUSR | stat.S_IWUSR)
            except FileNotFoundError:
                pass
        self.temporary.cleanup()

    def prepare(self, candidate_id: str) -> None:
        prepare_answer_inputs(
            self.run_dir,
            self.workspace,
            candidate_id,
            self.question,
            [self.workflow],
            [self.course],
        )

    def write_and_stage(self, candidate_id: str, content: str) -> None:
        output = run_paths(self.run_dir, candidate_id)["output"] / "answer.json"
        output.write_text(content, encoding="utf-8")
        stage_output(self.run_dir, candidate_id, output)

    def test_answer_tree_contains_only_question_workflow_course_and_manifest(self) -> None:
        self.prepare("candidate-a")
        input_root = run_paths(self.run_dir, "candidate-a")["input"]
        relative_files = sorted(path.relative_to(input_root).as_posix() for path in input_root.rglob("*") if path.is_file())
        self.assertEqual(
            [
                "course/course-rule.md",
                "manifest.json",
                "question/question.json",
                "workflow/candidate-workflow.md",
            ],
            relative_files,
        )
        combined = b"\n".join(path.read_bytes() for path in input_root.rglob("*") if path.is_file())
        self.assertNotIn(b"SECRET GOLD", combined)
        self.assertNotIn(b"SECRET KAP", combined)
        self.assertNotIn(b"SECRET PRIOR ANSWER", combined)

    def test_manifest_read_records_allowed_and_outside_requests(self) -> None:
        self.prepare("candidate-a")
        self.assertEqual(b"course", request_open(self.run_dir, "candidate-a", "course/course-rule.md"))
        with self.assertRaises(HarnessError):
            request_open(self.run_dir, "candidate-a", "../gold.json")
        report = isolation_report(self.run_dir)
        self.assertEqual("FAIL", report["status"])
        self.assertEqual(1, report["hard_isolation_failure_count"])
        self.assertEqual("unsafe_or_absolute_path", report["candidates"][0]["hard_isolation_failures"][0]["reason"])

    @unittest.skipUnless(shutil.which("sandbox-exec"), "macOS sandbox-exec required")
    def test_os_sandbox_blocks_and_records_intentional_secret_escape(self) -> None:
        self.prepare("candidate-a")
        result = probe_external_path(self.run_dir, "candidate-a", self.gold)
        self.assertTrue(result["blocked"])
        report = isolation_report(self.run_dir)
        self.assertEqual("FAIL", report["status"])
        failure = report["candidates"][0]["hard_isolation_failures"][0]
        self.assertEqual(str(self.gold.resolve()), failure["requested_path"])
        self.assertEqual("intentional_escape_blocked", failure["reason"])

    @unittest.skipUnless(shutil.which("sandbox-exec"), "macOS sandbox-exec required")
    def test_os_sandbox_does_not_treat_arbitrary_system_data_as_runtime_input(self) -> None:
        self.prepare("candidate-a")
        result = probe_external_path(self.run_dir, "candidate-a", Path("/etc/hosts"))
        self.assertTrue(result["blocked"])
        report = isolation_report(self.run_dir)
        self.assertEqual("FAIL", report["status"])
        self.assertEqual("intentional_escape_blocked", report["candidates"][0]["hard_isolation_failures"][0]["reason"])

    @unittest.skipUnless(shutil.which("sandbox-exec"), "macOS sandbox-exec required")
    def test_answer_command_reads_only_isolated_input_and_writes_separate_output(self) -> None:
        self.prepare("candidate-a")
        script = (
            "import os,pathlib; "
            "root=pathlib.Path(os.environ['ROUTING_INPUT_ROOT']); "
            "out=pathlib.Path(os.environ['ROUTING_OUTPUT_ROOT'])/'answer.json'; "
            "out.write_text((root/'question/question.json').read_text()+'|'+"
            "(root/'course/course-rule.md').read_text())"
        )
        result = run_answer(
            self.run_dir,
            "candidate-a",
            [str(SANDBOX_PYTHON), "-c", script],
            ["question/question.json", "course/course-rule.md"],
        )
        self.assertEqual(0, result["returncode"])
        output = run_paths(self.run_dir, "candidate-a")["output"] / "answer.json"
        self.assertEqual("question-only|course", output.read_text(encoding="utf-8"))

    @unittest.skipUnless(shutil.which("sandbox-exec"), "macOS sandbox-exec required")
    def test_direct_read_of_prepared_but_undeclared_file_is_blocked_and_recorded(self) -> None:
        self.prepare("candidate-a")
        full_input = run_paths(self.run_dir, "candidate-a")["input"] / "course/course-rule.md"
        script = "import pathlib,sys; pathlib.Path(sys.argv[1]).read_text()"
        result = run_answer(
            self.run_dir,
            "candidate-a",
            [str(SANDBOX_PYTHON), "-c", script, str(full_input)],
            ["question/question.json"],
        )
        self.assertNotEqual(0, result["returncode"])
        report = isolation_report(self.run_dir)
        self.assertEqual("FAIL", report["status"])
        self.assertEqual("sandbox_denial_during_answer", report["candidates"][0]["hard_isolation_failures"][0]["reason"])

    @unittest.skipUnless(shutil.which("sandbox-exec"), "macOS sandbox-exec required")
    def test_caught_permission_error_is_still_recorded_from_seatbelt_audit(self) -> None:
        self.prepare("candidate-a")
        script = (
            "from pathlib import Path; "
            "\ntry: Path('/etc/hosts').read_text()"
            "\nexcept PermissionError: print('BLOCKED')"
        )
        result = run_answer(
            self.run_dir,
            "candidate-a",
            [str(SANDBOX_PYTHON), "-c", script],
            ["question/question.json"],
        )
        self.assertEqual(0, result["returncode"])
        report = isolation_report(self.run_dir)
        self.assertEqual("FAIL", report["status"])
        failure = report["candidates"][0]["hard_isolation_failures"][0]
        self.assertEqual("sandbox_denial_during_answer", failure["reason"])
        self.assertIn("/private/etc/hosts", failure["requested_path"])

    def test_evaluator_inputs_are_impossible_before_all_hashes_lock(self) -> None:
        self.prepare("candidate-a")
        self.prepare("candidate-b")
        self.write_and_stage("candidate-a", "answer-a")
        self.write_and_stage("candidate-b", "answer-b")
        with self.assertRaises(HarnessError):
            prepare_evaluator_inputs(self.run_dir, self.workspace, [self.gold, self.kap])

        lock = lock_answers(self.run_dir, ["candidate-b", "candidate-a"])
        self.assertEqual("LOCKED", lock["state"])
        self.assertEqual(["candidate-a", "candidate-b"], [item["candidate_id"] for item in lock["candidates"]])
        manifest = prepare_evaluator_inputs(self.run_dir, self.workspace, [self.gold, self.kap])
        self.assertEqual("EVALUATOR_READY_AFTER_LOCK", manifest["state"])
        categories = {item["category"] for item in manifest["files"]}
        self.assertEqual({"answer", "evaluation"}, categories)
        for candidate_id in ("candidate-a", "candidate-b"):
            input_root = run_paths(self.run_dir, candidate_id)["input"]
            self.assertFalse(any(path.name in {"gold.json", "kap.txt"} for path in input_root.rglob("*")))

    def test_locked_output_cannot_be_restaged(self) -> None:
        self.prepare("candidate-a")
        self.write_and_stage("candidate-a", "answer-a")
        lock_answers(self.run_dir, ["candidate-a"])
        output = run_paths(self.run_dir, "candidate-a")["output"] / "answer.json"
        with self.assertRaises(HarnessError):
            stage_output(self.run_dir, "candidate-a", output)


if __name__ == "__main__":
    unittest.main()
