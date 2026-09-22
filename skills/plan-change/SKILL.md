---
name: plan-change
description: Use when the requested result needs an ordered implementation plan because the change has multiple dependent units, meaningful risk, cross-component sequencing, or a handoff boundary.
---

# Plan a Change

Turn accepted behavior and design into the smallest sequence of verifiable implementation units. Do not create a plan as ceremony for a trivial edit.

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
- the implementation move;
- the task-shaped evidence that completes it.

Order units so the system remains understandable and, where practical, usable between them. Parallelize only units with independent inputs, outputs, and writable state. Test-first is useful when a fail-before check is cheap and discriminating; it is not a universal phase.

Use [assets/implementation-plan.md](assets/implementation-plan.md) as a compact starting point.

## Finish at implementation readiness

Check that the plan covers the requested result, preservation obligations, integration edges, and final evidence without speculative future infrastructure. Distinguish executable units from conditional ones; coverage counts do not establish readiness. Stop at the plan unless implementation is also authorized.
