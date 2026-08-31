# Frozen routing corpus

`cases.json` is the pre-implementation gold routing corpus. It is frozen before
`routing-prompt.md` is authored or used by a candidate agent.

Every case records:

- the task and changed fact, where it belongs to a minimal pair;
- jurisdiction, regime, entity, actor, transaction-stage and governing-articles locks;
- mandatory (`must_open`), conditional and forbidden (`must_not_open`) routes;
- the expected course-appendix/document chain;
- a disposition for every material fact;
- any course-material gap or source conflict; and
- the source-precedence rationale and unresolved branches.

The corpus deliberately contains 23 cases: all five Specimen Paper 1 questions plus
nine two-case minimal-pair sets. The same-name examination Appendix 1 is always in the
`exam_attachment` namespace and is never treated as course Appendix 1A, 1B or 1C.

After the hash in `freeze-record.md` is recorded, a gold expectation must not be edited
to make a candidate output pass. If a course source proves an expectation wrong, record
the old value, new value, exact source pinpoint and reason in `gold-amendments.md`, then
issue a new corpus version and rerun every case.
