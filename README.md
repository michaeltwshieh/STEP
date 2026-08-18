# STEP Exam Assistant

Turns a STEP course manual PDF into a knowledge base an AI assistant can answer exam questions from. Built to be repeated for each of the four STEP exams.

## Where things are

| Folder | What it holds |
|---|---|
| `Materials/<exam>/` | **Source PDFs.** One subfolder per exam. This is where you drop new material. |
| `Markdown/<exam>/` | Intermediate: the whole manual as one `.md`, plus a footnotes sidecar. Regenerable. |
| `KnowledgeBase/<exam>/` | Split output: one file per module and per appendix, plus `Content.md`. Regenerable. |
| `KnowledgeBase/<exam> Bot/` | **The finished product.** Self-contained — content *plus* the assistant's instructions. This is what you upload to a claude.ai Project. |
| `Past Papers/<exam>/` | Specimen papers and model answers, for dry-running. |
| `Archive/` | Superseded instruction versions and old snapshots. Nothing here is live. |
| `SETUP.md` | The detailed playbook: pipeline, per-exam settings, verification checklist, every gotcha hit so far. **Read this before starting a new exam.** |

Current bots: `KnowledgeBase/Company Law Exam Bot/` and `KnowledgeBase/Trust Exam bot/`.

## Adding a new exam

```bash
# 1. Drop the PDFs in Materials/<exam>/, named exactly:
#      Course Manual.pdf     (capital M -- the footnote extractor matches this string)
#      Appendices.pdf

# 2. Convert  (~3 min; docling)
.venv/bin/python convert_pdfs.py "<exam>"

# 3. Add an EXAMS entry in split_corpus.py -- module titles from the manual's
#    own Contents page, plus the topic map. See SETUP.md section 3.

# 4. Split
.venv/bin/python split_corpus.py "<exam>"

# 5. Verify -- SETUP.md section 4. Footnote gaps should be zero.

# 6. Build the bot folder: copy the split output into
#    "KnowledgeBase/<exam> Bot/", then adapt CLAUDE.md, section-a.md and
#    section-b.md from an existing bot.
```

## Two things that will bite you

**`split_corpus.py` wipes its output folder on every run.** It only ever targets `KnowledgeBase/<exam>/`, never a `... Bot/` folder — which is exactly why the bots are separate copies. Anything hand-written inside `KnowledgeBase/<exam>/` is lost on the next run.

**The bot folders hold copies.** After regenerating content, re-copy the module/appendix/`Content.md` files into the bot folder. Do not copy the instruction files back.

## The exam

Section A — 20 MCQs, in the assessment portal, done first.
Section B — 5 essay questions, 4 to be answered, uploaded as a single file.
4 hours total, open-book, non-invigilated, no word limit. There is no Section C or D.
