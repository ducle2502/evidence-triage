# Audit Failure Modes

A catalogue of ways audit reporting goes wrong. Each entry gives the
signal, why it fails, the fix, and the prevention. Use it as a
self-review before drafting, reviewing, or releasing.

The list is not exhaustive. If a new failure mode appears, add it here
and map it to the relevant topic file.

## Evidence failure modes

| Failure | Signal | Why it fails | Fix | Prevention |
| --- | --- | --- | --- | --- |
| Filename as data | The number exists only in a file name or folder label | The content may say something different | Open the source and verify the value | Treat metadata as a pointer, not evidence |
| Stale copy | A working copy is older than the authoritative source | The report describes a superseded state | Reconcile the hash and check source history | Record the source and snapshot date |
| Source mismatch | Two versions of the same document differ | The wrong version may be cited | Register a new version and mark the old one superseded | Append-only evidence register |
| Self-authored evidence | The only support is a document from the area being reviewed | It proves an assertion, not the fact | Seek independent or system evidence | Apply the source-tier test |
| Meeting note as progress | The note records a discussion, not a completed action | Activity is mistaken for outcome | Verify the action in the system or output | Distinguish discussion, decision, action, and result |
| Derived metric | A grouping or ratio is based on a blank, mapped, or imputed field | The aggregate looks like raw data but is not | Trace the derivation and re-verify against records | Require a provenance chain for every aggregate |
| Double count | The same exposure appears under multiple findings | The total overstates the risk | Define pools and an anti-double-count rule | Reconcile the total to the pool |
| Blocked as zero | A metric is reported as zero because it could not be measured | Zero looks like a clean result | Report "not measured" with the reason | Make blocked metrics a first-class status |
| Missing denominator | A percentage has no population or sample | The reader cannot judge the rate | State numerator, denominator, period, and unit | Use a ratio template |
| False precision | A number has more decimals than the source supports | It implies accuracy that does not exist | Round to the source precision or use a range | Match precision to the evidence |
| Hidden gap | A known gap is omitted from the report | The conclusion looks more complete than it is | Disclose the gap and its assurance impact | Keep a gap register |
| Claim beyond evidence | The conclusion covers more than the evidence set | The finding cannot be defended | Narrow the claim or expand the evidence | Run claim QC |
| Causal overreach | A sequence is presented as a cause | Correlation is mistaken for causation | State the mechanism and test alternatives | Use the event chain and falsification test |
| Merged branches | Independent causes are joined into one chain | The narrative is cleaner than the evidence | Separate the branches and label each status | Do not merge without a mechanism |
| No falsification condition | No evidence could weaken the conclusion | The conclusion is not empirical | State what would change it | Reverse-conclusion test |
| Trend from non-equivalent periods | Two periods with different scope or method are compared | The trend is an artifact | Normalize the periods or state the limitation | Check comparability before comparing |

## Claim and conclusion failure modes

| Failure | Signal | Why it fails | Fix | Prevention |
| --- | --- | --- | --- | --- |
| Fact and inference blurred | An inference is written as an observed fact | The reader cannot tell what is proven | Label fact, inference, and condition | Use a claim-type column |
| Cause and symptom mixed | The recommendation addresses the symptom | The condition recurs | Separate direct, root, and contributing cause | Use a cause table |
| Surface fix as root cause | The action removes the visible symptom only | The underlying mechanism remains | Identify the control failure and the mechanism | Ask why until the evidence stops |
| Unproven root cause stated as fact | A plausible cause is presented as confirmed | The finding is vulnerable to challenge | Keep the status "insufficient evidence" | Record the why-level cap |
| Intent attribution | The report implies bad faith without evidence | It is unfair and creates defamation risk | Describe the act and the control failure | Require evidence for intent |
| Individual blame | A person is named as the cause | It ignores the system conditions | Analyze authority, training, workload, and controls | Use a system view |
| Decision judged by outcome | A past decision is criticized using later information | It is hindsight bias | Judge by the information available at the time | State the information set |
| No alternative explanation | Only one explanation is considered | Confounders may be missed | List alternatives and test them | Use a falsification table |

## Report failure modes

| Failure | Signal | Why it fails | Fix | Prevention |
| --- | --- | --- | --- | --- |
| Buried conclusion | The reader must reach the end to learn the answer | The decision-maker cannot act | Put the conclusion and ask first | Use a decision layer |
| Technical codes in the body | The narrative reads like a ticket log | The reader loses the business message | Move codes to a source map or appendix | Use a jargon filter |
| Positive percentage hides an unmet condition | A high completion rate is presented without the mandatory gate | The reader may approve a blocked programme | Report both the percentage and the mandatory condition | Use a gate table |
| Activity as completion | A meeting, document, or training is counted as done | The outcome is not verified | Distinguish activity, output, outcome, assurance | Use a closure test |
| Generic impact | "This creates risk" with no path | The reader cannot prioritize | Show the transmission path, delay, and reversibility | Use an impact chain |
| Unsupported recommendation | The action is not owned, feasible, or measurable | It cannot be closed | Add owner, date, criterion, evidence, confirmer | Use a recommendation template |
| No closure evidence | The action is accepted on assertion | The finding may recur | Define the evidence that proves remediation | Require independent closure evidence |
| Appendix dependency | The body cannot be understood without the appendix | The report does not stand alone | Move the essential reasoning into the body | Run the standalone test |
| Inconsistent numbers | The same metric differs across documents | Trust is destroyed | Use one source and one reconciliation | Cross-document check |
| Entity naming drift | The same entity has several names | Ownership and scope become unclear | Define names at first use and use them consistently | Run a naming check |
| Overloaded report | Every detail is in the main narrative | The decision is hard to find | Move detail to the explanation and verification layers | Apply the reader-first test |

## Review failure modes

| Failure | Signal | Why it fails | Fix | Prevention |
| --- | --- | --- | --- | --- |
| Reviewer fixes conclusions | The reviewer rewrites the finding | The owner loses accountability | Record the exception; the owner decides | Separate review from ownership |
| One reviewer covers everything | The same person checks numbers, cause, language, and packaging | Conflicts of attention and expertise | Assign independent lenses | Use a lens menu |
| No falsification | The review asks "is this supported?" but not "what would break it?" | Weak conclusions survive | Run the reverse-conclusion test | Add an adversarial lens |
| No failure scenario | The team assumes the report will be accepted | It is unprepared for challenge | Simulate publication and challenge | Add a red-team lens |
| No unintended-consequence test | Recommendations create new risks | The fix becomes the next problem | Test secondary effects | Add a consequence lens |
| Redundant reviewers | Many people read the same scope | Cost without additional assurance | Assign distinct scopes | Plan the review by lens |
| Review record missing | No one can show what was reviewed | The review is not auditable | Record lens, scope, result, evidence, reviewer | Use a review scorecard |

## Release failure modes

| Failure | Signal | Why it fails | Fix | Prevention |
| --- | --- | --- | --- | --- |
| Version mismatch | The report and the package have different versions | The reader may use the wrong file | Regenerate the package from the approved source | Version the manifest |
| Duplicate cover note | Two emails or notes exist | Recipients may act on the wrong one | Keep one cover note per version | Clean the release folder |
| Local paths in the package | A file references a personal or temporary folder | It leaks information and breaks for the reader | Replace with stable, permission-appropriate links | Run a path scan |
| Uncorrected formulas | A spreadsheet shows stale cached values | The reported number is wrong | Recalculate and verify the cached value | Add a formula check |
| Page overflow | Tables or headings run off the page | The report is unreadable in print | Re-render and fix the layout | Page-by-page QA |
| Missing hash | The manifest has no hash for an artefact | Integrity cannot be verified | Add the hash and re-verify | Use a manifest template |
| Post-approval edit | Content changes after approval | The approved version is not what is issued | Create a new version and re-approve | Lock the approved file |
| Sensitive residue | Metadata, comments, or tracked changes remain | Confidential content leaks | Scrub metadata and review the diff | Pre-release confidentiality check |

## Governance failure modes

| Failure | Signal | Why it fails | Fix | Prevention |
| --- | --- | --- | --- | --- |
| Hardcoded workflow | The method assumes a fixed number of phases, gates, or report sections | It does not fit the engagement | Use the engagement profile to select the pattern | Keep the workflow configurable |
| Plan numbers treated as truth | A self-reported target is used as an actual result | The report repeats an unverified claim | Verify against a source | Separate plan, actual, and evidence |
| Closure on assertion | The auditee says it is fixed | The condition may persist | Test the closure evidence | Require independent confirmation |
| Individual error only | The review stops at the person who made the mistake | The system condition remains | Check authority, training, workload, and controls | Use a system view |
| No base rate | An unusual period is treated as a trend | Regression to the mean is missed | Compare with the base rate | Add a baseline check |
| No stop rule | The team keeps collecting evidence | Analysis paralysis | Stop when new evidence no longer changes the decision | Set a decision threshold |
| Pre-formed conclusion | Evidence is selected to fit the expected answer | Confirmation bias | State the question and criteria first | Run a disconfirming-evidence check |
| Over-generalization | The method is so abstract that it gives no guidance | The reader cannot act | Keep concrete decision rules and examples | Test the method on a real scenario |
| Confidentiality breach | A real name, number, or incident appears in a public example | Irreversible disclosure | Remove it and follow the incident process | Use the public-safety checklist |

## Adaptation points

- Which failure modes are most likely in this audit type?
- Which are blocking, and which are advisory?
- Who owns the fix for each failure?
- How are failures recorded and trended across engagements?
