# Routing v2 Whiteboard Deck - Prompt Manifest

Generation path: built-in ImageGen, one 16:9 raster slide per call.

Style references used on every generation:

1. `/Users/michaelshieh/.codex/skills/ms-whiteboard-slide-decks/assets/whiteboard-style-anchor.png`
2. `/Users/michaelshieh/.codex/skills/ms-whiteboard-slide-decks/assets/marker-stroke-anchor.png`

Shared prompt rules: photographed warm off-white physical dry-erase board; nearly
straight-on camera; slim dark rails; soft broken fluorescent reflections in the upper
8–15%; faint erased-marker ghosts and cleaning streaks; broad 3–5 mm dry-erase marker;
10–25% natural stroke variation; darker starts, overlaps and corners; dry lift-offs and
felt-fiber streaks; black/blue/green/red semantic palette; no digital fonts, flat fills,
watermarks, logos, UI, people or copied calibration content. Every visible string is
quoted verbatim and no visible string may end in `.` or `。`.

## Slide 1

- Claim: a validated RoutePlan sits between question and answer
- Layout: hero flow with rejected shortcut
- Text: `Routing v2 做咩？` / `問題唔直接變答案` / `先做 RoutePlan` /
  `VALID 先輸出` / `可靠答案 = 路線 + 證據 + 閘門`
- Final repair: erased an extra duplicate `RoutePlan` from inside the clipboard

## Slide 2

- Claim: every answer follows the same classified and validated sequence
- Layout: four-stage left-to-right flow
- Text: `一題點樣行完整流程` / `1 分類 MCQ / PROSE / DRAFTING` /
  `2 Content 揀來源` / `3 RoutePlan 鎖 facts / branches / files` /
  `4 Validator PASS → Adapter` / `先 routing 後 writing`

## Slide 3

- Claim: RoutePlan makes hidden assumptions explicit
- Layout: central mechanism with five satellites
- Text: `RoutePlan 鎖住啲咩` / `6 locks` / `facts + claims` / `XOR branches` /
  `allowlist + actual_open` / `document chain` / `唔畀隱藏假設混入答案`

## Slide 4

- Claim: each file owns one responsibility in the pipeline
- Layout: dependency tree from rules and evidence to validated adapters
- Text: `每個 file 點樣合作` / `AGENTS + CLAUDE → 任務規則` /
  `Content → source map` / `routing-core → RoutePlan` /
  `schema + validator → 閘門` / `section-a / section-b → render` /
  `12 Manuals + 90 Appendices → 法律證據` / `一個 file 一個清楚角色`

## Slide 5

- Claim: deterministic and isolated tests stop critical defects
- Layout: risk-and-safeguard shield
- Text: `點樣 test 同守住質素` / `21 clean / fail fixtures` /
  `XOR + counts + authority checks` / `Seatbelt sandbox` /
  `hash lock 後先見 gold` / `2 個 independent candidates` /
  `捉到 critical fail 就唔准 render`
- Final repair: erased five invented `TEST 1:` to `TEST 5:` labels

## Slide 6

- Claim: validated routing produces a more complete and traceable answer
- Layout: before/after transformation
- Text: `最後 output 點解會更好` / `靠記憶 routing` / `易漏 second module` /
  `drafting 少 clause` / `source contamination` / `雙重 routing pass` /
  `精確 file ledger` / `component counts` / `VALID trace` /
  `更完整  更可查  更少亂估`

## Slide 7

- Claim: the ordinary bot takes a direct route while Routing v2 inserts planning and
  validation
- Layout: two paths from one question
- Text: `兩種做法 一眼睇晒` / `普通 bot` / `問題 → 搵資料 → 寫答案` /
  `Routing v2 bot` / `問題 → RoutePlan → VALID → 答案` /
  `多一步 planning  少幾步補鑊`
- Final repair: consolidated three separated lower-path labels into the exact continuous
  Routing v2 path string

## Slide 8

- Claim: Routing v2 freezes source access first and leaves a complete open ledger
- Layout: loose file pile versus locked tray and checked ledger
- Text: `Source 使用有咩分別` / `普通 bot` / `見到相關就可能開` /
  `之後先講用咗咩` / `Routing v2` / `先 freeze allowlist` /
  `actual_open 全部留痕` / `知道開咗咩  知道排除咩`
- Final repair: replaced a repeatedly misrendered Cantonese `冇` phrase with the simpler
  exact wording `知道開咗咩  知道排除咩`

## Slide 9

- Claim: Routing v2 checks a complete drafting chain instead of compressing everything
  into one resolution
- Layout: overloaded broken resolution versus distinct linked document stages
- Text: `Drafting 有咩分別` / `普通 bot` / `一份 resolution 包晒` /
  `可能漏 clause / attachment` / `Routing v2` /
  `actor → authority → document` / `counts → execution → filing` /
  `每個 component 都要對數`

## Slide 10

- Claim: Routing v2 changes the control process, not the course law
- Layout: shared question and materials feeding direct versus validated paths
- Text: `最簡單嘅講法` / `同一條問題` / `同一套 course materials` /
  `普通 bot = 直接作答` / `Routing v2 = 先規劃 再驗證` /
  `唔係多咗法律  係少咗漏步驟`

## Slide 11

- Claim: freeze allowlist is the approved source guest list locked before retrieval
- Layout: approved file cards, hash stamp and padlocked clipboard
- Text: `Freeze allowlist = 先鎖名單` / `先列出可以開嘅 files` /
  `每項有 path / namespace / role` / `計 hash 後 freeze` /
  `之後唔可以偷偷加 file`

## Slide 12

- Claim: actual_open records the sources that were truly accessed
- Layout: file scanner creating ledger rows and hashes
- Text: `actual_open = 實際入場紀錄` / `開一個 file 就記一行` /
  `path + role + SHA-256` / `未開過就唔可以當證據` /
  `計劃名單 ≠ 實際紀錄`
- Final repair: replaced the repeatedly misrendered `冇開過` phrase with the equivalent
  exact wording `未開過就唔可以當證據`

## Slide 13

- Claim: validator reconciles planned and actual source access
- Layout: allowlist and actual ledger feeding a balance check
- Text: `兩張表點樣對數` / `actual_open ⊆ allowlist` / `role 必須一致` /
  `incorporated route 必須真係開過` / `名單外開 file = critical fail`
- Final repair: erased invented `RULE 1:` to `RULE 3:` and `TAKEAWAY:` prefixes

## Slide 14

- Claim: first three locks establish where, what entity and who is acting
- Layout: three padlocks with map, company and identity icons
- Text: `6 locks 前三把` / `1 jurisdiction → 邊個司法區` /
  `2 regime / entity → 邊種公司` / `3 actor / capacity → 邊個用咩身份` /
  `先答清楚  邊度  邊種  邊個`

## Slide 15

- Claim: last three locks establish relationship, stage and governing instruments
- Layout: three padlocks with handshake, progress path and law/articles icons
- Text: `6 locks 後三把` / `4 relationship → 雙方咩關係` /
  `5 lifecycle stage → 行到邊一步` /
  `6 governing instruments → 邊套 law / articles` /
  `唔好混 regime / stage / rules`

## Slide 16

- Claim: XOR selects one route only when a deciding fact exists
- Layout: selected fork versus two unresolved conditional branches
- Text: `XOR = 只可以揀一條` / `A route` / `B route` /
  `有 deciding fact → 揀一條` / `缺 deciding fact → 兩條 conditional` /
  `唔知道就唔硬揀`
- Final repair: erased duplicate A/B labels from the unresolved fork

## Slide 17

- Claim: missing board decision leaves approval and refusal routes conditional
- Layout: mandatory transfer form feeding an unresolved branch fork
- Text: `例子：董事會未有決定` / `transfer form → 必須` / `批准 route` /
  `拒絕 route` / `board decision = missing` /
  `結果：兩條 route 都 conditional`

## Slide 18

- Claim: hash is a deterministic, change-sensitive digital fingerprint
- Layout: same content, changed content and blocked reverse path
- Text: `Hash = 數碼指紋` / `同內容 → 同 hash` / `改一個字 → hash 全變` /
  `由 hash 唔會還原內容` / `Hash 只證明內容有否改變`

## Slide 19

- Claim: secretly adding a file after seeing the answer direction turns routing into
  outcome-driven evidence selection
- Layout: proper question/source/answer flow corrupted by a red feedback loop
- Text: `偷偷加 file 點解嚴重` / `先見答案方向` /
  `後加支持自己嘅 evidence` / `source boundary 被改寫` /
  `blind test 即刻失效` / `由 routing 變成追答案`

## Slide 20

- Claim: adding one file changes frozen allowlist hash A into hash B
- Layout: sealed list A, red extra file, altered list B and validator stop gate
- Text: `Hash 點樣捉到改名單` / `freeze 前 hash = A` / `偷偷加一個 file` /
  `重新計 hash = B` / `A ≠ B → Validator FAIL`

## Slide 21

- Claim: allowlist, source content and answer output require separate hash layers
- Layout: three fingerprint cards protecting list, file and answer
- Text: `Routing v2 有三層 hash` / `allowlist hash → 名單版本` /
  `file hash → 內容版本` / `answer hash → output 版本` /
  `名單  內容  output 都可核對`

## Slide 22

- Claim: hash is tamper evidence and must be combined with access control and validation
- Layout: three interlocking puzzle pieces around a protected answer
- Text: `Hash 唔係保安本身` / `hash ≠ encryption` /
  `hash ≠ access control` / `sandbox 真正守門` / `validator 負責對數` /
  `Hash + Sandbox + Validator 先完整`
- Final repair: erased invented TITLE/TEXT/TAKEAWAY prefixes and quotation marks

## Factual basis and notes

- Workflow relationship: standalone Routing v2 package `AGENTS.md`, `CLAUDE.md`,
  `Content.md`, `routing-core.md`, schema, validator and Section A/B adapters
- Legal evidence inventory: 12 course manuals and 90 appendices
- Deterministic fixture inventory: 21 clean/failing RoutePlan fixtures
- Safeguards: exact route/claim dispositions, six locks, XOR isolation, source
  allowlist/actual-open reconciliation, document-component counts, corporate authority,
  Seatbelt filesystem isolation, answer hash locking and delayed evaluator release
- Status caveat: Routing v2 remains a tested candidate rather than an activated GO
