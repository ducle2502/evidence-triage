# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository is

A public agent-skill package for internal audit and fraud evidence
triage. `SKILL.md` is the entry point and router. `references/` contains
the phase procedures and the audit layer. There is no build step.

## Commands

```bash
python scripts/validate_skill.py    # structural validation
npx markdownlint-cli2 "**/*.md"     # Markdown lint
```

## Editing rules

- Keep `SKILL.md` frontmatter `name: evidence-triage` and bump
  `version` for behavior changes.
- When adding or renaming a file under `references/`, update the
  reference table in `SKILL.md`, the repository structure in both
  READMEs, and any validator expectations.
- `README.vi.md` is a parallel translation, not a replacement. Update
  both.
- Use synthetic examples and generic organization language. Read
  [CONTRIBUTING.md](CONTRIBUTING.md) before adding any example.
- Cite public standards by name. Do not copy their text.
- Keep fact, inference, and opinion visibly separate.
- Do not use emojis as icons in documentation.
- Preserve both copyright lines in `LICENSE`.

## Before finishing

1. Run the validation script.
2. Run Markdown lint.
3. Check `git diff` for confidential data, real identifiers, or
   internal system names.
4. Confirm the banner and social preview still match the README.

## Do not

- Add employer- or client-specific content to this public repository.
- Replace the three-phase model without updating all phase references.
- Add automation that acts on findings.
- Commit credentials, tokens, or connection strings.
