# Shared Routing Core

Run this algorithm for every MCQ, prose sub-part and drafting sub-part before entering
the section adapter. `Content.md` is the only legal source map. This file contains no
topic-to-source mapping and does not state law.

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
4. An examination Appendix 1 is never course Appendix 1A, 1B or 1C. Apply the same
   separation to every same-number or same-name attachment.

## 2. Source precedence

Apply this fixed order:

1. question instructions and examination attachments determine facts and requested output;
2. applicable mandatory legislation in the permitted materials;
3. the company's actual memorandum and articles;
4. course-manual explanation and footnotes; and
5. course model articles and appendix examples.

A lower source cannot silently displace a higher source. Record conflicts and their
effect. If an outcome-changing conflict cannot be resolved internally, preserve
separate conditional branches or state a materials gap.

## 3. Mode and unit split

Set mode: `MCQ`, `PROSE` or `DRAFTING`.

- MCQ: split the stem and every option into independent claims.
- Prose/drafting: split every sub-part by command word, marks, facts and deliverables.
- Never classify the whole question from its first or most obvious label.

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

## 5. Six locks

Lock or expressly mark unknown:

1. jurisdiction;
2. regime/entity type;
3. legal actor/capacity;
4. transaction/legal relationship;
5. current and requested lifecycle stage; and
6. governing legislation, memorandum and articles.

Jurisdiction has exactly three states:

- `supplied`: apply it and exclude other regimes;
- `choice delegated`: choose once using complete course coverage, actual-article fit,
  document-chain completeness and fewest gaps; break a true tie alphabetically; or
- `genuinely unknown`: do not choose; isolate supported alternatives.

A lender address, asset location, registry or counterparty is not the company's
jurisdiction without an express fact.

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

A preceding corporate step is not automatically part of a document that the question
asks the candidate to draft. A simpler neighbouring precedent is not a companion to a
selected complex precedent unless it contributes a unique requested component.

## 7. Independent second pass

Ignore the first-pass labels and reconstruct the problem independently.

### 7.1 Legal-relationship pass

List each relationship and the capacities on both sides: company/member, board/director,
registered/beneficial owner, transferor/transferee, principal/agent, debtor/secured
creditor, company/liquidator, or other relationship supported by the facts.

### 7.2 Transaction-lifecycle pass

Give every stage a verdict: `triggered`, `not triggered`, `conditional` or `gap`.

1. instructions and due diligence;
2. status, capacity, eligibility and consent;
3. decision-maker and authority;
4. recommendation or prior approval;
5. meeting/written-decision procedure;
6. document, attachment and execution;
7. delivery/closing/implementation;
8. internal registers, certificates, minutes and accounts;
9. external notices, filings, registration and time limits; and
10. enforcement, remedies, distribution, final account or dissolution.

A route found only here is a first-pass map miss and must be added.

## 8. Conditional branch isolation

Represent alternatives separately:

`IF condition -> THEN rule/actor/stage/document -> OPEN sources -> EXCLUDE conflicting branch`

Never merge jurisdictions, regimes, actors, stages or precedents. Select a branch only
when the deciding fact is supplied. A desired end state is not proof of the intermediate
board/member decision that produces it.

Record mutually exclusive routes as XOR sets. In particular, an approval document and
its refusal/notice alternative, or two alternative completion methods, cannot be made
cumulative merely because each appears in the source map.

## 9. Mandatory, conditional and forbidden routes

### Mandatory

A source is mandatory only if it supplies a unique rule, authority, procedure,
distinction, document component or consequence needed to answer.

### Conditional

State the exact activating fact. Do not incorporate the route without it.

### Forbidden

Forbid plausible contamination routes, including:

- wrong jurisdiction/regime/entity;
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
4. Does it match every lock?
5. Is it proportionate to the polarity/marks/deliverable?

For an MCQ, a second source is incorporated only if it can change the answer letter or
confidence. Mentioning a document or resolution in an option does not activate Section B
drafting.

## 11. Exact source-passage verification

Before using a proposition:

1. open the exact module section, footnote, article or appendix passage;
2. record its heading and filename;
3. verify the proposition, actor, condition, exception and stage against the text;
4. distinguish a citation-only footnote from reproduced mandatory wording; and
5. reject memory, index titles and neighbouring doctrine as proof.

Run a removal test: if deleting a mandatory source leaves the answer unchanged, either
the source is irrelevant or its unique contribution is missing from the answer.

## 12. Materials-gap handling

Use one outcome:

- `answerable`
- `answerable with placeholders`
- `conditional answer`
- `partial course coverage`
- `materials do not resolve`

State exactly what is missing, what sources were checked, what remains answerable and
what must stay blank or conditional. Never invent statute, section, article, form,
filing rule or precedent.

## 13. Final route trace

Keep a private trace and expose its result in the section output:

| Route | Source/passage | Contribution | Verdict | Answer location |
|---|---|---|---|---|

Record incorporated, checked-not-relevant, conditional, forbidden and gap routes.
Routing completes only when all facts/claims have dispositions, all locks are fixed or
unknown, both passes reconcile, exact passages are verified and every requested
deliverable has a source or explicit gap.
