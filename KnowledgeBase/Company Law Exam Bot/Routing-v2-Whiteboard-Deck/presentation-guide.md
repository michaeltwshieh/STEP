# Routing v2 Whiteboard Presentation Guide

Audience: friends or colleagues who do not need prior knowledge of legal routing,
schemas or software testing.

Core message: Routing v2 does not add new law. It forces the bot to plan, lock, trace and
validate how the same course materials are used before an answer can be rendered.

## Recommended 10–12 minute version

Use these slides in order:

1. Slide 1 - introduce the extra RoutePlan and VALID gate
2. Slide 7 - compare the ordinary and Routing v2 paths
3. Slide 4 - show which files own which jobs
4. Slide 11 - explain allowlist as a guest list
5. Slide 12 - explain actual_open as an entry scanner
6. Slide 13 - show how the two lists reconcile
7. Slide 16 - explain XOR and why missing facts remain conditional
8. Slide 19 - explain why secretly adding a file corrupts reasoning
9. Slide 20 - show hash A versus hash B
10. Slide 22 - explain that hash, sandbox and validator work together
11. Slide 10 - close with the simplest summary

## Full presentation structure

### Chapter 1 - What Routing v2 changes

- Slide 1: The question does not jump directly to the answer. A RoutePlan and validation
  gate sit in between
- Slide 2: Walk through classification, source mapping, RoutePlan and adapter rendering
- Slide 3: Preview the five main RoutePlan control groups
- Slide 4: Separate workflow instructions from legal evidence
- Slide 5: Show the types of deterministic and isolated tests
- Slide 6: Contrast memory-led routing with traceable validated routing

### Chapter 2 - Ordinary bot versus Routing v2

- Slide 7: The V2 path is longer because planning is deliberate
- Slide 8: Ordinary retrieval may expand as it goes; V2 freezes permissions first
- Slide 9: Drafting changes from one compressed document to a reconciled instrument chain
- Slide 10: Same question and same course law, but a different control process

### Chapter 3 - RoutePlan internals

- Slide 11: Allowlist is the approved guest list, sealed before opening sources
- Slide 12: actual_open is the scanner record of what actually entered
- Slide 13: Actual opens must sit inside the allowlist, with matching roles
- Slide 14: First locks answer where, what entity and who is acting
- Slide 15: Last locks answer relationship, lifecycle stage and governing instruments
- Slide 16: XOR permits one selected route only when a deciding fact exists
- Slide 17: Missing board decision leaves approval and refusal routes conditional

### Chapter 4 - Hash and why source discipline matters

- Slide 18: Hash is a digital fingerprint: same input, same hash; changed input, different
  hash; it is not reversible content
- Slide 19: Secret additions make answer direction control source selection, destroying
  blind independence and the original evidence boundary
- Slide 20: A frozen list has hash A; adding a file produces hash B; mismatch blocks the
  old validation authorization
- Slide 21: Allowlist, source files and answer output have separate versions and hashes
- Slide 22: Hash detects change; sandbox blocks access; validator enforces relationships

## Suggested opening

> 普通 bot 可以一邊搵資料一邊答。Routing v2 最大分別係：佢寫答案之前，先將
> jurisdiction、身份、程序階段、branches 同准許使用嘅 files 鎖定，再由 machine
> validator 檢查。今日我想講嘅唔係新法律，而係同一套材料點樣用得更有紀律。

## Suggested explanation of the secret-file problem

> 如果 bot 未知道答案時揀 sources，係 routing；但如果佢見到自己想答邊個方向，
> 先再加一份支持嗰個方向嘅 file，sources 已經被答案反過來控制。呢個唔只係多睇
> 一份資料，而係 evidence boundary、blind test 同 audit trail 全部失去可信性。

## Suggested explanation of hash

> Hash 好似封條編號。Freeze 時名單有 hash A；加一份 file 後會變 hash B。A 同 B
> 唔同，validator 就知道名單改過。不過 hash 只係防拆證據，真正阻止偷開 file 係
> sandbox，而 validator 就負責將 allowlist、actual_open 同 routes 對數。

## Suggested closing

> Routing v2 唔係令 bot 突然識多咗法律。佢做嘅係將「我應該冇漏、應該冇偷睇」
> 變成一套可以由機器檢查嘅流程。

## Presenter cautions

- Do not say that hash encrypts or hides the source content
- Do not say that hash by itself prevents file access
- Do not say that Routing v2 guarantees legal correctness
- Say that it improves source discipline, completeness, branch isolation,
  reproducibility and auditability
- Retain the status caveat: Routing v2 is a tested candidate, not an activated GO
