# Detection evidence — Turnitin AI report, July 2026

Everything in the writing-style section of `section-b.md` marked **[measured]** comes from here. This file exists so a future session does not have to re-derive it from the PDF.

## The source

A full practice attempt at **Specimen Examination Paper 1** (on disk at `STEP Exam/Testing/Specimen Paper/`), written under the July 2026 version of `section-b.md`, submitted to Turnitin.

| | |
|---|---|
| Submission | `Answers.docx`, 40 pages, 14,857 words |
| Report | `AI_Report_2996746493.pdf`, 42 pages |
| **AI-generated** | **34%** |
| **AI-paraphrased** | **0%** |
| Questions answered | all five (only four were required) |

The 0% paraphrase score is the direct vindication of the two absolute bans in `section-b.md`: no commercial humanizer, no invisible-character tricks. Turnitin runs a separate classifier for AI-paraphrased text and found nothing. Keep both bans.

## Method

Turnitin marks flagged text with a cyan fill, `rgb(0.320, 0.777, 0.855)`, drawn as filled rectangles behind the words. Extracted with PyMuPDF by taking every word whose centre point falls inside one of those rectangles. Reproduces 25.9% against Turnitin's stated 34% (they exclude some text from the denominator as non-qualifying), so all figures below are internally consistent but should be read as relative, not absolute.

## Finding 1 — detection is blocky

| | count | median | mean | max |
|---|---|---|---|---|
| flagged runs | 35 | 47 words | 94 words | 346 words |
| clean runs | 36 | 32 words | 262 words | 2,395 words |

The classifier scores passages, not sentences. Once a passage tips, all of it tips — whole pages came back at 0% and whole pages at 98%, in one script written to one set of rules. **This is why sentence-level style rules were diluted: they operate below the scale being scored.**

## Finding 2 — the discriminator is particulars, not citations

Blocks of 60+ words, flagged vs clean:

| | flagged (n=15) | clean (n=17) |
|---|---|---|
| question-specific particulars per 100 words | 0.33 | **1.49** |
| blocks containing none at all | **67%** | 35% |
| $ and % figures per 100 words | 0.13 | **0.97** |
| article/section citations per 100 words | **1.22** | 0.86 |

Citing law does not protect. Flagged blocks cited *more* statute than clean ones. Sentence-level analysis showed the same: flagged sentences averaged 1.10 citation tokens against 0.80 for clean ones, and were *shorter* (25.1 vs 28.7 words). Every intuitive style hypothesis fails at sentence level; only the block-level particulars gap holds up.

**The two passages that scored 0%:**

1. Pages 8-9 — C's 70 per cent against D and E's 30 per cent, worked through articles 12.6, 12.7, 12.8, with the arithmetic on the page.
2. Pages 33-34 — the exoneration position statute by statute across the Bahamas, BVI, Bermuda, Jersey, Guernsey and England. No question facts at all, but unrepeatable specificity.

**The passage that scored 98%** (page 25), citing just as heavily:

> "A director appointed by a service provider owes the company the same fiduciary duty of good faith and the same duty of care and skill as any other director, restated for BVI companies in ss.120 and 122 BCA."

Accurate, well written, cited. Textbook. A model generates it fluently from priors.

## Finding 3 — where the flagged text actually was

Functional classification of the 3,292 flagged words (judgement, not machine-labelled):

| what the block was doing | share of flagged text | mark effect of fixing it |
|---|---|---|
| free-floating legal exposition | **~57%** | **positive** |
| applied analysis that flagged anyway | ~24% | — |
| conclusions and evaluative synthesis | ~13% | negative |
| case-story narration | ~6% | **positive** |

Examples of the largest category: the history of the Limited Liability Act 1855 (174 words), the general duties of a liquidator (164), the general position of a nominee director (337).

## Finding 4 — question choice dominates everything

| question | words | AI% | prose only | prose AI% |
|---|---|---|---|---|
| Q1 meetings, voting, C/D/E at 70/20/10 | 1,933 | 12.1% | 1,646 | **10.4%** |
| Q2 borrowing, Mr AB's $5m Lear jet | 3,419 | 15.1% | 2,107 | 24.5% |
| **Q3 division of powers, nominee directors** | 2,486 | **49.8%** | 2,486 | **49.8%** |
| Q4 essay, "a directorship is a double-edged sword" | 2,739 | 27.2% | 2,739 | 27.2% |
| Q5 liquidation, statement of account | 2,142 | 26.1% | 1,737 | 26.3% |
| **drafted precedent throughout** | **2,004** | | | **8.2%** |

Q3 alone produced 1,238 flagged words — **38% of everything flagged in the script.** Dropping it takes 34% to roughly 16% with no writing changes. Only four answers were required; five were written.

Drafting is nearly safe at 8.2%, and dilutes: it cut Q2's headline number by 9 points.

**Why Q3 and not Q4.** The prediction was that Q4, the pure essay with no facts at all, would be worst. It was not. Q3's sub-parts asked for *"the usual division of power… and why it arose from a historical perspective"* and *"how such division of power is affected when the Company is an underlying asset-holding company"* — general accounts with nothing to enumerate. Q4 asked candidates to *"identify the main problem areas and state how a director may seek to reduce the exposure"* — which decomposes into a list of risks, protections and jurisdictional positions, and produced the 0% pages. Hence the two-axis test in `section-b.md`: scenario-independence alone does not predict; independence **plus** non-enumerability does.

## Finding 5 — two of the file's own rules were counterproductive

Per 1,000 words, inside flagged vs clean blocks:

| construction | flagged | clean |
|---|---|---|
| rhetorical questions — *recommended* by the old line 101 | 0.66 | 0.22 |
| negative parallelism — already banned, appeared anyway | 1.65 | 0.33 |

Small counts, so weak evidence, but both point one way. The rhetorical-question rule has been deleted. The negative-parallelism ban has been extended specifically to conclusions, where the pressure to commit kept reproducing it: *"The director who is genuinely safe is not the one with the thickest indemnity. He is the one who…"* (page 35, 97% flagged).

Separately, the old burstiness rule ("some sentences must be very short — four words") contradicted the existing ban on clustered fragments, and the script resolved it the wrong way: *"The loan is $5 million. The board therefore cannot borrow this money on its own authority. The word 'previous' carries weight."* — page 11, inside a 280-word flagged block. `section-b.md` now states which rule governs.

## What is NOT established

- **That deleting the sentence-level style rules would lower the score.** There is no counterfactual. The whole script was written with burstiness, syntactic variety and perplexity rules in force; nobody has seen what happens without them. They may have been helping. They are retained and marked `[untested]` for exactly this reason.
- **That the fixes work.** No A/B test was run. The single highest-value experiment available is to regenerate Question 3 under the particulars constraint and resubmit it alone: 2,500 words, one number, and it would settle the causal story. If Turnitin access returns, do that before anything else.
- **Any of this at n>1.** One script, one paper, five questions. The block-level particulars gap is the most robust finding; the question-ranking heuristic is the least.

## Codex's review, for the record

A ChatGPT review of the July file proposed five additions. Checked against the report: (1) vary the analytical sequence and (2) dispose of peripheral points briefly were **already in the file**; (4) let uncertainty remain was already there at paragraph level; (3) do not polish every sentence was a genuine sharpening and has been adopted as `[untested]`; (5) let the reasoning change direction in real time was **rejected** — it collides with the booklet's "illogical order, repeating information" fault, and the report contains a direct counterexample, since *"Suppose the board went ahead anyway."* (page 11) is exactly that move and sits inside a flagged block.

Its diagnosis was right and its prescription was wrong: the file did instruct at the wrong level, but the answer was not a different *reasoning* posture. It was content selection.
