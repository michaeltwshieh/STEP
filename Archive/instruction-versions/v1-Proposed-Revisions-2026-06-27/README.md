# Proposed Revisions — cross-module routing (2026-06-27)

These are **drop-in replacement copies** of three knowledge-base files, with one
change each. The originals in `KnowledgeBase/` are **untouched**. Diff these against
the originals, and only copy them over if you're convinced.

## Why

The routing risk we're hardening against is **confidently-incomplete** answers:
the assistant answers fully from one correct module, feels sure, and never reaches
a second module that held part of the answer. The Section-A confidence-escalation
fires only when the assistant is *already unsure*, so it can't catch this — and it
is MCQ-only. Section B essays (the bigger cross-module risk) have no equivalent.

**Your Section-A MCQ escalation is working (full marks on test questions), so it is
left exactly as-is.** These changes are additive insurance, weighted to essays.

## What changed (three files)

1. **`CLAUDE.md`** — routing workflow **step 5** upgraded from the one-line
   "If the question spans several modules, draw on each" into a real **second-pass
   procedure** that runs on every question regardless of confidence: name a candidate
   second module → scan the section outlines already in `Content.md` → apply a
   relevance gate that **defaults to discard** → incorporate or drop → leave a
   one-line trace. Lives here so it binds **both** MCQ and essay.

2. **`section-a.md`** — escalation block untouched. Added one **`Cross-check:`** line
   to the output format and a one-sentence note that the proactive second-pass
   (CLAUDE.md step 5) is separate from the existing reactive escalation.

3. **`section-b.md`** — added a **`Cross-checked:`** line to the DO-NOT-SUBMIT check
   panel, and a one-line pointer to the second-pass. Submitted prose is unaffected.

## The relevance gate (the part that stops it backfiring)

Incorporate the second module **only if** it supplies a rule, procedure, or authority
the question actually asks for that the primary module doesn't already give. Overlap /
restatement / background → drop. For an MCQ, sharper: include only if it changes the
correct option or the confidence. **Bias to exclusion** — a wrong inclusion loses
marks for irrelevance; a correct exclusion costs nothing.

## The trace (so the invisible failure becomes visible)

Every answer carries a one-line trace in the check panel / Sources line **only** (never
the submitted prose), e.g.
`Cross-checked: Module 10 §5.7 → incorporated; Module 12 → considered, not relevant.`
An empty-handed trace ("considered X, nothing relevant") is still required — it proves
the pass ran, and lets you catch a wrong discard before transcribing.

## Deferred on purpose

No change to `split_corpus.py` / `TOPIC_MAP`. Curated cross-references in the topic map
were deferred until your dry-run shows a specific link the outline-scan actually misses.
The procedural rule + outline-scan + trace port unchanged to your other three exams;
only `TOPIC_MAP` is subject-specific.

## How to verify (your dry-run)

Run deliberately cross-module questions and judge by **the trace and the discard
decisions**, not by whether the prose looks right. Good candidates:
- "procedure to declare and pay a distribution from a BVI BC" → Module 6 + Module 10 §5.8 + Appendix 20E
- "a transaction in which a director is interested" → Module 8 (duties) + Module 10 (quorum) + Appendix 23A
- "borrowing secured by a charge, and default" → Module 6 §3 + Module 10 §5.11 + Module 12 (receivership)

Pass = the trace names the second/third module and a verdict you agree with. A blank or
single-module trace on these is a fail.
