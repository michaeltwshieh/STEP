# Deterministic routing tests

Run from the workspace root:

```sh
python3 -m unittest discover -s routing-v2/tests -p 'test_*.py'
```

The validator tests cover every named clean/failing RoutePlan fixture and stable exit
codes.  The isolation tests prove the answer tree contains no gold/KAP/prior answer,
that an intentional external read is blocked and recorded, and that evaluator inputs
cannot be built until all answer hashes are locked.
