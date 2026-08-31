# Routing-v2 Round 4 Focused Repair — Candidate A

## Frozen pre-open allowlist (set before substantive retrieval)

Question fixture permitted: `routing-v2/corpus/mcq-20-questions.json` (MCQ17 only).

Candidate workflow permitted: `routing-v2/candidate/CLAUDE.md`,
`routing-v2/candidate/Content.md`, `routing-v2/candidate/routing-core.md`, and
`routing-v2/candidate/section-a.md`. The root `CLAUDE.md` and root `Content.md`
were mandatory pre-flight instructions, read before the substantive-source freeze.

Course sources permitted to open for MCQ17:

- **OPEN:** `Course-Manual-Module-12-Termination-of-Companies.md`, §§3.1–3.1.2 and §6.2 (and no other module was needed for an outcome-changing proposition).
- **OPEN:** `Appendix-30A-Directors-declaration-of-solvency.md` and `Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md`, to verify the selected members’ voluntary winding-up route named in option C.
- **DO NOT OPEN:** `Appendix-31A-Directors-resolution-to-apply-for-voluntary-striking-off.md`, `Appendix-31B-Application-for-voluntary-striking-off-example-of.md`, `Appendix-31C-Statutory-declaration-of-compliance-in-support-of-voluntary.md`, and `Appendix-31D-Application-for-administrative-reinstatement-to-register.md` (distractor appendices).
- **DO NOT OPEN:** all other course appendices/modules, unless an outcome-changing materials gap is established under the candidate workflow.

The allowlist was frozen before substantive course-file retrieval. No gold, report,
answer, specimen, peer, or evaluation file was permitted.

## Input and locks

Fixture record (transcribed from `routing-v2/corpus/mcq-20-questions.json`, MCQ17,
lines 255–267):

> **Stem:** A solvent company has assets to realise and liabilities to pay before surplus can be returned to members. Which route may properly be initiated to terminate it?
>
> **Polarity:** correct; qualifier: **may**.
>
> **A:** Voluntary striking off under Appendix 31A plus the jurisdictionally applicable Appendix 31B or 31C.
>
> **B:** Administrative reinstatement under Appendix 31D.
>
> **C:** Members' voluntary winding-up beginning with Appendices 30A and 30B and continuing through the applicable notices/final-account chain.
>
> **D:** Compulsory winding-up solely because the members no longer want the company.

Locks: jurisdiction/regime and actual constitution are **genuinely unknown**; the
question nevertheless supplies solvency and the non-zero state. The legal actors are
the company, its directors, its members and the liquidator. The lifecycle stage is
pre-commencement termination, with assets and liabilities still to be collected and
paid. The downstream notice, filing and final-account details are therefore
jurisdiction-dependent, as option C expressly recognises.

## Independent passes and claim dispositions

Legal-relationship pass: members decide whether the solvent company should enter
voluntary winding-up; directors first make the solvency inquiry/declaration; a
liquidator then collects assets, pays debts and completes the winding-up.

Transaction-lifecycle pass: solvency inquiry/declaration — **triggered**; members’
decision and liquidator appointment — **triggered**; applicable notices, meetings,
accounts and dissolution filing — **triggered after commencement, but jurisdiction-
dependent**; zero-state striking-off conditions — **not triggered** because assets and
liabilities remain; reinstatement — **not triggered**; compulsory court route —
**not triggered by the supplied facts**.

| Claim | Jurisdiction / actor / stage / qualifier | Verdict | Reason |
|---|---|---|---|
| A | Unspecified jurisdiction; board application plus jurisdiction-specific striking-off filing; termination; **may** | **Refuted** | Module 12 §6.2 says voluntary striking off is for the company’s “zero state”: no assets, debts/liabilities or outstanding claims, no pending proceedings/insolvency matters and no business. The stated assets and liabilities defeat that condition. The route’s named distractor appendices were not opened. |
| B | Unspecified jurisdiction; administrative restoration/reinstatement; post-removal stage; **may** | **Refuted** | Reinstatement moves a removed company back onto the register; it is not a route initiated to terminate a company. The candidate Content appendix decision map classifies this as a reinstatement route. The named distractor appendix was not opened. |
| C | Unspecified jurisdiction; directors then members/liquidator; solvent voluntary winding-up; **may** | **Supported** | Module 12 §§3.1–3.1.2 identify the members’ decision that the company is no longer required and that assets, after debts/liabilities, be distributed to members as a ground for members’ voluntary winding-up. The usual sequence begins with the directors’ declaration of solvency, then the members’ special resolution and liquidator appointment, followed by the applicable notices, meetings, accounts and dissolution steps. |
| D | Unspecified jurisdiction; compulsory/court route; termination; **solely** | **Refuted** | The supplied reason — members no longer want the company — is expressly a voluntary-winding-up ground in Module 12 §3.1.1, not a stated compulsory trigger. On these facts the solvent voluntary route is available; no compulsory route is established solely by member preference. |

## Answer

**Answer:** **C** — Members' voluntary winding-up beginning with Appendices 30A and
30B and continuing through the applicable notices/final-account chain.

**Polarity:** **correct**. “May” asks which route is properly available to initiate
termination on these facts, not which route is mandatory in every jurisdiction.

**Why:** The company is solvent but not in the zero state: it still has assets to
realise and liabilities to pay. Module 12 §3.1.1–§3.1.2 therefore supports members’
voluntary winding-up, beginning with a genuine declaration of solvency and then the
members’ resolution/liquidator appointment. Appendix 30A contains the solvency
declaration and attached assets/liabilities statement; Appendix 30B contains the
members’ voluntary-winding-up resolution and liquidator appointment. Later notices,
meetings, final account and dissolution steps remain subject to the applicable
jurisdictional procedure.

**Closest two:** **A and C** — the outcome-changing distinction is the company’s
state. Voluntary striking off requires a zero-state company with no assets or
liabilities; the facts instead require liquidation so assets can be realised and
debts paid before surplus is returned.

**Sources used:**

- `Course-Manual-Module-12-Termination-of-Companies.md`, §§3.1–3.1.2 and §6.2.
- `Appendix-30A-Directors-declaration-of-solvency.md`.
- `Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md`.

**Cross-check:** `routing-v2/candidate/Content.md`, Appendix decision map (30A–30B
versus the striking-off and reinstatement route labels), was incorporated to confirm
the document-stage distinction. No second substantive course module could change the
letter: §3.1.1–§3.1.2 supplies the positive solvent route and §6.2 supplies the
outcome-changing zero-state contrast. The striking-off and reinstatement routes were
discarded without opening their appendices.

**Confidence:** **High (9/10)**. Exact governing passages determine C and directly
refute the closest distractor; only the later jurisdiction-specific chain is
conditional because the question does not identify the jurisdiction or constitution.

## Route trace

| Route | Source/passage | Contribution | Verdict | Answer location |
|---|---|---|---|---|
| Solvent members’ voluntary winding-up | Module 12 §§3.1.1–3.1.2 | Ground, solvency declaration, members’ resolution/liquidator and completion sequence | Incorporated | Answer / Why / C |
| Selected commencement instruments | Appendices 30A–30B | Verify declaration of solvency and members’ resolution/liquidator appointment | Incorporated | Answer / Why |
| Voluntary striking off | Module 12 §6.2; candidate Content appendix-decision distinction | Zero-state preconditions; facts fail because assets/liabilities remain | Discarded/refuted | Option A / Closest two |
| Administrative reinstatement | Candidate Content appendix-decision distinction | Restoration is opposite lifecycle direction to termination | Discarded/refuted | Option B |
| Compulsory winding-up | Question facts plus Module 12 §3.1.1 positive voluntary ground | No stated compulsory trigger; member preference supports voluntary route | Discarded/refuted | Option D |

## Exact-open attestation

Files actually opened, reconciled to the frozen plan:

1. Mandatory pre-flight/workflow files: root `CLAUDE.md`, root `Content.md`,
   `routing-v2/candidate/CLAUDE.md`, `routing-v2/candidate/Content.md`,
   `routing-v2/candidate/routing-core.md`, and `routing-v2/candidate/section-a.md`.
2. Permitted input fixture: `routing-v2/corpus/mcq-20-questions.json` (MCQ17 only).
3. Permitted substantive course files: `Course-Manual-Module-12-Termination-of-Companies.md`,
   `Appendix-30A-Directors-declaration-of-solvency.md`, and
   `Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md`.

Every substantive file opened appears in the frozen **OPEN** list. None of the four
frozen **DO NOT OPEN** distractor appendices was opened, and no gold, report, answer,
specimen, peer or evaluation file was opened. The MCQ document terminology was treated
as an MCQ claim; no Section B drafting workflow was activated.
