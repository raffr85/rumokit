---
name: design-change
description: Use when the requested result is a technical design, architecture choice, interface shape, or migration approach rather than implementation code.
---

# Design a Change

Select a design that fits the system actually present.

## Establish the design boundary

Establish or reuse the accepted outcome through `clarify-intent`, including direct invocation. Inspect current ownership, data flow, contracts, callers, constraints, and failure behavior. Carry forward the user's example and preservation obligations; separate settled requirements from facts to discover and choices still open.

Decide technical alternatives within delegated criteria without asking the user to repeat authorization. The design must satisfy the accepted outcome, not substitute a smaller one that is easier to build.

If a design choice changes who receives an effect, when it takes effect, or how existing state is processed, establish its authority through `clarify-intent` before treating it as settled. Mark unaccepted proposals as proposals; agreement on capabilities does not settle every behavior within them.

Describe the domain and state transitions before choosing modules or abstractions. Add `assess-blast-radius` for shared boundaries and `coordinate-change` for independently versioned components.

## Compare credible options

Develop only options that could reasonably be shipped. Compare them on:

- fit with existing ownership and conventions;
- correctness and failure modes;
- migration and compatibility risk;
- operational and security consequences;
- reversibility and evidence needed to validate them;
- reader and maintainer load.

Prefer removing or reusing structure before adding a new layer. Use `prototype-decision` only when a focused artifact can distinguish the options.

## Produce the selected design

Record:

- objective and non-goals;
- current-system evidence;
- selected ownership, data shape, interfaces, and state transitions;
- rejected alternatives and why;
- compatibility, failure, rollout, and rollback boundaries;
- open decisions and how they can be resolved;
- evidence that implementation must later produce.

Stop at a decision-ready design unless the user also requested a specification, plan, or implementation.
