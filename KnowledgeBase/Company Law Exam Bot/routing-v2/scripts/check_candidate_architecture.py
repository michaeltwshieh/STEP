#!/usr/bin/env python3
"""Static acceptance checks for the shared-routing candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "routing-v2/candidate"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_errors(path: Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_table = False
    expected = 0
    start = 0
    for number, line in enumerate(lines, 1):
        if line.startswith("|") and line.endswith("|"):
            width = len(re.split(r"(?<!\\)\|", line)) - 2
            if not in_table:
                in_table, expected, start = True, width, number
            elif width != expected:
                errors.append(f"{path.name}:{number}: table from line {start} has {width} columns, expected {expected}")
        else:
            in_table = False
    return errors


def duplicate_headings(path: Path) -> list[str]:
    seen: dict[str, int] = {}
    duplicates: list[str] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        key = f"{len(match.group(1))}:{match.group(2).casefold()}"
        if key in seen:
            duplicates.append(f"{path.name}:{number}: duplicates line {seen[key]}: {match.group(2)}")
        else:
            seen[key] = number
    return duplicates


def local_link_errors(path: Path) -> list[str]:
    errors: list[str] = []
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        target = match.group(1).split("#", 1)[0]
        if not target or re.match(r"^[a-z]+://", target):
            continue
        if not (path.parent / target).resolve().exists() and not (ROOT / target).exists():
            errors.append(f"{path.name}: unresolved local link {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    files = {
        name: CANDIDATE / name
        for name in ["Content.md", "routing-core.md", "section-a.md", "section-b.md", "CLAUDE.md"]
    }
    infrastructure = {
        "RoutePlan schema": ROOT / "routing-v2/schema/route-plan.schema.json",
        "RoutePlan validator": ROOT / "routing-v2/scripts/validate_route_plan.py",
        "isolation harness": ROOT / "routing-v2/scripts/isolation_harness.py",
        "source integrity checker": ROOT / "routing-v2/scripts/check_source_integrity.py",
        "focused behavioral runner": ROOT / "routing-v2/scripts/run_focused_behavioral.py",
        "validator tests": ROOT / "routing-v2/tests/test_route_plan_validator.py",
        "isolation tests": ROOT / "routing-v2/tests/test_isolation_harness.py",
        "focused behavioral tests": ROOT / "routing-v2/tests/test_focused_behavioral.py",
    }
    failures: list[str] = []
    warnings: list[str] = []

    for name, path in files.items():
        if not path.is_file():
            failures.append(f"missing candidate file: {name}")
    for name, path in infrastructure.items():
        if not path.is_file():
            failures.append(f"missing deterministic routing infrastructure: {name}")

    modules = sorted(ROOT.glob("Course-Manual-Module-*.md"))
    appendices = sorted(ROOT.glob("Appendix-*.md"))
    if len(modules) != 12:
        failures.append(f"module inventory: expected 12, found {len(modules)}")
    if len(appendices) != 90:
        failures.append(f"appendix inventory: expected 90, found {len(appendices)}")

    if failures:
        result = {"status": "FAIL", "failures": failures, "warnings": warnings}
        print(json.dumps(result, indent=2))
        return 1

    content = files["Content.md"].read_text(encoding="utf-8")
    core = files["routing-core.md"].read_text(encoding="utf-8")
    section_a = files["section-a.md"].read_text(encoding="utf-8")
    section_b = files["section-b.md"].read_text(encoding="utf-8")
    claude = files["CLAUDE.md"].read_text(encoding="utf-8")
    try:
        schema = json.loads(infrastructure["RoutePlan schema"].read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        failures.append(f"RoutePlan schema does not parse: {error}")
        schema = {}
    validator = infrastructure["RoutePlan validator"].read_text(encoding="utf-8")
    harness = infrastructure["isolation harness"].read_text(encoding="utf-8")

    module_refs = re.findall(r"^File: `([^`]+)`$", content, flags=re.MULTILINE)
    if len(module_refs) != 12 or len(set(module_refs)) != 12:
        failures.append(f"Content module registry must have 12 unique rows; found {len(module_refs)}/{len(set(module_refs))}")
    for filename in module_refs:
        if not (ROOT / filename).is_file():
            failures.append(f"unresolved module filename: {filename}")

    registry = re.findall(
        r"^\| \*\*([^*]+)\*\*[^|]*\| `(Appendix-[^`]+\.md)` \|",
        content,
        flags=re.MULTILINE,
    )
    labels = [label for label, _ in registry]
    registry_files = [filename for _, filename in registry]
    if len(registry) != 90 or len(set(labels)) != 90 or len(set(registry_files)) != 90:
        failures.append(
            "Content appendix registry must be bijective 90/90; "
            f"found rows={len(registry)}, labels={len(set(labels))}, files={len(set(registry_files))}"
        )
    for filename in registry_files:
        if not (ROOT / filename).is_file():
            failures.append(f"unresolved appendix filename: {filename}")
    if "25I" in labels:
        failures.append("invented Appendix 25I")

    ownership_rows = re.findall(r"^\| (\d{1,2}) \|", content, flags=re.MULTILINE)
    if ownership_rows[:12] != [str(n) for n in range(1, 13)]:
        failures.append("module ownership table does not contain ordered modules 1-12")

    for forbidden in ["## Quick topic map", "## Appendix file inventory", "## Acceptance tests for this routing index"]:
        if forbidden in content:
            failures.append(f"Content retains duplicate/non-map section: {forbidden}")

    algorithm_terms = ["Fact Disposition Ledger", "hard relevance gate", "Run two independent retrieval passes"]
    for term in algorithm_terms:
        if term in content:
            failures.append(f"Content contains routing algorithm text: {term}")

    core_required = [
        "input completeness", "namespace", "fact and claim disposition ledger", "jurisdiction",
        "regime/entity", "legal actor", "transaction/legal relationship", "lifecycle stage",
        "governing legislation", "supplied", "choice delegated", "genuinely unknown",
        "source precedence", "additive candidate-source union", "independent second pass",
        "conditional branch isolation", "mandatory", "conditional", "forbidden",
        "hard relevance gate", "exact source-passage verification", "materials-gap handling",
        "final route trace", "requested output", "necessary companion", "background/check only", "xor",
        "RoutePlan", "route-plan.schema.json", "validate_route_plan.py", "actual_open",
    ]
    lower_core = core.casefold()
    for term in core_required:
        if term.casefold() not in lower_core:
            failures.append(f"routing-core missing mechanism: {term}")
    for forbidden in ["content-test.md", "routing-prompt.md", "lear jet", "faa", "manx registry", "mr ab"]:
        if forbidden.casefold() in lower_core:
            failures.append(f"routing-core contains prohibited dependency/trigger: {forbidden}")
    if re.search(r"Course-Manual-Module-|Appendix-\d", core):
        failures.append("routing-core contains legal source mapping")

    for adapter_name, adapter in [("section-a.md", section_a), ("section-b.md", section_b)]:
        if "routing-core.md" not in adapter or "Content.md" not in adapter:
            failures.append(f"{adapter_name} does not consume Content.md and routing-core.md")
        if re.search(r"Course-Manual-Module-", adapter):
            failures.append(f"{adapter_name} contains a duplicate module map")
        for term in ["RoutePlan", "validate_route_plan.py", "VALID", "plan ID"]:
            if term.casefold() not in adapter.casefold():
                failures.append(f"{adapter_name} does not enforce validated RoutePlan rendering: {term}")

    for term in ["question stem", "polarity", "independent legal proposition", "absolute qualifier", "supported", "refuted", "partly true but not best", "materials do not resolve", "closest two", "Confidence", "Done when"]:
        if term.casefold() not in section_a.casefold():
            failures.append(f"section-a missing adapter requirement: {term}")

    for term in ["sub-part", "command word", "marks", "requested deliverables", "substantive rule", "constitution/capacity", "decision-maker/procedure", "duties/liability", "records/filings", "documents", "consequences/remedies", "legal actor", "document type", "decision method", "transaction stage", "operative part", "attachments", "execution block"]:
        if term.casefold() not in section_b.casefold():
            failures.append(f"section-b missing adapter requirement: {term}")

    for name in ["Content.md", "routing-core.md", "section-a.md", "section-b.md"]:
        if name not in claude:
            failures.append(f"CLAUDE missing workflow reference: {name}")
    for mode in ["MCQ", "PROSE", "DRAFTING"]:
        if mode not in claude:
            failures.append(f"CLAUDE missing mode: {mode}")
    for term in ["RoutePlan", "route-plan.schema.json", "validate_route_plan.py", "isolation_harness.py", "VALID"]:
        if term.casefold() not in claude.casefold():
            failures.append(f"CLAUDE missing deterministic gate: {term}")

    schema_required = {
        "answer_unit", "namespaces", "locks", "facts", "claims", "entities", "routes",
        "source_access", "xor_branch_sets", "requested_document_chain", "materials_gaps",
        "final_trace", "render_gate",
    }
    missing_schema = sorted(schema_required - set(schema.get("required", [])))
    if missing_schema:
        failures.append(f"RoutePlan schema missing required top-level fields: {missing_schema}")
    for term in [
        "FACT_CLAIM_DISPOSITIONS", "SOURCE_ALLOWLIST", "FORBIDDEN_SOURCE_ACCESS",
        "XOR_SELECTION", "BRANCH_DECIDING_FACT", "CORPORATE_ACTOR_AUTHORITY",
        "DOCUMENT_COUNT_RECONCILIATION", "ACTION_NOTICE_COMPONENTS",
        "COMPLEX_TRANSACTION_DOCUMENTS", "MATERIALS_GAP_PRESERVATION",
        "FINAL_ROUTE_TRACE",
    ]:
        if term not in validator:
            failures.append(f"RoutePlan validator missing invariant: {term}")
    for term in [
        "sandbox-exec", "answer-inputs", "answer-outputs", "answer-lock.json",
        "evaluator-inputs", "hard_isolation_failure", "prior_answer", "peer_output",
    ]:
        if term not in harness:
            failures.append(f"isolation harness missing mechanism: {term}")

    production_text = "\n".join([core, section_a, section_b, claude, validator, harness, json.dumps(schema)])
    for forbidden in ["S01", "S02", "S03", "S04", "S05", "P05B", "P08A", "P08B", "lear jet", "mr ab", "blackacre"]:
        if forbidden.casefold() in production_text.casefold():
            failures.append(f"production deterministic layer contains specimen-specific trigger: {forbidden}")

    for path in files.values():
        failures.extend(table_errors(path))
        failures.extend(duplicate_headings(path))
        failures.extend(local_link_errors(path))

    known_warning_markers = ["Appendix 7C", "Appendix 15C", "Appendix 21G", "Appendix 25E", "25I"]
    for marker in known_warning_markers:
        if marker not in content:
            failures.append(f"Content missing source warning: {marker}")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "inventory": {"modules": len(modules), "appendices": len(appendices)},
        "registries": {"modules": len(module_refs), "appendices": len(registry)},
        "candidate_hashes": {name: sha256(path) for name, path in files.items()},
        "infrastructure_hashes": {name: sha256(path) for name, path in infrastructure.items()},
        "failures": failures,
        "warnings": warnings,
    }
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
