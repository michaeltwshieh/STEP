# Section A MCQ evaluation — shared-routing Round 0

## Lock and scope check

The following SHA-256 values match `routing-v2/blind/section-a/hash-lock.md`:

| Input | SHA-256 | Lock result |
|---|---|---|
| `routing-v2/corpus/mcq-20-gold.json` | `b3e5f2a07ba732bc231b06b58df0e39a5fda7b977bca1a47323e81d01047b807` | match |
| `routing-v2/blind/section-a/baseline.md` | `a7f6de27ca85ebd73ef3b5fade886805ec85f2a06a1906bfe3d4ca2261465826` | match |
| `routing-v2/blind/section-a/candidate-a.md` | `e20fbfb571893a2862105d4533de1e0d657db5ab7df2204f5537ee2234fa4676` | match |
| `routing-v2/blind/section-a/candidate-b.md` | `f9f9220680048ebd55cc740883f8a2cd6cd274065effc02fbb5bec22dfd417a4` | match |
| Candidate `Content.md` | `ce886f1f510c48094cf118d065dee42e6a0684ca9a8134a79236a5a05a2fc48f` | match |
| Candidate `routing-core.md` | `1c48e4ba391b47dc88acd07eddd078b995510ba7cf88af5d13eb73189aa15d84` | match |
| Candidate Section A adapter | `d35c707d13035f6abd763cc6ccd10e928482d605f26dfca2bc03d8ff7d513c48` | match |
| Candidate dispatcher (`CLAUDE.md`) | `07ff62d2791faa0692ce9b548f87ee6f75cf94142b0385ddf9bb4a4d738c42a3` | match |

The gold file's recorded status is synthetic regression only (`official_section_a_holdout: false`). I found no substantive conflict between the frozen propositions and the exact relevant manual/article/appendix passages. Appendix 27B is genuinely incomplete (`etc., as above`); the materials-gap treatment is required.

## Scoring convention

- Letters: one point per MCQ against `gold.correct_letter`.
- Option dispositions: one point per option; labels are exact. `partly true but not best` is not interchangeable with `refuted`.
- Governing passage: one point where the chosen route is supported by the exact governing course passage/source, not merely a similar citation.
- Wrong lock: count an operative wrong jurisdiction, regime/entity, actor, or lifecycle stage. Unsupported narrowing is noted separately if it does not change the route.
- Forbidden route: primary count below is an unqualified gold `must_not_open` route placed in `Sources used`/treated as an opened source. Explicitly rejected qualified contrasts (for example, “as a substitute” or “as presently applicable”) are not counted as operative use. I also give the answer-level adoption count, which counts only selecting/adopting a forbidden route.
- Closest/critical: one point only where both the two-option pair and the outcome-changing distinction match the gold.
- Confidence: one point per item for conformity to the gold confidence band (high/medium/low). For MCQ20, `high` is expected for identifying the materials gap; low applies only to a purported complete verbatim declaration.

## Scorecard

| Metric | Baseline | Candidate A | Candidate B |
|---|---:|---:|---:|
| Letter accuracy | **20/20** | **20/20** | **20/20** |
| Option dispositions | **77/80** | **76/80** | **75/80** |
| Governing passage located | **20/20** | **20/20** | **20/20** |
| Wrong jurisdiction/regime/actor/stage | **0** | **0** | **0** |
| Forbidden-route breaches — strict source-use count | **1** | **6** | **0** |
| Forbidden-route breaches — answer-level adoption | **0** | **0** | **0** |
| Closest-two + critical distinction | **17/20** | **17/20** | **17/20** |
| Confidence conformity (band) | **20/20** | **20/20** | **17/20** |
| Hard pass | **FAIL** | **FAIL** | **FAIL** |

All three therefore fail the required candidate hard pass: neither candidate reaches 100% on every count, and Candidate A/B do not achieve exact closest/critical performance. Candidate B additionally misses confidence conformity.

## Option-disposition failures

The chosen letters are all correct. The misses are calibration of a distractor's exact gold disposition:

- Baseline (3): Q01 option B is gold `refuted` but marked `partly true but not best`; Q02 options A and D are gold `refuted` but marked `partly true but not best`.
- Candidate A (4): Q02-B, Q04-D, Q19-B and Q20-D are gold `partly true but not best` but marked `refuted`.
- Candidate B (5): Candidate A's four misses plus Q14-A, which is gold `partly true but not best` but marked `refuted`.

The distinctions are material: the gold treats a conditional/alternative route as partly true where the item asks for the best or exact route. Wording similarity was not used for credit.

## Closest-two / distinction failures

- Baseline: Q03 selected C/D instead of gold B/D; Q05 selected A/D instead of A/C; Q06 selected A/D instead of A/C. Score 17/20.
- Candidate A: Q03 selected A/D instead of B/D; Q06 selected A/D instead of A/C; Q10 selected A/C instead of B/C. Score 17/20.
- Candidate B: Q03 selected A/D instead of B/D; Q06 selected A/D instead of A/C; Q15 selected B/D instead of A/B. Score 17/20.

The corresponding critical distinctions are also wrong in those cells: Q03 is voluntary inter vivos disposition versus death/transmission; Q05/Q06 turn on whether the registered legal holder/register changes; Q10 turns on the exact management article and existing special-resolution reserve power; Q15 is registered-agent compliance versus company-secretary administration.

## Confidence

Baseline and Candidate A use a high-confidence band for all 20 items, which conforms to the gold. Candidate B is medium on Q07 and Q08 despite the exact source route determining the answer, and medium on Q20 despite correctly identifying the explicit Appendix 27B gap; all three are gold-high items. Hence Candidate B is 17/20.

If an evaluator instead requires the numeric score to equal the gold number exactly (rather than the adapter's high/medium/low band), the exact-number counts would be Baseline 18/20, Candidate A 14/20 and Candidate B 1/20. The scorecard uses the adapter's confidence-band rule; the numeric deviations are mostly one-point calibration differences.

## Forbidden/source-isolation details

Under the strict source-use convention, the breaches are:

- Baseline: Q18 lists Appendix 31D (administrative reinstatement) in `Sources used`.
- Candidate A: Q01 lists Appendix 20E; Q02 lists the shareholder-loan repayment route (20B/20D); Q03 lists Appendix 26; Q11 lists the migration route (10A–10C); Q18 lists Appendix 31D; Q20 lists Appendix 18A. These are all gold-forbidden unqualified source openings even though the answer text rejects them.
- Candidate B: no unqualified gold-forbidden source appears in its source lists. Its references to qualified contrasts (e.g. Appendix 26 as insufficient, Appendix 21G only after checking the article, and 31B/31C as jurisdictional alternatives) are not operative forbidden-route adoption.

No answer selected a forbidden route as its governing answer. Candidate A also narrows the otherwise unknown regime to “private company” in Q03–04 and Q13–14; because that narrowing does not select a conflicting legal branch, it is logged as an ungrounded lock detail rather than a wrong-jurisdiction/regime/actor/stage error.

## A/B agreement and comparison with baseline

- Letters: A and B agree **20/20**, and both equal baseline on every letter.
- Closest/critical labels: A and B agree **18/20**. They disagree at Q10 (A/C versus B/C) and Q15 (A/B versus B/D); both jointly give the same wrong A/D pair/distinction at Q03 and Q06. Against gold, A and B each score 17/20; their common gold-matching cells are 16/20 because their error sets are the union `{Q03,Q06,Q10,Q15}`.
- Baseline comparison: baseline is best on dispositions (77 versus A 76 and B 75); all three locate the governing passage for all 20; all three have no operative lock error; baseline and A conform on confidence bands (20), while B is 17. A improves baseline's Q05 closest pair but introduces Q10; B likewise improves Q05 but introduces Q15. The candidates do not improve the baseline's letter accuracy.

## Verdict and failure classes

**Verdict: FAIL for both candidates.** Failure classes are: (1) exact option-disposition calibration, especially collapsing `partly true but not best` into `refuted`; (2) closest-two/critical-distinction selection errors around transfer/transmission, nominee legal-title movement, management-article variants and officer roles; (3) Candidate B under-confident banding on Q07/Q08/Q20; and (4) Candidate A source over-retrieval into unqualified forbidden routes. The corpus is synthetic and not evidence of real-exam accuracy.
