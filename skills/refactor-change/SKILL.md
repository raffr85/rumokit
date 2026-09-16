---
name: refactor-change
description: Use when the requested result is a structural code change that should preserve externally relevant behavior while improving ownership, readability, maintainability, or internal design.
---

# Refactor a Change

Improve structure under an explicit preservation contract.

## Define what must not change

Identify callers, public and internal contracts, state transitions, side effects, error behavior, performance-sensitive paths, generated boundaries, and user-visible behavior relevant to the refactor. Inspect current evidence before editing.

Use characterization or differential checks when the behavior is poorly specified. The goal is discriminating preservation evidence, not maximum test count.

## Move in reversible units

- Prefer deletion, directness, and clearer ownership over new abstraction.
- Keep each step behavior-preserving and reviewable.
- Migrate concrete callers before removing a legacy API.
- Avoid mixing unrelated feature changes or formatting churn into the refactor.
- Re-evaluate whether the abstraction reduces reader load at real call sites.

Add `assess-blast-radius` for shared contracts and `coordinate-change` for independently versioned consumers.

## Verify preservation

Apply `verify-change` to the preservation contract, using equivalence, characterization, integration, build, static, or real-surface evidence as appropriate. Include representative edge and failure behavior when material. Use `finish-change` for a multi-component handoff or release-readiness claim. Neither composition requires a new phase, agent, or approval.

Return the structural change, preservation contract, migrated consumers, evidence, and any behavior that could not be proven equivalent. Do not call an intentional behavior change a refactor.
