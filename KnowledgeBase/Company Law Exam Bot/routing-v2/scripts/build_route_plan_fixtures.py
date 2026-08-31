#!/usr/bin/env python3
"""Materialise the generic deterministic RoutePlan regression fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "routing-v2/tests"
FIXTURES = TESTS / "fixtures"
sys.path.insert(0, str(TESTS))

from route_plan_fixture_factory import all_fixtures  # noqa: E402


def main() -> int:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    expected = all_fixtures()
    for stale in FIXTURES.glob("*.json"):
        if stale.name not in expected:
            stale.unlink()
    for name, fixture in sorted(expected.items()):
        rendered = json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
        (FIXTURES / name).write_text(rendered, encoding="utf-8")
    print(json.dumps({"status": "PASS", "fixtures": len(expected)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
