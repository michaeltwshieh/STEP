# New Goal Repair Round 3

- Failure class: MCQ forbidden-source over-retrieval.
- Evidence: Round 2 full evaluation recorded 5 strict forbidden hits for Candidate A
  and 31 for Candidate B, even though neither adopted those routes as its answer.
- Focused change: require distractors to be tested first against the governing passage;
  prohibit opening/listing a distractor source unless it can change the letter or
  confidence; restrict `Sources used` to incorporated evidence.
- File changed: candidate `section-a.md` only.
- Gold/oracle: unchanged.

## Focused result

- Candidate A used only the governing sources for MCQ11/15/17 and did not open the
  named distractor appendices.
- Candidate B kept its source lists clean but its exact-open attestation shows it still
  opened Appendix 31A for MCQ17, a frozen hard-prohibition route.
- Verdict: **FAIL reliability**. Source-list contamination improved, but actual
  forbidden opening persists nondeterministically.
- Full-suite rerun: not started because both focused candidates did not pass.
