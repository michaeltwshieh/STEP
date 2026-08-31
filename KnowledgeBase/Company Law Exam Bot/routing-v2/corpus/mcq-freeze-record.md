# Section A Synthetic Corpus Freeze Record

- Frozen: 2026-08-30, before any baseline or candidate answer run.
- Scope: 20 synthetic MCQs in 10 one-fact minimal pairs.
- Gold fields: correct letter, governing proposition, must-open, conditional,
  must-not-open, option dispositions, closest-two distinction, exact course-source
  rationale and expected confidence.
- Answer balance: {'A': 5, 'B': 5, 'C': 5, 'D': 5}.
- Official status: synthetic regression only. No official Section A holdout is present;
  passing this corpus must not be described as real-exam accuracy.
- Gold SHA-256: `b3e5f2a07ba732bc231b06b58df0e39a5fda7b977bca1a47323e81d01047b807`
- Question-only fixture SHA-256: `2fdbc426e31d9d924d5f131033946537ab30d67c0a857de318eb93147d096be1`

The question-only fixture contains no gold fields and is the sole question input for
blind answer agents. The gold file is released only to the independent evaluator after
all answer files are locked.
