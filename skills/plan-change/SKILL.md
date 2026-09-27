---
name: plan-change
description: Use when the requested result needs an ordered implementation plan because the change has multiple dependent units, meaningful risk, cross-component sequencing, or a handoff boundary.
---

# Plan a Change

Turn accepted behavior and design into the smallest sequence of verifiable implementation units. For a software change, the units describe future code, configuration, data, or operational changes and their checks. Delivering the plan as documentation does not turn those units into tasks for writing documentation or authorize executing them. Do not create a plan as ceremony for a trivial edit.

A specification does not automatically require a plan or a separate approval turn. Plan only when the current request includes it or the implementation genuinely needs durable sequencing. Honor an approval gate when the user explicitly set one or a material decision remains unresolved.

## Reconcile the starting point

Establish or reuse the outcome through `clarify-intent`, including direct invocation. Verify the current code, accepted decisions and examples, relevant specification, and existing work. A plan inherits that acceptance boundary; it does not silently defer required capabilities. Name exact files, symbols, contracts, or repositories when known; mark unresolved locations instead of inventing them.

Before sequencing dependent implementation, resolve choices that change what it must do. If behavior across components, authority, or recovery needs a durable shared contract, use `specify-change`; file count alone does not require it. Do not move foundational intent into a generic first unit and call the remaining sequence executable. A requested discovery plan or conditional impact map may legitimately leave these choices open: label it accordingly and identify which units depend on them. Continue independent mapping while awaiting answers.

Add `assess-blast-radius` before sequencing shared contracts. Add `coordinate-change` when multiple independently versioned components participate.

## Sequence by evidence and dependency

Each unit should state:

- the behavior or contract it changes;
- its concrete scope and exclusions;
- dependencies and compatibility requirements;
- the implementation move, what it reuses, and the requirement or concrete failure that makes any new mechanism necessary;
- the task-shaped evidence that completes it;
- its current status and any evidence already obtained, bound to the artifact checked.

Order units so the system remains understandable and, where practical, usable between them. Parallelize only units with independent inputs, outputs, and writable state. Test-first is useful when a fail-before check is cheap and discriminating; it is not a universal phase.

Use [assets/implementation-plan.md](assets/implementation-plan.md) as a compact starting point. Follow [the durable work-state contract](../resume-work/references/work-state.md) so a new session can locate the accepted contract, distinguish planned checks from completed evidence, and identify the next authorized unit. Extend the existing task entry point instead of creating another status document.

## Finish at implementation readiness

Apply `remove-slop` to the plan before handoff, reusing an equivalent check of unchanged content. Cover the requested result, preservation obligations, integration edges, and final evidence without speculative future infrastructure. Keep optional improvements outside required units, dependencies, and estimates. Distinguish executable units from conditional ones; coverage counts do not establish readiness.

Reconcile the current summary, estimates, and next action with changed or completed units. Explain what will change, in which components, why, what is preserved, and how completion will be checked in the response. Stop at the plan unless implementation is also authorized.
