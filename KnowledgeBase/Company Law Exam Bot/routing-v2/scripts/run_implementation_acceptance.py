#!/usr/bin/env python3
"""Run and summarize the deterministic-routing implementation acceptance suite."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "routing-v2/tests/fixtures"
REPORT_VERSION = "deterministic-routing-implementation-acceptance-v1"
EXPECTED_LIVE_HASHES = {
    "CLAUDE.md": "511e564e9f6f3c40be76582ccfe2f2ee24beae00aac2dbc8d7ab2386ec74aa58",
    "Content.md": "24b08234f7a29266d6d199d5f5bc8c721253f4b23a53757fc370473bd677416b",
    "section-a.md": "bc6697e97513d3922b8b7304e414a812dad35973ff5ef6331c400187e4c746e7",
    "section-b.md": "2f80861e1fd8f23dfa50b181216c4eb96899aefdc01213884ab409df51473d75",
}
IMPLEMENTATION_SCAN_ROOTS = (
    ROOT / "routing-v2/schema",
    ROOT / "routing-v2/scripts",
    ROOT / "routing-v2/tests",
    ROOT / "routing-v2/behavioral",
    ROOT / "routing-v2/candidate/CLAUDE.md",
    ROOT / "routing-v2/candidate/routing-core.md",
    ROOT / "routing-v2/candidate/section-a.md",
    ROOT / "routing-v2/candidate/section-b.md",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )


def run_json(command: list[str]) -> tuple[dict[str, Any], subprocess.CompletedProcess[str]]:
    completed = run(command)
    try:
        value = json.loads(completed.stdout)
    except json.JSONDecodeError:
        value = {"status": "ERROR", "stdout": completed.stdout, "stderr": completed.stderr}
    return value, completed


def whitespace_failures() -> list[str]:
    failures: list[str] = []
    paths: set[Path] = set()
    for scan_root in IMPLEMENTATION_SCAN_ROOTS:
        if scan_root.is_file():
            paths.add(scan_root)
        elif scan_root.is_dir():
            paths.update(item for item in scan_root.rglob("*") if item.is_file())
    for path in sorted(paths):
        if not path.is_file() or path.suffix not in {".py", ".md", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if text and not text.endswith("\n"):
            failures.append(f"{path.relative_to(ROOT)}: no final newline")
        if text.endswith("\n\n"):
            failures.append(f"{path.relative_to(ROOT)}: blank line at EOF")
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip(" \t") != line:
                failures.append(f"{path.relative_to(ROOT)}:{number}: trailing whitespace")
            if re.match(r"^(?:<<<<<<<|=======|>>>>>>>)", line):
                failures.append(f"{path.relative_to(ROOT)}:{number}: conflict marker")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    failures: list[str] = []

    unit = run([sys.executable, "-m", "unittest", "discover", "-s", "routing-v2/tests", "-p", "test_*.py"])
    match = re.search(r"Ran (\d+) tests?", unit.stderr + unit.stdout)
    unit_result = {
        "status": "PASS" if unit.returncode == 0 else "FAIL",
        "tests": int(match.group(1)) if match else None,
        "returncode": unit.returncode,
    }
    if unit.returncode:
        failures.append("deterministic routing unittest suite failed")

    architecture, architecture_process = run_json([sys.executable, "routing-v2/scripts/check_candidate_architecture.py"])
    if architecture_process.returncode or architecture.get("status") != "PASS":
        failures.append("candidate architecture checker failed")

    corpus, corpus_process = run_json([sys.executable, "routing-v2/scripts/check_mcq_corpus.py"])
    if corpus_process.returncode or corpus.get("status") != "PASS":
        failures.append("frozen MCQ corpus checker failed")

    legacy, legacy_process = run_json([sys.executable, "routing-tests/scripts/check_routing.py"])
    if legacy_process.returncode or legacy.get("status") != "PASS":
        failures.append("legacy routing checker failed")

    source_integrity, source_process = run_json([sys.executable, "routing-v2/scripts/check_source_integrity.py"])
    if source_process.returncode or source_integrity.get("status") != "PASS":
        failures.append("immutable source integrity check failed")

    fixture_matrix: list[dict[str, Any]] = []
    for path in sorted(FIXTURES.glob("*.json")):
        report, completed = run_json([
            sys.executable,
            "routing-v2/scripts/validate_route_plan.py",
            str(path.relative_to(ROOT)),
            "--compact",
        ])
        expected_valid = path.name.endswith(".clean.json")
        observed_valid = completed.returncode == 0 and report.get("status") == "VALID"
        expected_failure = path.name.endswith(".fail.json") and completed.returncode == 1 and report.get("status") == "INVALID"
        matches = observed_valid if expected_valid else expected_failure
        if not matches:
            failures.append(f"fixture expectation mismatch: {path.name}")
        fixture_matrix.append({
            "fixture": path.name,
            "expected": "VALID" if expected_valid else "INVALID",
            "observed": report.get("status"),
            "exit_code": completed.returncode,
            "issue_codes": sorted({item["code"] for item in report.get("issues", [])}),
        })

    behavior_path = ROOT / "routing-v2/behavioral/evidence/report.json"
    behavior = json.loads(behavior_path.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="routing-acceptance-behavior-") as directory:
        fresh_behavior_root = Path(directory) / "evidence"
        fresh_behavior, fresh_behavior_process = run_json([
            sys.executable,
            "routing-v2/scripts/run_focused_behavioral.py",
            "--output-dir",
            str(fresh_behavior_root),
        ])
        fresh_report_bytes = (fresh_behavior_root / "report.json").read_bytes()
    retained_report_bytes = behavior_path.read_bytes()
    retained_lock = json.loads(
        (ROOT / "routing-v2/behavioral/evidence/answer-lock.json").read_text(encoding="utf-8")
    )
    retained_artifacts_valid = True
    for candidate in retained_lock.get("candidates", []):
        for item in candidate.get("outputs", []):
            retained_path = (
                ROOT
                / "routing-v2/behavioral/evidence/candidates"
                / candidate["candidate_id"]
                / item["path"]
            )
            if not retained_path.is_file() or sha256(retained_path) != item["sha256"]:
                retained_artifacts_valid = False
    for candidate in behavior.get("candidates", []):
        manifest_path = (
            ROOT
            / "routing-v2/behavioral/evidence/input-manifests"
            / f"{candidate['candidate_id']}.json"
        )
        if not manifest_path.is_file() or sha256(manifest_path) != candidate.get("input_manifest_sha256"):
            retained_artifacts_valid = False
    behavior_pass = (
        fresh_behavior_process.returncode == 0
        and fresh_behavior.get("status") == "PASS"
        and behavior.get("status") == "PASS"
        and behavior.get("candidate_count") == 2
        and behavior.get("isolation", {}).get("status") == "PASS"
        and all(all(candidate["target_checks"].values()) for candidate in behavior.get("candidates", []))
        and retained_report_bytes == fresh_report_bytes
        and retained_artifacts_valid
    )
    if not behavior_pass:
        failures.append("focused two-candidate RoutePlan behavior evidence failed")

    live_hashes = {name: sha256(ROOT / name) for name in EXPECTED_LIVE_HASHES}
    live_unchanged = live_hashes == EXPECTED_LIVE_HASHES
    if not live_unchanged:
        failures.append("live exam workflow hash changed")

    diff_check = run(["git", "diff", "--check"])
    if diff_check.returncode:
        failures.append("git diff --check failed")
    routing_whitespace = whitespace_failures()
    if routing_whitespace:
        failures.append("routing-v2 whitespace/conflict-marker scan failed")

    result = {
        "report_version": REPORT_VERSION,
        "status": "PASS" if not failures else "FAIL",
        "unit_tests": unit_result,
        "fixtures": fixture_matrix,
        "candidate_architecture": {
            "status": architecture.get("status"),
            "inventory": architecture.get("inventory"),
            "registries": architecture.get("registries"),
        },
        "mcq_corpus": {
            "status": corpus.get("status"),
            "questions": corpus.get("questions"),
            "minimal_pairs": corpus.get("minimal_pairs"),
            "answer_balance": corpus.get("answer_balance"),
        },
        "legacy_checker": {
            "status": legacy.get("status"),
            "metrics": legacy.get("metrics"),
        },
        "source_integrity": source_integrity,
        "live_workflow": {
            "status": "UNCHANGED" if live_unchanged else "CHANGED",
            "expected_hashes": EXPECTED_LIVE_HASHES,
            "actual_hashes": live_hashes,
        },
        "focused_behavioral": {
            "status": behavior.get("status"),
            "fresh_execution_status": fresh_behavior.get("status"),
            "retained_matches_fresh": retained_report_bytes == fresh_report_bytes,
            "retained_artifact_hashes_valid": retained_artifacts_valid,
            "report_sha256": sha256(behavior_path),
            "candidate_count": behavior.get("candidate_count"),
            "answer_lock_sha256": behavior.get("answer_lock_sha256"),
            "scope_note": behavior.get("scope_note"),
        },
        "diff_checks": {
            "git_diff_check": "PASS" if diff_check.returncode == 0 else "FAIL",
            "routing_v2_whitespace_scan": "PASS" if not routing_whitespace else "FAIL",
            "routing_v2_whitespace_failures": routing_whitespace,
        },
        "unresolved_evaluation_policy": [
            "Exact MCQ closest-two scoring remains undecided; gold was not relaxed.",
            "The combined 2.605m versus 905k account presentation remains undecided; gold was not relaxed."
        ],
        "activation": "NOT RUN - implementation remains candidate-only and is not a GO decision.",
        "failures": failures,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.output:
        destination = args.output if args.output.is_absolute() else ROOT / args.output
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
