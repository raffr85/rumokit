---
name: verify-change
description: Use when choosing checks or assessing whether current evidence supports a claimed result.
---

# Verify a Change

Evaluate the claim against the resulting artifact. As a supporting skill, return evidence and gaps to the implementation, debugging, or refactoring owner without changing its authority or stopping point. When verification itself is the requested result, remain read-only unless fixes are also authorized.

## Bind the claim to the expected outcome

Recover the requested outcome, accepted decisions, representative example, preservation obligations, and stopping point from the conversation or existing task artifacts. An agent-authored spec or test is not an independent source of user intent. If a material expectation was never settled, identify that gap and use `clarify-intent` before claiming agreement; do not validate the assumption by repeating it in the report.

Name the exact claim, acceptance boundary, final artifact identity, revision or state, and material consumers. Distinguish integrated output from a worker's branch or worktree. A claim about the wrong revision or a pre-mutation result is not current evidence.

Determine the impact surface before choosing checks. Add `assess-blast-radius` or `coordinate-change` when the claim spans shared or versioned boundaries.

## Build a task-shaped evidence portfolio

Choose independent observations appropriate to the claim:

- examples derived from requirements rather than copied from the implementation;
- focused automated tests or reproduction steps;
- compile, type, lint, or static checks;
- real command, runtime, UI, API, or integration behavior;
- negative, failure, and preservation cases where material.

For migration or backward-compatibility claims, confirm that the disposable fixture represents the prior schema, data, or caller contract before running the change. Check both preservation and the new behavior against that starting state. A fixture already updated by the candidate does not prove the transition.

Select representative operations by their identity, commitment, and duplicate-prevention guarantees, not just a shared interface or transport. Exercise them through the nearest authoritative boundary and compare expected effects, actual effects, and preserved behavior. Include the consequential failure or intervening change established during clarification when relevant. This may be one command, API call, rendered flow, or integrated scenario, not necessarily a new test suite.

When correctness depends on state transitions, time, retries, interacting rules, asynchronous work, or a changing UI context, load [state and recovery checks](references/state-and-recovery.md) before selecting the checks. That reference covers invariants, authoritative effects, consumer consistency, and recovery. Apply only the parts relevant to the claim; a static change does not require a concurrency scenario.

Use an existing test, a small direct probe, or a property/stateful test when its generated cases earn their cost. This does not require a testing framework, a separate reviewer, or a fixed test count.

For a resource-use claim or a material change to a cost-sensitive path, measure the resulting program on a representative workload while checking equivalent output. Compare with the starting implementation or another relevant baseline when usable; report the workload, environment, time and relevant resource use separately from the agent's own execution cost. Do not turn an unrequested optimization into a new acceptance requirement.

Ask what plausible incorrect behavior a passing check would reject. If the check cannot distinguish it, strengthen the observation rather than count another pass. For a known defect, failing-before/passing-after evidence is useful when feasible. A green check sharing the implementation's mistaken assumption is weak evidence. An absent, documented-only, or unintegrated capability remains a gap regardless of passing tests elsewhere.

Separate process success from execution of the claimed behavior. When a runner can skip the relevant tests or exit early, inspect the execution output or entrypoint to establish whether those tests ran. An exit-zero command with no execution of the target is `NOT_RUN` for that target, not `PASSED`; report deliberate skips and their reasons. Compilation-only checks support compilation claims, not behavioral claims.

## Resolve shared prerequisites once

Before a costly family of checks, probe shared execution prerequisites once: declared and active runtime versions, required services, workspace mode, listeners, generated state, and caches when relevant. Record the observed state with the current evidence; no separate ledger is required.

After classifying a capability as unavailable, do not retry the same boundary until a relevant environment, artifact, input, or configuration change could alter the result. Use an independent reachable boundary or issue `INCONCLUSIVE`; repeated failure is not stronger evidence.

When comparing candidates, establish the minimum outcome contract before comparing cost, time, tokens, or correction count. A smaller or incomplete result may be cheaper, but it has not demonstrated greater efficiency for the same task.

Report every named target separately as `PASSED`, `FAILED`, `BLOCKED`, or `NOT_RUN`, with the exact command or boundary and reason. A passing subtarget inside a failing or blocked aggregate command does not make the command or suite pass. `BLOCKED` is neither `FAILED` nor `PASSED`.

## Issue a bounded verdict

Report at the scale of the claim. An inline summary is enough when no durable report is needed; otherwise use [assets/evidence-report.md](assets/evidence-report.md). Choose one:

- `SUPPORTED`: current evidence supports the exact claim within the named scope;
- `NOT_SUPPORTED`: observed evidence contradicts the claim;
- `INCONCLUSIVE`: evidence is missing, stale, ambiguous, or cannot reach the needed boundary;
- `NOT_APPLICABLE`: the proposed check does not address this claim.

Separate outcome fit, technical correctness, and unverified scope. List failures and gaps before a verdict, mapping each material expectation to the observed result and its evidence. Reuse fresh observations against unchanged artifacts and environments; do not rerun checks for the wording of a final claim. Never translate advisory evidence into enforcement, confinement, universal correctness, or production proof.
