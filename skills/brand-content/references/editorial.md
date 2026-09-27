# Editorial and bilingual rules

## Arabic

Use plain, readable Arabic. Prefer “ماذا” over “وش” or “إيش”; “كيف” over dialect alternatives; “نحافظ على” or a precise action over “نصون”. Avoid “عشان” in Saudi-facing written content. These are editing preferences, not search-and-replace instructions for quotations.

Names and established terms stay English: Figma, Google, AI Agent, Design System, Prototype, API. Do not translate them to meet a language-purity rule. Arabic UX search phrases may remain Arabic.

Mechanics:
- Keep Arabic in logical Unicode order. No presentation-form characters, no decorative tatweel.
- Use Arabic punctuation (، ؛ ؟) and one numeral system per piece.
- Numeric ranges inside Arabic text use an ASCII hyphen (25-34). The en dash is bidi-neutral and can render the range reversed.
- Check mixed-direction punctuation where English names meet Arabic text.
- Arabic tracking is zero; account for its line-height in design handoff.

Write from the idea, not from English grammar. English adaptations preserve qualifications, sources and the difference between observed results and proposals. They may reorder examples for clarity but may not invent another first-person history.

## Human voice: no AI tells

Copy must read as written by a careful human editor, in both languages. These patterns mark text as machine-written; remove them before delivery.

**Punctuation**
- No em-dashes (U+2014), in any language or channel. Use a comma, period, colon or parentheses. Rewrite the sentence if none of those fits.
- No emojis in headlines, body copy, subject lines or captions.
- No exclamation marks doing the selling, no ALL-CAPS urgency.

**Structure**
- No reflexive triads (“fast, simple and powerful”). One strong claim beats three padded ones.
- No “not just X, but Y” / “it's not X, it's Y” reframes, and their Arabic twins «ليس مجرد... بل» and «لا يقتصر... بل».
- No symmetric paragraphs or mirrored sentence openers. Vary length and rhythm the way an editor would.
- No summary that restates the heading, and no conclusion that repeats the introduction.
- Commit where the evidence allows. Hedging every sentence (“may help”, “can enable”) is as weak as overclaiming; keep qualifications where the evidence is genuinely uncertain.

**Vocabulary**
- English: seamlessly, effortlessly, robust, truly, cutting-edge, revolutionary, game-changing, world-class, leverage, elevate, unlock, empower, delve, tapestry, “navigate the complexities”.
- English openers and closers: “In today's fast-paced world”, “In conclusion”, “At the end of the day”.
- Arabic: «في عالم اليوم المتسارع»، «في ظل التطورات المتسارعة»، «تجدر الإشارة إلى»، «من الجدير بالذكر»، «مما لا شك فيه»، «يلعب دورًا محوريًا»، «نقلة نوعية»، «في الختام».

These lists are signals, not a thesaurus swap. Replacing “leverage” with “utilise” keeps the problem. Fix the sentence by saying something specific.

## Specificity

- Open with a useful problem, decision or concrete scenario.
- Explain who does what and why it matters. Delete generic claims that fit any competitor: if a competitor could paste the sentence over their logo, sharpen it.
- Preserve useful qualifications; never replace uncertainty with confidence the evidence does not support.
- No fake mistakes, personal anecdotes, user quotes, research participants or client results.

Review each paragraph for contribution: new evidence, explanation, example, implication or action. Merge repetition. Preserve the writer's point of view; an authored piece needs the author's confirmation for newly introduced first-person claims.

## Headlines

Headlines must match the actual argument and intent. Separate reader-facing H1, shorter SEO title, email subject and thumbnail line when they have different jobs. Never silently change one while leaving a contradictory old title in delivery fields.

## Checking

`scripts/review_copy.py` flags em-dashes, Arabic range dashes, emojis, repeated sentence openers and the phrase lists above. Kinds ending in `_review` need judgment: a quotation or a verbatim calibration sample can match legitimately. A clean run is not proof of quality; read the copy.
