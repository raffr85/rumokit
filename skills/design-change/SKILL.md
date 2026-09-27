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

Start with the existing path and the smallest change that could satisfy the accepted outcome. For a material new service, persistent state, abstraction, or operational dependency, identify the required outcome, guarantee, or concrete failure mode it addresses and why reuse is insufficient. A credible failure mode can justify prevention before an incident occurs; a generic appeal to robustness cannot justify unrelated infrastructure.

Compare viable options against correctness, security, compatibility, reversibility, maintenance effort, and the team's stated delivery and operating constraints. Separate necessary changes from optional improvements. Simplicity cannot justify dropping required behavior or protection. Use `prototype-decision` only when a focused artifact can distinguish the options.

Apply `remove-slop` to the proposed design before carrying its mechanisms into a specification or plan. Reuse an equivalent check of the same proposal; do not add a separate stage, document, or reviewer.

## Produce the selected design

Explain the selected solution in the response: what changes, where, why it is needed, and what remains unchanged. Supporting documents do not replace that explanation. Record the relevant detail:

- objective and non-goals;
- current-system evidence;
- selected ownership, data shape, interfaces, and state transitions;
- rejected alternatives and why;
- compatibility, failure, rollout, and rollback boundaries;
- open decisions and how they can be resolved;
- evidence that implementation must later produce.

Stop at a decision-ready design unless the user also requested a specification, plan, or implementation.
