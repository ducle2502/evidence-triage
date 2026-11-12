# Audit Templates

Copy these templates into the engagement workpaper and fill them in.
They contain no real data. Replace every placeholder with the
engagement's own terms, or delete the field if it does not apply.

## Engagement profile

```markdown
# Engagement profile

- Engagement name:
- Purpose:
- Decisions to support:
- Audience and reading order:
- Scope in:
- Scope out:
- Criteria categories and sources:
- Period and cut-off:
- Subject and population:
- Evidence sources and access:
- Report type:
- Language and style contract:
- Materiality:
- Severity scale:
- Conclusion scale:
- Approval authority:
- Gate model:
- Release artefacts:
- Confidentiality and distribution:
- Known constraints:
```

## Evidence register

Use the organization's columns if they exist. These are categories, not a
fixed schema.

```csv
evidence_id,title,description,evidence_type,source_system,entity,period,version,hash,location,collector,collection_date,status,citation_location,limitation,related_workpaper
```

## Evidence request ledger

```csv
request_id,question_or_criterion,evidence_needed,owner,due_date,status,received_date,evidence_id,limitation,next_action
```

Status values: not requested, requested, received, partial, insufficient,
out of scope.

## Coverage map

```csv
question_or_criterion,assertion,evidence_ids,coverage_status,gap_or_limitation,owner,due_date
```

Coverage status values: covered, partially covered, gap, out of scope.

## Triage decision record

```markdown
## Triage decision <id>

- Item or claim:
- Evidence IDs:
- Evidence QC result:
- Claim QC result:
- Decision state:
- Limitation or gap:
- Next action / owner / due:
- Reviewer:
```

## Claim-evidence matrix

```csv
claim_id,claim_text,claim_type,evidence_ids,evidence_type,coverage,corroboration,confidence,disconfirming_evidence,status
```

## Finding record

```markdown
## Finding <id>: <short title>

- Criteria:
- Condition:
- Cause:
- Effect / risk:
- Recommendation:
- Owner:
- Due date:
- Closure criteria:
- Closure evidence:
- Independent confirmer:
- Risk rating:
- Confidence:
- Status:
- Evidence IDs:
- Limitations:
```

## Impact chain

| Field | Content |
| --- | --- |
| Event | What happened |
| Direct impact | The first-order effect |
| Mechanism | How the effect propagates |
| Affected parties | Who or what is affected |
| Delay | When the effect appears |
| Reversibility | Can it be undone, and at what cost |
| Compensating control | What reduces the effect |
| Final consequence | The decision-relevant outcome |

## Review scorecard

```markdown
# Review scorecard

| Lens | Scope | Result | Evidence | Exception | Action | Reviewer |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Result values: pass, fail, conditional.

## Open exceptions

| ID | Exception | Severity | Owner | Due | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Sign-off

- Reviewer:
- Date:
- Residual disagreement:
```

## Release manifest

```csv
artefact,version,format,size,hash,source,status,owner,approval_date
```

## Cover note

```markdown
# Cover note

- Report title:
- Version:
- Decision or action requested:
- Key conclusion:
- Conditions or limitations:
- Attached artefacts:
- Approval status:
- Distribution:
- Known gaps:
```

## Report outline selector

Use one pattern, not all of them.

```markdown
# Report outline

- Pattern: decision memo / full report / dashboard / briefing / investigation / follow-up / regulatory
- Decision layer:
  - Conclusion:
  - Decision options:
  - Key issues:
  - Conditions:
- Explanation layer:
  - Criteria:
  - Condition:
  - Cause:
  - Effect:
  - Recommendation:
- Verification layer:
  - Source map:
  - Method:
  - Limitations:
  - Appendices:
```

## Adaptation points

- Which templates are mandatory in the methodology?
- Which fields are organization-specific?
- Which IDs and status vocabularies apply?
- Who reviews and approves the completed template?
