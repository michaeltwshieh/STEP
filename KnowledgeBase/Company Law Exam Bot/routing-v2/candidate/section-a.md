# Section A - MCQ Adapter

Run `Content.md` and `routing-core.md` first. This file contains only MCQ analysis,
output, confidence and completion rules.

Do not write the MCQ response until the unit's RoutePlan has passed
`routing-v2/scripts/validate_route_plan.py`. The adapter consumes the validated plan;
it never reconstructs routing fields from the response.

## Option-level decomposition

For every MCQ record:

1. the complete question stem;
2. polarity: `correct`, `incorrect`, `not`, `except`, `best` or other exact wording;
3. each option as an independent legal proposition;
4. for each option: jurisdiction, regime, actor, stage, absolute qualifier
   (`always`, `only`, `must`, `may`) and stated/unstated exception;
5. candidate source required for that option; and
6. verdict: `supported`, `refuted`, `partly true but not best`, or
   `materials do not resolve`.

Do not route only the stem. Do not let one true clause rescue an option whose absolute
qualifier or second clause is false.

## Closest-two test

Identify the two closest options and state the single outcome-changing distinction:
jurisdiction, actor, stage, condition, exception, qualifier or governing source.

For `best`, explain why the runner-up is tempting but incomplete, less direct or
dependent on an unstated condition.

## Source use

- Before opening any substantive course file, create a per-option access plan from the
  `Content.md` map. Mark each candidate `OPEN` or `DO NOT OPEN`. Only `OPEN` files may
  be accessed for that MCQ. Freeze the plan before retrieval; a filename printed in an
  option is never self-authorising.
- Verify the governing passage exactly.
- Incorporate a second source only if it changes the letter or confidence.
- Do not open every appendix or module named in a distractor. First test each option's
  proposition against the already-open governing passage and the declarative
  distinction in `Content.md`. Open the distractor's own source only when the governing
  passage cannot determine whether it is supported, refuted or conditionally true and
  the result could change the letter or confidence.
- `Sources used` lists only passages actually incorporated as evidence. A rejected
  distractor route stays in the option explanation or cross-check as a descriptive
  route label; do not add its exact filename merely to prove that it was rejected.
- A frozen/test `must not open` route is a hard prohibition, including source-list use
  as a comparator. Refute it from the governing source, the question facts and the
  declarative `Content.md` appendix-decision row. Do not open the prohibited appendix
  “only to check” it.
- After the answer is determined, provide an exact-open attestation. Any accessed file
  absent from the frozen `OPEN` plan is a completion failure; do not answer until the
  plan and access ledger reconcile.
- An option mentioning a notice, resolution, minute or form remains an MCQ claim; do
  not draft the document.
- If materials do not resolve the letter after the shared escalation, say so rather
  than inventing a high-confidence answer.

## Output format

- **Answer:** `<letter>` - `<full chosen option>`
- **Polarity:** `<exact polarity and how it was applied>`
- **Why:** governing rule and decisive distinction.
- **Option A:** supported / refuted / partly true but not best / unresolved - reason.
- **Option B:** ...
- **Option C:** ...
- **Option D:** ...
- **Closest two:** `<letters>` - `<one outcome-changing distinction>`
- **Sources used:** exact module/section/appendix filenames.
- **Cross-check:** incorporated or discarded second source and why.
- **RoutePlan validation:** `VALID` - plan ID, canonical plan SHA-256 and retained
  validation-report reference.
- **Confidence:** high / medium / low plus score out of 10 and verify note if needed.

Commit one letter unless the course materials genuinely do not resolve the item. If
several MCQs are supplied, repeat the complete format for each.

## Confidence

- **High (8-10):** exact governing passages determine the letter and refute the closest
  distractor without an inferential leap.
- **Medium (5-7):** governing passages are located but one option requires an inference
  or an unstated fact remains genuinely arguable.
- **Low (0-4):** after full shared routing and adjacent-source escalation, course
  materials do not resolve the letter. Name the missing proposition.

Never inflate confidence. A synthetic regression pass is not evidence of real exam
accuracy; official unseen Section A material remains an external holdout.

## Done when

- [ ] Stem and polarity transcribed exactly.
- [ ] Every option independently routed and given a verdict.
- [ ] Jurisdiction, actor, stage, qualifier and exception checked per option.
- [ ] Exact governing passage located for the chosen letter and closest distractor.
- [ ] Closest-two distinction stated.
- [ ] One letter committed, or a genuine materials gap expressly stated.
- [ ] Sources, cross-check and honest confidence included.
- [ ] RoutePlan validator returned exit code zero; plan ID/hash/report recorded.
- [ ] No Section B drafting workflow activated merely by document terminology.
