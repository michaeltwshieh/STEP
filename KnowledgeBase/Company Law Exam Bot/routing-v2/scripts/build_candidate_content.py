#!/usr/bin/env python3
"""Build the candidate authoritative Content.md from verified existing map sections."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
OVERLAY = (ROOT / "content-test.md").read_text(encoding="utf-8")
OUTPUT = ROOT / "routing-v2/candidate/Content.md"


def between(text: str, start: str, end: str) -> str:
    before, marker, rest = text.partition(start)
    if not marker:
        raise ValueError(f"missing start marker: {start}")
    body, marker, _ = rest.partition(end)
    if not marker:
        raise ValueError(f"missing end marker: {end}")
    return start + body


def appendix_filenames(text: str) -> dict[str, str]:
    inventory = between(text, "## Appendix file inventory", "## Known source and index warnings")
    pairs = re.findall(r"^- \*\*([^*]+)\*\* `([^`]+)`$", inventory, flags=re.MULTILINE)
    result = dict(pairs)
    if len(result) != 90:
        raise ValueError(f"expected 90 appendix filenames, found {len(result)}")
    return result


def canonical_appendix_registry(text: str) -> str:
    """Fold the separate filename inventory into the appendix decision tables."""
    filenames = appendix_filenames(OVERLAY)
    decision = between(text, "## Appendix decision map", "## High-risk distinctions")
    output: list[str] = []
    seen: set[str] = set()
    for line in decision.splitlines():
        if line == "| Appendix | Class and correct use | Combination / guardrail |":
            output.append("| Appendix | Exact filename | Class and correct use | Combination / guardrail |")
        elif line == "|---|---|---|":
            output.append("|---|---|---|---|")
        elif line.startswith("| **"):
            match = re.match(r"\| \*\*([^*]+)\*\*([^|]*)\|", line)
            if not match:
                raise ValueError(f"cannot parse appendix row: {line}")
            label = match.group(1)
            filename = filenames[label]
            first_cell_end = match.end()
            output.append(
                line[: first_cell_end - 1]
                + f"| `{filename}` |"
                + line[first_cell_end:]
            )
            seen.add(label)
        else:
            output.append(line)
    if seen != set(filenames):
        missing = sorted(set(filenames) - seen)
        raise ValueError(f"appendix decision map missing labels: {missing}")
    return "\n".join(output)


MODULE_OWNERSHIP = """## Module ownership

| Module | Primary ownership |
|---|---|
| 1 | course framework, source hierarchy and company-law setting |
| 2 | company characteristics, legal personality, limited liability and ownership/control separation |
| 3 | promoters, pre-incorporation contracts, formation, onboarding and initial records |
| 4 | foreign-company registration and migration/continuation |
| 5 | memorandum, articles, objects, capacity and constitutional alteration |
| 6 | equity, capital, allotment/issue, transfer/transmission, distributions and owner debt |
| 7 | division of member/director power and director appointment, resignation and removal |
| 8 | director powers, execution, duties, conflicts, remedies and liability |
| 9 | company secretary and registered agent |
| 10 | member/board decision procedures, meetings, resolutions and transaction procedure |
| 11 | company management services, nominee/beneficial-owner control, delegated management and agency |
| 12 | security consequences, receivership, winding-up, striking off, dissolution and reinstatement |

Ownership identifies the starting module only. The additive issue map controls every
required cross-module overlay.
"""


parts = [
    "# Content Index - Authoritative Section A and Section B Source Map\n\n"
    "This file is the single authoritative legal routing map for both exam sections. "
    "It identifies sources to inspect; it does not state law. Open every selected "
    "passage before answering. Do not copy legal mapping into `routing-core.md`, "
    "`section-a.md`, `section-b.md` or `CLAUDE.md`.\n\n"
    "## Map contract\n\n"
    "- Course manuals and appendices are the only substantive course-law sources.\n"
    "- Routes are additive candidates until final route selection is completed.\n"
    "- Conditional overlays activate only on their stated facts.\n"
    "- Examination attachments use a separate namespace from course appendices.\n"
    "- Source warnings preserve internal gaps or conflicts; they do not authorize outside law.\n\n",
    MODULE_OWNERSHIP,
    between(OVERLAY, "## Additive issue map", "## Appendix decision map"),
    canonical_appendix_registry(OVERLAY),
    between(OVERLAY, "## High-risk distinctions", "## Module file index and section outlines"),
    between(OVERLAY, "## Module file index and section outlines", "## Appendix file inventory"),
    between(OVERLAY, "## Known source and index warnings", "## Acceptance tests for this routing index")
    + "\n- The appendix sequence intentionally jumps from 25H to 25J; Appendix 25I does not exist.\n",
]

content = "\n\n".join(part.rstrip() for part in parts) + "\n"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(content, encoding="utf-8")
print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(content.splitlines())} lines)")
