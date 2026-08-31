# Round 4 final Section B evaluation

Scope: S01-S05 only. The 23 critical routes are the four S01 routes, five S02 routes, five S03 routes, four S04 routes and five S05 routes in `section-b-oracle-v2.json`. P = full route, P* = route present but with a material completeness/lock defect, F = route not safely satisfied. No Section A output, prior answer, report or external source was used. The hash-lock note about Candidate B's Section A contamination is outside this evaluation scope.

## Hash verification

All locked Section B inputs match.

| object | expected / actual SHA-256 prefix | result |
|---|---|---|
| Section B Candidate A | `e1ef04a8cbbb4d8da32a0a8910ea8ac19cb207ac704aa6b9098ed01f1766149d` | PASS |
| Section B Candidate B | `53448e9762b87b3d34b76ab6342093400fe18d49dfc72b986939de6dafbfa953` | PASS |
| corrected Section B oracle | `4f3adcda45c483864296a027d692d1f132903d1e3e08b0eb534380f5696ae8e9` | PASS |
| specimen question extract | `07d07ec52ed17dc4d0fe360d297ba8c88d9c48fae9f27c2da7b94cbf68b198a6` | PASS |
| routing core | `b3d52ff790e3f6aef979b185109fa87c435959efc7e1dee05df6899138fdf95e` | PASS |
| Section B adapter | `11f04bbb861eb55a6660cc09ca99d736b06b5c14ac42b394d59c658b72320014` | PASS |

The KAP hash observed is `cc9fc7ce0e0b77dae24d1758f9e7ccab7a790a520436e425162bccd9d5659350`.

## Critical-route score

Strict full-pass count, treating P* as non-full: Candidate A `20/23`; Candidate B `18/23`.

| case | Candidate A | Candidate B | material route evidence |
|---|---:|---:|---|
| S01 (4) | 3 P, 1 F | 4 P | A 1.1 contains only resolution 1 at lines 21-29 and wrongly makes the 30B additions conditional at lines 72-73. B contains the 30B core and two extra accurate 30B items at lines 17-29. |
| S02 (5) | 4 P, 1 F | 3 P, 1 P*, 1 F | Both satisfy art.19.3, the member/director stages and BVI choice. Both miss the distinct Bill of Sale and an actual Appendix 7C entry. B's upstream instruments also assume unsupported sole directors. |
| S03 (5) | 5 P | 4 P, 1 F | A states BVI before the answer at line 293. B starts 3.1 directly at line 205, then uses BVI law at lines 229-233, contrary to the question's required preliminary jurisdiction lock. |
| S04 (4) | 4 P | 3 P, 1 F | A includes the Foss/proper-plaintiff rule at line 402. B's prose omits it at lines 251-271, although its coverage box falsely claims Foss at lines 427-428. |
| S05 (5) | 4 P, 1 P* | 4 P, 1 P* | A's valid fixed-charge memorandum/free-estate adaptation totals $905,000 in the account (lines 475-497), not the KAP/oracle $2,605,000 receipts/payments schedule. B reproduces the expected total at lines 307-327, but applies a BVI lock to the Companies Act 1948 priority model without clearly isolating the BVI variation (lines 275-283). |

P* route-present defects are: A S05.5; B S02.3 and S05.2. If partial route presence is counted rather than strict completeness, the tallies are A `21/23` and B `20/23`.

## Candidate A

- S01.2-1.5 are materially correct: the C/D/E and A/B recipient treatment, 14-clear-day calculation (13 August effective service, 9 August posting), accidental-omission qualification, C-only quorum/adjournment and 70% poll are all present. The hard defect is S01.1: corrected oracle S01 requires the 25E notice plus 30B core voluntary-winding-up, liquidator appointment and no-audit business. A drafts only the first resolution.
- S02 uses a clean BVI lock and generic board authority for both corporate subsidiaries, which is safer than inventing their internal board composition. It correctly separates Mr AB, the nominee member, the corporate director and the human signatories. The requested-document chain is incomplete: its definitions at lines 200-208 omit the distinct Bill of Sale; lines 234-236 only direct a later charge-register entry and do not produce the Appendix 7C record. The prose also does not expressly obtain Mr AB's written instruction.
- S03 is the strongest prose answer: explicit BVI preamble, Article 19.1/Article 80 analysis, Quin & Axtens, separate corporate asset ownership, continuing director duties, nominee-control risks and Articles 15.3-15.4 removal/replacement are all covered.
- S04 includes the proper-plaintiff rule, remedies, ratification limits, fiduciary/care authorities, nominee risks, insolvency, exoneration, DSA, management-agreement and insurance protections. No material mandatory route is missing.
- S05 chooses Bermuda, making the 1948-model qualification reasonably consistent. The route, waterfall, shareholder-loan treatment and dividend arithmetic are correct. The account is a defensible Module 12 treatment of fixed-charge proceeds outside the liquidator's free estate, but it does not match the KAP/oracle requested combined 2,605,000 receipts and payments presentation. Treat as P*, not fabricated law.

## Candidate B

- S01 is materially better than A. It carries the required 30B core in the notice. Resolutions 4 and 5 are accurate 30B wording, extra to the oracle's minimum core but not forbidden contamination.
- S02 gets the high-level route right, but the two upstream headings at lines 87-107 and 135-155 say `sole director` for the nominee and directorship subsidiaries. The facts establish only that they are subsidiaries; they do not establish their own board composition. That is an actor-capacity lock error. Like A, B omits the distinct Bill of Sale and actual 7C register entry. Its five definitions at lines 165-173 are not a Bill of Sale, facility, mortgage, registry-document and charge-record chain.
- S03 has good substantive law but fails the explicit jurisdiction preamble requirement. This is a lock defect, not a source hallucination: BVI sections are used without first stating BVI for Question 3.
- S04 is otherwise broad and well sourced, but the body never says that the company is the proper plaintiff under Foss v Harbottle, that a shareholder resolution is needed, or that the fraud exception permits a derivative claim. The coverage line falsely ticks a point absent from the essay, and Foss is absent from the Authorities line. This is a direct coverage-check failure.
- S05's account matches KAP/oracle totals and all listed payments. The only material concern is the BVI choice followed by an unqualified 1948 priority model; the answer should state that the course supplies the model and that current BVI priority/account rules remain a gap.

## Locks, precedents, facts and forbidden material

Both candidates keep the examination Appendix 1 distinct from course Appendices 1A/1B/1C in S01-S03 and use only authorities appearing in the course materials. Neither contains a Section A reference, old answer/report, web source or outside law used to fill a gap. FAA/Isle of Man requirements are correctly left as materials gaps.

Material lock/precedent defects are A's S01 notice-scope decision, A's non-KAP S05 account presentation, B's unsupported sole-director assumptions, B's missing S03 jurisdiction preamble and B's missing Foss route. Both candidates omit the S02 Bill of Sale and actual 7C record. Both refer to C with an unprovided gender (`His` in A, `She` in B), a minor fact-precision defect. B's global Source line also names a non-existent `Course-Manual-Module-09-Other-Officers-and-Registered-Agent.md`; the actual course filename includes `Secretary`.

## Output/check-panel and branch assessment

Candidate A follows the per-question `SUBMIT THIS` and check-panel architecture. Its S01 check panel is substantively wrong because it labels required 30B operative business conditional. Candidate B uses one global submit/check structure rather than a separate check panel per question, has no explicit Q3 jurisdiction preamble and globally claims coverage for Foss that its body does not contain. Both appropriately preserve aviation, local filing, seal/deed and other genuine materials gaps. A isolates more branches cleanly; B handles S01 better but leaves the BVI/1948 S05 branch under-qualified.

Agreement is high on the underlying law and outcomes: both agree on S01 service/quorum/poll, S02 art.19.3 approval, S03 Article 19.1 and removal, S04 core director risks and S05 insolvency/waterfall. The decisive disagreements are drafting completeness and lock discipline. B supplies the required S01 notice core and KAP-style S05 account; A supplies the safer S02 corporate-actor lock, explicit S03 jurisdiction and complete S04 remedies route. Neither is submission-ready without repairing the listed gaps.

Recommended merge for any further repair: retain B's S01 notice and S05 combined account, retain A's generic upstream corporate-authority chain and S03/S04 prose, then add the S02 written-instruction stage, Bill of Sale, Appendix 7C entry, explicit jurisdiction/priority qualifications and the Foss paragraph.
