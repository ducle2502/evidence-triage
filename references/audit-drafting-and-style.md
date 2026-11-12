# Audit Drafting and Style

How to write the report so it is accurate, readable, and hard to
misquote. Style carries evidential weight: a sentence that overstates
certainty, hides a denominator, or drops a subject produces a finding
that cannot be defended.

This file gives a default style contract. Replace the defaults with the
engagement profile's language and house style.

## Style contract

Before drafting, agree on:

| Element | Decision |
| --- | --- |
| Language and variant | Which language, which regional standard |
| Sentence limit | A maximum length, or a readability target |
| Voice and tense | Active or passive; past, present, or conditional |
| Person | First person, third person, or impersonal |
| Terminology | Approved terms and forbidden synonyms |
| Entity naming | Full name at first use, short name thereafter |
| Date format | One format, one timezone |
| Number and unit format | Separators, decimals, currency, units |
| Ratio format | Always numerator / denominator and period |
| Citation style | Inline and reference-list convention |
| Technical detail | What stays in the body and what moves to an appendix |
| Tone | Neutral, factual, non-accusatory |

If the organization has a style guide, use it. Do not import a style rule
from a different language or regulator without checking it.

## Sentence discipline

- One idea per sentence.
- Put the conclusion or the number first.
- Use an active subject: who did what, to what, when.
- Keep the verb close to the subject.
- Prefer the concrete over the abstract.
- Cut throat-clearing and self-reference.
- Do not use a semicolon to hide two unrelated ideas.

Weak:

> It should be noted that, in relation to the process concerned, a number
> of exceptions were identified during the review.

Stronger:

> The review found 14 exceptions in the approval process.

The second sentence is shorter, has a subject, and states the number.
The first sentence hides all three.

## Entity naming

- Use the full legal or official name at first use.
- Define the short name immediately.
- Use the same short name everywhere.
- Distinguish a legal entity from a governance body, a business unit, a
  system, and a project.
- Do not use a brand name as a synonym for a legal entity unless the
  organization does so formally.

Inconsistent naming makes it unclear who owns the finding and which
entity is affected.

## Citations

Every material statement should be traceable. A citation needs:

1. the document or data source name;
2. the issuer or owner;
3. the period or cut-off;
4. the precise location: page, paragraph, table, row, cell, field, or
   timestamp;
5. the evidence ID or workpaper reference, if the organization uses one.

A filename alone is not a citation. A folder name is not a citation. A
link that may break is not a citation unless the location is also
recorded.

## Ratios, counts, and units

- Give the numerator and denominator.
- State the period.
- State the unit and currency.
- State whether the denominator is the population, the tested sample, or
  the items with data.
- Do not use a percentage when the denominator is unknown.
- Do not compare ratios with different definitions or periods.
- Round only after the calculation, and state the rounding.

Weak:

> The completion rate was high.

Stronger:

> 12 of 30 applicable items were complete at the cut-off (40%).

The second sentence lets the reader check the claim.

## Modality and certainty

Use one modal verb for future or conditional risk. Do not stack
"may", "could", "might", and "potentially" in the same sentence. Choose
the level the evidence supports:

- **Is**: observed fact.
- **Indicates**: inference from evidence.
- **Could**: conditional possibility with a stated mechanism.
- **Will**: only with a deterministic mechanism or a commitment.

Do not use "clearly", "obviously", "proves", or "undoubtedly" unless the
evidence is direct and complete.

## Self-reported, independent, and observed

Label the source of each material figure:

- **Self-reported**: provided by the area being reviewed.
- **Independent**: provided by an external or independent party.
- **Observed**: seen or re-performed by the audit team.

Do not merge them into one number. A management update and an
independent test are not the same evidence.

## Neutral tone

- Describe the act and the condition, not the person.
- Do not attribute intent without evidence.
- Do not use loaded adjectives.
- Do not use irony, sarcasm, or rhetorical questions.
- Do not call a disagreement a failure of cooperation.
- State the auditee's position fairly, even when you disagree.

Be precise without being accusatory.

## False precision and unsupported numbers

- Do not give a decimal place the source does not support.
- Do not present an estimate as a measurement.
- Do not present a partial total as the total.
- Do not present a plan target as an actual result.
- Do not present a self-assessment as an independent finding.
- If a number cannot be traced, remove it or mark it as a known gap.

A precise-looking wrong number is worse than an honest range.

## Technical codes in the main narrative

Keep internal codes, ticket numbers, evidence IDs, module names, and
tool-specific identifiers out of the main narrative. Put them in:

- a source map;
- a traceability table;
- an appendix;
- a footnote, if the reader needs the link.

The main narrative should read as a business document, not a database
export.

## Language quality

- Read the report aloud, or use a read-aloud tool.
- Run the organization's language checker, if one exists.
- Check sentence length, repeated words, and machine-translated phrasing.
- Check that every acronym is expanded at first use.
- Check that every number has a unit and a period.
- Check that every "this" and "it" has a clear referent.
- Have a second reader mark every sentence they had to read twice.

## Drafting checklist

- [ ] The conclusion appears before the supporting detail.
- [ ] Every material number has a source, period, and unit.
- [ ] Every ratio has a denominator.
- [ ] Every entity is named consistently.
- [ ] Every citation has a precise location.
- [ ] Self-reported, independent, and observed data are distinguished.
- [ ] No unsupported certainty or intent attribution.
- [ ] No technical code appears in the main narrative.
- [ ] The language checker and a human read-aloud pass.

## Adaptation points

- Which language and style guide applies?
- What sentence length or readability target is required?
- Which citation style and evidence-ID convention are used?
- Which terms are approved, and which are forbidden?
- Who performs the language review?
