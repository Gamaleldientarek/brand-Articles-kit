# ClickUp article workflow: Idea to ready for design

Use this for an authorized full article workflow or to identify the next incomplete phase. It is not a command to move every card or repeat completed stages. For a targeted edit, preserve the current workflow state unless asked otherwise.

## What ready means

The default endpoint of writing work is **ready for editorial/design handoff**: complete requested article editions, reviewed factual claims, SEO plan, final draft titles, designer summary, two distinct image briefs and a verified document/card link.

That is not designed artwork, author approval, SEO implementation or publication. If a source PDF still needs correction, the article may be ready for design with that dependency recorded; the download/publication remains blocked.

## 1. Read the real task before changing it

Open the supplied task ID/link. Read description, brand, content type, author, title fields, keywords, audience, dates, assignments, attachments and subtasks relevant to the request. Read pertinent comments when they contain editorial decisions; do not post a comment unless authorized.

Discover the list's available statuses and field metadata, and read this card with its custom fields; neither is a complete inventory (see section 8, Field discovery). Identify whether title fields belong to the list or to the task type. Duplicate labels do not prove identical fields. Use the fields designated by the user; map their current IDs and values at runtime.

Follow the current article/report link and enumerate every document tab before editing. Find the actual Arabic and English editions, research, SEO and brief tabs. Note existing user edits and gaps. Do not create another document simply because an older conversation used a different title.

Determine the scope from the latest request: research only, plan only, writing, English adaptation, review, briefs, or the full workflow. Load the selected brand's linked skill. Ask only about a consequential unknown such as an ambiguous brand or missing commercial fact.

## 2. Enter Research when research work is authorized

Typical observed stage: **Research**. Use the actual available label/value, not a hard-coded string. Do not move a later-stage card backwards just to replay the diagram.

Follow [research.md](research.md): inspect source material, frame the questions, find and read current sources, test significant claims, inspect the keyword inventory and identify uncertainties. Record report corrections separately from the new article.

Choose **Article** or **Blog Post** based on the required argument, source material and author voice. A longer researched explanation usually needs an Article; a focused first-person account may work better as a shorter Blog Post. Map the actual content-type dropdown value when updating the field.

Research exit: the main claims are supportable, the angle is useful, the audience is clear, the keyword group is justified and the remaining uncertainties are explicit. Do not move to writing with invented facts filling essential gaps.

## 3. Build a reviewable editorial plan

Write the audience, central question, takeaway, proposed AR/EN titles and format rationale. Lay out the sections in an argument that progresses, with the job of each section and approximate word allocations when the target is long-form.

Plan the opening scenario, evidence placement, practical application, reader's next step if useful, and the distinction from related articles. Use a connected hypothetical example where it clarifies the topic; do not imply a case study exists.

Map keywords to relevant sections and identify internal-link opportunities. State proposed slugs rather than pretending they are published URLs. Propose the cover's job and the internal image's explanatory job; refine their composition after the article is stable.

For a plan-only request, stop with the completed plan and keep the card at the appropriate stage. For an authorized full workflow, continue without asking whether to begin each already-authorized step.

## 4. Write in Blog Writing

Typical observed stage: **Blog Writing**. Read [articles.md](articles.md) and [editorial.md](editorial.md).

Write the complete requested edition, normally Arabic first in a full bilingual package. Long-form default is 2,000–2,500 body words; do not pad a shorter authored format to this range. Keep metadata and briefs outside the body.

Attach direct factual citations, preserve limitations and identify the hypothetical example. Remove generic intros, repeated conclusions and unsupported universal claims. Write names and technical terms in English while keeping natural Arabic keyword phrases.

Review the first edition, then adapt into English with equivalent claims and qualifications, an appropriate English keyword group and independent sentence structure. Do not recreate the first author's personal history in the adaptation. If the user requested one language only, do not add another.

## 5. Run the editorial and SEO review

Check argument, usefulness, brand, clarity, paragraph rhythm, evidence, source links and terminology. Review Arabic as written Arabic, not English grammar wearing Arabic words. The preferred register is easy standard Arabic; avoid dialect-heavy or ornate wording.

Check the body length of each requested edition separately and state what the count excludes. Automated checks are signals, not a human-authorship certificate. No detector-proof promise.

Revisit final titles now that the argument is settled. Align H1 and card title fields to the final draft, while allowing shorter SEO titles to serve their own role. The team's usual card name is English, with both language titles in their designated fields; preserve an explicitly different naming choice.

Complete the SEO plan: historical versus newly validated data, keyword placement, AR/EN metadata, proposed slugs, real/pending internal links, publication implementation notes and meaningful measurement. Do not fabricate missing volumes or claim schema/canonical work was deployed.

For an authored article, flag new first-person statements needing the author's confirmation. A prepared draft is not author approval.

## 6. Prepare the designer's handoff

Write a simple Arabic summary in 3–5 short sentences, normally four. Cover topic, problem, example/approach and takeaway in approximately 45–75 words.

Use [visual-briefs.md](visual-briefs.md) for a cover and a distinct internal image, normally two total and at most three unless requested otherwise. Specify the idea, visible scene, hierarchy, short image copy in requested languages, actual section placement, brand treatment, mobile/crop considerations and alt text.

Avoid a vague “human and AI collaboration” instruction. Name what is on the canvas and what the viewer should understand. Do not show percentages or chart lengths that imply measurements not in the article. Written briefs do not imply artwork has been produced.

## 7. Put current content in the document

Read [delivery.md](delivery.md) and the host's native document guidance. Reuse the existing file or create one when authorized and none exists. Full bilingual packages use Arabic, English, SEO Plan, Thumbnail Brief and Image Brief tabs. Retain useful Research & Review notes for claims, sources and blockers.

Preserve native tab structure and content outside scope. Use actual native headings and links, Arabic RTL direction and correct index ranges. Re-read after index-changing operations and use revision guards where supported.

Confirm article text did not absorb briefs, metadata or internal instructions. English CTA must identify an Arabic-only PDF accurately. If a source asset needs correction, keep a clear review note before removing duplicated notes from the card.

## 8. Simplify the card and update designated fields

The description contains only the current Arabic summary, article link, Thumbnail Brief and Image Brief. Detailed research/SEO remains in the linked document. Do not retain an obsolete raw draft beneath the current brief unless explicitly requested; preserve a reference copy locally or in an authorized source artifact before replacement.

### Card fields: a gate before the design handoff

The gate runs before an article card moves into the design-handoff status (section 9, typically observed as Blog & Design Ideation) or any later status, whether that move is part of a full workflow, a complete-package request or a plain request to move the card. Until it passes, the card does not move. Earlier status moves are not gated.

The gate passes when every field in the table below that field discovery found holds a value on a fresh read-back. Two rows may stay empty, each named in the report: Publication Date, until a real date is agreed, and a title row for an edition that is out of scope. Any other empty row holds the move until it is set or the user answers. A field counts as found even when the card does not show it yet. An edition is out of scope only when a language limit is recorded in the request, the card or the document; otherwise both title rows apply, and a missing edition is asked about before the move.

Anything else on an existing card is a narrow edit. Change only the fields the request touches; a title change also updates its title field. Leave other fields unchanged, and the status unless the request moves it; a move that triggers the gate runs it first. Report any empty rows by name.

Field names are as observed on the team's article cards; map their IDs at runtime and never write them into this skill.

| Field | Value | Source |
|---|---|---|
| Brand | the resolved brand | section 1 |
| Author Name | the confirmed byline, a person or the brand; ask if unknown | section 1 |
| Content Type | Article or Blog Post | section 2 |
| Target Audience fields (text and dropdown, where both exist) | the audience in the editorial plan | section 3 |
| Persona | the lead audience in the editorial plan | section 3 |
| AR Article/Blog Title | the final Arabic H1 | section 5; update whenever the title changes |
| EN Article/Blog Title | the final English H1 | section 5; same |
| SEO Keywords | the chosen cluster; provenance labels stay in the SEO Plan tab | section 5 |
| Publication Date | a real, agreed date only | when agreed |

**Field discovery.** Neither a list's field listing nor a card's own field read is a complete inventory: a card can accept task-type, folder or space fields it does not show until they hold a value. Build the field map from this card read with its custom fields, the list, folder and space listings, and a recent card of the same task type in the same space whose title fields are filled. A field seen only on that reference card may be task-type scoped or tied to another list; set it by ID on this card and read back to find out. If two fields share a name, use the one the user designated; if still ambiguous, ask before writing. Set values by ID, write dropdowns by option, then read the card back with custom fields and confirm every row. A field missing from the read-back counts as empty; re-read once before reporting. An update that reports success does not prove the value was stored.

**When a field cannot be set.** If a found field rejects the value, has no option that fits the plan, or is still empty on read-back, the card does not move to design; report the field name, the error and where it was found, and ask the user. If no source above has the field, report it as not used on this list; for the AR and EN title fields and Content Type, ask, and the card does not move until the user answers. Never create, rename or attach custom fields to make a row fit.

**Preserving values.** Fill a row when it is empty. Keep every existing value, plus assignees and priority. When an existing title or SEO Keywords value disagrees with the current draft, update it only if this session set or changed that H1 (or chose that keyword cluster) or the user asked for the field change; otherwise keep it, name the mismatch and ask, and the card does not move until the user answers. Any other existing value that disagrees with the plan is kept and named in the report. When a row's value is a judgment, such as Persona or a single-choice audience dropdown, take it from the lead audience in the editorial plan and name the choice in the report.

**Required fields outside the table** stay unchanged even when a value seems inferable from the work. Report each empty one by name and ask for its value; it does not hold the design move under this gate. If ClickUp itself rejects the status change because of one, leave the card where it is, report the rejection and ask.

When briefs exist both in the card and document, synchronize the authorized copies. Keep article URLs distinct from public publishing URLs. A private editing link belongs in the internal card, not in public article copy.

## 9. Verify, then mark ready for design

Read back the card and document. Check: both requested editions exist; titles are current; the URL opens the intended document; summary/briefs match; the section 8 card-field gate passes, with each row left empty named in the report; unfound AR or EN title fields or Content Type, and any title or SEO Keywords mismatch, have been answered by the user; rows found nowhere and empty required fields outside the table are named in the report; untouched tabs and task fields remain unchanged.

Typical observed target: **Blog & Design Ideation**. Transition only after the writing/brief handoff is actually complete and the full workflow or that move was authorized. Report remaining publication dependencies alongside the handoff. Do not claim Published or Approved.

## Later stages: evidence needed to move forward

| Observed stage family | Required reality, not just text preparation |
|---|---|
| Design | Actual visual production is underway within the requested scope. |
| Design Review | Artwork exists and is ready for the designated review. |
| SEO Review | The actual page/metadata/links are available for the requested publishing checks. |
| Blog Approved | The designated approval has been explicitly received. |
| Scheduling | A real authorized schedule has been set. |
| Published | The authorized public publication exists and was verified. |

These stage names describe the workflow encountered in this project. Discover the live list's options each time. Do not create or rename statuses merely to match them, and do not treat a status field as permission to publish or send.

## Continuation and failure handling

Keep a small task note outside the skill repository with current URLs, completed phase, last verified revision and next step. On resume, compare it with live state. If the user asks for a correction during work, apply it to the active task without restarting all stages.

If a create/write times out, read back before retrying. If content changed concurrently, refresh and reconcile the intended edit; never overwrite the entire document blindly. After repeated unresolved failures, report the precise action and completed artifacts. Do not substitute fake links, duplicate cards or a claimed success.
