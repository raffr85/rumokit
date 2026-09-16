---
name: remove-slop
description: Use when the user asks to remove AI slop, redundant scaffolding, noisy comments, repetition, or generic filler from existing code, documentation, or prose while preserving its intended behavior or meaning.
---

# Remove Slop

Clean the requested artifact without changing its contract. A direct invocation needs no router, spec, plan, or reviewer panel. If the user requested an audit rather than edits, return findings without modifying it.

## Establish what must survive

Inspect the artifact and enough surrounding context to identify its purpose and local conventions. Preserve behavior, public interfaces, facts, qualifications, obligations, and the author's voice. An explicit cleanup request can supply the scope immediately; use `clarify-intent` only if the proposed cleanup opens a material choice about meaning or behavior.

## Remove with a reason

Look for concrete noise, not stylistic tells alone:

- prose that repeats a conclusion, inflates certainty, or adds generic filler without information;
- comments that narrate obvious syntax rather than explain a non-obvious constraint;
- redundant wrappers, checks, abstractions, or branches whose lack of purpose is supported by callers, invariants, or tests;
- duplicated explanations that can be consolidated without losing distinct conditions.

Keep useful edge cases, domain language, compatibility boundaries, and necessary defensive behavior. Unfamiliar code is not automatically slop. Preserve uncertainty when its removal would make a stronger unsupported claim.

Make the smallest coherent edits. If simplification requires a broader structural change or different behavior, surface that separately; use `refactor-change` or the relevant change owner only within existing authorization. Do not smuggle a redesign into cleanup.

## Check preservation and stop

Compare before and after against the preserved contract. For code or executable configuration, use `verify-change` with the affected public behavior and current evidence. For prose, check that facts, meaning, caveats, and required content survived; shorter is not inherently better.

Return the material cleanup and any deliberately retained complexity or verification gap. Do not invoke this skill for every generated response: the owner's short relevance pass remains sufficient unless artifact cleanup itself is requested.
