# Trust Exam Bot - Routing v2 Test Package

This is a self-contained test copy of the STEP Advanced Certificate in Trusts - Law and
Practice (International) exam bot. It includes the deterministic Routing v2 workflow and
its complete local course-material set. It does not depend on the parent bot folder for
legal sources or instructions.

## Included

- standalone `AGENTS.md` and `CLAUDE.md`;
- Routing v2 `Content.md`, `routing-core.md`, `section-a.md` and `section-b.md`;
- RoutePlan schema, validator and filesystem isolation harness under `routing-v2/`;
- all 11 course manuals;
- all 37 appendices;
- `submission-checklist.md`; and
- `SOURCE-MANIFEST.json` plus `routing-v2/scripts/check_package.py` for integrity checks.

No self-assessment answers, gold answers, KAP, past answers, peer answers or prior
behavioural outputs are included in the package.

## Test it in another Codex session

Open **this folder itself** as the workspace. A first message can simply be:

> Read `AGENTS.md` and `CLAUDE.md`, use this folder as the self-contained Routing v2
> Trusts test bot, and answer the following question: [paste the question or attach the
> screenshot].

Do not point the test session back to the parent bot folder.

## Verify the package

From this folder, run:

```sh
python3 routing-v2/scripts/check_package.py
```

The expected result is `PASS`, with 11 modules, 37 appendices, all Content registry
paths resolved and every immutable source hash matching `SOURCE-MANIFEST.json`.

Routing v2 remains a test candidate. This folder is deliberately separate so testing it
does not activate or alter the live exam workflow.
