# Internal Audit Reporting Reference

Entry point for the audit-reporting lessons in this folder. These files
are deliberately domain-neutral: they apply to financial, operational,
compliance, IT, project-assurance, third-party, fraud, and investigative
engagements. They describe patterns and decision rules, not a mandatory
methodology.

Bản tiếng Việt: [`audit-index.vi.md`](audit-index.vi.md).

Read `audit-evidence.md` and `audit-findings.md` first if you need the
basics of usable evidence and finding anatomy. The files below extend
those basics into evidence triage, claim testing, report architecture,
drafting, review, and release.

## Reading order by task

| Task | Start with | Then |
| --- | --- | --- |
| A new engagement | `audit-engagement-profile.md` | `audit-evidence-model.md` |
| Evidence intake or a new document set | `audit-evidence-model.md` | `audit-evidence-triage.md` |
| Deciding what evidence to trust or pursue | `audit-evidence-triage.md` | `audit-claim-and-conclusion.md` |
| Testing whether a conclusion is supported | `audit-claim-and-conclusion.md` | `audit-review-lenses.md` |
| Designing the report | `audit-report-architecture.md` | `audit-drafting-and-style.md` |
| Reviewing a draft | `audit-review-lenses.md` | `audit-failure-modes.md` |
| Issuing a report | `audit-release-and-issuance.md` | `confidentiality.md` |
| Preparing public examples | `confidentiality.md` | `audit-public-safety.md` |
| Building a workpaper or checklist | `audit-templates.md` | The relevant topic file |

## Global rules

1. **Evidence before conclusion.** Do not select evidence to fit a
   conclusion that already exists. State the question and criteria first.
2. **Evidence fitness is claim-specific.** A system extract may prove a
   count; a signed approval may prove authority; a meeting note proves
   only that a discussion was recorded.
3. **No fabricated values.** A blocked or unmeasured metric is a finding,
   not a zero. Record the blocking reason, the missing evidence, and the
   assurance impact.
4. **No hardcoded workflow.** Use the engagement profile to select the
   report type, conclusion scale, review depth, gates, and artefacts.
5. **No silent overwrite.** Evidence and report versions are append-only;
   preserve the prior version and record the supersession.
6. **Public safety.** This repository is public. Read
   `confidentiality.md` before adding any example, name, number, path, or
   screenshot.
7. **Professional judgment prevails.** These files are aids, not a
   substitute for the organization's methodology, applicable standards,
   legal advice, or the approval authority.

## How the files fit together

```text
engagement profile
        |
        v
evidence model ---> evidence triage ---> claim and conclusion
                                             |
                                             v
                                  report architecture ---> drafting
                                             |                 |
                                             v                 v
                                       review lenses <--- failure modes
                                             |
                                             v
                                  release and issuance
                                             |
                                             v
                                  public safety / confidentiality
```

The arrows show a common path, not a required sequence. An engagement may
start at any point, loop back, or use only one file.

## Adaptation points

- Which files are mandatory in your methodology?
- Which report type and conclusion scale does the engagement use?
- Which review lenses and review depth are proportionate to the risk?
- Which gates and artefacts does the approval authority require?
- Which language and citation profile applies?
