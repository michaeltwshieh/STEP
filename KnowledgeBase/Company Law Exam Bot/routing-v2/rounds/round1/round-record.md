# New Goal Repair Round 1

- Failure class: drafting document-chain completeness.
- Evidence: both Round 0 Section B candidates omitted two core Appendix 30B notice
  resolutions and the separate upstream authority instruments for the corporate
  nominee/corporate director; Candidate A also selected 25M over 25N and omitted a
  distinct Bill of Sale.
- Focused change: added a requested-document chain, independent instrument-count
  derivation, corporate-actor upstream authority rule, notice-operative reconciliation,
  exhibit enumeration and expected/actual count gate.
- Files changed: candidate `routing-core.md` and `section-b.md` only.
- Gold/oracle: unchanged.

## Focused result

- Candidate A: Q1.1 produced five operative resolutions; Q2.2 produced four authority
  instruments and five attachment categories.
- Candidate B: Q2.2 produced the same four-instrument/five-attachment architecture,
  but Q1.1 still produced only the winding-up resolution.
- Verdict: **FAIL reliability**. The upstream Q2 chain is repaired in both, but the
  notice-operative omission persists nondeterministically.
- Full-suite rerun: not started because the affected focused test did not pass in both
  candidates, as required by the iteration gate.
