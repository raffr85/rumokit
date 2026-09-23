---
name: delegate-work
description: Use when a bounded work unit benefits from independent, parallel, or specialist execution enough to justify briefing and integration.
---

# Delegate Work

Partition work without transferring ownership of the user's result.

## Test separability first

Before allocating workers, apply [references/model-policy.md](references/model-policy.md) to existing user preferences, project or host policy, and available capabilities. Respect an inline-only instruction; multiple repositories alone do not authorize or require delegation.

Delegate a unit only when it has bounded inputs, a concrete output, isolated writable state or read-only scope, and evidence the owner can inspect. Keep work inline when it is small, tightly coupled, sequential, or cheaper to complete than to explain and integrate.

Do not create workers merely to generate opinions, repeat the same analysis, or satisfy a fixed fan-out count.

Before each initial or follow-up unit, name the unresolved gap and what result could change the owner's conclusion or artifact. Do not dispatch repeated work over equivalent inputs, retry a known unavailable prerequisite without a relevant state change, or start another wave when the owner can already decide. This is a marginal-value test, not a fixed limit on workers or depth.

## Write a bounded brief

Give each worker:

- accepted outcome, why it matters, and the worker's contribution;
- authoritative inputs and current revision;
- authorized operation (investigate, implement, or review), owned scope, preservation obligations, and explicit exclusions;
- representative acceptance example and any still-open material decisions;
- expected artifact or findings;
- required evidence and stopping condition;
- shared-state and communication rules.

Pass the task-relevant context and precise evidence locations. Inherit full history only when the unit needs it; a small review should not restart the whole investigation. Workers may inspect additional evidence to resolve their assigned gap, but return unrelated findings to the owner instead of expanding the assignment.

Use isolated branches, worktrees, files, or read-only tasks when concurrent writes could collide. Never let multiple workers silently edit the same state.

## Integrate as the owner

Inspect outputs and evidence against the accepted outcome, not just the worker's local completion criteria. Select worker changes for integration by their necessity to that outcome and its preservation checks; keep incidental findings separate instead of converting every valid finding into another implementation unit. Workers return newly exposed product choices to the owner; they do not independently narrow the result. The owner resolves choices needed for the current result through `clarify-intent`, rather than merely collecting pending decisions. Resolve contradictions from source evidence; agreement or voting is not proof. The primary owner remains responsible for integration, cross-unit behavior, final edits, and the final claim. Unintegrated worker output is not the delivered artifact.

Keep requested configuration separate from host-attested execution identity when reporting worker results. For cost comparisons, include workers and integration for the same work unit, preserving the host's distinct token and cache counters; report missing accounting rather than treating it as zero.
