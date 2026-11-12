# Security Policy

## Supported versions

The current major version (3.x) is supported. Older versions may receive
documentation fixes at the maintainer's discretion.

## Reporting a vulnerability

Use GitHub private vulnerability reporting:

<https://github.com/ducle2502/evidence-triage/security/advisories/new>

Do not open a public issue for a security problem. Include the affected
file, a reproduction, and the impact you believe it has.

## Confidential data exposure

This repository is public. If confidential, personal, or employer data
has been committed:

1. Treat it as a security incident and stop pushing.
2. Notify the organization's security or compliance contact through the
   approved channel.
3. Remove the data from the working tree, the commit, and the remote
   history as directed.
4. Rotate any exposed credentials immediately.
5. Do not paste the exposed data into an issue, discussion, or pull
   request.

Removing a file in a later commit does not remove it from history.
Assume anything pushed to a public remote is already disclosed.

## Scope

This policy covers the skill instructions, reference content, scripts,
and workflows in this repository. It does not cover the security of the
data platform or audit tooling you connect the skill to. Use the
organization's own controls for that.

## Response

The maintainer will acknowledge a report as soon as practical, assess
it, and coordinate a fix and disclosure timeline with the reporter.
