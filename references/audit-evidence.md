# Audit Evidence

How triage work becomes audit evidence. Read this before you document
evidence in any phase, and before you hand artifacts to someone who was
not in the session.

The concepts here are general internal audit practice. They do not
replace your organization's methodology or the applicable standards,
such as the IIA Global Internal Audit Standards and COSO.

## What makes evidence usable

Audit evidence has to be sufficient, relevant, and reliable.

- **Sufficient:** there is enough of it to support the conclusion,
  given the risk and the quality of the evidence.
- **Relevant:** it bears on the objective, the population, and the
  period you are testing.
- **Reliable:** the source and the collection method make it
  trustworthy.

All three matter. A large extract of unreliable data is not sufficient
evidence. A reliable extract that covers the wrong period does not
answer the question.

## Which evidence is stronger

Use the strongest evidence you can get. Say so when you had to settle
for something weaker.

| Evidence type | Reliability | Notes |
| --- | --- | --- |
| System-generated extract with a logged query, reconciled to source | Higher | Reproducible and independent of the person who ran it |
| System report with visible parameters and row counts | Higher | Save the parameters as well as the output |
| Screenshot or exported spreadsheet with no query | Lower | Hard to reproduce and easy to alter |
| Manual summary or verbal explanation | Lowest | Useful as a lead; corroborate before relying on it |

Independent evidence usually outweighs evidence from the area under
review. Original documents usually outweigh copies. Two independent
sources that agree are stronger than one source repeated.

## Define the population

Before you test, write down:

- **Scope:** which entities, transactions, or records are included.
- **Period:** the exact start and end, including the timezone.
- **Filters:** every exclusion and the reason for it.
- **Source:** the system, table, or report the population came from.
- **Row count:** before and after filters.

The population sets the limit on what the test can show. If it leaves
out late-posted records, archived data, or manual overrides, say so.

## Check the data before you interpret it

1. **Reconcile counts.** Compare the population with the source report
   or a control total.
2. **Check the date boundary.** Confirm inclusive and exclusive
   endpoints, the timezone, and whether records arrived late.
3. **Check duplicates.** Look for duplicate keys, replayed
   transactions, and multiple records per entity.
4. **Check nulls and defaults.** Missing attributes, placeholder
   values, and default timestamps can change the result.
5. **Check joins.** Many-to-one and one-to-many joins can multiply or
   drop rows. Compare counts before and after.
6. **Check the query.** Save the parameters, filters, and logic
   exactly as they ran.
7. **Sanity-check the magnitudes.** Compare totals, averages, and
   distributions with a known baseline.

Write down each check and its result, including the clean ones. A
record of what you checked is part of the evidence.

## Workpapers for query-based evidence

Every test should leave a pair of files and a short note:

- The query as it ran (`.sql`, notebook, or script), with parameters
  and environment noted.
- The result (`.csv` or equivalent), with the row count and extraction
  timestamp.
- A note covering the objective, population, source, filters,
  interpretation, limitations, and conclusion.
- A cross-reference from the note to the query and result files.

Use the folder layout in `output-conventions.md`. If a result cannot be
re-run or traced back to its query, it is not evidence you can defend.

## Chain of custody

- Extract read-only. Do not edit source data.
- Hash large extracts before you share or retain them.
- Keep artifacts in an access-controlled location. This public repo is
  not one.
- Record who extracted the data, when, and from where.
- Follow the organization's retention policy.

## Limits and professional skepticism

State the limits of the work:

- Data that is missing or incomplete.
- A proxy used instead of the real attribute.
- A test you could not perform.
- Alternative explanations you did not rule out.
- The precision limits of thresholds and matching rules.

A negative result means the test did not find the condition. It does
not prove the condition was absent.

## Documentation template

```markdown
## Test <id>: <short name>

- Objective:
- Population:
- Period:
- Source:
- Filters / exclusions:
- Query file:
- Result file:
- Row count (before / after):
- Data-integrity checks:
- Result summary:
- Interpretation:
- Limitations:
- Conclusion:
- Reviewer:
```

Keep the template short enough that people use it. A complete, plain
record is better than an elaborate one that never gets filled in.

## From evidence to findings

Evidence supports a finding. Before you write the conclusion, read
`audit-findings.md` and separate what you observed from what you
inferred.
