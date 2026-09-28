---
name: finish-change
description: Use when assessing delivery readiness or handing off a change with its remaining gates.
---

# Finish a Change

Reconcile the final artifact, evidence, and authority into a bounded next-step decision.

## Inspect the current state

Confirm repository and revision identity, working-tree changes, intended scope, dependent components, generated artifacts, tests and checks, review findings, CI state when available, and unresolved approvals. Refresh material evidence after the last mutation.

For multi-repository work, derive the final changed-component inventory from repository diffs against the starting revisions and staged, unstaged, and untracked state across the worktrees used. Reconcile it with the handoff, including configuration and deployment repositories. Do not count from memory or label pre-existing user changes as this task's work.

Use `coordinate-change` when readiness depends on multiple repositories, versions, or release edges. Do not infer that a green local check proves a remote, deployed, or production state.

## Resolve contradictions

Compare the final artifact with the accepted user outcome, examples, and preservation obligations, not only the latest plan or specification. State what was expected, what is integrated, and what is actually evidenced. Worker-only output and documented but absent capabilities remain unfinished. Surface unplanned changes, stale results, skipped boundaries, open findings, and claims that exceed the evidence. Confirm that no recommendation, rollout gate, or next artifact still depends on a superseded direction. Do not hide blockers in a general success summary.

For a durable handoff, follow [the durable work-state contract](../resume-work/references/work-state.md) and use [assets/change-handoff.md](assets/change-handoff.md) as needed. Update the existing entry point with final progress and the next action; do not leave a competing current summary behind. A separate handoff file is unnecessary when the existing task document already provides it.

## Give the next-step decision

Choose one:

- `READY_FOR_NEXT_STEP`: the named next action is supported within scope;
- `NOT_READY`: a concrete blocker prevents that action;
- `INCONCLUSIVE`: required state or evidence cannot be established.

State the next observation or action within the requested stopping point and who or what owns it. A status-only answer may be complete without another action; missing evidence calls for the missing observation, not an instruction to merge or deploy afterward. Do not merge, deploy, publish, delete, or approve on the user's behalf without authority.
