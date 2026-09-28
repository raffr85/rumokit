---
name: remove-slop
description: Use when checking or removing unnecessary complexity in code, designs, plans, or prose.
---

# Remove Slop

Remove unnecessary complexity while preserving the accepted contract. Support the current owner within the affected artifact and its existing authority, before proposed mechanisms become requirements or implementation. A direct cleanup request owns its stated artifact. Neither mode requires a router, spec, plan, or reviewer panel. For a read-only review, return findings without modifying anything.

## Establish what must survive

Inspect the artifact, its decision sources, and enough surrounding context to identify its purpose and local conventions. Preserve accepted outcomes, existing behavior, public interfaces, facts, qualifications, obligations, and the author's voice. Distinguish these from mechanisms introduced by the agent in a draft. If removing a mechanism would change accepted behavior, surface that choice through the owner and `clarify-intent`; do not silently narrow the result.

## Remove with a reason

Look for concrete noise, not stylistic tells alone:

- proposed infrastructure or states without a required guarantee or concrete failure mode that existing capabilities cannot handle;
- reimplementations of existing helpers, standard-library or platform capabilities, and dependencies added without a needed capability;
- speculative options, forwarding layers, or abstractions without a current consumer or requirement;
- redundant checks, catch blocks, type-system bypasses, or nested branches where a simpler equivalent preserves the observed contract;
- comments narrating syntax, repeated explanations, generic filler, and prose that inflates certainty.

Check callers and data boundaries before removing defensive behavior. Preserve trust-boundary validation, data-loss prevention, security, accessibility, compatibility, required tests, and useful domain explanations. A single caller or unfamiliar pattern alone does not prove an abstraction unnecessary. Do not trade readability or required behavior for fewer lines, or remove uncertainty to make prose sound stronger.

Consolidate repeated normative rules at their existing owning definition and update dependent references. Preserve useful local summaries and all distinct obligations. Make the smallest coherent edits. If simplification requires a broader structural change or different behavior, return that decision to the relevant owner within existing authorization.

## Check preservation and stop

Compare before and after against the preserved contract. For code or executable configuration, use `verify-change` with the affected public behavior and current evidence. For prose, check that facts, meaning, caveats, and required content survived; shorter is not inherently better.

Return material cleanup or supported findings and any preservation gap to the current owner. If the artifact is already appropriate, leave it alone. Recheck only changed content or affected assumptions; the owner's response-relevance pass remains separate.
