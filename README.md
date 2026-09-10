# Brand Content

Private writing skill for **AZMX** and **Colab**, built around articles, emails and website copy in Arabic and English. Version **1.0.1**.

## What it does

- Articles: angle, research, keyword clusters, drafting, bilingual review, metadata, designer summary and two-image briefs.
- Emails: subjects, newsletter preheaders, complete body copy and appropriate next steps. Drafting does not send messages.
- Website copy: page purpose, hierarchy, section copy, CTA labels, relevant microcopy and search metadata.
- Focused review/adaptation and optional Google Docs/ClickUp handoff without restarting completed work.

Each brand has a separate editorial profile and visual-brief baseline. Full artwork still uses the current complete brand skill and approved assets. This package contains no client articles, keyword spreadsheets, credentials or workspace IDs.

## Linked brand skills

| Brand | Skill | Repository | Direct instructions |
|---|---|---|---|
| AZMX | `azmx-brand` | [GitHub](https://github.com/Gamaleldientarek/azmx-brand) | [SKILL.md](https://github.com/Gamaleldientarek/azmx-brand/blob/main/SKILL.md) |
| Colab | `colab-design` | [GitHub](https://github.com/Gamaleldientarek/colab-design) | [SKILL.md](https://github.com/Gamaleldientarek/colab-design/blob/main/SKILL.md) |

Brand Content loads the appropriate installed brand skill, or reads the linked source when needed. These links do not automatically install either skill. The brand skills supply identity and voice; this skill supplies the content workflow. Current user instructions remain authoritative.

## Install on Codex and Claude Code

Prerequisites: Node.js/npm, Git, and GitHub access to this **private** repository. Authenticate using your existing Git credential helper, GitHub CLI or SSH configuration. Do not paste tokens into the command or commit them.

```bash
DISABLE_TELEMETRY=1 npx skills@1.5.25 add Gamaleldientarek/brand-content-kit --skill brand-content --agent codex claude-code --global
```

The public `skills` CLI is the installer; the skill contents are fetched from this private GitHub repository. There is no public npm package containing this skill. Installation does not connect Google Docs, ClickUp, search providers or email accounts.

To install only in the current project, omit `--global`. Use `--copy` when copies are preferred over the installer's default symlinks. Open a fresh agent session if the new skill does not appear in an existing session.

## Use

Codex:

```text
Use $brand-content to write an AZMX article from this report, in Arabic and English, with a keyword plan and designer handoff.
```

Claude Code:

```text
/brand-content اكتب إيميل لكولاب يدعو فريق المنتج لمراجعة سؤال البحث. أريد الموضوع والمتن فقط.
```

Website copy:

```text
Use brand-content to write the Arabic and English copy for these two AZMX service pages. Use only the supplied service facts and flag missing proof separately.
```

Focused editing:

```text
Use brand-content to improve only the image briefs and add a four-sentence Arabic summary to each article card. Preserve the article body and status.
```

NPX installs into local agent environments, including Claude Code; it does not install directly into a claude.ai chat. The portable skill directory can be packaged for another supported interface, but that interface's upload and tool requirements need separate validation.

## Defaults you can override

- Easy standard Arabic for Saudi readers; English company/tool/technical names retained.
- A long Article generally has 2,000–2,500 body words per edition; authored Blog Posts may be shorter.
- Full article packages normally include Arabic and English. Other channels use requested languages.
- Four-sentence Arabic designer summary; two images by default, maximum three unless requested otherwise.
- Card description: summary, article link, Thumbnail Brief and Image Brief.
- Article document tabs: Arabic, English, SEO Plan, Thumbnail Brief, Image Brief; Research & Review when useful.

Current user instructions always override defaults. No AI-detector guarantee, invented metrics or automatic publishing.

## Optional helpers

Run from the installed skill directory:

```bash
python3 scripts/review_copy.py article.md --min-words 2000 --max-words 2500
python3 scripts/keyword_inventory.py inventory.csv --query "تجربة المستخدم"
python3 scripts/keyword_inventory.py inventory.xlsx --sheet Inventory --query "design system"
```

Copy review and CSV reading use the Python standard library. XLSX needs `openpyxl` in the chosen Python environment. The scripts are read-only. They do not validate search demand, facts, SEO success or authorship. Word counting is an estimate with documented exclusions.

## Integrations and privacy

The skill uses whichever authenticated tools the host exposes, discovered at runtime. It does not bundle an MCP server or credentials. Missing integrations are reported, and locally possible work can continue.

Keep task outputs and local configuration outside this repository, for example in an ignored `private/` or `runs/` directory. Do not copy the user's personal agent repository into this package. Private GitHub access controls distribution; it does not make model-provider processing local.

## Versioning and updates

The current release is tagged `v1.0.1`; `v1.0.0` remains available. Re-run the tested add command to install the current repository version; inspect the installer's changes before replacing a locally modified skill. A project can install from the tag URL to request that release:

```bash
DISABLE_TELEMETRY=1 npx skills@1.5.25 add https://github.com/Gamaleldientarek/brand-content-kit/tree/v1.0.1/skills/brand-content --agent codex claude-code
```

Keep improvements in the repository, not only in installed copies. Review source-profile changes against `references/brand-sources.json`, update the version, run checks and publish a new tag. The original upstream brand repositories are not modified by this package.

## Development and validation

```bash
python3 -m unittest discover -s tests -v
```

See [validation notes](VALIDATION.md) for what was actually tested. [Behavioral cases](tests/behavioral-cases.md) describe future model-output evaluations; they are not automatic test results. Agent Skills structural validation does not prove editorial quality.

Sources: [Agent Skills specification](https://agentskills.io/specification), [skills installer](https://github.com/vercel-labs/skills), [Claude Code skills](https://code.claude.com/docs/en/skills).
