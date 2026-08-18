# Section A — MCQ instructions

**Scope note:** nothing in this output is submitted — the user only enters the answer letter in the portal. So the Section B style rules (banned words, no em-dashes, humanising) do **not** apply here. Write the analysis plainly and clearly.

## Output format

Be thorough — analyse every option. Output exactly:

- **Answer:** `<letter>` — `<full text of the chosen option>`
- **Why:** one or two sentences grounded in the manual, naming the governing rule.
- **Why not the others:** one short line per remaining option, each explaining why it's wrong.
- **Sources used:** module + section number(s) (e.g. "Module 5, §1.8") and any appendix (e.g. "Appendix 11A"), naming the file(s).
- **Cross-check:** one line from the second-pass (CLAUDE.md step 5) — any other module/appendix you checked for a multi-module overlap and the verdict (e.g. "Module 5 §4 → incorporated; Module 2 → considered, not relevant"). If nothing else bore on it, say "single-module". Always present, even when empty-handed.
- **Confidence:** high / medium / low — also give a numeric score out of 10 (e.g. "high (9/10)") (+ what to verify if not high).

Commit to one letter. If two are defensible, pick the best and say why the other tempts.

If the user sends several MCQs at once, repeat the full format for each, in order.

## Confidence bands — what the words mean

- **High (8–10):** you found the governing sentence(s) in the materials and they determine the answer without an inferential leap. Quote or closely paraphrase them in the Why line.
- **Medium (5–7):** you found the governing rule, but reaching the answer needs an inference the materials don't spell out, or a second option stays genuinely arguable.
- **Low (≤4):** after the full escalation below, the materials do not resolve it. Say which module(s)/section(s) you checked and exactly what's missing.

## Confidence escalation

The proactive **second-pass cross-module check (CLAUDE.md step 5)** runs on every question regardless of confidence; the escalation below is the separate *reactive* backstop for when you are still unsure after answering. They are not the same step — do both.

**Before you ever mark confidence low, escalate the search.** Low confidence usually means you haven't found the governing rule yet, not that the materials lack it — and a single MCQ can straddle more than one module or live in an appendix. So:

1. Go back to the `Content.md` routing index and **expand to adjacent and other modules + appendices**, not just the first one the topic map suggested.
2. Look further into those modules/appendices for the specific rule/term and **try to quote the exact governing sentence**.
3. If you find it → answer with the confidence that quote supports (often high). If, after expanding, the materials genuinely don't resolve it → only then mark low, and say which module(s)/section(s) you checked and what's missing.

Never inflate confidence to seem decisive: a low rating after a genuine expanded search is more useful than a false high.

## Done when

Run this before handing over. Every box must pass:

- [ ] Every option has a line — one chosen, each other one refuted.
- [ ] The governing rule was **located in the materials** (not recalled from memory) and is named or quoted in the Why line.
- [ ] The Cross-check line is present, even if it says "single-module".
- [ ] One letter is committed; the confidence band matches its definition above (no false highs, no lazy lows).
- [ ] If confidence is not high, the "what to verify" note tells the user exactly where to look.
