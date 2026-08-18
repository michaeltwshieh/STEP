# Section B — Essay instructions

## Output format

Produce a **complete, submit-ready essay in full prose** the user transcribes directly. Lay it out in two clearly separated blocks:

```
─────────── SUBMIT THIS ───────────
[the full essay — pure prose, nothing else; no source tags, no headings
 unless the question structure calls for them]

──── DO NOT SUBMIT — for your check ────
Authorities cited: <every case / statute / article, so the user can verify each>
Source: <module(s) + section(s) + appendix(es) + filenames>
Cross-checked: <the second-pass (CLAUDE.md step 5) result — any other module/appendix checked for a multi-module overlap and the verdict, e.g. "Module 10 §5.8 → incorporated; Module 12 → considered, not relevant"; or "single-module". Always present, even when empty-handed.>
Confidence: high / medium / low — also give a numeric score out of 10 (e.g. "high (9/10)")
Verify: <anything to double-check, or "none">
```

The `SUBMIT THIS` block must contain **only** the essay. Never let a source tag, module reference, or page number leak into it — that text is submitted and must read as the user's own work.

## How to build the essay (examiner's approach)

Follow the booklet's standard approach:

1. **State the relevant principles of law accurately.**
2. **Apply them to the specific facts/issues** the question raises.
3. **Support with authority** — relevant cases and statutes (see citation form).
4. **Make informal, critical comment** on the law where apt.
5. **Conclude** — reach a position; do not jump to it and do not leave it open.

An essay is more likely than an MCQ to span several modules, so **run the second-pass cross-module check (CLAUDE.md step 5) before finalising**: name a candidate second module, scan the `Content.md` outlines, and incorporate it only if it supplies a rule/procedure/authority the question asks for that your primary module doesn't (default to discard — irrelevant cross-module padding loses marks). Record the result on the `Cross-checked:` line of the check panel, never in the submitted prose.

Read the examiner's **command word** and answer what it actually demands:

- **Advise** — put forward information, opinions or recommendations that enable action.
- **Analyse** — examine in detail to discover its meaning / essential features.
- **Assess / Evaluate** — judge the worth or importance; give a reasoned opinion.
- **Compare / Contrast / Distinguish** — bring out resemblances and/or differences.
- **Criticise** — give your views, backed by a discussion of the evidence.
- **Describe / Explain** — give a clear, detailed account of the important features.
- **Discuss** — give all sides of the argument, then reach a conclusion.
- **Draft** — reproduce the relevant precedent document (see "Drafting sub-parts" below). This is not a prose task.
- **Illustrate** — clarify by the use of examples.
- **Reconcile** — make apparently conflicting views consistent.
- **Summarise / Outline** — give a brief account of the main points.
- **"What is the significance of…?"** — define, then outline its uses, consequences and implications.

## Drafting sub-parts (the "draft" command, or a notice / resolution / minute / form / statement of account)

This is a **precedent-reproduction task**, not a prose task. The reword rule below is suspended for it.

1. **Open the named or implied Appendix first.** If the question says "draft a notice that complies with Article X" or points to an Appendix, view that exact precedent file before drafting.
2. **Reproduce its full structure.** Count its operative parts and include every one. If a precedent contains three resolutions, your draft contains three, not two.
3. **Keep the precedent's operative wording**, including headings, recipient blocks, execution/date/signature blocks, and singular/plural and joint-and-several formulations (e.g. "the Liquidators … jointly and severally"). Do not paraphrase these into your own words. This holds even when a precedent is used only for its shape. Lifting its layout while rewording its operative clauses is the most common way marks are lost... If you open a precedent for any reason, its operative wording is reproduced, not paraphrased.
4. **Run the drafting checklist before finishing:** heading matches the precedent ✓; all recipients listed ✓; every resolution / clause present ✓; execution block (date, signature, seal if required) ✓; proxy line or other standard notes ✓.
5. Where a precedent uses a placeholder ([name], [date], [venue]), keep it as a placeholder unless the facts supply the value, then insert the value.

## Writing style (matters — answers are AI- and plagiarism-checked)

This style guidance governs **prose sub-parts**. For drafting sub-parts, the precedent's wording governs instead.

The two signals AI detectors weight most heavily are **burstiness** (variation in sentence length) and **perplexity** (how unpredictable each word choice is). Optimise for both throughout.

### Burstiness — sentence and paragraph length

Mix lengths aggressively, not gently. Some sentences must be very short. Four words. Others should run much longer, building through subordinate clauses and qualifications before landing on the operative point, as a candidate under exam pressure tends to do when working through a complex argument in real time. One-sentence paragraphs are fine alongside four-sentence ones. Never let three consecutive sentences be the same length.

### Perplexity — word choice

Prefer the less obvious but equally correct word over the statistically safe one. "The rule cuts both ways" over "This principle establishes a dual obligation." "There is no real dispute that" over "It is clear that." Compressed, direct phrasing over the most predictable formulation. Vary between slightly more formal and slightly more compressed register across paragraphs — not inconsistently, but not uniformly either.

### Syntactic variety

- Start some sentences with a subordinate clause: "Where a member has not been given notice…"
- Start some with a conjunction: "But the position becomes more complex when…" / "Yet the statute is silent on…"
- Use parenthetical asides in brackets: "the liquidator (who may be a non-member) is nonetheless bound by…"
- Use interrupted constructions occasionally: "The articles, whatever their precise wording, cannot override the statute."
- Avoid three-item lists in perfect parallel grammatical structure. Break the pattern: list two items cleanly, then introduce the third differently.

### Banned words and phrases

Never use: "crucial", "significant", "essential", "examine", "delve", "it is worth noting", "it bears mentioning", "it is important to note", "navigate", "robust", "nuanced", "comprehensive", "shed light on", "in conclusion", "to summarise", "furthermore", "moreover", "firstly/secondly/thirdly", "in addition", "additionally". Also avoid the AI vocabulary cluster: "landscape", "tapestry", "interplay", "foster", "underscore", "testament", "pivotal", "realm", "multifaceted", "leverage", "utilise", "facilitate", "vital", "that being said", "ultimately". Avoid speculative filler ("only time will tell", "at a rapid pace") and dated openers ("in today's world").

**Never use em-dashes (—).** Use commas, full stops, brackets, or a colon instead.

### Sentence construction — AI tells to strip out

These are the constructions a detector and a careful human reader both clock instantly. They matter more than vocabulary.

- **Use plain "is / are / has".** AI dresses up the verb: "serves as", "stands as", "operates as", "boasts", "represents". A director *is* a fiduciary; he does not "serve as" one. The doctrine *is* settled; it does not "stands as settled".
- **Cut "-ing" tails.** AI bolts a present participle onto the end of a sentence to fake depth: "...the articles are binding, reflecting the contractual nature of membership" or "...highlighting the importance of notice". Stop the sentence at the point. If the trailing clause carries real content, make it its own sentence.
- **No negative parallelism.** "It is not X, it is Y" and "This is less about X than about Y" are strong tells. State the positive directly. Not "The duty is not merely procedural, it is substantive" but "The duty is substantive, not just a procedural box to tick" only if you must, and better still just assert the substantive point.
- **Repeat the precise term; do not cycle synonyms.** AI varies wording to avoid repetition ("the company", then "the entity", then "the corporate body"). Legal writing wants the opposite. Pick the correct term and reuse it. A "member" stays a "member", not a "shareholder" then a "stakeholder".
- **Replace filler stems.** "in order to" → "to"; "due to the fact that" → "because"; "has the ability to" → "can"; "at this point in time" → "now" / "here".
- **No vague attribution.** "Commentators argue", "it has been observed", "academics suggest" without a name is both a marks-loser and an AI tell. Either cite a real authority from the materials or assert the point in your own voice using the endorsed forms ("it is arguable that").
- **Don't manufacture drama with clustered fragments.** Short sentences create burstiness, which is good, but several short punchy fragments in a row to build intensity ("The rule is clear. The breach is plain. The result follows.") is itself an AI signature. Let a short sentence sit next to a long one, not next to two more short ones.

### Structural asymmetry — the strongest single tell

AI applies balanced, parallel structure far more often than humans do, and it does so at every level: word, phrase, sentence, paragraph, and whole answer. This symmetry appears in the large majority of AI text and is one of the most reliable things a detector keys on. Human writing is lopsided. Build that lopsidedness in deliberately.

- **Uneven paragraphs.** Do not make paragraphs roughly the same length. One issue might take a long, worked-through paragraph; the next disposes of a weaker point in two sentences. The variance is the signal.
- **Let one side win.** When you weigh two views, do not give them equal column inches and a tidy balance. A real candidate finds one argument stronger and spends more on it, conceding the other briefly. "There is an argument that X, but it does not survive contact with the statute" is more human than two perfectly matched paragraphs.
- **Vary how paragraphs open.** Do not start consecutive paragraphs the same way (e.g. every one with "The..." or every one naming the rule first). Mix: lead one with the facts, the next with the authority, the next with a question or a concession.
- **Break the rule-case-application template.** AI tends to structure every paragraph identically (state rule, cite case, apply). Vary the order. Sometimes apply first and bring the authority in to confirm; sometimes open on the difficulty.
- **Don't over-resolve.** AI ties a neat bow on every paragraph. You still need a clear overall conclusion (the exam demands it), but individual paragraphs can end on an unresolved tension or a concession rather than a mini-summary. Reach your position once, at the end, not five times along the way.
- **No tricolons by reflex.** The three-parallel-item list ("the duty of care, the duty of loyalty, and the duty of good faith") is a heavy tell when forced. If there genuinely are three, fine, but break the parallel grammar or give one of them an extra clause so the rhythm is uneven.

### Coverage — leave some things brief

A human under exam pressure does not develop every point equally. Some sub-points deserve a sentence; others deserve a paragraph. Briefly dismissing a less relevant issue ("the question of X does not arise on these facts") reads human. Exhaustively developing every angle reads AI.

### Impersonality and register

**Stay impersonal — no first person.** Do not write "I think", "in my view", "I would argue". Use the examiner-endorsed forms: "a better view is…", "it is suggested that…", "it is arguable that…". Strike a balance between formal and informal. No slang; define any abbreviation on first use.

### Rewording

**Interpret the law into your own words** — do not quote or closely track the manual's wording. Per the guidance booklet: *"ensure that any content that is not in your own wording has been appropriately referenced, this includes any materials provided as part of the course."* Anything genuinely quoted must sit in quotation marks and be attributed; everything else must be properly reworded. **Limited marks are awarded for answers over-reliant on the course material** — show application of knowledge, not reproduction. This rule does not apply to drafting sub-parts, where reproducing the precedent is the point.

## When the rules conflict

If the reword / own-words rule and the precedent-fidelity rule point in opposite directions, **precedent-fidelity wins for drafted documents**. Article-accurate or "improved" wording does not override the wording of the named precedent. Reword only the substantive legal explanation that surrounds or follows a draft, never the drafted document itself.

## Citation form

- **Cases:** name + (year) where the materials give it, the relevant facts, and the outcome — then **relate the outcome to the point**. Don't retell the parties' background or a judge's dicta. Don't reuse one case for every point.
- **Statutes:** section + full Act name + year, e.g. *section 31 Trustee Act 1925*. Standard abbreviations are fine (IHTA 1984, LPA 1925); don't repeat the Act once context makes it clear.
- **Latin** only where there's no real alternative (a proper name or special meaning), e.g. *donatio mortis causa*, *sui juris*.
- In the essay body, **never cite the course manual itself or page numbers** — write as a candidate. Source attribution belongs only in the check panel. (Article numbers from articles attached to the question itself may be cited in the body; they are part of the question, not the manual.)

## Practices to avoid

Don't retype/repeat the question; no long introductions; no irrelevance or ambiguity; not too much / too little / irrelevant authority; don't over-tell case stories; never jump to a conclusion and never omit one; keep a logical order with proper paragraphs; mind grammar (tenses, singular/plural, a/the).
