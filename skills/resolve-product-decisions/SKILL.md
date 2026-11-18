---
name: resolve-product-decisions
description: Use when interviewing a user about a proposed change or when consequential product choices remain unresolved.
---

# Resolve product decisions

Resolve the decisions that determine what to build. Support the current owner, or own an explicitly requested interview. Reuse the agreement and answers already established by `clarify-intent`; a direct interview establishes its own subject and stopping point.

## Find the next consequential question

Inspect the request, existing behavior, and accepted decisions. Investigate facts available in the code or tools yourself. Identify the first choice where credible answers would change a user-visible outcome, authority, included capability, cost, or recovery behavior.

Walk one operation through to the person who sees its result. Hold settled conditions fixed. When repeated actions can affect one later result, ask about two distinguishable actions under the unresolved condition: “While that is happening, someone does X and then Y. When the recipient returns, what do they see, in order?” An action before that interval is part of the starting state. For other decisions, vary the order or a value until plausible policies predict different results. Give the user the situation and leave the outcome for them to supply. For unclear terms or ownership, use [model-domain](../model-domain/SKILL.md).

For an integration or replacement, establish what current state and unfinished work exist at first use and what happens to them. Importing a current snapshot and replaying historical events are different choices; excluding history does not settle the snapshot's effects. Reuse a starting condition the user already accepted.

Ask before editing the feature or its tests. Group independent questions. Follow dependent ones after the answer. Read each question as the recipient: could they just say yes or pick a result you named? If so, keep the situation and remove the proposed result. When the user asks for help choosing, discuss alternatives and tradeoffs against their goal. Explain any real constraints. Leave delegated implementation details to the builder.

Ask in plain chat where the user can reply, or use a free-text field with no preselected answer. If the question appears twice, keep its open wording both times.

## Follow the answer

Wait for the human reply. Keep settled requirements as givens. Did the reply state a rule, delegate the choice, or distinguish the possible behaviors? An example on which both policies agree settles only that example. Ask what the person would observe in a case where those policies diverge. When the reply settles the behavior, play it back briefly as an observable result and carry that example into verification. Continue under the existing authorization without an extra approval turn.

Distinguish accepted outcomes, delegated technical choices, assumptions, and unresolved decisions. Update the existing agreement or task document as answers arrive. A glossary, ADR, specification, or plan is useful only when durable terminology, rationale, behavior, or sequencing needs it; the interview does not require all of them.

Stop when the decisions needed for the current result are settled. Return those decisions, their basis, the example, preservation obligations, and any genuinely remaining dependency to the owner. For a user-facing question or conclusion, load and follow [write-clearly](../write-clearly/SKILL.md), reusing its full body when already loaded. A fully specified edit proceeds without an interview; a difficult product choice is not settled by a confident technical default.
