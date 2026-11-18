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
  -> unresolved product choices use resolve-product-decisions; ambiguous domain models use model-domain
  -> impact, coordination, or delegation overlays, when observed conditions require them
  -> check-agreement compares material proposed changes and delivered effects with accepted intent
  -> evidence on the final artifact and a write-clearly response inside the owner
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

An owner may investigate facts without interruption, but it must not silently convert technical maturity or a conservative default into product priority. `scope-product-increment` reconciles each material outcome and keeps product priority separate from implementation order. When multiple material outcomes remain credible without a settled priority, it composes `clarify-intent` before drafting a preferred boundary or order. The clarification resolves the material choice needed for the current result and then returns control to the owner; RumoKit does not require an up-front interview or an exhaustive decision tree.

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
| Outcome/support | `resolve-product-decisions` | Consequential product choices resolved through an example-driven interview |
| Outcome/support | `model-domain` | Precise terms, states, invariants, and authority relationships |
| Outcome | `prototype-decision` | A disposable artifact that answers one uncertain question |
| Outcome | `design-change` | A selected design with boundaries and tradeoffs |
| Outcome | `specify-change` | A behavioral specification and acceptance boundary |
| Outcome | `plan-change` | Ordered, verifiable implementation units |
| Outcome | `implement-change` | New or changed behavior on the real path |
| Outcome | `debug-change` | Root-cause fix with reproduction and regression evidence |
| Outcome | `refactor-change` | Structural change with preservation evidence |
| Outcome/support | `reduce-complexity` | Changed-artifact necessity check or requested cleanup, preserving behavior and meaning |
| Outcome/support | `check-agreement` | Proposed or delivered effects reconciled with accepted outcomes and exclusions |
| Outcome/support | `write-clearly` | Understandable technical writing with concrete result, evidence, and limits |
| Outcome | `verify-change` | Regression coverage for independent failure modes and a verdict on the delivered behavior |
| Outcome | `review-change` | Prioritized, evidence-backed findings |
| Outcome | `finish-change` | Final-state readiness and handoff |
| Outcome | `prepare-pr` | Reviewable PR description and requested creation or update |
| Outcome | `address-review` | Evidence-backed feedback dispositions and authorized resolutions |
| Outcome | `fix-ci` | CI cause, authorized repair, and current-revision check status |
| Outcome | `watch-pr` | Monitoring or authorized follow-through until the agreed stop condition |
| Overlay | `assess-blast-radius` | Concrete downstream impact and tested safety facts |
| Overlay | `coordinate-change` | Dependency, revision, integration, and release topology |
| Overlay | `delegate-work` | Safe partitioning and adjudication of independent work |
| Utility | `resume-work` | Current state reconstructed from history and live evidence |
| Utility | `create-project-verification` | Created or repaired project-local instructions for driving the real surface |

The catalog size is not a target or a cap. A separate capability can improve discovery and application when it has a distinct trigger and completion condition. Router-led new work loads clarification and one owner. A directly requested narrow result can establish its already-explicit scope inline. Design, specification, and planning share `reduce-complexity` with code-changing owners and review. Its necessity check distinguishes accepted obligations from proposed mechanisms before those mechanisms become required work. Reuse an equivalent check of unchanged content rather than adding a cleanup phase. Placement remains conditional.

`clarify-intent` binds the current task and working agreement. A consequential unresolved product choice activates `resolve-product-decisions` before dependent work; ambiguous terminology, transitions, or effect ownership activates `model-domain`. These are reusable independent capabilities, not a requirement to interview every fully specified edit or create a glossary for every task.

`check-agreement` runs before a newly exposed material commitment, at worker integration, after conflicting recovery, and when assessing final outcome fit. It distinguishes aligned, unresolved, and conflicting changes from evidence gaps. New persistence or infrastructure is allowed when the accepted guarantees justify it; the check must not reduce the requested capability to make the artifact easier to validate.

`write-clearly` governs substantive user-facing technical results, including focused direct entries. `reduce-complexity` still owns unnecessary complexity in the artifact. Readable writing and technical necessity are separate checks. Neither one replaces verification or turns a model's self-report into enforcement.

PR work follows the requested result. `review-change` finds defects; `address-review` evaluates an existing feedback queue. `prepare-pr` makes the change reviewable and performs requested PR creation or updates. `fix-ci` diagnoses check executions and carries out authorized repairs. `watch-pr` owns ongoing follow-through, using the host's monitoring facilities and composing repairs only within the user's authority. None implies a pipeline, a push, or a merge. One-time readiness questions remain with `finish-change`.

Descriptions distinguish these entry points before their bodies are loaded. The common verification path stays in `verify-change`; state, asynchronous-effect, and recovery details load from its reference when those properties affect correctness. This changes instruction organization, not the required guarantees. More available skills need not mean more active instructions; routing and behavior still need validation on the actual host.

## Coexistence with other frameworks

Keep domain and tool skills available. Choose a default workflow through the user's instruction or host configuration; useful focused skills can support it. A second framework's mandatory router can still impose its own process. RumoKit reports a real conflict and respects the host's instruction hierarchy rather than claiming that its skill text disables another plugin. Changing startup hooks, global settings, or installed skills requires the corresponding user authority. A mixed-stack exercise must be reported as mixed-stack evidence.

## Process follows task shape

- A small reversible edit can stay inline with an inline acceptance statement.
- A bug uses reproduction and root-cause tracing. A fail-before test is useful only when it is cheap and discriminating.
- New behavior derives examples from user intent and checks the nearest authoritative boundary.
- A refactor defines preservation before changing structure and uses characterization or differential evidence.
- A UI change exercises the rendered user path when the host can drive it.
- A configuration or migration change uses the real loader or consumer, compatibility checks, and safe rehearsal where needed.
- A cross-repository change checks each producer-consumer edge and one integrated scenario against exact revisions.

Specs and plans are outputs, not taxes. Create them when the current request includes them or when decisions, dependencies, risk, or handoff make durable state necessary for the requested work. Neither artifact creates an approval gate or requires the other.

Task tracking uses the host's available task tools and reuses its existing list. It does not create a parallel `todo.md`, require a specification, or enter planning mode. If task tools are unavailable, tracking stays briefly in the conversation unless the user or an established project convention requires a task file.

The shared [work-state contract](../skills/resume-work/references/work-state.md) separates accepted behavior, planned units, and observed progress without requiring separate files. A specification records behavior and decision authority; a plan references it and defines units and expected checks; live status and evidence stay in the chosen task record. Native records are reused when they preserve the content needed for recovery. Documents remain available for a concrete persistence, portability, or handoff need, not as mandatory mirrors. Update at material transitions and resume from the existing entry point. This is a portable content convention, not a memory service or a pre-compaction hook.

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
