# Round 0 Metric Addendum

The frozen denominator is **31**, taken directly from the explicit
`unresolved_branches` arrays in `cases.json`.

| Candidate | Correct result | Threshold |
|---|---:|---|
| Candidate A | **30/31 = 96.77%** | **FAIL**, all 31 required |
| Candidate B | **29/31 = 93.55%** | **FAIL**, all 31 required |

Missed branches:

- Candidate A, P05B: `board approval/refusal`.
- Candidate B, P01B: `whether solvency evidence is sufficient`.
- Candidate B, P05B: `board approval/refusal`.

A branch counted as disclosed where the output selected it, excluded it using the
deciding fact or expressly identified the relevant fact/form/evidence as a gap, even if
it was not under the output's `UNRESOLVED_BRANCHES` label.

The corrected denominator does not change the round verdict, Candidate A/B agreement
failure or any other metric. The evaluator performed the correction read-only using
the frozen corpus and five hash-locked outputs only.
