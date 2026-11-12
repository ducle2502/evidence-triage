# Audit Findings

How analysis becomes a finding or a conclusion. Read this before you
write the final section of `investigation.md`, a triage summary, or
anything that will be quoted outside the session.

The structure below is general audit practice. Use your organization's
finding template and rating scale where they exist.

## The five parts of a finding

| Part | Question | Example |
| --- | --- | --- |
| **Condition** | What did you observe? | 38 vendor records share a bank account with an employee record. |
| **Criteria** | What should have happened? | Vendor master changes require independent approval and a uniqueness check. |
| **Cause** | Why did it happen? | The uniqueness check is manual and leaves no evidence. |
| **Effect** | What is the risk? | Payments could be diverted to an employee-controlled account without detection. |
| **Recommendation** | What should change? | Enforce an automated duplicate-account check and retain the result. |

A finding with a missing part is incomplete. Recommendations should
address the cause, not the symptom.

## Fact, inference, opinion

Label each statement for what it is:

- **Fact:** you observed it and can trace it to evidence.
- **Inference:** you reasoned from facts. State the reasoning and the
  alternatives you considered.
- **Opinion:** judgment or preference. Keep it out of the finding unless
  the methodology asks for it.

Wording that claims more certainty than the evidence supports
("clearly", "obviously", "proves") weakens the finding. Use numbers and
cite the artifact behind each one.

## Severity and priority

Severity depends on impact and likelihood, adjusted for materiality and
how widespread the issue is. It does not depend on how interesting the
pattern is.

Consider:

- Financial exposure, both actual and potential.
- Regulatory, customer, or reputational impact.
- The number of affected records or entities.
- Whether the issue is isolated or systemic.
- Whether a compensating control exists.
- Whether the condition is still live.

Do not invent thresholds. If the organization has a rating scale, use it
and cite it. If not, present impact and likelihood separately and
explain your judgment.

## Writing the finding

- Lead with the condition, not the story of how you found it.
- One finding per issue. Do not bundle unrelated conditions.
- Quantify counts, amounts, periods, and rates.
- Cite the evidence: file names, query IDs, or workpaper references.
- State limitations and alternative explanations.
- Use the organization's names for systems and controls.
- Make each recommendation specific, feasible, and owned.

## Report structure

A defensible investigation report usually has:

1. **Objective and scope:** what you tested and what you did not.
2. **Methodology:** population, sources, tests, and tools.
3. **Results:** findings in severity order, each with the five parts.
4. **Conclusion:** does the evidence support the objective?
5. **Recommendations:** cause-directed and assigned.
6. **Limitations:** missing data, untested paths, and open questions.
7. **Appendices:** queries, extracts, and evidence references.

`investigation.md` can be informal while the work is in progress. The
final section should read as if someone who was not there will review
it.

## Management response and follow-up

Writing a recommendation does not close a finding. Track:

- Management's response and the action it committed to.
- An owner and a due date.
- The evidence that will show remediation.
- A follow-up test, if the risk warrants one.

The skill stops at the recommendation and the evidence package. It does
not accept risk, close findings, or issue an opinion.

## Synthetic example

> **Illustrative only. The details are invented.**
>
> **Condition:** 12 vendor records created in Q3 share a bank account
> with another active vendor record. **Criteria:** the vendor master
> procedure requires a duplicate-account check before activation.
> **Cause:** the check is manual and leaves no evidence. **Effect:**
> payments could be split across records and escape duplicate-payment
> monitoring. **Recommendation:** enforce an automated duplicate-account
> check at activation and retain the result.

## Quality checklist

- [ ] Condition is factual and traceable to an artifact.
- [ ] Criteria are cited and apply to the period.
- [ ] Cause is distinguished from symptom.
- [ ] Effect is quantified or clearly reasoned.
- [ ] Recommendation addresses the cause and has an owner.
- [ ] Inferences are labeled and alternatives are stated.
- [ ] Limitations are explicit.
- [ ] No confidential or personal data appears in the text.
