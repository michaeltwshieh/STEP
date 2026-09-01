# Shared Routing Core

Run this algorithm for every MCQ, prose sub-part and drafting sub-part before entering
the section adapter. `Content.md` is the only legal source map. This file contains no
topic-to-source mapping and does not state law.

## 0. Deterministic pre-answer gate

Routing is a structured artifact, not prompt-only bookkeeping. For each answer unit:

1. create a `RoutePlan` JSON conforming to
   `routing-v2/schema/route-plan.schema.json` before rendering answer prose;
2. populate the answer-unit fields, facts/claims, mandatory Trust classification
   arrays, entities, candidate routes, route relationship sets and a frozen pre-open
   allowlist before opening a substantive source;
3. open only allowlisted sources and add their exact relative path, namespace, role and
   SHA-256 to `actual_open`;
4. complete the requested-document chain, materials gaps and final route trace;
5. run `python3 routing-v2/scripts/validate_route_plan.py <plan.json> --output
   <validation-report.json>`; and
6. after a `VALID` report and exit code zero, apply the plan's render decision: enter the
   adapter for `render`, enter it with explicit gaps for `render_with_placeholders`, and
   do not produce substantive content for `do_not_render`. Retain the report and its
   plan hash in the private check trace.

Never infer these fields by parsing a completed answer. If validation fails, repair the
RoutePlan and validate again; do not render around the failure. In a blind or behavioral
test, use `routing-v2/scripts/isolation_harness.py` so the allowlist is also enforced at
the filesystem/tool layer and evaluator-only files remain unavailable until answer
hashes lock.

## 1. Input completeness and namespace

1. Transcribe the complete stem, every option, command word, marks, facts and requested
   deliverable.
2. Confirm every referenced attachment is present and legible. A missing or cut-off
   attachment is an input gap; do not substitute another document.
3. Namespace inputs:
   - `exam_question:*`
   - `exam_attachment:*`
   - `course_manual:*`
   - `course_appendix:*`
4. An examination Appendix 1 is never course Appendix 1. Apply the same separation to
   every same-number or same-name attachment.

## 2. Source precedence

Apply this fixed order:

1. question instructions and examination attachments determine facts and requested output;
2. applicable mandatory legislation in the permitted materials;
3. the trust's actual instrument or the foundation's actual constitution;
4. course-manual explanation and footnotes; and
5. course precedent and appendix examples.

A lower source cannot silently displace a higher source. Record conflicts and their
effect. If an outcome-changing conflict cannot be resolved internally, preserve
separate conditional branches or state a materials gap.

## 3. Mode and unit split

Set mode: `MCQ`, `PROSE` or `DRAFTING`.

- MCQ: split the stem and every option into independent claims.
- Prose/drafting: split every sub-part by command word, marks, facts and deliverables.
- Never classify the whole question from its first or most obvious label.

Each answer unit records `subpart_ref`, `command_word`, `marks`,
`requested_deliverables` and `polarity`. An MCQ also records `selected_option` and
`closest_options`; non-MCQs leave option-selection fields inapplicable. Advice about an
existing statement, letter or memorandum of wishes is `PROSE` unless the requested
deliverable is a new or revised document.

## 4. Fact and Claim Disposition Ledger

Create one row for every material fact and, for an MCQ, every option claim.

| Item | Capacity/status | Possible legal effect | Source needed | Final disposition |
|---|---|---|---|---|

Allowed dispositions:

- `used - outcome`
- `used - content`
- `supported`
- `refuted`
- `partly true but not best`
- `condition`
- `not outcome-changing`
- `input gap`
- `materials gap`
- `materials do not resolve`

No fact or option may remain orphaned.

Record each row in `facts` or `claims` with one scalar `disposition`. For an MCQ,
`answer_unit.mcq_options` and the `mcq_option` claims must be bijective.

## 5. Mandatory Trust classifications

Populate all eight required arrays. Each entry records its state, value, deciding fact
IDs and any isolated alternatives; an unknown or disputed value remains conditional or
a gap rather than being silently selected.

1. `jurisdiction_factors`: classify separately the proper law, forum, place of
   administration, relevant party connecting factors, asset situs, transferor's place
   of incorporation and foundation registration jurisdiction, but only as applicable to
   the issue.
2. `trust_architecture`: vehicle and architecture, including conventional trust,
   reserved-powers trust, life-interest trust, purpose trust, Cayman STAR trust or
   foundation, plus any dispositive, administrative or governance structure that
   changes the route.
3. `actor_capacities`: every actor in each legally relevant capacity, including when a
   company acts as trustee, settlor, protector, enforcer, founder or council member.
4. `power_characteristics`: identify the power holder and whether the power is a duty
   or discretion, and dispositive, administrative or enforcement in nature; separately
   record direction, consent, veto, approval, revocation or other operative character.
5. `relationships`: classify both sides of each legal relationship rather than relying
   on role labels alone.
6. `lifecycle_stages`: current, prerequisite, requested and later implementation stages.
7. `governing_instruments`: applicable legislation, trust instrument, foundation
   charter, regulations/by-laws and actor authority instruments.
8. `standing`: identify who may request, decide, consent, enforce, challenge, receive or
   seek a remedy, and on what supplied basis.

Do not collapse jurisdiction into one label. Proper law does not by itself establish the
forum, administration place, asset law, transferor-capacity law or foundation registry.
A trustee, protector or beneficiary address, asset location, registry or counterparty
does not establish another jurisdictional factor without an issue-specific rule and
fact. If choice is genuinely delegated, choose only from the course-supported factors,
actual-instrument fit, complete document chain and fewest materials gaps; an unresolved
tie stays conditional.

Any exact trustee, protector, councillor, enforcer or corporate-director count is a
separate entity assertion and needs its own supplied fact; do not infer the board
composition of a trust company or other corporate actor from its role.

## 6. Additive candidate-source union

Use `Content.md` once to retrieve all routes triggered by:

- every sub-part or option;
- every outcome-changing fact;
- each legal relationship and actor;
- each requested document or consequence; and
- each plausible interpretation of an ambiguous fact.

Do not stop after the first topic match. Classify every candidate as mandatory,
conditional or forbidden only after both retrieval passes below.

Before lifecycle expansion, classify each possible contribution by deliverable scope:

- `requested output` - must appear in the answer or requested instrument;
- `necessary companion` - mention or perform it only where the answer would otherwise
  be legally or procedurally incomplete; or
- `background/check only` - verify privately and exclude from the submitted answer.

Carry that scope on every route, together with its `relationship_set_ids`; one route
may participate in more than one relationship set.

A preceding trustee, protector or corporate step is not automatically part of a document
that the question asks the candidate to draft. A simpler neighbouring precedent is not
a companion to a selected complex precedent unless it contributes a unique requested
component.

## 7. Independent second pass

Ignore the first-pass labels and reconstruct the problem independently.

### 7.1 Legal-relationship pass

List each relationship and the capacities on both sides: settlor/trustee,
trustee/beneficiary, trustee/protector, trustee/investment manager or delegate,
enforcer/purpose trust, founder/foundation/councillor/guardian/beneficiary,
transferor/transferee, debtor/creditor or other relationship supported by the facts.

### 7.2 Transaction-lifecycle pass

Give every stage a verdict: `triggered`, `not triggered`, `conditional` or `gap`.

1. instructions and due diligence;
2. status, capacity, eligibility and consent;
3. power, decision-maker and authority;
4. direction, consent, veto or prior approval;
5. trustee, council or corporate-board meeting/written-decision procedure;
6. deed, resolution, memorandum, attachment and execution;
7. transfer of title, delivery, funding and implementation;
8. trust records, minutes, accounts, releases and receipts;
9. external notices, filings, registration and time limits; and
10. enforcement, remedies, distribution, resettlement, revocation or termination.

A route found only here is a first-pass map miss and must be added.

## 8. Route relationship sets and conditional isolation

Represent alternatives separately:

`IF condition -> THEN rule/actor/stage/document -> OPEN sources -> EXCLUDE conflicting branch`

Never merge jurisdictions, regimes, trust types, actors, stages or precedents. Select a
branch only when the deciding fact is supplied. A desired end state is not proof of the
intermediate trustee, protector, settlor, beneficiary or council decision that produces
it.

Give each related group an ID, add it to every participating route's
`relationship_set_ids`, and classify the relationship from the actual governing
instrument and requested act:

- `XOR`: mutually exclusive jurisdictions, actors, powers, precedents or completion
  methods. An unresolved set has no selected route; a selected set has exactly one route
  and an outcome-supporting deciding fact.
- `AND prerequisite`: every listed authority, consent, capacity, decision or instrument
  must exist before the target act can be validly completed.
- `SEQUENCE`: routes occur in order, such as decision, deed, transfer, receipt and
  record; an earlier step is not automatically part of the requested deliverable.
- `OPTIONAL overlay`: activate only on its stated fact, such as a protector consent,
  underlying company, foreign asset, release, filing or tax consequence.

Do not infer a relationship type from neighbouring appendix titles. A positive direction
and a negative consent or veto may be XOR alternatives, prerequisites or separate
stages depending on the instrument. Keep unresolved conditions isolated.

## 9. Mandatory, conditional and forbidden routes

### Mandatory

A source is mandatory only if it supplies a unique rule, authority, procedure,
distinction, document component or consequence needed to answer.
In the RoutePlan, a final mandatory route has `requirement: mandatory` and
`verdict: incorporated`. Every conditional, forbidden or checked-not-relevant candidate
remains `requirement: optional` until the relevance gate selects it.

### Conditional

State the exact activating fact. Do not incorporate the route without it.

### Forbidden

Forbid plausible contamination routes, including:

- wrong jurisdiction/regime/trust type/entity;
- correct topic but wrong actor, relationship or stage;
- examination/course appendix collision;
- precedent with conflicting operative assumptions;
- outside law used to fill a gap;
- KAP or past answer during blind answering; and
- related background that cannot change the answer or confidence.

## 10. Hard relevance gate

Default to discard. Incorporate a source only if all are answered:

1. Which fact, option or requested dimension triggers it?
2. What unique contribution does it add?
3. What answer letter, confidence, sentence, calculation or document component changes
   without it?
4. Does it match every applicable Trust classification?
5. Is it proportionate to the polarity/marks/deliverable?

For an MCQ, a second source is incorporated only if it can change the answer letter or
confidence. Mentioning a document or resolution in an option does not activate Section B
drafting.

## 11. Exact source-passage verification

Before using a proposition:

1. open the exact module section, footnote, clause or appendix passage;
2. record its heading and filename;
3. verify the proposition, actor, condition, exception and stage against the text;
4. distinguish a citation-only footnote from reproduced mandatory wording; and
5. reject memory, index titles and neighbouring doctrine as proof.

Run a removal test: if deleting a mandatory source leaves the answer unchanged, either
the source is irrelevant or its unique contribution is missing from the answer.

The frozen allowlist and actual-open ledger are independent of `Sources used`. A
forbidden source or prior answer remains prohibited even if described as check-only or
omitted from the displayed source line.

## 12. Requested-document chain and component reconciliation

Run this section only when the answer unit requests an operative document. Start from
the requested legal act, not from the first precedent title found.

Build one row for every legally distinct instrument:

| Sequence | Instrument owner/actor | Own authority instrument | Target act/document | Decision method | Signatory | Operative parts | Attachments/exhibits | Execution | Records/filings |
|---|---|---|---|---|---|---|---|---|---|

Rules:

1. A corporate trustee's decision must be expressed through the corporate decision
   method and human signatories used by the selected course precedent. The directors'
   resolution of a corporate trustee may itself be the authority for the trust act; do
   not invent a duplicate upstream instrument. A corporate settlor, protector,
   beneficiary, founder or other distinct actor needs its own upstream authority only
   where the facts and course materials support that requirement. An unspecified
   “authorised signatory” is never a substitute for an authority instrument that the
   route has identified as required.
2. Derive the instrument count independently from every actor, power, consent or veto,
   transaction stage and requested deliverable. Do not let one trustees' resolution or
   deed absorb a distinct actor's decision.
3. For a deed or resolution that implements a dispositive or administrative decision,
   include every applicable operative clause or resolution in the selected precedent.
   A prior trustee decision is `necessary companion/check` unless the question also asks
   to draft it. Derive the operative count from the exact precedent, not the broad label
   in the question. If an operative part depends on a missing fact, retain it as an
   expressly bracketed/conditional item or disclose the omission in the route dossier;
   never reduce the expected count without a source-based reason.
4. For a multi-document trust transaction, identify each distinct trustee resolution,
   deed, direction, consent, appointment, statement of wishes, release, receipt,
   schedule and other exhibit supported by the facts. Do not hide an independently
   required instrument inside a generic collective noun.
5. Select the closest precedent by trust type, actor, power, lifecycle stage,
   transaction complexity and component architecture. A simpler precedent is forbidden
   once a selected precedent uniquely supplies required definitions, recitals,
   schedules, execution or amendment machinery.
6. Count expected and produced instruments, operative parts, attachments and execution
   blocks. Reconcile every mismatch before writing; a gap stays an explicit placeholder
   rather than disappearing.
7. Classify precedent fitness as complete, incomplete, defective or attachment-dependent.
   An incomplete or defective precedent is not authority to reconstruct omitted wording.
   A referenced but unsupplied deed, schedule, agreement, conveyance or execution block
   remains a distinct gap, even when the surrounding precedent is usable.

The validator computes these counts from included instruments, components, attachments,
execution blocks and records/filings. A direction to update records later is not an
actual minute, account, release, receipt, registration or filing entry.

The section adapter renders only the selected instruments. Sources opened as rejected
comparators or check-only companions are not reproduced.

## 13. Materials-gap handling

Use one outcome:

- `answerable`
- `answerable with placeholders`
- `conditional answer`
- `partial course coverage`
- `materials do not resolve`

State exactly what is missing, what sources were checked, what remains answerable and
what must stay blank or conditional. Assign `render` only where the sourced answer or
instrument is complete, `render_with_placeholders` where identified gaps can safely
remain explicit, and `do_not_render` where missing input or source material prevents a
responsible substantive output. `VALID` by itself does not select a render decision.
Never invent statute, section, instrument clause, form, filing rule or precedent.

## 14. Final route trace

Keep a private trace and expose its result in the section output:

| Route | Source/passage | Contribution | Verdict | Answer location |
|---|---|---|---|---|

Record incorporated, checked-not-relevant, conditional, forbidden and gap routes.
Routing completes only when all facts/claims have dispositions, all required
classification arrays are populated, both passes reconcile, exact passages are verified,
every requested deliverable has a source or explicit gap and the render decision matches
those gaps.

Each mandatory incorporated route must have exactly one trace entry whose contribution
matches that route's unique contribution and identifies the planned answer location.
Append `RoutePlan validation: VALID`, the render decision, plan ID and validator's
canonical plan hash to the adapter check trace. This line is evidence of the gate, not
part of the submitted answer.
