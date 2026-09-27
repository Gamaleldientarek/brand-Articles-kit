# Pre-delivery quality checklist

Run this once, at the end, before presenting or delivering any artifact. Check only the sections that apply to the requested scope. A failed item gets fixed or reported; it never gets silently skipped.

## Every deliverable

**Scope**
- [ ] The artifact answers the latest request, in the requested language(s), channel and length.
- [ ] Nothing outside the scope changed: names, recipients, status, fields, untouched tabs and copy.
- [ ] Nothing was added that nobody asked for (extra language, SEO plan, images, CTA, hashtags).

**Brand**
- [ ] Exactly one brand profile applied. No AZMX blue or chevrons in Colab work; no Colab greens in AZMX work.
- [ ] Voice matches the brand profile's dimensions, not a generic corporate register.
- [ ] Upstream brand skill was loaded, or its absence is stated and nothing claims brand verification.

**Facts**
- [ ] Every factual claim the copy relies on has an inspected source, or is removed or qualified.
- [ ] Hypothetical scenarios are labelled. No invented participants, quotes, clients, metrics or approvals.
- [ ] Qualifications survived adaptation: “may” did not become “will” in the other language.
- [ ] Offers, dates, amounts and terms match the source exactly.

**Language and voice** (see [editorial.md](editorial.md))
- [ ] Arabic reads as written Arabic, easy standard register, English names kept in English.
- [ ] English reads as written English, not a sentence-by-sentence translation.
- [ ] No em-dashes, no emojis in copy, no “not just X, but Y” / «ليس مجرد... بل», no banned intensifiers.
- [ ] Paragraphs and sentence openers vary; no paragraph restates its heading.
- [ ] Numeric ranges inside Arabic text use an ASCII hyphen.
- [ ] `python3 scripts/review_copy.py <file> --format text` run where a file exists; every flag resolved or consciously kept.

**Separation**
- [ ] Reader-facing copy contains no research notes, internal instructions, metadata or briefs.
- [ ] Open questions and missing facts sit in a separate editorial note, not as placeholders in the copy.

## Articles

- [ ] Each edition's body length checked separately; the report states what the count excludes.
- [ ] Title, H1, SEO title and card title fields agree with the final argument.
- [ ] Keyword provenance recorded; historical values labelled historical, blanks unknown, new seeds unvalidated.
- [ ] Designer summary is Arabic, 3 to 5 short sentences (default four), about 45 to 75 words.
- [ ] Two image briefs (at most three unless asked) with different jobs; the internal image names its real section.
- [ ] Image briefs show no quantities the article does not support.
- [ ] Authored pieces: new first-person claims are flagged for the author, not presented as approved.

## Emails

- [ ] Subject is specific and accurate; the body's main point appears early.
- [ ] Preheader only for newsletters or campaigns, and it adds information rather than repeating the subject.
- [ ] Sender and sign-off are the verified ones; no recipient imported from an example.
- [ ] One clear next step when relevant, none manufactured when not.
- [ ] No fabricated urgency, open rates or personalised facts.
- [ ] Nothing was sent, scheduled or activated. The report says “draft”.

## Website copy

- [ ] Every requested page and language is complete; the work did not stop after the first page.
- [ ] Each page has one clear intent; two pages do not compete for the same intent without a reason.
- [ ] No fabricated logos, testimonials, case studies, statistics or credentials fill a proof section.
- [ ] CTA labels map to known destinations; unresolved routes are listed in the editorial note.
- [ ] Hreflang, canonical and slug items are recommendations until actually implemented.

## Remote delivery

- [ ] The document and card were read back after writing, and the link opens the intended file.
- [ ] Brief copies in the card and document match.
- [ ] Status moved only if requested or part of an authorized full workflow, and only as far as the evidence allows.
- [ ] Retries did not create duplicate files or cards.

## Reporting

State what was delivered, what was verified and how, and what remains open. Never report research complete, approved, sent, published or tested without the evidence for it.
