# STEP Exam Assistant — Build Playbook (repeatable for any STEP exam)

An assistant that answers a STEP exam's questions from its course materials. You
screenshot a question, Claude routes via `Content.md` to the right module/appendix,
answers, and reports exactly what it used. Runs on **either** surface: **Claude Code**
(opens files deterministically) or a **claude.ai Project** (retrieval).

This file is written so you can rebuild the same thing for the **other three STEP
exams** (same publisher/format). It documents the pipeline, the **per-exam settings
you must change**, the **verification checklist**, and every **gotcha** we hit (with
how to detect and fix it).

---

## 0. Environment / dependencies

- Python venv at `.venv/` with `docling` (PDF→Markdown) and `pypdfium2` (text-layer
  footnote extraction). Run scripts with `.venv/bin/python` (not system python).
- First docling run downloads models (slow); later runs are cached. A full Course
  Manual conversion takes ~3 min. **docling is deterministic** for these PDFs
  (verified) — re-converting reproduces identical output.
- These are **digital PDFs with a real text layer** (not scans). docling still runs
  OCR by default and that OCR is what mangles footnotes — see Gotcha F.

---

## 1. Pipeline overview

```
Materials/<Exam>/*.pdf
   │  convert_pdfs.py   (docling → Markdown, + remove footnotes, + footnotes sidecar)
   ▼
Markdown/<Exam>/*.md  (+ Course Manual.footnotes.json)
   │  split_corpus.py   (split by module/appendix, descriptive names, build Content.md)
   ▼
KnowledgeBase/<Exam>/  ← the files the assistant uses
```

Three scripts + one helper:
- `convert_pdfs.py` — PDF → Markdown. Removes footnotes from the body and writes a
  per-module `…footnotes.json` sidecar (Course Manual only). `<exam>` subfolder arg.
- `extract_footnotes.py` — pulls footnotes from the PDF **text layer** (pypdfium2)
  using font size + sequential numbering. Used by `convert_pdfs.py`.
- `text_cleanup.py` — shared cleanup of docling artifacts (bullet glyph "y", lettered
  lead-ins). Used by both convert + split.
- `split_corpus.py` — splits Markdown into descriptively-named KB files and builds the
  `Content.md` routing index. Re-runnable; wipes & rebuilds the KB subfolder.

### KnowledgeBase contents (this exam: 105 files)
- `Content.md` — routing index: topic→location map, per-module section outlines, every
  appendix's title + filename.
- `Course-Manual-Module-NN-<Title>.md` — the modules (substantive law). Each ends with
  a `## Footnotes` section (the legal-citation footnotes, lifted out of the body).
- `Course-Manual-Self-Assessment-Answers.md`.
- `Appendix-<Label>-<Title>.md` — per-sub-document precedent files (e.g. `Appendix-25K-Minutes-of-AGM.md`).
- `Syllabus.md`. (Transcript intentionally excluded.)

---

## 2. Process for a NEW exam (do this in order)

1. **Drop the PDFs** in `Materials/<Exam name>/` (Course Manual, Appendices, Syllabus,
   Transcript, plus past papers + model answers if you have them).
2. **Convert:** `.venv/bin/python convert_pdfs.py "<Exam name>"`
   → writes `Markdown/<Exam>/*.md` + `Course Manual.footnotes.json`.
3. **Adjust the per-exam settings** in the scripts — **see §3** (this is the part that
   changes every time; do NOT skip it).
4. **Split:** `.venv/bin/python split_corpus.py "<Exam name>"`
   → writes `KnowledgeBase/<Exam>/`.
5. **Run the verification checklist — see §4.** Fix anything it flags (the gotchas in
   §5 tell you how), then re-run steps 2/4 as needed.
6. **Write `project-instructions.md`** for this exam (domain + 1–2 model-answer
   exemplars). Stand up the assistant — §6.
7. **Dry-run against past papers — §7.** Only trust question types that pass.

---

## 3. Per-exam settings you MUST review (everything else is generic)

The scripts have exam-specific constants. **They no longer get overwritten per exam** —
as of 2026-08-16 `split_corpus.py` holds them in an `EXAMS` dict keyed by the subfolder
name, so every exam's settings coexist and any exam can be rebuilt at any time. Add one
`EXAMS` entry per new exam; an unknown subfolder exits with a message rather than
silently reusing another exam's titles.

### `split_corpus.py` — the `EXAMS` entry
- **`modules`** — module number → clean title. Different exam = different count and
  titles (Company Law 12, Trusts 11). **Take them from the manual's own Contents page**,
  not the syllabus: it is authoritative for what the manual actually contains, and it is
  available even when the syllabus PDF is missing (as it was for Trusts). The in-body
  `## Module N:` headings are unreliable — the PDF wraps long ones mid-title.
- **`topics`** — hand-curated `(topics, module, [appendix labels])` rows that build the
  `Content.md` quick topic map. **Entirely exam-specific**; write them from the module
  section outlines the split itself generates (run it once with `topics=[]`, read the
  outlines in `Content.md`, then author). Highest-value routing aid; budget time for it.
  Verify afterwards that every appendix label cited actually exists and that no appendix
  is left unrouted.
- **`missing`** — appendix headings docling dropped (Company Law needed Appendix 4
  re-injected; Trusts needed none). Found by verification §4; add `(label, title, anchor_line)`.
- **Regexes** — confirm the new manual uses the same heading conventions:
  - module starts: `^## Module (\d+):`
  - end-of-modules / answers marker: `^## All Modules: Answers` (Trusts lowercases the
    rest of that line — the match is deliberately prefix-only, so it still works)
  - appendix headings: `^## Appendix ([0-9]+[A-Za-z]?):`
  - appendix TOC rows (fallback titles): `^\|\s*Appendix …`
  If the new manual differs (e.g. "Chapter" not "Module", or no appendices), adjust.
- **Appendix source filename** is globbed (`Append*.md`), so the `Appendicies`/`Appendices`
  spelling difference between exams needs no config.
- **Two generic appendix repairs** (added during the Trusts build, both apply to any exam):
  a duplicated/bare heading that leaves an empty segment is skipped instead of emitting a
  contentless stub (Trusts had a second bare `## Appendix 32:`); and a heading the PDF
  wrapped mid-title is rejoined with its tail, which is the next `## ` line — but only when
  that tail starts lowercase or the title ends on a dangling word like "of"/"to". Do **not**
  widen that test to any following heading: an ALL-CAPS one is a document heading of its
  own, and swallowing it corrupts the title (it briefly did, on Company Law Appendix 1A).
  Do not use the TOC rows to complete a wrapped title either — they drop spaces
  (`Trustees'Resolution`, `SampleTerms`), so prefix matching against them silently fails.

### `extract_footnotes.py`
- **The numbering reset** is now **auto-detected, no longer per-exam config** (fixed
  2026-08-15 during the Trusts build). Numbering schemes differ per exam: Company Law
  runs 1–111 across Modules 1–5 then **restarts** and runs 1–236 across Modules 6–12,
  whereas Trusts runs **1–350 straight through**. The extractor treats a `1.` seen while
  deep into the count (`expected > 20`) as a restart, which handles both, plus multiple
  resets, with no editing. Verified: Company Law 347, Trusts 350, zero gaps in each.
  Symptom if it ever misfires: a whole run of modules with massive gaps (that was the
  old hard-coded `module >= 6` rule silently dropping 189 Trusts footnotes).
- **`_body_height(doc) * 0.9`** — the font-size threshold separating footnotes (small)
  from body. Verify with the height inspection in Gotcha F; widen/narrow if footnotes
  render at a different size.
- **`_WINDOW = 8`** — how far the sequence counter may skip to resync. Generally fine.
- Module-header regex `Module (\d+):` — used to map footnotes → module. Adjust if the
  running header differs.

### `convert_pdfs.py`
- Footnote handling is gated to `"Course Manual" in pdf.stem`, and `split_corpus.py`
  later opens `Course Manual.md` / `Appendicies.md` by exact name. **Rename the source
  PDFs to those exact spellings** (including the `Appendicies` misspelling) rather than
  editing the scripts — it is the one-step fix and keeps every exam consistent. The
  Trusts download arrived as `Course manual.pdf` (lowercase m), which silently skips
  **all** footnote handling: the run "succeeds" and just writes no `.footnotes.json`.

### `project-instructions.md`
- Domain description (this one says offshore/common-law company law), the MCQ/essay
  rules are generic, and the **two model-answer exemplars** must be filled with real
  past Q+A for the new exam.

---

## 4. Verification checklist (run after every build — this is how we caught the bugs)

Run these against the new exam; each line is a real failure mode we hit.

1. **Footnote completeness (most important).**
   `.venv/bin/python extract_footnotes.py "Materials/<Exam>/Course Manual.pdf"`
   - Read the per-module ranges + `gaps`. Expect **zero gaps** — both exams now hit that.
     Many gaps ⇒ wrong font threshold (Gotcha F) or a missed restart (§3). Before writing
     a gap off as "absent in the source", grep the PDF text layer for it: the one gap we
     long assumed was a source omission (Company Law fn 2) was actually a bug —
     `_is_furniture()` dropped any line containing "STEP Advanced Certificate" to strip
     the running header, which also ate footnotes *citing another STEP certificate*
     (Company Law fn 2; Trusts fn 75 and 248). Fixed by letting a leading footnote number
     override the furniture patterns.
   - Note the total; compare to the highest footnote number you can see in the PDF.
2. **No footnotes left in the body, but legit case mentions kept.** After convert,
   check the body has 0 lines matching a footnote signature, and that a sentence like
   "in the case of <X>" survives. (We verified fn 38 removed, "Kelner v Baxter" kept.)
3. **Bullet-glyph artifact gone.** `grep -rE '^(\s*(-|[0-9]+\.)\s+)y ' Markdown/<Exam>`
   should return nothing. If it matches, the bullet glyph differs — see Gotcha A.
4. **Lettered lead-ins.** Spot-check a module with `a./b.` sub-headings followed by
   bullets (e.g. "Traditional articles" type lists): the lead-in should be flush and its
   bullets indented under it; genuine `(a)/(b)` lists should stay as bullets (Gotcha B).
5. **Heading drops.** Compare the appendix **TOC count** to the number of `Appendix-*`
   files produced, and scan appendix numbers for a missing one in the sequence. A gap ⇒
   add it to `MISSING` (Gotcha C). Note the TOC itself can be wrong (Gotcha D).
6. **Clean module split.** Open one split module file; confirm it starts at its own
   heading and ends before the next module (doesn't bleed in self-assessment of the next).
7. **Descender words.** `grep` a few words with p/y/g/j (e.g. "professional",
   "Guernsey") in the footnotes; they must not be mangled ("rofessional"). If mangled,
   the line-clustering tolerance is wrong (Gotcha F).

---

## 5. Gotchas & fixes (lessons from building exam #1)

**A. Bullet glyph reads as "y".** The PDF's round sub-bullet (•) is OCR'd as a lone
letter `y`, arriving as `- y text` (dash) or `N. y text` (spurious number). Both are
bullets. `text_cleanup.strip_bullet_artifacts` normalises them to `- text`. If a new
exam uses a different glyph, the artifact letter may differ — inspect a converted module
and update the regex.

**B. Lettered sub-heading rendered as a bullet, sub-bullets not nested.** A lead-in like
`a. Traditional articles:` came through as `- a. …` with its bullets at the same level.
`text_cleanup.fix_leadin_subbullets` de-bullets the lead-in and indents the following
plain bullets — **only** when the next bullet is plain (not enumerated) and the line
isn't preceded by another enumerated bullet, so genuine `(a)/(b)/(c)` lists are left
alone.

**C. Dropped appendix/section headings.** docling silently lost the `## Appendix 4:`
heading, merging its content into Appendix 3. Detected by a gap in appendix numbers.
Fixed via the `MISSING` list in `split_corpus.py` (inject the heading before a unique
anchor line). Check for this every exam.

**D. The PDF's own table-of-contents has errors.** The Appendices TOC mislabelled 17A
and omitted 2 and 4. So titles are derived from the **document body** first, with the
TOC only as a fallback for fragments. Don't trust the TOC as ground truth.

**E. Footnote numbering resets mid-document.** See §3 — this manual resets at Module 6.
Always determine the scheme before trusting footnote output.

**F. docling drops/garbles ~70 of ~347 footnotes; the fix is the text layer.**
- docling inlines page-bottom footnotes into body sentences AND misclassifies many
  (no-OCR re-convert was identical, so it's the layout model, not OCR).
- `extract_footnotes.py` reads them from the text layer: footnotes are a **smaller
  font** at the page bottom, **numbered sequentially**. It (1) reconstructs lines to
  find small-font footnote lines, (2) gets each line's **clean text via per-line
  `get_text_bounded`** (this is essential), (3) assembles footnotes with a resilient
  running counter, (4) maps to modules via the page header.
- Subtle bugs we fixed, in case you must re-tune:
  - **Descenders (p/y/g/j) split into phantom lines** when clustering glyphs by bottom-y
    → use clustering tolerance ≥ 4.5; and never trust the reconstructed line *text* for
    content — only for locating lines. Pull text with `get_text_bounded`.
  - **Body contamination**: extracting a whole y-band pulls body text in. Extract
    **per line** (thin band), not one band per page.
  - **Page numbers / running headers** are small-font too → filtered as "furniture"
    (bare digits, "Module N:", "STEP Advanced Certificate").
  - **HTML escaping**: the docling body escapes `&`→`&amp;`; match footnotes for body
    removal on the **unescaped** line.
  - **Bare-number / multi-part footnotes**: docling sometimes split a number from its
    text or a footnote across items; the merge logic in the extractor reattaches them.
- Footnotes are removed from the docling body by a normalised **content signature**
  match (not docling's labels), which correctly distinguishes a footnote dumped inline
  from a legitimate body sentence naming the same case.

**G. Transcript excluded.** The Transcript Document is intentionally not in the KB
(low retrieval value). Keep or drop per exam.

---

## 6. Build the assistant

### Option A — Claude Code
- Keep `KnowledgeBase/<Exam>/` as-is. Put `project-instructions.md`'s body into a
  `CLAUDE.md` at the repo root so it loads automatically. Paste/attach a screenshot;
  Claude reads `Content.md`, opens the named files, answers, reports files/sections used.

### Option B — claude.ai Project (desktop)
- New Project → upload **all** of `KnowledgeBase/<Exam>/` (incl. `Content.md`) + the
  converted past papers/model answers. Paste `project-instructions.md` (below its line)
  into the Project instructions field.

`project-instructions.md` requirements: answer only from the materials; consult
`Content.md` first; never fabricate authority; **MCQ** → letter + reasoning + "why not"
+ sources + confidence; **essay** → full submit-ready prose with proper legal
authorities + "Authorities used" + "Sources used". Fill the two model-answer exemplars.

---

## 7. Dry run BEFORE exam day (the real de-risking step)
- **MCQs:** screenshot past-paper MCQs (or the manual's per-module *Self-assessment
  questions*) and check against known answers.
- **Essays:** paste past essay questions; compare to model answers for structure,
  authorities, depth. Tune `project-instructions.md` until essays match examiner style.
- **Routing/footnotes:** confirm the "Sources used" line is right and that a question
  needing a citation surfaces the correct footnote from a module's `## Footnotes`.

## 8. Exam-day workflow
1. Screenshot a question → paste in.
2. **MCQ:** read answer + reasoning; check "Sources used"/"Confidence"; spot-check
   medium/low.
3. **Essay:** transcribe the prose; sanity-check "Authorities used" exist in the materials.
4. Start a fresh chat every question or few to keep routing focused.

## Assumptions
- You can alt-tab/screenshot to your chosen surface during the exam (not a locked-down
  proctored browser).
- Your claude.ai plan's knowledge base holds the full corpus (~270K tokens + past papers).
