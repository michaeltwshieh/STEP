"""Shared text-cleanup for PDF->Markdown conversion artifacts.

Use clean_markdown(text) for the full pass. It runs, in order:

1. strip_bullet_artifacts — the course PDFs use a round bullet glyph (•) that
   docling mis-converts into a lone "y" marker, sometimes with a spurious list
   number prepended. So a real bullet can arrive as "- y text" or "2. y text".
   Both are normalised to a clean dash bullet "- text".

2. fix_leadin_subbullets — docling also renders a lettered SUB-HEADING (e.g.
   "a. Traditional articles:") as a dash bullet and leaves its following bullets
   at the same level, e.g.:
       - a. Traditional articles : Appendix 1B (...)
       - Articles 16.1 and 16.2 require ...
       - Article 16.4 provides ...
   The lettered lead-in should be a flush line and its plain bullets nested under
   it. A "- <letter>." line is treated as a lead-in ONLY when the next bullet is a
   plain (non-enumerated) bullet — so genuine "(a)/(b)/(c)" enumerated lists, whose
   next item is itself enumerated, are left untouched.
"""
import re

# A real bullet that arrived as "- y …" or "N. y …".
_BULLET_Y = re.compile(r"^(\s*)(?:-|\d+\.)\s+y (?=\S)", re.MULTILINE)

# A top-level dash bullet.
_TOP_BULLET = re.compile(r"^- ")
# An enumerated top-level bullet: "- a. ", "- b. ", "- ii. ", "- iv. " etc.
_ENUM_BULLET = re.compile(r"^- (?:[a-z]|[ivxlcdm]{2,4})\. ")


def strip_bullet_artifacts(text: str) -> str:
    return _BULLET_Y.sub(r"\1- ", text)


def fix_leadin_subbullets(text: str, indent: str = "  ") -> str:
    lines = text.split("\n")
    out = list(lines)
    n = len(lines)
    i = 0
    while i < n:
        if not _TOP_BULLET.match(lines[i]):
            i += 1
            continue
        # Extent of this contiguous block of top-level "- " bullets.
        j = i
        while j < n and _TOP_BULLET.match(lines[j]):
            j += 1
        under_leadin = False
        for k in range(i, j):
            if _ENUM_BULLET.match(lines[k]):
                nxt = lines[k + 1] if k + 1 < j else ""
                next_is_plain = bool(_TOP_BULLET.match(nxt)) and not _ENUM_BULLET.match(nxt)
                # Exclude a trailing item of a genuine "a./b./c." list: a lead-in is
                # never preceded by another enumerated bullet within the block.
                prev_is_enum = k > i and bool(_ENUM_BULLET.match(lines[k - 1]))
                if next_is_plain and not prev_is_enum:
                    out[k] = lines[k][2:]   # drop "- " -> flush "a. ..."
                    under_leadin = True
                else:
                    under_leadin = False    # part of a genuine enumerated list
            elif under_leadin:
                out[k] = indent + lines[k]  # nest the plain sub-bullet
        i = j
    return "\n".join(out)


def clean_markdown(text: str) -> str:
    return fix_leadin_subbullets(strip_bullet_artifacts(text))
