# New Goal Repair Round 4

- Failure class: MCQ forbidden file opening despite clean source output.
- Evidence: Repair 3 Candidate B disclosed opening Appendix 31A for MCQ17 even though
  it was a frozen hard-prohibition route and was omitted from `Sources used`.
- Focused change: add a frozen pre-open allowlist, make option filenames
  non-self-authorising, require rejection from the governing source/Content decision
  row, and reconcile an exact-open ledger before completion.
- File changed: candidate `section-a.md` only.
- Gold/oracle: unchanged.
- This is the fourth and final repair round.

## Focused result

- Both candidates froze an allowlist containing Module 12 and Appendices 30A/30B,
  answered MCQ17 as C, and attested that Appendices 31A-31D were not opened.
- Verdict: PASS focused reliability gate; final full Section A + Section B rerun
  authorised.

## Final full-suite result

- Section A letters: 20/20 for both; strict dispositions and closest-two distinctions
  remained below 100%. Candidate A had out-of-plan source accesses; Candidate B
  disclosed prior-focused-answer contamination.
- Section B strict critical routes: Candidate A 20/23; Candidate B 18/23.
- Verdict: **FAIL**. Four-round limit reached. Candidate not activated; terminal
  decision recorded in `routing-v2/NO-GO.md`.
