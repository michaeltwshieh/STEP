# Synthetic Candidate B

## Boundary attestation / file-open ledger

- `BOUNDARY`: Read-only replay performed only in `/Users/michaelshieh/Desktop/Claude Projects/STEP Exam/KnowledgeBase/Company Law Exam Bot`.
- `ATTESTATION`: No file was edited, created, deleted, renamed or hashed; no subagent was spawned; no baseline, blind output, report, KAP, past-answer, gold, freeze-record, amendment, or other candidate file was searched, listed or opened.
- `CONTROL_FILES_OPENED`: `CLAUDE.md`; `Content.md`; `routing-prompt.md`; `section-b.md`; `Syllabus.md`; `content-test.md`; `routing-tests/corpus/question-fixtures.json`.
- `MODULE_PASSAGES_OPENED`: Module 3 §§2, 4.1.1–4.1.5, 4.5.1–4.5.7 and footnote 35; Module 4 §§1–2.4; Module 5 §§2.2, 3–3.2; Module 6 §§5–7.3; Module 8 §§1.2–1.4 and relevant footnotes; Module 9 §§1–2.4; Module 10 §§2.2–2.2.6, 3–5.8; Module 11 §§2.4–2.9, 3; Module 12 §§3–4.
- `APPENDICES_OPENED_IN_FULL`: 4; 7A; 7B; 7D; 10A; 10B; 10C; 12; 16D; 18A–18E; 19A–19C; 20E; 24A; 24C; 25A; 25B; 25E; 26; 27A; 27B; 30A–30G.
- `NOTATION`: Fact dispositions: `UO` = used—outcome; `UC` = used—content; `NO` = not outcome-changing; `IG` = input gap; `MG` = materials gap. Seven-layer order: `1 substantive; 2 constitution/capacity; 3 decision/procedure; 4 duties/liability; 5 records/filings; 6 documents; 7 consequences/remedies`.

---

## P01A — Traditional final dividend

- `TASK_TYPE`: Hybrid—explain procedure; draft two-organ approval chain.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown; only the supplied traditional/Table A regime is selected.
  - `REGIME`: Traditional final dividend under actual Table A-style articles.
  - `ACTORS`: Board recommends; members declare; secretary/CSP implements payment.
  - `TRANSACTION`: $100,000 final dividend from $120,000 distributable profits.
  - `STAGE`: Financial review → recommendation → member approval → payment/records.
  - `GOVERNING_DOCUMENTS`: Actual articles supplied as to division of power; remaining clauses and legislation unknown; traditional rules are course extracts.
- `MATERIAL_FACT_DISPOSITIONS`: `$120,000 profits`=`UO` (funding ceiling); `$100,000 dividend`=`UO/UC`; `final`=`UO`; `members declare on board recommendation`=`UO`; AB Ltd/name=`UC`; share count, record date, financial year and payment date=`IG`.
- `MUST_OPEN`: Module 6 §§6.1–6.2; Module 10 §5.7 and §4 if written resolutions are used; Appendix 19A, Director’s resolution to recommend payment of a dividend; Appendix 19B, Member’s resolution to declare and pay a dividend recommended by board.
- `CONDITIONAL`:
  - `IF live general meeting ->` open Module 10 §§2.2–2.12 and Appendices 25A/25E for convening and notice; exclude written-resolution-only mechanics.
  - `IF actual articles instead give directors sole authority ->` open Appendix 19C; exclude 19A+19B. Trigger is absent and conflicts with supplied facts.
- `MUST_NOT_OPEN`: Appendix 20E (BVI/IBC solvency-distribution regime); Appendix 19C (board-only article route); Module 12 (no insolvency fact).
- `DOCUMENT_CHAIN`: Financial review → Appendix 19A board recommendation for $100,000 → Appendix 19B member declaration not exceeding recommendation → secretary/CSP payment instruction and accounting/minute records.
- `MATERIALS_GAPS`: Drafting particulars listed above; full actual articles and jurisdiction-specific filing/account requirements are absent.
- `UNRESOLVED_BRANCHES`: Member approval by written resolution versus live general meeting.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—actual articles control; 3 incorporate; 4 checked-not-relevant—no misconduct; 5 conditional—account/minute/payment records, local filings unknown; 6 incorporate; 7 incorporate—invalid if no board recommendation or if declaration exceeds it.`
- `CONCLUSION`: Use the traditional two-organ chain—Appendix 19A followed by Appendix 19B; neither a board-only dividend nor a BVI solvency distribution fits.

---

## P01B — BVI BC solvency distribution

- `TASK_TYPE`: Hybrid—explain BVI procedure; draft board-only authorisation.
- `SIX_LOCKS`:
  - `JURISDICTION`: Supplied—BVI.
  - `REGIME`: BVI Business Company, BVI BCA distribution regime.
  - `ACTORS`: Directors authorise; administrator/CSP pays.
  - `TRANSACTION`: $100,000 statutory distribution to members.
  - `STAGE`: Accounts/solvency review → board authorisation and statement → payment.
  - `GOVERNING_DOCUMENTS`: BVI BCA ss.56–57 course extract; actual BVI memorandum/articles mentioned as governing but not reproduced.
- `MATERIAL_FACT_DISPOSITIONS`: `BVI BC`=`UO`; `directors may authorise`=`UO`; `statutory solvency test`=`UO`; `$120,000 profits`=`NO as traditional profits ceiling, but relevant financial evidence`; `$100,000`=`UO/UC`; `final dividend` wording=`NO where inconsistent—BVI terminology is distribution`; share/record/payment details=`IG`.
- `MUST_OPEN`: Module 6 §7.3, including BVI BCA ss.56–57 extract; Module 10 §5.8; Appendix 20E, Director’s resolution to distribute from IBC/BC with statement of solvency.
- `CONDITIONAL`: `IF payment is delayed and directors cease to be satisfied before payment ->` reconsider/revoke distribution under the applicable BVI rule; exact recovery mechanics are not fully supplied.
- `MUST_NOT_OPEN`: Appendices 19A/19B (traditional two-organ dividend); Appendix 19C (different board-only dividend terminology without BVI statutory statement); Module 6 §6 except as discarded comparison.
- `DOCUMENT_CHAIN`: Accounting review → board written resolution stating reasonable satisfaction that assets exceed liabilities and debts remain payable as due immediately after distribution → authorise $100,000 → administrator payment instruction → accounting/minute records.
- `MATERIALS_GAPS`: Actual memorandum/article clause; allocation/record date, recipients, bank details and payment date.
- `UNRESOLVED_BRANCHES`: None outcome-changing; factual placeholders remain.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—subject to actual memorandum/articles; 3 incorporate; 4 incorporate—reasonable grounds/director care; 5 incorporate—accounts and resolution records; 6 incorporate; 7 conditional—improper authorisation/recovery detail not fully covered.`
- `CONCLUSION`: The BVI facts select a single Appendix 20E directors’ authorisation with the statutory solvency statement; no member declaration is required.

---

## P02A — Board accepts voluntary share transfer

- `TASK_TYPE`: Drafting with short procedural explanation.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Voluntary inter vivos share transfer; board-registration route.
  - `ACTORS`: Transferor/transferee execute; board approves; secretary/RA/CSP registers.
  - `TRANSACTION`: Legal-title transfer accepted for registration.
  - `STAGE`: Execution and delivery already reached → approval → registration/certificate.
  - `GOVERNING_DOCUMENTS`: Actual articles mentioned implicitly but absent; course traditional transfer model.
- `MATERIAL_FACT_DISPOSITIONS`: Executed form=`UO`; old certificate=`UO`; required fee=`UC/NO`; board accepts=`UO`; party/share particulars=`IG`; pre-emption compliance=`IG`.
- `MUST_OPEN`: Module 6 §5.1 stages 2–5; Module 10 §5.3; Appendix 18A, Share transfer form; Appendix 18B, Director’s resolution authorising transfer; Appendix 7A, Register of members; Appendix 16D, Share certificate.
- `CONDITIONAL`: `IF transferee also becomes beneficial owner ->` update BO register using Module 3 §4.1.5/Appendix 7D and make any competent-authority filing; `IF local return required ->` file it.
- `MUST_NOT_OPEN`: Appendices 18C/18D (refusal branch); Appendix 18E (death transmission); Appendices 26/27 (beneficial-only transfer with nominee remaining).
- `DOCUMENT_CHAIN`: Appendix 18A already executed/delivered with old certificate → Appendix 18B approval → enter transferee and cessation/transfer in Appendix 7A → cancel old certificate → issue Appendix 16D new certificate → conditional BO/Registrar update.
- `MATERIALS_GAPS`: Actual transfer article, pre-emption evidence/waiver, parties, shares, consideration, certificate numbers and jurisdiction-specific external filing.
- `UNRESOLVED_BRANCHES`: BO-register and public-return requirements depend on jurisdiction and ultimate ownership.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—actual articles/pre-emption; 3 incorporate; 4 checked-not-relevant—no improper purpose; 5 incorporate/conditional; 6 incorporate; 7 incorporate—registration makes transferee legal holder.`
- `CONCLUSION`: Approval route is Appendix 18A → Appendix 18B → register/certificate implementation; refusal and transmission documents are excluded.

---

## P02B — Board refuses voluntary share transfer

- `TASK_TYPE`: Drafting with notification-stage explanation.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Voluntary transfer—refusal branch.
  - `ACTORS`: Transferor/transferee executed; board refuses; company/director/secretary notifies proposed transferee.
  - `TRANSACTION`: Refusal to register legal-title transfer.
  - `STAGE`: Delivery complete → refusal resolution → notice/return documents.
  - `GOVERNING_DOCUMENTS`: Actual articles absent; course transfer/refusal model only.
- `MATERIAL_FACT_DISPOSITIONS`: Executed form, old certificate, fee=`UO/UC`; refusal=`UO`; reasons=`IG`; actual article/time limit=`IG`.
- `MUST_OPEN`: Module 6 §5.1 stages 3–4; Module 10 §5.3; Appendix 18A; Appendix 18C, Director’s resolution refusing registration; Appendix 18D, Notice of refusal.
- `CONDITIONAL`: `IF governing law/articles require reasons ->` accurate reasons must appear in 18C/18D; `IF traditional Appendix 1B model controls ->` notice as soon as possible and within two months; verify exact article before use.
- `MUST_NOT_OPEN`: Appendix 18B (approval branch); Appendix 7A/16D implementation (no registration/new certificate); Appendix 18E (transmission); Appendices 26/27 (beneficial-only route).
- `DOCUMENT_CHAIN`: Appendix 18A lodged → Appendix 18C refusal resolution → Appendix 18D notice to proposed transferee within governing period → return transfer form and old certificate.
- `MATERIALS_GAPS`: Reason for refusal; exact governing article; whether reasons are legally mandatory; jurisdiction-specific deadline. Appendix 18C/18D cite art.8.2 while Module 6 describes approval/refusal under arts.8.3/8.5, so actual articles must resolve the conflict.
- `UNRESOLVED_BRANCHES`: Reasons-required versus reasons-not-required; precise notice period.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 materials gap—actual article; 3 incorporate; 4 conditional—unreasonable/frivolous refusal may be challenged; 5 incorporate—notice/returned documents; 6 incorporate; 7 conditional—challenge consequences depend on facts/law.`
- `CONCLUSION`: Use Appendix 18C followed by Appendix 18D, but do not invent reasons or an article number where the governing materials are absent.

---

## P03A — Registered holder alive; voluntary transfer

- `TASK_TYPE`: Drafting—complete voluntary-transfer chain.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Voluntary inter vivos transfer.
  - `ACTORS`: Jordan=registered transferor; Morgan=transferee; board=approver; administrator=registrar.
  - `TRANSACTION`: Legal title changes from living holder Jordan to Morgan.
  - `STAGE`: Agreement → execution/delivery → board approval → registration/certificate.
  - `GOVERNING_DOCUMENTS`: Actual articles absent.
- `MATERIAL_FACT_DISPOSITIONS`: Jordan alive=`UO`; Jordan agrees=`UO`; sole registered share=`UO/UC`; Morgan to be registered=`UO`; company willing=`UO`; consideration, addresses, certificate and pre-emption=`IG`.
- `MUST_OPEN`: Module 6 §5.1; Module 10 §5.3; Appendices 18A, 18B, 7A and 16D.
- `CONDITIONAL`: `IF Morgan is also new beneficial owner ->` Appendix 7D/competent-authority update; `IF pre-emption exists ->` evidence of compliance/waiver before approval.
- `MUST_NOT_OPEN`: Appendix 18E (Jordan is alive); Appendices 18C/18D (company willing); Appendix 26/27 (registered holder changes).
- `DOCUMENT_CHAIN`: Jordan and Morgan execute Appendix 18A → deliver it with old certificate/required fee → board executes Appendix 18B → update Appendix 7A → cancel Jordan’s certificate → issue Morgan Appendix 16D → conditional BO/Registrar filing.
- `MATERIALS_GAPS`: Actual article, pre-emption status, consideration and execution/certificate particulars.
- `UNRESOLVED_BRANCHES`: BO/public filing only.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—articles; 3 incorporate; 4 checked-not-relevant; 5 incorporate/conditional; 6 incorporate; 7 incorporate—Morgan becomes legal holder on register entry.`
- `CONCLUSION`: Jordan’s life and consent require the voluntary Appendix 18A/18B route, not transmission.

---

## P03B — Registered holder deceased; transmission

- `TASK_TYPE`: Drafting—death-transmission chain.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Transmission by death, not voluntary transfer.
  - `ACTORS`: Jordan=deceased registered holder; Morgan=duly appointed personal representative and applicant; company administrator registers.
  - `TRANSACTION`: Legal title passes by operation of law and Morgan elects registration as personal representative.
  - `STAGE`: Status/evidence → written request → registration/certificate.
  - `GOVERNING_DOCUMENTS`: Actual articles absent; course transmission model.
- `MATERIAL_FACT_DISPOSITIONS`: Death=`UO`; Morgan personal representative=`UO`; sole share=`UO/UC`; company willing=`UO`; probate/death-certificate particulars=`IG though appointment is stated`.
- `MUST_OPEN`: Module 6 §5.2; Module 10 §5.3; Appendix 18E, Personal representative request; Appendix 7A; Appendix 16D.
- `CONDITIONAL`: `IF Morgan instead transfers directly to an heir ->` PR executes voluntary transfer form under Module 6 §5.2/Appendix 18A; exclude 18E registration election.
- `MUST_NOT_OPEN`: Appendices 18A/18B on selected facts (voluntary inter vivos route); 18C/18D (refusal); 26/27 (beneficial-only nominee route).
- `DOCUMENT_CHAIN`: Death certificate + grant of probate + old certificate → Morgan’s Appendix 18E request → update register of members/BO register → cancel old certificate → issue new certificate to Morgan if applicable.
- `MATERIALS_GAPS`: Actual transmission article and evidence particulars; no separate exact board-approval precedent is supplied for an 18E request.
- `UNRESOLVED_BRANCHES`: None—the facts select Morgan’s own registration rather than direct transfer to heirs.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—articles; 3 incorporate; 4 checked-not-relevant; 5 incorporate; 6 incorporate; 7 incorporate—transmission is by law, evidenced and recorded through 18E.`
- `CONCLUSION`: Jordan’s death displaces the voluntary-transfer forms; use Appendix 18E with probate/death evidence and registration records.

---

## P04A — Registered-office move within jurisdiction

- `TASK_TYPE`: Hybrid—procedure plus approval drafting.
- `SIX_LOCKS`:
  - `JURISDICTION`: Supplied only as “existing jurisdiction”; exact jurisdiction unknown.
  - `REGIME`: Same-jurisdiction registered-office relocation.
  - `ACTORS`: Board decides; secretary/RA/CSP notifies Registrar and implements.
  - `TRANSACTION`: Address change, not migration.
  - `STAGE`: Board approval → Registrar notice → physical/administrative implementation.
  - `GOVERNING_DOCUMENTS`: Actual articles and local statute absent; course traditional/BVI comparisons.
- `MATERIAL_FACT_DISPOSITIONS`: Old/new addresses=`UC`; both in same jurisdiction=`UO`; incorporation jurisdiction unchanged=`UO`.
- `MUST_OPEN`: Module 5 §§2.2 and 3.2; Module 10 §5.4; Appendix 12, Board resolution to change location of registered office.
- `CONDITIONAL`: `IF actual articles condition the board’s power ->` satisfy that condition; `IF local prescribed form applies ->` file form/fee within local deadline.
- `MUST_NOT_OPEN`: Module 4 §2 and Appendices 10A–10C (migration/continuance); Appendix 25E/member resolution absent a contrary actual rule.
- `DOCUMENT_CHAIN`: Appendix 12 resolution changing address to 2 Harbour Road → notify Registrar → move statutory registers/common seal as applicable → amend stationery/name plate → notify bankers and other interested parties.
- `MATERIALS_GAPS`: Jurisdiction, exact article, prescribed form/fee and deadline; the manual gives 14 days as a common/traditional illustration, not a universal rule.
- `UNRESOLVED_BRANCHES`: Local filing mechanics only.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—no nationality/memorandum change; 3 incorporate; 4 checked-not-relevant; 5 incorporate with local gap; 6 incorporate; 7 incorporate—same entity/jurisdiction.`
- `CONCLUSION`: This is an Appendix 12 board-address change, not a continuance.

---

## P04B — Continuation into another jurisdiction

- `TASK_TYPE`: Hybrid—explain continuance and draft approval/evidence package.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown—both old and new jurisdictions omitted.
  - `REGIME`: Outgoing/incoming continuance as same legal entity.
  - `ACTORS`: Board initiates/recommends; members approve unless governing regime authorises otherwise; director swears evidence; service provider files.
  - `TRANSACTION`: Migration/re-domiciliation, not an office relocation.
  - `STAGE`: Eligibility → board approval → member approval → evidential affidavit/exhibits → filing/certificate → records move.
  - `GOVERNING_DOCUMENTS`: Both jurisdictions’ legislation and actual constitution mentioned but absent.
- `MATERIAL_FACT_DISPOSITIONS`: New address abroad=`UO`; same entity continues=`UO`; old/new street addresses=`UC`; jurisdiction names, solvency/good-standing/exhibits=`IG`.
- `MUST_OPEN`: Module 4 §§2.1–2.3; Module 5 §§2.2 and 3.2; Module 10 §§2–4; Appendices 10A, 10B and 10C.
- `CONDITIONAL`:
  - `IF new law requires conforming articles ->` attach them under 10A’s optional branch.
  - `IF board alone is authorised ->` member approval may be excluded only after actual law/articles confirm.
  - `IF outgoing BVI company ->` advertisement and 14-day member/creditor notice identified in Module 4 §2.2.
- `MUST_NOT_OPEN`: Appendix 12 (same-jurisdiction address only); Module 4 §1 foreign-company registration (does not change domicile); Appendices 13A/13B (public/private re-registration).
- `DOCUMENT_CHAIN`: 10A board initiation/recommendation → 10B member approval → 10C affidavit/declaration with certificate, constitution, registers, good standing, financial statements, solvency and legal evidence → continuation application → certificate of continuation → registry/records implementation.
- `MATERIALS_GAPS`: Old/new jurisdictions, enabling statutory provisions, threshold, actual articles, good-standing/solvency/legal evidence and exhibits. Package cannot be completed non-conditionally.
- `UNRESOLVED_BRANCHES`: Member versus authorised-board approval; new-articles requirement; outgoing notice requirements.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate/conditional; 3 incorporate/conditional; 4 incorporate—solvency/creditor protection; 5 incorporate with gaps; 6 incorporate; 7 incorporate—property, contracts, debts and shares continue in same entity.`
- `CONCLUSION`: Cross-border continuity selects the 10A→10B→10C migration package; Appendix 12 is forbidden.

---

## P05A — Beneficial owner changes; nominee remains

- `TASK_TYPE`: Hybrid—explain and draft beneficial-only ownership chain.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Nominee-shareholding/beneficial-ownership change.
  - `ACTORS`: Owner A=outgoing beneficial owner/instruction signer; Owner B=incoming beneficial owner/endorser; Nominee Ltd=unchanged registered holder and implementer.
  - `TRANSACTION`: Beneficial interest changes; legal title does not.
  - `STAGE`: Instruction/endorsement → cancel old nominee instrument → new nominee instrument → BO/tax records.
  - `GOVERNING_DOCUMENTS`: Existing nominee agreement/declaration mentioned by relationship but absent; local BO/FATCA/CRS rules unknown.
- `MATERIAL_FACT_DISPOSITIONS`: Nominee remains=`UO`; A→B beneficial transfer=`UO`; nominee identity=`UC`; consideration/effective date/existing instrument type=`IG`.
- `MUST_OPEN`: Module 11 §§2.5 and 3; Module 10 §5.3 beneficial-only paragraph; Module 3 §4.1.5; Appendix 26; Appendix 27A; Appendix 27B; Appendix 7D.
- `CONDITIONAL`:
  - `IF bilateral arrangement ->` use complete Appendix 27A.
  - `IF unilateral declaration is required ->` Appendix 27B is only an incomplete extract; omitted provisions remain a gap.
- `MUST_NOT_OPEN`: Appendices 18A–18D, 7A and 16D (registered holder does not change); Appendix 18E (no death).
- `DOCUMENT_CHAIN`: Owner A signs and Owner B endorses Appendix 26 → Nominee Ltd cancels/replaces old nominee instrument → execute new 27A or incomplete 27B branch in favour of B → update Appendix 7D and FATCA/CRS/competent-authority records; no register-of-members change.
- `MATERIALS_GAPS`: Existing nominee instrument; local BO definitions/forms/filing; Appendix 27B’s omitted operative clauses; consideration/effective date.
- `UNRESOLVED_BRANCHES`: 27A bilateral agreement versus 27B unilateral declaration.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—legal holder unchanged; 3 incorporate; 4 incorporate—nominee acts under contract/instructions; 5 incorporate; 6 incorporate/27B gap; 7 incorporate—B acquires beneficial interest only.`
- `CONCLUSION`: Because Nominee Ltd stays registered, use Appendix 26 plus a replacement 27A/27B nominee instrument and BO records, not the legal-transfer appendices.

---

## P05B — Legal title changes; nominee leaves register

- `TASK_TYPE`: Hybrid—explain and draft legal-title transfer chain.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Voluntary legal-title share transfer ending nominee holding.
  - `ACTORS`: Owner A instructs under the nominee relationship; Nominee Ltd is legal transferor; Owner B is transferee/new registered holder; board approves.
  - `TRANSACTION`: Both economic ownership and registered legal title move to B.
  - `STAGE`: Authority/instruction → transfer execution → board approval → register/certificate/BO update → terminate nominee arrangement.
  - `GOVERNING_DOCUMENTS`: Existing nominee contract and actual transfer articles absent.
- `MATERIAL_FACT_DISPOSITIONS`: Nominee leaves register=`UO`; B entered=`UO`; A→B beneficial interest=`UO`; Nominee Ltd registered holder=`UO`; consideration/pre-emption/document particulars=`IG`.
- `MUST_OPEN`: Module 11 §2.5 for actor distinction; Module 6 §5.1; Module 10 §5.3; Appendices 18A, 18B, 7A, 16D and 7D.
- `CONDITIONAL`: `IF pre-emption applies ->` comply/waive before board approval; `IF public/BO return required ->` file after registration.
- `MUST_NOT_OPEN`: Appendix 26 as operative transfer (its stated model keeps the nominee registered and creates a new nominee declaration); Appendices 27A/27B as replacement arrangements (B is to hold directly); Appendix 18E (no death).
- `DOCUMENT_CHAIN`: Owner A’s instruction/termination under existing nominee arrangement (no exact precedent) → Nominee Ltd and Owner B execute Appendix 18A → board Appendix 18B → Appendix 7A replaces Nominee Ltd with B → cancel old certificate/issue Appendix 16D to B → update Appendix 7D/FATCA/CRS → terminate old nominee instrument.
- `MATERIALS_GAPS`: Exact Owner A instruction/nominee-termination precedent; existing agreement terms; actual article/pre-emption; jurisdictional filings.
- `UNRESOLVED_BRANCHES`: None on transaction classification; filing requirements remain conditional.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—legal-title rules/articles; 3 incorporate; 4 incorporate—nominee must act within A’s contractual authority; 5 incorporate; 6 materials gap for instruction/termination, otherwise incorporate; 7 incorporate—B becomes member on register entry.`
- `CONCLUSION`: Nominee Ltd must sign Appendix 18A as transferor; the Appendix 18 legal-title chain replaces the Appendix 26 beneficial-only route.

---

## P06A — Contract signed before incorporation

- `TASK_TYPE`: Hybrid—advise liability; draft post-incorporation adoption instrument.
- `SIX_LOCKS`:
  - `JURISDICTION`: Supplied—BVI.
  - `REGIME`: BVI modern statutory pre-incorporation-contract adoption.
  - `ACTORS`: Signer acted as promoter/pre-incorporation actor, not director at signing; now sole director/board may adopt; supplier is counterparty.
  - `TRANSACTION`: Ordinary supply contract purportedly made for a non-existent company.
  - `STAGE`: Contract pre-dates certificate → company now exists → adoption decision required.
  - `GOVERNING_DOCUMENTS`: BVI BCA s.104 identified in Module 3 footnote 35; exact statutory text and actual articles absent.
- `MATERIAL_FACT_DISPOSITIONS`: One day before certificate=`UO`; later became sole director=`UO`; ordinary written supply contract=`UC`; company name used=`UO`; supplier good faith=`NO for non-existence issue`; BVI=`UO`.
- `MUST_OPEN`: Module 3 §§2.1–2.2 and footnote 35; Appendix 4; Module 8 §§1.2 and 1.4 for the board/sole-director and execution stage.
- `CONDITIONAL`: `IF company adopts under BVI s.104 ->` company becomes bound and Appendix 4 is used; `IF adoption is not made ->` company remains unbound and common-law/promoter position persists; `IF statutory adoption does not release signer ->` release/novation requires separate support.
- `MUST_NOT_OPEN`: Module 8 §1.3 good-faith outsider rule as a substitute for corporate existence; it cannot bind a company that did not yet exist. No Appendix 25 meeting package is needed for a valid sole-director written action.
- `DOCUMENT_CHAIN`: Verify contract/certificate dates → sole-director Appendix 4 resolution adopting contract under BVI statutory power → retain adopted contract/resolution; any separate counterparty release/novation only if required.
- `MATERIALS_GAPS`: Full text/effect of BVI BCA s.104 is cited but not reproduced; the manual says modern provisions may release the promoter, not that every provision does. Appendix 4’s release wording cannot alone prove statutory release. Actual article number and contract particulars are missing.
- `UNRESOLVED_BRANCHES`: Precise continuation/cessation of the signer’s personal liability after BVI adoption.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—company did not exist at signing; 3 incorporate; 4 conditional—promoter liability; 5 incorporate—corporate records; 6 incorporate with release caveat; 7 conditional—adoption binds company, release effect needs verification.`
- `CONCLUSION`: The company was not originally bound; the now-sole director should use Appendix 4 to adopt under the BVI statutory route, while the signer’s release must not be overstated from the available extract.

---

## P06B — Contract signed after incorporation

- `TASK_TYPE`: Prose; no drafting required on stated facts.
- `SIX_LOCKS`:
  - `JURISDICTION`: Supplied—BVI.
  - `REGIME`: Existing BVI BC; ordinary post-incorporation corporate contract.
  - `ACTORS`: Duly appointed sole director acts as the board/company signatory; supplier is good-faith counterparty.
  - `TRANSACTION`: Ordinary written supply contract.
  - `STAGE`: Corporate existence and appointment precede execution; contract already concluded.
  - `GOVERNING_DOCUMENTS`: BVI BCA ss.31, 103 and 107 course extracts/citations; actual articles absent.
- `MATERIAL_FACT_DISPOSITIONS`: One day after certificate=`UO`; duly appointed=`UO`; sole director=`UO`; signed in company name=`UO`; ordinary written contract=`UO`; supplier good faith=`UO/supportive`.
- `MUST_OPEN`: Module 8 §§1.2–1.4 and footnotes 77–79.
- `CONDITIONAL`: `IF the contract is a deed/special transaction ->` apply additional execution formalities; trigger absent. `IF supplier knew of a limitation ->` outsider protection may differ; contradicted by facts.
- `MUST_NOT_OPEN`: Module 3 §2 and Appendix 4 (not pre-incorporation); novation materials (no original personal contract); meeting precedents (sole director already acted).
- `DOCUMENT_CHAIN`: Existing contract only → file/record it as appropriate; no adoption, ratification or novation instrument.
- `MATERIALS_GAPS`: Actual articles are absent, but this does not change the stated result given due appointment, sole-director status and good faith.
- `UNRESOLVED_BRANCHES`: None.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 incorporate—company existed; 3 incorporate—sole director is board; 4 checked-not-relevant—no breach fact; 5 checked-not-relevant beyond ordinary recordkeeping; 6 checked-not-relevant—no new instrument; 7 incorporate—company bound.`
- `CONCLUSION`: AB Ltd is bound by its duly appointed sole director’s post-incorporation contract; no corporate instrument is required now.

---

## P07A — Board originates general meeting

- `TASK_TYPE`: Drafting with procedural explanation.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Board-originated general meeting under supplied actual article.
  - `ACTORS`: Board convenes; secretary/CSP issues notice; members decide resolution.
  - `TRANSACTION`: Convening a meeting to consider supplied resolution.
  - `STAGE`: Originating board decision → notice → meeting.
  - `GOVERNING_DOCUMENTS`: Actual article supplied as to board/requisition powers; other notice/voting clauses absent.
- `MATERIAL_FACT_DISPOSITIONS`: Board originates=`UO`; proposed resolution/venue/date/time=`UC but exact text absent`; 15% member threshold=`NO on selected board branch`.
- `MUST_OPEN`: Module 10 §§2.2.1 and 2.2.4–2.2.5; Appendix 25A board-convening resolution; Appendix 25E specific-resolution notice.
- `CONDITIONAL`: `IF short notice ->` Module 10 §2.2.3/Appendix 25C; `IF proxy documents requested ->` 25F or 25G; neither trigger is stated.
- `MUST_NOT_OPEN`: Appendix 25B (member requisition branch); Appendix 25D (ordinary AGM notice); unrelated substantive resolution appendices until the resolution’s subject is known.
- `DOCUMENT_CHAIN`: First document=Appendix 25A general-meeting branch with supplied place/date/time/resolution → next document=Appendix 25E notice to members/directors/[auditors] → meeting/proxy/minutes as required.
- `MATERIALS_GAPS`: The fixture says particulars are supplied but does not reproduce the proposed resolution, venue, date or time; actual notice period/service/voting clauses are absent.
- `UNRESOLVED_BRANCHES`: Short notice, proxies and resolution threshold depend on omitted facts/articles.
- `SEVEN_LAYER_CLOSURE`: `1 conditional—the resolution’s substantive topic unknown; 2 incorporate—actual convening article; 3 incorporate; 4 checked-not-relevant; 5 incorporate—notice/minutes; 6 incorporate; 7 conditional—defective notice may invalidate proceedings.`
- `CONCLUSION`: Because the board originates, draft Appendix 25A first and Appendix 25E next; Appendix 25B is excluded.

---

## P07B — Qualifying members originate general meeting

- `TASK_TYPE`: Drafting with procedural explanation.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Member-requisitioned general meeting under supplied actual article.
  - `ACTORS`: Members holding 20% requisition; directors then convene; secretary/CSP notices; members decide.
  - `TRANSACTION`: Statutory/article requisition followed by company meeting.
  - `STAGE`: Member request → board convening response → notice → meeting.
  - `GOVERNING_DOCUMENTS`: Actual article supplied as to 15% threshold; other clauses absent.
- `MATERIAL_FACT_DISPOSITIONS`: 20% holding=`UO`; 15% threshold=`UO`; members originate=`UO`; resolution/venue/date/time=`UC but particulars absent`.
- `MUST_OPEN`: Module 10 §§2.2.1 and 2.2.4–2.2.5; Appendix 25B; Appendix 25A general-meeting branch; Appendix 25E.
- `CONDITIONAL`: `IF board fails to respond and legislation grants members a self-help convening power ->` apply only if supplied by actual law; course passage does not give full default procedure.
- `MUST_NOT_OPEN`: Appendix 25D (AGM); member request must not be replaced with Appendix 25A as the originating act; outside law to invent default/time limits.
- `DOCUMENT_CHAIN`: First document=Appendix 25B signed by qualifying 20% members → immediate next procedural document=board Appendix 25A convening resolution → Appendix 25E notice → meeting/minutes.
- `MATERIALS_GAPS`: Exact request/resolution/venue/date/time particulars; statutory response deadline/default powers; remaining articles.
- `UNRESOLVED_BRANCHES`: Board non-compliance/default branch is not fully covered.
- `SEVEN_LAYER_CLOSURE`: `1 conditional—resolution topic unknown; 2 incorporate; 3 incorporate; 4 checked-not-relevant; 5 incorporate; 6 incorporate; 7 conditional—valid requisition obliges board, but default remedy is a gap.`
- `CONCLUSION`: The 20% holding clears the 15% threshold, so Appendix 25B is first, followed by Appendix 25A and then Appendix 25E.

---

## P08A — Solvent voluntary winding-up

- `TASK_TYPE`: Prose with complete course-document-chain identification.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Members’ voluntary winding-up; traditional model subject to local law.
  - `ACTORS`: Directors inquire/declare; members resolve/appoint; liquidator realises, pays and accounts; Registrar dissolves.
  - `TRANSACTION`: Solvent voluntary liquidation, not striking off.
  - `STAGE`: Solvency declaration → commencement/appointment/notices → liquidation → final account/approval → filing/dissolution.
  - `GOVERNING_DOCUMENTS`: Actual legislation/articles absent; traditional course model only.
- `MATERIAL_FACT_DISPOSITIONS`: Cease business=`UO`; full inquiry=`UO`; debts payable in full within statutory period=`UO`; asset/liability particulars and jurisdiction=`IG`.
- `MUST_OPEN`: Module 12 §§3.1 and 4; Module 10 §§2–4; Appendices 30A–30G.
- `CONDITIONAL`:
  - `IF completion by final meeting ->` Appendix 30E + 30G.
  - `IF valid written-approval route ->` Appendix 30F + 30G; exclude 30E.
  - `IF IBC directors may commence under actual constitution ->` alter actor/package only after verification.
- `MUST_NOT_OPEN`: Module 12 §3.2 (creditors’ route); Appendices 31A–31C (striking off); compulsory winding-up §2.
- `DOCUMENT_CHAIN`: 30A declaration + attached assets/liabilities → 30B members’ special resolution and liquidator appointment → 30C publication → 30D Registrar notice → liquidator collects assets/pays creditors → 30G final account → either 30E final-meeting notice or 30F written approval → file account/request dissolution → certificate after statutory period.
- `MATERIALS_GAPS`: Jurisdictional statutory period, threshold, forms, filing deadlines and dissolution period; verified financial schedule and liquidator details.
- `UNRESOLVED_BRANCHES`: Final meeting versus written approval; traditional member versus authorised IBC director commencement.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 conditional—articles/local law; 3 incorporate; 4 incorporate—false/negligent declaration liability; 5 incorporate; 6 incorporate/conditional; 7 incorporate—debts paid before surplus and dissolution.`
- `CONCLUSION`: Solvency selects the members’ route beginning with Appendix 30A and 30B, followed by notices, liquidation and one of the two Appendix 30G completion branches.

---

## P08B — Insolvent voluntary winding-up

- `TASK_TYPE`: Prose with course-document-chain identification and visible precedent gap.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Creditors’ voluntary winding-up.
  - `ACTORS`: Directors convene member and creditor meetings; members resolve; creditors choose liquidator; liquidator realises/distributes/accounts.
  - `TRANSACTION`: Insolvent voluntary liquidation.
  - `STAGE`: Board calls meetings → members resolve → creditors appoint → realisation/priority distribution → final meetings/accounts/filings.
  - `GOVERNING_DOCUMENTS`: Actual insolvency statute/articles absent; Module 12 traditional summary only.
- `MATERIAL_FACT_DISPOSITIONS`: Cannot pay all debts in full within period=`UO`; full inquiry=`UO`; cease business=`UO`; creditor/assets/liabilities details=`IG`.
- `MUST_OPEN`: Module 12 §§3.2 and 4; Module 10 §§2.2–2.12 to the extent applicable; Appendices 25A and 25E only as generic board/member-meeting documents.
- `CONDITIONAL`: `IF local law supplies creditor-meeting forms, notices and filings ->` use them; they are not in the course appendix set. `IF compulsory petition instead chosen ->` Module 12 §2, but that is not the selected voluntary route.
- `MUST_NOT_OPEN`: Appendix 30A (false/conflicting solvency declaration); Appendix 30B (expressly notes solvency and member-appointed liquidator); Appendices 30C–30G as claimed complete creditors’ precedents because each is labelled/assumes members’ voluntary winding-up; Appendices 31A–31C (striking off).
- `DOCUMENT_CHAIN`: Generic 25A/25E may support the first member meeting → member special resolution, filing and publication (no exact action-specific course precedent) → creditor-meeting notice and directors’ financial statement/list (no exact precedent) → creditors’ vote appointing liquidator (no exact precedent) → liquidator realisation and Module 12 §4 priority payments → periodic/final creditor and member meetings/accounts/filings (no exact creditors’ forms).
- `MATERIALS_GAPS`: No exact creditors’ voluntary-winding-up resolution, creditor-meeting notice, creditor appointment, publication/Registrar, final-meeting or final-account precedent; jurisdictional procedure/forms/deadlines absent. Outcome=`partial course coverage`.
- `UNRESOLVED_BRANCHES`: Local thresholds, filing/publication mechanics, and final-document forms.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 materials gap—local law; 3 incorporate at high level; 4 incorporate—avoid wrongful/fraudulent trading; 5 materials gap; 6 materials gap; 7 incorporate—creditor priority, no member surplus unless all debts paid.`
- `CONCLUSION`: Insolvency selects creditors’ voluntary winding-up; the course explains the stages but does not supply a complete matching Appendix 30 document chain.

---

## P09A — Appoint company secretary

- `TASK_TYPE`: Drafting—appointment instrument plus records step.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown.
  - `REGIME`: Optional/required company secretary appointment, exact local branch unknown.
  - `ACTORS`: Sole director/board appoints; Taylor consents and serves as secretary.
  - `TRANSACTION`: Appointment for a fixed term with delegated minutes/filings duties.
  - `STAGE`: Eligibility/consent → board appointment/delegation → officer register → conditional Registrar notice.
  - `GOVERNING_DOCUMENTS`: Actual legislation/articles absent; course secretary models.
- `MATERIAL_FACT_DISPOSITIONS`: Taylor is secretary=`UO`; sole director appoints=`UO subject to articles`; fixed term=`UC/MG`; minutes and filings=`UO/UC`; Taylor’s qualifications/residence/consent=`IG`.
- `MUST_OPEN`: Module 9 §§1.1–1.4; Module 10 §§3–4; Module 3 §4.1.2; Appendix 24A; Appendix 24C; Appendix 7B.
- `CONDITIONAL`:
  - `IF secretary mandatory ->` verify qualification/residence and notify Registrar.
  - `IF optional and articles authorise board ->` board appointment and register entry suffice.
- `MUST_NOT_OPEN`: Appendix 24B (removal/replacement branch); Module 9 §2/registered-agent route; Appendix 7D (not BO).
- `DOCUMENT_CHAIN`: Taylor’s written consent (no standalone course form) → Appendix 24A sole-director resolution naming Taylor and attaching Appendix 24C duties → record Taylor and appointment date in Appendix 7B → conditional Registrar filing.
- `MATERIALS_GAPS`: No standalone consent precedent; Appendix 24A does not provide a fixed-term clause; actual eligibility, residence, article and filing rule are absent. Fixed-term wording must remain a supported factual placeholder rather than invented statutory language.
- `UNRESOLVED_BRANCHES`: Mandatory versus optional secretary regime; Registrar notification.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate; 2 materials gap—actual law/articles; 3 incorporate; 4 incorporate—secretary duties/care; 5 incorporate/conditional; 6 incorporate with consent/term gaps; 7 conditional—appointment validity depends on eligibility and authority.`
- `CONCLUSION`: Use Appendix 24A with Appendix 24C, then Appendix 7B; verify eligibility, consent, term and any Registrar filing.

---

## P09B — Appoint registered agent; exact precedent gap

- `TASK_TYPE`: Drafting request constrained by a materials gap.
- `SIX_LOCKS`:
  - `JURISDICTION`: Genuinely unknown; registered-agent regime implies an IBC/BC-type entity but does not identify one.
  - `REGIME`: Registered-agent appointment or replacement; current stage is unknown.
  - `ACTORS`: Taylor=proposed RA; initial promoter/incorporator or members/board may appoint depending stage/articles; outgoing RA files and incoming RA endorses if replacement.
  - `TRANSACTION`: Statutory resident/licensed-agent appointment, not secretary appointment.
  - `STAGE`: Eligibility → determine initial/replacement and decision-maker → consent/approval → prescribed filing → RA register/records.
  - `GOVERNING_DOCUMENTS`: Entity statute, memorandum, articles and existing RA details absent.
- `MATERIAL_FACT_DISPOSITIONS`: Taylor to be RA=`UO`; statutory records/service duties=`UO`; sole director wishes to appoint=`UO but not proof of power`; fixed term=`MG/UC`; Taylor licence/residence=`IG`; existing RA/stage=`IG`.
- `MUST_OPEN`: Module 9 §§2.1–2.4; Module 3 §§4.1.2, 4.5.4 and 4.5.7; Module 11 §§2.7–2.9; Appendix 7B as the only relevant records template.
- `CONDITIONAL`:
  - `IF initial appointment ->` promoter selects licensed RA, memorandum names it, RA signs/files as incorporator.
  - `IF replacement and articles authorise board ->` board may resolve.
  - `IF replacement but board lacks authority ->` members resolve.
  - `IF replacement ->` outgoing RA files prescribed notice endorsed by Taylor’s consent.
- `MUST_NOT_OPEN`: Appendices 24A–24C (secretary-only instruments); Appendix 25A (meeting-convening, not appointment); outside-law forms used to conceal the gap.
- `DOCUMENT_CHAIN`: Confirm Taylor is resident/licensed → identify initial versus replacement route and actual decision-maker → consent/appointment resolution or incorporation memorandum stage → prescribed Registrar notice endorsed by incoming RA if replacement → enter Taylor in RA register/Appendix 7B and retain statutory records.
- `MATERIALS_GAPS`: No exact registered-agent appointment/removal precedent exists in the indexed appendices; no prescribed filing form; no fixed-term model; jurisdiction/entity, Taylor’s eligibility, actual articles, existing RA and appointment stage are absent. Outcome=`partial course coverage; cannot produce a complete operative instrument`.
- `UNRESOLVED_BRANCHES`: Initial versus replacement; board versus members; eligibility; fixed term’s compatibility with uninterrupted statutory-agent requirement.
- `SEVEN_LAYER_CLOSURE`: `1 incorporate at high level; 2 materials gap; 3 conditional/materials gap; 4 incorporate—licensed accountable officer; 5 incorporate with prescribed-form gap; 6 materials gap; 7 incorporate—failure to maintain RA may lead to offence/striking off under the stated models.`
- `CONCLUSION`: Do not adapt Appendix 24A: the course supplies the RA rules and records step but no exact appointment precedent, so drafting must stop at a clearly identified form/authority gap.

END SYNTHETIC CANDIDATE B
