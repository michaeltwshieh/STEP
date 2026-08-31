# Routing v2 詳細解釋筆記

呢份 notes 配合 Slide 11–17 使用。目標係用非技術方式解釋 Routing v2 嘅核心
控制，同時保留足夠 detail，俾想知道實際資料結構同 validator 行為嘅人閱讀。

## 1. 一句講晒 RoutePlan

RoutePlan 係一份**寫答案之前建立嘅結構化工作表**。

普通做法可能係：見到題目，開始搜尋相關材料，跟住一邊諗一邊寫。Routing v2
會先停一停，將以下問題變成可檢查嘅資料：

- 呢一題係 MCQ、prose 定 drafting
- 題目真正提供咗咩 facts
- 有邊啲 facts 係會改變答案
- 適用邊個 jurisdiction、regime、actor、relationship 同 stage
- 應該考慮邊啲 course files
- 邊啲 routes 必須用、只係 conditional、應該禁止，或者只係 check 過但唔相關
- 有冇互相排斥嘅選擇
- 如果要 draft 文件，完整 document chain 有幾多份文件、clauses、attachments、
  execution blocks 同 records/filings
- 最後每個 mandatory route 對答案貢獻咗乜

所以 RoutePlan 唔係答案本身，亦唔係另一套法律。佢係答案之前嘅「設計圖 +
checklist + audit trail」。

## 2. Freeze allowlist 係乜

### 最簡單比喻：活動賓客名單

想像一個私人活動：

1. 活動開始前，主辦方先寫低邊啲人可以入場
2. 名單確認後鎖定
3. 保安只可以放名單上嘅人入場
4. 唔可以見到一個熟面口，就臨時偷偷加佢入名單

Routing v2 嘅 allowlist 就係「可以打開嘅 source file 名單」。

### 每一行有咩

一個 allowlist entry 主要有三項：

| 欄位 | 意思 | 例子 |
|---|---|---|
| `path` | 準確 relative file path | `Course-Manual-Module-10-...md` |
| `namespace` | 呢份 file 屬於邊類來源 | `course_manual`、`course_appendix` |
| `role` | 打算點用 | `incorporated`、`conditional`、`check_only` |

Role 嘅意思：

- `incorporated`：預計會實際支持答案或文件內容
- `conditional`：只喺某個 activating fact 出現時先適用
- `check_only`：需要核對，但預計唔會成為 submitted answer 嘅證據

### Freeze 實際做咩

RoutePlan 會將 allowlist 標記為 frozen，然後將整張 allowlist 用固定格式計一個
SHA-256 hash，存入 `allowlist_sha256`。

可以將 hash 理解為名單嘅「數碼封條」：

- 名單順序或內容冇變，重新計出嚟嘅 hash 會相同
- 有人加、刪或改一行，hash 就唔同
- validator 會重新計 hash，確認 frozen 名單冇被改過

### 點解要喺開 substantive sources 之前 freeze

因為答案開始形成之後，人或模型會有誘惑：

- 見到 MCQ distractor 提到某份 appendix，就順手開嚟睇
- 發現原本 route 唔夠完整，就偷偷再開另一份 file
- 將 prior answer 或 KAP 當成「只係比較」
- 開晒所有可能相關 files，再揀一個似答案嘅結果

Freeze allowlist 迫使 routing decision 先行：**先講點解有權開，後至真正開**。

Allowlist 唔代表所有 entries 最後一定成為答案證據。佢只代表喺呢個 answer unit
入面，呢啲係事前批准可以接觸嘅 sources。

## 3. actual_open 係乜

### 最簡單比喻：入場掃描紀錄

Allowlist 係賓客名單；`actual_open` 係門口 scanner 真正記錄邊個入過場。

如果一份 file 真係被打開，actual-open ledger 應該加一行。每行包括：

| 欄位 | 意思 |
|---|---|
| `path` | 實際打開嘅準確 relative path |
| `namespace` | 呢份 file 嘅來源類別 |
| `role` | 實際以咩角色打開 |
| `sha256` | 打開嗰一刻觀察到嘅 file hash |

File hash 有兩個作用：

1. 證明 ledger 指向嘅係同一份內容，而唔係同名但已經改過嘅 file
2. 令測試結果可以重現同核對

### allowlist 同 actual_open 唔係同一樣嘢

- Allowlist：**計劃上批准可以開**
- actual_open：**實際真係開過**

例如 allowlist 有 6 份 files，但最後只需要開 4 份，actual_open 可以只有 4 行。
不過，如果某條 route 已經標記為 `incorporated`，佢嘅 source 就唔可以只存在於
allowlist；必須真係出現喺 actual_open，因為你唔可以話一份從未打開嘅材料支持
答案。

### `Sources used` 又係乜

三者要分開：

1. `allowlist`：預先批准接觸
2. `actual_open`：實際接觸過
3. `Sources used`：最後答案展示畀使用者、實際用作證據嘅 sources

一份 file 可以 actual-open 作 conditional/check，但最終唔出現喺 Sources used。
相反，一份 file 唔可以冇 actual-open，卻突然出現喺 Sources used。

## 4. 兩張表點樣 reconciliation

Validator 會做幾個核心檢查：

### 規則 A：actual_open 必須係 allowlist 入面嘅項目

概念上：

`actual_open ⊆ allowlist`

任何名單外開檔，都係 source isolation failure。

### 規則 B：role 要一致

如果 allowlist 話一份 file 只係 `conditional`，actual_open 唔可以無聲無息變成
`incorporated`。否則 routing decision 已經被 retrieval 過程改寫。

### 規則 C：incorporated route 必須實際開過

如果 Route A 係 mandatory + incorporated：

- source 必須出現喺 frozen allowlist
- allowlist role 必須係 incorporated
- 同一個 source 必須出現喺 actual_open
- actual-open role 亦必須係 incorporated

### 規則 D：forbidden / prior-answer path 永遠唔可以開

就算將 role 寫成 `check_only`，亦唔可以洗白 forbidden appendix、KAP、gold、prior
answer 或 peer output。

### Filesystem 層點配合

Blind test 時，isolation harness 唔只相信 agent 自己填 ledger。佢會：

1. 將事前批准嘅 file copy 入 mediated `opened-inputs` tree
2. Sandbox 只准 answer command 讀呢個 tree 同必要 runtime files
3. Undeclared path 會被 Seatbelt 阻止
4. 即使 answer command catch 咗 `PermissionError` 再正常退出，kernel denial audit
   仍然會記 hard isolation failure

呢一層係防止「ledger 寫得好睇，但實際偷睇咗其他 files」。

## 5. 6 locks 係乜

Locks 係答題前必須固定或明確標記 unknown 嘅六個基本維度。佢哋防止用啱咗
topic，但用錯咗 jurisdiction、身份、程序階段或 governing instrument。

每一把 lock 大致有：

- `state`：`supplied`、`choice_delegated` 或 `genuinely_unknown`
- `value`：實際鎖定值；如果 genuinely unknown，就應該係 null
- `deciding_fact_ids`：邊啲 typed facts 支持呢個 value
- `alternatives`：如果未能唯一決定，有咩隔離咗嘅 alternatives

### Lock 1：jurisdiction

問：公司受邊個司法區法律管？

- `supplied`：題目已講明，直接鎖定
- `choice_delegated`：題目要求答題者揀一個 course-supported jurisdiction，揀一次
  後全題一致
- `genuinely_unknown`：題目冇講，亦冇授權揀，唔可以靠 lender address、asset
  location 或 registry 自己推斷

### Lock 2：regime / entity type

問：呢間係咩公司、用邊套 regime？

例如 traditional/Table A company、BVI BC、IBC、public/private、solvent/insolvent
liquidation regime。相同 topic 喺唔同 regime 可以有唔同 actor、test 或 precedent。

### Lock 3：legal actor / capacity

問：而家邊個以咩身份做嘢？

常見分別包括：

- registered member vs beneficial owner
- individual director vs corporate director
- company board vs shareholder/member
- transferor vs transferee
- company vs liquidator

同一個人可能有幾個身份，但每個 action 要用正確 capacity。Beneficial owner 唔會
因為經濟上控制公司，就自動變成 registered member 或 director。

### Lock 4：transaction / legal relationship

問：雙方之間究竟係咩法律關係？

例如：

- registered ownership vs beneficial ownership
- company/member
- board/director
- debtor/secured creditor
- principal/agent
- company/liquidator

Relationship lock 決定邊個有權做決定、邊份文件由邊個簽，同邊個 procedure 適用。

### Lock 5：current and requested lifecycle stage

問：件事而家行到邊一步，題目又要求做到邊一步？

同一宗 transaction 可以有：instruction、authority、approval、resolution、execution、
delivery、register update、external filing、enforcement、final account 等階段。

題目只叫 draft notice，唔代表要將之前嘅 board resolution 都塞入 notice；但 notice
本身提出嘅 operative business 又必須完整。

### Lock 6：governing legislation / memorandum / articles

問：真正控制呢個決定嘅 law、memorandum 同 articles 係邊套？

優先次序由題目同實際 governing instruments 控制。Course model articles 或
appendix examples 只係 examples，唔可以蓋過題目提供嘅 actual articles。

## 6. XOR branches 係乜

XOR 即 exclusive OR：一組互相排斥嘅 routes，最多只可以揀一條。

典型例子：

- share transfer：board approval **或者** refusal + refusal notice
- solvent winding-up completion：final meeting **或者** written approval route
- 一個 jurisdiction-specific form **或者** 另一個 jurisdiction-specific form

一個 XOR set 主要記錄：

| 欄位 | 意思 |
|---|---|
| `route_ids` | 呢組所有互斥 routes |
| `selection_state` | `selected`、`unresolved` 或 `not_applicable` |
| `selected_route_ids` | 真正揀中嘅 route；selected 時只可以有一條 |
| `deciding_fact_ids` | 題目邊個 fact 令呢條 route 勝出 |

### State 1：selected

題目提供咗 outcome-changing deciding fact。Validator 要求：

- exactly one selected route
- selected route 必須 incorporated
- 同一 XOR set 其他 route 唔可以同時 incorporated
- deciding fact 必須存在，而且係 supporting disposition

### State 2：unresolved

題目未提供決定分支嘅 fact。正確做法唔係估，而係：

- selected routes = 0
- 所有仍可能適用嘅 branches 保持 conditional
- 答案清楚講 IF approval / IF refusal，或者保留 placeholder

### State 3：not_applicable

呢組 branch 喺鎖定 facts 下完全唔適用，所以唔選任何 route。

## 7. 一個簡單 XOR 實例

假設 facts 係：registered nominee 要將 legal title 轉俾 buyer，但題目冇講 board 最後
批准定拒絕 transfer。

### 已知 facts

- registered holder 會改變，所以係 legal-title transfer
- registered nominee 先係 transferor
- buyer 只會喺 register update 後成為 registered holder
- board decision 未知

### Mandatory base route

- transfer instrument 係必須
- transfer/registration procedure 係必須分析

### XOR branch

- Branch A：如果 board approves → approval resolution + register/certificate update
- Branch B：如果 board refuses → refusal resolution + refusal notice

因為 `board decision = missing`：

- XOR state = unresolved
- selected route = none
- approval branch = conditional
- refusal branch = conditional

如果答案直接揀 approval，RoutePlan validator 應該報：selected branch lacks a deciding
fact。呢個正係 Routing v2 防止「覺得正常應該會批准，所以當已批准」嘅方法。

## 8. RoutePlan 其他重要部分

### Facts and claims

每個 material fact，同 MCQ 每個 option claim，都要有 exactly one disposition，例如：

- `used - outcome`
- `used - content`
- `supported`
- `refuted`
- `partly true but not best`
- `condition`
- `not outcome-changing`
- `input gap`
- `materials gap`
- `materials do not resolve`

作用係防止 facts 或 options 被忽略。

### Routes

每條 route 有 source、triggering fact、deciding facts、unique contribution 同 verdict：

- incorporated
- conditional
- forbidden
- checked-not-relevant

### Entities

記錄 human/corporate entity 同 capacities。Exact director count 要有 typed supporting
fact，唔可以因為某公司係「sole corporate director」就推斷嗰間 provider subsidiary
自己都係 sole-director company。

### Requested-document chain

如果題目要求 operative document，RoutePlan 會逐份 instrument 記：

- sequence
- owner/actor
- upstream authority
- human signatory
- operative components
- attachments
- execution
- records/filings

Expected counts 同 actual counts 要對得上。Complex transaction 仲要分開
conveyance/Bill of Sale、facility、security、registry document，同真正 produced 嘅
register-of-charges stage。

### Materials gaps

Course 冇 exact form 或 rule 時，唔可以創作。Gap 必須：

- 保持 conditional；或者
- 用明確 placeholder 表示

### Final trace

每條 incorporated、conditional、forbidden 或 checked route 都要留一條 trace，講清楚
unique contribution 同答案位置。呢個係 removal test：如果刪走一條 mandatory route
答案完全冇變，可能代表 route 其實 irrelevant，或者佢嘅貢獻漏咗寫。

## 9. RoutePlan 完整運作次序

1. 讀完整題目同 attachments
2. 分類 MCQ / prose / drafting
3. 將 facts、claims 同 requested deliverables 拆開
4. 固定或標記六把 locks
5. 用 Content map 建立 candidate routes
6. 做第二次 independent relationship/lifecycle pass
7. 分類 incorporated / conditional / forbidden / checked-not-relevant
8. 建立 XOR sets 同 document chain
9. 建立並 freeze source allowlist，計 allowlist hash
10. 只開 allowlisted sources，更新 actual_open ledger
11. 記 materials gaps 同 final trace
12. Validator 檢查 schema 同 cross-field invariants
13. 只有 `VALID` + exit code 0 先可以 render answer
14. Section A 或 Section B adapter 做最後格式、coverage、style 同 confidence checks

## 10. 常見誤解

### 「Allowlist 入面嘅 files 全部都要引用？」

唔係。Allowlist 係批准接觸範圍，唔等於全部會成為 submitted evidence。

### 「actual_open 就係 Sources used？」

唔係。Actual open 可以包括 conditional 或 check-only sources；Sources used 只列真正
incorporated 入答案嘅 evidence。

### 「Freeze 之後發現真係漏咗 source 點算？」

唔應該偷偷改。應該承認 route plan 未完成，退返去 routing stage，修訂 plan、重新
freeze 同重新 validate。舊 validation report 唔再有效。

### 「XOR unresolved 即係兩條都揀？」

相反。Unresolved 係零條 selected，兩條只保持 conditional。兩條一齊 incorporated
會 fail。

### 「6 locks 係咪六條法律規則？」

唔係。佢哋係六個 routing dimensions，用嚟確定應該套用邊條法律規則。

### 「RoutePlan 令 bot 識多咗法律？」

唔會。Course manuals 同 appendices 完全相同。RoutePlan 改善嘅係 selection、
completeness、branch discipline、source traceability 同 validation。

## 11. Presenter 可以點樣簡單講

可以用以下三句：

1. Allowlist 係活動前鎖定嘅賓客名單
2. actual_open 係門口真正掃過嘅入場紀錄
3. RoutePlan 係寫答案前先鎖定司法區、公司類型、人物身份、關係、程序階段同
   governing rules，再用 XOR 防止同時揀兩條互相矛盾嘅路

最後一句總結：Routing v2 唔係加多一套法律，而係令同一套材料用得更有紀律、更
完整同更容易核查。

## 12. Hash 係乜

Hash 可以理解為一份資料嘅「數碼指紋」。Routing v2 使用 SHA-256，將任意長度嘅
內容轉成固定長度嘅 64 個 hexadecimal characters。

Hash 有四個最重要特性：

1. 同一份內容，用同一個方法計，每次得到同一個 hash
2. 內容改一個字、一個空格或一個 list entry，hash 通常會完全不同
3. 由 hash 基本上唔能夠還原原本內容
4. Hash 只顯示「有冇變」，唔會話你改咗邊一行

Allowlist 計 hash 前會先用 canonical JSON format：keys 固定排序，分隔符固定，避免
同一張名單只因為排版或空格不同就得到不同 hash。

概念上：

```text
allowlist_sha256 = SHA-256(canonical allowlist JSON)
```

## 13. 點解舊 bot 偷加一份 file 係大問題

表面睇，只係「多睇一份資料」。真正問題係**證據範圍改變嘅時間**。

正確 routing 應該係：

```text
完整理解題目
      ↓
決定需要邊啲 sources
      ↓
開 sources
      ↓
形成答案
```

偷偷加 file 通常變成：

```text
先開部分 sources
      ↓
開始見到想答邊個方向
      ↓
再搵一份支持嗰個方向嘅 file
      ↓
將新 file 包裝成原本 routing 一部分
```

呢個會造成幾個嚴重後果。

### 13.1 Outcome-driven source selection

Source selection 唔再由題目 facts 同 locks 決定，而係由已經浮現嘅答案決定。模型
可以不斷搵 supporting material，直到原本想答嘅 conclusion 睇落合理。

### 13.2 Confirmation bias

一旦模型傾向某個 MCQ option 或 drafting route，就容易只開支持嗰個方向嘅 files，
而忽略相反 branch 或真正 governing source。

### 13.3 Distractor 自我授權

MCQ option 可能刻意寫出一份錯誤 appendix。如果「option 提到 file」已經足以授權
開 file，distractor 就可以控制 retrieval，破壞先由 governing proposition 判斷嘅流程。

### 13.4 Blind test 失效

Blind evaluation 要證明 answer agent 未見 gold、KAP、prior answer 或 peer output。
一旦事後可以靜靜加 file，測試再無法證明答案係獨立產生。

### 13.5 Audit trail 變成假紀錄

RoutePlan、Cross-check 同 Sources used 會令人以為 sources 係事前根據題目選擇，實際
卻係答案形成後先補入。表面 trace 完整，因果次序係相反。

### 13.6 任意答案都可能被合理化

如果 bot 可以先揀答案，再擴大 source universe，佢往往可以搵到某段 related text
令錯誤答案睇落「有來源」。Course materials 多、regimes 多、precedents 相似時，風險
尤其大。

所以真正問題唔係 file 數量，而係由「題目決定 sources」變成「答案決定 sources」。

## 14. Hash 點樣發現 allowlist 被改

假設 freeze 時 allowlist 係：

```text
Module 6
Module 10
Appendix 18A
Appendix 18B
```

計出：

```text
Hash A = 123abc...
```

答案開始形成後，有人加入 Appendix 18C：

```text
Module 6
Module 10
Appendix 18A
Appendix 18B
Appendix 18C
```

重新計會得到另一個值：

```text
Hash B = 9f82de...
```

因為 `Hash A ≠ Hash B`，validator 知道 frozen list 同而家 list 唔同。原本 validation
authorization 失效。

正確處理唔係偷偷更新 hash，而係：

1. 退返 routing stage
2. 解釋新 file 由邊個 fact、route 或 gap 觸發
3. 更新 RoutePlan
4. 重新 freeze
5. 重新 retrieval／actual-open reconciliation
6. 重新 validate

## 15. Routing v2 嘅三層 hash

### 15.1 Allowlist hash

保護「批准名單版本」。回答：retrieval 前批准嘅 source universe 有冇改過？

### 15.2 actual-open file hash

每個 actual-open row 都記 observed file SHA-256。保護「實際內容版本」。回答：兩個
session 所講嘅同名 file，係咪真係 byte-identical？

### 15.3 Answer/output hash

Answer artifacts staged 後計 hash，再 lock。保護「評估時睇到嘅 output 版本」。回答：
gold 或 KAP release 後，candidate answer 有冇再被改過？

三層唔可以互相取代：

- Allowlist 冇變，不代表 source file 內容冇變
- File 內容冇變，不代表 answer output 冇變
- Answer hash 冇變，不代表 retrieval source boundary 正確

## 16. Hash 可以做乜，同唔可以做乜

Hash 可以提供：

- change detection
- content identity
- reproducibility
- machine-checkable audit evidence
- state-transition gate

Hash 唔係：

- encryption
- password
- permission system
- source truthfulness proof
- legal correctness proof
- filesystem access control

如果同一個人可以同時修改資料同 stored hash，佢可以對修改後內容重新計一個新
hash。所以 hash 必須放喺完整 protocol 入面：

```text
Hash          → 證明資料有冇變
Sandbox       → 真正阻止名單外讀取
Validator     → 對 allowlist、actual_open 同 routes
Retained report → 保存當時嘅 plan/hash/result
Hash lock     → 防止 evaluator release 後改 answer
```

最準確嘅講法係：hash 提供 tamper evidence；sandbox 提供 access control；validator
提供 rules enforcement。三者一齊先構成完整保護。

## 17. 俾朋友聽嘅 30 秒版本

可以咁講：

> 普通 bot 可能一邊答、一邊再搵資料。問題係，佢見到自己想答嘅方向後，可以再
> 加一份支持自己嘅 file，令人唔知 sources 係事前揀定，定係事後追答案。Routing
> v2 會先鎖定准許開嘅 files，再為張名單計 hash。名單加減任何一行，hash 都會變，
> validator 就知道原本封條被拆過。不過 hash 只係防拆證據，真正守門仲要靠 sandbox，
> 最後再由 validator 對數。

一句結論：

> Hash 將「我應該冇改過」變成「機器可以檢查我有冇改過」
