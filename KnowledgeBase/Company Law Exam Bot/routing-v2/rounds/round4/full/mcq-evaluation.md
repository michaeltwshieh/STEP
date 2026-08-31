# Round 4 final Section A evaluation

Scope was limited to the locked Round 4 Section A artifacts, the Section A
adapter/routing workflow, the frozen synthetic MCQ fixture and gold, and the
course materials. Section A only; no prior answer/report was used as evidence.
The corpus is a synthetic regression, not an official Section A holdout.

## Integrity

The following SHA-256 values matched the Round 4 lock/freeze records:

| Artifact | Actual / locked prefix | Result |
|---|---|---|
| final Section A, Candidate A | `8295ee5b81b472557d96076dd243c4b6df4b273374a88d640b027b38561a3af2` | MATCH |
| final Section A, Candidate B | `12cf8bf89ac28947a58a3e7a3e8f832f1b1039266de3900c6039332989237eba` | MATCH |
| Candidate Section A adapter | `b969f9f4c20fbac50df698aeaaf9f766fcb1c2d0b8d34662ccedb4ddb993e004` | MATCH |
| Candidate routing core | `b3d52ff790e3f6aef979b185109fa87c435959efc7e1dee05df6899138fdf95e` | MATCH |
| frozen gold | `b3e5f2a07ba732bc231b06b58df0e39a5fda7b977bca1a47323e81d01047b807` | MATCH |
| frozen question fixture | `2fdbc426e31d9d924d5f131033946537ab30d67c0a857de318eb93147d096be1` | MATCH |

## Scores

| Dimension | Candidate A | Candidate B |
|---|---:|---:|
| Letters | 20/20 | 20/20 |
| Strict oracle option dispositions | 16/20 | 18/20 |
| Governing passage/rule support | 20/20 | 20/20 |
| Answer-driving locks (jurisdiction/regime/actor/relationship/stage/qualifier) | 20/20 | 20/20 |
| Exact frozen closest-two pair | 17/20 | 17/20 |
| Materially valid outcome-changing distinction | 20/20 | 20/20 |
| Confidence band | 20/20 high | 19/20 expected high |

Letters in order (gold = both candidates): `A C D B C A A D B C D B A C B D C A D B`.

Disposition exceptions, strict against the gold labels:

- Candidate A: MCQ02 option B (`refuted` rather than `partly true but not best`);
  MCQ04 option D; MCQ19 option B; MCQ20 option D (same label difference in
  each latter three cases).
- Candidate B: MCQ02 option B and MCQ20 option D. “Supported/conditional” for
  MCQ06 option B was normalized to supported because the option itself is
  qualified by “may”.

All substituted closest pairs still state a real distinction between the
selected option and a distractor. Pair mismatches are: Candidate A MCQ03
(`A/D`, gold `B/D`), MCQ10 (`A/C`, gold `B/C`), MCQ16 (`C/D`, gold `B/D`);
Candidate B MCQ03 (`A/D`), MCQ15 (`B/D`, gold `A/B`), MCQ16 (`C/D`).

Candidate A is high on every item; its numeric score matches the gold expectation
on 18/20 (it gives 10 rather than 9 on MCQ12 and MCQ19). Candidate B is high on
19/20 and medium 7/10 on MCQ18; its numeric score matches 13/20. There are no
false-high confidence calls. Both candidates correctly preserve the MCQ20
materials gap rather than inventing missing declaration wording.

## Source passages and lock audit

Both outputs name and materially apply the governing course passages for all 20
letters: dividend regime/article (M6/M10), transfer/transmission (M6/M10),
capacity/authority (M5/M8), management articles (M7 and Appendices 1B/1C),
office move/migration (M5/M10/M4), allotment/issue (M6), officer/representative
roles (M9/M10), termination state (M12), and nominee documentation (M11 and
Appendices 26/27A/27B). No wrong regime, actor, lifecycle stage, or absolute
qualifier drove an answer. MCQ18's polarity line abbreviates the fixture's
`may,best` metadata to “correct”, but both explanations apply the zero-state
and best-route tie-break correctly.

Companion-source differences that do not change the letter: Candidate B's
item plans close some oracle-listed supporting companions (notably 27A/27B for
MCQ05 and 16C for MCQ13–14), and neither run opens the later 30C–30G examples
for MCQ17. The selected governing M10/M6/M12 passages nevertheless supply the
tested propositions and no source gap is claimed for those letters.

## Exact-open / isolation audit

Candidate B has 20 item-level exact-open attestations. They reconcile to its
frozen per-item allowlist, with zero hard-prohibited course-appendix opens,
including the MCQ17 31A–31D prohibition. Its MCQ19 opening of 27B is expressly
limited to the permitted closest-runner-up check.

Candidate A provides one global, not 20 item-level, attestation. Its own
MCQ19 source list includes `Appendix-26-Irrevocable-instruction-to-transfer-
beneficial-ownership.md` although the frozen grouped plan limits the item to
the matching bilateral nominee instrument. Its MCQ20 source list includes
both Appendix 26 and bilateral Appendix 27A although that item is the
unilateral 27B route. These are at least three evidence-supported out-of-plan
file-item accesses (two affected items); the non-itemized attestation makes
any additional cross-check access unreproducible. No gold `must_not_open`
course appendix is shown as opened, but Candidate A fails the candidate
workflow's stricter item allowlist/source-use hygiene here.

Blind isolation:

- Candidate A: PASS on its attestation (no gold, reports, peer answers, KAP or
  external law claimed).
- Candidate B: CONTAMINATED/FAIL for blind isolation. The locked Round 4 hash
  record explicitly discloses accidental access to its prior focused answer.
  The final output is retained as contamination evidence; it was not silently
  rerun and its raw scores above are not independent blind evidence.

## Agreement and disposition

The candidates agree on letters 20/20, governing rule, and answer-driving locks.
They agree on exact closest pair 19/20 (only MCQ10 differs); strict disposition
labels agree 17/20, or 18/20 after normalizing Candidate B's qualified
“supported/conditional”.

Overall: both are letter-perfect on the frozen synthetic corpus and passage-
correct. Candidate A has the cleaner confidence calibration but an incomplete
item-level open ledger and the MCQ19–20 out-of-plan nominee-file accesses.
Candidate B has slightly better strict disposition fidelity and cleaner
per-item opens, but its prior focused-answer access is a material blind-
isolation contamination and must remain flagged.
