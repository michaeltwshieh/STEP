#!/usr/bin/env python3
"""Build question-only synthetic fixtures from the frozen routing corpus."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "routing-tests/corpus/cases.json"
OUTPUT = ROOT / "routing-tests/corpus/question-fixtures.json"


def main() -> None:
    corpus = json.loads(SOURCE.read_text(encoding="utf-8"))
    fixtures = [
        {
            "id": case["id"],
            "group": case["group"],
            "title": case["title"],
            "question": case["question"],
            "task_type_hint": case["task_type"],
        }
        for case in corpus["cases"]
        if case["id"].startswith("P")
    ]
    if len(fixtures) != 18:
        raise SystemExit(f"expected 18 synthetic fixtures, found {len(fixtures)}")
    allowed = {"id", "group", "title", "question", "task_type_hint"}
    if any(set(fixture) != allowed for fixture in fixtures):
        raise SystemExit("question fixture leaked an unexpected field")
    payload = {
        "schema_version": "1.0",
        "source_corpus_sha256": "7a0010d184925ad20ff12f61a60ba059e4a4e68fd6cee102c2694fedf37abed9",
        "fixture_count": len(fixtures),
        "fixtures": fixtures,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(fixtures)} question-only fixtures")


if __name__ == "__main__":
    main()
