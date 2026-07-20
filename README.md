# Proposed Revisions v2 — self-sufficiency for a cheaper model (2026-07-12)

Drop-in replacements for `CLAUDE.md`, `section-a.md`, `section-b.md`. The originals
in `KnowledgeBase/` and the earlier `Proposed-Revisions/` (2026-06-27) are untouched.

## Why

The originals were written for a strong model that fills gaps itself. These versions
make the implicit explicit so Opus/Sonnet can follow them without guessing: file
locations, the complete file inventory, testable confidence bands, letter-format
questions, sub-part labelling, and a "Done when" checklist per section.

## What changed

**Folded in the pending 2026-06-27 revisions** (second-pass cross-module check +
Cross-check/Cross-checked lines) — verified their §-references against `Content.md`
before adopting. If your dry-run rejected them, strip CLAUDE.md step 5, the
Cross-check bullet in section-a, and the Cross-checked line + second-pass paragraph
in section-b; everything else stands alone.

**CLAUDE.md** — added "Where everything lives" (paths); completed the source-of-truth
inventory (Self-Assessment Answers, Syllabus, exam-admin docs, with usage rules);
multi-question screenshots; a Definition of done pointing at the per-section
checklists; one line routing letters to section-b.

**section-a.md** — scope note (MCQ output is never submitted, so Section B style
bans don't apply); confidence bands defined testably (high = governing sentence
found, no inference; medium = inference or live second option; low = unresolved
after escalation); multi-question handling; "Done when" checklist.

**section-b.md** — sub-part labelling + conditional mark-weighting; letter sub-parts
section (from the guidance booklet: prose task, formal layout, placeholder
signature); drafting rule 3 extended (opened precedent ⇒ operative wording
reproduced, even if used only for shape); in-materials citation examples
(*Trevor v Whitworth (1887)*, *section 61 of the Companies Act 1948*); em-dash ban
scoped to the submitted essay; "Done when" = the booklet's five self-check questions
+ a mechanical style/leak sweep. **All style/humanising rules are byte-identical to
the original.**

## 2026-07-12 (later): humanizer section upgraded after online research

`section-b.md`'s Writing style section is no longer byte-identical to the original —
it was extended after researching current detector mechanics (Turnitin windowed
sentence-level scoring), the Wikipedia "Signs of AI writing" catalogue, and the
stylometry literature. New: three-lever hierarchy (structure > grounding > vocabulary),
2024+ banned-word cluster + density principle, typography/mechanics rules (en-dashes,
curly quotes, BrE, markdown residue), "not only…but also" / "This ensures…" / false-range
tells, referential cohesion, bare paragraph openers (transition density), fact-grounding
with a portability test, stance/hedging rules, pet-phrase idiolect, and questions as a
syntactic move. The Done-when sweep gained matching checks. All pre-existing rules kept.

## 2026-07-12 (later still): detector-ensemble audit folded in

After a per-detector audit (Turnitin, GPTZero, Originality.ai, Copyleaks, Winston,
Pangram, ZeroGPT, Sapling) and a humanizer-tool study, `section-b.md` gained: the
ensemble framing (different detectors weight different signals, so all levers must
hold at once); compose-in-register-from-sentence-one (never draft-then-humanise —
Turnitin flags "AI-paraphrased" as its own category); hard bans on commercial
humanizer tools and invisible-character tricks (the latter reads as deliberate
deception); and the anti-polish rule (uniform fluency is itself a signal and the
top false-positive trigger). Hue Write was specifically investigated: marketing
only, no technical disclosure, and it failed Originality.ai/Copyleaks/Scribbr
(Turnitin-linked) at 99-100% in the one independent-ish test found — its stated
principles are already what this file teaches. Do not bolt it on after the fact.

## How to verify

Diff each file against the original, then run one MCQ and one essay (ideally one
with a letter or drafting sub-part) with a cheaper model and judge by: the trace
lines, the Done-when sweep actually running, and zero style-ban hits in the
SUBMIT block.
