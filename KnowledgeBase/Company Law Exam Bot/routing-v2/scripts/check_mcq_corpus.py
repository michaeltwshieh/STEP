#!/usr/bin/env python3
"""Validate the frozen 20-item synthetic MCQ corpus and question fixture."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "routing-v2/corpus"
GOLD = CORPUS / "mcq-20-gold.json"
FIXTURE = CORPUS / "mcq-20-questions.json"
FREEZE = CORPUS / "mcq-freeze-record.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    gold = json.loads(GOLD.read_text(encoding="utf-8"))
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    questions = gold.get("questions", [])
    fixtures = fixture.get("questions", [])

    if len(questions) != 20:
        failures.append(f"expected 20 gold questions, found {len(questions)}")
    if len(fixtures) != 20:
        failures.append(f"expected 20 fixture questions, found {len(fixtures)}")
    ids = [item.get("id") for item in questions]
    if len(set(ids)) != 20:
        failures.append("question ids are not unique")
    pairs = Counter(item.get("pair_id") for item in questions)
    if len(pairs) != 10 or any(count != 2 for count in pairs.values()):
        failures.append(f"expected ten two-item pairs, found {dict(pairs)}")

    required_gold = {
        "correct_letter", "governing_proposition", "must_open", "conditional",
        "must_not_open", "option_by_option_verdict", "closest_two",
        "critical_distinction", "exact_course_source_rationale", "expected_confidence",
    }
    allowed_verdicts = {"supported", "refuted", "partly true but not best", "materials do not resolve"}
    letters: list[str] = []
    combined_text = json.dumps(gold, ensure_ascii=False).casefold()

    for item in questions:
        id_ = item.get("id", "unknown")
        if set(item.get("options", {})) != set("ABCD"):
            failures.append(f"{id_}: options are not exactly A-D")
        if set(item.get("gold", {})) != required_gold:
            failures.append(f"{id_}: incomplete or extra gold fields")
            continue
        answer = item["gold"]["correct_letter"]
        letters.append(answer)
        if answer not in "ABCD":
            failures.append(f"{id_}: invalid answer letter {answer}")
        dispositions = item["gold"]["option_by_option_verdict"]
        if set(dispositions) != set("ABCD"):
            failures.append(f"{id_}: dispositions are not exactly A-D")
        for letter, disposition in dispositions.items():
            if disposition.get("verdict") not in allowed_verdicts:
                failures.append(f"{id_}/{letter}: invalid verdict {disposition.get('verdict')}")
            if not disposition.get("reason"):
                failures.append(f"{id_}/{letter}: missing verdict reason")
        if len(item["gold"]["closest_two"]) != 2:
            failures.append(f"{id_}: closest_two must contain two letters")
        if not item["gold"]["must_open"] or not item["gold"]["must_not_open"]:
            failures.append(f"{id_}: must_open and must_not_open must be non-empty")
        if not item["gold"]["exact_course_source_rationale"]:
            failures.append(f"{id_}: exact source rationale missing")

        encoded = json.dumps(item, ensure_ascii=False)
        for filename in re.findall(r"(?:Course-Manual|Appendix)-[A-Za-z0-9][A-Za-z0-9.-]*\.md", encoded):
            if not (ROOT / filename).is_file():
                failures.append(f"{id_}: unresolved source filename {filename}")

    if Counter(letters) != Counter({"A": 5, "B": 5, "C": 5, "D": 5}):
        failures.append(f"answer letters are not balanced 5 each: {dict(Counter(letters))}")

    fixture_by_id = {item["id"]: item for item in fixtures}
    for item in questions:
        public = {key: value for key, value in item.items() if key != "gold"}
        if fixture_by_id.get(item["id"]) != public:
            failures.append(f"{item['id']}: fixture differs from gold question fields")
    if '"gold"' in FIXTURE.read_text(encoding="utf-8"):
        failures.append("question-only fixture leaks gold")

    for marker in ["correct", "incorrect", "not contradicted", "except", "must", "only", "always", "may", "best"]:
        if marker not in combined_text:
            failures.append(f"missing required polarity/qualifier marker: {marker}")
    topic_markers = [
        "traditional", "bvi", "transfer", "transmission", "legal title", "beneficial",
        "capacity", "authority", "shareholders", "directors", "registered office",
        "migration", "allotment", "issue", "secretary", "registered agent",
        "corporate representative", "winding-up", "striking off", "reinstatement",
        "materials gap",
    ]
    for marker in topic_markers:
        if marker not in combined_text:
            failures.append(f"missing required topic marker: {marker}")

    freeze = FREEZE.read_text(encoding="utf-8")
    if sha256(GOLD) not in freeze or sha256(FIXTURE) not in freeze:
        failures.append("freeze record hashes do not match corpus files")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "questions": len(questions),
        "minimal_pairs": len(pairs),
        "answer_balance": dict(Counter(letters)),
        "gold_sha256": sha256(GOLD),
        "fixture_sha256": sha256(FIXTURE),
        "failures": failures,
    }
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
