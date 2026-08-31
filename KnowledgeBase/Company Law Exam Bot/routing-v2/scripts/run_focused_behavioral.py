#!/usr/bin/env python3
"""Run two isolated focused RoutePlan candidates and retain acceptance evidence."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "routing-v2/scripts"
TESTS = ROOT / "routing-v2/tests"
sys.dont_write_bytecode = True
sys.path.insert(0, str(SCRIPTS))

from isolation_harness import (  # noqa: E402
    isolation_report,
    lock_answers,
    prepare_answer_inputs,
    prepare_evaluator_inputs,
    run_answer,
    run_paths,
    SANDBOX_PYTHON,
    sha256,
    stage_output,
    write_json,
)
from validate_route_plan import DEFAULT_SCHEMA, validate  # noqa: E402


QUESTION = ROOT / "routing-v2/behavioral/focused-case-manifest.json"
BUILDER = ROOT / "routing-v2/behavioral/behavioral_candidate_builder.py"
FACTORY = TESTS / "route_plan_fixture_factory.py"
WORKFLOW = [
    ROOT / "routing-v2/candidate/CLAUDE.md",
    ROOT / "routing-v2/candidate/Content.md",
    ROOT / "routing-v2/candidate/routing-core.md",
    ROOT / "routing-v2/candidate/section-a.md",
    ROOT / "routing-v2/candidate/section-b.md",
    BUILDER,
    FACTORY,
    ROOT / "routing-v2/scripts/validate_route_plan.py",
    DEFAULT_SCHEMA,
]
COURSE = [
    ROOT / "Course-Manual-Module-03-Company-Formation-and-Related-Issues.md",
    ROOT / "Course-Manual-Module-06-Equity-Capital-and-Distributions.md",
    ROOT / "Course-Manual-Module-10-Company-Decision-making-Procedures.md",
    ROOT / "Course-Manual-Module-12-Termination-of-Companies.md",
    ROOT / "Appendix-7C-Register-of-charges.md",
    ROOT / "Appendix-18A-Share-transfer-form.md",
    ROOT / "Appendix-18B-Directors-resolution-authorising-share-transfer.md",
    ROOT / "Appendix-18C-Directors-resolution-refusing-to-register-share-transfer.md",
    ROOT / "Appendix-18D-Notice-of-refusal-to-register-share-transfer.md",
    ROOT / "Appendix-25E-Notice-of-general-meeting-to-pass-a-specific.md",
    ROOT / "Appendix-25H-Directors-resolution-to-appoint-corporate.md",
    ROOT / "Appendix-25J-Notice-to-company-of-appointment-of-corporate.md",
    ROOT / "Appendix-25N-Directors-resolution-to-approve-complex-borrowing.md",
    ROOT / "Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md",
    ROOT / "Appendix-30E-Notice-of-final-general-meeting-of-the-company.md",
    ROOT / "Appendix-30F-Members-resolutions-approving-liquidators-statement-of.md",
    ROOT / "Appendix-30G-Liquidators-statement-of-account.md",
]
EVALUATION_ONLY = [
    ROOT / "routing-v2/corpus/mcq-20-gold.json",
    ROOT / "routing-v2/corpus/section-b-oracle-v2.json",
    ROOT / "routing-tests/sources/kap/specimen-paper-1-kap.txt",
]


def target_checks(plans: dict[str, dict[str, Any]]) -> dict[str, bool]:
    notice = plans["action"]["requested_document_chain"]["instruments"][0]
    selected = set(notice["selected_action_component_ids"])
    present = {
        item["source_component_id"]
        for item in notice["operative_components"]
        if item["status"] in {"produced", "placeholder"}
    }

    managed = plans["managed"]
    instruments = managed["requested_document_chain"]["instruments"]
    attachment_kinds = {
        item["kind"]
        for document in instruments
        for item in document["attachments"]
        if item["status"] in {"produced", "placeholder"}
    }
    corporate_authorities = all(
        document["upstream_authority_instrument_id"]
        for document in instruments
        if document["target_company_act"] and document["actor_id"] in {"E_member", "E_director"}
    )
    charge_entry = any(
        item["kind"] == "register_of_charges" and item["status"] == "produced"
        for document in instruments
        for item in document["records_filings"]
    )

    transfer_xor = plans["transfer"]["xor_branch_sets"][0]
    completion_xor = plans["completion"]["xor_branch_sets"][0]
    source_access_ok = all(
        not (
            set(item["path"] for item in plan["source_access"]["actual_open"])
            & (set(plan["source_access"]["forbidden_paths"]) | set(plan["source_access"]["prior_answer_paths"]))
        )
        for plan in plans.values()
    )
    return {
        "action_notice_all_selected_operatives": selected <= present and len(selected) >= 3,
        "managed_distinct_bill_facility_security_registry": {
            "conveyance_bill_of_sale", "facility", "security", "registry"
        } <= attachment_kinds,
        "managed_both_corporate_authorities": corporate_authorities,
        "managed_actual_charge_register_entry": charge_entry,
        "transfer_unresolved_without_hard_selection": transfer_xor["selection_state"] == "unresolved" and not transfer_xor["selected_route_ids"],
        "completion_routes_not_cumulative": len(completion_xor["selected_route_ids"]) <= 1,
        "forbidden_and_prior_sources_not_opened": source_access_ok,
    }


def run(output_dir: Path) -> dict[str, Any]:
    schema = json.loads(DEFAULT_SCHEMA.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="routing-focused-behavioral-") as directory:
        run_dir = Path(directory)
        candidate_results: list[dict[str, Any]] = []
        for candidate_id in ("candidate-a", "candidate-b"):
            answer_manifest = prepare_answer_inputs(
                run_dir,
                ROOT,
                candidate_id,
                QUESTION,
                WORKFLOW,
                COURSE,
            )
            declared = [
                "question/focused-case-manifest.json",
                *[f"workflow/{path.name}" for path in WORKFLOW],
                *[f"course/{path.name}" for path in COURSE],
            ]
            command_result = run_answer(
                run_dir,
                candidate_id,
                [str(SANDBOX_PYTHON), "workflow/behavioral_candidate_builder.py", "--variant", candidate_id],
                declared,
            )
            if command_result["returncode"] != 0:
                raise RuntimeError(f"isolated candidate failed: {candidate_id}")
            candidate_paths = run_paths(run_dir, candidate_id)
            package = json.loads((candidate_paths["output"] / "package.json").read_text(encoding="utf-8"))
            plans: dict[str, dict[str, Any]] = {}
            validations: list[dict[str, Any]] = []
            for entry in package["plans"]:
                plan_path = candidate_paths["output"] / entry["path"]
                if sha256(plan_path) != entry["sha256"]:
                    raise RuntimeError(f"candidate package hash mismatch: {candidate_id}/{entry['label']}")
                plan = json.loads(plan_path.read_text(encoding="utf-8"))
                report, exit_code = validate(plan, schema)
                if exit_code != 0:
                    raise RuntimeError(f"invalid focused RoutePlan: {candidate_id}/{entry['label']}: {report['issues']}")
                plans[entry["label"]] = plan
                report_path = candidate_paths["output"] / entry["validation_path"]
                candidate_report = json.loads(report_path.read_text(encoding="utf-8"))
                if sha256(report_path) != entry["validation_sha256"] or candidate_report != report:
                    raise RuntimeError(
                        f"candidate pre-render validation report mismatch: {candidate_id}/{entry['label']}"
                    )
                validations.append({
                    "label": entry["label"],
                    "status": report["status"],
                    "plan_sha256": report["plan_sha256"],
                    "report_sha256": sha256(report_path),
                })
            checks = target_checks(plans)
            if not all(checks.values()):
                raise RuntimeError(f"focused target check failed: {candidate_id}: {checks}")
            for output_path in sorted(candidate_paths["output"].rglob("*")):
                if output_path.is_file():
                    stage_output(run_dir, candidate_id, output_path)
            candidate_results.append({
                "candidate_id": candidate_id,
                "input_manifest_sha256": sha256(candidate_paths["manifest"]),
                "input_file_count": len(answer_manifest["files"]),
                "input_categories": sorted({item["category"] for item in answer_manifest["files"]}),
                "command": command_result,
                "validations": validations,
                "target_checks": checks,
            })

        answer_lock = lock_answers(run_dir, ["candidate-a", "candidate-b"])
        evaluator = prepare_evaluator_inputs(run_dir, ROOT, EVALUATION_ONLY)
        isolation = isolation_report(run_dir)
        if isolation["status"] != "PASS":
            raise RuntimeError(f"unexpected isolation failure: {isolation}")

        evidence_root = output_dir / "candidates"
        manifest_root = output_dir / "input-manifests"
        manifest_root.mkdir(exist_ok=True)
        for candidate_id in ("candidate-a", "candidate-b"):
            source = run_paths(run_dir, candidate_id)["output"]
            shutil.copytree(source, evidence_root / candidate_id, dirs_exist_ok=True)
            shutil.copyfile(
                run_paths(run_dir, candidate_id)["manifest"],
                manifest_root / f"{candidate_id}.json",
            )
        write_json(output_dir / "answer-lock.json", answer_lock)

        result = {
            "report_version": "focused-route-plan-behavioral-report-v1",
            "status": "PASS",
            "candidate_count": 2,
            "case_refs": ["S01", "S02", "P05B", "P08A"],
            "candidates": candidate_results,
            "answer_lock_sha256": sha256(output_dir / "answer-lock.json"),
            "isolation": isolation,
            "evaluator_release": {
                "state": evaluator["state"],
                "answer_lock_sha256": evaluator["answer_lock_sha256"],
                "evaluation_only_basenames": sorted(path.name for path in EVALUATION_ONLY),
            },
            "policy_decisions_not_relaxed": [
                "Exact MCQ closest-two scoring remains an evaluation-policy decision.",
                "The combined 2.605m versus 905k account presentation remains an evaluation-policy decision."
            ],
            "scope_note": "Focused deterministic RoutePlan candidate run; not a full Section A/Section B activation audit and not a GO decision."
        }
        write_json(output_dir / "report.json", result)
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "routing-v2/behavioral/evidence",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result = run(args.output_dir)
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
