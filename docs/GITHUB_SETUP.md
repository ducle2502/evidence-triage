# GitHub setup

Manual settings checklist for `ducle2502/evidence-triage`. The
repository files are committed. Configure these steps in the GitHub UI;
the `gh` commands below work once `gh` is installed.

## Repository description

Use:

> Internal audit evidence triage for AI agents: hunting, exception
> triage, and investigation with audit-grade evidence, findings, and
> reporting references. Synthetic examples only.

## Topics

```text
internal-audit
audit
evidence
triage
fraud
investigation
agent-skills
claude-code
codex
forensics
```

## Social preview

Upload `assets/social-preview.png` (1280×640):

Settings → General → Social preview → Edit → Upload image.

The light SVG source is `assets/banner.svg`. The dark variant is
`assets/banner-dark.svg`.

## Labels

The label set is defined in `.github/labels.json`. Apply it after
installing `gh` and authenticating:

```powershell
Get-Content .github/labels.json -Raw | ConvertFrom-Json | ForEach-Object {
  gh label create $_.name --color $_.color --description $_.description --force
}
```

Or create the labels manually in Issues → Labels, using the names,
colors, and descriptions in the JSON file.

Apply labels before you enable the issue forms. The forms reference
`type: bug`, `type: feature`, `type: question`, and
`status: needs-triage`.

## Branch ruleset

Settings → Rules → Rulesets → New branch ruleset.

Solo maintainer setup:

- Target branch: `main`
- Enforcement: Active
- Require a pull request before merging: on, with 0 required approvals
- Block force pushes: on
- Restrict deletions: on
- Require linear history: on
- Bypass list: repository admin

If a second maintainer joins, raise required approvals to 1 and enable
"Require review from Code Owners".

Legacy branch protection also works; these steps assume rulesets.

## Security

Settings → Code security and analysis:

- Private vulnerability reporting: on.
- Secret scanning: on.
- Push protection: on.

The repository has no runtime dependencies, so Dependabot alerts are
optional. Keep them on if you add automation later.

## Features

Settings → General:

- Wikis: off.
- Discussions: optional; enable if you want usage questions outside
  issues.
- Projects: off unless you plan a roadmap.
- Sponsorships: optional.

## Release

After the first push of version 3.0.0:

```bash
git tag -a v3.0.0 -m "evidence-triage 3.0.0"
git push origin v3.0.0
```

Then create a GitHub release from the tag and paste the `3.0.0` section
of [CHANGELOG.md](../CHANGELOG.md).

## Verification

- [ ] Description and topics set.
- [ ] Social preview shows the banner.
- [ ] Labels created and visible.
- [ ] Issue forms open without a label error.
- [ ] Ruleset active on `main`.
- [ ] Secret scanning and push protection enabled.
- [ ] CI passes on the first pull request.
- [ ] Release `v3.0.0` exists.
