# RoutePlan contract

`route-plan.schema.json` is the machine-readable pre-answer routing contract. It carries
the answer unit, namespaces, typed facts, six locks, entities, route verdicts, frozen
source allowlist and actual-open ledger, XOR branches, requested-document chain,
materials gaps and final answer trace.

Validate a plan before an adapter renders anything:

```sh
python3 routing-v2/scripts/validate_route_plan.py route-plan.json \
  --output validation-report.json
```

Exit codes are stable: `0` means `VALID`, `1` means the RoutePlan is invalid, and `2`
means the input/schema/tool could not be read or parsed. Reports contain no timestamp or
absolute input path, so equal inputs produce byte-identical JSON.

The validator does not parse answer prose and contains no case-specific legal trigger.
Any failed critical invariant blocks rendering. A later adapter records the plan ID,
canonical plan hash and retained report reference only in its non-submitted check trace.
