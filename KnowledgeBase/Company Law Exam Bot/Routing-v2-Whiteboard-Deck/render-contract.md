# Routing v2 Whiteboard Deck - Render Contract

Communication goal: explain, in simple Cantonese, how Routing v2 converts an exam
question into a validated course-grounded answer, how the files work together, and how
deterministic tests improve completeness and source safety.

Format: twenty-two separate 16:9 raster slides, photographed physical dry-erase whiteboard
style, using the same camera, board, reflections and real-marker character throughout.

## Slide 1 - Core idea

- Purpose: establish that Routing v2 inserts a validated plan between question and answer
- Exact title: `Routing v2 做咩？`
- Exact fragments:
  - `問題唔直接變答案`
  - `先做 RoutePlan`
  - `VALID 先輸出`
- Exact takeaway: `可靠答案 = 路線 + 證據 + 閘門`
- Layout: hero claim
- Diagram: question sheet flows into a RoutePlan clipboard, then through a green gate to
  an answer page; a red cross blocks a shortcut arrow from question straight to answer
- Speaker note: the core change is pre-answer structured routing and validation, not a
  new source of law

## Slide 2 - End-to-end flow

- Purpose: show the answer sequence in four compact stages
- Exact title: `一題點樣行完整流程`
- Exact fragments:
  - `1 分類 MCQ / PROSE / DRAFTING`
  - `2 Content 揀來源`
  - `3 RoutePlan 鎖 facts / branches / files`
  - `4 Validator PASS → Adapter`
- Exact takeaway: `先 routing 後 writing`
- Layout: four-stage flow
- Diagram: four hand-drawn cards from left to right, ending in a checked answer page
- Speaker note: the adapter is Section A for MCQs or Section B for prose/drafting

## Slide 3 - RoutePlan anatomy

- Purpose: make the structured controls concrete
- Exact title: `RoutePlan 鎖住啲咩`
- Exact fragments:
  - `6 locks`
  - `facts + claims`
  - `XOR branches`
  - `allowlist + actual_open`
  - `document chain`
- Exact takeaway: `唔畀隱藏假設混入答案`
- Layout: mechanism
- Diagram: a large central RoutePlan sheet with five arrows to locks, fact cards, a fork,
  a file ledger and a linked document chain
- Speaker note: the six locks cover jurisdiction, regime/entity, actor/capacity,
  relationship, lifecycle stage and governing instruments

## Slide 4 - File relationships

- Purpose: explain which file owns which responsibility
- Exact title: `每個 file 點樣合作`
- Exact fragments:
  - `AGENTS + CLAUDE → 任務規則`
  - `Content → source map`
  - `routing-core → RoutePlan`
  - `schema + validator → 閘門`
  - `section-a / section-b → render`
  - `12 Manuals + 90 Appendices → 法律證據`
- Exact takeaway: `一個 file 一個清楚角色`
- Layout: file relationship tree
- Diagram: a top-down hand-drawn dependency tree with rules at the top, source map and
  evidence on the left, routing and validation in the centre, adapters and output on the
  right
- Speaker note: manuals and appendices are substantive evidence; routing files are
  workflow instructions and cannot prove legal propositions by themselves

## Slide 5 - Tests and safeguards

- Purpose: show the concrete methods used to catch routing and isolation defects
- Exact title: `點樣 test 同守住質素`
- Exact fragments:
  - `21 clean / fail fixtures`
  - `XOR + counts + authority checks`
  - `Seatbelt sandbox`
  - `hash lock 後先見 gold`
  - `2 個 independent candidates`
- Exact takeaway: `捉到 critical fail 就唔准 render`
- Layout: risk and safeguard
- Diagram: red bug and warning symbols enter a blue validator shield; green checks emerge
  for source access, document completeness and branch isolation
- Speaker note: targeted failures include missing notice operatives, Bill of Sale,
  charge-register entry, corporate authority, unresolved branches and forbidden opens

## Slide 6 - Output improvement

- Purpose: close with the practical improvement to answer quality
- Exact title: `最後 output 點解會更好`
- Exact left-side fragments:
  - `靠記憶 routing`
  - `易漏 second module`
  - `drafting 少 clause`
  - `source contamination`
- Exact right-side fragments:
  - `雙重 routing pass`
  - `精確 file ledger`
  - `component counts`
  - `VALID trace`
- Exact takeaway: `更完整  更可查  更少亂估`
- Layout: before/after
- Diagram: red messy answer page on the left transforms through a RoutePlan gate into a
  green checked answer page on the right
- Speaker note: Routing v2 improves process reliability but remains a test candidate,
  not a GO decision or proof of real-exam accuracy

## Slide 7 - Two paths

- Purpose: show the ordinary-bot and Routing-v2 paths in one glance
- Exact title: `兩種做法 一眼睇晒`
- Exact left-side fragments:
  - `普通 bot`
  - `問題 → 搵資料 → 寫答案`
- Exact right-side fragments:
  - `Routing v2 bot`
  - `問題 → RoutePlan → VALID → 答案`
- Exact takeaway: `多一步 planning  少幾步補鑊`
- Layout: before/after choice
- Diagram: the same question card splits into a short red direct path and a longer green
  planned path with a blue clipboard and validation gate
- Speaker note: the extra planning step is deliberate; it blocks unsupported shortcuts

## Slide 8 - Source discipline

- Purpose: explain source selection and traceability without technical detail
- Exact title: `Source 使用有咩分別`
- Exact left-side fragments:
  - `普通 bot`
  - `見到相關就可能開`
  - `之後先講用咗咩`
- Exact right-side fragments:
  - `Routing v2`
  - `先 freeze allowlist`
  - `actual_open 全部留痕`
- Exact takeaway: `知道開咗咩  知道排除咩`
- Layout: before/after choice
- Diagram: an untidy open file pile on the left versus a locked file tray and checked
  ledger on the right
- Speaker note: the allowlist is frozen before substantive retrieval and actual opens
  are reconciled against it

## Slide 9 - Drafting discipline

- Purpose: show why document drafting is less likely to omit a legal step or component
- Exact title: `Drafting 有咩分別`
- Exact left-side fragments:
  - `普通 bot`
  - `一份 resolution 包晒`
  - `可能漏 clause / attachment`
- Exact right-side fragments:
  - `Routing v2`
  - `actor → authority → document`
  - `counts → execution → filing`
- Exact takeaway: `每個 component 都要對數`
- Layout: risk and safeguard
- Diagram: one overloaded broken resolution on the left versus a linked document chain
  with separate authority, document, attachment and filing icons on the right
- Speaker note: the requested-document chain reconciles actors, upstream authority,
  counts, attachments, execution and records/filings

## Slide 10 - Simplest explanation

- Purpose: give the presenter one memorable closing explanation
- Exact title: `最簡單嘅講法`
- Exact fragments:
  - `同一條問題`
  - `同一套 course materials`
  - `普通 bot = 直接作答`
  - `Routing v2 = 先規劃 再驗證`
- Exact takeaway: `唔係多咗法律  係少咗漏步驟`
- Layout: mechanism with a fork and recombination
- Diagram: one question and one stack of course books feed two paths; the direct path has
  a warning mark while the planned path passes a RoutePlan clipboard and green gate
- Speaker note: Routing v2 changes the control process, not the governing course law

## Slide 11 - Frozen allowlist

- Purpose: explain the allowlist through the guest-list analogy
- Exact title: `Freeze allowlist = 先鎖名單`
- Exact fragments:
  - `先列出可以開嘅 files`
  - `每項有 path / namespace / role`
  - `計 hash 後 freeze`
- Exact takeaway: `之後唔可以偷偷加 file`
- Layout: mechanism
- Diagram: a bouncer clipboard lists approved blank file cards, receives a wax-style hash
  stamp, and closes behind a padlock before any file door opens
- Speaker note: freezing occurs before substantive retrieval and the validator recomputes
  the allowlist hash

## Slide 12 - Actual-open ledger

- Purpose: distinguish planned permission from actual access
- Exact title: `actual_open = 實際入場紀錄`
- Exact fragments:
  - `開一個 file 就記一行`
  - `path + role + SHA-256`
  - `未開過就唔可以當證據`
- Exact takeaway: `計劃名單 ≠ 實際紀錄`
- Layout: mechanism
- Diagram: approved file cards pass a door scanner; each entry creates one row in a
  green ledger with a fingerprint-like hash doodle
- Speaker note: an actual-open row carries the exact relative path, namespace, role and
  observed file hash

## Slide 13 - Reconciliation

- Purpose: explain the validator's relationship between allowlist and actual opens
- Exact title: `兩張表點樣對數`
- Exact fragments:
  - `actual_open ⊆ allowlist`
  - `role 必須一致`
  - `incorporated route 必須真係開過`
- Exact takeaway: `名單外開 file = critical fail`
- Layout: simple equation
- Diagram: blue allowlist clipboard on the left and green actual-open ledger on the right
  feed a balance scale; an extra red file outside the list is stopped
- Speaker note: the validator rejects out-of-list opens, role mismatches and incorporated
  routes without an actual-open record

## Slide 14 - First three locks

- Purpose: explain the first half of the six locks in plain language
- Exact title: `6 locks 前三把`
- Exact fragments:
  - `1 jurisdiction → 邊個司法區`
  - `2 regime / entity → 邊種公司`
  - `3 actor / capacity → 邊個用咩身份`
- Exact takeaway: `先答清楚  邊度  邊種  邊個`
- Layout: three-stage flow
- Diagram: three large padlocks contain a map pin, company silhouette and person badge
- Speaker note: each lock stores a state, value, deciding fact IDs and alternatives

## Slide 15 - Last three locks

- Purpose: explain the second half of the six locks in plain language
- Exact title: `6 locks 後三把`
- Exact fragments:
  - `4 relationship → 雙方咩關係`
  - `5 lifecycle stage → 行到邊一步`
  - `6 governing instruments → 邊套 law / articles`
- Exact takeaway: `唔好混 regime / stage / rules`
- Layout: three-stage flow
- Diagram: three padlocks contain a handshake, progress path and law-book/articles pair
- Speaker note: these locks prevent the right topic being applied to the wrong
  relationship, stage or governing instrument

## Slide 16 - XOR branches

- Purpose: explain exclusive branch selection and unresolved facts
- Exact title: `XOR = 只可以揀一條`
- Exact fragments:
  - `A route`
  - `B route`
  - `有 deciding fact → 揀一條`
  - `缺 deciding fact → 兩條 conditional`
- Exact takeaway: `唔知道就唔硬揀`
- Layout: mechanism with a fork
- Diagram: one route fork has a green selected branch when a fact card is present; a
  second fork with a question-mark card leaves both branches amber and conditional
- Speaker note: selected means exactly one incorporated route; unresolved means no
  selected route and both alternatives remain conditional

## Slide 17 - Worked branch example

- Purpose: demonstrate unresolved XOR behavior with a simple share-transfer decision
- Exact title: `例子：董事會未有決定`
- Exact fragments:
  - `transfer form → 必須`
  - `批准 route`
  - `拒絕 route`
  - `board decision = missing`
- Exact takeaway: `結果：兩條 route 都 conditional`
- Layout: mechanism
- Diagram: a mandatory transfer form feeds a fork into approve and refuse document
  chains; a missing-decision card prevents either branch receiving a green check
- Speaker note: once an actual decision fact is supplied, exactly one branch may be
  selected and incorporated

## Slide 18 - Hash basics

- Purpose: explain hash as a deterministic digital fingerprint rather than encryption
- Exact title: `Hash = 數碼指紋`
- Exact fragments:
  - `同內容 → 同 hash`
  - `改一個字 → hash 全變`
  - `由 hash 唔會還原內容`
- Exact takeaway: `Hash 只證明內容有否改變`
- Layout: mechanism
- Diagram: one document produces the same fingerprint twice; a one-character edit
  produces a visually different fingerprint string; a one-way arrow blocks reversal
- Speaker note: SHA-256 is deterministic and change-sensitive, but does not identify the
  changed field or reveal the source content

## Slide 19 - Why secret file additions matter

- Purpose: show why changing the evidence boundary after seeing an answer direction is
  a fundamental test and reasoning failure
- Exact title: `偷偷加 file 點解嚴重`
- Exact fragments:
  - `先見答案方向`
  - `後加支持自己嘅 evidence`
  - `source boundary 被改寫`
  - `blind test 即刻失效`
- Exact takeaway: `由 routing 變成追答案`
- Layout: risk and safeguard
- Diagram: a normal question-to-source-to-answer line bends backward into a red feedback
  loop that cherry-picks an extra file after the answer direction is visible
- Speaker note: the problem is outcome-driven source selection, not merely one extra file

## Slide 20 - Hash mismatch

- Purpose: show the exact before/after detection mechanism
- Exact title: `Hash 點樣捉到改名單`
- Exact fragments:
  - `freeze 前 hash = A`
  - `偷偷加一個 file`
  - `重新計 hash = B`
- Exact takeaway: `A ≠ B → Validator FAIL`
- Layout: simple equation
- Diagram: a sealed allowlist with fingerprint A receives one red extra file and becomes
  fingerprint B; a large not-equal sign leads to a red validator stop gate
- Speaker note: the validator recomputes canonical allowlist SHA-256 and compares it with
  the frozen value

## Slide 21 - Three hash layers

- Purpose: distinguish the identities protected at three different stages
- Exact title: `Routing v2 有三層 hash`
- Exact fragments:
  - `allowlist hash → 名單版本`
  - `file hash → 內容版本`
  - `answer hash → output 版本`
- Exact takeaway: `名單  內容  output 都可核對`
- Layout: three-stage flow
- Diagram: three linked fingerprint cards protect a guest list, source document and
  answer page respectively
- Speaker note: each layer answers a different question and cannot substitute for the
  others

## Slide 22 - Hash limits

- Purpose: explain that hash is tamper evidence rather than access control
- Exact title: `Hash 唔係保安本身`
- Exact fragments:
  - `hash ≠ encryption`
  - `hash ≠ access control`
  - `sandbox 真正守門`
  - `validator 負責對數`
- Exact takeaway: `Hash + Sandbox + Validator 先完整`
- Layout: mechanism
- Diagram: hash seal, security guard/sandbox gate and validator checklist interlock as
  three puzzle pieces around a protected answer
- Speaker note: a party able to change both the data and stored hash can recompute it;
  retained reports, enforced ordering and sandbox isolation complete the control
