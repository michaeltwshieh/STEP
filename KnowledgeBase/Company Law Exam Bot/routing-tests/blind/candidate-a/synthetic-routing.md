# Synthetic Candidate A

## Boundary attestation / file-open ledger

- **Workspace boundary:** Worked only in `/Users/michaelshieh/Desktop/Claude Projects/STEP Exam/KnowledgeBase/Company Law Exam Bot`.
- **State:** Strictly read-only. No files created, edited, deleted, renamed or hashed. No subagents used.
- **Blindness:** No forbidden path was searched, listed or opened. No gold, KAP, past-answer, baseline, blind-output, report or other-agent material was consulted.
- **Routing/control files opened:** `CLAUDE.md`; `Content.md`; `routing-prompt.md`; `section-b.md`; `content-test.md`; `routing-tests/corpus/question-fixtures.json`.
- **Manual files opened:** Modules 3, 4, 5, 6, 8, 9, 10, 11 and 12.
- **Appendices opened:** 4, 7A, 7B, 7D, 9, 10A, 10B, 10C, 12, 16D, 18A, 18B, 18C, 18D, 18E, 19A, 19B, 20E, 24A, 24C, 25A, 25B, 25E, 26, 27A, 27B and 30A-30G.
- **Not opened because unnecessary:** `Syllabus.md`, Modules 1, 2 and 7, and every appendix not listed above.

## P01A — Traditional final dividend

**TASK_TYPE:** Hybrid: explain procedure plus draft two precedent resolutions.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown; no jurisdiction-specific mandatory rule may be added.
2. **Regime:** Supplied traditional/Table A final-dividend division.
3. **Actors:** AB Ltd; board recommending; members declaring; secretary/administrator paying.
4. **Transaction:** $100,000 final dividend from $120,000 distributable profits.
5. **Stage:** Accounts review → board recommendation → member declaration → payment/records.
6. **Governing document:** Actual articles described but text absent; traditional course articles are analogous course models.

**FACT_DISPOSITIONS:** `$120,000 distributable profits = used-outcome` because the proposed amount is covered; `$100,000 = used-content/outcome`; `final dividend = used-outcome` because it triggers two organs; `actual traditional articles = used-outcome`; shareholder count, shareholdings, record date, financial year and payment date = input gaps/placeholders.

**MUST_OPEN:**

- Module 6 §§6.1-6.2: distributable-profits restriction and traditional two-resolution power.
- Module 10 §5.7: chronological procedure and payment implementation.
- Appendix 19A: board recommendation, comprising financial-statements note, one recommendation resolution and execution block.
- Appendix 19B: recital of board recommendation, one member declaration resolution and execution block.

**CONDITIONAL:**

- IF the actual articles instead confer final-dividend power on directors alone → OPEN Appendix 19C → EXCLUDE 19A+19B. The stated facts negate this branch.
- IF solvency, capital impairment or creditor prejudice is disputed → OPEN Module 8 §2.2 and Module 12 §§2-4.

**MUST_NOT_OPEN/USE:**

- Appendix 19C: wrong decision-maker under the supplied articles.
- Appendix 20E and Module 10 §5.8: BVI/IBC solvency-distribution regime, not traditional declaration.
- Module 12: no insolvency fact.

**DOCUMENT_CHAIN:** Financial/accounts evidence → Appendix 19A board recommendation → Appendix 19B members’ declaration, not exceeding recommendation → payment instruction and accounting/minute records.

**MATERIALS_GAPS:** Exact article number, member/share particulars, year end, record date and payment date are absent. Jurisdiction-specific filing requirements cannot be stated.

**UNRESOLVED_BRANCHES:** None on decision-maker; factual placeholders remain.

**SEVEN_LAYER_CLOSURE:** Substantive rule `incorporate`; constitution/capacity `incorporate actual traditional division`; procedure `incorporate`; duties/liability `checked-not-relevant absent impropriety`; records/filings `incorporate internal payment/accounts, external filing unknown`; documents `incorporate 19A+19B`; consequences/remedies `incorporate prohibition on exceeding profits/recommendation`.

**CONCLUSION:** Route the $100,000 final dividend through Appendix 19A followed by Appendix 19B; neither 19C nor 20E belongs in the selected branch.

## P01B — BVI BC solvency distribution

**TASK_TYPE:** Hybrid: explain BVI distribution procedure and draft the board-only instrument.

**SIX_LOCKS:**

1. **Jurisdiction:** Supplied BVI.
2. **Regime:** BVI Business Company under BVI BCA distribution rules.
3. **Actors:** AB Ltd; directors authorising; administrator making payment.
4. **Transaction:** $100,000 statutory distribution, despite the question’s colloquial “final dividend”.
5. **Stage:** Solvency review → director authorisation → payment → records.
6. **Governing document:** BVI legislation and actual articles mentioned but absent; course extract of BVI BCA ss.56-57 supplied in Module 6.

**FACT_DISPOSITIONS:** `$120,000 distributable profits = not independently outcome-changing` because BVI solvency, not traditional profits alone, controls; `$100,000 = used-content/outcome`; `BVI BC = used-outcome`; `directors may authorise subject to solvency = used-outcome`; asset/liability values and debt-payment evidence = input gaps.

**MUST_OPEN:**

- Module 6 §7.3, including BVI BCA ss.56-57: balance-sheet and cash-flow limbs, board power and mandatory resolution statement.
- Module 10 §5.8: board review, authorisation and payment implementation.
- Appendix 20E: one financial-review note, solvency declaration with two limbs, two operative resolutions and execution block.

**CONDITIONAL:**

- IF the payment causes or approaches insolvency → OPEN Module 8 §§2.2, 6 and Module 12 §§2-4.
- IF the actual BVI articles impose additional restrictions → incorporate them above the precedent.

**MUST_NOT_OPEN/USE:**

- Appendices 19A+19B: wrong traditional member-declaration regime.
- Appendix 19C: “declare dividend” terminology and precedent assumptions do not replace BVI authorisation/solvency wording.
- Module 6 §6 except as checked contrast: traditional capital-maintenance route displaced.

**DOCUMENT_CHAIN:** Current accounts and solvency evidence → Appendix 20E board resolution containing both solvency limbs → administrator’s bank transfer → accounting/minute records.

**MATERIALS_GAPS:** The $120,000 profit figure does not prove that assets exceed liabilities or that debts remain payable as due after the $100,000 transfer. Actual articles, shareholder/payment details and dates are absent.

**UNRESOLVED_BRANCHES:** Whether solvency can factually be certified remains unresolved; no rival legal regime remains.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution/capacity `incorporate subject to absent actual articles`; procedure `incorporate`; duties/liability `conditional if solvency judgment is defective`; records/filings `incorporate internal payment/accounting only`; documents `incorporate 20E`; consequences/remedies `conditional insolvency/director exposure`.

**CONCLUSION:** Use the board-only Appendix 20E route, but do not certify the BVI solvency test from distributable-profit figures alone.

## P02A — Board accepts voluntary share transfer

**TASK_TYPE:** Drafting with short records-stage explanation.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Private-company voluntary inter vivos transfer; actual articles absent.
3. **Actors:** Transferor, transferee, AB Ltd board, secretary/administrator.
4. **Transaction:** Registration of a voluntary legal-title transfer.
5. **Stage:** Executed instrument/certificate/fee already delivered → board approval → registration/certificate/records.
6. **Governing document:** Actual articles mentioned implicitly but absent.

**FACT_DISPOSITIONS:** Executed transfer form, old certificate and fee `used-outcome` because delivery prerequisites are complete; board decision to register `used-outcome`; party identities, share class/number, consideration and article number `input gaps`.

**MUST_OPEN:**

- Module 6 §5.1 stages 2-5: transfer, board approval and registration consequences.
- Module 10 §5.3: corporate procedure and beneficial/legal-title distinction.
- Appendix 18A: already-executed transaction instrument and its two signatures.
- Appendix 18B: two recitals, transfer table, three resolutions and execution block.
- Module 3 §§4.1.3, 4.1.5 plus Appendices 7A and 7D: legal-holder and conditional beneficial-owner records.
- Appendix 16D: replacement certificate structure.

**CONDITIONAL:**

- IF pre-emption rights exist → verify compliance/waiver before approval.
- IF beneficial ownership also changes → update Appendix 7D and applicable authority records.
- IF local law requires a Registrar return → make it after registration.

**MUST_NOT_OPEN/USE:**

- Appendices 18C+18D: refusal branch conflicts with the board’s decision.
- Appendix 18E: transmission by death, not voluntary transfer.
- Appendices 26-27: beneficial-only route where registered title remains unchanged.

**DOCUMENT_CHAIN:** Existing Appendix 18A and old certificate → Appendix 18B approval → register of members update → old certificate cancellation → Appendix 16D new certificate → beneficial-owner/Registrar updates if triggered.

**MATERIALS_GAPS:** Actual articles, pre-emption status, identities, share particulars, consideration, dates and local filing rule are absent. Module 10’s “transferee’s certificate” wording conflicts with Module 6/18B’s coherent old transferor-certificate route; follow the latter subject to actual records.

**UNRESOLVED_BRANCHES:** Beneficial-owner and Registrar updates depend on facts/local law.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `materials gap actual articles`; procedure `incorporate`; duties `checked-not-relevant absent improper motive`; records `incorporate/conditional`; documents `incorporate 18A, 18B, 16D and record templates`; consequences `incorporate registration as title stage`.

**CONCLUSION:** Approve through Appendix 18B and complete registration, cancellation and replacement-certificate records; the refusal and transmission precedents are excluded.

## P02B — Board refuses voluntary share transfer

**TASK_TYPE:** Drafting with notification-stage explanation.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Voluntary transfer subject to board refusal power.
3. **Actors:** Transferor, proposed transferee, board and company signatory giving notice.
4. **Transaction:** Refusal to register legal-title transfer.
5. **Stage:** Instrument delivered → board refusal → notice and return of lodged documents.
6. **Governing document:** Actual articles absent; Appendix article references conflict internally with Module 6.

**FACT_DISPOSITIONS:** Executed form/certificate/fee `used-outcome`; refusal decision `used-outcome`; reason, article, time limit and party/share particulars `input/materials gaps`.

**MUST_OPEN:**

- Module 6 §5.1 stage 4: refusal, notice, timing and reasons-law comparison.
- Module 10 §5.3: transfer procedure checked up to board stage.
- Appendix 18A: lodged input instrument.
- Appendix 18C: two recitals, transfer table, refusal resolution, optional reasons and execution.
- Appendix 18D: addressee, refusal notice, table, reasons, document-return recital and signature.

**CONDITIONAL:**

- IF governing law follows the older course position → reasons may not be mandatory.
- IF it follows a reasons-required rule or reasons are strategically given → insert accurate, non-frivolous reasons.
- IF actual articles set a notification period → obey that period; Module 6 gives the traditional two-month model.

**MUST_NOT_OPEN/USE:**

- Appendix 18B: approval branch.
- Appendix 16D and register-entry route: no new member/certificate on refusal.
- Appendix 18E: wrong transaction.
- Appendices 26-27: wrong ownership stage.

**DOCUMENT_CHAIN:** Existing 18A/certificate → Appendix 18C refusal resolution → Appendix 18D notice to proposed transferee within the governing period → return form and certificate → retain refusal minutes/correspondence.

**MATERIALS_GAPS:** Appendices 18C/18D cite art.8.2, while Module 6 routes board approval/refusal to art.8.3 and notice to art.8.5. Actual articles must resolve this. Reasons and applicable reasons requirement are absent.

**UNRESOLVED_BRANCHES:** Reasons-required versus reasons-optional; exact article and notice deadline.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `materials gap`; procedure `incorporate conditionally`; duties `conditional if refusal is improper/conflicted`; records `incorporate refusal file, no register change`; documents `incorporate 18C+18D`; consequences `incorporate non-registration/challenge risk`.

**CONCLUSION:** The selected chain is Appendix 18C followed by Appendix 18D, but article references, deadline and reasons cannot be completed without the actual governing materials.

## P03A — Registered holder alive; voluntary transfer

**TASK_TYPE:** Draft the complete voluntary-transfer chain.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Voluntary inter vivos transfer.
3. **Actors:** Jordan as registered transferor; Morgan as transferee; board; records officer.
4. **Transaction:** Jordan voluntarily transfers one share to Morgan.
5. **Stage:** Agreement → transfer instrument → delivery/approval → registration/certificate.
6. **Governing document:** Actual articles unknown.

**FACT_DISPOSITIONS:** Jordan alive `used-outcome`; Jordan sole registered holder of one share `used-content/outcome`; Jordan’s agreement `used-outcome`; Morgan seeking registration `used-content/outcome`; consideration/date/addresses/share denomination/certificate number `input gaps`.

**MUST_OPEN:**

- Module 6 §5.1 and Module 10 §5.3.
- Appendix 18A: Jordan/Morgan transfer form.
- Appendix 18B: board approval and records resolutions.
- Appendix 7A and Module 3 §4.1.3: register update.
- Appendix 16D: new certificate.

**CONDITIONAL:**

- IF pre-emption restrictions exist → comply with or waive them before delivery/approval.
- IF beneficial ownership records change → Appendix 7D.
- IF local law requires a return or stamp duty → comply; course coverage is jurisdiction-dependent.

**MUST_NOT_OPEN/USE:**

- Appendix 18E: Jordan is alive, so transmission is excluded.
- Appendices 18C+18D: company is willing to register.
- Appendices 26-27: legal title changes.

**DOCUMENT_CHAIN:** Appendix 18A signed by Jordan and Morgan → old certificate and any fee delivered → Appendix 18B → Appendix 7A update ending Jordan’s holding and entering Morgan → old certificate cancelled → Appendix 16D issued to Morgan → conditional BO/Registrar update.

**MATERIALS_GAPS:** Actual articles, pre-emption facts, consideration, addresses, dates, denomination and certificate particulars.

**UNRESOLVED_BRANCHES:** Pre-emption and external filing only.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `materials gap`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate`; documents `incorporate`; consequences `incorporate registration passes legal title`.

**CONCLUSION:** Jordan must use the voluntary Appendix 18A/18B route, followed by register and certificate work; Appendix 18E is categorically wrong.

## P03B — Registered holder deceased; transmission

**TASK_TYPE:** Draft the transmission request and identify its evidential/records chain.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Transmission on death.
3. **Actors:** Jordan deceased; Morgan as duly appointed personal representative; company records officer.
4. **Transaction:** Morgan elects to become registered in place of Jordan by operation of law.
5. **Stage:** Proof of death/authority → request → registration and certificate replacement.
6. **Governing document:** Actual articles unknown; course model art.8.7 is analogous only.

**FACT_DISPOSITIONS:** Jordan’s death `used-outcome`; Morgan’s personal-representative capacity `used-outcome`; sole share `used-content`; Morgan seeks own registration `used-outcome`; actual death certificate/probate and details `input gaps`.

**MUST_OPEN:**

- Module 6 §5.2: transmission, evidential attachments, election and records.
- Module 10 §5.3 only for the distinction and records mechanics.
- Appendix 18E: definitions, request, probate/certificate attachments and PR execution.
- Appendix 7A and Appendix 16D: register and replacement certificate.

**CONDITIONAL:**

- IF Morgan instead directs registration of an heir → Morgan signs Appendix 18A as personal representative; that alternative excludes Morgan’s own 18E registration.
- IF beneficial-owner records change → Appendix 7D.

**MUST_NOT_OPEN/USE:**

- Appendix 18B as an ordinary voluntary-transfer approval: transmission request does not depend on Jordan’s signature or an inter vivos sale.
- Appendices 18C+18D: no refusal fact.
- Appendices 26-27: nominee/beneficial-only transaction absent.

**DOCUMENT_CHAIN:** Jordan’s death certificate + grant of probate → Appendix 18E request signed by Morgan → register of members updated → old certificate cancelled → Appendix 16D issued to Morgan → BO records if applicable.

**MATERIALS_GAPS:** Evidential documents are asserted by status but not supplied; article, addresses, certificate/share details and dates remain placeholders.

**UNRESOLVED_BRANCHES:** None unless Morgan elects the heir-transfer alternative.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `conditional on actual transmission article`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate`; documents `incorporate 18E plus evidence/certificate`; consequences `incorporate Morgan’s registration by transmission`.

**CONCLUSION:** Jordan’s death displaces the voluntary-transfer chain; Morgan should use Appendix 18E with probate evidence and complete the register/certificate stages.

## P04A — Registered-office move within jurisdiction

**TASK_TYPE:** Hybrid: explain the internal move and draft board approval.

**SIX_LOCKS:**

1. **Jurisdiction:** Existing jurisdiction acknowledged but unnamed.
2. **Regime:** Same-jurisdiction registered-office relocation.
3. **Actors:** Board; secretary/registered agent/administrator; Registrar.
4. **Transaction:** Move from 1 Harbour Road to 2 Harbour Road without changing domicile.
5. **Stage:** Board approval → Registrar notice → records/property/stakeholder implementation.
6. **Governing document:** Actual articles and local statute absent.

**FACT_DISPOSITIONS:** Both exact addresses `used-content`; same jurisdiction `used-outcome`; no entity/domicile change `used-outcome`.

**MUST_OPEN:**

- Module 5 §§2.2 and 3.2: nature of office, board power model and distinction from nationality.
- Module 10 §5.4: implementation steps.
- Appendix 12: two resolutions and sole-director execution block.

**CONDITIONAL:**

- IF the actual articles do not confer board power where local law requires them to do so → obtain the decision required by those higher sources.
- IF the jurisdiction has a prescribed form/deadline → file it; the manual gives a common 14-day model, not a universal rule.

**MUST_NOT_OPEN/USE:**

- Module 4 §2 and Appendices 10A-10C: no migration.
- Constitutional amendment precedents: the memorandum ordinarily states jurisdiction, not street address.
- Appendix 24A: officer appointment is unrelated.

**DOCUMENT_CHAIN:** Appendix 12 changing address to 2 Harbour Road and authorising notification → prescribed Registrar notice/letter and fee → move statutory registers/seal as required → update stationery/nameplate → notify banks and other interested parties.

**MATERIALS_GAPS:** Jurisdiction, actual articles, prescribed form, fee and binding filing deadline are absent.

**UNRESOLVED_BRANCHES:** Board power and local filing mechanics.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `conditional`; procedure `incorporate`; duties `checked-not-relevant`; records/filings `incorporate with local gap`; documents `incorporate Appendix 12`; consequences `incorporate address/service update, no domicile change`.

**CONCLUSION:** Draft Appendix 12 for the Harbour Road move and complete local notification; the migration package must be excluded.

## P04B — Continuation into another jurisdiction

**TASK_TYPE:** Hybrid: explain continuation and draft the approval/supporting package.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown old and new jurisdictions.
2. **Regime:** Cross-border migration/continuation as the same entity.
3. **Actors:** Board, members, administrator, de-registration and continuation Registrars, director/deponent.
4. **Transaction:** Change of domicile, registered-office jurisdiction and governing law.
5. **Stage:** Eligibility/legal advice → board initiation → member approval → evidence/application → certificate of continuation.
6. **Governing document:** Old/new statutes and actual constitution mentioned only by implication; absent.

**FACT_DISPOSITIONS:** Different jurisdiction `used-outcome`; same legal entity `used-outcome`; addresses `not outcome-changing except evidence`; jurisdiction names, company status, solvency and good-standing evidence `input gaps`.

**MUST_OPEN:**

- Module 4 §§2.1-2.3: migration, eligibility, application contents and continuity.
- Module 5 §§2.2, 3.2: office/nationality distinction.
- Module 10 §§2-4: board/member and written-resolution mechanics.
- Appendix 10A: board note, migration resolution, optional new-articles branch, member-resolution attachment and implementation authority.
- Appendix 10B: member note and special-resolution limbs for departure and continuation.
- Appendix 10C: affidavit/declaration with corporate, good-standing, solvency, consent and legal-advice evidence.

**CONDITIONAL:**

- IF new articles are needed for destination compliance → activate Appendix 10A resolution 3 and attach them.
- IF destination or origin uses a different approval threshold/actor → higher mandatory law and actual articles displace Appendix 10B’s sample “special” formulation.
- IF migration out of BVI → add the course-noted member/creditor notice requirements.

**MUST_NOT_OPEN/USE:**

- Appendix 12: same-jurisdiction street-address move only.
- Module 4 §1: foreign-company registration without changing domicile.
- Winding-up/incorporation forms: continuation preserves the entity.

**DOCUMENT_CHAIN:** Origin/destination legal and good-standing evidence → Appendix 10A with AB2 member resolution and conditional AB1 new articles → Appendix 10B → Appendix 10C with exhibits → certified constitution/articles of continuation and solvency evidence → applications/de-registration → certificate of continuation.

**MATERIALS_GAPS:** Both jurisdictions, legislation, thresholds, company number/date, actual constitution, solvency, creditor/contract consents, exhibits and affidavit formalities are absent. Appendix 10B’s numbering is malformed and must be reconstructed without changing effect.

**UNRESOLVED_BRANCHES:** Destination eligibility, approval threshold, new-articles requirement and evidential form.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `conditional`; procedure `incorporate conditionally`; duties `checked-not-relevant absent evasion`; records/filings `incorporate with jurisdiction gaps`; documents `incorporate 10A-C`; consequences `incorporate continuity of property, debts, contracts and shares`.

**CONCLUSION:** Treat this as migration through Appendices 10A-10C, but a complete non-placeholder package is impossible until both jurisdictions and supporting evidence are supplied.

## P05A — Beneficial ownership changes; nominee remains

**TASK_TYPE:** Hybrid: distinguish beneficial from legal title and draft the nominee-chain documents.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Nominee-held shares; beneficial-only transfer.
3. **Actors:** Owner A outgoing beneficial owner/signatory; Owner B incoming beneficial owner/endorser; Nominee Ltd addressee and continuing registered holder.
4. **Transaction:** Transfer beneficial interest without legal-title transfer.
5. **Stage:** Instruction/endorsement → cancel old nominee instrument → new nominee instrument → BO/FATCA/CRS records.
6. **Governing document:** Existing nominee agreement/declaration mentioned but not supplied; actual articles/statute absent.

**FACT_DISPOSITIONS:** Nominee Ltd remains registered `used-outcome`; A-to-B beneficial transfer `used-outcome`; parties `used-content`; type of existing nominee instrument and local BO rules `input gaps`.

**MUST_OPEN:**

- Module 11 §2.5: nominee/beneficial relationship and instrument alternatives.
- Module 10 §5.3 beneficial-only paragraph.
- Module 3 §4.1.5 and Appendix 7D: BO records.
- Appendix 26: outgoing instruction, cancellation direction, incoming endorsement and consequential records.
- Appendix 27A: bilateral route with two recitals and four nominee obligations.
- Appendix 27B: inspect because it is the unilateral alternative, while recording incompleteness.

**CONDITIONAL:**

- IF the arrangement is bilateral → execute Appendix 27A between Nominee Ltd and Owner B → EXCLUDE 27B.
- IF unilateral declaration is required → Appendix 27B is the intended branch, but its missing operative wording is a materials gap.
- IF FATCA/CRS status/reporting changes → use only locally supported forms/rules; Appendix 26 directs updates but does not supply the forms.

**MUST_NOT_OPEN/USE:**

- Appendices 18A-18D: registered legal title does not move.
- Appendix 16D/register of members amendment: Nominee Ltd remains the certificate holder/member.
- Appendix 18E: no death.

**DOCUMENT_CHAIN:** Appendix 26 signed by Owner A and endorsed by Owner B → cancel/replace A’s nominee instrument → Appendix 27A or incomplete 27B in favour of B → Appendix 7D update → FATCA/CRS records as applicable; register of members remains unchanged.

**MATERIALS_GAPS:** The bilateral/unilateral choice is unstated. Appendix 27B says “etc., as above” and cannot yield a complete declaration. Existing instrument, BO particulars and local reporting forms are absent.

**UNRESOLVED_BRANCHES:** 27A versus 27B.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `checked-not-relevant to legal-title change`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate`; documents `conditional 26+27A/27B`; consequences `incorporate nominee remains legal holder`.

**CONCLUSION:** Use Appendix 26 and replace the nominee instrument while leaving the members’ register untouched; the precise 27A/27B branch remains unresolved.

## P05B — Legal title changes; nominee leaves register

**TASK_TYPE:** Hybrid: explain the legal-title consequence and draft the transfer/registration chain.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Nominee arrangement terminates and direct registered ownership follows.
3. **Actors:** Owner A as outgoing beneficial owner/instruction-giver; Nominee Ltd as registered legal transferor; Owner B as transferee/new member; board.
4. **Transaction:** Legal-title transfer from Nominee Ltd to Owner B.
5. **Stage:** Underlying A/B arrangement and nominee authority → legal transfer → board registration → registers/certificate.
6. **Governing document:** Existing nominee contract and actual articles absent.

**FACT_DISPOSITIONS:** Nominee leaves register `used-outcome`; Owner B must enter register `used-outcome`; Owner A transfers beneficial interest `used-outcome but does not make A legal transferor`; identities `used-content`.

**MUST_OPEN:**

- Module 11 §2.5: identify A’s beneficial capacity and Nominee Ltd’s legal title.
- Module 6 §5.1 and Module 10 §5.3: legal-title transfer.
- Appendix 18A: Nominee Ltd as transferor and Owner B as transferee.
- Appendix 18B: board approval.
- Appendices 7A, 7D and 16D: legal/beneficial records and new certificate.

**CONDITIONAL:**

- IF existing nominee agreement requires a separate instruction/release → follow that supplied contract; no exact compatible course form exists.
- IF pre-emption rights apply → comply/waive before registration.
- IF local BO/Registrar filings apply → update them.

**MUST_NOT_OPEN/USE:**

- Appendix 26 as the operative precedent: it assumes the nominee remains registered and directs execution of a new nominee declaration, which conflicts with the facts.
- Appendices 27A/27B: no continuing nominee arrangement for Owner B.
- Appendix 18E: no transmission.

**DOCUMENT_CHAIN:** Supported instruction/termination of A’s nominee arrangement → Appendix 18A signed by Nominee Ltd and Owner B → old certificate delivered → Appendix 18B → Appendix 7A removes Nominee Ltd and enters B → Appendix 7D replaces A with B as applicable → cancel old certificate → Appendix 16D to B.

**MATERIALS_GAPS:** No course precedent exactly documents Owner A’s beneficial sale plus direction to Nominee Ltd to transfer legal title directly to B. Existing nominee authority, consideration, share details, articles and filing law are absent.

**UNRESOLVED_BRANCHES:** Pre-emption and external filing; authority under the absent nominee contract.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `materials gap actual articles`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate`; documents `incorporate 18A/18B, gap for underlying instruction`; consequences `incorporate direct legal ownership by B`.

**CONCLUSION:** Nominee Ltd, not Owner A, must execute the legal transfer to Owner B through Appendices 18A and 18B; the continuing-nominee precedents are excluded.

## P06A — Contract signed before incorporation

**TASK_TYPE:** Hybrid: advise on liability/adoption and draft the adoption resolution.

**SIX_LOCKS:**

1. **Jurisdiction:** Supplied BVI.
2. **Regime:** BVI BC modern statutory pre-incorporation-contract regime.
3. **Actors:** Pre-incorporation signatory/promoter; later-incorporated company; later sole director; supplier.
4. **Transaction:** Ordinary written supply contract purportedly made for a nonexistent company.
5. **Stage:** Signature one day before incorporation → company comes into existence → board adoption now.
6. **Governing document:** BVI BCA s.104 identified in Module 3 footnote; statutory text and actual articles absent.

**FACT_DISPOSITIONS:** Pre-certificate timing `used-outcome`; later sole-director status `used-outcome for adoption actor, not retroactive capacity`; BVI `used-outcome`; supplier good faith `not outcome-changing for existence/adoption`; ordinary written contract `used-content for form`; actual contract/date/parties `input gaps`.

**MUST_OPEN:**

- Module 3 §§2.1-2.2 and footnote 35: common-law baseline, modern adoption route and BVI pinpoint.
- Module 3 §3.6: certificate marks corporate existence.
- Module 8 §§1.2 and 1.4: sole-director corporate decision and ordinary contract execution.
- Appendix 4: two factual notes, one adoption/release resolution and execution block.

**CONDITIONAL:**

- IF BVI s.104 has the promoter-release effect contemplated by the course discussion → adoption transfers liability to the company and ends personal liability.
- IF it does not release automatically → the company may become bound on adoption while promoter liability requires the statutory text or a novation/release.
- IF adoption is declined → company remains outside the pre-incorporation contract, subject to the governing statutory rule on the signatory.

**MUST_NOT_OPEN/USE:**

- Appendix 4 as proof by itself that every promoter is released: a precedent cannot supply missing mandatory-law effect.
- Pure common-law “company can never ratify” conclusion: BVI modern provision is specifically identified.
- Post-incorporation authority-only route: the signing date prevents it.

**DOCUMENT_CHAIN:** Original supply contract and certificate → Appendix 4 completed with true parties/dates/subject → company adoption → any separately required supplier/promoter release or novation only if BVI effect is not established.

**MATERIALS_GAPS:** The permitted manual identifies BVI s.104 but does not reproduce its exact effect on promoter liability. Contract particulars, incorporation date and article are absent.

**UNRESOLVED_BRANCHES:** Whether adoption automatically discharges the signatory cannot be decided from the reproduced BVI course text.

**SEVEN_LAYER_CLOSURE:** Substantive `partial course coverage`; constitution `conditional actual articles`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate adopted contract/resolution`; documents `incorporate Appendix 4`; consequences `materials gap on promoter discharge`.

**CONCLUSION:** The company should adopt through Appendix 4, but the precise post-adoption liability split requires the unreproduced effect of BVI BCA s.104.

## P06B — Contract signed after incorporation

**TASK_TYPE:** Prose advice; no drafting required on stated facts.

**SIX_LOCKS:**

1. **Jurisdiction:** Supplied BVI.
2. **Regime:** Existing BVI BC entering an ordinary corporate contract.
3. **Actors:** Company; duly appointed sole director; good-faith supplier.
4. **Transaction:** Post-incorporation written supply contract.
5. **Stage:** Incorporation and appointment complete → director signs → contract binding.
6. **Governing document:** BVI BCA ss.31, 103 and 107 course extracts/pinpoints; actual articles absent.

**FACT_DISPOSITIONS:** One day after certificate `used-outcome`; duly appointed sole director `used-outcome`; ordinary written supply contract `used-outcome`; supplier good faith `used-outcome/confirmatory`; no irregularity alleged `used-outcome`.

**MUST_OPEN:**

- Module 3 §§3.6-4: company exists and may contract after certification.
- Module 8 §§1.2-1.4 and footnotes 77-79: sole-director authority, BVI outsider protection, contract form and authentication.

**CONDITIONAL:**

- IF actual articles restrict this supply contract or internal approval was omitted → company remains externally protected on the supplied good-faith facts, but director liability/internal ratification may arise.
- IF the instrument was a deed or special transaction rather than an ordinary written supply contract → execution requirements would change.

**MUST_NOT_OPEN/USE:**

- Module 3 §2 pre-incorporation rules and Appendix 4: wrong temporal stage.
- Novation/adoption documents: no nonexistent principal at signing.
- General-meeting documents: no member approval trigger.

**DOCUMENT_CHAIN:** Existing contract signed by sole director → retain contract and execution evidence in corporate records. No new corporate instrument is required on stated facts.

**MATERIALS_GAPS:** Actual articles are absent, but no fact suggests a restriction material to external liability.

**UNRESOLVED_BRANCHES:** Internal restriction only if later proved by actual articles.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `conditional but non-dispositive externally`; procedure `incorporate`; duties `conditional only on hidden restriction`; records `incorporate`; documents `checked-not-relevant beyond existing contract`; consequences `incorporate company bound`.

**CONCLUSION:** AB Ltd is bound by its duly appointed sole director’s post-incorporation supply contract, and no adoption resolution should be drafted.

## P07A — Board originates general meeting

**TASK_TYPE:** Draft first convening resolution and identify subsequent notice.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** General meeting under supplied article powers.
3. **Actors:** Board as originator; secretary/administrator issuing notice; members voting.
4. **Transaction:** Convening a meeting to consider supplied resolution.
5. **Stage:** Board decision → notice → meeting/vote/minutes.
6. **Governing document:** Article powers described; actual article text absent.

**FACT_DISPOSITIONS:** Board-originated process `used-outcome`; proposed resolution/venue/date/time said to be supplied but omitted from fixture `input gap`; 15% requisition threshold `not outcome-changing in board branch`.

**MUST_OPEN:**

- Module 10 §§2.2.1, 2.2.5 and 2.3: board power, notice and agenda.
- Appendix 25A general-meeting alternative: two resolutions and execution block.
- Appendix 25E: recipients, meeting particulars, substantive resolution, execution and proxy note.

**CONDITIONAL:**

- IF notice is shorter than the actual article period → Appendix 25C consent to short notice.
- IF proxies/corporate representatives are requested → select 25F/25G or 25H/25J.
- IF a certified special resolution must be filed after passage → Appendix 25L.

**MUST_NOT_OPEN/USE:**

- Appendix 25B: members did not originate the process.
- Appendix 25D: AGM ordinary-business notice, not the stated specific resolution.
- Appendix 21D: unrelated director-appointment operative content.

**DOCUMENT_CHAIN:** Appendix 25A general-meeting branch → Appendix 25E notice setting out supplied resolution → conditional proxy documents → meeting/resolution/minutes → filing if required.

**MATERIALS_GAPS:** The fixture asserts but does not reproduce the resolution, venue, date or time. Notice period, resolution threshold and actual article are absent.

**UNRESOLVED_BRANCHES:** Short notice, proxy and filing requirements.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate meeting purpose`; constitution `conditional`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate minutes/conditional filing`; documents `incorporate 25A then 25E`; consequences `incorporate invalidity risk from defective notice`.

**CONCLUSION:** The first document is Appendix 25A’s general-meeting branch, followed by Appendix 25E notice.

## P07B — Qualifying members originate general meeting

**TASK_TYPE:** Draft member requisition and identify the immediate board/notice stages.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Article-based member requisition requiring the board to convene.
3. **Actors:** Members holding 20%; board receiving/acting; secretary notifying; members voting.
4. **Transaction:** Requisitioned general meeting.
5. **Stage:** Member request → board convening decision → notice → meeting.
6. **Governing document:** Supplied threshold/power summary; full articles absent.

**FACT_DISPOSITIONS:** `20% holding = used-outcome`, exceeding 15%; member origin `used-outcome`; resolution/venue/date/time described as supplied but absent `input gap`.

**MUST_OPEN:**

- Module 10 §§2.2.1 and 2.2.5.
- Appendix 25B: threshold recital, request, proposed resolution and member execution.
- Appendix 25A general-meeting branch: immediate board response under a right merely to require the board to convene.
- Appendix 25E: subsequent notice.

**CONDITIONAL:**

- IF actual law/articles permit requisitionists themselves to convene after board default → branch to that procedure; the fixture presently says only “require one”.
- IF short notice → Appendix 25C.
- IF resolution filing applies → Appendix 25L after passage.

**MUST_NOT_OPEN/USE:**

- Appendix 25A as the first document: members, not the board, originate.
- Appendix 25D: wrong meeting/business type.
- A 10% generic manual threshold: supplied 15% article controls.

**DOCUMENT_CHAIN:** Appendix 25B signed by qualifying 20% members → Appendix 25A board convening resolution → Appendix 25E notice → meeting/vote/minutes → conditional filing.

**MATERIALS_GAPS:** Resolution, venue, date, time, member identities/holdings, notice period and default procedure are absent.

**UNRESOLVED_BRANCHES:** Board-default/requisitionist-convening procedure; short notice.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `incorporate supplied 15% rule, actual text gap`; procedure `incorporate`; duties `checked-not-relevant`; records `incorporate`; documents `incorporate 25B→25A→25E`; consequences `conditional board-default remedy`.

**CONCLUSION:** Appendix 25B is the first document; because the members only require the board to act, Appendix 25A is the immediate next stage before Appendix 25E notice.

## P08A — Solvent voluntary winding-up

**TASK_TYPE:** Prose explanation with complete course-document-chain identification.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Members’ voluntary winding-up, subject to local variations.
3. **Actors:** Directors declaring solvency; members resolving; liquidator realising/paying/reporting; Registrar.
4. **Transaction:** Solvent voluntary liquidation.
5. **Stage:** Inquiry/declaration → member resolution/liquidator → notices → realisation/payment → final account/approval → dissolution.
6. **Governing document:** Actual statute/articles absent; manual supplies typical 1948-model procedure.

**FACT_DISPOSITIONS:** Ceasing business `used-outcome`; full inquiry `used-outcome`; ability to pay all debts in statutory period `used-outcome`; actual asset/liability figures, period and jurisdiction `input gaps`.

**MUST_OPEN:**

- Module 12 §§3.1.1-3.1.2 and §4.
- Module 10 §§2-4 for member decision mechanics.
- Appendix 30A: solvency declaration plus attached asset/liability statement.
- Appendix 30B: solvency recitals, five resolutions and execution.
- Appendices 30C and 30D: publication and Registrar notices.
- Appendices 30E and 30G: final-meeting route.
- Appendices 30F and 30G: alternative written-approval route.

**CONDITIONAL:**

- IF local law permits board rather than member commencement for an IBC/BC → use that actor only if actual constitution/statute proves it.
- IF final meeting is held → 30E+30G → EXCLUDE 30F.
- IF final meeting is validly dispensed with → 30F+30G → EXCLUDE 30E.
- IF local law requires interim/anniversary meetings → add them.

**MUST_NOT_OPEN/USE:**

- Module 12 §3.2 creditor route: solvency finding excludes it.
- Appendices 31A-31C striking-off route: liquidation selected and debts/assets exist.
- Both 30E and 30F as cumulative completion documents: they are alternatives.

**DOCUMENT_CHAIN:** Appendix 30A + true statement of assets/liabilities → Appendix 30B → 30C publication + 30D Registrar notice → liquidator collects assets and pays debts → 30G final account → either 30E final meeting or 30F written approval → final Registrar filing/request → dissolution certificate.

**MATERIALS_GAPS:** Jurisdiction, statutory period, exact threshold/actor, declaration timing, figures, liquidator details, publication deadline and dissolution waiting period are absent. Appendix 30G is skeletal and requires reconstruction from real figures.

**UNRESOLVED_BRANCHES:** Final meeting versus written approval; local member/board authority.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `conditional`; procedure `incorporate`; duties/liability `incorporate declaration accuracy`; records/filings `incorporate with local gaps`; documents `incorporate 30A-G as branched`; consequences `incorporate director powers cease, debts paid, surplus distributed, dissolution`.

**CONCLUSION:** The solvent branch is a members’ voluntary winding-up beginning with 30A and 30B, then notices and liquidation, and ending with 30G plus either 30E or 30F.

## P08B — Insolvent voluntary winding-up

**TASK_TYPE:** Prose explanation and identification of the available/incomplete creditors’ course chain.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Creditors’ voluntary winding-up.
3. **Actors:** Directors convening members and creditors; members resolving; creditors selecting liquidator; liquidator; Registrar.
4. **Transaction:** Voluntary liquidation where debts cannot be paid in full.
5. **Stage:** Member meeting → creditor meeting/appointment → realisation and priority distribution → final creditor/member meetings/accounts/filings.
6. **Governing document:** Local insolvency statute/articles absent; course gives typical 1948-model outline.

**FACT_DISPOSITIONS:** Cease business `used-outcome`; full inquiry `used-content`; inability to pay all debts within statutory period `used-outcome`; creditor/assets figures `input gaps`.

**MUST_OPEN:**

- Module 12 §§3.2.1-3.2.3 and §4.
- Module 10 §§2.2, 2.5-2.12 to the limited extent applicable to the members’ meeting.
- Appendix 25A general-meeting branch and Appendix 25E for the initial member-meeting convening/notice structure.

**CONDITIONAL:**

- IF local law allows adaptation → Appendix 30C, 30D and 30G may provide publication, Registrar-notice and account structures after changing the members’-voluntary assumptions and verifying creditor requirements.
- IF continued trading raises director/officer exposure → Module 8 §6 and Module 9 §1.5.
- IF creditor meeting proxy/notice rules are supplied separately → incorporate them.

**MUST_NOT_OPEN/USE:**

- Appendix 30A: directors cannot make the solvency declaration.
- Appendix 30B as drafted: recital B states the company can pay debts in full.
- Appendices 30E/30F as complete creditor-route precedents: they provide only member-finalisation assumptions and omit creditor approval.
- Striking-off forms: insolvent liabilities remain.

**DOCUMENT_CHAIN:** Board convenes members → member notice/special winding-up resolution and publication/filing → board convenes creditors with financial statement → creditors select liquidator → liquidator realises assets and pays in priority → periodic/final creditor and member meetings → final account and filings → dissolution.

**MATERIALS_GAPS:** The course appendix set contains no exact creditors’ meeting notice, creditor appointment resolution, creditor proxy, insolvent commencement resolution or dual final-meeting package. Jurisdiction, thresholds, deadlines and financial particulars are absent.

**UNRESOLVED_BRANCHES:** Whether/how 30C, 30D and 30G may be adapted under local law; exact creditor-meeting procedure.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `materials gap`; procedure `partial course coverage`; duties `conditional continued-trading exposure`; records/filings `partial coverage`; documents `materials gap for creditor-specific chain`; consequences `incorporate priority distribution/dissolution`.

**CONCLUSION:** Route this as a creditors’ voluntary winding-up and expose the absence of creditor-specific course precedents; the solvent 30A/30B package cannot be reused.

## P09A — Appoint company secretary

**TASK_TYPE:** Drafting: appointment resolution, role schedule and records step.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Secretary appointment; mandatory/optional status unknown.
3. **Actors:** Sole director appointing; Taylor as proposed secretary; company/administrator updating records.
4. **Transaction:** Fixed-term secretary appointment with delegated minute/filing duties.
5. **Stage:** Eligibility/consent → appointment/delegation → register → conditional Registrar filing.
6. **Governing document:** Actual statute/articles absent.

**FACT_DISPOSITIONS:** Sole director as appointing actor `used-outcome`; Taylor distinct from director `used-outcome`; fixed term `used-content`; minutes and filings `used-content/outcome`; Taylor’s written consent/qualifications/address `input gaps`.

**MUST_OPEN:**

- Module 9 §§1.1, 1.2.1 and 1.3-1.4: eligibility, appointment, role and delegation.
- Module 10 §§3-4: sole-director written action.
- Module 3 §4.1.2 and Appendix 7B: officer record.
- Appendix 24A: two appointment/delegation recitals, two resolutions and execution.
- Appendix 24C: 15 delegated responsibilities, including minutes and public filings.

**CONDITIONAL:**

- IF local law makes the secretary mandatory → obtain written consent, verify qualification/residence and notify Registrar.
- IF optional → board appointment under actual articles, with no external filing unless local law requires it.
- IF only the stated two duties are intended → adapt the 24C delegation consciously rather than conferring every listed function.

**MUST_NOT_OPEN/USE:**

- Appendix 9 as the main precedent: first-board package and many unrelated resolutions.
- Module 9 §2/registered-agent route: Taylor is expressly secretary.
- Appendix 24B: removal/replacement, not appointment.

**DOCUMENT_CHAIN:** Taylor’s written consent/eligibility evidence → Appendix 24A inserting fixed term and approving selected Appendix 24C responsibilities → Appendix 7B entry → conditional Registrar notice → retain consent/resolution/schedule.

**MATERIALS_GAPS:** Jurisdiction, actual articles, consent, eligibility, address, appointment dates and fixed-term end date. Appendix 24A lacks an express fixed-term clause, so the supplied term must be added without inventing termination law.

**UNRESOLVED_BRANCHES:** Mandatory versus optional secretary; full versus limited 24C delegation; external filing.

**SEVEN_LAYER_CLOSURE:** Substantive `incorporate`; constitution `conditional`; procedure `incorporate`; duties/liability `incorporate secretary duties`; records `incorporate`; documents `incorporate 24A/24C`; consequences `conditional filing/term expiry`.

**CONCLUSION:** Appoint Taylor through Appendix 24A with a deliberately scoped 24C schedule, then enter Taylor in Appendix 7B and file only if local law requires it.

## P09B — Appoint registered agent; exact precedent gap

**TASK_TYPE:** Drafting requested, but constrained by an exact course-precedent and factual eligibility gap.

**SIX_LOCKS:**

1. **Jurisdiction:** Genuinely unknown.
2. **Regime:** Statutory registered-agent appointment or replacement.
3. **Actors:** Sole director, subject to article power; Taylor as proposed licensed resident agent; existing/outgoing agent if replacement; Registrar.
4. **Transaction:** Appointment of registered agent, not secretary.
5. **Stage:** Eligibility/licensing → consent → corporate appointment → prescribed change filing → register/records transfer.
6. **Governing document:** Actual IBC/BC statute, memorandum/articles and existing-agent status absent.

**FACT_DISPOSITIONS:** Taylor will maintain statutory records and accept service `used-outcome`; express registered-agent capacity `used-outcome`; sole director decision `conditional on article power`; fixed term `used-content but compliance risk`; Taylor’s residence/licence and whether this is initial or replacement appointment `input gaps`.

**MUST_OPEN:**

- Module 9 §§2.1-2.3: statutory status, licensing/residence, appointment/replacement, prescribed consent/filing, records and service.
- Module 3 §§4.1.2, 4.5.4 and 4.5.7: registered-agent record and initial-board context.
- Appendix 7B: registered-agent entry.

**CONDITIONAL:**

- IF this is the first appointment on incorporation → Appendix 9 resolution 3 is the closest course wording, but it belongs to an inaugural package and still lacks the statutory filing/term details.
- IF this is replacement and articles permit directors to act → board resolution plus prescribed outgoing/new-agent filing and consent.
- IF articles do not confer board power → member resolution is required.
- IF Taylor is not locally resident and licensed → appointment cannot proceed.
- IF a fixed term expires without replacement → mandatory-agent breach/strike-off risk; appointment must preserve continuous coverage.
- IF Taylor is a service provider → Module 11 §§2.7-2.9 may supplement operational responsibilities.

**MUST_NOT_OPEN/USE:**

- Appendix 24A: appoints a secretary only.
- Appendix 24C: secretary role schedule, not registered-agent instrument.
- Appendix 24B: secretary removal branch.
- Appendix 9 as an exact replacement precedent: wrong lifecycle stage and incomplete statutory package.

**DOCUMENT_CHAIN:** Verify Taylor’s licence/residence and current-agent status → obtain consent → correct member/board appointment instrument, for which no exact course precedent exists → prescribed form signed/filed by outgoing agent and endorsed by Taylor where replacement → Registrar record → Appendix 7B/register of agents → transfer/maintain statutory records and service arrangements.

**MATERIALS_GAPS:** No exact registered-agent appointment/removal precedent is indexed. No prescribed form, licence/residence evidence, jurisdiction, existing agent, actual memorandum/articles, term dates or continuous-replacement provision is supplied. Unsupported statutory wording must not be invented.

**UNRESOLVED_BRANCHES:** Initial versus replacement appointment; board versus member authority; Taylor’s eligibility; compatibility of fixed term with mandatory continuous appointment.

**SEVEN_LAYER_CLOSURE:** Substantive `partial course coverage`; constitution `materials gap`; procedure `conditional`; duties/liability `incorporate statutory compliance risk`; records `incorporate Appendix 7B`; documents `materials gap exact instrument/form`; consequences `conditional offence/strike-off if vacancy occurs`.

**CONCLUSION:** The registered-agent route is legally identifiable but not completely draftable from the supplied course precedents; Appendix 24A must not be repurposed to conceal the gap.

END SYNTHETIC CANDIDATE A
