# Company Law Exam Bot

Everything the assistant needs for the **STEP Advanced Certificate in Company Law and Practice** examination, in one folder. Upload the folder to a claude.ai Project, or point Claude Code at it.

## What's here

| | |
|---|---|
| `CLAUDE.md` | The operating brief. Read on every turn. |
| `section-a.md` | Section A — MCQ instructions (output format, confidence bands, escalation). |
| `section-b.md` | Section B — essay instructions (structure, drafting rules, writing style, citation form). |
| `submission-checklist.md` | What to check before uploading Section B. |
| `Content.md` | Routing index: topic map, every module's section outline, every appendix's title and filename. **Consult first, every time.** |
| `Course-Manual-Module-01…12-*.md` | The 12 modules. Each ends with a `## Footnotes` section. |
| `Appendix-1A…31D-*.md` | 90 precedent documents (forms, resolutions, minutes, notices). |
| `Syllabus.md` | Each module's purpose and outcomes. Secondary routing aid. |
| `Examination Briefing Document ITM Adv Cert.md` | Official exam format, submission rules, late penalties. |
| `Examination Guidance Booklet ITM (1).md` | Examiner's approach, command words, citation and language guidance. |
| `Detection-Evidence-2026-07.md` | Research behind the writing-style rules in `section-b.md`. Reference, not instructions. |
| `CHANGELOG.md` | How the instruction files reached their current version. |

## The exam

Section A — 20 MCQs, in the assessment portal, completed first.
Section B — 5 essay questions, 4 to be answered, uploaded as one file.
4 hours total, open-book, non-invigilated, no word limit. There is no Section C or D.

## Related

Past papers and model answers: `../../Past Papers/STEP Advanced Certificate in Company Law and Practice/`.
Earlier versions of the instruction files: `../../Archive/instruction-versions/`.
The sibling bot for the other exam: `../Trust Exam bot/`.

## Keeping content current

The module, appendix, `Content.md`, `Syllabus.md` and self-assessment files here are **copies**. They are generated into `../STEP Advanced Certificate in Company Law and Practice/` by:

```
.venv/bin/python convert_pdfs.py  "STEP Advanced Certificate in Company Law and Practice"
.venv/bin/python split_corpus.py  "STEP Advanced Certificate in Company Law and Practice"
```

`split_corpus.py` wipes its own output folder on every run, which is why this folder is a separate copy — the instruction files above would not survive otherwise. After any regeneration, re-copy the content files (not the instruction files) across.

**This folder's content is a June 2026 snapshot** and has not been re-synced since. The regenerated output in `../STEP Advanced Certificate in Company Law and Practice/` differs in four appendix filenames, where truncated titles were completed; the file bodies are identical.
