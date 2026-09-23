---
name: remove-slop
description: Use when implementation or review needs a final check for unnecessary complexity in the changed artifact, or the user requests cleanup of code, documentation, or prose while preserving behavior and meaning.
---

# Remove Slop

Remove unnecessary complexity without changing the contract. During implementation or review, support that owner within the current diff and its existing authority. A direct cleanup request owns its stated artifact. Neither mode requires a router, spec, plan, or reviewer panel. For a read-only review, return findings without modifying anything.

## Establish what must survive

Inspect the artifact and enough surrounding context to identify its purpose and local conventions. Preserve behavior, public interfaces, facts, qualifications, obligations, and the author's voice. An explicit cleanup request can supply the scope immediately; use `clarify-intent` only if the proposed cleanup opens a material choice about meaning or behavior.

## Remove with a reason

Look for concrete noise, not stylistic tells alone:

- reimplementations of existing helpers, standard-library or platform capabilities, and dependencies added without a needed capability;
- speculative options, forwarding layers, or abstractions without a current consumer or requirement;
- redundant checks, catch blocks, type-system bypasses, or nested branches where a simpler equivalent preserves the observed contract;
- comments narrating syntax, repeated explanations, generic filler, and prose that inflates certainty.

Check callers and data boundaries before removing defensive behavior. Preserve trust-boundary validation, data-loss prevention, security, accessibility, compatibility, required tests, and useful domain explanations. A single caller or unfamiliar pattern alone does not prove an abstraction unnecessary. Do not trade readability or required behavior for fewer lines, or remove uncertainty to make prose sound stronger.

Make the smallest coherent edits. If simplification requires a broader structural change or different behavior, surface that separately; use `refactor-change` or the relevant change owner only within existing authorization. Do not smuggle a redesign into cleanup.

## Check preservation and stop

Compare before and after against the preserved contract. For code or executable configuration, use `verify-change` with the affected public behavior and current evidence. For prose, check that facts, meaning, caveats, and required content survived; shorter is not inherently better.

Return material cleanup or supported findings and any preservation gap to the current owner. If the diff is already appropriate, leave it alone. Check the changed artifact once, not every progress message; the owner's response-relevance pass remains separate.
