#!/usr/bin/env python3
"""Verify the self-contained Routing v2 Trusts test package."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_MODULES = 11
EXPECTED_APPENDICES = 37
EXPECTED_IMMUTABLE_SOURCES = EXPECTED_MODULES + EXPECTED_APPENDICES + 1
MANIFEST_SCHEMA_V2 = "trusts-routing-v2-source-manifest-v2"
REQUIRED_WORKFLOW_PATHS = (
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
)
EXPECTED_WORKFLOW_PATHS = {
    "AGENTS.md",
    "CLAUDE.md",
    "Content.md",
    "README.md",
    "routing-core.md",
    "routing-v2/schema/route-plan.schema.json",
    "routing-v2/scripts/check_package.py",
    "routing-v2/scripts/isolation_harness.py",
    "routing-v2/scripts/validate_route_plan.py",
    "routing-v2/tests/test_check_package.py",
    "routing-v2/tests/test_isolation_harness.py",
    "routing-v2/tests/test_validate_route_plan.py",
    "section-a.md",
    "section-b.md",
}
DEVELOPMENT_PREFIXES = ("answers", "evaluation", "routing-v2/artifacts", "tmp")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bundle_sha256(hashes: dict[str, str]) -> str:
    canonical = json.dumps(hashes, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def under_prefix(relative: str, prefixes: Iterable[str]) -> bool:
    return any(relative == prefix or relative.startswith(f"{prefix}/") for prefix in prefixes)


def load_hash_map(
    manifest: dict[str, Any],
    key: str,
    failures: list[str],
    *,
    required: bool,
) -> dict[str, str]:
    value = manifest.get(key)
    if value is None and not required:
        return {}
    if not isinstance(value, dict):
        failures.append(f"SOURCE-MANIFEST.json {key} entry must be an object")
        return {}
    result: dict[str, str] = {}
    for relative, expected in value.items():
        if not isinstance(relative, str) or not isinstance(expected, str):
            failures.append(f"SOURCE-MANIFEST.json {key} must map path strings to hash strings")
            continue
        result[relative] = expected
    return result


def validate_hashes(
    root: Path,
    registered: dict[str, str],
    label: str,
    failures: list[str],
) -> dict[str, str]:
    actual_hashes: dict[str, str] = {}
    for relative, expected in sorted(registered.items()):
        path = root / relative
        if not path.is_file() or path.is_symlink():
            failures.append(f"{label} file missing or not a regular file: {relative}")
            continue
        actual = sha256(path)
        actual_hashes[relative] = actual
        if actual != expected:
            failures.append(f"{label} hash changed: {relative}")
    return actual_hashes


def check_package(root: Path = ROOT, allow_development_artifacts: bool = False) -> dict[str, Any]:
    root = root.resolve()
    manifest_path = root / "SOURCE-MANIFEST.json"
    failures: list[str] = []

    for relative in REQUIRED_WORKFLOW_PATHS:
        path = root / relative
        if not path.is_file() or path.is_symlink():
            failures.append(f"missing required workflow file: {relative}")

    modules = sorted(root.glob("Course-Manual-Module-*.md"))
    appendices = sorted(root.glob("Appendix-*.md"))
    if len(modules) != EXPECTED_MODULES:
        failures.append(f"expected {EXPECTED_MODULES} modules, found {len(modules)}")
    if len(appendices) != EXPECTED_APPENDICES:
        failures.append(f"expected {EXPECTED_APPENDICES} appendices, found {len(appendices)}")
    if (root / "Syllabus.md").exists():
        failures.append("Syllabus.md must not be included in the Trusts package")

    try:
        content = (root / "Content.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        failures.append(f"Content.md unavailable: {error}")
        content = ""
    module_refs = re.findall(r"^File: `([^`]+)`$", content, flags=re.MULTILINE)
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
        if not (root / relative).is_file():
            failures.append(f"unresolved Content.md source path: {relative}")

    filesystem_module_paths = {path.relative_to(root).as_posix() for path in modules}
    filesystem_appendix_paths = {path.relative_to(root).as_posix() for path in appendices}
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
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("top-level value is not an object")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        failures.append(f"SOURCE-MANIFEST.json unavailable: {error}")
        manifest = {}

    manifest_files = load_hash_map(manifest, "files", failures, required=True)
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

    schema = manifest.get("schema")
    if schema == MANIFEST_SCHEMA_V2:
        workflow_files = load_hash_map(manifest, "workflow_files", failures, required=True)
        missing_workflow_paths = sorted(EXPECTED_WORKFLOW_PATHS - set(workflow_files))
        extra_workflow_paths = sorted(set(workflow_files) - EXPECTED_WORKFLOW_PATHS)
        if missing_workflow_paths:
            failures.append(f"manifest omits required workflow paths: {missing_workflow_paths}")
        if extra_workflow_paths:
            failures.append(f"manifest contains unregistered workflow paths: {extra_workflow_paths}")
    else:
        workflow_files = {}
        failures.append(f"unsupported SOURCE-MANIFEST.json schema: {schema!r}")

    workflow_development_paths = sorted(
        relative
        for relative in workflow_files
        if under_prefix(relative, DEVELOPMENT_PREFIXES)
    )
    if workflow_development_paths:
        failures.append(
            "workflow manifest contains development artifact paths: "
            f"{workflow_development_paths}"
        )
    overlap = sorted(set(manifest_files) & set(workflow_files))
    if overlap:
        failures.append(f"source and workflow manifest paths overlap: {overlap}")

    actual_source_hashes = validate_hashes(root, manifest_files, "source", failures)
    source_bundle_hash = bundle_sha256(actual_source_hashes)
    if len(actual_source_hashes) != EXPECTED_IMMUTABLE_SOURCES:
        failures.append(
            f"expected {EXPECTED_IMMUTABLE_SOURCES} immutable source hashes, "
            f"found {len(actual_source_hashes)}"
        )
    if source_bundle_hash != manifest.get("bundle_sha256"):
        failures.append("immutable source bundle hash changed")

    actual_workflow_hashes = validate_hashes(root, workflow_files, "workflow", failures)
    workflow_bundle_hash = bundle_sha256(actual_workflow_hashes) if schema == MANIFEST_SCHEMA_V2 else None
    if schema == MANIFEST_SCHEMA_V2 and not isinstance(manifest.get("workflow_bundle_sha256"), str):
        failures.append("SOURCE-MANIFEST.json workflow_bundle_sha256 entry must be a hash string")
    elif schema == MANIFEST_SCHEMA_V2 and workflow_bundle_hash != manifest.get("workflow_bundle_sha256"):
        failures.append("workflow bundle hash changed")

    symlinks = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_symlink()
    )
    if symlinks:
        failures.append(f"package contains symlinks: {symlinks}")

    permitted_package_paths = set(REQUIRED_WORKFLOW_PATHS) | expected_manifest_paths | set(workflow_files)
    actual_package_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.name != ".DS_Store" and not path.is_symlink()
    }
    development_artifact_paths = sorted(
        relative
        for relative in actual_package_paths
        if under_prefix(relative, DEVELOPMENT_PREFIXES)
    )
    if development_artifact_paths and not allow_development_artifacts:
        failures.append(
            "package contains development artifacts forbidden in clean-distribution mode: "
            f"{development_artifact_paths}"
        )
    unexpected = actual_package_paths - permitted_package_paths
    if allow_development_artifacts:
        unexpected = {
            relative for relative in unexpected if not under_prefix(relative, DEVELOPMENT_PREFIXES)
        }
    unexpected_package_paths = sorted(unexpected)
    if unexpected_package_paths:
        failures.append(
            "package contains unregistered files or answer artifacts: "
            f"{unexpected_package_paths}"
        )

    return {
        "status": "PASS" if not failures else "FAIL",
        "mode": "development" if allow_development_artifacts else "clean-distribution",
        "inventory": {
            "modules": len(modules),
            "appendices": len(appendices),
            "immutable_sources": len(actual_source_hashes),
            "workflow_files": len(actual_workflow_hashes),
        },
        "content_registry": {
            "modules": len(module_refs),
            "appendices": len(appendix_refs),
        },
        "bundle_sha256": source_bundle_hash,
        "workflow_bundle_sha256": workflow_bundle_hash,
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--allow-development-artifacts",
        action="store_true",
        help="permit files only under answers/, evaluation/, routing-v2/artifacts/, and tmp/",
    )
    args = parser.parse_args(argv)
    result = check_package(ROOT, args.allow_development_artifacts)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
