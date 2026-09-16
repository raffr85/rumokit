---
name: understand-code
description: Use when the user asks how existing code behaves or why a current design or historical decision exists, without requesting changes.
---

# Understand Code

Explain the system that exists. A direct invocation needs no router or change lifecycle. If the question is explicit, investigate it; ask only when an unresolved distinction would materially change the answer. Do not implement a change unless the user separately asks for one. A request only for where a proposed change belongs is owned by `locate-change`.

## Trace the real path

Start from the user-visible behavior, entry point, error, command, or public interface in question. Follow the executed path through:

1. dispatch and ownership;
2. data and state transitions;
3. side effects and external boundaries;
4. callers, consumers, and configuration that materially alter behavior.

For **how**, establish the executed path and observable behavior. For **why**, inspect relevant decisions, history, and constraints and distinguish the recorded reason from your present-day explanation of the tradeoff. Plausible benefits in current code do not establish the original author's intent. Say when the historical reason cannot be established; do not invent it.

Read source before inferring architecture. Use tests, documentation, generated artifacts, or runtime observations only for claims they support. Search history when rationale is requested or it resolves a material contradiction, not for every behavior question. Add `coordinate-change` when an unresolved versioned edge affects the answer.

When source freshness matters, establish the relevant repository roots, revisions, branches, working-tree state, and local-versus-canonical boundary once. Record and reuse that identity. Recheck it only after a checkout, mutation, synchronization, contradictory observation, or another named freshness change.

## Keep evidence honest

Separate:

- verified behavior, with concrete source or runtime evidence;
- a reasoned inference, with the evidence that makes it likely;
- an unknown that was not found or cannot be established from available artifacts.

Do not turn names, comments, mocks, or one isolated test into proof of production behavior. Prefer the shortest source map that answers the question over a repository tour.

## Finish with a usable mental model

Return:

- the behavior in plain language;
- the execution path and ownership boundaries;
- the important state, contracts, and side effects;
- any material variation or uncertainty;
- direct pointers to the decisive evidence.

Stop when the user's question is answered, not when every related module has been cataloged.
