---
name: locate-change
description: Use when the user asks which repository, layer, module, symbol, or consumers should own a proposed behavior or fix.
---

# Locate a Change

Return an evidence-backed placement map. This is a read-only result, not authorization to design, plan, or implement the change. A direct invocation needs no router or lifecycle first.

## Follow ownership

Start from the proposed behavior and the nearest real entry point, caller, or observable symptom. Search names to find candidates, then trace enough code to establish which boundary owns the decision, state, and side effect. A matching filename is a lead, not proof of ownership.

Identify the smallest coherent change surface:

- the repository, file, and symbol owning the behavior;
- callers or consumers that must move with a changed contract;
- the nearest existing test or observable boundary;
- relevant generated sources, shared packages, or versioned edges.

Separate the primary owner, required companions, and merely related code. Do not place domain behavior in an adapter just because that is where the request enters. Prefer existing ownership unless evidence shows why it cannot support the requested behavior.

## Resolve only placement uncertainty

Inspect discoverable facts yourself. When two placements encode materially different product behavior, state the fork and use `clarify-intent` for that choice. If the desired behavior is already clear, do not invent a product interview. Add `coordinate-change` only when an unresolved version or integration edge affects placement.

If evidence is insufficient, provide the candidates and the exact missing fact instead of an invented definitive location. Do not expand a local search into a whole-system tour.

## Return the map

Lead with where the change belongs and why. Include direct source pointers, required companion changes, the verification entry point, and material uncertainty. Stop there unless the user also requested explanation, planning, or implementation.
