# Contributing

Thanks for helping with evidence-triage. This is a public skill package
for internal audit and fraud work.

## This repo is public

Anything committed here is visible to anyone, including in the git
history. Read this section before you add an example, an artifact, or
organization-specific guidance.

### The rule

Do not commit employer, client, customer, or personal data. Do not
commit anything that could identify an organization, a person, a
system, or a live control environment without authorization.

### Do not commit

- Employer or client names, org charts, or internal project names.
- Internal system, application, table, column, or schema names.
- Real account, customer, employee, vendor, or transaction data.
- Real thresholds, tuning parameters, or population sizes.
- Screenshots of internal tools, dashboards, or reports.
- Incident details, investigation output, or audit findings.
- Internal terminology that is not public.
- Credentials, tokens, connection strings, or hostnames.

### You can commit

- Public frameworks and standards, cited and paraphrased.
- Generic typologies and control concepts.
- Synthetic examples, labeled as synthetic.
- Structural patterns that do not reveal a specific environment.
- Aggregate observations that cannot be traced to an organization.

### Keep organization-specific material outside

Put your team's signals, schema, thresholds, and past cases in:

- a private repository with its own access controls,
- a local folder excluded by `.gitignore` (for example `local/`), or
- a reference pack distributed through an approved channel.

The skill works with this material wherever it lives. It does not need
to be in this repo.

Do not commit an overlay "temporarily" and remove it later. Git keeps
the history.

### Redact carefully

When an example has to resemble real data:

- Replace identifiers with stable pseudonyms or hashes.
- Shift dates by a constant offset.
- Scale amounts by a constant factor.
- Replace free-text fields with categories.
- Reduce granularity, for example region instead of branch.
- Check again that the remaining fields cannot re-identify anyone.

Deleting fields does not always remove the risk. A combination of
quasi-identifiers can reconstruct the original.

### Before you commit

- [ ] No organization, system, table, or schema names.
- [ ] No real people, accounts, vendors, or transactions.
- [ ] No live thresholds or population sizes.
- [ ] Synthetic examples are labeled.
- [ ] No credentials, tokens, or internal URLs.
- [ ] You reviewed `git diff` line by line, including the changed
      content.
- [ ] If you are unsure, leave it out.

If confidential data is committed, follow the exposure process in
[SECURITY.md](SECURITY.md). Deleting a file in a later commit does not
remove it from history.

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
