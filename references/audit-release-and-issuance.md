# Audit Release and Issuance

How to turn an approved draft into a clean, reproducible release.
Saving the file does not issue a report; issue it when the approved
version, the evidence package, the manifest, and the distribution
record agree.

This file is about the release layer. It does not replace the approval
authority's decision.

## What counts as a release

Define the release package in the engagement profile. A typical package
contains:

- the report in its approved format;
- the executive summary or cover note;
- the source map or evidence index;
- the evidence pack or data pack;
- the manifest;
- the hash list;
- the distribution record;
- the known-gap register.

Not every engagement needs every artefact. The profile decides.

## Versioning and preservation

- Give every release a version.
- Preserve the prior version unchanged.
- Archive the pre-release working copy before the final edit.
- Maintain a change log: version, change, reason, evidence, approver.
- Record what changed, why, and which evidence supports the change.
- Never overwrite an issued version.
- Keep the version identifier consistent across every artefact.

If a release contains two versions of the same document, recipients
will not know which is authoritative.

## Release manifest

The manifest should list:

| Field | Content |
| --- | --- |
| Artefact | File or item name |
| Version | Release version |
| Format | DOCX, PDF, XLSX, CSV, ZIP, or other |
| Size | File size |
| Hash | Content hash |
| Source | Workpaper or evidence ID |
| Status | Final, supporting, or reference |
| Owner | Who produced or approved it |

The manifest is the contract between the report and the package. If the
package does not match the manifest, stop.

## Integrity checks

Before release:

1. **Report hash**: the approved report hash matches the manifest.
2. **Cross-format hash**: the same content in different formats is
   generated from the same source version.
3. **Archive contents**: every file in the archive is listed in the
   manifest; no extra files, no missing files.
4. **Archive paths**: no internal codes, personal folders, temporary
   directories, or local drive paths.
5. **Spreadsheet formulas**: recalculate, then verify the cached values.
   If the tool rewrites links, perform the recalculation outside the
   synced folder and check the links again afterwards.
6. **Links**: stable, permission-appropriate, and free of download
   wrappers or session tokens.
7. **Page count and pagination**: the table of contents and page
   references match the final file.
8. **Language check**: the final file passes the language QA.
9. **Known gaps**: every known gap is disclosed in the report and the
   gap register.
10. **Distribution list**: the recipients match the confidentiality
    profile.

A clean result is part of the evidence. Record the checks and their
results.

## One cover note per version

Issue one cover note or email per version. It should state:

- the version;
- the decision or action requested;
- the key conclusion;
- the conditions or limitations;
- the list of attached artefacts;
- the approval status.

Remove duplicate unsuffixed versions and draft cover notes from the
release folder. A reader who receives two versions will read the wrong
one.

## Page-by-page visual QA

After every content or layout change:

1. Re-render the final format.
2. Open every page.
3. Check for overflow, overlap, cut headings, orphan rows, broken
   tables, missing figures, and unreadable footnotes.
4. Check the table of contents and page numbers.
5. Check the print view as well as the screen view.
6. Record the page-by-page result.

A report that is correct but unreadable in print is not ready.

## Charts and exhibits

- Use a resolution that matches the medium.
- Label axes and units.
- State the source and cut-off date under the exhibit.
- Start bar-chart axes at zero unless there is a stated reason not to.
- Do not encode a material distinction by color alone.
- Do not use a chart to hide a small denominator.
- Make the exhibit readable without the surrounding text.

## Approval gate

The approval authority approves the conclusion and the release. The
analyst or agent can:

- prepare the package;
- record that the evidence and review gates passed;
- list open conditions;
- flag a material gap.

The analyst or agent cannot approve its own conclusion, accept risk, or
issue the report on behalf of the authority.

After approval:

- do not change the content;
- if a change is required, create a new version, re-run the checks, and
  obtain approval again;
- record the change and the reason.

## NOT READY FOR DELIVERY

If a material gap remains unresolved, mark the package **NOT READY FOR
DELIVERY**. State:

- the gap;
- why it is material;
- what assurance is affected;
- what would close it;
- who owns the closure;
- when it will be re-checked.

Do not soften the status to avoid an uncomfortable conversation. A
conditional release is clearer than a false clean release.

## Known gaps

A known gap is not a failure of the report if it is disclosed. Record it
in:

- the report's limitations section;
- the gap register;
- the cover note, if it affects the decision;
- the next review cycle.

Do not remove a known gap because a later draft looks cleaner. Do not
replace a known gap with a plausible number.

## Post-release changes

If a material error is found after release:

1. Stop distribution of the affected version.
2. Record the error and the affected conclusions.
3. Correct the source, the report, and the manifest.
4. Re-run the integrity checks.
5. Issue a new version with a clear change note.
6. Notify the recipients through the approved channel.

Do not silently replace a released file. The history is part of the
assurance.

## Release checklist

- [ ] Approved version is the only version in the release folder.
- [ ] Prior version is preserved.
- [ ] Manifest matches the package.
- [ ] Hashes match.
- [ ] Archive contains only intended files and no internal paths.
- [ ] Spreadsheet formulas are recalculated and links are stable.
- [ ] One cover note per version.
- [ ] Every page has been visually checked.
- [ ] Language QA passes.
- [ ] Known gaps are disclosed.
- [ ] Approval authority has signed.
- [ ] Distribution list matches the confidentiality profile.

## Adaptation points

- Which artefacts make up a release for this engagement?
- Who approves, and what evidence do they require?
- Which integrity checks are mandatory?
- What is the retention and distribution policy?
- Who owns post-release corrections?
