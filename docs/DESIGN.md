# Capability-led design

**Status:** version 1.0, with thin Claude-compatible and Codex bootstrap integrations. The defined acceptance case passed on Codex and Devin; broad effectiveness across tasks and hosts remains unproven. See [validation and limits](VALIDATION.md).

## Architecture

```text
host SessionStart adapter, when supported and trusted
  -> bootstrap to the portable router in session context
request + developer context
  -> use-rumokit
  -> clarify-intent establishes the requested outcome and material decisions
  -> one primary outcome owner
  -> focused supporting skills, when their output is needed
  -> impact, coordination, or delegation overlays, when observed conditions require them
  -> expected outcome compared with evidence on the final artifact
  -> relevance pass inside the owner before return
```

The framework does not own the host's agent loop. It supplies focused decision procedures to the model and uses native host tools. A host adapter raises the visibility and persistence of the portable router; it does not classify user intent independently or block an unsupported recommendation.

A direct invocation can enter at a focused owner instead of the router. The skill establishes or reuses the relevant intent within its scope and retains any real dependencies. A placement map, explanation, or cleanup does not require a whole change lifecycle.

Keep decision rules with their owner. The bootstrap activates routing; `scope-product-increment` owns product-priority authority. Do not duplicate its procedure in adapters or require a fixed authority label as a substitute for resolving the choice. This architecture is shared across models; model-specific variants need evidence of a behavioral difference.

Codex, Claude Code, and compatible hosts load the same skills and `SessionStart` hook from one package through their native manifests. Version 1.0.1 removes the schema-declared root manifest because Codex 0.153.1 skips lifecycle hooks for that format. The portable skills remain unchanged; portability does not require a particular host's manifest. The separate Codex adapter is retained only for legacy installations and is not part of the current setup.

## The primary owner closes the current request

For router-led work, the router composes `clarify-intent` to establish the current requested result and material decisions before selecting a solution. It distinguishes that result from future intentions, then selects the skill whose output matches it. That skill owns completion through the requested stopping point. Explicit or already accepted intent can satisfy clarification without another question; a new material choice requires a human answer or sufficient delegated criteria, not an agent-announced default.

If a request asks for research and a specification in the same scope, `specify-change` owns the result and can use `research-decision` for the research output. Research cannot stop that request early. If the user says to research first and create a specification later, the current owner depends on the research result: `research-decision` owns evidence alone, while `scope-product-increment` owns a requested MVP, V1, first-increment, product-boundary, or release-order recommendation. The specification remains deferred. Temporal words such as "initially", "later", "after approval", and "in the next step" define the stopping point rather than a mandatory lifecycle.

A supporting skill returns a distinct artifact or evidence to the owner. An overlay adds obligations without changing the result. No skill can infer permission for implementation, merge, deployment, deletion, or another external action.

The working agreement connects clarification to delivery: observable outcome, a representative user operation, preservation obligations, decision authority, open choices, and stopping point. It stays in the conversation or an existing artifact. For consequential behavior, walking the relevant failure or intervening change exposes product choices that a happy-path paraphrase misses. Specs, plans, workers, and recovery inherit this agreement rather than redefining it. Final verification compares it with the integrated output and names missing or unverified capabilities even if local tests pass.

Implementation, debugging, and refactoring use `verify-change` when choosing and interpreting evidence. A multi-component handoff or release-readiness claim also uses `finish-change`. These are instruction dependencies inside the current task, not mandatory lifecycle stages. The owner retains its authority and reuses fresh evidence. Direct skill invocation must retain these dependencies, not rely on a prior router invocation.

For stateful, temporal, retry-sensitive, or interacting rules, verification derives a material invariant from the accepted outcome and exercises a short sequence that could violate it, including the visible consequence. This adds a way to select discriminating evidence, not a universal TDD requirement, test quota, review stage, or domain-specific oracle. The support-queue failure motivated the mechanism; its effectiveness beyond that case remains to be established.

An owner may investigate facts without interruption, but it must not silently convert technical maturity or a conservative default into product priority. `scope-product-increment` reconciles each material outcome and keeps product priority separate from implementation order. When multiple material outcomes remain credible without a settled priority, it composes `clarify-intent` before drafting a preferred boundary or order. The clarification covers only the current decision frontier and then returns control to the owner; RumoKit does not require an up-front interview or an exhaustive decision tree.

Before returning, the owner removes repeated evidence, detail that cannot change the current result, late decorative questions, and artifacts beyond the requested stopping point. This relevance pass cannot narrow required outcomes or authorize a product choice. If it finds an unsupported commitment, control returns to the decision owner and `clarify-intent`.

A utility can own the result when the user directly requests its artifact. Otherwise it restores or creates reusable context for the primary outcome owner.

## Catalog

| Kind | Skill | Result |
| --- | --- | --- |
| Router | `use-rumokit` | Primary owner and smallest justified composition |
| Outcome | `understand-code` | Evidence-backed explanation of the current system |
| Outcome | `locate-change` | Owning path, required companions, and verification entry point |
| Outcome | `research-decision` | Facts, options, contradictions, and evidence gaps |
| Outcome | `scope-product-increment` | MVP, V1, product boundary, and release-order decisions |
| Outcome | `clarify-intent` | Material human decisions needed for the requested result |
| Outcome | `prototype-decision` | A disposable artifact that answers one uncertain question |
| Outcome | `design-change` | A selected design with boundaries and tradeoffs |
| Outcome | `specify-change` | A behavioral specification and acceptance boundary |
| Outcome | `plan-change` | Ordered, verifiable implementation units |
| Outcome | `implement-change` | New or changed behavior on the real path |
| Outcome | `debug-change` | Root-cause fix with reproduction and regression evidence |
| Outcome | `refactor-change` | Structural change with preservation evidence |
| Outcome/support | `remove-slop` | Changed-artifact necessity check or requested cleanup, preserving behavior and meaning |
| Outcome | `verify-change` | Bounded verdict from task-shaped evidence |
| Outcome | `review-change` | Prioritized, evidence-backed findings |
| Outcome | `finish-change` | Final-state readiness and handoff |
| Overlay | `assess-blast-radius` | Concrete downstream impact and tested safety facts |
| Overlay | `coordinate-change` | Dependency, revision, integration, and release topology |
| Overlay | `delegate-work` | Safe partitioning and adjudication of independent work |
| Utility | `resume-work` | Current state reconstructed from history and live evidence |
| Utility | `create-project-verification` | Project-local instructions for driving the real surface |

The catalog size is not a target. Keep a skill separate only while it has a distinct trigger and completion condition. Router-led new work loads clarification and one owner. A directly requested narrow result can establish its already-explicit scope inline. Add supporting skills for concrete work: code-changing owners and review share `remove-slop` for the final diff, while placement remains conditional. Reuse the same artifact check rather than adding a cleanup phase.

## Process follows task shape

- A small reversible edit can stay inline with an inline acceptance statement.
- A bug uses reproduction and root-cause tracing. A fail-before test is useful only when it is cheap and discriminating.
- New behavior derives examples from user intent and checks the nearest authoritative boundary.
- A refactor defines preservation before changing structure and uses characterization or differential evidence.
- A UI change exercises the rendered user path when the host can drive it.
- A configuration or migration change uses the real loader or consumer, compatibility checks, and safe rehearsal where needed.
- A cross-repository change checks each producer-consumer edge and one integrated scenario against exact revisions.

Specs and plans are outputs, not taxes. Create them when the current request includes them or when decisions, dependencies, risk, or handoff make durable state necessary for the requested work. Neither artifact creates an approval gate or requires the other.

When those artifacts exist, their owners use the shared [durable work-state contract](../skills/resume-work/references/work-state.md). A specification records expected behavior and decision authority; a plan records units, status and observed evidence; a compact continuation block identifies the next authorized action. These may share one existing document. Update current state at material transitions, mark replaced directions as history, and resume from that entry point with artifact checks. This is a portable document convention, not a memory service or a pre-compaction hook.

## Delegation follows separability

Use a worker when the unit has bounded inputs, an independent output, isolated writable state, and evidence the lead can inspect. Research, implementation, and review can all qualify.

Keep work inline when it is small, tightly coupled, or cheaper to complete than to explain and integrate. The lead remains responsible for the requested result. Worker agreement is not proof.

Delegation depth has no fixed cap. Each additional unit or wave must identify an unresolved gap and an output capable of changing the owner's conclusion. Once no such marginal decision value remains, the owner integrates instead of continuing to fan out.

The portable framework defines explorer, implementer, reviewer, and integrator roles. A host adapter maps those roles to available models, reasoning settings, tools, and subagent APIs. The user can override that policy. Record the requested configuration without claiming that the provider attested the served model.

## Project-local verification

Generic guidance cannot know how every product starts, which account state it needs, or how an agent drives its public surface. `create-project-verification` can generate a project-local skill with exact launch, health, drive, evidence, isolation, and cleanup instructions.

Create this knowledge only when the repository lacks a reliable path and the path will be reused. It belongs with the project, not in RumoKit's generic core.

## Assurance boundary

- **Advisory:** a skill or bootstrap guides the model and the model reports its evidence.
- **Observed:** a host component authenticates an action, artifact, or result.
- **Enforced:** the host can prevent or downgrade an action or claim.
- **Confined:** the host independently verifies process, filesystem, network, secret, and state boundaries.

These capabilities are independent. The portable core is advisory. The Claude Code and Codex integrations add session context at startup and after supported context resets, but remain advisory. Delivery and behavior must be validated separately on each named host and version. A host without native routing needs its own separately validated adapter.
