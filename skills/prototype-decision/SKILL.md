---
name: prototype-decision
description: Use when one material design or technical uncertainty is cheaper and more reliable to answer with a disposable executable or visual artifact than with discussion alone.
---

# Prototype a Decision

Build the smallest disposable artifact that answers one named question.

## Define the experiment

State:

- the uncertain decision;
- the observable that would discriminate between options;
- what the prototype deliberately will not prove;
- the time, fidelity, and cleanup boundary.

Inspect the real system and relevant evidence before prototyping. A prototype should close an evidence gap, not substitute for understanding it.

## Keep it disposable

Use the cheapest faithful surface: a narrow spike, mock, trace, benchmark, rendered interaction, contract probe, or isolated integration. Avoid production architecture, generalized abstractions, broad polish, and hidden coupling.

Exercise the artifact against the named observable. Record failures and ambiguous results; do not repair the metric until it says yes.

## Return the answer

Report:

- what was built and where;
- what was observed;
- which decision the evidence supports;
- limitations and unresolved risks;
- whether the artifact should be discarded, preserved for reference, or deliberately promoted through a separate implementation task.

Do not merge prototype code into production merely because it ran.
