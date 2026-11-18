# Validation and claim limits

These are maintainer-reported checks and results, separated by version.
For the original controlled acceptance case, the external evaluator was separate
from the candidate, not an independent public auditor. Raw private artifacts are
not distributed, so this report alone is not a publicly reproducible benchmark.

## Evidence at a glance

| Evidence | What it supports | What it does not support |
| --- | --- | --- |
| Original 1.0 acceptance | The agreed workshop-waitlist outcome on two host/model configurations | General superiority or validation of later changes |
| Recorded consumption | A lower token count in that known case, with comparator limits below | A universal savings rate or speed advantage |
| Later focused exercises | Specific observed decisions and behaviors | Causal reliability gains or a full new acceptance run |
| Package tests | Manifest consistency, hook output, and relocation | Model compliance or automatic activation in every host |

## 2.1.0, 18 November 2026

We installed 2.0.0 and the candidate in separate Codex CLI 0.159.0 profiles.
The task prompts, product-owner replies, fixture setup and executable graders
are in [portable workflow exercises](../tests/scenarios/portable-workflows.md).
We inspected the bootstrap delivered to the scored sessions. An earlier setup
still exposed user-level Superpowers skills and was excluded. The clean runs
disabled those ambient skills per process. Fresh handoff consumers had the
same host defaults with plugins disabled and received only their respective spec
as task data. These are maintainer-run synthetic exercises, one run per cell.

| Exercise | 2.0.0 | Final candidate |
| --- | --- | --- |
| Merge saved views, Sol | Implemented a duplicate rule before asking. It happened to match the later decision. | Asked what counts as a duplicate before editing. After the reply all five checks passed, as on 2.0.0. |
| Same request, Astra, different user preference | Its first patch failed three of five checks for that preference. It corrected the patch after the reply. | Asked before editing. Its first implementation after the reply passed all five. |
| Transfer to draft expiry, Sol | Asked which date starts the clock. | Also asked. Both passed after clarification and implemented directly in the fully specified control. |
| Spec passed to a fresh implementer, Sol | Five of five input/output and preservation cases passed. | Five of five passed. An earlier candidate incorrectly turned an absent slot into a blank line and failed two; the reader faithfully implemented the faulty spec. |
| Repair with an offline feed, Sol | Four of four external CLI cases passed. Used the captured feed. | Same result. The checks cover the saved feed and the resulting report. |
| PR review, Sol | Found the newly reachable failure, with no unrelated blocking comments. | Same result. The unchanged helper now receives a valid input that the old caller filtered out. |

The control with workflow plugins disabled also guessed the merge rule on Sol.
The first candidate guessed it too. We revised clarification to check for
different visible outcomes that satisfy the same constraints, and spec revision
to preserve the rules the new decision leaves in force. The merge retest is a
development regression. The separate expiry task checks transfer and unnecessary
questioning. These exercises do not measure failure rates in the field.

For the six matched Sol workflows (review, handoff including its consumer,
repair, two-turn merge, two-turn expiry, and settled expiry), the CLI reported:

| Version | Input incl. cache hits | Cached input | Input minus cache hits | Output incl. reasoning | Sum of active turn seconds |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2.0.0 | 781,098 | 646,400 | 134,698 | 10,085 | 297.06 |
| 2.1.0 candidate | 721,091 | 511,872 | 209,219 | 11,107 | 335.62 |

Each resumed conversation contributes its final cumulative token counter once.
Active times exclude waiting for the operator and may overlap across exercises.
The requested models were GPT-6.1 Sol and GPT-6 Astra, medium reasoning. Cache
utilization varied; these observations do not establish lower cost or latency.
The startup skill itself shrank from 8,382 to 5,198 bytes. Both builds in that
comparison had 30 skills. On the two-turn Astra merge case, 2.0.0 used 167,292 input
tokens (144,384 cached) and 2,199 output. The candidate used 190,646 input
(167,808 cached) and 2,182 output. Active times were 70.12 and 70.77 seconds.

The 15 package tests passed, as did metadata validation for all 30 skills.
Claude Code 2.1.319 accepted the plugin and marketplace manifests. Model
execution in this comparison used Codex. No new end-to-end Devin or Claude
behavioral run was recorded.

### Same-session intent receipt

In a synthetic archive task on Codex CLI 0.159.0 with GPT-6.1 Sol at medium
reasoning, the user supplied a rule without an example. Before editing, the
agent worked out that visible A, B, A followed by a withdrawn B should yield
B, A. Its delivery reply reported that same result from the local Python API,
and the named test asserted it. We then substituted first-occurrence ordering
and three tests that still passed. Asked to review the checkout in the same
conversation, the agent observed A, B and flagged the mismatch. The working
files were unchanged during review. An earlier draft ran the right check but
omitted the observation from its successful delivery reply. This exercise
covers local behavior on one model.

### Reusing coverage and adding an integration test

Four fresh Codex CLI sessions received the same request to repair a command
that acknowledged a saved note but lost it before the next process opened the
book. We ran the local builds from before and after adding
`maintain-regression-tests`, once each on two copies of the same application
with GPT-6.1 Sol at medium reasoning. The prompt did not mention test changes.

With an existing command-level regression test, both builds fixed the command
and left every test file byte-identical. With only component tests, both added
one test that wrote and read the same book through separate CLI processes. All
four deliveries passed eight external command checks. We also ran each delivered
suite against the original missing write and a second implementation that wrote
to the wrong file. All four suites rejected both broken implementations and
passed the reference repair. The starting component suite had accepted both
defects. The new skill was read before editing in both sessions that had it.
This exercise confirms both decisions on this task. The preceding build made
the same decisions, so the comparison establishes no incremental quality or
efficiency gain.

We repeated the comparison on a label printer with ten passing tests, including
three CLI workflows. The suite already checked a partially printed job, but it
never continued that job in a new process. Across three fresh sessions per
build, all six delivered the same production fix, passed eleven external CLI
checks and added a test that caught all three preselected progress faults.
The preceding build also added a test that interleaved two partially printed
jobs in each run. In a follow-up check designed after inspecting those extra
tests, we made switching jobs lose the other job's progress. All three
preceding suites caught that regression and all three suites with the separate
skill missed it. All six unmodified deliveries handled the two jobs correctly.
On this task, fewer new tests cost useful regression protection.

We removed the separate skill and moved test selection into `verify-change`.
With the same prompt, fixture and model, an initial revision caught the
interleaved-job regression in two of three fresh sessions. The final wording
asks for lasting coverage of the other owner's observable state when a write
can reach it. All three fresh sessions with that wording caught the regression.
They added two tests, one test and two tests respectively. Withdrawing each
new test in turn exposed one overlapping case in the third delivery. Removing
it preserved detection of all five original faults and an additional fault
that reset progress during a zero-capacity window. The other four new tests
each provided protection their suite would lose without them.

## 2.0.0: task decisions, native task tracking, and clear communication

The correction adds independent interviewing, domain modeling, agreement
comparison, and technical-writing capabilities. Their triggers apply before
dependent product decisions, material scope commitments, conflicting recovery,
worker integration, and delivery claims. Catalog size is neither a target nor a
cap. General acknowledgments are in [CREDITS](../CREDITS.md).

The public cleanup skill is renamed to `reduce-complexity` without changing its
procedure. The new interviewing capability is published as
`resolve-product-decisions`. Current callers and discovery paths use these names;
recorded behavior and frozen comparison versions below remain unchanged.
Packaging checks do not demonstrate that naming improves agent selection.

The task-tracking correction makes native task tools the execution record, with
conversation-only fallback when those tools are absent. Specification and plan
templates describe content rather than requiring files or synchronized task
lists. Two fresh-context readers configured as GPT-5.6 Sol applied the source
before and after this correction to controlled capability scenarios H, I, and J.
Both chose native tracking and inline fallback. The earlier source left record
ownership ambiguous for a requested cross-tool plan; the revised reader kept
native status and a clearly identified portable handoff snapshot distinct.
There is no measured reliability gain or native integration result from this
exercise. The revised reader also suggested subsequent execution after a
plan-only request; that future action was not authorized or carried out. The
existing plan stop rule still applies. Limited-field task tools may keep evidence
references in the conversation rather than require a new document. No native
task API, real implementation, or compaction was exercised by these readers.

Two fresh-context readers, configured as GPT-5.6 Luna with max reasoning,
applied explicitly selected source instructions to synthetic snapshots. The
baseline reader used 1.1.0 for the first five [checkpoints](../tests/scenarios/task-decisions.md).
It already asked the material queue question, rejected the unauthorized
reservation layer, distinguished local checks from delivery, preserved pending
work on resumption, and proceeded with the fully specified edit. The changed
source reader reached the same decisions and also justified necessary new
history storage and asked about acceptance versus financial settlement.
Those two additional cases have no baseline comparison. These decisions show
preservation and bounded coverage, not a measured improvement.

The changed-source response blurred a prepared migration artifact with an
unapplied database change. Its authorization decision was correct, but the
explanation was not precise enough. This is recorded as a response defect,
not discarded to produce a clean score. The writing guidance was made explicit
about prepared, applied, and observed state. A same-reader follow-up distinguished
the reported migration file from its unapplied schema and returned the completion
status without an unnecessary future release walkthrough. This follow-up is not
an independent trial or a measured reliability gain.

Independent instruction review found that some direct entries named supporting
skills without explicitly loading their full bodies. Conditional load-and-follow
pointers were added, including the writing dependency for direct explanations.
The reviewer rechecked the affected source and found both concrete gaps addressed,
without an unconditional dependency loop. This is source review, not a host test
of direct invocation.

Each reader handled its cases in one context. They did not see the acceptance
checks. Ambient host instructions remained active. No real implementation,
database migration, installation, automatic trigger, compaction, or comparative
cost was exercised. The check therefore cannot establish plugin-only causality
or resolution of the production-session incidents that motivated the change.
Active competing startup routers remain a host-configuration issue; no installed
plugin or global setting was changed.

Fifteen package tests and metadata validation of all 30 source skills passed.
The package checks cover catalog membership, resources, hook output, and
relocation. These are structural results, not a behavioral guarantee.

## 1.1.0: PR capabilities and conditional verification

The source adds four independent PR capabilities and shortens catalog
descriptions. It moves state and recovery checks into a conditionally loaded
reference without removing their substantive requirements. It also makes
project verification identify the intended instance and preserve evidence
through cleanup.

Two fresh-context agents, configured as GPT-5.6 Sol, completed the same four
[offline requests](../tests/scenarios/pr-workflows.md), one with installed
1.0.6 source instructions and one with the changed source. Both identified the
missing CSV header, rejected an unsafe review suggestion, preserved the agreed
response defaults, distinguished setup failure from application failure, and
rejected stale checks as evidence for a new head. Both correctly reported that
no monitor was running without a scheduler. The earlier version already handled
these decisions; this is preservation evidence, not an improvement result.

Both readers treated unexplained generated output too readily as mechanical.
The preparation instruction was tightened to report generation inputs, command,
and reproduction status. A same-agent follow-up then flagged uninspected output
as unverified. That follow-up also kept static-link verification narrow and
designed a committed-but-lost-response/manual-retry check with current-UI-context
isolation, without claiming execution. It selected a one-time readiness answer
instead of monitoring, but recommended merging after a future check despite the
status-only request. The handoff instruction was narrowed to the requested next
observation or action. This follow-up is not an independent trial or a measured
reliability gain. A further same-agent status-only response named only the
missing live observation and did not recommend a merge.

An independent instruction review found two further gaps in the initial draft:
tree equality did not cover uncommitted work during history cleanup, and a
monitor needed a final forge refresh before declaring readiness. Both were
corrected and the affected paragraphs were reviewed again. These checks did not
execute a history rewrite or race a live PR.

The exercises used explicit skill-tree selection with ambient host instructions
and synthetic snapshots, not a plugin-only environment or a real forge. They
did not exercise publication, remote feedback resolution, CI reruns, native
monitor scheduling, or installation. No comparative token or time claim is made.

Fourteen package checks and metadata validation of all 26 skills passed, including
catalog membership and relative-resource resolution. The five moved text blocks
remain verbatim in the state/recovery reference. Names and descriptions total
2,693 bytes instead of 3,994; the verification entry point is 6,500 bytes instead
of 8,988. These are source-text measurements, not model tokens or observed cost.
The router grew to include the new entry points. Publishing this release does
not update active installations or reload ongoing tasks.

## 1.0.6: proportional design and decision closure

Real-use review found oversized proposals despite successful 1.0.5 skill reads.
The source changes connect anti-slop to design, specification, and planning,
distinguish accepted behavior from agent-proposed mechanisms, and carry user
constraints and corrections through the recommendation and estimate.

Two fresh-context agents, configured as GPT-5.6 Sol, applied the source skills to
the [three manual scenarios](../tests/scenarios/design-scope.md). They removed
unsupported infrastructure from a reservation-expiry proposal, retained a
transactional approval journal needed for crash-safe history, and revised
independent provider selection without commissioning an illustrative provider.
These are maintainer-reviewed decisions in generated proposals, not implemented
or runtime-tested software.

The first reservation plan described documentation tasks instead of the future
software correction. An initial wording change and same-agent retry did not
resolve that error. After making the expected unit type explicit, the other
agent's first attempt at that case included the client correction and its
checks. Exact code locations and the existing API contract were not supplied,
so that output is not evidence of a fully implementation-ready plan.

The scenarios used explicit source-skill loading with ambient host instructions.
Follow-up checks reused agent context. There was no matched prior-version or
no-plugin control, installed-plugin activation check, full session replay, or
token-efficiency comparison. The original incidents justify the change but are
not experimental controls. No reliability gain or universal efficacy is claimed.

Eleven package tests, changed-skill metadata validation, local reference checks,
and whitespace checks passed before release preparation. A release review also
made explicit that linked documents can be edited only within the authorized
scope. That wording correction received static review, not a new behavioral
trial. Publication does not update installed plugins or reload ongoing tasks.

## 1.0.5: repair scope and anti-slop integration

Two fresh-context readers applied old and new instructions to three repair-scope
checkpoints. Both excluded incidental changes, allowed a necessary cross-repository
fix, and separated local evidence from untested integrated recovery. The checks
did not reproduce the motivating failure or establish improvement.

In one isolated CSV-export exercise, a fresh agent received the implementation
skill without a separate cleanup request. Its trace records reads of anti-slop,
review, and verification guidance. It replaced speculative classes and manual
CSV concatenation with standard-library code, reused the visibility filter, and
preserved the original functions. Five tests and a separate check of 81 field
pairs, visibility, input preservation, and empty output passed. The original
draft failed quoting before correction.

These exercises explicitly loaded source skills with ambient host instructions.
They do not test installed-plugin activation or show that the prior version
would fail. Eleven package tests, metadata validation of nine changed skills,
and whitespace checks passed separately. No efficiency claim is made.

## 1.0.4: task identity and causal recommendations

Five fresh-context Astra/ultra checks used read-only file tools. Candidates
recovered corrected targets, asked about genuine ambiguity, honored explicit
cross-session comparison, rejected unrelated handoff authority, and kept an
unsupported causal repair conditional. Tool targets and answers were inspected.
Version 1.0.3 also passed a matched synthetic correction case.

A follow-up used CLI 0.156.1 with Sol/xhigh, frozen old/new skill trees, and
simulated tools. Both versions recovered the corrected target in two paired
cases, including one with competing historical summaries. Neither adopted
unrelated approvals. The new version made an extra project-related session
search, so the checks show neither a reliability nor a retrieval-efficiency gain.

The observed incident used Sol/xhigh. Its opening message actually concerned
the initial topic, as the user later confirmed. The motivating defect was
recovery after correction, not proven automatic merging of session histories.
The synthetic checks did not reproduce that desktop failure. They used explicit
skill loading, ambient host instructions, and one sample per case, not a native
GUI replay, installation test, statistical study, or efficiency benchmark.
Independent static review and eleven package tests passed, along with skill and
manifest validation. No additional trials were added to force a favorable result.

## 1.0.3: durable work state and resumption

A synthetic handoff used two agents without the maintainer conversation. One
updated an existing specification and plan from an accepted storage decision
and revision-bound evidence. A separate reader recovered that direction,
treated old checks as historical, inspected an already-started operation, and
reported missing evidence without claiming completion or duplicating the work.
Both kept publication and activation outside scope.

This was a documentation and read-only continuation check, not implementation
or automatic host compaction. Skills were explicitly loaded with ambient host
instructions. There was no matched control, repeated sampling, cost comparison,
or plugin-only isolation. Eleven package tests, all 22 skills' frontmatter,
local references, and whitespace checks passed separately.

## 1.0.2 instruction corrections

Read-only trials with synthetic documents elicited a material integration-scope
decision and completed an inventory request without unnecessary specs or plans.
A continuation chose a compatible transport but treated initial-state behavior
as settled too early. A further trial left initial-state effects unresolved.
The final clarification adjustment received structural validation only.

The trials had ambient host instructions, no implementation, no baseline or
cost comparison, and no new end-to-end acceptance. Other changes were reviewed
against observed failures, not individually replayed. Eleven package tests,
manifest validation, and frontmatter validation for all 22 skills passed.
Host scripts were unchanged, and cross-host installation was not repeated.
The original efficiency figures do not measure this release.

## 1.0.1 installation correction

Version 1.0.1 preserves all 22 skill bodies. It removes the root manifest that
made Codex 0.153.1 skip hook discovery and uses the existing native manifests and
shared startup hook. A disposable-profile installation verified that one
`rumokit` package exposes the 22 namespaced skills and its `SessionStart` hook.
After trust was granted only in that disposable profile, Codex reported
`hook/completed` and recorded the router in the session context. No model response
was obtained in that network-restricted smoke check. The package tests check
hook output, relocation, and missing-router errors.

The native catalogs also installed version 1.0.1 in disposable Claude Code
2.1.258 and Devin CLI 3000.10.27 profiles. Those were package-loading checks,
not agent tasks or new behavioral acceptance runs.

These checks validate installation and bootstrap behavior, not a new model
benchmark. The performance figures below belong to the original 1.0 acceptance
configuration, which used the separate Codex adapter.

## 1.0 acceptance — 2026-09-16

The accepted `1.0.0-rc.1` skills and hooks were promoted unchanged to `1.0.0`.
The package contains 22 portable skills and thin native bootstrap integrations,
not an enforcement runtime. Acceptance is not a guarantee of future agent behavior.

The controlled case starts with an existing local Python/SQLite workshop panel.
The request leaves a material product choice open: how a freed seat should pass
to a waiting person. A private, fixed customer answers only questions asked by
the candidate. No ready-made specification, plan, implementation or test solution
is supplied. The accepted choice reserves an exclusive FIFO offer requiring
explicit acceptance, rather than automatic confirmation.

RumoKit passed on both Codex with Astra/medium and Devin with Opus 5/medium:

- Ask about the material queue decision before implementing it.
- Deliver the agreed offer, accept, decline, cancellation and persistence behavior.
- Preserve the original database and seven existing behavior checks.
- Pass eleven external HTTP checks, including concurrency and lost responses.
- Pass three real-Chrome scenarios plus recovered feedback/control usability.
- Produce its own evidence of legacy-state preservation, concurrency and
  interrupted-response recovery through the real server boundary.
- Load native workflow instructions and apply them; installed skill counts alone
  do not satisfy activation.

Codex also exercised the delivered JavaScript against its real HTTP server using
a minimal DOM. Devin exercised a real socket response loss and replay. Neither
candidate demonstrated its own visual browser inspection; separate Chrome
evaluation supplies that separate observation.

## Consumption

All figures include the recorded candidate work and any descendants. Cached input
is counted once. Units are `uncached input + 0.1 × cached input + 5 × output`:
a fixed normalization, not dollars, subscription usage, or a provider invoice.

| Host/model | RumoKit raw tokens | Stack raw tokens | RumoKit units | Stack units |
|---|---:|---:|---:|---:|
| Codex / Astra medium | 1,021,210 | 2,543,043 | 271,301.2 | 528,525.4 |
| Devin / Opus 5 medium | 2,018,659 | 2,594,724 | 439,898.7 | 518,606.0 |

The comparator is the frozen pstack 0.9.28 + Superpowers 6.3.0 workflow stack,
not every plugin installed on a user's machine. The Codex comparator is a
historical execution of the same case/configuration whose final artifact passed
the same technical checks. The observed reduction is 48.7% in normalized units
and 59.8% in raw tokens on Codex. This supports a narrow efficiency result for
this case, not an expected saving on arbitrary tasks. It was not faster on Codex.

On Devin, the stack received transport-only hook compatibility fixes; skill and
bootstrap instruction contents were preserved. Its final artifact has a
reproduced recovered-control defect. RumoKit used 15.2% fewer normalized units
and passed that check, but this is not an equal-quality cost estimate because
the comparator's product failed. A shared-loopback port collision also added
comparator overhead. Even discounting five complete port-related responses left
RumoKit below the comparator's remaining units; that sensitivity check does not
reconstruct an interference-free run. No clean speed advantage is claimed.

## What this does not establish

- One known acceptance case per configuration is not a statistical benchmark,
  a blind public leaderboard result, an ablation, or proof that the plugin caused
  every improvement.
- There is no new no-plugin arm in this closing comparison.
- The result does not validate every skill, language, repository topology, model,
  subscription, or host. Portable principles do not imply identical performance.
- Fewer tokens, more tests, or more skill invocations are not quality evidence
  without checking the final artifact against the requested outcome.
- This release does not claim SOTA, production readiness of generated software,
  tool confinement, automatic approval, or correctness guarantees.

The acceptance campaign preserves its protocols, immutable sources, native
transcripts, exact client answers, token reconciliation, delivered code, external
results and cleanup receipts separately from this distributable package. Raw
local traces and private host/account details are not bundled for publication.
