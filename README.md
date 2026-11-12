<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg?v=2">
  <img src="assets/banner.svg?v=2" alt="evidence-triage banner">
</picture>

# evidence-triage

< English | [Tiếng Việt](./README.vi.md) >

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Version](https://img.shields.io/badge/version-3.0.0-0F172A)
[![CI](https://github.com/ducle2502/evidence-triage/actions/workflows/ci.yml/badge.svg)](https://github.com/ducle2502/evidence-triage/actions/workflows/ci.yml)
![Synthetic data only](https://img.shields.io/badge/data-synthetic%20only-15803D)

Evidence triage for internal audit teams. The skill looks for unusual
patterns, ranks what deserves attention, and takes one cohort to a
written conclusion.

> [!IMPORTANT]
> This repository is public. Do not commit employer, client, customer,
> or personal data, internal system or table names, tuned thresholds,
> or real investigation output. Every example is synthetic. See
> [references/confidentiality.md](references/confidentiality.md).

## Why

An agent given a vague instruction tends to run queries in every
direction and come back with observations that look odd but prove
nothing. Audit work makes that worse, because the result has to survive
review. A reviewer will ask which population you tested, which query
you ran, and how you ruled out the obvious alternative.

The skill answers those questions before you write the report:

- Three phases, each with its own output.
- Rules for when a shared attribute is enough to link two entities.
- Evidence that can be re-run and traced.
- One folder per session, so the next reviewer can pick it up.

## How it works

| Phase | Question | Audit use | Output |
| --- | --- | --- | --- |
| **Hunting** | What are we missing? | Risk sensing, continuous audit, anomaly discovery | Queries and extracts that surface candidate populations |
| **Triage** | What should we look at first? | Exception prioritization | A ranked short-list with cluster boundaries and risk |
| **Investigation** | What happened, and can we prove it? | A documented investigation | An evidence package and a written conclusion |

The phases usually run in order. You can start at any of them. The skill
reads your request, works out which phase you are in, and loads the
matching reference.

## Audit layer

The skill supports an audit workflow; the auditor, the methodology, and
the standards still govern the result.

- **Evidence.** It tests for sufficiency, relevance, and reliability,
  checks that the population is complete, and records the query, the
  extract, and the checks. See
  [references/audit-evidence.md](references/audit-evidence.md).
- **Findings.** It keeps the observed condition separate from the
  criteria, cause, effect, and recommendation. It also keeps fact,
  inference, and opinion apart. See
  [references/audit-findings.md](references/audit-findings.md).
- **Confidentiality.** It keeps the public repo generic and moves
  organization-specific knowledge into a private layer. See
  [references/confidentiality.md](references/confidentiality.md).
- **Judgment.** The skill assembles the evidence and the argument. The
  auditor rates and signs the conclusion.

The reporting set in
[references/audit-index.md](references/audit-index.md) extends this
into engagement profiling, report design, review, release, and public
safety.

If your organization has its own terminology or methodology, use it.
The defaults here are a starting point.

## Invoke it

Describe the work in plain language. Examples:

- "Anything unusual in this quarter's vendor master changes?" → hunting
- "Rank these 200 journal-entry exceptions." → triage
- "These 12 vendor records look related. Investigate them." → investigation
- "After-hours access to the payment table jumped last month. What happened?" → hunting → triage → investigation
- "Check the approvals that skipped the second reviewer." → investigation

## Installation

Clone the repo, or download the ZIP from **Code → Download ZIP** and
unzip it into the install folder.

### Claude Code

Install at the user level to make the skill available in every project:

```bash
git clone https://github.com/ducle2502/evidence-triage.git \
  ~/.claude/skills/evidence-triage
```

Or use the ZIP:

```bash
unzip evidence-triage-main.zip -d ~/.claude/skills/
mv ~/.claude/skills/evidence-triage-main ~/.claude/skills/evidence-triage
```

Restart Claude Code and check `/skills`, or trigger the skill with an
audit question.

For a single project, install under `.claude/skills/evidence-triage/`
in that project instead.

### Claude Cowork

Cowork installs plugins, not raw skills. If you run Cowork through the
Claude desktop app, it reads the same user-level skills directory, so
the Claude Code instructions work.

The repo has no `.claude-plugin/plugin.json` manifest. If you need the
custom-plugin route, add a minimal manifest in a private fork or open
an issue.

### OpenAI Codex

For a per-repo install, put the files under `.agents/skills/` at the
root of the repo you are working in:

```bash
mkdir -p .agents/skills
git clone https://github.com/ducle2502/evidence-triage.git \
  .agents/skills/evidence-triage
```

Codex finds skills under `.agents/skills/` by walking up from the
working directory.

For a global install, register the path in `~/.codex/config.toml`:

```toml
[[skills]]
path = "/absolute/path/to/evidence-triage"
enabled = true
```

Use `/skills` in the Codex CLI or IDE, or describe an audit task.

## Repository layout

```text
evidence-triage/
├── SKILL.md                       # entry point and router
├── references/
│   ├── hunting.md                 # phase: hunting (find new patterns)
│   ├── triage.md                  # phase: triage (rank exceptions)
│   ├── investigation.md           # phase: investigation (drive a cohort to a verdict)
│   ├── linkage-attributes.md      # when shared attributes link entities
│   ├── fraud-patterns.md          # common typologies and their signals
│   ├── output-conventions.md      # workspace layout and slug rules
│   ├── audit-evidence.md          # evidence standards, workpapers, chain of custody
│   ├── audit-findings.md          # condition / criteria / cause / effect / recommendation
│   ├── confidentiality.md         # public-repo rules and redaction
│   ├── audit-index.md             # entry point for the audit reporting set
│   ├── audit-engagement-profile.md
│   ├── audit-evidence-model.md
│   ├── audit-evidence-triage.md
│   ├── audit-claim-and-conclusion.md
│   ├── audit-report-architecture.md
│   ├── audit-drafting-and-style.md
│   ├── audit-review-lenses.md
│   ├── audit-failure-modes.md
│   ├── audit-release-and-issuance.md
│   ├── audit-public-safety.md
│   ├── audit-templates.md
│   └── audit-index.vi.md           # Vietnamese index
├── assets/                        # banner and social preview
├── docs/                          # architecture and GitHub setup
├── scripts/                       # repository validation
├── .github/                       # issue forms, PR template, labels, CI
├── README.md
├── README.vi.md
├── AGENTS.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── VISION.md
├── CHANGELOG.md
└── LICENSE
```

## Local customization

Every audit team has its own signals, schema, thresholds, and prior
incidents. Keep that material out of this repo:

1. Put it in a private repo or a local folder such as `local/`, which
   `.gitignore` excludes.
2. Add markdown files for your named signals, schema, typologies,
   thresholds, and past cases.
3. Point a private wrapper skill, or a local copy of `SKILL.md`, at
   those files. Do not put internal file names in the public reference
   table.
4. Keep the public repo generic.

The overlay can live anywhere. Never commit real data "temporarily",
because git history keeps it. See
[references/confidentiality.md](references/confidentiality.md).

## Origins

This repo started from
[finic-ai/fraud-investigation-skills](https://github.com/finic-ai/fraud-investigation-skills)
under the MIT License. This repo keeps that project's three-phase
method and typologies; [VISION.md](VISION.md) covers what this version
adds and changes.

Maintained by duke2502.

## License

MIT. See [LICENSE](LICENSE). The original copyright belongs to Finic.
Changes are copyright duke2502.
