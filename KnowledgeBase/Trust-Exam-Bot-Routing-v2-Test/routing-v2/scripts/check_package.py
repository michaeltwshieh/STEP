#!/usr/bin/env python3
"""Verify the self-contained Routing v2 Trusts test package."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "SOURCE-MANIFEST.json"
EXPECTED_MODULES = 11
EXPECTED_APPENDICES = 37
EXPECTED_IMMUTABLE_SOURCES = EXPECTED_MODULES + EXPECTED_APPENDICES + 1  # submission checklist


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
        "SOURCE-MANIFEST.json",
        "submission-checklist.md",
        "routing-v2/schema/route-plan.schema.json",
        "routing-v2/scripts/check_package.py",
        "routing-v2/scripts/validate_route_plan.py",
        "routing-v2/scripts/isolation_harness.py",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    modules = sorted(ROOT.glob("Course-Manual-Module-*.md"))
    appendices = sorted(ROOT.glob("Appendix-*.md"))
    if len(modules) != EXPECTED_MODULES:
        failures.append(f"expected {EXPECTED_MODULES} modules, found {len(modules)}")
    if len(appendices) != EXPECTED_APPENDICES:
        failures.append(f"expected {EXPECTED_APPENDICES} appendices, found {len(appendices)}")
    if (ROOT / "Syllabus.md").exists():
        failures.append("Syllabus.md must not be included in the Trusts package")

    try:
        content = (ROOT / "Content.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        failures.append(f"Content.md unavailable: {error}")
        content = ""
    module_refs = re.findall(r"^File: `([^`]+)`$", content, flags=re.MULTILINE)
    # Trusts Content.md uses a bullet registry; retain support for the table form
    # so the checker remains format-tolerant if the registry is reformatted.
    appendix_refs = re.findall(
        r"^\s*-\s+\*\*Appendix\b[^`]*`(Appendix-[^`]+\.md)`",
        content,
        flags=re.MULTILINE,
    )
    if not appendix_refs:
        appendix_refs = re.findall(
            r"^\| \*\*[^*]+\*\*[^|]*\| `(Appendix-[^`]+\.md)` \|",
            content,
            flags=re.MULTILINE,
        )
    if len(module_refs) != EXPECTED_MODULES or len(set(module_refs)) != EXPECTED_MODULES:
        failures.append(f"Content.md does not contain {EXPECTED_MODULES} unique module registry paths")
    if len(appendix_refs) != EXPECTED_APPENDICES or len(set(appendix_refs)) != EXPECTED_APPENDICES:
        failures.append(f"Content.md does not contain {EXPECTED_APPENDICES} unique appendix registry paths")
    for relative in [*module_refs, *appendix_refs]:
        if not (ROOT / relative).is_file():
            failures.append(f"unresolved Content.md source path: {relative}")
    filesystem_module_paths = {path.relative_to(ROOT).as_posix() for path in modules}
    filesystem_appendix_paths = {path.relative_to(ROOT).as_posix() for path in appendices}
    if filesystem_module_paths != set(module_refs):
        failures.append(
            "filesystem module set differs from Content.md registry: "
            f"filesystem_only={sorted(filesystem_module_paths - set(module_refs))}, "
            f"registry_only={sorted(set(module_refs) - filesystem_module_paths)}"
        )
    if filesystem_appendix_paths != set(appendix_refs):
        failures.append(
            "filesystem appendix set differs from Content.md registry: "
            f"filesystem_only={sorted(filesystem_appendix_paths - set(appendix_refs))}, "
            f"registry_only={sorted(set(appendix_refs) - filesystem_appendix_paths)}"
        )

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        failures.append(f"SOURCE-MANIFEST.json unavailable: {error}")
        manifest = {"files": {}, "bundle_sha256": None}
    manifest_files = manifest.get("files", {})
    if not isinstance(manifest_files, dict):
        failures.append("SOURCE-MANIFEST.json files entry must be an object")
        manifest_files = {}
    if "Syllabus.md" in manifest_files:
        failures.append("SOURCE-MANIFEST.json must not include Syllabus.md")
    expected_manifest_paths = set(module_refs) | set(appendix_refs) | {"submission-checklist.md"}
    manifest_paths = set(manifest_files)
    missing_manifest_paths = sorted(expected_manifest_paths - manifest_paths)
    extra_manifest_paths = sorted(manifest_paths - expected_manifest_paths)
    if missing_manifest_paths:
        failures.append(f"manifest omits registered source paths: {missing_manifest_paths}")
    if extra_manifest_paths:
        failures.append(f"manifest contains unregistered source paths: {extra_manifest_paths}")
    permitted_package_paths = set(required) | expected_manifest_paths
    actual_package_paths = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    unexpected_package_paths = sorted(actual_package_paths - permitted_package_paths)
    if unexpected_package_paths:
        failures.append(f"package contains unregistered files or answer artifacts: {unexpected_package_paths}")
    actual_hashes: dict[str, str] = {}
    for relative, expected in sorted(manifest_files.items()):
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
    if len(actual_hashes) != EXPECTED_IMMUTABLE_SOURCES:
        failures.append(
            f"expected {EXPECTED_IMMUTABLE_SOURCES} immutable source hashes, found {len(actual_hashes)}"
        )
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
