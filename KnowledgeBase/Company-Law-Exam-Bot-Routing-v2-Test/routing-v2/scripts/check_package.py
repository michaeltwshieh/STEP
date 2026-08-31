#!/usr/bin/env python3
"""Verify the self-contained Routing v2 Company Law test package."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "SOURCE-MANIFEST.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    required = [
        "AGENTS.md",
        "CLAUDE.md",
        "README.md",
        "Content.md",
        "routing-core.md",
        "section-a.md",
        "section-b.md",
        "Syllabus.md",
        "submission-checklist.md",
        "routing-v2/schema/route-plan.schema.json",
        "routing-v2/scripts/validate_route_plan.py",
        "routing-v2/scripts/isolation_harness.py",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    modules = sorted(ROOT.glob("Course-Manual-Module-*.md"))
    appendices = sorted(ROOT.glob("Appendix-*.md"))
    if len(modules) != 12:
        failures.append(f"expected 12 modules, found {len(modules)}")
    if len(appendices) != 90:
        failures.append(f"expected 90 appendices, found {len(appendices)}")

    content = (ROOT / "Content.md").read_text(encoding="utf-8")
    module_refs = re.findall(r"^File: `([^`]+)`$", content, flags=re.MULTILINE)
    appendix_refs = re.findall(
        r"^\| \*\*[^*]+\*\*[^|]*\| `(Appendix-[^`]+\.md)` \|",
        content,
        flags=re.MULTILINE,
    )
    if len(module_refs) != 12 or len(set(module_refs)) != 12:
        failures.append("Content.md does not contain 12 unique module registry paths")
    if len(appendix_refs) != 90 or len(set(appendix_refs)) != 90:
        failures.append("Content.md does not contain 90 unique appendix registry paths")
    for relative in [*module_refs, *appendix_refs]:
        if not (ROOT / relative).is_file():
            failures.append(f"unresolved Content.md source path: {relative}")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        failures.append(f"SOURCE-MANIFEST.json unavailable: {error}")
        manifest = {"files": {}, "bundle_sha256": None}
    actual_hashes: dict[str, str] = {}
    for relative, expected in sorted(manifest.get("files", {}).items()):
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"manifest file missing: {relative}")
            continue
        actual = sha256(path)
        actual_hashes[relative] = actual
        if actual != expected:
            failures.append(f"source hash changed: {relative}")
    canonical = json.dumps(actual_hashes, sort_keys=True, separators=(",", ":")).encode("utf-8")
    bundle_hash = hashlib.sha256(canonical).hexdigest()
    if len(actual_hashes) != 104:
        failures.append(f"expected 104 immutable source hashes, found {len(actual_hashes)}")
    if bundle_hash != manifest.get("bundle_sha256"):
        failures.append("immutable source bundle hash changed")

    symlinks = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_symlink())
    if symlinks:
        failures.append(f"package contains symlinks: {symlinks}")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "inventory": {
            "modules": len(modules),
            "appendices": len(appendices),
            "immutable_sources": len(actual_hashes),
        },
        "content_registry": {
            "modules": len(module_refs),
            "appendices": len(appendix_refs),
        },
        "bundle_sha256": bundle_hash,
        "failures": failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
