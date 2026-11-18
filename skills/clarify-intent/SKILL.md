---
name: clarify-intent
description: Use when starting software work or when the intended outcome or material constraints change.
---

# Clarify Intent

Before editing, follow a real situation the old product could not represent through to the person who sees the result. When several actions can occur before that result and their combined effect is unsettled, put two distinct occurrences inside that interval in the question you send. Ask what the person sees, in order. An answer about a single occurrence settles only that case.

Check the behavior you are about to promise. For each material outcome, including a proposed refusal, name what selects it: the user's words, an existing contract for that situation, or delegated criteria. If two responses still meet those terms and affect the user differently, describe the starting situation and ask the user to supply the missing outcome. If they can answer by picking an outcome you named, rewrite the question. Ask about independent decisions separately in the same message.

While waiting, inspect facts or run existing checks. Leave implementation of the feature and its acceptance tests until the decisions arrive; a partial edit can silently make a default observable. Follow up when a material choice remains open or the answer opens a new one. Fully specified behavior and delegated implementation details can proceed immediately.

## Establish the outcome

Inspect the request, accepted decisions, relevant existing behavior, and available evidence. Facts are the agent's job: do not ask the user to perform research or design an experiment they delegated to you.

Bind source and tool selection to the current task and its relevant project, environment, resource or session. Resolve shorthand from the request and task-local evidence. A similarly named app, recent conversation or memory hit does not establish that connection. Follow another project or session when the current request or an observed dependency connects it; do not adopt its task or permissions merely because it is accessible.

Keep a compact working agreement in the conversation or an existing task artifact: the observable outcome and who needs it, material constraints and preservation obligations, settled decisions and their basis, open choices, and the requested stopping point. Distinguish the investigation surface from the authorized changes: permission to inspect broadly or prepare repositories does not authorize repairing every discovered problem. Distinguish user decisions, delegated choices, technical facts, and assumptions. Do not create a separate document or approval turn merely to hold this understanding.

When material behavior is settled, give the user a short **intent receipt** before the first dependent edit. Use one “Agreed” sentence in their language. Attribute the rule to the user's answer or an accepted spec passage and show the distinguishing input and expected result together. Quote an example the user already gave, or derive one from their explicit rule. Include a consequential exclusion or open choice when it limits the claim. Continue under existing approval. Routine mechanical edits need no separate receipt.

An explicit, sufficiently defined request can establish this agreement immediately. Otherwise, test the understanding against a concrete example of the user's operation. Extract the behavior the example illustrates; a sample vendor, technology, or name is not an additional integration requirement.

When the user rejects the subject, scope, or complexity, stop work based on that interpretation. Discard stale search terms and tool targets. Reconcile the affected mechanisms, worker assignments, estimates, and next steps with the correction before continuing. Retain required behavior and still-valid evidence. Continue if the target is clear; otherwise ask the smallest question that distinguishes the remaining targets. Do not search unrelated sessions to guess what the correction meant.

## Resolve material choices

Use a concrete example to check what the answer settles. Use [model-domain](../model-domain/SKILL.md) for unclear terms, states or owners.

When credible alternatives would materially change outcomes, included capabilities, authority, risk, or cost, load and follow [resolve-product-decisions](../resolve-product-decisions/SKILL.md) before dependent research, planning, delegation, or implementation. Its interview resolves the needed choice rather than producing a generic open-decisions list. Use `scope-product-increment` when the product boundary itself needs resolution. For an inventory-only request, report unknowns without pulling future choices into scope.

An asynchronous question being accepted by a tool is not a human answer. Wait before the dependent commitment and continue only independent authorized work. If the user does not know yet, help them decide through the interview or `prototype-decision`; an unknown preference is not a technical default.

For a cheap, reversible detail that does not change the core outcome, make a clearly stated assumption and continue. Do not assume permission for external writes, destructive actions, release, or materially broader scope.

## Carry the agreement into delivery

Closure requires an explicit request or answer, a prior accepted decision, delegated choice with sufficient criteria, or evidence that eliminates the material alternatives. Silence about an announced default is not acceptance. Writing an assumption into a draft does not settle it. Preserve decisions and constraints in the resulting recommendation; do not ask the user to approve them again.

Keep the receipt in this conversation by default. When the work already uses a task record or spec for handoff, put it there or point to the exact passage that already captures it. If a later decision changes an expectation, identify what it replaces, cite the new authority, and carry unaffected promises forward. Return the current receipt to the owner for implementation and final verification.

Before a newly exposed material commitment or a disputed delivery-fit claim, compose [check-agreement](../check-agreement/SKILL.md). Reuse the established understanding; reopen only the choice that the comparison shows is unresolved.
