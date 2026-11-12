# Audit Report Architecture

How to shape a report so the reader can decide, the reviewer can trace,
and the auditee can act. Read this with `audit-findings.md`; that file
covers finding anatomy, while this file covers the architecture around
the findings.

Do not treat the structures below as mandatory. Select the pattern that
fits the report type, audience, and decision in the engagement profile.

## Reader-first ordering

Write in the order the reader needs, not the order the work was done:

1. What is the conclusion?
2. What decision or action does it require?
3. What are the few issues that change the decision?
4. What is the basis, including limitations?
5. Where can the reader verify the detail?

If the reader has to reconstruct the conclusion from the appendix, the
report is ordered wrong.

## Report layers

A useful default is three layers:

- **Decision layer**: conclusion, decision, key issues, conditions,
  what to do next.
- **Explanation layer**: criteria, condition, cause, effect,
  recommendation, evidence summary.
- **Verification layer**: source map, detailed tests, extracts,
  methodology, limitations.

The layers can be separate sections, a main report plus appendices, or a
dashboard plus drill-down. They do not have to be three physical parts.

## Report-type patterns

| Pattern | Use when | Core shape |
| --- | --- | --- |
| Decision memo | A senior reader needs a decision | Conclusion, decision options, key issues, conditions, basis |
| Full report | The reader needs reasoning and traceability | Objective, scope, method, results, conclusion, recommendations, appendices |
| Dashboard | The reader monitors status or exceptions | Indicators, thresholds, exceptions, trend, drill-down |
| Briefing note | The message must land in a short meeting | One message, three supports, one ask |
| Investigation report | Allegation or incident | Chronology, evidence, findings, conclusion, actions |
| Follow-up report | Prior actions need closure | Action, owner, due date, evidence of closure, residual risk |
| Regulatory filing | A prescribed form applies | Use the prescribed form; do not redesign it |

## The skim path

Design a path a busy reader can follow in a short time:

- a small set of key indicators;
- a conclusion box;
- one exhibit that carries the main message;
- the first row of the comparison or findings table;
- the decision or action requested.

If the skim path misleads when read alone, move the qualifying detail
into it instead of leaving it in an appendix.

## Finding pattern

A finding should answer:

- **Criteria**: what should be, and why it applies.
- **Condition**: what is, factually.
- **Cause**: why it happened, at the depth the evidence supports.
- **Effect**: so what, including the transmission path.
- **Recommendation**: what should change, addressed to an owner.

Add metadata the reader needs: risk rating, confidence, status, evidence
references, and the closure condition. The familiar five-part structure
is one pattern; use the organization's pattern if it differs.

## Recommendations and closure

A recommendation needs:

- a single accountable owner;
- a due date or trigger;
- a measurable completion criterion;
- the evidence that will demonstrate completion;
- an independent confirmer;
- a stop or escalation control if the action fails.

Separate the recommendation from the management response. A response is
not closure. Closure requires evidence that the condition is remediated
and the risk is reduced.

## Standalone report

The report must stand alone. A reader with only the report should be able
to understand:

- the objective and scope;
- the conclusion and its basis;
- the limitations;
- the actions required;
- where each material number comes from.

Do not require the reader to know the internal folder structure, the
engagement code, or the author's naming conventions.

## Appendices and source map

Appendices should carry verification, not hide the conclusion. A useful
source map has:

| Report statement | Evidence ID | Source | Issuer | Period | Location | Status |
| --- | --- | --- | --- | --- | --- | --- |

The reader should be able to move from a statement to a source without
asking the auditor for a file.

Page breaks are a layout choice. A short appendix may leave trailing
whitespace; that is not an overflow defect. Check that headings, tables,
and figures remain intact across the break.

## Technical to operational translation

Translate technical failures into consequences the reader can act on:

- money: loss, leakage, reconciliation effort, capital;
- customers: access, service, complaints, harm;
- operations: delay, rework, manual workaround, capacity;
- legal and regulatory: breach, reporting, remediation;
- reputation: trust, publicity, stakeholder confidence.

Keep the technical detail in the explanation or verification layer. Do
not make the decision layer depend on a term the reader does not know.

## Activity is not completion

Do not report a document, a meeting, a training session, or a task as a
completed outcome. Distinguish:

- **Activity**: something was done.
- **Output**: something was produced.
- **Outcome**: the condition changed.
- **Assurance**: the change was independently verified.

A report that counts activities as closure hides the remaining risk.

## Positive percentages and mandatory conditions

Do not use a high completion percentage to hide an unmet mandatory
condition. Report both:

- the percentage of items complete;
- whether the mandatory gates or conditions are met.

A programme can be 90% complete and still unable to proceed because the
remaining 10% includes a mandatory control.

## Decision support

Give the reader the decision options as well as the findings:

- approve;
- approve with conditions;
- reject;
- request more evidence;
- escalate to a higher authority;
- pause or stop.

State which option the evidence supports, and what would change the
recommendation.

## Cross-document consistency

Keep the same numbers, names, dates, and conclusions across:

- the report;
- the executive summary;
- the dashboard;
- the appendices;
- the cover note;
- the data pack.

Vary only the level of detail. A number that changes between documents
destroys trust faster than a missing number.

## Adaptation points

- Which report pattern and layers does the engagement use?
- What belongs in the decision layer for this audience?
- Which finding pattern and rating scale are approved?
- What closure evidence does the organization accept?
- Which documents must be consistent with the report?
