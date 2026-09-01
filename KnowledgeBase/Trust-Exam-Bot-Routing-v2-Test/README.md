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

A clean distribution contains no self-assessment answers, gold answers, KAP, past
answers, peer answers or prior behavioural outputs. A development workspace may retain
local `answers/`, `evaluation/`, `routing-v2/artifacts/` and `tmp/` trees; they are never
permitted by the default distribution check.

The `route-plan-v2` Trust-native RoutePlan records issue-specific jurisdiction factors, vehicle and
trust architecture, actor capacities, power characteristics, relationships, lifecycle,
governing instruments and standing. Related routes use XOR, AND-prerequisite, SEQUENCE
or OPTIONAL-overlay sets, and structural validation is followed by an explicit
`render`, `render_with_placeholders` or `do_not_render` decision.

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
python3 -m unittest discover -s routing-v2/tests -p 'test_*.py' -v
```

The default package check is the clean-distribution gate. Its expected result is `PASS`,
with 11 modules, 37 appendices, all Content registry paths resolved and both source and
workflow hashes matching `SOURCE-MANIFEST.json`. In a development workspace that
intentionally retains the four local artifact trees, run:

```sh
python3 routing-v2/scripts/check_package.py --allow-development-artifacts
```

That flag permits only those named trees; it does not suppress any other unexpected-file,
hash, symlink or integrity failure.

Routing v2 remains a test candidate. This folder is deliberately separate so testing it
does not activate or alter the live exam workflow.
