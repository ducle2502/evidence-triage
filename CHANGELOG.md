# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2026-11-12

### Added

- Internal audit layer: `references/audit-evidence.md` and
  `references/audit-findings.md`, plus public-repo rules in
  `CONTRIBUTING.md` and `SECURITY.md`.
- Audit reporting set starting at `references/audit-index.md`:
  engagement profile, evidence model, evidence triage, claim testing,
  report architecture, drafting, review, failure modes, release,
  public safety, and templates.
- Vietnamese audit index: `references/audit-index.vi.md`.
- Audit triggers in the `SKILL.md` description.
- Vietnamese README (`README.vi.md`).
- Banner assets, social preview, repository documentation, issue forms,
  pull request template, label definitions, validation CI, and a
  repository validation script.

### Changed

- Renamed the skill from `fraud-investigation` to `evidence-triage`.
- Reframed the README and install paths for internal audit use.
- Retained the Finic MIT notice and added the maintainer copyright.

## [2.0.0] - upstream baseline

- Baseline import of the three-phase fraud investigation skill from
  [finic-ai/fraud-investigation-skills](https://github.com/finic-ai/fraud-investigation-skills).
