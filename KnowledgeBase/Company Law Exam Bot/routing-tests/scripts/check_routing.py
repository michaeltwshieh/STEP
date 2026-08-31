#!/usr/bin/env python3
"""Static and corpus checks for the Section B routing workflow."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

EXPECTED_HASHES = {
    "routing-tests/baseline/operational/AGENTS.md": "1cc89f60975b14f2708386cb9937272b3ad2131b43c7b605c0b29e2243fa7f46",
    "routing-tests/baseline/operational/CLAUDE.md": "511e564e9f6f3c40be76582ccfe2f2ee24beae00aac2dbc8d7ab2386ec74aa58",
    "routing-tests/baseline/operational/Content.md": "24b08234f7a29266d6d199d5f5bc8c721253f4b23a53757fc370473bd677416b",
    "routing-tests/baseline/operational/section-b.md": "2f80861e1fd8f23dfa50b181216c4eb96899aefdc01213884ab409df51473d75",
    "routing-tests/baseline/operational/Syllabus.md": "6d6b24a63f8e08203660b90b675a6405060d144dc59046672b2d906184a3a519",
    "routing-tests/baseline/operational/content-test.md": "c90286879ff00772590811bf794840c693c4a55caef6da0ebd40d7d301fd4e7b",
    "routing-tests/corpus/cases.json": "7a0010d184925ad20ff12f61a60ba059e4a4e68fd6cee102c2694fedf37abed9",
    "routing-tests/corpus/question-fixtures.json": "59c3d1038de547444651bf7d9a09a7cf97b631fa75ba7146f8ca4c7fbfcb5c0a",
    "routing-tests/sources/question/specimen-paper-1.txt": "07d07ec52ed17dc4d0fe360d297ba8c88d9c48fae9f27c2da7b94cbf68b198a6",
    "routing-tests/sources/kap/specimen-paper-1-kap.txt": "cc9fc7ce0e0b77dae24d1758f9e7ccab7a790a520436e425162bccd9d5659350",
}

REQUIRED_PROMPT_PHRASES = (
    "Fact Disposition Ledger",
    "transaction-lifecycle routing",
    "Jurisdiction lock",
    "Regime lock",
    "Actor lock",
    "Stage lock",
    "Source precedence",
    "Isolate conditional branches",
    "seven-layer closure",
    "hard relevance gate",
    "Mandatory routes",
    "Forbidden routes",
    "Materials-gap handling",
    "exam_attachment:*",
)

FORBIDDEN_PROMPT_TRIGGERS = (
    "lear jet",
    "lear star",
    "tail fin",
    "federal aviation authority",
    "faa",
    "manx aircraft",
    "mr ab",
    "blackacre",
    "redhouse trust",
    "midcity bank",
)


class Audit:
    def __init__(self) -> None:
        self.passes: list[str] = []
        self.warnings: list[str] = []
        self.failures: list[str] = []
        self.metrics: dict[str, object] = {}

    def require(self, condition: bool, message: str) -> None:
        if condition:
            self.passes.append(message)
        else:
            self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def count_table_cells(line: str) -> int:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells = re.split(r"(?<!\\)\|", stripped)
    return len(cells)


def table_issues(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    issues: list[str] = []
    index = 0
    while index < len(lines) - 1:
        header = lines[index]
        delimiter = lines[index + 1]
        if "|" not in header or "|" not in delimiter:
            index += 1
            continue
        delimiter_cells = [
            cell.strip()
            for cell in delimiter.strip().strip("|").split("|")
        ]
        if not delimiter_cells or not all(
            re.fullmatch(r":?-{3,}:?", cell) for cell in delimiter_cells
        ):
            index += 1
            continue
        expected = count_table_cells(header)
        if count_table_cells(delimiter) != expected:
            issues.append(f"{path.relative_to(ROOT)}:{index + 2}: delimiter width")
        row = index + 2
        while row < len(lines) and lines[row].strip().startswith("|"):
            if count_table_cells(lines[row]) != expected:
                issues.append(f"{path.relative_to(ROOT)}:{row + 1}: row width")
            row += 1
        index = row
    return issues


def duplicate_headings(path: Path) -> dict[str, list[int]]:
    found: dict[str, list[int]] = collections.defaultdict(list)
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            found[match.group(1)].append(lineno)
    return {heading: lines for heading, lines in found.items() if len(lines) > 1}


def local_link_issues(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        clean = target.strip().strip("<>").split("#", 1)[0]
        if not clean or re.match(r"^(?:https?://|mailto:)", clean):
            continue
        candidate = (path.parent / clean).resolve()
        if not candidate.exists():
            issues.append(f"{path.relative_to(ROOT)} -> {target}")
    return issues


def run() -> Audit:
    audit = Audit()

    modules = sorted(ROOT.glob("Course-Manual-Module-*.md"))
    appendices = sorted(ROOT.glob("Appendix-*.md"))
    audit.metrics["module_count"] = len(modules)
    audit.metrics["appendix_count"] = len(appendices)
    audit.require(len(modules) == 12, "inventory has exactly 12 course modules")
    audit.require(len(appendices) == 90, "inventory has exactly 90 course appendices")

    module_numbers = [
        re.match(r"Course-Manual-Module-(\d\d)-", path.name).group(1)
        for path in modules
    ]
    audit.require(
        module_numbers == [f"{number:02d}" for number in range(1, 13)],
        "module numbers are unique and continuous from 01 to 12",
    )

    appendix_labels = [
        re.match(r"Appendix-([0-9]+[A-Z]?)-", path.name).group(1)
        for path in appendices
    ]
    audit.require(
        len(appendix_labels) == len(set(appendix_labels)),
        "appendix filename labels are unique",
    )

    content = (ROOT / "Content.md").read_text(encoding="utf-8")
    indexed_modules = re.findall(r"^File:\s*`([^`]+\.md)`", content, re.MULTILINE)
    indexed_appendices = re.findall(
        r"^- \*\*Appendix\s+([0-9]+[A-Z]?)\*\*.*?`([^`]+\.md)`",
        content,
        re.MULTILINE,
    )
    audit.require(len(indexed_modules) == 12, "Content.md indexes 12 module filenames")
    audit.require(len(indexed_appendices) == 90, "Content.md indexes 90 appendix filenames")
    missing_content = [
        name
        for name in indexed_modules + [name for _, name in indexed_appendices]
        if not (ROOT / name).is_file()
    ]
    audit.require(not missing_content, "every Content.md indexed filename resolves")
    audit.require(
        set(indexed_modules) == {path.name for path in modules},
        "Content.md module index is bijective with module files",
    )
    audit.require(
        {name for _, name in indexed_appendices} == {path.name for path in appendices},
        "Content.md appendix index is bijective with appendix files",
    )

    overlay = (ROOT / "content-test.md").read_text(encoding="utf-8")
    overlay_module_names = set(
        re.findall(r"`(Course-Manual-Module-[^`]+\.md)`", overlay)
    )
    overlay_appendix_names = set(re.findall(r"`(Appendix-[^`]+\.md)`", overlay))
    audit.require(
        overlay_module_names == {path.name for path in modules},
        "content-test.md names every module file",
    )
    audit.require(
        overlay_appendix_names == {path.name for path in appendices},
        "content-test.md names every appendix file",
    )

    for relative, expected in EXPECTED_HASHES.items():
        path = ROOT / relative
        audit.require(path.is_file(), f"frozen artifact exists: {relative}")
        if path.is_file():
            audit.require(sha256(path) == expected, f"frozen hash matches: {relative}")

    cases_path = ROOT / "routing-tests/corpus/cases.json"
    try:
        corpus = json.loads(cases_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        audit.failures.append(f"cases.json parses: {error}")
        corpus = {"cases": []}
    cases = corpus.get("cases", [])
    ids = [case.get("id") for case in cases]
    pair_counts = collections.Counter(
        case.get("group")
        for case in cases
        if str(case.get("group", "")).startswith("minimal-pair-")
    )
    required_fields = {
        "locks",
        "must_open",
        "conditional",
        "must_not_open",
        "expected_document_chain",
        "mandatory_critical_routes",
        "fact_dispositions",
        "expected_course_gap",
        "source_precedence",
        "unresolved_branches",
    }
    audit.metrics["case_count"] = len(cases)
    audit.metrics["minimal_pair_count"] = len(pair_counts)
    audit.require(len(cases) == corpus.get("case_count") == 23, "corpus contains 23 declared cases")
    audit.require(len(ids) == len(set(ids)), "corpus case IDs are unique")
    audit.require(
        len(pair_counts) == corpus.get("minimal_pair_count") == 9
        and set(pair_counts.values()) == {2},
        "corpus contains nine complete two-case minimal pairs",
    )
    incomplete = [
        case.get("id")
        for case in cases
        if not required_fields.issubset(case)
    ]
    audit.require(not incomplete, "every case has all frozen routing fields")

    concrete_md = set(re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]*\.md", cases_path.read_text(encoding="utf-8")))
    missing_case_sources = sorted(name for name in concrete_md if not (ROOT / name).is_file())
    audit.require(not missing_case_sources, "all concrete case-source filenames resolve")

    fixture_path = ROOT / "routing-tests/corpus/question-fixtures.json"
    try:
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        audit.failures.append(f"question-fixtures.json parses: {error}")
        fixture = {"fixtures": []}
    allowed_fixture_fields = {"id", "group", "title", "question", "task_type_hint"}
    audit.require(
        fixture.get("source_corpus_sha256") == EXPECTED_HASHES["routing-tests/corpus/cases.json"],
        "question-only fixture names the frozen source-corpus hash",
    )
    audit.require(
        fixture.get("fixture_count") == len(fixture.get("fixtures", [])) == 18,
        "question-only fixture contains 18 synthetic cases",
    )
    audit.require(
        all(set(item) == allowed_fixture_fields for item in fixture.get("fixtures", [])),
        "question-only fixture exposes no gold fields",
    )

    prompt_path = ROOT / "routing-prompt.md"
    audit.require(prompt_path.is_file(), "routing-prompt.md exists")
    prompt = prompt_path.read_text(encoding="utf-8") if prompt_path.is_file() else ""
    for phrase in REQUIRED_PROMPT_PHRASES:
        audit.require(phrase.lower() in prompt.lower(), f"routing prompt includes: {phrase}")
    for trigger in FORBIDDEN_PROMPT_TRIGGERS:
        audit.require(trigger not in prompt.lower(), f"routing prompt omits specimen trigger: {trigger}")

    markdown_files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "routing-tests").rglob("*.md"))
    table_failures: list[str] = []
    link_failures: list[str] = []
    duplicate_operational: list[str] = []
    duplicate_source_count = 0
    for path in markdown_files:
        table_failures.extend(table_issues(path))
        link_failures.extend(local_link_issues(path))
        duplicates = duplicate_headings(path)
        if not duplicates:
            continue
        if path.name.startswith("Course-Manual-") or path.name.startswith("Appendix-") or path.name == "Syllabus.md":
            duplicate_source_count += sum(len(lines) - 1 for lines in duplicates.values())
        elif not any(
            excluded in path.as_posix()
            for excluded in (
                "routing-tests/baseline/operational",
                "routing-tests/blind/",
                "routing-tests/reports/",
                "routing-tests/rounds/",
            )
        ):
            duplicate_operational.extend(
                f"{path.relative_to(ROOT)}:{','.join(map(str, lines))}:{heading}"
                for heading, lines in duplicates.items()
            )
    audit.metrics["markdown_files_checked"] = len(markdown_files)
    audit.metrics["known_source_duplicate_heading_instances"] = duplicate_source_count
    audit.require(not table_failures, "Markdown table column widths are consistent")
    audit.require(not link_failures, "all local Markdown links resolve")
    audit.require(not duplicate_operational, "no duplicate headings in operational or new routing artifacts")
    if duplicate_source_count:
        audit.warn(
            f"source-of-truth files contain {duplicate_source_count} duplicate-heading instances; retained as source warnings"
        )

    git = subprocess.run(
        ["git", "diff", "--name-only"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    changed_sources = [
        line
        for line in git.stdout.splitlines()
        if Path(line).name.startswith("Course-Manual-") or Path(line).name.startswith("Appendix-")
    ]
    audit.require(not changed_sources, "course manuals and appendices remain unmodified")

    audit.warn("known source reference: Appendix 6A mentions absent Appendix 4A")
    audit.warn("known source cross-reference: Module 3 points to nonexistent Module 9 §1.3.2(viii)")
    audit.warn("known source cross-reference: Module 5 points to nonexistent Module 9 §2.8")
    return audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--require-integration", action="store_true")
    args = parser.parse_args()

    audit = run()
    if args.require_integration:
        for name in ("CLAUDE.md", "Content.md", "section-b.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            audit.require(
                "routing-prompt.md" in text,
                f"{name} is integrated with routing-prompt.md",
            )

    report = {
        "status": "PASS" if not audit.failures else "FAIL",
        "metrics": audit.metrics,
        "passes": audit.passes,
        "warnings": audit.warnings,
        "failures": audit.failures,
    }
    output = json.dumps(report, indent=2, ensure_ascii=True)
    print(output)
    if args.json_out:
        destination = args.json_out
        if not destination.is_absolute():
            destination = ROOT / destination
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output + "\n", encoding="utf-8")
    return 0 if not audit.failures else 1


if __name__ == "__main__":
    sys.exit(main())
