"""Split the converted Markdown corpus into descriptively-named, retrieval-friendly
files for the exam assistant, and generate a Content.md routing index.

Output -> KnowledgeBase/<subfolder>/
  - Course-Manual-Module-NN-<Title>.md         (one per module, 1..12)
  - Course-Manual-Self-Assessment-Answers.md
  - Appendix-<Label>-<Title>.md                (one per sub-document, e.g. 1A, 25J)
  - Syllabus.md                                (copied whole)
  - Content.md                                 (routing index for both Claude Code & Project)

The Transcript Document is intentionally excluded.
Re-runnable: the output dir is wiped each run.

Usage:
    python split_corpus.py "STEP Advanced Certificate in Company Law and Practice"
"""
import json
import re
import shutil
import sys
from pathlib import Path

from text_cleanup import clean_markdown


def read_clean(path: Path) -> list[str]:
    """Read a source markdown file with conversion artifacts cleaned."""
    return clean_markdown(path.read_text()).splitlines(keepends=True)

ROOT = Path(__file__).parent
subfolder = sys.argv[1] if len(sys.argv) > 1 else "STEP Advanced Certificate in Company Law and Practice"
SRC = ROOT / "Markdown" / subfolder
OUT = ROOT / "KnowledgeBase" / subfolder

# ---- Per-exam settings -------------------------------------------------------
# Everything outside this dict is generic. For a new exam add one entry, keyed by
# the Materials/Markdown subfolder name (see SETUP.md §3):
#   modules — clean module titles; take them from the manual's own Contents page
#             (authoritative, and available even when the syllabus PDF is missing).
#   topics  — curated "topic -> module + appendices" rows for the Content.md quick map.
#   missing — appendix headings docling dropped: (label, title, exact anchor line).
EXAMS = {
    "STEP Advanced Certificate in Company Law and Practice": dict(
        modules={
            1: "An Introduction to Company Law and Practice",
            2: "Characteristics of a Company",
            3: "Company Formation and Related Issues",
            4: "Registration and Migration of Foreign Companies",
            5: "The Company's Constitution",
            6: "Equity, Capital and Distributions",
            7: "Directors Part I - Role, Appointment and Removal of Directors",
            8: "Directors Part II - Powers and Duties",
            9: "Other Officers - Secretary and Registered Agent",
            10: "Company Decision-making Procedures",
            11: "Company Management Services and Beneficial Owner Control",
            12: "Termination of Companies",
        },
        topics=[
            ("separate legal personality, veil of incorporation, Salomon, lifting/piercing the veil", 2, ["3"]),
            ("company vs partnership, types of company, public vs private, offshore vehicles (IBC/BC)", 2, ["2", "6A", "6B"]),
            ("promoters, pre-incorporation contracts, incorporation procedure, first board minutes, statutory registers", 3, ["4", "5", "7A", "7B", "7C", "7D", "8", "9", "21B"]),
            ("foreign companies, migration, continuance, re-domiciliation, establishing a place of business", 4, ["10A", "10B", "10C"]),
            ("memorandum & articles, constitution, objects clause, ultra vires, capacity, altering articles, change of name", 5, ["1A", "1B", "1C", "11", "12", "13A", "13B", "14", "15A", "15B", "15C"]),
            ("share capital, issue & transfer of shares, share certificates, capital maintenance, dividends/distributions, share premium, shareholder loan, class rights, balance sheet", 6, ["16A", "16B", "16C", "16D", "16E", "17A", "17B", "18A", "18B", "18C", "18D", "18E", "19A", "19B", "19C", "20A", "20B", "20C", "20D", "20E"]),
            ("appointment & removal of directors, Table A art. 80/70, Model Article 3, director's consent/service agreement", 7, ["21A", "21B", "21C", "21D", "21E", "21F", "21G"]),
            ("directors' powers & duties, fiduciary duty, conflicts of interest, care & skill, fraudulent/wrongful trading, director liability, indemnity, management agreement", 8, ["22", "23A", "23B", "23C"]),
            ("company secretary, registered agent, appointment/removal of secretary", 9, ["24A", "24B", "24C"]),
            ("general & board meetings, notice, quorum, proxies, resolutions, minutes, AGM, decision-making", 10, ["25A", "25B", "25C", "25D", "25E", "25F", "25G", "25H", "25J", "25K", "25L", "25M", "25N"]),
            ("company management services, beneficial owner control, nominee shareholders, powers of attorney, AML/CFT", 11, ["26", "27A", "27B", "28", "29A", "29B"]),
            ("fixed & floating charges, receivership, winding-up/liquidation, striking off, dissolution, reinstatement, declaration of solvency", 12, ["30A", "30B", "30C", "30D", "30E", "30F", "30G", "31A", "31B", "31C", "31D"]),
        ],
        missing=[
            ("4", "Board resolution to adopt pre-incorporation contract",
             "## Board resolution to adopt pre-incorporation contract\n"),
        ],
    ),
    "STEP Advanced Certificate in Trusts - Law and Practice": dict(
        modules={
            1: "Review of the Trust Concept",
            2: "Marketing Trust Services and Accepting New Business",
            3: "The Trust Instrument - Part 1: Preliminary Provisions",
            4: "The Trust Instrument - Part 2: Dispositive Provisions",
            5: "The Trust Instrument - Part 3: Administrative Provisions",
            6: "Choice of Law to Govern the Trust",
            7: "The Role and Status of a Protector",
            8: "Estate Planning and Forced Heirship Avoidance",
            9: "Asset Protection Trusts",
            10: "Purpose Trusts",
            11: "Private Foundations",
        },
        topics=[
            ("definition of a trust, three certainties, certainty of intention, capacity of settlor, legal vs equitable ownership, transfer of legal title, separate fund, trustee's core duties, beneficiaries' in personam and in rem rights, tracing, Hague Convention, trust compared with company / contract / will / foundation, civil law systems", 1, []),
            ("marketing trust services, marketing the jurisdiction, remuneration and the remuneration rule, charging clause, negotiating fees, appointment of first trustee, removal / retirement / appointment of trustees, duties on accepting existing trust business, acquainting with trust terms and property, review of trust accounts, investment review, compliance", 2, ["2", "3", "4", "5"]),
            ("trust instrument preliminary provisions, formal parts, recitals, definitions clause, the trust fund, the trust period, definition of beneficiaries, the trustees, the protector, the proper law, trust for sale, trusts of original and additional property", 3, ["7"]),
            ("discretionary trust, dispositive provisions over income and capital, power of appointment, power of re-settlement, ultimate default trust, duties owed under a dispositive power, factors in the decision-making process, letter / statement / memorandum of wishes, sham trust, distribution procedure and checklist, releases and receipts, settlor-directed (reserved powers) trust, reserved powers legislation, life interest trust, determinable life interest", 4, ["1", "6", "8", "9", "10", "11A", "11B", "12", "13", "14B", "15", "16A", "16B", "17", "18", "20A", "20B", "21"]),
            ("administrative provisions, power to invest, prudent investor rule, power to lend and give guarantees, real estate and chattels, power to operate a business, power to insure, powers in relation to companies, anti-Bartlett clause, power to delegate, power to sue and compromise claims, appropriation and distribution in specie, power to vary administrative provisions, payment of foreign taxes, Government of India v Taylor, trustee indemnity, exoneration and restriction of liability, charging clause, power to revoke, execution", 5, ["14A", "19", "22", "23", "24A", "24B", "25", "26"]),
            ("choice of law, conflict of laws, characterisation, renvoi, forum, governing law of the trust, selecting and changing the governing law, matters determined by the governing law, validity of the trust and of the disposition into trust, firewall provisions, exclusion of foreign law and its exceptions, foreign real estate, testamentary trusts, express choice of law clause, flee clauses", 6, ["27", "28"]),
            ("protector, appointment of a protector, dispositive and administrative powers of a protector, power to appoint or remove trustees, power to approve remuneration or self-dealing, veto powers, whether a protector's powers are fiduciary, duty of reasonable care and skill, exoneration of protectors, rights of protectors, position of the trustee where a protector is appointed, binding directions, position of the beneficiaries", 7, ["29"]),
            ("estate planning, forced heirship, freedom of disposition, forced heirship on death and over inter vivos gifts, domicile, nationality, habitual residence, clawback, attack in the forum of the foreign state, jurisdiction over offshore trustees, enforcement of foreign judgments, defence of the trust", 8, []),
            ("asset protection trusts, Statute of Elizabeth, fraudulent dispositions, intent to defraud, creditor, limitation period, burden of proof, survivability of the trust, structuring an asset protection trust, bankruptcy, transaction at an undervalue, recognition of a foreign trustee in bankruptcy, divorce, nuptial settlement, treating trust assets as a resource, setting the trust aside", 9, []),
            ("purpose trusts, human beneficiary principle, trusts of imperfect obligation, charitable trusts, offshore purpose trust legislation, Bermuda second generation, STAR trusts (Cayman), enforcer, private trust company, employee benefit trusts, subordination trusts, project and asset financing", 10, ["30"]),
            ("private foundations, definition and characteristics, formation and registration, separate legal entity, charter (foundation deed), regulations / by-laws, founder's reserved rights, the council and councillors' duties, guardian or supervisory body, beneficiaries of a foundation, capacity, termination, trusts versus foundations compared", 11, ["31", "32"]),
        ],
        missing=[],
    ),
}

if subfolder not in EXAMS:
    print(f"No per-exam settings for {subfolder!r}.\n"
          f"Add an EXAMS entry (see SETUP.md §3). Known: {list(EXAMS)}")
    sys.exit(1)
MODULE_TITLES = EXAMS[subfolder]["modules"]
TOPIC_MAP = EXAMS[subfolder]["topics"]

if not SRC.is_dir():
    print(f"Source markdown folder not found: {SRC}")
    sys.exit(1)
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)


def slug(text: str, maxlen: int = 60) -> str:
    text = re.sub(r"[‘’'`]", "", text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    if len(text) > maxlen:
        text = text[:maxlen].rsplit("-", 1)[0]
    return text


def write_file(name: str, header: str, lines: list[str], footer: str = "") -> None:
    body = "".join(lines).strip()
    (OUT / name).write_text(f"# {header}\n\n{body}{footer}\n")


# ---- Course Manual: one file per module + answers ----------------------------
module_outlines: dict[int, list[str]] = {}


def split_course_manual() -> None:
    src = SRC / "Course Manual.md"
    if not src.exists():
        print("Course Manual.md not found, skipping.")
        return
    print("Splitting Course Manual.md ...")
    lines = read_clean(src)

    fn_path = SRC / "Course Manual.footnotes.json"
    footnotes = json.loads(fn_path.read_text()) if fn_path.exists() else {}

    starts: dict[int, int] = {}
    for i, ln in enumerate(lines):
        m = re.match(r"^## Module (\d+):", ln)
        if m:
            starts.setdefault(int(m.group(1)), i)
    answers_start = next(
        (i for i, ln in enumerate(lines) if ln.startswith("## All Modules: Answers")),
        len(lines),
    )

    ordered = sorted(starts.items())
    for pos, (n, start) in enumerate(ordered):
        end = ordered[pos + 1][1] if pos + 1 < len(ordered) else answers_start
        seg = lines[start:end]
        title = MODULE_TITLES.get(n, f"Module {n}")
        mod_fns = footnotes.get(str(n), [])
        footer = "\n\n## Footnotes\n\n" + "\n\n".join(mod_fns) if mod_fns else ""
        write_file(f"Course-Manual-Module-{n:02d}-{slug(title)}.md",
                   f"Course Manual — Module {n}: {title}", seg, footer)
        # capture numbered section outline for the index
        outline = []
        for ln in seg:
            m = re.match(r"^## (\d+(?:\.\d+)*)\.?\s+(.+)", ln)
            if m:
                outline.append(f"{m.group(1)} {m.group(2).strip()}")
        module_outlines[n] = outline
        print(f"  -> Course-Manual-Module-{n:02d}-{slug(title)}.md")

    if answers_start < len(lines):
        write_file("Course-Manual-Self-Assessment-Answers.md",
                   "Course Manual — Answers to Self-Assessment Questions",
                   lines[answers_start:])
        print("  -> Course-Manual-Self-Assessment-Answers.md")


# ---- Appendices: one file per sub-document -----------------------------------
appendix_entries: list[tuple[str, str, str]] = []  # (label, title, filename)


def split_appendices() -> None:
    # Spelling varies by exam ("Appendicies.md" / "Appendices.md"), so glob for it.
    src = next(iter(sorted(SRC.glob("Append*.md"))), None)
    if src is None:
        print("No Append*.md found, skipping.")
        return
    print(f"Splitting {src.name} (per sub-document) ...")
    lines = read_clean(src)

    # Repair appendix headings dropped during PDF->Markdown conversion. Each entry
    # injects a synthetic "## Appendix <label>: <title>" before a unique anchor line.
    for label, title, anchor in EXAMS[subfolder]["missing"]:
        if any(re.match(rf"^## Appendix {label}:", ln) for ln in lines):
            continue  # already present
        for i, ln in enumerate(lines):
            if ln == anchor:
                lines.insert(i, f"## Appendix {label}: {title}\n")
                print(f"  injected missing heading: Appendix {label}")
                break

    # Parse the appendix TOC (table rows) as a fallback title source.
    toc: dict[str, str] = {}
    for ln in lines:
        m = re.match(r"^\|\s*Appendix ([0-9]+[A-Za-z]?):\s*(.+?)\s*\|", ln)
        if m:
            toc.setdefault(m.group(1), re.sub(r"\s+", " ", m.group(2)).strip())

    heads = []  # (line_idx, label, inline_title)
    for i, ln in enumerate(lines):
        m = re.match(r"^## Appendix ([0-9]+[A-Za-z]?):\s*(.*)$", ln)
        if m:
            heads.append((i, m.group(1), m.group(2).strip()))

    def next_heading_title(after: int, stop: int) -> str:
        for j in range(after + 1, stop):
            s = lines[j].strip()
            if s.startswith("## ") and not s.startswith("## Appendix"):
                return s[3:].strip()
        return ""

    # Words a real title never ends on -- their presence means the PDF wrapped it.
    DANGLING = {"of", "to", "the", "a", "an", "and", "or", "for", "in",
                "on", "upon", "with", "from", "by", "at"}

    def is_fragment(t: str) -> bool:
        # conversion artifacts where the title wrapped across lines
        return bool(t) and (t[0].islower() or re.match(r"^(and|or|to|the)\b", t, re.I))

    for pos, (idx, label, inline) in enumerate(heads):
        end = heads[pos + 1][0] if pos + 1 < len(heads) else len(lines)
        # A duplicated/bare heading (e.g. Trusts has "## Appendix 32:" immediately
        # before the real "## Appendix 32: AB Foundation ...") leaves an empty
        # segment; skip it rather than emit a contentless stub file.
        if not "".join(lines[idx + 1:end]).strip():
            print(f"  skipped empty duplicate heading: Appendix {label}")
            continue
        title = inline or next_heading_title(idx, end) or f"Appendix {label}"
        title = re.sub(r"\s+", " ", title).strip()
        if is_fragment(title) and label in toc:
            title = toc[label]
        elif inline:
            # A heading that wrapped in the PDF leaves its tail as the very next
            # "## " line ("... to Exercise a Power of" + "Appointment"). Rejoin when
            # the tail reads as a continuation, or the title ends mid-phrase. (The
            # TOC is not a reliable source here -- its rows drop spaces, e.g.
            # "Trustees'Resolution".)
            # A lowercase tail is a continuation; an upper/caps one is a document
            # heading of its own ("THE COMPANIES LEGISLATION ...") -- leave those.
            tail = next_heading_title(idx, end)
            if tail and (tail[:1].islower() or title.split()[-1].lower() in DANGLING):
                title = f"{title} {tail}"
        fname = f"Appendix-{label}-{slug(title)}.md"
        write_file(fname, f"Appendix {label}: {title}", lines[idx:end])
        appendix_entries.append((label, title, fname))
    print(f"  -> {len(appendix_entries)} appendix sub-document files")


# ---- Content.md routing index ------------------------------------------------
def appendix_label_sort_key(label: str):
    m = re.match(r"(\d+)([A-Za-z]?)", label)
    return (int(m.group(1)), m.group(2)) if m else (999, label)


def build_content_index() -> None:
    print("Building Content.md ...")
    by_label = {lbl: (title, fn) for lbl, title, fn in appendix_entries}
    out = [f"# Content Index — {subfolder}",
           "",
           "Routing map for the exam assistant. Use the **Quick topic map** to find the",
           "right module + appendices for a question, then open/cite the named files.",
           "Module files: `Course-Manual-Module-NN-*.md`. Appendix files: `Appendix-<Label>-*.md`.",
           "",
           "## Quick topic map (topic → where to look)",
           ""]
    for topics, mod, apps in TOPIC_MAP:
        mt = MODULE_TITLES.get(mod, "")
        app_str = ", ".join(f"Appendix {a}" for a in apps) if apps else "—"
        out.append(f"- **{topics}** → Module {mod} ({mt}); {app_str}")
    out += ["", "## Modules (with section outlines)", ""]
    for n in sorted(module_outlines):
        out.append(f"### Module {n}: {MODULE_TITLES.get(n, '')}")
        out.append(f"File: `Course-Manual-Module-{n:02d}-{slug(MODULE_TITLES.get(n, ''))}.md`")
        for sec in module_outlines[n]:
            out.append(f"- {sec}")
        out.append("")
    out += ["## Appendices (precedent documents)", ""]
    for lbl, title, fn in sorted(appendix_entries, key=lambda e: appendix_label_sort_key(e[0])):
        out.append(f"- **Appendix {lbl}** — {title}  ·  `{fn}`")
    out.append("")
    (OUT / "Content.md").write_text("\n".join(out))
    print("  -> Content.md")


def copy_whole(name: str) -> None:
    src = SRC / name
    if src.exists():
        (OUT / name).write_text(clean_markdown(src.read_text()))
        print(f"  copied whole (cleaned): {name}")


split_course_manual()
split_appendices()
copy_whole("Syllabus.md")
build_content_index()

print(f"\nDone. Knowledge base written to:\n{OUT}")
