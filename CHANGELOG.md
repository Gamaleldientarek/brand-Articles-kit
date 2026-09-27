# Changelog

All notable changes to the brand-content skill. Versions follow semantic versioning: a major bump changes a default a user relies on, a minor bump adds capability, a patch fixes wording or tooling.

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
