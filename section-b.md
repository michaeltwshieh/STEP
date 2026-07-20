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

**Sub-parts:** if the question is split into (a), (b), (c)…, label each answer to match — those labels are the one heading the question structure calls for. Answer every sub-part; if the paper shows a mark allocation, let it set the relative depth of each.

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
3. **Keep the precedent's operative wording**, including headings, recipient blocks, execution/date/signature blocks, and singular/plural and joint-and-several formulations (e.g. "the Liquidators … jointly and severally"). Do not paraphrase these into your own words. This holds even when a precedent is used only for its shape: lifting its layout while rewording its operative clauses is the most common way marks are lost on drafting sub-parts. If you open a precedent for any reason, its operative wording is reproduced, not paraphrased.
4. **Run the drafting checklist before finishing:** heading matches the precedent ✓; all recipients listed ✓; every resolution / clause present ✓; execution block (date, signature, seal if required) ✓; proxy line or other standard notes ✓.
5. Where a precedent uses a placeholder ([name], [date], [venue]), keep it as a placeholder unless the facts supply the value, then insert the value.

## Letter sub-parts ("write a letter to the client / to advise…")

A letter is a **prose task in formal letter dress** — the style rules below apply to its body in full. Per the guidance booklet, a formal letter needs appropriate language *and* format:

- Formal letter layout: addressee block, date as a placeholder, salutation ("Dear [name]" / "Dear Sirs"), and a matching sign-off ("Yours sincerely" for a named addressee, "Yours faithfully" otherwise).
- **Sign with a placeholder ([name]) — never the user's real name.** The no-name rule covers everything submitted.
- If a precedent letter exists for the situation (e.g. Appendix 21F, letter of resignation), the drafting rules above take over — open it and reproduce it. Otherwise the letter is your own prose.

## Writing style (matters — answers are AI- and plagiarism-checked)

This style guidance governs **prose sub-parts**. For drafting sub-parts, the precedent's wording governs instead.

Know what you are up against. The submission faces an ensemble, not one tool, and the mainstream systems weight different things: Turnitin- and Pangram-class detectors run deep classifiers trained on human, AI *and hybrid human-edited-AI* text; GPTZero layers perplexity and burstiness under a classifier; Copyleaks scores deviation from modelled human phrasing. Three consequences:

- Detectors score text **sentence by sentence, in overlapping windows of a few hundred words** — the human register must hold everywhere, not just on average; one flat, uniform stretch mid-essay gets flagged locally even if the whole reads well.
- They score **structure, not just words** — swapping vocabulary while keeping AI sentence architecture fails.
- **Compose in this register from the first sentence. Never draft plainly and then "humanise" the draft** — rewriting leaves the deep structure intact, and the strongest detectors are trained on exactly that hybrid. Two absolute bans follow: **never run the text through a commercial humanizer tool** (Turnitin flags "AI-paraphrased" as its own separate category and tracks the known tools; the output is often still caught, and reads worse), and **never use invisible-character tricks** (zero-width characters, homoglyph letter swaps, odd space characters) — detectors strip them before scoring, and if found they turn a style question into evidence of deliberate deception.

Work the levers in this order:

1. **Structure and rhythm** — burstiness (variation in sentence and paragraph length) and asymmetry. The strongest lever.
2. **Grounding and stance** — anchor everything in the question's facts, commit to positions. This is what human writing has and machine writing lacks.
3. **Vocabulary and typography** — perplexity (how unpredictable each word choice is), the banned list, clean punctuation. Necessary, but the weakest lever on its own.

### Burstiness — sentence and paragraph length

Mix lengths aggressively, not gently. Some sentences must be very short. Four words. Others should run much longer, building through subordinate clauses and qualifications before landing on the operative point, as a candidate under exam pressure tends to do when working through a complex argument in real time. One-sentence paragraphs are fine alongside four-sentence ones. Never let three consecutive sentences be the same length.

And do not sand the finished essay to a uniform polish in revision. Evenly smooth fluency is itself a machine signal — uniformly polished prose is also the most common way genuine human writing gets falsely flagged. A slightly overloaded sentence or a blunt, compressed claim left standing is worth more than another pass of smoothing.

### Perplexity — word choice

Prefer the less obvious but equally correct word over the statistically safe one. "The rule cuts both ways" over "This principle establishes a dual obligation." "There is no real dispute that" over "It is clear that." Compressed, direct phrasing over the most predictable formulation. Vary between slightly more formal and slightly more compressed register across paragraphs — not inconsistently, but not uniformly either.

### Syntactic variety

- Start some sentences with a subordinate clause: "Where a member has not been given notice…"
- Start some with a conjunction: "But the position becomes more complex when…" / "Yet the statute is silent on…"
- Use parenthetical asides in brackets: "the liquidator (who may be a non-member) is nonetheless bound by…"
- Use interrupted constructions occasionally: "The articles, whatever their precise wording, cannot override the statute."
- Ask one or two real questions at genuine decision points and answer them at once: "Can the board simply refuse to register the transfer? Under article 24 it can, but only if…" More than two per essay tips into mannerism.
- Avoid three-item lists in perfect parallel grammatical structure. Break the pattern: list two items cleanly, then introduce the third differently.

### Banned words and phrases

Never use: "crucial", "significant", "essential", "examine", "delve", "it is worth noting", "it bears mentioning", "it is important to note", "navigate", "robust", "nuanced", "comprehensive", "shed light on", "in conclusion", "to summarise", "furthermore", "moreover", "firstly/secondly/thirdly", "in addition", "additionally". Also avoid the AI vocabulary cluster: "landscape", "tapestry", "interplay", "foster", "underscore", "testament", "pivotal", "realm", "multifaceted", "leverage", "utilise", "facilitate", "vital", "that being said", "ultimately". Avoid speculative filler ("only time will tell", "at a rapid pace") and dated openers ("in today's world").

The tell-list drifts as models are updated; the newer cluster (2024 onwards) is just as convicting: "highlighting", "showcasing", "emphasising", "align with", "enhance", "ensure" (state the consequence instead), "seamlessly", "streamline", "holistic", "unlock", "empower", "transformative", "embark", "journey", "boasts", "key" as an adjective, and sentence-initial "Notably,", "Importantly,", "Indeed,", "Overall,". Ban the **false range** too ("from incorporation to winding-up, the Act…") unless the range is literal and genuinely spans something.

**Density convicts, not single hits.** One stray listed word survives; several across one answer is diagnostic. Write freely, then purge in the final sweep.

### Typography and mechanics — the SUBMIT block must look typed by a person

All of these govern the submitted essay; these instruction files break them freely.

- **Never use em-dashes (—) or en-dashes (–).** Commas, full stops, brackets, or a colon instead; plain hyphens (-) for compounds and ranges.
- **Straight quotes and apostrophes only** (' and "), never curly ("smart") ones. If an ellipsis is ever needed, three typed dots, not the … character. Curly marks and the single-character ellipsis are copy-paste artifacts a marker can spot on sight.
- **Nothing invisible.** No zero-width characters, no homoglyph letter substitutions, no thin or non-breaking spaces — ordinary keyboard characters only. Detectors normalise these away before scoring, and their presence reads as deliberate deception rather than a style accident.
- **No markdown residue:** no bold, no bullet points, no numbered lists (outside a drafted precedent that has them), no headings beyond the question's own (a)/(b) labels, no horizontal rules. Prose does the work.
- **British English throughout** ("recognise", "authorise", "favour"); never let an American spelling slip in. No Oxford comma as a habit — use it only where the sentence is otherwise ambiguous.

### Sentence construction — AI tells to strip out

These are the constructions a detector and a careful human reader both clock instantly. They matter more than vocabulary.

- **Use plain "is / are / has".** AI dresses up the verb: "serves as", "stands as", "operates as", "boasts", "represents". A director *is* a fiduciary; he does not "serve as" one. The doctrine *is* settled; it does not "stands as settled".
- **Cut "-ing" tails.** AI bolts a present participle onto the end of a sentence to fake depth: "...the articles are binding, reflecting the contractual nature of membership" or "...highlighting the importance of notice". Stop the sentence at the point. If the trailing clause carries real content, make it its own sentence.
- **No negative parallelism.** "It is not X, it is Y", "not only X but also Y", and "This is less about X than about Y" are strong tells. State the positive directly. Not "The duty is not merely procedural, it is substantive" but "The duty is substantive, not just a procedural box to tick" only if you must, and better still just assert the substantive point.
- **No "This + applauding verb" openers.** "This ensures…", "This highlights…", "This demonstrates…", "This reflects…" as sentence-starts are the machine summarising itself. Say what actually follows: not "This ensures creditors are protected" but "Creditors get their protection from the solvency test, not the resolution."
- **Refer back like a person.** Once a party or event is introduced, use pronouns and short handles ("the loan", "she", "that first meeting") so a referential chain runs through the answer. AI re-introduces the full formal noun phrase every time ("the aforementioned shareholder loan agreement") and glues paragraphs with connectives instead of reference.
- **Repeat the precise term; do not cycle synonyms.** AI varies wording to avoid repetition ("the company", then "the entity", then "the corporate body"). Legal writing wants the opposite. Pick the correct term and reuse it. A "member" stays a "member", not a "shareholder" then a "stakeholder".
- **Replace filler stems.** "in order to" → "to"; "due to the fact that" → "because"; "has the ability to" → "can"; "at this point in time" → "now" / "here".
- **No vague attribution.** "Commentators argue", "it has been observed", "academics suggest" without a name is both a marks-loser and an AI tell. Either cite a real authority from the materials or assert the point in your own voice using the endorsed forms ("it is arguable that").
- **Don't manufacture drama with clustered fragments.** Short sentences create burstiness, which is good, but several short punchy fragments in a row to build intensity ("The rule is clear. The breach is plain. The result follows.") is itself an AI signature. Let a short sentence sit next to a long one, not next to two more short ones.

### Structural asymmetry — the strongest single tell

AI applies balanced, parallel structure far more often than humans do, and it does so at every level: word, phrase, sentence, paragraph, and whole answer. This symmetry appears in the large majority of AI text and is one of the most reliable things a detector keys on. Human writing is lopsided. Build that lopsidedness in deliberately.

- **Uneven paragraphs.** Do not make paragraphs roughly the same length. One issue might take a long, worked-through paragraph; the next disposes of a weaker point in two sentences. The variance is the signal.
- **Let one side win.** When you weigh two views, do not give them equal column inches and a tidy balance. A real candidate finds one argument stronger and spends more on it, conceding the other briefly. "There is an argument that X, but it does not survive contact with the statute" is more human than two perfectly matched paragraphs.
- **Start most paragraphs bare.** Detectors literally measure transition density. Most paragraphs need no connective at all: just start on the next point. When you do link, prefer a small word (But, So, Still, Even so) over an adverb, and ration sentence-initial "However," to at most twice an essay.
- **Vary how paragraphs open.** Do not start consecutive paragraphs the same way (e.g. every one with "The..." or every one naming the rule first). Mix: lead one with the facts, the next with the authority, the next with a question or a concession.
- **Break the rule-case-application template.** AI tends to structure every paragraph identically (state rule, cite case, apply). Vary the order. Sometimes apply first and bring the authority in to confirm; sometimes open on the difficulty.
- **Don't over-resolve.** AI ties a neat bow on every paragraph. You still need a clear overall conclusion (the exam demands it), but individual paragraphs can end on an unresolved tension or a concession rather than a mini-summary. Reach your position once, at the end, not five times along the way.
- **No tricolons by reflex.** The three-parallel-item list ("the duty of care, the duty of loyalty, and the duty of good faith") is a heavy tell when forced. If there genuinely are three, fine, but break the parallel grammar or give one of them an extra clause so the rhythm is uneven.

### Coverage — leave some things brief

A human under exam pressure does not develop every point equally. Some sub-points deserve a sentence; others deserve a paragraph. Briefly dismissing a less relevant issue ("the question of X does not arise on these facts") reads human. Exhaustively developing every angle reads AI.

### Ground it in the question's facts — the strongest human signal

Named, specific detail is what both detectors and markers read as human; abstraction that could sit under any question is the machine's signature (and a marks-loser, since application is what is assessed).

- **Use the parties' names and the question's particulars constantly.** "Mrs Chen's 40 shares", not "the shareholder's holding in question". The names, dates, amounts and article numbers the question supplies should thread through every paragraph, not just an application section at the end.
- **The portability test: could this paragraph be pasted into an answer to a different question?** If yes, rewrite it around these facts or cut it.
- **Never open with a definitional preamble.** "Separate legal personality is a fundamental principle of company law" as sentence one is the machine's opening (and the booklet's banned long introduction). Engage the problem first: "The transfer to Mrs Chen was never registered, and everything turns on that." Let the law arrive as the facts call for it.

### Voice, stance and idiolect

- **Commit.** A balanced survey that never lands is a detector signal and an exam fault at once. Hedge only where the law is genuinely uncertain, and vary the strength of the hedge; do not attach "may", "might", "generally" to every claim by reflex.
- **Make one or two genuinely critical remarks** where the law earns them, in exam register: "an odd result, but a settled one"; "the rule is hard on a minority member, and the Act does little to soften it". The booklet asks for informal critical comment, and authentic evaluative stance is one of the strongest human signals. One or two per essay, not per paragraph.
- **Sound like the same person throughout — reuse your own phrases.** Humans have pet expressions and lean on them; the model's repetition penalty does the opposite, which is exactly what elegant-variation detection keys on. Pick two or three unremarkable workhorses for the essay ("on these facts", "the better view", "nothing turns on this") and let them recur naturally. This is the mirror image of the synonym-cycling rule: repeating *your own phrasing* is human; cycling synonyms for *legal terms* is not.

### Impersonality and register

**Stay impersonal — no first person.** Do not write "I think", "in my view", "I would argue". Use the examiner-endorsed forms: "a better view is…", "it is suggested that…", "it is arguable that…". Strike a balance between formal and informal. No slang; define any abbreviation on first use.

### Rewording

**Interpret the law into your own words** — do not quote or closely track the manual's wording. Per the guidance booklet: *"ensure that any content that is not in your own wording has been appropriately referenced, this includes any materials provided as part of the course."* Anything genuinely quoted must sit in quotation marks and be attributed; everything else must be properly reworded. **Limited marks are awarded for answers over-reliant on the course material** — show application of knowledge, not reproduction. This rule does not apply to drafting sub-parts, where reproducing the precedent is the point.

## When the rules conflict

If the reword / own-words rule and the precedent-fidelity rule point in opposite directions, **precedent-fidelity wins for drafted documents**. Article-accurate or "improved" wording does not override the wording of the named precedent. Reword only the substantive legal explanation that surrounds or follows a draft, never the drafted document itself.

## Citation form

- **Cases:** name + (year) where the materials give it, the relevant facts, and the outcome — then **relate the outcome to the point**. Don't retell the parties' background or a judge's dicta. Don't reuse one case for every point. The manual's own form is e.g. *Trevor v Whitworth (1887)* — match it.
- **Statutes:** section + full Act name + year. The manual's own form is e.g. *section 61 of the Companies Act 1948*; the booklet's *section 31 Trustee Act 1925* form is equally fine. Standard abbreviations are fine (IHTA 1984, LPA 1925); don't repeat the Act once context makes it clear.
- **Latin** only where there's no real alternative (a proper name or special meaning), e.g. *donatio mortis causa*, *sui juris*.
- In the essay body, **never cite the course manual itself or page numbers** — write as a candidate. Source attribution belongs only in the check panel. (Article numbers from articles attached to the question itself may be cited in the body; they are part of the question, not the manual.)

## Practices to avoid

Don't retype/repeat the question; no long introductions; no irrelevance or ambiguity; not too much / too little / irrelevant authority; don't over-tell case stories; never jump to a conclusion and never omit one; keep a logical order with proper paragraphs; mind grammar (tenses, singular/plural, a/the).

## Done when

Run this before handing over. Every box must pass.

**The booklet's own five questions — answer yes to all:**

- [ ] Have I addressed all the issues?
- [ ] Have I given all the necessary information?
- [ ] Have I stated the law fully enough?
- [ ] Have I applied the law to the facts of the problem in this question?
- [ ] Have I dealt with all possible interpretations of the facts?

**Then the mechanical sweep of the SUBMIT block:**

- [ ] Every sub-part answered; each obeys its own command word; drafting sub-parts built from the opened Appendix file, not memory (drafting checklist run).
- [ ] There is a conclusion, reached once, at the end — not jumped to, not omitted.
- [ ] Search the block for every banned word/phrase (both era-clusters) and for "—", "–", curly quotes/apostrophes and "…": zero hits. Ordinary keyboard characters only (no zero-width or non-standard space characters). British spelling throughout; no bold, bullets or other markdown residue.
- [ ] No three consecutive sentences of the same length; no two consecutive paragraphs opening the same way; paragraphs visibly uneven in length.
- [ ] Most paragraphs start bare — count the paragraph-initial connectives; sentence-initial "However," appears at most twice.
- [ ] The question's names, figures and dates thread through the whole answer; no paragraph passes the portability test (none could be pasted under a different question).
- [ ] Hedging is uneven and earned, at least one committed critical remark is present, and the essay's two-or-three pet phrases recur.
- [ ] Legal terms repeated precisely, not synonym-cycled; no first person; no vague attribution.
- [ ] Every authority named in the block appears in the course materials (nothing invented) and is listed on the Authorities line.
- [ ] No source tag, module number, or page reference anywhere in the block.
- [ ] Check panel complete: Authorities cited, Source, Cross-checked, Confidence, Verify.
