# Implementation plan

## Outcome and starting evidence

State the requested result, accepted behavior and example with their source, current revision or state, and decisive constraints. Reuse an existing agreement or specification rather than duplicating it.

Identify the task entry point and when this plan was reconciled. Link the current behavioral contract and decisions. Keep superseded directions in clearly marked history, not in the current work summary.

Identify whether this is an executable implementation plan or a conditional discovery/impact map. Name material open decisions and their dependent units; do not bury unresolved behavior in a generic first unit.

## Verifiable units

For each unit:

1. **Result:** behavior or contract completed.
2. **Scope:** exact files, symbols, components, or a marked discovery task.
3. **Dependencies:** prerequisites and compatibility boundary.
4. **Change:** focused implementation action, reused capability, and the requirement or concrete failure that justifies a new mechanism.
5. **Completion check:** observation that would prove this unit on the resulting artifact.
6. **Status and observed evidence:** pending, in progress, blocked, or complete; actual result and artifact revision/state when checked. Separate local verification from publication and activation. Use the project's equivalent status names if they already exist.

Use stable unit identifiers when dependencies or evidence refer to them. Keep optional improvements outside required units, dependencies, and estimates.

## Continuation state

State the current unit and next authorized action, with links to completed evidence. Record material blockers and their owners, pending decisions, relevant uncommitted work, and running operations or workers when present. If another task document already owns this state, link it rather than maintaining a second copy. Update at material transitions, not after every tool call.

## Integration and release order

Include only when components or revisions must move in a particular order.

## Final evidence and stop point

Define the integrated checks, preserved behavior, unresolved approvals, and the exact point at which implementation returns to the user.
