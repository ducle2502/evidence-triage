# Audit Claim and Conclusion

How to move from evidence to a defensible claim, and from a claim to a
conclusion. Read this with `audit-findings.md`; that file covers finding
anatomy and severity, while this file covers claim types, causal depth,
disconfirming evidence, and confidence.

## Claim types and evidence fitness

Different claims need different evidence. State the claim type before
choosing the evidence.

| Claim type | The claim says... | Strongest evidence | Weak substitute |
| --- | --- | --- | --- |
| Existence | The item exists | Direct observation, system record | A list that says it exists |
| Occurrence | The event happened | Timestamped log, source document | A narrative summary |
| Completeness | All items are included | Reconciled population, control total | A sample with no population |
| Accuracy | The value is correct | Recalculation, independent confirmation | A copied figure |
| Valuation | The amount is measured properly | Model, inputs, and independent check | A management estimate |
| Rights and obligations | The entity controls or owes it | Contract, legal opinion, register | An assertion |
| Presentation | It is classified and disclosed correctly | Criteria and disclosure checklist | A draft |
| Compliance | A rule was followed | Rule text, effective date, test evidence | A policy summary |
| Effectiveness | The control works | Test of design and operation | A one-off observation |
| Efficiency | Resources are used well | Cost, time, output, and baseline | An opinion |
| Cause | Why it happened | Event chain, mechanism, counterfactual | A plausible story |
| Impact | What it changes | Transmission path, exposure, sensitivity | A generic risk statement |
| Forecast | What is likely | Base rate, trend, assumptions, sensitivity | Extrapolation from one period |

A claim can be true but unsupported, or supported by evidence that cannot
bear it. Both are defects.

## Fact, inference, and condition

Label every material statement:

- **Fact**: observed directly and traceable to a source location.
- **Inference**: a reasoned conclusion; state the reasoning, the
  alternatives considered, and what would change it.
- **Conditional scenario**: what could happen if an assumption holds;
  state the trigger, the mechanism, the delay, and the reversibility.

Write inferences and conditional scenarios so they cannot be mistaken
for facts or observed losses.

## Event chain

For a causal claim, reconstruct the chain:

1. Initial state.
2. The change or event that altered it.
3. The trigger.
4. The first manifestation.
5. Propagation to other processes, records, or entities.
6. The response already taken.
7. The result after the response.
8. The control that failed.
9. The remaining control gap.

If a material link is missing, label the conclusion incomplete. Do not
fill the gap with a plausible narrative.

## Why chain

Use a why chain only as far as the evidence supports. Each row should
have six fields:

| Field | Question |
| --- | --- |
| Question and answer | What did we ask, and what did we conclude? |
| Evidence | Which item supports the answer, at which location? |
| Mechanism | How does this cause produce the effect? |
| Alternative explanation | What else could explain it? |
| Status | Confirmed, supported, not supported, or insufficient evidence |
| Depth | Which why level does the evidence reach? |

Stop at the last level with direct evidence. A deeper story may be
interesting, but it is not a finding.

## Cause categories

Separate:

- **Direct cause**: the immediate condition that produced the effect.
- **Root cause**: the underlying mechanism that allows the direct cause
  to persist or recur.
- **Contributing cause**: a factor that increased likelihood or impact
  but is not sufficient on its own.
- **Coincidence or confounder**: a factor associated with the effect but
  not on the causal path.

Do not merge independent branches into one chain to make the story
cleaner. Do not call a surface fix a root-cause fix.

## Disconfirming evidence

For every material claim, ask:

1. What evidence would make this claim false or weaker?
2. Did we look for it?
3. If we found it, how did we address it?
4. If we did not find it, why not?

A claim with no falsification condition is written too strongly. Record
the disconfirming evidence and the reason it does or does not change the
conclusion.

## Confounders and base rates

Before concluding that A caused B, check:

- Did A occur before B?
- Is there a plausible mechanism linking A to B?
- Does the pattern repeat?
- Is there a third factor that explains both?
- If A were removed, would B still occur?
- What is the normal base rate of B?
- Is the change simply regression to the mean?

Order in time does not establish causation, and one unusual period does not establish a trend.

## Reasoning journal

Keep a short journal for each material conclusion:

- the initial hypothesis;
- the evidence for and against it;
- the assumptions that had to hold;
- the alternatives considered and why they were rejected;
- the decision and the reviewer.

This is not the report. It is the audit trail that lets a reviewer see how
the conclusion was reached, including the paths that were abandoned.

## Confidence and conclusion scale

State confidence separately from severity. A high-impact finding can have
medium confidence; a low-impact finding can be certain.

For each material conclusion, record:

- the conclusion;
- the confidence level and why;
- the evidence that carries the most weight;
- the evidence that could change it;
- the conditions under which it would be revised;
- the responsible reviewer.

Use the conclusion scale in the engagement profile. Examples include
satisfactory / needs improvement / unsatisfactory, or pass / conditional /
fail. These are examples, not a required scale.

## No intent attribution

Do not conclude intent, collusion, or bad faith from an error, a gap, or
an outlier. Describe the act, the control failure, and the effect. If
intent is material, label it as an allegation or a specialist question
and state the evidence needed.

## Escalation

Escalate when:

- the evidence is insufficient or conflicting;
- the claim depends on a legal, tax, actuarial, engineering, or other
  specialist judgment;
- the conclusion would name an individual or allege intent;
- the impact crosses a legal entity, jurisdiction, or regulatory
  boundary.

Label the item for specialist review and state the question the
specialist must answer.

## No individual blame without a system view

Before naming an individual, check:

- Was the person authorized and trained?
- Did the system or procedure permit the action?
- Was there a compensating control?
- Was the workload or deadline a factor?
- Is the same condition present elsewhere?

Most operational failures are system conditions, not individual
misconduct. Do not use an individual as a substitute for a control
analysis.

## Adaptation points

- Which claim types and conclusion labels does the methodology use?
- What confidence scale is approved?
- How deep must the event chain go for this engagement?
- Who reviews causal claims and intent allegations?
- What triggers a specialist review?
