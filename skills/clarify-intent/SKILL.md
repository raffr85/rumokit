---
name: clarify-intent
description: Use when starting software work or when the intended outcome or material constraints change.
---

# Clarify Intent

Establish a shared understanding of the requested result. Clarification is always part of the work; it is not an optional reaction to feeling uncertain.

## Establish the outcome

Inspect the request, accepted decisions, relevant existing behavior, and available evidence. Facts are the agent's job: do not ask the user to perform research or design an experiment they delegated to you.

Bind source and tool selection to the current task and its relevant project, environment, resource or session. Resolve shorthand from the request and task-local evidence. A similarly named app, recent conversation or memory hit does not establish that connection. Follow another project or session when the current request or an observed dependency connects it; do not adopt its task or permissions merely because it is accessible.

Keep a compact working agreement in the conversation or an existing task artifact: the observable outcome and who needs it, material constraints and preservation obligations, settled decisions and their basis, open choices, and the requested stopping point. Distinguish the investigation surface from the authorized changes: permission to inspect broadly or prepare repositories does not authorize repairing every discovered problem. Distinguish user decisions, delegated choices, technical facts, and assumptions. Do not create a separate document or approval turn merely to hold this understanding.

State the understood outcome and decisive constraints briefly before committing to a solution, so the user can recognize a misunderstanding. This is a write-back, not a new permission request. An explicit accepted instruction already supplies authority within its scope.

An explicit, sufficiently defined request can establish this agreement immediately. Otherwise, test the understanding against a concrete example of the user's operation. Extract the behavior the example illustrates; a sample vendor, technology, or name is not an additional integration requirement.

When the user rejects the subject, scope, or complexity, stop work based on that interpretation. Discard stale search terms and tool targets. Reconcile the affected mechanisms, worker assignments, estimates, and next steps with the correction before continuing. Retain required behavior and still-valid evidence. Continue if the target is clear; otherwise ask the smallest question that distinguishes the remaining targets. Do not search unrelated sessions to guess what the correction meant.

## Resolve material choices

For new or changed behavior, trace a representative operation and what must remain unchanged. If the terms, states, or effect owners are ambiguous, apply [model-domain](../model-domain/SKILL.md). Code can reveal existing behavior; it cannot choose the intended result.

When credible alternatives would materially change outcomes, included capabilities, authority, risk, or cost, load and follow [resolve-product-decisions](../resolve-product-decisions/SKILL.md) before dependent research, planning, delegation, or implementation. Its interview resolves the needed choice rather than producing a generic open-decisions list. Use `scope-product-increment` when the product boundary itself needs resolution. For an inventory-only request, report unknowns without pulling future choices into scope.

An asynchronous question being accepted by a tool is not a human answer. Wait before the dependent commitment and continue only independent authorized work. If the user does not know yet, help them decide through the interview or `prototype-decision`; an unknown preference is not a technical default.

For a cheap, reversible detail that does not change the core outcome, make a clearly stated assumption and continue. Do not assume permission for external writes, destructive actions, release, or materially broader scope.

## Carry the agreement into delivery

Closure requires an explicit request or answer, a prior accepted decision, delegated choice with sufficient criteria, or evidence that eliminates the material alternatives. Silence about an announced default is not acceptance. Writing an assumption into a draft does not settle it. Preserve decisions and constraints in the resulting recommendation; do not ask the user to approve them again.

Return the agreement to the primary owner. Keep its concrete example and preservation obligations available to implementation, delegation, and final verification. Revisit only newly opened material choices. When a decision changes, replace the superseded expectation and its dependent plan or checks; do not silently rewrite the expectation to match what was built.

Before a newly exposed material commitment or a disputed delivery-fit claim, compose [check-agreement](../check-agreement/SKILL.md). Reuse the established understanding; reopen only the choice that the comparison shows is unresolved.
