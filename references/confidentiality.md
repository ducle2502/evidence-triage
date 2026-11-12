# Confidentiality

This repository is public. Anything committed here is visible to
anyone, including in the git history. Read this before you add an
example, an artifact, or organization-specific guidance.

## The rule

Do not commit employer, client, customer, or personal data. Do not
commit anything that could identify an organization, a person, a
system, or a live control environment without authorization.

## Do not commit

- Employer or client names, org charts, or internal project names.
- Internal system, application, table, column, or schema names.
- Real account, customer, employee, vendor, or transaction data.
- Real thresholds, tuning parameters, or population sizes.
- Screenshots of internal tools, dashboards, or reports.
- Incident details, investigation output, or audit findings.
- Internal terminology that is not public.
- Credentials, tokens, connection strings, or hostnames.

## You can commit

- Public frameworks and standards, cited and paraphrased.
- Generic typologies and control concepts.
- Synthetic examples, labeled as synthetic.
- Structural patterns that do not reveal a specific environment.
- Aggregate observations that cannot be traced to an organization.

## Keep organization-specific material outside

Put your team's named signals, schema, thresholds, and past cases in:

- a private repository with its own access controls,
- a local folder excluded by `.gitignore` (for example `local/`), or
- a reference pack distributed through an approved channel.

The skill works with this material wherever it lives. It does not need
to be in this repo.

Do not commit an overlay "temporarily" and remove it later. Git keeps
the history.

## Redact carefully

When an example has to resemble real data:

- Replace identifiers with stable pseudonyms or hashes.
- Shift dates by a constant offset.
- Scale amounts by a constant factor.
- Replace free-text fields with categories.
- Reduce granularity, for example region instead of branch.
- Check again that the remaining fields cannot re-identify anyone.

Deleting fields does not always remove the risk. A combination of
quasi-identifiers can reconstruct the original.

## Before you commit

- [ ] No organization, system, table, or schema names.
- [ ] No real people, accounts, vendors, or transactions.
- [ ] No live thresholds or population sizes.
- [ ] Synthetic examples are labeled.
- [ ] No credentials, tokens, or internal URLs.
- [ ] You reviewed `git diff` line by line, including the changed
      content.
- [ ] If you are unsure, leave it out.

## If confidential data is committed

1. Stop pushing. Treat it as a security incident.
2. Notify the organization's security or compliance contact through the
   approved channel.
3. Remove the data from the working tree, the commit, and the remote
   history as directed.
4. Rotate any exposed credentials immediately.
5. Follow the organization's incident and reporting requirements.

Deleting a file in a later commit does not remove it from history.
Assume anything pushed to a public remote is already disclosed.

## Review

Review this file when the repository's visibility changes or when a new
contributor joins. Whether this repository is public depends on where it
is hosted, not on what this file says.
