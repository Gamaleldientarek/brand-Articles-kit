# Delivery and resuming work

For an authorized full article workflow, use [clickup-workflow.md](clickup-workflow.md) to determine the next incomplete phase and its readiness criteria. This reference covers the mechanics shared by full workflows and narrow edits.

Remote delivery is optional. Discover current tools and credentials; do not hard-code MCP tool names, account IDs, machine paths or ClickUp field IDs. Do not request secrets in chat.

## Capability preflight
Identify the actual card/document from supplied links and confirm brand/author. Read current content, all document tabs and relevant custom fields/status options. Preserve unknown fields and user edits. If access is unavailable, draft locally and state what is missing; never simulate a remote update.

## Google Docs
Follow the environment's native document skill/tool requirements when available. Edit existing files in place unless a new file is requested. Keep tab titles/order and rich content outside the authorized edit unchanged.

Article tabs: Arabic; English; SEO Plan; Thumbnail Brief; Image Brief. Add Research & Review only when useful. Do not add empty tabs for an explicitly single-language or narrow task.

Use native headings, links and RTL paragraph direction. Keep briefs/metadata out of article text. Resolve ranges from a fresh read; use revision guards where supported. Verify content and untouched tabs after edits. Do not flatten a native multi-tab document through a lossy conversion.

## ClickUp
Default article-card description:
1. 3–5-sentence Arabic summary.
2. Link to the current article file.
3. Thumbnail Brief.
4. Image Brief.

Keep detailed research/SEO in the document, not repeated in the card description. Preserve a material publication dependency in the review artifact; removing card clutter must not erase the only record of it.

Before an article card moves into the design-handoff status or any later status, run the card-field gate in [clickup-workflow.md](clickup-workflow.md) section 8, following its discovery and preservation rules. In a narrow edit, change only the fields the request touches (a title change also updates its title field), leave the rest unchanged, and report empty rows. Map fields by observed name AND type/scope. Similar duplicate fields can exist at task-type and list level: prefer the user-designated fields; if ambiguous, resolve before writing. Do not assume dropdown labels are API values. Read the card back after writing.

Change workflow status only when requested or included in an authorized full workflow. A move into the design-handoff status or any later status first runs that gate. Discover valid options and preserve assignments/dates. “Design ideation” is not publication approval.

## Reliable continuation
Use a local task note outside the skill repository recording artifact URLs, language/stage, last verified revision and remaining work. This is task state, never package content. Before creating a file on retry, check whether the prior creation succeeded. On uncertain writes, read back before repeating. Stop and report unresolved failures after bounded retries; don't create duplicates.

Follow the user's authorization for document/card edits. Email sending, live publishing and new external actions are not authorized by installing or invoking a skill. Present the concrete artifact before requesting any genuinely missing approval.
