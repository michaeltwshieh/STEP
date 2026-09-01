import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_package.py"
SPEC = importlib.util.spec_from_file_location("trust_check_package", SCRIPT)
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class PackageCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "package"
        self.root.mkdir()
        self.required = (
            "Content.md",
            "SOURCE-MANIFEST.json",
            "submission-checklist.md",
            "workflow.txt",
        )
        self.module = "Course-Manual-Module-01-Test.md"
        self.appendix = "Appendix-Test.md"
        self.write(self.module, "module\n")
        self.write(self.appendix, "appendix\n")
        self.write("submission-checklist.md", "checklist\n")
        self.write("workflow.txt", "workflow\n")
        self.write(
            "Content.md",
            f"File: `{self.module}`\n\n- **Appendix test** `{self.appendix}`\n",
        )
        source_files = {
            relative: checker.sha256(self.root / relative)
            for relative in (self.module, self.appendix, "submission-checklist.md")
        }
        self.manifest = {
            "schema": checker.MANIFEST_SCHEMA_V2,
            "files": source_files,
            "bundle_sha256": checker.bundle_sha256(source_files),
        }
        self.save_manifest()
        patches = (
            mock.patch.object(checker, "EXPECTED_MODULES", 1),
            mock.patch.object(checker, "EXPECTED_APPENDICES", 1),
            mock.patch.object(checker, "EXPECTED_IMMUTABLE_SOURCES", 3),
            mock.patch.object(checker, "REQUIRED_WORKFLOW_PATHS", self.required),
        )
        for patcher in patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.configure_v2_manifest()

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def save_manifest(self):
        (self.root / "SOURCE-MANIFEST.json").write_text(
            json.dumps(self.manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def configure_v2_manifest(self):
        for relative in checker.EXPECTED_WORKFLOW_PATHS:
            path = self.root / relative
            if not path.exists():
                self.write(relative, f"workflow fixture: {relative}\n")
        workflow_files = {
            relative: checker.sha256(self.root / relative)
            for relative in checker.EXPECTED_WORKFLOW_PATHS
        }
        self.manifest["schema"] = checker.MANIFEST_SCHEMA_V2
        self.manifest["workflow_files"] = workflow_files
        self.manifest["workflow_bundle_sha256"] = checker.bundle_sha256(workflow_files)
        self.save_manifest()

    def test_ds_store_is_ignored_in_both_modes(self):
        self.write(".DS_Store", "metadata")
        self.write("nested/.DS_Store", "metadata")
        self.assertEqual(checker.check_package(self.root)["status"], "PASS")
        self.assertEqual(
            checker.check_package(self.root, allow_development_artifacts=True)["status"],
            "PASS",
        )

    def test_default_rejects_development_artifacts(self):
        self.write("answers/candidate.txt", "answer")
        result = checker.check_package(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("answers/candidate.txt" in failure for failure in result["failures"]))

    def test_flag_permits_only_known_development_prefixes(self):
        for relative in (
            "answers/candidate.txt",
            "evaluation/gold.txt",
            "routing-v2/artifacts/run/report.json",
            "tmp/pdfs/page-01.png",
        ):
            self.write(relative, relative)
        self.assertEqual(
            checker.check_package(self.root, allow_development_artifacts=True)["status"],
            "PASS",
        )
        self.write("scratch/unregistered.txt", "unexpected")
        result = checker.check_package(self.root, allow_development_artifacts=True)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("scratch/unregistered.txt" in failure for failure in result["failures"]))

    def test_workflow_hash_mismatch_fails_when_workflow_files_present(self):
        self.configure_v2_manifest()
        self.write("AGENTS.md", "changed workflow\n")

        result = checker.check_package(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("workflow hash changed: AGENTS.md", result["failures"])
        self.assertIn("workflow bundle hash changed", result["failures"])

    def test_registered_answer_artifact_still_fails_clean_distribution(self):
        self.configure_v2_manifest()
        answer_path = "answers/gold.txt"
        self.write(answer_path, "gold answer\n")
        self.manifest["workflow_files"][answer_path] = checker.sha256(self.root / answer_path)
        self.manifest["workflow_bundle_sha256"] = checker.bundle_sha256(
            self.manifest["workflow_files"]
        )
        self.save_manifest()

        result = checker.check_package(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(
            any(
                "development artifacts forbidden" in failure and answer_path in failure
                for failure in result["failures"]
            )
        )

    def test_arbitrary_registered_workflow_path_fails(self):
        self.configure_v2_manifest()
        rogue_path = "scratch/rogue.py"
        self.write(rogue_path, "rogue\n")
        self.manifest["workflow_files"][rogue_path] = checker.sha256(self.root / rogue_path)
        self.manifest["workflow_bundle_sha256"] = checker.bundle_sha256(
            self.manifest["workflow_files"]
        )
        self.save_manifest()

        result = checker.check_package(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(
            any(
                "unregistered workflow paths" in failure and rogue_path in failure
                for failure in result["failures"]
            )
        )

    def test_v2_manifest_missing_workflow_metadata_fails(self):
        self.manifest.pop("workflow_files")
        self.manifest.pop("workflow_bundle_sha256")
        self.save_manifest()

        result = checker.check_package(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn(
            "SOURCE-MANIFEST.json workflow_files entry must be an object",
            result["failures"],
        )
        self.assertIn(
            "SOURCE-MANIFEST.json workflow_bundle_sha256 entry must be a hash string",
            result["failures"],
        )

    def test_exact_expected_v2_workflow_set_passes(self):
        self.configure_v2_manifest()
        self.assertEqual(checker.check_package(self.root)["status"], "PASS")

    def test_manifest_downgrade_cannot_remove_workflow_gate(self):
        self.manifest["schema"] = "trusts-routing-v2-source-manifest-v1"
        self.manifest.pop("workflow_files")
        self.manifest.pop("workflow_bundle_sha256")
        self.save_manifest()

        result = checker.check_package(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn(
            "unsupported SOURCE-MANIFEST.json schema: 'trusts-routing-v2-source-manifest-v1'",
            result["failures"],
        )


if __name__ == "__main__":
    unittest.main()
