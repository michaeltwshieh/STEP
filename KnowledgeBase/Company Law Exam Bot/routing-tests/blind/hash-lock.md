# Blind output hash lock

Locked: 2026-08-30 (Asia/Hong_Kong), before the Independent Evaluator Agent was
spawned or given access to any answer.

| Lane | File | Words | SHA-256 |
|---|---|---:|---|
| Baseline specimen | `baseline/specimen-answers.md` | 6,282 | `67a7c625c911ff4a6d495f9ff9f72ec11bfefc66952182e81d3e243a0b30c503` |
| Candidate A specimen | `candidate-a/specimen-answers.md` | 9,269 | `958a325fd3899f1f97f9c076be748a3684dc156b9c8af01ec083c446ba242783` |
| Candidate B specimen | `candidate-b/specimen-answers.md` | 8,208 | `b7daf243e4613f3ad83df1e60166e04fb7c9af668d350cb4370419b0e88ad74a` |
| Candidate A synthetic replay | `candidate-a/synthetic-routing.md` | 6,439 | `aab4ee1355a8fc26f5d30e6534f01c0f07037099e57a28ae2c84a58fb387e626` |
| Candidate B synthetic replay | `candidate-b/synthetic-routing.md` | 5,283 | `150be61b021ae1321fc23ed9aae9b22861594c53e0bb73856e419f5a613d1bf5` |

All five files contain their expected start and end markers. The three specimen lanes
and two replay lanes were fresh-context GPT-5.6 Sol / high reasoning agents. Each
attested that it remained read-only and did not search, list or open its forbidden
KAP, gold, prior-answer or peer-output paths.

The answer agents were not shown this manifest. Any later repair round writes to a new
round directory and never overwrites these locked round-0 outputs.
