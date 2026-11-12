# Audit Public Safety

Rules for turning real audit experience into public examples without
disclosing confidential information. This file applies the repository's
contribution rules to audit reporting material; the full checklist is in
[CONTRIBUTING.md](../CONTRIBUTING.md).

The repository is public, and its git history with it.

## The rule

Do not publish anything that could identify:

- an employer, client, or counterparty;
- a person, account, vendor, or transaction;
- a live system, application, module, table, or schema;
- a programme, project, incident, or investigation;
- a threshold, population size, or control configuration that describes
  a live environment;
- a legal or regulatory position that could be attributed to a specific
  matter.

If a lesson cannot be told without one of these, abstract it further or
leave it out.

## Prohibited content

- Organization, parent, subsidiary, or client names.
- Project, programme, system, vendor, or product names.
- Internal codes, ticket prefixes, evidence prefixes, or file naming
  conventions that mirror a live environment.
- Real dates, amounts, counts, percentages, thresholds, or population
  sizes.
- Incident signatures: a unique combination of time, system, error, and
  impact that could identify the event.
- Personal names, roles that identify one person, email addresses, phone
  numbers, or account identifiers.
- Internal URLs, repository paths, drive letters, folder names, or
  document IDs.
- Screenshots, logos, org charts, report covers, or extracted tables.
- Legal citations, regulatory instrument numbers, or jurisdiction-specific
  procedures that point to a specific matter.
- Credentials, tokens, connection strings, or hostnames.

## Allowed content

- Public frameworks and standards, paraphrased and cited.
- Generic control concepts and audit techniques.
- Synthetic examples, clearly labeled as synthetic.
- Structural patterns that do not reveal a specific environment.
- Aggregate observations that cannot be traced back to one organization.
- Fictional composites that combine features from several contexts.

## Abstraction patterns

When an example is needed:

1. **Change the domain.** Move the example to a different industry,
   process, or control type.
2. **Change the entity.** Use a generic organization, not a real one.
3. **Change the scale.** Do not preserve the real count, amount, or
   percentage.
4. **Change the time.** Do not preserve the real date, duration, or
   sequence if it is identifying.
5. **Change the system.** Describe the control, not the product.
6. **Change the roles.** Use generic roles, not real titles that map to
   one person.
7. **Combine features.** Build a composite that no single real
   engagement matches.
8. **Remove the unique combination.** A set of individually harmless
   details can re-identify the source.

## Metadata scrubbing

Before publishing a file:

- remove author and last-modified metadata;
- remove comments and tracked changes;
- remove document properties and custom fields;
- remove embedded images and attachments;
- remove hidden sheets, hidden rows, and hidden columns;
- check that the visible content does not contain a leftover path or
  identifier;
- check the file name and folder name as well as the content.

A clean body with a revealing filename is still a disclosure.

## Banned-token sweep

Build a local, private list of tokens that must never appear in the
public repo. Include:

- organization and parent names;
- project, programme, and system names;
- vendor and product names;
- internal code prefixes;
- the private report titles;
- the source folder names;
- the specific incident numbers, dates, and amounts;
- the names of the individuals involved.

Run the sweep before every commit. Do not commit the banned-token list
itself.

## Manual read

Automated scans miss context. Read every file as if you were the
organization's legal or compliance reviewer. Ask:

- Could a reader identify the organization from the combination of
  details?
- Could a reader identify a person or a live system?
- Could a reader infer a confidential incident?
- Is the example necessary, or is it decoration?
- Would a generic example teach the same lesson?

If the answer to the last question is yes, use the generic example.

## Second-reviewer sign-off

Before pushing:

1. A second reviewer reads the public diff, including the changed content.
2. The reviewer checks the banned-token sweep and the manual-read
   questions.
3. The reviewer records the sign-off in the private workpaper, not in
   the public content.
4. If the reviewer is unsure, the content is removed or abstracted.

## Public statement

Use a short, accurate statement:

> These are generalized lessons from internal audit report production.
> Examples are fictionalized and do not describe a specific organization,
> person, system, or engagement.

Do not claim a specific client, jurisdiction, or incident. Do not imply
that the examples are real.

## Git history

If confidential content has already been committed:

1. Stop pushing.
2. Treat it as a security incident.
3. Notify the organization's security or compliance contact through the
   approved channel.
4. Remove the content from the working tree, the commit, and the remote
   history as directed.
5. Rotate any exposed credentials.
6. Follow the organization's incident and reporting requirements.

Removing a file in a later commit does not remove it from history.
Assume anything pushed to a public remote is already disclosed.

## Pre-publication checklist

- [ ] No organization, project, system, vendor, or product names.
- [ ] No real people, accounts, vendors, or transactions.
- [ ] No real dates, amounts, counts, percentages, or thresholds.
- [ ] No incident signatures or unique combinations.
- [ ] No internal paths, URLs, emails, or credentials.
- [ ] No screenshots, logos, or extracted tables.
- [ ] Examples are labeled synthetic.
- [ ] Metadata, comments, and tracked changes are removed.
- [ ] Banned-token sweep passes.
- [ ] Manual read passes.
- [ ] Second reviewer signs off.
- [ ] The public statement is accurate.
- [ ] Git history is clean, or an incident process is underway.

## Adaptation points

- Which additional tokens are sensitive for this organization?
- Who is the second reviewer?
- Which approval channel applies before a public push?
- Which retention and incident policies apply?
