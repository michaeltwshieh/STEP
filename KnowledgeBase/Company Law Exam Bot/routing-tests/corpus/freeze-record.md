# Corpus freeze record

Frozen: 2026-08-30 (Asia/Hong_Kong), before creation of `routing-prompt.md`.

## Locked hashes

| Artifact | SHA-256 |
|---|---|
| `routing-tests/corpus/cases.json` | `7a0010d184925ad20ff12f61a60ba059e4a4e68fd6cee102c2694fedf37abed9` |
| question text extract | `07d07ec52ed17dc4d0fe360d297ba8c88d9c48fae9f27c2da7b94cbf68b198a6` |
| KAP text extract | `cc9fc7ce0e0b77dae24d1758f9e7ccab7a790a520436e425162bccd9d5659350` |
| question-only synthetic fixture | `59c3d1038de547444651bf7d9a09a7cf97b631fa75ba7146f8ca4c7fbfcb5c0a` |

The source PDFs themselves are locked in `routing-tests/baseline/baseline-record.md`.

## Freeze checks

- 23 cases present: five Specimen Paper 1 questions and 18 synthetic cases.
- Nine minimal-pair groups present; every group contains exactly two cases.
- Every case has locks, must-open, conditional, must-not-open, document-chain,
  mandatory-critical-route, fact-disposition, materials-gap, source-precedence and
  unresolved-branch fields.
- All case IDs are unique.
- All 52 concrete Markdown source filenames named in the corpus resolve.
- Same-number examination appendices are namespaced as `exam_attachment:*`.
- `routing-prompt.md` did not exist when this hash was recorded.
- The 18-case question-only fixture was derived mechanically after freeze and contains
  only ID, pair group, title, question and task-type hint. It exposes no gold route.

## Independent pre-freeze evidence

Fresh-context read-only source auditors independently derived the five specimen routes
without access to the KAP, existing answers, `content-test.md`, candidate artifacts or
other agents' work. A separate read-only auditor proposed eight minimal-pair sets from
course sources alone. The main agent checked the cited course passages and the rendered
question/KAP pages before freezing the corpus.

The source audit corrected one draft arithmetic error before freeze: Q5 has $810,000
available to $1,620,000 of ordinary unsecured claims, producing a 50 percent dividend.
The official KAP's individual payments independently reconcile to the same $810,000.
Because the corpus had not yet been frozen, this is not a post-freeze gold amendment.
