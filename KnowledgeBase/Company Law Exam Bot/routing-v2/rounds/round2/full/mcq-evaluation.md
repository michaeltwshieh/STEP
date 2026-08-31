# Independent Repair Round 2 — Full Section A Evaluation

Date: 2026-08-30  
Scope: frozen synthetic MCQ corpus only; no official-paper accuracy claim.

## Integrity / hash verification

The following SHA-256 values were recomputed and match `routing-v2/rounds/round2/full/hash-lock.md`:

| Input | Recomputed SHA-256 | Lock result |
|---|---|---|
| Full Section A Candidate A | `0719f4795e6ad5c3129c2caaad7acc6e0ad95d0b2b136705f0d1aa8733544c8c` | match |
| Full Section A Candidate B | `813b10fb74f5202eba77a8a6b8eef78ae1a845b8eb71f8606883aee6c2d8eb59` | match |
| MCQ fixture | `2fdbc426e31d9d924d5f131033946537ab30d67c0a857de318eb93147d096be1` | match |
| MCQ gold | `b3e5f2a07ba732bc231b06b58df0e39a5fda7b977bca1a47323e81d01047b807` | match |

The frozen record confirms 20 questions / 10 minimal pairs, balanced A/B/C/D (5 each), synthetic-only status, and the same fixture/gold hashes. Candidate workflow files read were `routing-v2/candidate/CLAUDE.md`, `Content.md`, `routing-core.md`, and `section-a.md`; `Syllabus.md` and the cited course modules/appendices were used for source checks.

## Scores

| Metric | Candidate A | Candidate B | Evidence / notes |
|---|---:|---:|---|
| Letters | **20/20** | **20/20** | Every committed letter matches frozen gold. |
| Option dispositions | **77/80** | **78/80** | A mismatches gold at MCQ04-D, MCQ14-A, MCQ19-B; B mismatches MCQ02-B and MCQ04-D. Each is labelled `refuted` where gold requires `partly true but not best`. |
| Governing passages | **20/20** | **19/20 strict; 20/20 substantive** | A cites the frozen governing source set for all 20. B substantively has the exact M6 §5.2 + Appendix 18E route for MCQ04 but omits the frozen must-open Appendix 1B arts.8.6–8.8 citation. |
| Wrong locks | **0** | **0** | No jurisdiction/regime, actor/capacity, transaction, lifecycle-stage, or governing-article lock is reversed. |
| Strict forbidden routes | **5 violating question-units / 15 clean** | **15 violating question-units / 5 clean** | Literal frozen `must_not_open` filename hits in each item’s source list/text. A hits MCQ02 (20B), MCQ06 (26), MCQ09 and MCQ10 (21G), MCQ18 (31B). B hits MCQ01 (20E/20B/20D), MCQ02 (19A/19B), MCQ03 (18E/26/16C), MCQ04 (26/18B), MCQ06 (26), MCQ09 and MCQ10 (21G), MCQ11 (10A/10B/10C/13A/31D), MCQ12 (12/13A/31D), MCQ15 (25H/25J), MCQ16 (24A/24C), MCQ17 (31A/31D), MCQ18 (31B/31D), MCQ19 and MCQ20 (18A). Total literal filename hits: A **5**, B **31**. Conditional-context caveat: MCQ10’s 21G is valid only after verifying Appendix 1C art.4 (both candidates do); MCQ18’s 31B/31C are alternatives, not to be combined. |
| Closest pair + distinction | **18/20** | **18/20** | A misses frozen pair at MCQ03 (D/A vs B/D) and MCQ06 (A/D vs A/C). B misses MCQ02 (A/C vs B/C) and MCQ15 (B/D vs A/B). Remaining pair sets and distinctions track gold. |
| Confidence | **20/20 band-valid** | **20/20 band-valid** | All 20 are `high` with 8–10 scores; MCQ20 expressly preserves the incomplete-27B gap. Numeric exact matches: A 15/20, B 4/20; this is not treated as a failure because `section-a.md` defines high as 8–10 and gold’s expected values are reference calibration. |
| A/B agreement | **20/20 letters** | **20/20 letters** | The lanes agree on all committed letters. Supplemental agreement: 78/80 option dispositions; 16/20 closest-pair sets. |

## Per-item letter / pair audit

| Q | Gold | A | B | Gold closest pair | A pair | B pair |
|---|---|---|---|---|---|---|
| 01 | A | A | A | A/B | A/B | A/B |
| 02 | C | C | C | B/C | B/C | A/C |
| 03 | D | D | D | B/D | A/D | B/D |
| 04 | B | B | B | B/D | B/D | B/D |
| 05 | C | C | C | A/C | A/C | A/C |
| 06 | A | A | A | A/C | A/D | A/C |
| 07 | A | A | A | A/D | A/D | A/D |
| 08 | D | D | D | A/D | A/D | A/D |
| 09 | B | B | B | B/C | B/C | B/C |
| 10 | C | C | C | B/C | B/C | B/C |
| 11 | D | D | D | B/D | B/D | B/D |
| 12 | B | B | B | B/D | B/D | B/D |
| 13 | A | A | A | A/C | A/C | A/C |
| 14 | C | C | C | A/C | A/C | A/C |
| 15 | B | B | B | A/B | A/B | B/D |
| 16 | D | D | D | B/D | B/D | B/D |
| 17 | C | C | C | A/C | A/C | A/C |
| 18 | A | A | A | A/C | A/C | A/C |
| 19 | D | D | D | B/D | B/D | B/D |
| 20 | B | B | B | B/D | B/D | B/D |

## Materials / source observations

- The decisive source checks are consistent with the frozen gold: traditional dividend route (M6 §6.1 / M10 §5.7 / Appendix 1B art.23.1); BVI distribution route (M6 §7.3 / M10 §5.8 / Appendix 20E); transfer/transmission and beneficial-only distinctions (M6 §5.1–5.2 / M10 §5.3 / Appendices 18A, 18B, 18E, 26–27); capacity versus director authority (M5 §2.4 / M8 §1.3); article-80 versus modern reserve power (M7 §2.2 / Appendices 1B, 1C, 21G); office move versus migration (M5 §3.2 / M10 §5.4 / M4 §2 / Appendices 10A–10C, 12); allotment versus issue (M6 §1.2.2 / M10 §5.9 / Appendix 16C); secretary versus corporate representative (M9 §§1.2–1.4 / M10 §§2.4, 2.7 / Appendices 24A, 24C, 25H, 25J); winding-up versus zero-state striking off (M12 §§3.1, 6.2 / Appendices 30A–30G, 31A–31C); and bilateral 27A versus incomplete unilateral 27B.
- MCQ20 is correctly treated as answerable for the letter but incomplete for any purported complete verbatim declaration; neither candidate invents the omitted 27B language.
- The strict-forbidden line is intentionally literal and conservative. The context caveats above identify where a filename is mentioned as a rejected comparator or as an explicitly conditional alternative; under a semantic-only “incorporated route” reading, the hard contamination count would be lower, but the source lists still over-open the frozen forbidden set.

