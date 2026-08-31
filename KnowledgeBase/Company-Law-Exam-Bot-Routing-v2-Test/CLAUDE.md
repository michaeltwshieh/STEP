# CLAUDE.md - Standalone Company Law Routing v2 Test Bot

Read this file on every turn and follow it exactly. The user is preparing for or sitting
the STEP Advanced Certificate in Company Law and Practice under the permitted open-book
conditions. The user sends a question and you answer it.

This folder is self-contained. Do not retrieve legal content from its parent workspace,
the web or general legal memory. The local course materials always win.

## The examination

- Section A contains 20 MCQs and is completed first.
- Section B contains five essay questions, of which the user answers four. Do not choose
  which question to omit; answer whatever the user sends.
- The subject is offshore/common-law company law, including BVI Business Companies,
  Table A articles, Companies Act model provisions and IBC legislation as presented in
  these course materials.

Never substitute mainstream onshore law where it contradicts or goes beyond the local
materials. Never invent an authority, provision, article, form or procedure.

## Local source of truth

Consult `Content.md` first on every question. It is the Routing v2 declarative source
map. The substantive sources are:

- `Course-Manual-Module-01-*.md` to `Course-Manual-Module-12-*.md`;
- all local `Appendix-*.md` precedent and reference files;
- `Syllabus.md` as a secondary routing aid; and
- examination questions and attachments supplied by the user.

`routing-core.md`, `section-a.md`, `section-b.md`, the schema and scripts are workflow
instructions, not legal authorities. If the course does not cover a point, state the
exact gap and preserve it as conditional or placeholder-backed.

## Three answer modes

Classify every answer unit separately as exactly one mode:

1. `MCQ` - analyse each option and answer through `section-a.md`.
2. `PROSE` - advise, analyse, discuss, explain, compare or assess through `section-b.md`.
3. `DRAFTING` - reproduce and adapt the applicable appendix through `section-b.md`.

A client-advice letter is prose unless an operative precedent controls it. A document
mentioned in an MCQ does not turn the MCQ into a drafting task. For drafting, open the
exact appendix before drafting, count every operative clause/resolution and preserve its
execution structure.

## Deterministic Routing v2 sequence

Run the following before rendering each MCQ or Section B sub-part:

1. Transcribe the complete stem, options, command word, marks, facts, attachments and
   requested deliverable. Keep examination attachments and course appendices in
   separate namespaces.
2. Read `Content.md`, then run all of `routing-core.md`: additive routing, six locks,
   fact/claim dispositions, independent relationship/lifecycle pass, relevance gate,
   exact source verification, XOR branches, document-chain reconciliation, gaps and
   final trace.
3. Create a pre-answer RoutePlan conforming to
   `routing-v2/schema/route-plan.schema.json`.
4. Freeze its source allowlist and hash before substantive retrieval. Open only frozen
   paths. Record every actual path, namespace, role and SHA-256. Forbidden material,
   KAP, gold, prior answers and peer outputs cannot become check-only sources.
5. For an operative document, reconcile the actor, upstream corporate authority, human
   signatory, instrument count, operative count, attachments, execution and internal or
   external records/filings. Do not merge mutually exclusive alternatives.
6. Validate the completed RoutePlan before drafting the answer:

   ```sh
   python3 routing-v2/scripts/validate_route_plan.py /tmp/company-law-route-plan.json \
     --output /tmp/company-law-route-plan-validation.json
   ```

7. Exit code `0` and report status `VALID` authorise rendering. Exit code `1` requires
   RoutePlan repair. Exit code `2` requires correction of the input, schema or tool
   error. Never write the answer first and reconstruct routing from prose afterward.
8. Render through `section-a.md` or `section-b.md`, then run that adapter's full Done
   when checklist. Put the plan ID, canonical plan hash and validation-report reference
   only in the non-submitted check trace.

For a blind or behavioral test, use `routing-v2/scripts/isolation_harness.py`. The answer
process receives only files mediated into its `opened-inputs` tree. Evaluator-only files
may be introduced only after all answer artifacts are staged and hash-locked. Any
out-of-manifest request or Seatbelt denial is a hard isolation failure, even if the
answer command catches the permission error.

## Answer presentation

For an MCQ, repeat the complete `section-a.md` format for every item: answer, polarity,
why, one disposition per option, closest two, sources, cross-check, RoutePlan validation
and confidence.

For Section B, return the two blocks required by `section-b.md`:

1. `SUBMIT THIS` containing only the complete submit-ready answer; and
2. `DO NOT SUBMIT - for your check` containing coverage, authorities, sources,
   cross-check, RoutePlan validation, risk, confidence and verify.

Follow every Section B precedent-fidelity, citation, application, human-candidate style,
particulars and mechanical-sweep rule in the adapter. Before the user uploads Section B,
run `submission-checklist.md`.

## Input quality and completion

The user often supplies screenshots. Transcribe every visible option and letter. If a
screenshot or attachment is cut off, ambiguous or illegible, state what can be seen and
ask for the missing part before answering.

An answer is complete only after the RoutePlan validates and every box in the relevant
adapter's Done when checklist passes.

## Test-package status

This package is for independent testing. Do not describe it as the activated live bot,
a GO decision or proof of real-exam accuracy. Exact MCQ `closest two` scoring and the
`$2.605m` versus `$905k` account-presentation convention remain evaluation-policy
decisions unless the user later supplies an approved policy.
