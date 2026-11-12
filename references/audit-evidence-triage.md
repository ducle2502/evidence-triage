# Audit Evidence Triage

How to decide what each evidence item can support, what still needs
corroboration, and what is missing. Each item is tested against the
claim it must support, not ranked by how suspicious the file looks.

Use this after `audit-evidence-model.md`. Use `audit-evidence.md` for the
underlying tests of sufficiency, relevance, and reliability.

## The two questions

Ask two separate questions:

1. **Evidence QC**: is this item usable on its own terms?
2. **Claim QC**: can this evidence set bear the specific claim?

An authentic document can fail claim QC because it covers the wrong
period. A conclusion can be right and still be unsupported, if the
evidence covers only part of the claim. Do not collapse the two into
one confidence score.

| Evidence QC | Claim QC |
| --- | --- |
| Is it relevant to the objective? | Does the evidence set cover every part of the claim? |
| Is it current at the claim's cut-off? | Is the evidence type capable of proving this claim? |
| Is the source reliable and independent enough? | Do the sample and population support the generalization? |
| Can the extraction or observation be reproduced? | Is each element supported by a cited item? |
| Is the scope of the item clear? | Is there disconfirming evidence, and was it addressed? |

## Triage rubric

Score each material item or claim on these dimensions. Use a scale the
engagement profile defines; the questions matter more than the labels.

| Dimension | Question | Typical failure |
| --- | --- | --- |
| Relevance | Does it bear on the objective, population, and period? | A good document about the wrong entity |
| Reliability | Is the source and method trustworthy? | A screenshot with no query or parameters |
| Currency | Is it current for the cut-off? | A trend snapshot used as a current status |
| Verifiability | Can someone else reproduce or inspect it? | A summary with no source location |
| Coverage | Does it cover the whole claim, including every part? | One exception treated as the population |
| Corroboration | Is there independent support or a material conflict? | Repetition of the same source |
| Materiality | Would a different value change the decision? | Precision spent on an immaterial item |
| Actionability | What should happen next? | A gap with no owner or request |

## Decision states

Use a controlled set of outcomes. A workable default:

- **Accept**: usable for the claim as stated.
- **Accept with limitation**: usable, but the limitation must travel
  with the claim.
- **Request update**: the item is stale or incomplete; ask for the
  current version.
- **Seek corroboration**: single-source, self-reported, or conflicting;
  find an independent item.
- **Gap**: missing or inaccessible; record the assurance impact.
- **Out of scope**: not relevant to this objective; preserve it for a
  separate review if material.
- **Reject**: unreliable or not representative; do not cite it as
  support.

Do not use "accept" for an item that only supports part of a claim.
Split the claim or mark the limitation.

## Dual-code classifications

For any label that changes a decision (type, status, severity,
completion, compliance), record two values:

- the planned, claimed, or intended label;
- the observed, actual, or implemented label.

Record divergence as a finding. Do not collapse the two into one
"final" label without recording the difference.

## Coverage map

Maintain a map from the question, criterion, or assertion to the
evidence and its status.

Record one row per claim: the criterion, the evidence IDs and status,
any gap, and the owner and due date.

The map shows whether the conclusion is covered. If one component has
strong evidence and another has none, the conclusion is only partly
supported.

## Gaps and blocked metrics

Record a gap as a finding:

- what is missing;
- why it is missing (not requested, not provided, inaccessible, not
  measurable, destroyed, outside the period);
- what assurance it affects;
- what would close it;
- who owns the request;
- when it will be re-checked.

If a metric cannot be measured, do not write zero. Write "not measured"
and state the reason. A fabricated zero is worse than an admitted gap
because it looks like evidence.

## Derived metrics and aggregates

Every aggregate needs a provenance chain:

```text
raw field -> transformation -> grouping -> aggregate -> report statement
```

Flag any grouping that is derived, mapped, imputed, or based on a blank
or default field. Re-verify the aggregate against the raw records before
using it in a finding. A chart or dashboard that hides the derivation is
not evidence of the underlying population.

## Conflict protocol

When two sources disagree, do not pick the one that is easier to use.
Compare:

1. **Definition**: are they measuring the same thing?
2. **Scope**: same entities, locations, and exclusions?
3. **Cut-off**: same period and snapshot date?
4. **Denominator**: same population and unit?
5. **Approver**: same authority and sign-off status?
6. **Status**: current, draft, superseded, or unverified?

Record the comparison and the decision. If the conflict cannot be
resolved, label the claim disputed and state what would resolve it.

## Impact deduplication

Before ranking findings by impact:

- define the pools or exposure categories;
- state which findings draw on the same pool;
- apply an explicit anti-double-count rule;
- reconcile the total to the pool;
- keep severity and confidence separate.

Summing overlapping findings inflates the total without adding risk.

## Stop rule

Stop triage when new evidence no longer changes the decision. More
documents can always be found. The test is whether a new item would
change a conclusion, a rating, a recommendation, or a closure condition.
If it would not, record it as background and move on.

## Triage record

Keep the decisions inspectable:

```markdown
## Triage decision <id>

- Item / claim:
- Evidence IDs:
- Evidence QC result:
- Claim QC result:
- Decision state:
- Limitation or gap:
- Next action / owner / due:
- Reviewer:
```

## Adaptation points

- Which rubric dimensions and decision states does the methodology use?
- Who owns the coverage map, and how often is it refreshed?
- Which aggregates are material enough to require independent
  re-performance?
- How are conflicts escalated?
- What is the stop rule for this engagement?
