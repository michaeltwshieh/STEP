# Pre-integration evidence summary

Status: prompt implemented for candidate testing; live exam instructions not yet
changed.

## Frozen inputs

- Baseline operational snapshot: six files, byte-for-byte hash matched.
- Specimen Paper 1 PDF: 19 pages, read-only, rendered and visually checked.
- Specimen Paper 1 KAP PDF: 12 pages, read-only, rendered and visually checked.
- Gold corpus: 23 cases, comprising five specimen questions and nine two-case
  minimal-pair sets.
- Question-only replay fixture: 18 cases with no gold fields.

## Corpus coverage

- drafting/prose hybrids;
- facts without legal labels;
- same-number examination/course appendix namespace isolation;
- supplied, delegated and genuinely unknown jurisdiction states;
- regime, actor, transaction and lifecycle-stage changes;
- conditional branch isolation;
- materials and precedent gaps;
- multi-module substance/procedure/records/document/consequence routes; and
- arithmetic and final-account drafting.

## Independent source audits

Fresh-context auditors, barred from the KAP and existing answers, independently routed
Specimen Questions 1-5 and proposed minimal pairs. The main agent checked the cited
module and appendix passages before freezing the corpus.

One arithmetic error was caught before freeze: Q5 has $810,000 for ordinary creditors
against $1,620,000 of ordinary claims. The resulting 50 percent dividend reconciles
the six individual payments and the $2,605,000 final total.

## Static audit

`routing-tests/scripts/check_routing.py` passed before integration:

- 12 modules and 90 appendices;
- unique, continuous module numbers and unique appendix labels;
- complete bijective `Content.md` index;
- complete `content-test.md` module and appendix inventory;
- frozen baseline, corpus and source-extract hashes;
- 23 complete cases and nine complete minimal pairs;
- all concrete case-source filenames resolved;
- question-only fixture contains no gold fields;
- all required routing-prompt mechanisms present;
- all prohibited specimen-specific prompt triggers absent;
- Markdown table widths consistent;
- local Markdown links resolved;
- no duplicate headings in new/operational artifacts; and
- no modified course manual or appendix.

`git diff --check` also passed, and both new Python scripts parsed and executed.

## Retained source warnings

The following are pre-existing course-source defects and were not edited:

- source-of-truth Markdown contains redundant or intentionally repeated headings;
- Appendix 6A mentions an absent Appendix 4A;
- Module 3 points to nonexistent Module 9 §1.3.2(viii), with the relevant material in
  Module 9 §1.4.2; and
- Module 5 points to nonexistent Module 9 §2.8, with the relevant material in Module
  10 §2.8.

The live `CLAUDE.md`, `Content.md` and `section-b.md` remain unchanged pending blind
comparison and the zero-critical-error gate.
