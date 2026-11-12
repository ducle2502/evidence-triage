---
name: evidence-triage
description: Use for internal audit and fraud-analyst work that turns a population of records into evidence: risk sensing and hunting for new patterns, triaging exceptions into a prioritized short-list, and investigating a specific cohort to a documented conclusion. Triggers include internal audit, audit evidence, exception testing, control gaps, workpapers, findings, fraud hunting, fraud triage, ATO / account takeover, first-party fraud, dispute fraud, mule activity, money laundering, suspicious clusters or cohorts, ranking alerts, "look into these accounts", "check this signal", "find what's worth investigating", shared device identifiers, named signals, and vague requests like "anything weird?", "what should I look at?", "spike in X", or "these records look related". The skill classifies the phase and routes accordingly.
version: 3.0.0
---

# evidence-triage

Evidence triage for internal audit and fraud work. The skill has three
phases. They usually run in sequence, but each one is a valid entry
point.

- **Hunting.** No seed cohort. Scan a domain for patterns the current
  monitors miss. In audit terms, this is risk sensing and anomaly
  discovery. The output is queries and extracts that surface candidate
  populations.
- **Triage.** A population exists. Rank it, mark the cluster
  boundaries, and size the risk. In audit terms, this is exception
  prioritization.
- **Investigation.** A specific cohort exists. Test hypotheses, gather
  evidence, and write the conclusion. In audit terms, this is a
  documented audit investigation.

Investigate **coordinated** activity: clusters of users, accounts,
vendors, transactions, or other entities linked by a strong shared
attribute, or by several weak attributes that overlap. One-off
exceptions can be raised when impactful and unmitigated, but do not
focus on them.

## Audit context

This skill sits inside an internal audit workflow. It does not replace
the workflow, the auditor, or the standards. It uses public, general
audit concepts:

- **Evidence.** Sufficiency, relevance, reliability, corroboration, and
  population completeness. See `references/audit-evidence.md`.
- **Findings.** Condition, criteria, cause, effect, and recommendation.
  Keep fact, inference, and opinion apart. See
  `references/audit-findings.md`.
- **Professional judgment.** The skill produces the analysis and
  evidence. The auditor owns the conclusion and signs the report.
  Follow the organization's methodology and the applicable standards,
  such as the IIA Global Internal Audit Standards and COSO.

If the organization has its own methodology, terminology, or templates,
those take precedence over the defaults here.

## Terminology

These are general terms. If the organization uses a more specific term,
adopt it.

**Mitigated:** the organization has acted on the account or finding.
That could mean restricted, closed, blocked, frozen, suspended,
accepted, or another remediation step. No further action is needed.

**Unmitigated:** still a live surface where loss, misstatement, or
customer harm can happen. The account is not restricted, funds are
still in transit, or the control is still unaddressed.

## Step 0: consult the reference library

List the organization's reference docs (commonly
`.claude/skills/<this-skill>/references/` plus any local `docs/`
folder in the repo). They encode tribal knowledge — known red flags,
KRIs, prior typologies, which signals are strong vs. weak. Skim broadly
in hunting; read topic-relevant ones in scoped phases.

This skill ships its own references:

| File | When to read it |
| --- | --- |
| `references/hunting.md` | Hunting mode. |
| `references/triage.md` | Triage mode. |
| `references/investigation.md` | Investigation mode. |
| `references/linkage-attributes.md` | Deciding whether to expand a cluster. |
| `references/fraud-patterns.md` | Common typologies and their signals — for naming clusters, picking angles, and choosing evidence queries. |
| `references/output-conventions.md` | Workspace folder layout and slug rules. |
| `references/audit-evidence.md` | Audit evidence standards, workpaper conventions, and data-integrity checks. Read before documenting evidence in any phase. |
| `references/audit-findings.md` | Turning analysis into a finding or conclusion: condition, criteria, cause, effect, recommendation. |
| `references/audit-index.md` | Entry point for the audit reporting set; reading order by task. |
| `references/audit-engagement-profile.md` | Engagement type, report type, conclusion scale, and review depth. |
| `references/audit-evidence-model.md` | Evidence intake: categories, source hierarchy, and custody. |
| `references/audit-evidence-triage.md` | Fitness of each evidence item against a specific claim. |
| `references/audit-claim-and-conclusion.md` | Testing whether the evidence set supports the conclusion. |
| `references/audit-report-architecture.md` | Report structure and argument order. |
| `references/audit-drafting-and-style.md` | Drafting, wording, and style rules. |
| `references/audit-review-lenses.md` | Review perspectives for a draft. |
| `references/audit-failure-modes.md` | Common ways audit reports fail. |
| `references/audit-release-and-issuance.md` | Release, approval, and issuance checks. |
| `references/audit-public-safety.md` | Preparing public examples without leaking data. |
| `references/audit-templates.md` | Workpaper and checklist templates. |

Vietnamese translations sit next to their English source as `X.vi.md`.
The router reads the English source; use the translation when the
reader needs Vietnamese.

In audit work, start with `audit-index.md` for the reporting set. Read
`audit-evidence.md` before producing artifacts, and `audit-findings.md`
before writing the conclusion.

Don't try to do hunting / triage / investigation from memory; the
phase references are the heart of the skill.

## Step 1: classify the phase

- **Hunting** — rough direction with no seed cohort, no scope at all,
  or a domain to scan but no specific entities. In audit terms, this
  includes continuous-audit monitoring and risk sensing.
- **Triage** — user has data to rank; phrases like "rank these",
  "where are the boundaries", "top candidates", or a file with cohort
  data and a request for prioritization. In audit terms, an exception
  population that needs prioritization.
- **Investigation** — user has a specific cohort (seed list, signal
  resolved to users, device cluster); phrases like "investigate
  these", "build a case", "what are they doing"; or a follow-up to
  triage opening a case on a top alert.

If genuinely ambiguous between two phases, ask one clarifying
question — usually "do you already have a cohort, or are you looking
for one?" Once classified, read `references/<phase>.md` and follow it.

## Sequential handoffs

When a phase ends, suggest the next one in plain terms (describe what
would happen; don't name the skill or a command) and wait for the
user's go-ahead. Don't auto-execute. If the user defers, recommend the
top 1–2 candidates by priority + exposure.

The user can start at any phase, skip phases, or loop back. If a
finding overlaps a known cluster, surface it and ask whether to extend
the existing case or move on.

## Cohort exposure

Required in triage and investigation. Optional in hunting (useful
context, but not worth interrupting fast iteration for).

The goal is to size the live surface a cohort represents so ranking
isn't driven by raw count alone — a 200-user cluster that's all
mitigated is worth less than a 5-user ATO ring with $500K of live
balance. The right metrics depend on what the organization's accounts
do:

- **Common across most organizations:** account balance (static exposure),
  money-in volume over a recent window (flow), money-out volume
  (drain).
- **Organization-specific examples:** loan amounts outstanding, crypto
  trading volume, disbursement volumes, promotional credit amounts,
  card transaction volume, merchant-of-record exposure.

Pick 2–4 metrics that best capture *"if this cohort remained undetected
what would the financial impact be?"*. Always include both a static
and a flow metric — static-only misses drained-but-flowing patterns (mule,
ATO with same-day drain). Always split each metric into mitigated vs.
unmitigated portions, and present them side-by-side in any output table;
never collapse.

## Save every query, reuse what's already there

Save every query and every result, every time. One `.sql` paired with
one `.csv`, written into the workspace's `data/` folder with a
chronological prefix and descriptive slug:
`data/03_ach-originator-grouping.sql` +
`data/03_ach-originator-grouping.csv`.

Default location: agent workspace under
`{workspace_root}/{date}_{slug}/`. If the user names another
location, treat that as `{workspace_root}` for the session.

Before writing a new query, grep the workspace by attribute, signal,
table, or slug. Adapt close matches; for exact-question matches,
surface the prior result rather than re-running, unless the result
is stale.

## Other shared principles

- **Time-boxing.** Hunting: 15–45 minutes. Triage: ~10–15 minutes.
  Investigation: variable, but >60 minutes without a check-in is a
  sign something's off.
- **Query cost discipline.** Refine before forcing. Cohort-selection
  queries (producing the case CSV in triage or investigation setup)
  must stay under the soft limit (commonly ~100k rows). Per-user
  data-pull pipelines for an existing cohort may legitimately use
  forcing.
- **Cross-reference for novelty.** Every promising finding gets
  cross-checked against prior workspaces (grep `{workspace_root}` for
  user IDs, device identifiers, or attribute values) and against
  recent monitor output. Findings that fully overlap prior work or
  an active monitor aren't novel; usually not worth opening as a new
  workspace. Record the verdict explicitly in `investigation.md`.
- **Cluster-expansion discipline.** Don't silently expand a cluster
  on weak or single-moderate signals. Attributes are **strong** (link
  on their own — device keys, payment instrument tokens, low-occurrence
  counterparties), **moderate** (link only in combination — IP,
  browser fingerprint, uncommon email domains), or **weak** (slicing
  only — user-agent, DOB, common email domains, area code, signup
  time). See `references/linkage-attributes.md` for the
  lift-plus-significance ratio test.
- **Output discipline.** All artifacts for a session live under one
  workspace folder `{workspace_root}/{YYYY-MM-DD}_{slug}/`, with
  `data/` for query artifacts and `investigation.md` as the single
  running document. Slug is
  2–4 kebab-case words describing the hypothesis, angle, or alert.
  See `references/output-conventions.md`.

## What this skill does NOT do

- Run downstream investigation pipelines (per-user data-pull scripts,
  automated analyst loops). Prepare the inputs and hand off.
- Build monitors. If an investigation concludes a pattern should be
  monitored, recommend it in the report. Building it is separate work.
- Take remediation action (restrict accounts, close findings, file
  reports). The accountable function acts on the analysis.
- Replace professional judgment or issue an audit opinion. The skill
  assembles evidence and a defensible narrative. The auditor concludes.
- Guarantee completeness. A negative test means you did not find the
  condition, not that it was absent. State the limits of the population
  and the tests.
