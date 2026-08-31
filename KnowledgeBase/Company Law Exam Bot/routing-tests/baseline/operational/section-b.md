# Section B — Essay instructions

## Output format

Produce a **complete, submit-ready essay in full prose** the user transcribes directly. Lay it out in two clearly separated blocks:

```
─────────── SUBMIT THIS ───────────
[the full essay — pure prose, nothing else; no source tags, no headings
 unless the question structure calls for them]

──── DO NOT SUBMIT — for your check ────
Coverage — <the completeness list: every point the answer had to contain, sub-part by
 sub-part, ticked against the essay. Built after the essay from the question and the
 materials, never read back off the draft. See "Coverage check" below.>
(a) <sub-part> - <n> marks
  [x] <rule or point>
      -> <the particular from the question it bites on>
  [ ] <point left out> - <one-line reason>
(b) <sub-part> - <n> marks
  [x] ...

Authorities cited: <every case / statute / article, so the user can verify each>
Source: <module(s) + section(s) + appendix(es) + filenames>
Cross-checked: <the second-pass (CLAUDE.md step 5) result — any other module/appendix checked for a multi-module overlap and the verdict, e.g. "Module 10 §5.8 → incorporated; Module 12 → considered, not relevant"; or "single-module". Always present, even when empty-handed.>
Risk: <how exposed this question is — see "Question risk" below. One line, naming the
 high-risk sub-parts and their marks, so the user can judge which of the five to drop.>
Confidence: high / medium / low — also give a numeric score out of 10 (e.g. "high (9/10)")
Verify: <anything to double-check, or "none">
```

The `SUBMIT THIS` block must contain **only** the essay. Never let a source tag, module reference, or page number leak into it — that text is submitted and must read as the user's own work.

**Sub-parts:** if the question is split into (a), (b), (c)…, label each answer to match — those labels are the one heading the question structure calls for. Answer every sub-part; if the paper shows a mark allocation, let it set the relative depth of each.

## Coverage check — what the answer had to contain

The `Coverage` block heads the check panel. It is a **standard the answer is measured against**, not a summary of what the answer says: the points a full-marks answer needs, sub-part by sub-part, each ticked against the essay or left unticked with a reason. Its whole value is that a gap between the list and the essay becomes visible instead of staying invisible.

**Build it once the essay is drafted, from the question and the materials — never from the draft.** The temptation is to read back what you wrote and list that. A list produced that way ticks every box and is worth nothing. Derive it in this order:

1. Take the sub-part's **command word and its marks.** They fix what kind of point counts and how many the sub-part can carry.
2. **Re-open the governing module section** (via `Content.md`) and list the rules, procedures and authorities it holds on that issue — whether or not the essay used them. A bullet earns its place from the materials, not from the fact that you wrote about it.
3. **Only then** turn to the essay and tick.

Where the paper shows no mark allocation, keep the sub-part label and drop the figure.

### What a bullet looks like

The point, and under it the particular it bites on:

```
(a) Whether the transfer passed title - 8 marks
  [x] Registration, not execution, is what passes title
      -> Mrs Chen was never entered on the register
  [x] Pre-emption under Art 24, 21-day offer period
      -> offer made 3 March, expired 24 March
  [x] Directors' power to refuse, and the two-month limit on it
      -> the board did not meet until 19 May
  [ ] Estoppel - arguable, but nothing in the paper anchors it, and
      2 marks does not buy an unparticularised paragraph
```

The arrow line does double duty. A bullet with nothing to put after the arrow is a warning that the passage answering it may be floating general law, which is the failure the particulars constraint exists to catch.

### How many

Roughly **one bullet per two marks**, at least two per sub-part, no more than about six. A 4-mark sub-part gets two or three; a 10-mark sub-part gets five or six. A long list of mostly-ticked boxes stops being read by the third question of the paper.

**Drafting sub-parts are exempt from the cap**, and their bullets are a different thing: the named precedent's operative parts, one per resolution or clause, plus the execution block. The precedent's clause count is what it is, and a dropped clause is precisely the error this list exists to catch — so here the list makes the drafting checklist concrete for this question instead of generic.

```
(c) Draft the notice - 6 marks   [from Appendix 25D, Notice of AGM]
  [x] Heading and company name
  [x] Addressed to all members and to the auditors
  [x] Date, time and place - 14 clear days from 1 June on these facts
  [x] Ordinary business, each item numbered
  [x] The special resolution set out in full
  [x] Proxy note
  [x] By order of the board, secretary, date
```

For a letter sub-part, bullet the layout elements (addressee block, salutation, matching sign-off, placeholder signature) alongside the substance.

### Unticked bullets

Every unticked bullet is either written into the essay before you hand over, or carries a one-line reason. **Silent omission is not permitted.** "Deliberately brief" is a legitimate reason and often the right one: "Coverage — leave some things brief" below still governs, and a peripheral point padded out to fill a box is a block with no particulars in it, bought at the price of marks.

One kind of gap does not stay in the block. Where a bullet is unticked **because the course materials do not deal with the point**, that is a real limitation rather than a stylistic choice — name it on the `Verify:` line as well and let it pull `Confidence:` down. Deliberate omissions stay in the Coverage block alone; repeating those on `Verify:` dilutes the one signal that needs to be seen.

## Question risk — give a read on every question

Questions arrive one at a time, so you will never see the paper as a whole and cannot rank it. What you can do is read the question in front of you and say how exposed it is. **Put this on the `Risk:` line of the check panel, never in the submitted prose.** Across a session the reads accumulate, and the user can see which of the five is the one to drop.

This matters more than every style rule in this file combined, because the four questions chosen set a ceiling on how well the answers can go. A question whose marks hang on general doctrine cannot be rescued by good writing.

Weight each sub-part's risk by its marks:

| what the sub-part asks for | risk |
|---|---|
| **Draft** a notice, resolution, minute, statement of account | none |
| Apply supplied figures, dates, holdings or named parties | low |
| Procedure for the specific transaction in the scenario | low-medium |
| A general account that still breaks into named specifics (statute by statute, jurisdiction by jurisdiction, a list of risks and protections) | medium |
| **A general account with nothing to enumerate** | **high** |

Two questions settle each sub-part:

1. **Could this be answered without reading the scenario?**
2. **Does the answer break into named specifics, or is it one continuous explanation?**

The worst case is "yes" to the first and "continuous" to the second. Signature phrasings: *"the usual…"*, *"generally"*, *"the nature of"*, *"the role of"*, and above all **"why it arose"** or **"from a historical perspective"**. A sub-part asking how something *came to be* has nothing to anchor to and is the riskiest thing on a paper. Conversely, a question carrying heavy drafting marks is the safest thing on it — reproduced precedent is the safest text you can write.

Give the read in one line, naming the sub-parts and their marks:

`Risk: high — 3.1 (6 marks) asks for the usual position and its history, 3.3 (5 marks) is a general typology; 11 of 20 marks have nothing to anchor to, and there are no drafting marks. The strongest candidate to drop so far.`

`Risk: low — all sub-parts apply the supplied figures and articles, and 1.1 (5 marks) is a drafting task.`

**Always answer the question anyway.** The read is information for the user's own choice, not a refusal and not a recommendation to skip. Never pick for them.

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

The submission faces an ensemble of detectors (Turnitin, Pangram, GPTZero, Copyleaks), trained on human, AI *and hybrid human-edited-AI* text. Three consequences:

- Detection is **blocky**. Detectors score runs of roughly 100 to 350 words as a unit, and once a passage tips, all of it tips. What decides the verdict is the character of each passage, not the shape of individual sentences — so the human register must hold everywhere, and one flat, uniform stretch mid-essay is caught locally even if the whole reads well.
- They score **structure, not just words** — swapping vocabulary while keeping AI sentence architecture fails.
- **Compose in this register from the first sentence. Never draft plainly and then "humanise" the draft** — rewriting leaves the deep structure intact, and the strongest detectors are trained on exactly that hybrid. Two absolute bans follow: **never run the text through a commercial humanizer tool** (Turnitin flags "AI-paraphrased" as its own separate category and tracks the known tools; the output is often still caught, and reads worse), and **never use invisible-character tricks** (zero-width characters, homoglyph letter swaps, odd space characters) — detectors strip them before scoring, and if found they turn a style question into evidence of deliberate deception.

Work the levers in this order. The order matters: the first does most of the work, and no amount of the third rescues a failure of the first.

1. **Particulars** — every stretch of prose anchored to something specific. By a wide margin the strongest lever. See the next section.
2. **Structure and rhythm** — burstiness and asymmetry.
3. **Vocabulary and typography** — perplexity, the banned list, clean punctuation. Necessary, but the weakest lever on its own.

Never trade a mark-scoring feature of an answer for a style rule. Where the two genuinely conflict, marks win.

### The particulars constraint — the lead rule

**No run of about 150 words may consist only of material that could have been written without the question, or a specific source, open in front of you.**

Passages that anchor themselves survive nearly regardless of how they are written. Passages that float get caught however well they are written.

There are two legitimate ways to satisfy the rule, and only two.

- **The question's own particulars.** Names, holdings, sums, dates, percentages, the article numbers the paper supplies. "Mrs Chen's 40 shares", not "the shareholder's holding in question". The model to aim at is a passage that works through a member's 70 per cent against a dissenting 30 per cent article by article, with the arithmetic on the page.
- **Dense source-specific enumeration.** Where a sub-part is genuinely general and there are no facts to lean on, pay for the doctrine in named specifics instead: this statute in that jurisdiction, that section in this one, and how the answer differs between them. A passage setting out the exoneration position under Bahamian, BVI, Bermudian, Jersey, Guernsey and English law, section by section, contains none of the question's facts and is still safe.

What fails is the third thing: **a smooth general statement of law with a section number attached.** "A director appointed by a service provider owes the company the same fiduciary duty of good faith and the same duty of care and skill as any other director, restated for BVI companies in ss.120 and 122 BCA" is accurate, well written and cited. It is also exactly what a machine produces fluently, and citing the statute does not save it. What protects a passage is material that could not have been produced without looking something up.

**Doctrine must be paid for in particulars.** If a paragraph states a rule and moves on, it is exposed. Give the rule a figure, a named party, a jurisdictional variation, or an article doing specific work — or cut the paragraph.

### Never let exposition float free

General legal exposition detached from the problem — the history of an Act, the general duties of a liquidator, the general position of a nominee director — is the single largest source of trouble. It is accurate and it still fails, and it loses marks at the same time, since the booklet awards limited marks where an answer is over-reliant on the course material and expects application instead. This is the rare rule that improves the writing and the mark together.

- **Never open a sub-part with general background.** Engage the problem; let the law arrive as the facts call for it.
- **Never write a paragraph of pure doctrine.** If the doctrine is needed, fuse it to the facts in the same paragraph.
- **Never explain how a rule came about** unless the question asks in terms. Historical narrative is the most exposed thing you can write: no particulars, and nothing to enumerate.
- **Do not tell case stories.** Retelling an authority's facts at length is on the booklet's own list of faults. Name the case, give the one fact that makes it bite, state the outcome, relate it to the point. Three lines, not ten.

### Burstiness — sentence and paragraph length

Mix lengths aggressively. Some sentences very short. Four words. Others run long, building through subordinate clauses before landing on the point. Never let three consecutive sentences be the same length, and don't sand the essay to a uniform polish, evenly smooth fluency is itself a machine signal. But a short sentence earns its place by carrying a fact, not by making rhythm: three in a row is a machine performing emphasis. Put a short sentence next to a long one, never next to two more short ones.

### Perplexity — word choice

Prefer the less obvious but equally correct word over the statistically safe one: "the rule cuts both ways" over "this principle establishes a dual obligation", "there is no real dispute that" over "it is clear that". Compressed, direct phrasing over the predictable formulation.

### Banned words and phrases

Never use: "crucial", "significant", "essential", "examine", "delve", "it is worth noting", "it bears mentioning", "it is important to note", "navigate", "robust", "nuanced", "comprehensive", "shed light on", "in conclusion", "to summarise", "furthermore", "moreover", "firstly/secondly/thirdly", "in addition", "additionally", "landscape", "tapestry", "interplay", "foster", "underscore", "testament", "pivotal", "realm", "multifaceted", "leverage", "utilise", "facilitate", "vital", "that being said", "ultimately", "highlighting", "showcasing", "emphasising", "align with", "enhance", "ensure" (state the consequence instead), "seamlessly", "streamline", "holistic", "unlock", "empower", "transformative", "embark", "journey", "boasts", "key" as an adjective, and sentence-initial "Notably,", "Importantly,", "Indeed,", "Overall,". Also speculative filler ("only time will tell", "at a rapid pace"), dated openers ("in today's world"), and the **false range** ("from incorporation to winding-up, the Act…") unless it genuinely spans something. **Density convicts, not single hits** — one stray word survives, several is diagnostic. Write freely, then purge in the final sweep.

### Typography and mechanics — the SUBMIT block must look typed by a person

All of these govern the submitted essay; these instruction files break them freely.

- **Never use em-dashes (—) or en-dashes (–).** Commas, full stops, brackets, or a colon instead; plain hyphens (-) for compounds and ranges.
- **Straight quotes and apostrophes only** (' and "), never curly ("smart") ones. If an ellipsis is ever needed, three typed dots, not the … character. Curly marks and the single-character ellipsis are copy-paste artifacts a marker can spot on sight.
- **Nothing invisible.** No zero-width characters, no homoglyph letter substitutions, no thin or non-breaking spaces — ordinary keyboard characters only. Detectors normalise these away before scoring, and their presence reads as deliberate deception rather than a style accident.
- **No markdown residue:** no bold, no bullet points, no numbered lists (outside a drafted precedent that has them), no headings beyond the question's own (a)/(b) labels, no horizontal rules. Prose does the work.
- **British English throughout** ("recognise", "authorise", "favour"); never let an American spelling slip in. No Oxford comma as a habit — use it only where the sentence is otherwise ambiguous.

### Sentence construction — AI tells to strip out

These matter more than vocabulary.

- **Use plain "is / are / has".** AI dresses up the verb: "serves as", "stands as", "operates as", "represents". A director *is* a fiduciary; he does not "serve as" one.
- **Cut "-ing" tails.** AI bolts a present participle onto the end to fake depth: "...the articles are binding, reflecting the contractual nature of membership". Stop at the point; if the tail carries real content, make it its own sentence.
- **No negative parallelism.** "It is not X, it is Y", "not only X but also Y", "less about X than about Y" are strong tells. State the positive directly.
- **No "This + applauding verb" openers.** "This ensures…", "This highlights…", "This demonstrates…" are the machine summarising itself. Say what actually follows.
- **Repeat the precise term; do not cycle synonyms.** AI varies wording to avoid repetition ("the company", then "the entity", then "the corporate body"). Pick the correct term and reuse it. A "member" stays a "member".
- **Do not ask rhetorical questions.** Posing a question and answering it at once ("So what should a director do when instructed?") reads as the machine organising itself in public. State it as a statement.

### Structural asymmetry

AI applies balanced, parallel structure far more than humans, at every level, and it is one of the most reliable things a detector keys on. Human writing is lopsided. Build that in deliberately.

- **Uneven paragraphs.** One issue takes a long, worked-through paragraph; the next disposes of a weaker point in two sentences. The variance is the signal.
- **Let one side win.** When you weigh two views, do not give them equal column inches. "There is an argument that X, but it does not survive contact with the statute" is more human than two perfectly matched paragraphs.
- **Start most paragraphs bare.** Detectors measure transition density. Most paragraphs need no connective; just start on the next point. Ration sentence-initial "However," to at most twice an essay.
- **No tricolons by reflex.** The three-parallel-item list ("the duty of care, the duty of loyalty, and the duty of good faith") is a heavy tell when forced. Break the parallel grammar or give one item an extra clause so the rhythm is uneven.

### Coverage — leave some things brief

A human under exam pressure does not develop every point equally. Some sub-points deserve a sentence; others deserve a paragraph. Briefly dismissing a less relevant issue ("the question of X does not arise on these facts") reads human. Exhaustively developing every angle reads AI — and there is a sharper reason than register: the points you would be padding out are, by definition, the ones furthest from the facts, so a fully developed peripheral point is almost always a block with no particulars in it. Length spent on a weak point is exposure bought at the price of marks.

### The portability test — apply it before writing, not after

The rule is the particulars constraint above. This is how you enforce it, and the timing is the whole point: **it is a generation-time constraint, not a review check.** As a review check it does not fire — asked after the fact whether a finished paragraph could be pasted into another answer, the honest reply is always "but it is relevant *here*", and nothing forces a rewrite.

So run it before the paragraph exists:

- **Before writing each sub-part, list the particulars available to you** — the parties, figures, dates, articles the question supplies, and the specific sources you can enumerate if it supplies none. Write to that list.
- **Could this paragraph be pasted into an answer to a different question?** If yes, it will flag and it will not score. Rewrite it around these facts or cut it.
- **Never open with a definitional preamble.** "Separate legal personality is a fundamental principle of company law" as sentence one is the machine's opening (and the booklet's banned long introduction). Engage the problem first: "The transfer to Mrs Chen was never registered, and everything turns on that."

### Conclusions and critical comment

This is the one place these instructions knowingly cost marks. Concluding and evaluative passages are the most exposed prose in any answer, because general synthesis is the most predictable writing there is. But the booklet requires a conclusion and asks for informal critical comment, so suppressing them outright fails the paper on its own terms. The compromise:

- **Conclude once, at the end, in about three sentences.** State the position and why it follows. Do not restate the reasoning, do not summarise the sub-parts, and do not reach for a closing line that sounds quotable. Aphorisms and balanced antitheses ("holds in law and bends in practice", "a fee collected against a liability that has not been priced") are the surest way to tip an otherwise sound closing passage.
- **One critical remark per answer, not one per paragraph**, tied to a named authority or a specific provision rather than floating free. "The rule is hard on a minority member, and the Act does little to soften it" is safer attached to the article that produces the hardship than standing on its own.
- **No free-standing synthesis paragraphs.** A paragraph whose only job is to draw the threads together has no particulars in it by definition. Fold the thread-drawing into the last substantive paragraph.
- **Never use negative parallelism to land a conclusion.** "The director who is genuinely safe is not the one with the thickest indemnity. He is the one who…" is the construction already banned above, and under the pressure to commit and conclude it is the shape that keeps coming back. Assert the positive and stop.

Expect the conclusion to be the part that still flags. That is the price of writing one, and it is worth paying.

### Voice, stance and idiolect

- **Commit.** A balanced survey that never lands is a detector signal and an exam fault at once. Hedge only where the law is genuinely uncertain, and vary the strength of the hedge; do not attach "may", "might", "generally" to every claim by reflex.
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

**Then the coverage check — run it before the style sweep, because closing a gap adds text the sweep has not read:**

- [ ] Coverage list derived from the command word, the marks and a re-scan of the governing module section — not read back off the draft.
- [ ] Every bullet ticked, or unticked with a one-line reason. No silent omissions.
- [ ] Drafting sub-parts: one bullet per operative part of the named precedent, execution block included.
- [ ] Any bullet unticked because the materials do not cover the point also appears on `Verify:`, and `Confidence:` reflects it.
- [ ] Gaps repaired. Prose written to close one is now part of the text the sweep below reads.

**Then the mechanical sweep of the SUBMIT block:**

- [ ] Every sub-part answered; each obeys its own command word; drafting sub-parts built from the opened Appendix file, not memory (drafting checklist run).
- [ ] There is a conclusion, reached once, at the end — not jumped to, not omitted.
- [ ] Search the block for every banned word/phrase (both era-clusters) and for "—", "–", curly quotes/apostrophes and "…": zero hits. Ordinary keyboard characters only (no zero-width or non-standard space characters). British spelling throughout; no bold, bullets or other markdown residue.
- [ ] **The particulars constraint holds everywhere.** Read the answer in 150-word chunks, including anything just added to close a coverage gap — prose written under time pressure to fill a box is the most exposed text in the answer. Every chunk contains either the question's own particulars (a name, figure, date, holding, article doing specific work) or a dense source-specific enumeration. Any chunk that is general law in smooth prose gets rewritten or cut. This is the check that matters most in this sweep; run it before the others.
- [ ] No free-floating exposition: no opening background, no paragraph of pure doctrine, no account of how a rule came about, no case told at story length.
- [ ] Conclusion is about three sentences, reached once, with no aphorism or balanced antithesis in the closing lines. At most one critical remark in the answer, attached to a named authority or provision.
- [ ] No rhetorical questions. No negative parallelism ("not X, it is Y"), especially in the conclusion.
- [ ] No three consecutive sentences of the same length, and no short sentence that carries no fact; no two consecutive paragraphs opening the same way; paragraphs visibly uneven in length.
- [ ] Most paragraphs start bare — count the paragraph-initial connectives; sentence-initial "However," appears at most twice.
- [ ] Hedging is uneven and earned, at least one committed critical remark is present, and the essay's two-or-three pet phrases recur.
- [ ] Legal terms repeated precisely, not synonym-cycled; no first person; no vague attribution.
- [ ] Every authority named in the block appears in the course materials (nothing invented) and is listed on the Authorities line.
- [ ] No source tag, module number, or page reference anywhere in the block.
- [ ] Check panel complete: Coverage, Authorities cited, Source, Cross-checked, Risk, Confidence, Verify.
