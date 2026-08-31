# Repair Round 2 - Independent Section B Evaluation

## Scope and hash gate

Inputs were limited to the round-2 full Section B archives, the full-suite hash
lock, the corrected Section B oracle/freeze, the specimen question and KAP, the
candidate workflow, Syllabus and the permitted course manuals/appendices. No
Section A material, old evaluation/report, past answer, peer output or external
source was used.

Hash verification: PASS.

- `routing-v2/rounds/round2/full/section-b/candidate-a.md`: `d94dba8c8c98ad36f4c995471cf3d9670bfe84fd915643114de3fd75b53af172`
- `routing-v2/rounds/round2/full/section-b/candidate-b.md`: `4bbe87f5c7f38a1be8165cbcfe0789eff70c017e167eca01a398fd7df5f87ab0`
- specimen question: `07d07ec52ed17dc4d0fe360d297ba8c88d9c48fae9f27c2da7b94cbf68b198a6`
- KAP: `cc9fc7ce0e0b77dae24d1758f9e7ccab7a790a520436e425162bccd9d5659350`
- corrected oracle: `4f3adcda45c483864296a027d692d1f132903d1e3e08b0eb534380f5696ae8e9`
- candidate workflow (`Content.md`, `routing-core.md`, `section-b.md`, `CLAUDE.md`): all match the workflow hashes recorded by the full pretest.

### Count basis

For S01 the round-2 repair record expressly fixes the action-specific Appendix
30B count at five operative resolutions. The actual appendix contains five
(Appendix-30B, lines 20-24). The KAP displays the minimum core (winding-up,
liquidator appointment and audit waiver), all of which must be present. The
additional remuneration and in-specie clauses are source-supported Appendix 30B
operatives and are counted for this repair gate. Appendix 25A is check-only: it is
the upstream board-convening companion, not part of the requested notice, as the
oracle freeze records.

## Twenty-three critical routes

`PASS` means the route is materially present and correctly scoped. `PARTIAL`
means the answer has the right direction but omits an oracle component or leaves
the required rule too general. `FAIL` means a material wrong or omission remains.

| # | Critical route | Candidate A | Candidate B | Evidence |
|---:|---|:---:|:---:|---|
| 1 | S01 notice recipients, contents, service methods and 14-clear-day calculation | PASS | PASS | A lines 7-42; B lines 7-45. Both identify C/D/E and A/B, email/personal/post, 13 August service and 9 August posting. |
| 2 | S01 original quorum, director-convened adjournment and later quorum | PASS | PASS | A lines 50-56; B lines 47-55. Both correctly reject C alone on 28 August and explain the article 12.3 adjournment route. |
| 3 | S01 show-of-hands, poll demand and 70/30 poll result | PASS | PASS | A lines 58-62; B lines 56-57. Both apply articles 12.6-12.8 and 13.1 and the article 1 two-thirds threshold. |
| 4 | S01 requested notice plus complete action-specific 30B business; 25A check-only | PASS | **FAIL** | A lines 7-34 reproduces all five 30B operatives and no 25A. B lines 7-22 includes only winding-up and its own panel wrongly calls the expected count 1; it omits liquidator appointment and audit waiver. This is a full-suite regression from the focused 5/5 result in `routing-v2/rounds/round2/round-record.md`. |
| 5 | S02 article 19.3 $1m threshold and prior member sanction for $5m | PASS | PASS | A lines 70-74; B lines 64-68. |
| 6 | S02 separate member/board written decisions, including member approval of acquisition | PARTIAL | PARTIAL | Both produce separate member and sole-director instruments, but each member resolution sanctions borrowing/mortgage for the acquisition without expressly approving the aircraft purchase itself, an expected chain component. A lines 99-108; B lines 97-118. |
| 7 | S02 legal actors, Mr AB instruction and corporate nominee/director authority stages | PASS | PARTIAL | A records the written instruction and both upstream corporate boards (lines 70-76, 84-125). B has both upstream boards, but describes only the Relationship Manager message/arrangement and never clearly requires Mr AB's written instruction (lines 64-70, 82-135). |
| 8 | S02 complex 25N architecture, distinct transaction documents and exhibits | PARTIAL | PASS | A uses a 25N-like definitions/notes/resolutions structure but collapses distinct instruments into collective `Purchase Documents`/`Registration Documents`, supplies no attachment set and does not expressly execute the Bill of Sale as a deed (lines 132-168). B separately defines and attaches A-E, including facility, purchase agreement, Bill of Sale/conveyance, mortgage and Registry Transfer Pack (lines 142-202). |
| 9 | S02 execution, closing, charge register and external-filing gap | PASS | PASS | A lines 78-80 and 162-166; B lines 72-76 and 174-184. Both distinguish internal charge record from aviation/public filing. A's BVI section 162 is supported by Module 3 footnote 60. |
| 10 | S02 jurisdiction/regime lock | PASS | PASS | A fixes BVI throughout Q2. B fixes Bahamas and expressly leaves domestic/IBC identity as a materials gap without mixing regimes. The delegated choice permits either course-supported selection. |
| 11 | S03 historical separation plus Module 7 organ allocation | PASS | PASS | A lines 176-186; B lines 206-219. Both cover capital, expertise, liquidity/transferability, limited liability, continuity and the board/member split. |
| 12 | S03 article 19.1 residual management power and no ad hoc binding member instruction | PASS | PASS | A lines 188-193; B lines 221-229. Both apply the 1948 Article 80 approach and Quin & Axtens. |
| 13 | S03 trustee/company property distinction and directors' continuing duties | PASS | PASS | A lines 195-207; B lines 231-240. Both keep the Midcity account/worldwide assets in Company, preserve trustee/member influence and reject a nominee-director defence. |
| 14 | S03 ordinary-resolution removal/replacement and jurisdiction lock | PASS | PASS | A lines 208-209; B lines 237-240. Both apply articles 15.3-15.4, consent, retirement timing and records/filing consequences. |
| 15 | S04 fiduciary, conflicts, profits/benefits, care, delegation and supervision | PASS | PASS | A lines 212-230; B lines 244-258. Both use course-supported named authorities and practical safeguards. |
| 16 | S04 remedies, proper-plaintiff rule and ratification limits | PARTIAL | PARTIAL | Both discuss internal exposure and non-ratifiable fraud, and A mentions set-aside/account consequences, but neither states the Module 8 section 4 proper-plaintiff rule or cites Foss v Harbottle. The KAP expressly expects that route. |
| 17 | S04 approval, article/DSA exoneration, management-agreement indemnity and insurance | PASS | PASS | A lines 220 and 230-232; B lines 248 and 260. Both state disclosure/ratification limits and fraud/dishonesty/wilful-default exclusions. |
| 18 | S04 fraudulent/wrongful trading, Module 12 response options and jurisdiction isolation | PARTIAL | PARTIAL | Both identify fraudulent/wrongful trading and advise stopping further debt, but neither clearly gives the KAP's operational alternatives: convene the board, cease trading and voluntarily wind up, or, if viable, propose a creditor compromise. A names creditor arrangement/receivership/liquidation (line 230); B says only rescue or winding-up (line 256). |
| 19 | S05 insolvency selects creditors' voluntary winding-up and excludes solvency declaration | PASS | PASS | A lines 238-248; B lines 266-276. |
| 20 | S05 fixed-charge, liquidation-cost, preferential-tax and unsecured waterfall | PASS | PASS | A lines 242-248 and 280-310; B lines 270-276 and 306-350. Both calculate the $700,000 mortgage shortfall, $40,000 costs and $55,000 preference before pari passu claims. |
| 21 | S05 promissory-note shareholder loan treated as ordinary unsecured debt | PASS | PASS | A lines 242, 288-310; B lines 319, 334-350. |
| 22 | S05 Appendix 30G structure and all account components | PARTIAL | PASS | A adapts 30G but inserts a non-precedent secured-realisation memorandum and omits Blackacre from the receipts/payments schedule (lines 268-294). B preserves the 30G headings and five realisation rows, with the creditor adaptation disclosed (lines 280-320). |
| 23 | S05 arithmetic total $2,605,000, 50% dividend and nil balance/return | **FAIL** | PASS | A's account totals only $905,000 because the $1,700,000 secured realisation is outside its tables, despite the separate memo; this does not meet the oracle/KAP account total of $2,605,000 (lines 270-310). B receipts and payments each total $2,605,000, ordinary claims total $1,620,000, distribution is $810,000 and balance is nil (lines 298-358). |

### Route totals

- Candidate A: 17 PASS, 5 PARTIAL, 1 FAIL. Strict critical-route gate: FAIL.
- Candidate B: 19 PASS, 3 PARTIAL, 1 FAIL. Strict critical-route gate: FAIL.

Candidate B is stronger on the Q2 exhibit chain and Q5 account. Candidate A is
stronger on the repaired S01 notice count. Neither reaches the required all-route
standard.

## Additional audit dimensions

### Wrong lock, stage or precedent

- No wrong jurisdiction is established. A consistently selects BVI in Q2, Q3 and
  Q5; B consistently selects Bahamas in those questions. Each question permits a
  delegated choice. B's unresolved domestic/IBC identity is properly marked as a
  gap rather than silently mixed with BVI rules.
- S01 is correctly scoped away from Appendix 25A in both submitted blocks. A's
  check panel explicitly marks 25A check-not-relevant. B does not reproduce it.
- A's Q2 25N choice is the correct complexity direction but the draft under-produces
  its document/exhibit architecture. B's Q2 25N-shaped draft is materially complete.
- A's Q5 secured-realisation memorandum is a stage/presentation deviation from the
  requested 30G account and causes the total mismatch. B's presentation follows the
  KAP schedule.

### Forbidden contamination and authority

No prohibited Section A, old-evaluation, past-answer, peer-output or external-law
material appears in either candidate's source/trace panels. The BVI section 162
charge-register citation in A is supported by the permitted Module 3 footnote 60,
so it is not an invented authority. Candidate B's `Bishopsgate ... (No.2)` label is
a minor citation-variant: the course passage names the case without that suffix;
the proposition and case are otherwise the supplied one.

### Material facts, requested documents and branches

- Both candidates correctly preserve the supplied names, figures, holdings, aircraft
  tail number, lender, registry transfer and insolvency figures. Placeholders are
  used for missing dates, names, forms and filing deadlines.
- A's Q1 notice has the full five-clause Appendix 30B package, while B's one-clause
  notice silently drops triggered operative business. Both correctly keep the
  board-convening resolution out of the requested notice.
- A and B both keep seal/deed execution, aviation-registration formalities and
  jurisdiction-specific filings conditional. B's Q2 five exhibits are explicit;
  A's collective definitions do not satisfy the distinct-exhibit requirement.
- Both identify the S01 short-notice and members/creditors uncertainty in their
  checks. Neither improperly treats the absent solvency fact as proved. Both Q5
  correctly select CVL once insolvency is supplied.

### A/B agreement

Agreement is strong on all S01 prose routes, S03, the main fiduciary/care routes in
S04 and the S05 insolvency waterfall. The material divergences are:

1. B's full-rerun S01 notice regresses to one resolution after the focused 5/5
   repair, whereas A retains all five.
2. B separately supplies the five Q2 exhibits; A hides them in collective
   definitions and omits the Bill of Sale deed step.
3. B's Q5 account totals $2.605m in the tables; A totals only the $905k free pool.
4. Both omit Foss/proper-plaintiff and leave the Module 12 operational response
   route too general.

### Regression lanes

The only directly testable focused-to-full regression is Candidate B S01, recorded
above. The corrected oracle's additional P05B, P08A and P08B lanes have no answer
artifacts in the round-2 full Section B archive. They are therefore UNTESTED, not
credited as passes or converted into invented failures. In particular, no claim can
be made from these files about the P05B approval/refusal XOR, the P08A 30E/30F XOR,
or P08B creditor-specific precedent gaps.

## Final verdict

Hash gate: PASS. Substantive full Section B gate: FAIL for both candidates.

- Candidate A's decisive defects are the Q2 missing distinct attachments/Bill of
  Sale execution and the Q5 account total/presentation mismatch, with Q4 remedies
  and insolvency-response gaps.
- Candidate B's decisive defect is the S01 full-rerun regression to a one-resolution
  notice, with the same Q4 omissions and a smaller Q2 instruction/member-approval
  gap.
