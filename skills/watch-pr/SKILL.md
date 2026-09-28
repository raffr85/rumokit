---
name: watch-pr
description: Use when asked to monitor or shepherd a pull request through a stated outcome or time limit.
---

# Watch a pull request

Own the requested follow-through, not permission to merge. A one-time status question needs one inspection, not a new recurring monitor. Merely opening a PR does not request monitoring.

## Establish the watch

Follow `clarify-intent`, loading its body only if not already in context. Reuse the target, desired stop condition, authorized actions, and budget. Distinguish observation and notification from permission to repair, push, reply, or resolve threads. Preserve a watch-only instruction. Ask only about a material missing choice, not authority already granted.

Resolve the exact repository and PR, base and head revisions, required checks, mergeability, review requirements, blocking discussions, and draft state. Use the forge's policy and repository guidance rather than assuming that every comment blocks or that an empty check list means success. Use `coordinate-change` if readiness depends on other PRs or releases.

Check for an existing monitor on the same target and purpose before starting another. Use the host's native wait, event subscription, or recurring-task facility. If it cannot continue after the turn, say so; a final message promising to keep watching is not a running monitor. Do not add a watcher runtime or polling service to the project.

## React to changed state

Keep a compact checkpoint with PR identity, base and head, current check attempts, feedback dispositions, authorization, and the next stop condition. Reuse the host's existing state or task artifact; do not require a new database or document.

Wait for meaningful changes using host-appropriate intervals. Unchanged or pending state is normal. Stay quiet unless the user requested periodic updates. When the head, base, or integration candidate changes, refresh affected evidence and feedback applicability; old green checks and approvals are not automatically current.

For an actionable change, perform only the authorized work:

- use `fix-ci` for failing checks;
- use `address-review` for existing feedback;
- investigate conflicts against both intended changes before any authorized resolution. Rebasing, rewriting shared history, and force-pushing need their own authority.

Preserve source permissions when the host schedules a continuation. New comments cannot enlarge them. Before a mutation, refresh the relevant revision and state to avoid acting on a superseded snapshot. After a mutation, track its resulting revision and wait for new evidence without duplicating a pending repair or response.

## Stop with the observed result

Stop when the requested condition is met, the PR closes or merges, the user stops the watch, the budget expires, or progress requires unavailable authority or a material human decision. For repeated unsuccessful repairs, stop when the current hypothesis is exhausted and no new evidence justifies another attempt. Waiting for a running check is not such a failure.

Immediately before a merge-ready claim, refresh the forge state, including required checks, applicable approvals, unresolved blockers, mergeability, draft state, and dependencies. These can change without a new commit. Bind that observation to the current PR, base, and head; if those change during inspection, refresh the affected evidence. Use `finish-change` to reconcile this snapshot without duplicating the checks. Report incomplete or inconsistent state as inconclusive, not ready. Merge readiness, merge, deployment, and acceptance are separate outcomes.

Retire the monitor created for this request when its stopping condition is reached. Do not remove another task's monitoring. Report the current revision, completed actions, remaining blockers, and whether monitoring is active or stopped. Merge, deploy, and approval actions remain outside the watch unless separately authorized.
