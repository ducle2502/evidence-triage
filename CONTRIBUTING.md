# Contributing

Thanks for helping with evidence-triage. This is a public skill package
for internal audit and fraud work.

## This repo is public

Do not submit employer, client, customer, or personal data. Do not
include internal system or table names, tuned thresholds, screenshots
of internal tools, or real investigation output. Examples must be
synthetic and labeled. Read
[references/confidentiality.md](references/confidentiality.md) before
you open a pull request.

If you are unsure whether something is confidential, leave it out.

## What to contribute

- **A problem report.** The skill routes to the wrong phase, a
  reference is unclear, or an instruction produces unsafe output.
- **A reference improvement.** A typology, linkage attribute, evidence
  rule, or finding pattern is missing or wrong.
- **An audit-layer improvement.** Evidence standards, workpaper
  conventions, findings structure, or alignment with public frameworks.
- **A docs improvement.** README, architecture, Vietnamese translation,
  or examples.
- **A tooling improvement.** Validation script, CI, or repository
  setup.

## Content rules

- One H1 per document. Sentence-case headings.
- Use American English in the English docs.
- Keep each reference file focused on one job. Do not turn it into a
  general essay.
- When you add, rename, or remove a file under `references/`, update
  the reference table in [SKILL.md](SKILL.md).
- Cite public frameworks and paraphrase them. Do not reproduce standard
  text or paywalled material.
- Separate fact, inference, and opinion. Quantify claims.
- Use generic, synthetic examples. Never use a real organization,
  system, account, or person.
- Do not use emojis as icons in documentation.
- Keep `README.md` and `README.vi.md` parallel. Keep reference
  translations as `references/X.vi.md` next to their English source.

## Adding a reference file

1. Create `references/<name>.md` with a single H1.
2. Add a row to the reference table in `SKILL.md` that says when to
   read it.
3. Add the file to the repository structure in both READMEs.
4. Run the validation script:

   ```bash
   python scripts/validate_skill.py
   ```

## Commits and pull requests

- Keep commits small and focused. Use an imperative subject, for
  example `add vendor-master typology to fraud patterns`.
- Fill in the pull request template, including the confidentiality
  checklist.
- Keep CI green. Markdown lint and skill validation must pass.
- Link the issue if one exists.

## Review

The maintainer checks accuracy, audit defensibility, and
confidentiality. Prose edits that weaken the evidence standard go back;
a new pattern with a synthetic example is welcome.

## License

By contributing, you agree that your contribution is licensed under the
MIT License in [LICENSE](LICENSE).
