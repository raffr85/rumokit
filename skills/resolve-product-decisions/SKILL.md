---
name: resolve-product-decisions
description: Use when interviewing a user about a proposed change or when consequential product choices remain unresolved.
---

# Resolve product decisions

Resolve the decisions that determine what to build. Support the current owner, or own an explicitly requested interview. Reuse the agreement and answers already established by `clarify-intent`; a direct interview establishes its own subject and stopping point.

## Find the next consequential question

Inspect the request, existing behavior, and accepted decisions. Investigate facts available in the code or tools yourself. Identify the first choice where credible answers would change a user-visible outcome, authority, included capability, cost, or recovery behavior.

Walk a concrete operation with the user: starting state, actor, action, visible result, and what must survive. Probe the relevant interruption, retry, existing data, or boundary case. Use a counterexample to expose a hidden choice, not to impose a speculative requirement. If terms or ownership are ambiguous, compose [model-domain](../model-domain/SKILL.md).

For an integration or replacement, establish what current state and unfinished work exist at first use and what happens to them. Importing a current snapshot and replaying historical events are different choices; excluding history does not settle the snapshot's effects. Reuse a starting condition the user already accepted.

Ask the question before work that depends on its answer. Explain the differing consequences and any recommendation grounded in the user's stated criteria. Lead with one decision; group questions only when their answers are independent. Do not bury the question in a discovery report or ask the user to choose implementation details already delegated to you.

## Follow the answer

Wait for the actual human answer. A submitted asynchronous question is not an answer. Continue independent authorized work, not the implementation of your preferred answer. Trace what the answer settles and what it newly opens. Ask dependent questions in a later round. Test the resulting understanding with a concrete accepted example and a plausible wrong result.

Distinguish accepted outcomes, delegated technical choices, assumptions, and unresolved decisions. Update the existing agreement or task document as answers arrive. A glossary, ADR, specification, or plan is useful only when durable terminology, rationale, behavior, or sequencing needs it; the interview does not require all of them.

Stop when the decisions needed for the current result are settled. Return those decisions, their basis, the example, preservation obligations, and any genuinely remaining dependency to the owner. For a user-facing question or conclusion, load and follow [write-clearly](../write-clearly/SKILL.md), reusing its full body when already loaded. A fully specified edit proceeds without an interview; a difficult product choice is not settled by a confident technical default.
