# Focused deterministic behavioral evidence

`run_focused_behavioral.py` executes two structurally different RoutePlan candidates in
separate macOS sandbox input/output trees. Both receive only the case-reference manifest,
the selected candidate workflow and allowlisted course files. The frozen gold, corrected
oracle and KAP enter an evaluator tree only after all answer artifacts are SHA-256 locked.

The retained evidence under `evidence/` covers the known action-notice, managed borrowing,
XOR branch and source-access defects. It is deliberately focused: it is not a rerun of the
full Section A plus Section B activation gate and must not be described as GO.

Reproduce into a fresh directory:

```sh
python3 routing-v2/scripts/run_focused_behavioral.py \
  --output-dir /tmp/company-law-focused-route-plan-evidence
```
