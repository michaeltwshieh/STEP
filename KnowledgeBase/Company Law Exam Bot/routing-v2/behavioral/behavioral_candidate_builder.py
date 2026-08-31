#!/usr/bin/env python3
"""Build one of two structurally independent focused RoutePlan packages.

This is test-only behavioral-fixture code.  It runs inside the isolation harness and
sees the question-only case manifest, candidate workflow, and allowlisted course files.
It never receives gold, KAP, prior answers or peer output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any


WORKFLOW_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(WORKFLOW_ROOT))

from route_plan_fixture_factory import (  # noqa: E402
    action_notice_clean,
    final_completion_clean,
    instrument,
    managed_borrowing_clean,
    recalculate_counts,
    rebuild_indexes,
    route,
    source_access_clean,
    transfer_unresolved_clean,
)
from validate_route_plan import validate  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_target_routes(plans: dict[str, dict[str, Any]]) -> None:
    plans["action"]["routes"].append(
        route("R_notice_frame", "course_appendix", "course/notice-frame.md")
    )
    plans["managed"]["routes"].extend([
        route("R_complex_precedent", "course_appendix", "course/complex-precedent.md"),
        route("R_charge_register", "course_appendix", "course/charge-register.md"),
        route("R_corporate_authority", "course_appendix", "course/corporate-authority.md"),
    ])
    plans["transfer"]["routes"].append(
        route("R_transfer_instrument", "course_appendix", "course/transfer-instrument.md")
    )
    for plan in plans.values():
        rebuild_indexes(plan)
        recalculate_counts(plan)


def apply_candidate_b_variation(plans: dict[str, dict[str, Any]]) -> None:
    for label, plan in plans.items():
        plan["plan_id"] = f"Behavioral_candidate_b_{label}"

    notice = plans["action"]["requested_document_chain"]["instruments"][0]
    notice["operative_components"] = list(reversed([
        {**item, "id": f"B_{item['id']}"}
        for item in notice["operative_components"]
    ]))

    managed = plans["managed"]
    resolution = next(
        item for item in managed["requested_document_chain"]["instruments"]
        if item["id"] == "I_complex_resolution"
    )
    bill = next(item for item in resolution["attachments"] if item["kind"] == "conveyance_bill_of_sale")
    resolution["attachments"] = [item for item in resolution["attachments"] if item["kind"] != "conveyance_bill_of_sale"]
    managed["requested_document_chain"]["instruments"].append(
        instrument(
            "I_distinct_conveyance",
            6,
            "conveyance",
            "E_owner",
            attachments=[{**bill, "id": "A_distinct_conveyance"}],
        )
    )

    plans["transfer"]["routes"] = list(reversed(plans["transfer"]["routes"]))

    completion = plans["completion"]
    meeting = next(item for item in completion["routes"] if item["id"] == "R_final_meeting")
    written = next(item for item in completion["routes"] if item["id"] == "R_written_approval")
    meeting["verdict"] = "conditional"
    meeting["deciding_fact_ids"] = []
    written["verdict"] = "incorporated"
    written["deciding_fact_ids"] = ["F_completion_method"]
    completion["xor_branch_sets"][0]["selected_route_ids"] = ["R_written_approval"]

    for plan in plans.values():
        rebuild_indexes(plan)
        recalculate_counts(plan)


def bind_real_isolated_sources(plan: dict[str, Any], manifest: dict[str, Any], input_root: Path) -> None:
    files = {item["virtual_path"]: item for item in manifest["files"]}
    questions = sorted(path for path, item in files.items() if item["category"] == "question")
    manuals = sorted(
        path for path, item in files.items()
        if item["category"] == "course" and Path(path).name.startswith("Course-Manual-")
    )
    appendices = sorted(
        path for path, item in files.items()
        if item["category"] == "course" and Path(path).name.startswith("Appendix-")
    )
    if len(questions) != 1 or not manuals or not appendices:
        raise RuntimeError("isolated manifest lacks the focused question/manual/appendix inputs")

    manual_index = 0
    appendix_index = 0
    for item in plan["routes"]:
        source = item["source"]
        if item["verdict"] == "forbidden":
            continue
        if source["namespace"] == "exam_question":
            source["path"] = questions[0]
        elif source["namespace"] == "course_manual":
            source["path"] = manuals[manual_index % len(manuals)]
            manual_index += 1
        elif source["namespace"] == "course_appendix":
            source["path"] = appendices[appendix_index % len(appendices)]
            appendix_index += 1

    rebuild_indexes(plan)
    actual_open: list[dict[str, str]] = []
    for entry in plan["source_access"]["allowlist"]:
        virtual = entry["path"]
        if virtual not in files:
            raise RuntimeError(f"RoutePlan allowlist is outside isolated manifest: {virtual}")
        observed = sha256(input_root / virtual)
        if observed != files[virtual]["sha256"]:
            raise RuntimeError(f"isolated course input changed: {virtual}")
        actual_open.append({**entry, "sha256": observed})
    plan["source_access"]["actual_open"] = actual_open


def build(variant: str) -> dict[str, Any]:
    input_root = Path(os.environ["ROUTING_INPUT_ROOT"])
    output_root = Path(os.environ["ROUTING_OUTPUT_ROOT"])
    manifest = json.loads((input_root / "manifest.json").read_text(encoding="utf-8"))
    case_manifest_path = next(
        input_root / item["virtual_path"]
        for item in manifest["files"]
        if item["category"] == "question"
    )
    case_manifest = json.loads(case_manifest_path.read_text(encoding="utf-8"))
    if case_manifest.get("case_refs") != ["S01", "S02", "P05B", "P08A"]:
        raise RuntimeError("unexpected focused case references")

    plans = {
        "action": action_notice_clean(),
        "managed": managed_borrowing_clean(),
        "transfer": transfer_unresolved_clean(),
        "completion": final_completion_clean(),
        "source_access": source_access_clean(),
    }
    add_target_routes(plans)
    prefix = "a" if variant == "candidate-a" else "b"
    for label, plan in plans.items():
        plan["plan_id"] = f"Behavioral_candidate_{prefix}_{label}"
    if variant == "candidate-b":
        apply_candidate_b_variation(plans)

    plans_root = output_root / "plans"
    validation_root = output_root / "validation"
    plans_root.mkdir(parents=True, exist_ok=True)
    validation_root.mkdir(parents=True, exist_ok=True)
    schema = json.loads((WORKFLOW_ROOT / "route-plan.schema.json").read_text(encoding="utf-8"))
    package_entries: list[dict[str, str]] = []
    for label, plan in sorted(plans.items()):
        bind_real_isolated_sources(plan, manifest, input_root)
        destination = plans_root / f"{label}.json"
        destination.write_text(
            json.dumps(plan, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        validation_report, exit_code = validate(plan, schema)
        if exit_code != 0:
            raise RuntimeError(f"candidate RoutePlan failed its pre-render gate: {label}")
        validation_path = validation_root / f"{label}.json"
        validation_path.write_text(
            json.dumps(validation_report, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        package_entries.append({
            "label": label,
            "path": f"plans/{label}.json",
            "sha256": sha256(destination),
            "validation_path": f"validation/{label}.json",
            "validation_sha256": sha256(validation_path),
        })

    package = {
        "schema": "focused-route-plan-candidate-package-v1",
        "candidate_id": variant,
        "case_refs": case_manifest["case_refs"],
        "plans": package_entries,
    }
    (output_root / "package.json").write_text(
        json.dumps(package, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return package


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=["candidate-a", "candidate-b"], required=True)
    args = parser.parse_args()
    package = build(args.variant)
    print(json.dumps({"status": "PASS", "candidate_id": package["candidate_id"], "plans": len(package["plans"])}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
