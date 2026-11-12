# Vision

## Origin

This repo started from
[finic-ai/fraud-investigation-skills](https://github.com/finic-ai/fraud-investigation-skills)
under the MIT License. The three-phase method and the fraud typologies
come from that project. This version reframes the skill for internal
audit and adds material on evidence, findings, and confidentiality.

## Principles

1. **Sort the work before writing queries.** Hunting, triage, and
   investigation answer different questions and produce different
   output.
2. **Build conclusions on evidence.** A conclusion depends on the
   population, the query, and the record behind it.
3. **Keep the public repo generic.** Organization-specific knowledge
   belongs in a private overlay.
4. **Make the work reproducible.** Every result should trace back to a
   query, a source, a period, and a reviewer.
5. **Leave the judgment to the auditor.** The skill assembles the
   analysis; the auditor rates and signs it.

## Current state

Version 3.0.0 includes:

- The three-phase method, reframed for audit.
- Audit evidence and findings references.
- A confidentiality reference and a private-overlay pattern.
- A standard layout for queries, extracts, and the running
  investigation document.
- Repository docs, issue forms, labels, and validation CI.

## Direction

- Add audit typologies: segregation of duties, journal-entry anomalies,
  vendor-master changes, access-path exceptions, and period-end
  patterns.
- Strengthen the evidence layer with sampling caveats, reconciliation
  patterns, and review trails.
- Improve the Vietnamese docs without duplicating the English source of
  truth.
- Keep the validation script and CI cheap enough to run on every pull
  request.

## What this project will not do

- Ship organization-specific content, real data, or tuned thresholds.
- Replace audit standards, methodology, or professional judgment.
- Take remediation action or issue an audit opinion.
- Add automation that acts on findings without human review.

## Contribution rules

A change should make the skill more defensible, more reproducible, or
easier to use in audit work. Changes that add breadth without evidence
discipline will be declined. See [CONTRIBUTING.md](CONTRIBUTING.md).
