#!/usr/bin/env python3
"""Verify immutable course/question/KAP sources against the implementation baseline."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_BUNDLE_SHA256 = "43eadd34fa7a613e0741aa5e0415d989b2bb3442446a3c290a89b802122d2c7e"
EXPECTED_INDIVIDUAL = {
    "Syllabus.md": "6d6b24a63f8e08203660b90b675a6405060d144dc59046672b2d906184a3a519",
    "routing-tests/sources/question/specimen-paper-1.txt": "07d07ec52ed17dc4d0fe360d297ba8c88d9c48fae9f27c2da7b94cbf68b198a6",
    "routing-tests/sources/kap/specimen-paper-1-kap.txt": "cc9fc7ce0e0b77dae24d1758f9e7ccab7a790a520436e425162bccd9d5659350",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = sorted(
        [
            *ROOT.glob("Course-Manual-Module-*.md"),
            *ROOT.glob("Appendix-*.md"),
            ROOT / "Syllabus.md",
            ROOT / "routing-tests/sources/question/specimen-paper-1.txt",
            ROOT / "routing-tests/sources/kap/specimen-paper-1-kap.txt",
        ],
        key=lambda item: item.relative_to(ROOT).as_posix(),
    )
    manifest = {
        path.relative_to(ROOT).as_posix(): sha256(path)
        for path in paths
        if path.is_file()
    }
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    bundle_hash = hashlib.sha256(canonical).hexdigest()
    failures: list[str] = []
    if len(list(ROOT.glob("Course-Manual-Module-*.md"))) != 12:
        failures.append("course module inventory is not 12")
    if len(list(ROOT.glob("Appendix-*.md"))) != 90:
        failures.append("course appendix inventory is not 90")
    if len(manifest) != 105:
        failures.append(f"immutable source inventory is not 105: {len(manifest)}")
    if bundle_hash != EXPECTED_BUNDLE_SHA256:
        failures.append("immutable source bundle hash changed")
    for relative, expected in EXPECTED_INDIVIDUAL.items():
        if manifest.get(relative) != expected:
            failures.append(f"frozen source hash changed: {relative}")
    result = {
        "status": "PASS" if not failures else "FAIL",
        "inventory": {
            "modules": len(list(ROOT.glob("Course-Manual-Module-*.md"))),
            "appendices": len(list(ROOT.glob("Appendix-*.md"))),
            "immutable_sources": len(manifest),
        },
        "expected_bundle_sha256": EXPECTED_BUNDLE_SHA256,
        "actual_bundle_sha256": bundle_hash,
        "failures": failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
