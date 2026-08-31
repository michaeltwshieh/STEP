#!/usr/bin/env python3
"""Derive the corrected Section B oracle without altering the frozen old corpus."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT / "routing-tests/corpus/cases.json"
OUT = ROOT / "routing-v2/corpus"
QUESTION = ROOT / "routing-tests/sources/question/specimen-paper-1.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    old = json.loads(OLD.read_text(encoding="utf-8"))
    selected = {
        item["id"]: copy.deepcopy(item)
        for item in old["cases"]
        if item["id"] in {"S01", "S02", "S03", "S04", "S05", "P05B", "P08A", "P08B"}
    }

    s01 = selected["S01"]
    s01["must_open"] = [
        value.replace(" :: preceding board authority and instruction to issue notice", " :: checked procedural companion; not part of the requested notice")
        for value in s01["must_open"]
    ]
    s01["expected_document_chain"] = [
        "Appendix 25E notice frame",
        "Appendix 30B core operative business inserted into the notice: voluntary winding-up, liquidator appointment and no-audit resolution",
        "date and authorised signature",
        "proxy entitlement note",
    ]
    s01["mandatory_critical_routes"][-1] = (
        "Appendix 25E plus the KAP/course-supported core Appendix 30B operative business in the drafted notice; "
        "Appendix 25A is check-only because the requested deliverable is the notice"
    )

    p05b = selected["P05B"]
    p05b["must_open"] = [
        value for value in p05b["must_open"] if "Appendix-18B" not in value
    ] + [
        "Appendix-18B-Directors-resolution-authorising-share-transfer.md XOR Appendices 18C/18D according to the actual board decision"
    ]
    p05b["conditional"] = [
        "18B if the board approves; 18C plus 18D if it refuses; preserve both branches because the decision is not supplied",
        "27A/27B only if a nominee relationship continues for Owner B",
    ]
    p05b["expected_document_chain"] = [
        "Owner A instruction/Appendix 26 as applicable",
        "Appendix 18A executed by registered Nominee Ltd and Owner B",
        "Appendix 18B XOR Appendices 18C+18D, selected only by the board's actual decision",
        "register/certificate update only on approval",
        "beneficial ownership records update",
    ]
    p05b["mandatory_critical_routes"] = [
        "Module 6 §5.1 + Module 10 §5.3",
        "18A + (18B XOR 18C+18D)",
        "nominee is legal transferor",
    ]

    p08a = selected["P08A"]
    p08a["expected_document_chain"] = [
        "30A", "30B", "30C", "30D",
        "30G plus (30E final-meeting route XOR 30F written-approval route)",
        "Registrar dissolution filing",
    ]
    p08a["mandatory_critical_routes"] = [
        "Module 12 §3.1",
        "declaration of solvency",
        "30A-30D plus 30G and one mutually exclusive 30E/30F completion route",
        "no creditor appointment",
    ]
    p08a["unresolved_branches"] = [
        "jurisdiction-specific procedural variant",
        "30E final meeting XOR 30F written approval where the jurisdiction permits the latter",
    ]

    p08b = selected["P08B"]
    p08b["expected_document_chain"] = [
        "adapted member special resolution with no solvency recital or member appointment of liquidator (exact creditor-specific precedent absent)",
        "creditors' meeting notice/materials and creditor appointment record (course precedent gaps)",
        "adapted publication/Registrar notices only where applicable",
        "creditor and member final-meeting/approval documents (course precedent gaps)",
        "adapted final account; Appendix 30G supplies structure only",
    ]
    p08b["mandatory_critical_routes"] = [
        "Module 12 §3.2",
        "no 30A",
        "creditors appoint liquidator",
        "creditor-specific precedent gaps stated; no exact Appendix 30B-30G transplantation",
    ]

    output = {
        "schema_version": "section-b-oracle-v2",
        "derived_from": "routing-tests/corpus/cases.json",
        "old_corpus_sha256": sha256(OLD),
        "question_extract_sha256": sha256(QUESTION),
        "specimen_case_ids": ["S01", "S02", "S03", "S04", "S05"],
        "focused_regression_case_ids": ["P05B", "P08A", "P08B"],
        "cases": [selected[key] for key in ["S01", "S02", "S03", "S04", "S05", "P05B", "P08A", "P08B"]],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "section-b-oracle-v2.json"
    path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    record = f"""# Section B Oracle Amendment and Freeze Record

- Built: 2026-08-30, before new shared-architecture answers were evaluated.
- Old frozen corpus remains unchanged: `{sha256(OLD)}`.
- Question extract remains unchanged: `{sha256(QUESTION)}`.
- Corrected v2 oracle: `{sha256(path)}`.

## Source-grounded corrections

1. **S01 deliverable scope:** move Appendix 25A from the requested notice chain to a
   checked procedural companion. The question asks for a notice; KAP 1.1 points to
   Appendices 25E and 30B. Module 10 §2.2.1 still supports 25A as the prior board step.
2. **P05B branch:** replace hard approval with `18A + (18B XOR 18C+18D)`. Module 6
   §5.1 and the actual transfer articles make approval/refusal alternative board
   outcomes; the deciding fact is absent.
3. **P08A completion:** replace cumulative 30E/30F with `30G + (30E XOR 30F)`.
   Module 12 §3.1.2 states written approval is in lieu of the final meeting.
4. **P08B gap:** score creditor-specific semantics and explicit missing precedents;
   do not require exact transplantation of members' voluntary forms.

These corrections precede evaluation and are not responses to candidate outputs.
"""
    (OUT / "section-b-oracle-freeze-record.md").write_text(record, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")
    print(f"wrote {(OUT / 'section-b-oracle-freeze-record.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
