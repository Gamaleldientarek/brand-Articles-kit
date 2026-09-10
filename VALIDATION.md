# Validation history

## 1.1.0 workflow and CI

Added a detailed source-research method, editorial-plan template and ClickUp lifecycle with phase exit criteria, field discovery, bilingual review, designer handoff, continuation and publication boundaries.

GitHub Actions is configured for Python 3.11/3.13 helper/package tests and copy/symlink installation checks on both agent paths. A configured workflow is not a successful run; consult the repository's Actions page for the actual run conclusion. These automated checks do not execute model-based writing evaluations or client mutations.

## 1.0.1 reference update

Verified both upstream SKILL.md paths through GitHub's contents API. Added explicit skill names, repository links, direct entrypoint links and runtime resolution instructions to the main skill, profiles and README. The structural validator and whitespace checks passed. Helper scripts and installer behavior did not change; the installation and unit-test results below describe 1.0.0.

## 1.0.0 packaging results

Completed during packaging:

- Nine Python unit tests passed, including Arabic/English copy handling, explicit length limits, CSV/XLSX reading, row provenance, duplicate columns, unknown metrics versus zero and input-file preservation.
- The bundled Codex skill validator passed the skill's structure/frontmatter checks.
- `skills@1.5.25` discovered one skill and installed it in project scope for Codex and Claude Code using copy mode. Installed skill files matched the source bytes.
- Package review checked relative references and excluded personal machine paths, client document/card IDs, private keys, token literals and unfinished scaffold text.
- Editorial review checked independent AZMX/Colab profiles, the three channel workflows, narrow-edit behavior, factual caveats, keyword provenance and optional tool delivery.

Remote test passed: `skills@1.5.25 add Gamaleldientarek/brand-content-kit --skill brand-content --agent codex claude-code --yes` fetched the authenticated private repository into a fresh project directory, installed the universal Codex skill and the Claude Code symlink. All installed skill files matched the source. GitHub's repository metadata confirmed private visibility before upload.

The tagged-release URL is provided as the installer's supported source format; the tested remote command above used the repository's main branch. Personal/global installation was intentionally not performed.

Limits: unit tests and installer tests do not establish model-output quality. No independent end-to-end article/email/website generation trial in both Codex and Claude Code has been completed. The manual scenarios in `tests/behavioral-cases.md` are available for that next evaluation. No live client card or document was changed while testing this package.

NPX tests are project-scoped and isolated from personal global skill installations. Optional XLSX support was exercised with an existing openpyxl runtime; the official validator used PyYAML in a temporary environment. These are developer validation dependencies, not mandatory installations for ordinary writing.
