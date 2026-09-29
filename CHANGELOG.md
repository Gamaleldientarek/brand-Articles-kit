# Changelog

All notable changes to the brand-content skill. Versions follow semantic versioning: a major bump changes a default a user relies on, a minor bump adds capability, a patch fixes wording or tooling.

## 1.3.0 (2026-09-29)

**Added**
- Card-field gate in `clickup-workflow.md` section 8: a table of the article card's fields (Brand, Author Name, Content Type, Target Audience fields, Persona, AR and EN title fields, SEO Keywords, Publication Date) with the plan section each value comes from. It runs before an article card moves into the design-handoff status or any later status, including a plain move request, and passes when every found row holds a value on read-back. Only two rows may stay empty, both named in the report: Publication Date until a date is agreed, and a title row for an edition outside a recorded language limit. Any other empty row holds the move until it is set or the user answers. Earlier status moves are not gated.
- Field discovery: the map combines the card's own read, the list, folder and space listings and a filled card of the same type in the same space; a field counts as found even when the card does not show it yet; a same-name duplicate uses the user-designated field or is asked about; every value is confirmed on read-back.
- A blocked-field path: a found field that cannot be set holds the move and is reported; missing title or Content Type fields hold the move until the user answers; no custom fields are created. Required fields outside the table are reported, never guessed.
- Behavioral case 13 for fields a list listing does not show.
- The package leak test also rejects UUIDs and numeric IDs of 12 or more digits, which covers custom-field IDs and long list IDs. Bare task IDs are still caught only inside task URLs.

**Changed**
- Preservation rule for card fields: empty rows are filled; existing values are kept; a title or SEO Keywords value that disagrees with the current draft is updated only when the session set or changed that H1 or chose that keyword cluster, or the user asked for the change; otherwise the mismatch is reported and holds the move until the user answers. Judgment values (Persona, a single-choice audience) come from the editorial plan's lead audience and are named in the report.
- Narrow edits change only the fields the request touches (a title change updates its title field) and may move status when asked; a move that triggers the gate runs it first.
- Section 1 now reads the card's own custom fields as well as the list metadata. Section 9, `delivery.md`, `quality-checklist.md` and SKILL.md (step 5 and the routing table) use the same trigger wording, and `articles.md` points to the gate. Behavioral case 6 now expects empty card fields to be reported, not filled, in a narrow edit.

**Fixed**
- A full handoff could finish with the AR and EN title fields empty, because field discovery relied on the list listing alone and the title step read as optional.

## 1.2.0 (2026-09-27)

**Added**
- `references/quality-checklist.md`: one pre-delivery pass/fail list covering scope, brand, facts, language, voice and separation, plus article, email, website and remote-delivery sections. SKILL.md now ends every task with it.
- Human-voice rules in `editorial.md`, in English and Arabic: em-dashes banned outright, no emojis in copy, no “not just X, but Y” or «ليس مجرد... بل», named banned vocabulary in both languages, no mirrored openers or heading-restating summaries.
- `review_copy.py` checks: `em_dash`, `arabic_range_dash`, `emoji_review`, `english_ai_pattern_review`, `arabic_ai_pattern_review`, `repeated_opener_review`, a broader English stock-phrase list, `issue_counts`, line-ordered output and `--format text`.
- AI-tell before/after rewrites in `examples.md` (English, Arabic, email subject, Arabic range).
- Behavioral cases 11 and 12 for voice cleanup and sub-brand routing.
- Tests: seven helper tests for the new checks; package tests for em-dash-free instructions, version agreement and reference routing.

**Changed**
- SKILL.md description rewritten with explicit “use when” triggers and Arabic request phrases so the skill loads reliably; out-of-scope uses listed.
- SKILL.md body reorganised into six numbered steps with a task-to-reference routing table.
- `azmx.md` synced with azmx-brand: parent house of Colab, Majarah, Clix and Anatomi; the Four Dimensions voice model; house rules (no emojis, three hashtags maximum, no mandatory CTA); five secondary palettes; gradient and image-text rules; ask before adding icons.
- `colab.md` synced with colab-design 4.4.1: voice dimensions and purpose modes; Electric Green never behind body text and Deep Jade text on Electric floods; Olive Green on light grounds; legacy fonts excluded; ASCII hyphen in Arabic ranges; motif on content pages is an open client question; A4 poster system.
- `brand-sources.json` re-hashed against upstream heads, profile version aligned with the skill version, Colab colour and RTL references added.
- README rewritten: quick start first, flow diagram, modes and file map, troubleshooting, release steps.

**Fixed**
- `openai.yaml` display name no longer uses an em-dash.
- README no longer claims earlier release tags exist.

## 1.1.0 (2026-09-10)

- Detailed source-research method and research-plan template.
- ClickUp lifecycle from Idea to Blog & Design Ideation with exit criteria, field discovery, bilingual review, designer handoff and continuation.
- GitHub Actions: Python 3.11/3.13 helper and package tests; copy and symlink installation checks for Codex and Claude Code.

## 1.0.1

- Explicit linked brand-skill names, repository links and runtime resolution instructions.

## 1.0.0

- Initial package: articles, emails and website copy for AZMX and Colab; editorial and brand profiles; `review_copy.py` and `keyword_inventory.py`; installer verification.
