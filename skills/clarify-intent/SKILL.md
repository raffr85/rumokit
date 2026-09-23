---
name: clarify-intent
description: Use at the start of every new software-work request and when its intent materially changes, before committing to a solution, scope, or implementation.
---

# Clarify Intent

Establish a shared understanding of the requested result. Clarification is always part of the work; it is not an optional reaction to feeling uncertain.

## Establish the outcome

Inspect the request, accepted decisions, relevant existing behavior, and available evidence. Facts are the agent's job: do not ask the user to perform research or design an experiment they delegated to you.

Bind source and tool selection to the current task and its relevant project, environment, resource or session. Resolve shorthand from the request and task-local evidence. A similarly named app, recent conversation or memory hit does not establish that connection. Follow another project or session when the current request or an observed dependency connects it; do not adopt its task or permissions merely because it is accessible.

Keep a compact working agreement in the conversation or an existing task artifact: the observable outcome and who needs it, material constraints and preservation obligations, settled decisions and their basis, open choices, and the requested stopping point. Distinguish the investigation surface from the authorized changes: permission to inspect broadly or prepare repositories does not authorize repairing every discovered problem. Distinguish user decisions, delegated choices, technical facts, and assumptions. Do not create a separate document or approval turn merely to hold this understanding.

An explicit, sufficiently defined request can establish this agreement immediately. Otherwise, test the understanding against a concrete example of the user's operation, not just the name of the requested artifact.

When the user rejects the subject or target, stop actions based on that interpretation. Discard its dependent search terms, tool targets and proposed next steps; an apology is not a corrected working agreement. Rebind to the user's correction and still-valid task context before the next dependent action. Continue if the target is clear; otherwise ask the smallest question that distinguishes the remaining targets. Do not search unrelated sessions to guess what the correction meant.

## Walk the consequential path

For new or changed behavior, trace a representative case: who starts with what, what they do, what should change, and what must remain unchanged. For stateful or consequential work, follow the relevant failure, retry, or intervening change far enough to expose decisions about authority, commitment, and recovery. Distinguish a preview or proposal from an action that changes state. This is a discovery aid, not a fixed interview or a checklist to apply to every task.

When introducing an integration or replacing a workflow, establish what state and work already exist at first use and what happens to them. Importing current state and processing historical events are different choices; either may trigger new effects. An exclusion of history does not settle those effects. Resolve material alternatives before treating the starting behavior as accepted; do not invent migration work or reopen a starting condition that the user already settled.

Find the first unresolved fork where credible alternatives produce materially different user outcomes, included capabilities, authority, risk, cost, or reversibility. Code can reveal what the system does; it cannot choose what the user wants. An instruction to implement authorizes execution, not every unstated product choice. Use `scope-product-increment` when the product boundary itself needs resolution.

Once evidence exposes such a fork, bring it to the user before expanding dependent research, delegation, or planning. A list of open decisions is not shared understanding. For an explicitly inventory-only or research-only request, report the relevant unknowns without pulling future decisions into scope; when the requested result requires resolving them, conduct that clarification rather than leaving it as a generic future task.

## Ask neutrally

- Explain the concrete consequence of the decision.
- Ask for missing outcomes or constraints; research and recommend technical choices against them rather than making the user design the solution.
- Present credible alternatives and their consequences without steering toward a preferred answer.
- Group questions only when they are independent and easy to answer together.
- Use a small concrete example when abstract alternatives hide different effects.

Ask before the dependent commitment and wait for the answer. An asynchronous question being accepted by a tool is not a human response. Continue only independent, authorized work; if the host cannot deliver an answer during the turn, return the question before doing work that assumes it. Do not implement a preferred answer while waiting.

If the user does not know yet, help them decide with consequences, concrete examples, or `prototype-decision`. Do not turn an unknown preference into a technical default. Ask only questions whose answers can affect the requested result; stop questioning once those decisions are established.

For a cheap, reversible detail that does not change the core outcome, make a clearly stated assumption and continue. Do not assume permission for external writes, destructive actions, release, or materially broader scope.

## Carry the agreement into delivery

Closure requires an explicit request or answer, a prior accepted decision, delegated choice with sufficient criteria, or evidence that eliminates the material alternatives. Silence about an announced default is not acceptance. Preserve an explicit decision closely enough that another owner can apply it; do not ask the user to approve it again.

Return the agreement to the primary owner. Keep its concrete example and preservation obligations available to implementation, delegation, and final verification. Revisit only newly opened material choices. When a decision changes, replace the superseded expectation and its dependent plan or checks; do not silently rewrite the expectation to match what was built.
