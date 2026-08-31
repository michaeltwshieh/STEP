# Round 0 record

Failure status: failed zero-critical-error and candidate-agreement gates.

| Artifact | SHA-256 |
|---|---|
| prompt version 0 | `095a1302f66b93a2153717db4807439b68e44771e2bf9a8ef01cf7cfb5880e94` |
| evaluator report | `14752e5c404ccc2f6e8832d1bffd8704d5a10a7d310323b8a7c124a6499dfc1c` |
| static check | `c5393728300188e1300dabf546aeab01b22ddf2c5604bbbdcbd0b727d3f698a1` |

Primary evaluator-recommended repair class: `drafting-stage omission`.

Main source verification confirmed the Q1, Q2, Q3, Q4 and P08B pinpoint findings.
It found one evaluator metric error: `cases.json` contains 31 frozen unresolved-branch
entries, not 34. A read-only evaluator addendum was requested before the metrics are
treated as final.

Corrected results: Candidate A 30/31 (96.77%); Candidate B 29/31 (93.55%). Both remain
failures, and the round verdict is unchanged.

No live operational instruction was changed in this round.
