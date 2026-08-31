# Independent evaluator protocol

Use only after the Baseline, Candidate A and Candidate B specimen outputs have been
saved and hash-locked.

## Inputs

- Specimen Paper 1 question extract and examination Appendix 1.
- Frozen `routing-tests/corpus/cases.json`.
- Course manuals, appendices and `Syllabus.md`.
- Official KAP extract.
- The three locked specimen outputs and their hash manifest.
- The two locked synthetic replay outputs and their hash manifest.

## KAP rule

The KAP is a Key Answer Points rubric. It is not a model-answer similarity target.
Do not score prose style, wording overlap, paragraph order or copying. A candidate may
earn coverage where its legally supported formulation differs from the KAP. A KAP
statement that conflicts with a higher course source must be logged as a source
conflict and resolved under the frozen source-precedence rule.

## Unit of evaluation

Score every question and every sub-part separately. For synthetic cases, score every
case separately. Never infer a route from a different sub-part or its partner case.

## Required comparisons

For each unit compare:

1. issue coverage;
2. routing completeness;
3. wrong inclusions;
4. governing articles and namespace;
5. jurisdiction and regime consistency;
6. lifecycle procedure stages;
7. actor and signatory selection;
8. requested and companion document selection;
9. drafting completeness, including operative components, attachments and execution;
10. authorities and source support; and
11. explicit course-material gaps and unresolved branches.

## Metrics

### Mandatory critical-route recall

`recalled frozen mandatory critical routes / all frozen mandatory critical routes`

The threshold for both candidates is 100 percent. A route counts only if the output
selects it for the correct sub-part and contribution, not if a filename appears in an
undifferentiated source list.

### Wrong lock or precedent count

Count each selected wrong jurisdiction, regime, actor, lifecycle stage or operative
precedent. Conditional alternatives do not count when clearly isolated and excluded
from the selected branch. Threshold: zero for each candidate.

### Forbidden-route breach

Count each frozen `must_not_open` route that contaminates the selected answer or draft.
A route merely recorded as excluded is not a breach. Threshold: zero.

### Material-fact disposition

`material facts given a correct and visible disposition / all frozen material facts`

Threshold: 100 percent for each candidate.

### Unresolved-branch disclosure

Every frozen unresolved branch must be selected, excluded with its deciding fact or
expressly disclosed as unresolved. Threshold: all disclosed.

### Candidate agreement

Candidate A and Candidate B must have identical selected critical routes and required
document chains. Differences in prose, optional verified sources, placeholders or
clearly discarded alternatives do not matter. Any critical route, KAP-required stage or
drafting component appearing in only one candidate is a reliability failure.

### Baseline comparison

List every baseline critical miss repaired by both candidates. Separately list every
candidate critical error absent from baseline. The new prompt passes only if it adds no
critical error relative to baseline.

## Critical failure categories

- `missed fact`
- `wrong branch`
- `wrong jurisdiction`
- `wrong regime`
- `wrong actor`
- `wrong stage`
- `wrong appendix/precedent`
- `false-positive route`
- `drafting-stage omission`
- `materials-gap concealment`
- `candidate disagreement`
- `authority unsupported`

Assign each failure to one primary category. A repair round may address only one
failure class.

## Evidence standard

Every finding must cite:

- output file and exact heading or line;
- frozen case ID and expectation;
- course file and exact section/heading or examination article; and
- KAP sub-part where relevant.

Return a pinpoint requiring verification if the source text has not been opened.
Do not award or deduct on memory.

## Required evaluator output

1. Isolation/input attestation and file-open ledger.
2. Per-question and per-sub-part specimen table.
3. Per-synthetic-case table.
4. Candidate A metrics.
5. Candidate B metrics.
6. Candidate agreement matrix.
7. Baseline misses repaired.
8. New critical errors versus baseline.
9. KAP differences and source conflicts.
10. Failure classification and focused repair recommendation, if any.
11. Pass/fail against every threshold.
12. Residual risks and untested scenarios.
