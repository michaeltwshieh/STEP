# Section B v2 independent evaluation — Round 0

## Scope and integrity

This is an independent, read-only evaluation of the two locked Section B answer
outputs against `section-b-oracle-v2.json`. No workspace file was edited. The
focused regression cases P05B, P08A and P08B were not scored because the task
instruction identifies them as generic regressions, not direct answer-agent inputs.

All locked hashes verified before evaluation:

| Input | SHA-256 | Status |
|---|---|---|
| Question extract | `07d07ec52ed17dc4d0fe360d297ba8c88d9c48fae9f27c2da7b94cbf68b198a6` | match |
| Reused baseline | `67a7c625c911ff4a6d495f9ff9f72ec11bfefc66952182e81d3e243a0b30c503` | match |
| Candidate A | `5b81857e9a0d110178ea894f0e9db88a7b7aac0c444d0436b3ff57f94c4e7d4e` | match |
| Candidate B | `385efa287c7155467bc9cbb5aad897e83cd2edd36fb181cf623e4bb135fbf555` | match |
| Candidate Content | `ce886f1f510c48094cf118d065dee42e6a0684ca9a8134a79236a5a05a2fc48f` | match |
| Shared routing core | `1c48e4ba391b47dc88acd07eddd078b995510ba7cf88af5d13eb73189aa15d84` | match |
| Candidate Section B adapter | `22bc4fa927f885821cd2af5259331a3631361f26369dddc5e93a53b1b12e25a8` | match |
| Candidate dispatcher (`CLAUDE.md`) | `07ff62d2791faa0692ce9b548f87ee6f75cf94142b0385ddf9bb4a4d738c42a3` | match |
| KAP | `cc9fc7ce0e0b77dae24d1758f9e7ccab7a790a520436e425162bccd9d5659350` | match |
| Corrected v2 oracle | `4f3adcda45c483864296a027d692d1f132903d1e3e08b0eb534380f5696ae8e9` | match |

The oracle freeze record and source extracts were read after the lock. No KAP
wording was used as a model answer; it was used only as a key-points rubric.

## Scoring basis and verdict

The scored denominator is 23 mandatory critical routes: S01 (4), S02 (5), S03
(5), S04 (5), and S05 (4). A strict full hit requires the route's substantive
rule, actor/stage, jurisdiction or branch treatment, and required document or
operative component to be present and correct. Near hits are reported separately
as partial, rather than inflated into recall.

| Candidate | Strict full hits | Partial | Missed | Hard-pass verdict |
|---|---:|---:|---:|---|
| A | 18/23 | 3 | 2 | FAIL |
| B | 19/23 | 2 | 2 | FAIL |

Neither candidate meets the hard-pass requirement of 100%, zero wrong/forbidden
routes, complete branches, and complete agreement on critical document chains.

## Critical-route matrix

| Case | Candidate A | Candidate B | Evaluation |
|---|---|---|---|
| S01 | 2 full, 1 partial, 1 miss | 3 full, 1 miss | Both correctly handle notice/service, quorum/adjournment and the poll outcome. A does not expressly give Article 12.8's operative poll-result effect. Both draft only the winding-up resolution and omit the Appendix 30B liquidator appointment and no-audit business required by the corrected oracle. |
| S02 | 3 full, 2 partial | 2 full, 2 partial, 1 miss | Both identify Article 19.3 sanction and separate member/director written resolutions and both preserve the aviation-registration gap. Both omit the corporate nominee's 25H/25J representative-appointment stage. A selects 25M and expressly excludes the required 25N attachment structure; its draft also lacks a distinct Bill of Sale. B has a useful 25N-like transaction-document set and includes bills of sale within “Purchase Documents”, but does not mark the 25N attachments explicitly. B also says the Bahamas company is not an IBC even though it has one corporate director, a regime/entity contradiction. |
| S03 | 5 full | 5 full | Both cover historical ownership/management separation, Article 19.1 and Quin & Axtens, trustee/board boundaries, director duties, and Articles 15.3–15.4 removal/replacement. Both choose a permitted course jurisdiction and do not turn the trustee into the board. B leaves the Bahamas entity type less explicit but does not apply a conflicting statute in this question. |
| S04 | 4 full, 1 miss | 5 full substantively | A fixes BVI as the governing context despite the oracle's genuinely-unknown-jurisdiction lock and imports S02's $5m/Article 19.3 facts. B properly compares jurisdictional variants and keeps protections conditional. Both nevertheless cite or treat the examination Appendix 1 protection articles as an attached/model source although Q4 supplies no governing articles; B's use is framed more illustratively but remains a namespace/authority defect. B also gives no express remuneration/reward framing. |
| S05 | 4 full | 4 full | Both select creditors' voluntary winding-up, apply the fixed-charge/cost/preferential/unsecured waterfall, treat the promissory-note shareholder loan as ordinary debt, and reconcile $2,605,000 to nil using an adapted Appendix 30G. B adds final-meeting/Registrar language and a claim table; A is closer to the 30G table but does not put final filing language in the draft. |

## Issue and error classes

### Wrong jurisdiction, regime, actor, stage, or precedent

Candidate A:

- S04 is a direct jurisdiction-lock failure. Q4 is genuinely unknown, but A
  starts with and applies BVI law and BVI statutory protection as though selected.
  It also carries the S02 $5m facility and Article 19.3 into an unrelated,
  fact-free essay.
- S02 has an actor/stage gap: the corporate nominee's directors should appoint
  the representative and notify Company (Appendices 25H and 25J) before the
  nominee acts. A only refers to an authorised signatory and includes the
  corporate-director representative.
- S02 has a precedent-selection error under the locked oracle: A's check panel
  says 25N is excluded because its example has two lenders, floating security
  and a priority deed, and selects 25M. The v2 route requires 25N's complex
  transaction/attachment structure as the closer precedent. The substantive
  draft also omits a distinct Bill of Sale.
- A's member resolution gives the sole director authority to approve/execute
  the entire transaction. This blurs the Article 19.3 member sanction with the
  board's Article 19.1/20.5 decision; it is a minor actor-boundary defect because
  a separate director resolution is still supplied.

Candidate B:

- S02 contains the most serious regime error. It expressly says the Bahamas
  company is not an IBC. The course's `Appendix-6B-Types-of-company-available-in-
  selected-jurisdictions.md` says a domestic Bahamian company limited by shares
  must have at least two directors, whereas its Bahamas IBC can have one. B's
  chosen non-IBC regime therefore cannot support the stipulated sole corporate
  director without an unresolved qualification. This is a wrong regime/entity
  lock, not merely a missing citation.
- S02 has the same missing 25H/25J corporate-nominee representative stage. Its
  member resolution also directly authorises the director, secretary, registered
  agent and board-appointed agents to sign and file, unnecessarily mixing the
  member-sanction and board-execution actors.
- S02's substantive transaction-document definitions are close to the required
  25N structure, but the draft does not explicitly identify the 25N precedent or
  mark the Bill of Sale, facility and mortgage as the attached exhibits in the
  25N style. It is scored partial for strict document/precedent completeness.

### Forbidden breaches and authority boundaries

- Candidate A's S04 answer uses the S02 transaction facts and treats Articles
  18.2, 19.3 and 29.1–29.3 of examination Appendix 1 as “supplied articles”.
  Q4 has no governing articles. This is a cross-question fact/namespace breach
  in addition to the wrong-jurisdiction failure.
- Candidate B avoids the S02 fact contamination and preserves conditional
  jurisdiction variants, but its S04 answer still invokes Article 19.4 and
  Articles 29.1–29.2 of an “attached traditional model”. The oracle lock says no
  governing articles are supplied for Q4; those references must be presented as
  course illustrations only or omitted. This is a residual forbidden authority
  boundary breach.
- The optional auditor line in both S01 notices is not scored as forbidden: the
  course Appendix 25E itself contains an auditor placeholder, and both candidates
  condition it on applicable entitlement.

### Material-fact disposition

- S01: both candidates correctly apply 28 August, the 14-clear-day dates,
  recipients A/B/C/D/E, C's 70% holding, the one-person initial quorum failure,
  D/E's show-of-hands result, and C's poll right. Neither explicitly isolates
  the missing-solvency fact and therefore neither preserves the members'/creditors'
  voluntary-winding-up branch in the check output.
- S02: both distinguish Mr AB as beneficial owner, Nominees Ltd as registered
  member, and Directorships Ltd as corporate sole director; both treat FAA/Isle
  of Man transfer and aircraft-security perfection as materials gaps. A omits a
  distinct Bill of Sale; B includes it within Purchase Documents. B's non-IBC
  Bahamas statement conflicts with the sole-director fact.
- S03: both correctly keep Company property and the Midcity account separate from
  the trustee's shareholding and retain independent director duties. Both state
  or preserve the detailed trust-law gap rather than inventing trust law.
- S04: A supplies remuneration framing but mis-disposes the jurisdiction. B
  covers the risk categories and conditional variants but does not expressly
  frame the “reward” side as remuneration.
- S05: both correctly treat Blackacre's $1.7m as fixed-charge proceeds, the
  $700k deficiency as unsecured, the $40k liquidator cost and $55k tax as prior
  payments, all listed claims as pari passu ordinary debt, and the $500k
  promissory-note shareholder loan as a creditor claim. Arithmetic is correct in
  both outputs.

### Requested documents and operative coverage

1. **S01 notice (1.1):** Appendix 25E supplies the notice frame. The corrected
   v2 oracle requires the core Appendix 30B business to be inserted into the
   requested notice: (i) voluntary winding-up, (ii) liquidator appointment, and
   (iii) no-audit resolution. A and B include only (i). Appendix 25A is correctly
   not reproduced; it is check-only.
2. **S02 resolutions (2.2):** Both contain the Article 19.3 member sanction,
   separate sole-director authority, transaction execution, registry-transfer,
   charge-register and records clauses. A's 25M selection and omission of an
   explicit Bill of Sale/25N attachment set are material document-chain losses.
   B's defined Purchase Documents cover bills of sale in substance and its
   closing clauses are fuller, but the member resolution over-allocates execution
   authority and the 25N exhibit structure is not explicit. Neither includes the
   25H/25J corporate nominee representative chain.
3. **S03/S04:** no document is requested for S03. S04 appropriately discusses
   the DSA, management agreement and insurance routes; A's jurisdiction/article
   anchoring is wrong, and B's model-article references require the Q4 gap
   qualification.
4. **S05 final account (5.2):** A is more faithful to Appendix 30G's receipts
   and payments tables. B has complete figures and adds useful balance/claim
   analysis and final filing language, but is less faithful to the precedent's
   table headings. Both give a complete $2.605m-to-nil account on the corrected
   waterfall.

### Unresolved branches and materials gaps

- S01 short-notice consent is conditional in both, but the missing solvency fact
  and members' versus creditors' branch is not expressly recorded by either.
- S02 aviation transfer, aircraft-mortgage perfection and external registry forms
  remain conditional materials gaps in both. A fixes BVI; B fixes Bahamas but
  fixes the wrong non-IBC entity description for the one-director fact. Seal/deed
  alternatives are kept conditional.
- S03 jurisdiction-specific filings/register updates and detailed trust-law
  consequences remain gaps/conditions in both.
- S04 should preserve both jurisdictional exoneration/indemnity and wrongful-
  trading variants. B does so; A collapses them into a BVI answer.
- S05 dates, liquidator particulars and jurisdiction-specific final-account/
  priority filings remain placeholders or conditions in both. No candidate
  improperly uses Appendix 30A for the insolvent route.

### A/B agreement on critical routes and document chains

- **S01:** agreement on all substantive meeting mechanics; shared omission of
  the 30B liquidator/no-audit notice business. B is more explicit on Article 12.8.
- **S02:** agreement on Article 19.3, separate member/board resolutions, charge
  record, execution and aviation-law gap; shared missing 25H/25J stage. They
  diverge on jurisdiction/entity (BVI versus Bahamas non-IBC) and selected
  precedent (A 25M versus B's 25N-like definitions).
- **S03:** substantive route agreement; jurisdictions differ but both are
  course-supported choices for this question and no conflicting jurisdictional
  statute is applied.
- **S04:** agreement on the risk/protection categories; A wrongly selects BVI,
  while B correctly keeps the jurisdiction conditional. Both retain the
  Appendix-1 article-boundary problem.
- **S05:** agreement on CVL, waterfall, shareholder-loan treatment, adapted 30G
  and arithmetic; B is stronger on final filing language, A on 30G layout.

### New errors relative to the reused baseline

The baseline is itself imperfect (notably its BVI choice in genuinely unknown S04
and its missing 25H/25J stage), so repeated defects are not counted as new.

- **Both A and B:** S01 is a regression from the baseline notice because the
  baseline included a liquidator appointment while neither new draft includes it.
  Both also retain the baseline's missing no-audit clause. The shared missing
  25H/25J stage is not new.
- **Candidate A:** the explicit move from the baseline's 25N-style S02
  resolution structure to 25M and the statement that 25N should be excluded are
  new oracle-relative precedent errors. The draft loses the baseline's more
  complete transaction-document definitions and explicit registry/charge
  resolutions, and still lacks a distinct Bill of Sale.
- **Candidate B:** the explicit statement that the Bahamas S02 company is not an
  IBC, while retaining a sole corporate director, is a new wrong-regime error.
  B improves the baseline's transaction-document specificity and final-account
  completion language. Its S04 article-boundary issue is substantially inherited
  from the baseline rather than new.
- Candidate A's S04 wrong-jurisdiction choice is repeated from the baseline, not
  new; Candidate B improves that point. Candidate A preserves the baseline's
  correct BVI choice and account treatment for S05; B's Bahamas choice is allowed
  by the delegated-jurisdiction oracle and is not itself a regression.

## Final verdict

**FAIL — Candidate A:** 18/23 strict mandatory-route hits, with a missed notice
operative chain, missing nominee-representative stage, wrong S02 precedent
selection, and a direct S04 unknown-jurisdiction failure plus cross-question
authority contamination.

**FAIL — Candidate B:** 19/23 strict mandatory-route hits, with the same S01
notice and nominee-representative gaps, a serious S02 Bahamas non-IBC/sole-
director contradiction, residual S04 article-namespace misuse, and less exact
30G formatting. Its generic S04 jurisdiction handling and S02 document content
are stronger than A's, but the hard-pass conditions are not met.

