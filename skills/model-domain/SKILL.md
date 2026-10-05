---
name: model-domain
description: Use when domain terms, states, invariants, or authority boundaries are ambiguous or changing.
---

# Model the Domain

Make the domain precise enough to discuss, implement, and test. Support clarification or design without selecting an unaccepted business policy or prescribing storage.

## Model behavior before mechanisms

Read the project's relevant language and actual callers. Identify the actors, things they act on, states, transitions, authoritative effects, and obligations that matter to this task. Use the project's canonical terms; distinguish concepts that share a name but have different effects or owners.

For each disputed term or transition, give a concrete example and a counterexample. Cross-check the description against code and the accepted operation. Explain a mismatch rather than deciding that either existing code or the agent's proposed model is automatically correct. Investigate technical facts yourself. When the requested result requires resolving intended behavior, load and follow [resolve-product-decisions](../resolve-product-decisions/SKILL.md); otherwise report that open choice without expanding a read-only modeling request. Reuse the existing model until a human answer or new evidence changes it rather than restarting the same ambiguity.

For stateful work, trace who can commit an effect, when it becomes authoritative, what survives failure, and what a retry may repeat. Separate availability, admission, reservation, acceptance, and settlement when the actual domain makes those distinctions. Do not invent these states merely to fill a model.

## Keep the model usable

Return the relevant terms, transitions, ownership, preservation obligations, and open disagreements. A short example or table can suffice. Check whether the model distinguishes a correct result from a plausible wrong one; matching names alone does not establish correctness.

Reuse an existing glossary, specification, or decision record when durable knowledge is needed and maintenance is authorized. Keep vocabulary distinct from implementation decisions and record a difficult-to-reverse tradeoff with its rationale. Do not create a glossary or ADR for every task, or erase useful domain distinctions to shorten the output.

Return control to the current owner. For a user-facing model, load and follow [write-clearly](../write-clearly/SKILL.md), reusing its full body when already loaded. A domain model does not authorize a new service, table, business policy, or deployment. Choosing those mechanisms belongs to design within the agreed outcomes and constraints.
