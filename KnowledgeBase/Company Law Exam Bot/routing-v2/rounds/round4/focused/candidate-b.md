# MCQ17 - Candidate B

## Frozen pre-open access plan

Frozen before opening any substantive course manual or appendix, from the MCQ17
fixture and `routing-v2/candidate/Content.md` only.

| Option | Route label | Access decision | Planned source(s) / reason |
|---|---|---|---|
| A | Voluntary striking off; Appendices 31A + 31B/31C | DO NOT OPEN | Content's striking-off row says to verify no remaining business, proceedings, assets or liabilities and to compare with voluntary winding-up where assets or liabilities remain. The supplied facts activate that exclusion. The option's distractor appendices are not self-authorising. |
| B | Administrative reinstatement; Appendix 31D | DO NOT OPEN | Reinstatement is a return-to-register lifecycle route, not an initiation route to terminate a live solvent company. The option's distractor appendix is not self-authorising. |
| C | Members' voluntary winding-up; Appendices 30A/30B and later chain | OPEN | `Course-Manual-Module-12-Termination-of-Companies.md`, §3.1 for solvent liquidation and the declaration/appointment route; `Appendix-30A-Directors-declaration-of-solvency.md` and `Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md` for the initiating documents. |
| D | Compulsory winding-up solely because members no longer want the company | DO NOT OPEN | Content routes compulsory winding-up to §2.1-2.4 (inability to pay / just-and-equitable grounds), while the facts support the solvent members' route. No distractor appendix is needed. |

**Plan status:** FROZEN. No file outside the planned `OPEN` set may be accessed as
substantive evidence. In particular, Appendices 31A, 31B, 31C and 31D are hard
prohibitions for this run.

## Input transcription and routing

**Fixture:** `routing-v2/corpus/mcq-20-questions.json`, item `MCQ17`.

**Stem:** A solvent company has assets to realise and liabilities to pay before
surplus can be returned to members. Which route may properly be initiated to
terminate it?

**Polarity:** correct; the qualifier is “may”.

**Options:**

- **A:** Voluntary striking off under Appendix 31A plus the jurisdictionally applicable Appendix 31B or 31C.
- **B:** Administrative reinstatement under Appendix 31D.
- **C:** Members' voluntary winding-up beginning with Appendices 30A and 30B and continuing through the applicable notices/final-account chain.
- **D:** Compulsory winding-up solely because the members no longer want the company.

## Exact-open ledger

| Accessed substantive file | Frozen decision | Exact passage used | Ledger result |
|---|---|---|---|
| `Course-Manual-Module-12-Termination-of-Companies.md` | OPEN | §§2.1-2.2 (compulsory winding-up grounds/procedure); §§3.1.1-3.1.2 (members' voluntary winding-up, solvency declaration, special resolution, liquidator and completion); §§6.2-6.3 (zero-state striking-off and reinstatement) | permitted and incorporated |
| `Appendix-30A-Directors-declaration-of-solvency.md` | OPEN | Director's declaration: full enquiry; ability to pay debts in full within 12 months; attached assets/liabilities statement | permitted and incorporated |
| `Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md` | OPEN | Member special resolutions: voluntary winding-up; liquidator appointment; related liquidation powers/records | permitted and incorporated |

**Exact-open attestation:** I accessed exactly the three substantive files listed in
the ledger, all of which were frozen `OPEN` before retrieval. I did not open
Appendices 31A, 31B, 31C or 31D, or any other distractor appendix. The fixture and
candidate workflow files were input/instruction files, not substantive legal
evidence. The ledger reconciles with the frozen substantive `OPEN` set: no
unplanned substantive file was accessed.

## Shared routing checks

**Locks:** jurisdiction genuinely unknown; offshore/common-law company regime is
not specified; the company is the legal actor, with directors making the solvency
declaration, members initiating the voluntary winding-up resolution, and a
liquidator conducting the later liquidation; transaction is solvent termination;
current stage is before commencement and requested stage is the proper initiating
route; the local statute/articles are not supplied, so the course's typical model
and jurisdictionally applicable later notices are kept conditional.

**Legal-relationship pass:** company/member (members decide whether the company is
no longer required and receive any surplus after debts); directors/company
(solvency declaration); liquidator/company and creditors/company (asset realisation
and payment of liabilities after commencement).

**Transaction-lifecycle pass:** status/solvency/eligibility triggered; decision-maker
and authority triggered; declaration and member decision triggered; meeting or
written-resolution procedure triggered; 30A/30B instruments triggered; liquidator
implementation, notices/filings, final account and dissolution are later stages,
not prerequisites to identify the initiating route. Reinstatement is not triggered.

**Fact and claim dispositions:** the supplied solvency fact supports a solvent
liquidation; remaining assets and liabilities refute a zero-state striking-off;
there is no prior removal to activate reinstatement; members' preference alone is
not a stated compulsory-winding-up ground; the requested result is termination,
not a document draft.

## MCQ17 answer

**Answer:** C - Members' voluntary winding-up beginning with Appendices 30A and
30B and continuing through the applicable notices/final-account chain.

**Polarity:** correct. “May properly be initiated” asks for an available opening
route; it does not require that every later liquidation step has already occurred.

**Why:** Module 12 §3.1.1 describes the members' decision to end a company whose
assets, after its debts and liabilities are discharged, can be distributed to
shareholders. Under §3.1.2, the directors first make a declaration of solvency
with an assets/liabilities statement (Appendix 30A), then the members usually pass
a special resolution to wind up the company and appoint a liquidator (Appendix
30B). The liquidator then realises assets, pays creditors, prepares the final
account and proceeds toward dissolution. That sequence fits a solvent company
with assets and liabilities still outstanding.

**Option A:** refuted - Module 12 §6.2 limits voluntary striking-off eligibility
to the statutory “zero state,” including no assets and no debts, liabilities or
outstanding claims. The facts expressly leave assets and liabilities to deal with
before a surplus can be returned.

**Option B:** refuted - Module 12 §6.3 treats administrative reinstatement as an
application to restore a company that has already been removed from the register;
the stem describes a live company at the start of termination, not a removed one.

**Option C:** supported - the solvent members' voluntary-winding-up route begins
with the solvency declaration and members' winding-up/liquidator resolution, then
uses the applicable notice, account and dissolution stages under Module 12 §3.1.2.

**Option D:** refuted - Module 12 §§2.1-2.2 describe compulsory winding-up as a
court-imposed route requiring a statutory ground, such as inability to pay debts
or a just-and-equitable case. Members simply no longer wanting the company is the
voluntary route described in §3.1.1, not a standalone compulsory ground.

**Closest two:** A and C - both are voluntary termination routes, but the supplied
assets/liabilities fact defeats striking-off's zero-state condition and selects
members' voluntary winding-up.

**Sources used:** `Course-Manual-Module-12-Termination-of-Companies.md`,
§§2.1-2.2, 3.1.1-3.1.2 and 6.2-6.3; `Appendix-30A-Directors-declaration-of-solvency.md`;
`Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md`.

**Cross-check:** Module 10 §§2-4 (meeting/written-resolution procedure) considered
but discarded: the fixture asks which termination route may be initiated, and
Module 12 §3.1 itself supplies the decision sequence; the overlay cannot change
the answer letter. No other source changes the route.

**Confidence:** high (9/10). Exact Module 12 passages and the two initiating
precedents determine C; the only qualification is that the jurisdiction and local
statutory variants are not supplied, which the option itself preserves through
“applicable” later stages.

## Completion

- [x] Stem and polarity transcribed exactly.
- [x] Every option independently routed and given a verdict.
- [x] Jurisdiction, actor, stage, qualifier and exception checked per option.
- [x] Exact governing passage located for the chosen letter and closest distractor.
- [x] Closest-two distinction stated.
- [x] One letter committed with sources, cross-check and honest confidence.
- [x] No Section B drafting workflow activated by appendix terminology.
- [x] Frozen pre-open allowlist and exact-open attestation reconcile.
