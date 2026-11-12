# Audit Evidence Model

How evidence is identified, versioned, sourced, and kept usable over the
life of an engagement. Read this after `audit-engagement-profile.md` and
alongside `audit-evidence.md`.

`audit-evidence.md` covers sufficiency, relevance, reliability,
population, data-integrity checks, and chain of custody. This file covers
the layer above that: identity, lifecycle, currency, source tier, and the
difference between what was requested and what was received.

## Evidence categories

Evidence comes in several forms. Common categories:

- Documents: policies, procedures, approvals, minutes, contracts.
- System extracts: queries, reports, logs, configuration, access lists.
- Interviews and walkthroughs: what people say happened.
- Observations: what the auditor saw happen.
- Confirmations: third-party or independent responses.
- Legal or specialist opinions.
- Physical evidence.
- External reports: regulator, auditor, consultant, certification body.

Each category proves different things. A walkthrough is strong evidence
of how a process is described; it is weak evidence of how often the
process runs that way.

## Identity

Use an identity tuple, not a filename:

```text
content hash + source system + entity + period + version
```

Consequences:

- The same filename from two sources may be two different artifacts.
- The same content hash from two locations may be the same artifact.
- A renamed file is not a new artifact.
- A new version with the same filename is a new evidence item.
- A local copy is not authoritative merely because it is easier to open.

Assign a stable evidence ID. Keep a mapping from local IDs to the master
register when more than one report or team uses its own numbering.

## Metadata

At minimum, record:

| Category | Examples of fields |
| --- | --- |
| Identity | Evidence ID, title, description, version |
| Source | Source system, owner, path or location, collection method |
| Entity | Legal entity, business unit, region, counterparty |
| Period | Event date, publication date, collection date, snapshot date, effective date |
| Integrity | Hash, file size, format, page or row count |
| Status | Current, superseded, issued, reference, draft, uncorroborated, gap |
| Traceability | Exact citation location, related workpaper, related finding |
| Accountability | Collector, collection date, reviewer |
| Limitation | What the item cannot prove, known gaps, access restrictions |

Organizations add fields. Do not force a fixed column count.

## Status vocabulary

Use a controlled vocabulary. A workable default:

- **Current**: the authoritative version in use.
- **Superseded**: replaced by a later version; retained for history.
- **Issued**: formally signed or published by the authorized body.
- **Reference**: useful context, not sufficient alone for a material
  conclusion.
- **Draft**: not approved; do not treat as final.
- **Uncorroborated**: single-source or unverified; label it.
- **Gap**: missing, inaccessible, or insufficient; record the assurance
  impact.

The labels are defaults. Map them to the organization's methodology.

## Append-only lifecycle

Evidence changes by addition, not replacement:

1. A new version gets a new evidence ID.
2. The prior version is marked superseded, not deleted.
3. The physical or digital prior version is retained in the evidence
   store.
4. The register records the supersession chain.
5. The report cites the version used.

Do not overwrite a file, mirror-sync a folder over an evidence store, or
"clean up" old versions. History is part of the evidence.

## Source versus working copy

The authoritative source and the working copy can diverge. Reconcile:

1. Compare the content hash.
2. If they match, record the check.
3. If they differ, inspect the source's version history.
4. If the source is newer, register a new version.
5. If the working copy is older, record a stale-copy limitation; do not
   present it as current.
6. If the source is inaccessible, record the access limitation and the
   provenance of the copy.

A working copy is a convenience; the source remains the authority.

## Currency clocks

Do not use a single "date" field. Track:

- **Event date**: when the event happened.
- **Publication date**: when the document was issued.
- **Collection date**: when the auditor obtained it.
- **Snapshot date**: the state of the data at extraction.
- **Effective date**: when a rule, approval, or version takes effect.

A trend snapshot can be stale for cut-off purposes but still valid for
direction. A document can be current but describe an old event. State
which clock the conclusion depends on.

Also track **source liveness**. A feed or repository that has stopped
updating may mean the process paused, was abandoned, or moved outside
the visible system.

## Source tier and independence

Use the strongest available evidence and state when you settled for
weaker evidence. A useful default:

| Tier | Examples | Strongest for |
| --- | --- | --- |
| System or machine evidence | Logged query, extract, configuration, access log | Counts, states, timestamps, completeness checks |
| Signed or issued primary document | Approval, contract, policy, formal notice | Authority, obligation, formal position |
| Independent corroboration | External auditor, regulator, independent monitor, confirmation | Conflicting accounts, independence |
| Self-reported or narrative | Management update, meeting note, draft summary | Leads and context, not proof of progress |
| Unsourced assertion | Verbal claim with no record | Nothing on its own |

A document written by the area being reviewed proves what that area
asserts. It does not prove the assertion is true. A meeting note proves a
discussion was recorded; it does not prove an action was completed.

## Demand versus supply

Keep two linked ledgers:

1. **Evidence request ledger**: what the engagement needs, from whom, by
   when, and its status: not requested, requested, received, partial,
   insufficient, out of scope.
2. **Evidence register**: what has been received, its identity, source,
   version, status, citation, and limitation.

Link them by evidence ID. Do not duplicate fields. Partial means the
item was accepted with a stated limitation; missing means it was not
received.

## Evidence-screening gate

Before drafting or rewriting a report:

1. List every material number, name, date, and conclusion in the draft.
2. Map each one to a root source and a precise location.
3. Open the source and verify the value.
4. Record the result: confirmed, corrected, downgraded, or known gap.
5. Do not proceed to drafting while a material number is unmapped.

This gate prevents a report from carrying a number that no one can
defend.

## Relationship to `audit-evidence.md`

Use `audit-evidence.md` for:

- sufficiency, relevance, and reliability;
- population definition and completeness;
- data-integrity checks;
- query-and-result workpapers;
- chain of custody;
- limitations and professional skepticism.

Use this file for:

- identity and metadata;
- lifecycle and supersession;
- source-versus-copy reconciliation;
- currency and source liveness;
- source tier and independence;
- demand-versus-supply tracking;
- the pre-draft screening gate.

## Adaptation points

- Which evidence categories and status labels does the methodology use?
- Which identity fields are mandatory?
- Which source is authoritative for each evidence type?
- Which clocks matter for the conclusion?
- How are requests, receipts, and gaps tracked?
- Who performs the evidence-screening gate, and when?
