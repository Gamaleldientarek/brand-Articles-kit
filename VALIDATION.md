# Validation — 1.0.0

Completed during packaging:

- Nine Python unit tests passed, including Arabic/English copy handling, explicit length limits, CSV/XLSX reading, row provenance, duplicate columns, unknown metrics versus zero and input-file preservation.
- The bundled Codex skill validator passed the skill's structure/frontmatter checks.
- `skills@1.5.25` discovered one skill and installed it in project scope for Codex and Claude Code using copy mode. Installed skill files matched the source bytes.
- Package review checked relative references and excluded personal machine paths, client document/card IDs, private keys, token literals and unfinished scaffold text.
- Editorial review checked independent AZMX/Colab profiles, the three channel workflows, narrow-edit behavior, factual caveats, keyword provenance and optional tool delivery.

Remote private-repository installation will be recorded after the repository is created and that test completes.

Limits: unit tests and installer tests do not establish model-output quality. No independent end-to-end article/email/website generation trial in both Codex and Claude Code has been completed. The manual scenarios in `tests/behavioral-cases.md` are available for that next evaluation. No live client card or document was changed while testing this package.

NPX tests are project-scoped and isolated from personal global skill installations. Optional XLSX support was exercised with an existing openpyxl runtime; the official validator used PyYAML in a temporary environment. These are developer validation dependencies, not mandatory installations for ordinary writing.
