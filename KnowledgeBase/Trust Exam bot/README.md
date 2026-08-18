# Trust Exam bot

Everything the assistant needs for the **STEP Advanced Certificate in Trusts – Law and Practice (International)** examination, in one folder. Upload the folder to a claude.ai Project, or point Claude Code at it.

## What's here

| | |
|---|---|
| `CLAUDE.md` | The operating brief. Read on every turn. |
| `section-a.md` | Section A — MCQ instructions (output format, confidence bands, escalation). |
| `section-b.md` | Section B — essay instructions (structure, drafting rules, writing style, citation form). |
| `submission-checklist.md` | What to check before uploading Section B. |
| `Content.md` | Routing index: topic map, every module's section outline, every appendix's title and filename. **Consult first, every time.** |
| `Course-Manual-Module-01…11-*.md` | The 11 modules. Each ends with a `## Footnotes` section. |
| `Appendix-1…32-*.md` | 37 precedent documents (deeds, trustees' resolutions, memoranda, powers of attorney). |
| `Examination Briefing Document ITM Adv Cert.md` | Official exam format, submission rules, late penalties. |
| `Examination Guidance Booklet ITM (1).md` | Examiner's approach, command words, citation and language guidance. |
| `Detection-Evidence-2026-07.md` | Research behind the writing-style rules in `section-b.md`. Reference, not instructions. |
| `CHANGELOG.md` | How this folder was built and what was adapted from the Company Law set. |

## The exam

Section A — 20 MCQs, in the assessment portal, completed first.
Section B — 5 essay questions, 4 to be answered, uploaded as one file.
4 hours total, open-book, non-invigilated, no word limit. There is no Section C or D.

## Related

Past papers and model answers: none yet for this exam. (Company Law's are at `../../Past Papers/STEP Advanced Certificate in Company Law and Practice/`.)
Earlier versions of the instruction files: `../../Archive/instruction-versions/`.
The sibling bot for the other exam: `../Company Law Exam Bot/`.

## Provenance

The three instruction files derive from the Company Law set in `../Company Law Exam Bot/`, adapted for this exam. See `CHANGELOG.md` for what changed and what was carried over.

`Syllabus.md` is deliberately absent — CLT International did not supply a syllabus PDF for this course, so module titles were taken from the course manual's own Contents page. It is the one file the Company Law bot has that this folder cannot.

## Keeping content current

The module, appendix and `Content.md` files here are **copies**. They are generated into `../STEP Advanced Certificate in Trusts - Law and Practice/` by:

```
.venv/bin/python convert_pdfs.py  "STEP Advanced Certificate in Trusts - Law and Practice"
.venv/bin/python split_corpus.py  "STEP Advanced Certificate in Trusts - Law and Practice"
```

`split_corpus.py` wipes its own output folder on every run, which is why this folder is a separate copy — the instruction files above would not survive otherwise. After any regeneration, re-copy the content files (not the instruction files) across.
