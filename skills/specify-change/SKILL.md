---
name: specify-change
description: Use when the requested result needs a durable behavioral contract, acceptance boundary, or shared definition of what a proposed change must and must not do.
---

# Specify a Change

Write the behavioral contract needed to build or review the change. A specification is conditional: create it when requested or when unresolved behavior, risk, dependencies, or handoff make inline intent unsafe.

## Ground the contract

Establish or reuse the outcome through `clarify-intent`, including direct invocation. Inspect current behavior and relevant interfaces. Carry forward accepted examples, preservation obligations, and the basis for decisions; do not replace user intent with a technically convenient scope. Incorporate accepted research and design without reopening settled choices. Use `coordinate-change` for versioned component edges.

Describe behavior independently of an imagined implementation unless the implementation mechanism is itself a requirement.

## Make boundaries testable

Cover the parts that matter:

- intent and non-goals;
- current evidence and accepted decisions;
- actors, states, transitions, inputs, outputs, and interfaces;
- invariants and behavior that must be preserved;
- forbidden effects and unsafe shortcuts;
- error, retry, concurrency, compatibility, and recovery behavior where relevant;
- examples and acceptance evidence;
- remaining decisions, owners, and consequences.

Use [assets/change-spec.md](assets/change-spec.md) as a starting shape, deleting sections that do not earn their place. Follow [the durable work-state contract](../resume-work/references/work-state.md) for document identity, decision authority, and its relationship to plans and continuation state. Reuse an existing entry point; a specification does not require a separate status file.

## Check completeness

Walk representative success, failure, boundary, and preservation cases. A reader without the prior conversation should be able to distinguish a compliant implementation from a plausible but wrong one, and identify which decisions are accepted rather than proposed. Reconcile changed decisions with the current summary and linked dependent artifacts, not only a new history entry.

Stop with the accepted behavioral boundary. Do not expand the document into an implementation plan unless that is also requested.

A completed specification does not create an approval ceremony or make a plan mandatory. Pause only for an explicit user gate, missing authority, or a material unresolved choice whose alternatives would change the contract.
