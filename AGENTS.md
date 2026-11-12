# AGENTS.md

Guidance for any AI coding agent working in this repository.

## Project

`evidence-triage` is a public agent-skill package for internal audit and
fraud work. It is Markdown-first: `SKILL.md` routes each request, and
`references/` holds the phase procedures and the evidence and findings
rules. There is no application runtime and no build step.

## Commands

```bash
# Validate the skill structure, assets, and secret patterns
python scripts/validate_skill.py

# Lint all Markdown
npx markdownlint-cli2 "**/*.md"
```

CI runs both. Keep them passing.

## Conventions

- **Public repository.** Use synthetic examples only. Never add
  employer, client, customer, or personal data, internal system or table
  names, tuned thresholds, or real investigation outputs. See
  [CONTRIBUTING.md](CONTRIBUTING.md).
- **Skill frontmatter.** `SKILL.md` must keep `name: evidence-triage`,
  a trigger-rich `description`, and a `version`.
- **Reference parity.** Every `references/*.md` file must appear in the
  `SKILL.md` reference table, and every listed file must exist.
- **Bilingual README.** `README.vi.md` mirrors `README.md`. Update both
  when the structure or install steps change.
- **Reference translations.** `references/X.vi.md` pairs with
  `references/X.md`. Update both when the English source changes.
- **English source of truth.** English docs use American English and
  sentence-case headings.
- **No emoji icons.** Use plain text. Do not use emoji as visual
  elements in documentation.
- **Standards.** Cite public frameworks and paraphrase them. Do not
  reproduce paywalled or proprietary text.
- **Evidence discipline.** Keep fact, inference, and opinion separate.

## File map

```text
SKILL.md                       Router and shared principles
references/hunting.md          Phase: hunting
references/triage.md           Phase: triage
references/investigation.md    Phase: investigation
references/linkage-attributes.md
references/fraud-patterns.md
references/output-conventions.md
references/audit-evidence.md   Audit evidence and workpapers
references/audit-findings.md   Finding structure and reporting
references/audit-index.md      Audit reporting set: reading order
references/audit-*.md          Engagement, evidence, claims, report, review, release
CONTRIBUTING.md                Public-repo rules, redaction, and review
SECURITY.md                    Exposure reporting and incident process
scripts/validate_skill.py      Repository validator
docs/ARCHITECTURE.md           Component and flow overview
docs/GITHUB_SETUP.md           Manual GitHub settings checklist
.github/                       Templates, labels, CI
assets/                        Banner and social preview
```

## Caveats

- Do not rename a reference file without updating `SKILL.md`, both
  READMEs, and the validator's expectations.
- Do not remove either copyright line from `LICENSE`.
- Do not add organization-specific content to the public repository.
  Use a private overlay instead.
- Only commit PNGs for the banner and social preview. Keep the SVG
  source.
