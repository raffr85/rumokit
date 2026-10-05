---
name: use-rumokit
description: Use when selecting RumoKit skills for new or resumed software work.
---

# Use RumoKit

Route the request; do not perform domain work here. When a focused skill was invoked directly and fits the result, keep it as owner and follow its own scope, clarification, and evidence obligations. Skip owner selection and do not add a lifecycle around that invocation. The user-facing response obligation below still applies.

## Load the selected instructions

A skill is loaded when its full body is in the current context, through the host's skill tool or by reading its `SKILL.md`. A name, catalog description, or this routing summary is not that body. A router supplied in full by a startup hook is already loaded; do not invoke it again.

When this router selects an owner or an applicable dependency, load that skill before doing the work it governs, then follow its instructions. Reuse a body already loaded. If it cannot be loaded, report the missing guidance and distinguish any fallback from following the skill. Load only the selected skills, not the catalog.

When other frameworks are present, follow the user's established workflow choice and the host's instruction hierarchy. Compose useful focused capabilities without silently adopting another router's lifecycle. If mandatory instructions still conflict, explain the conflict once and its consequence; do not claim an isolated RumoKit workflow or change plugin settings without authority. Another installed skill is not by itself an active competing process.

## Establish intent first

Load and follow `clarify-intent` for every new requested result, before selecting its solution or committing to its scope. This is a required dependency, not a conditional overlay. An implementation request does not bypass it. Reuse the understanding already established for an unchanged continuation; reopen it when new information changes a material decision.

If the user rejects the subject or target, return to that clarification before another dependent tool action. Retrieved history must not silently replace the current task.

Clarification determines what is settled and obtains the missing human decisions. It does not require a specification, plan, questionnaire, or repeated approval of an explicit instruction. Once intent is established, select the owner below and continue through the requested result.

## Choose one owner

Resolve temporal scope before choosing the owner. Match the result the user wants in the current request, not every future artifact they mention:

- "research first; later we can write a spec" means research owns the current request and the specification is deferred;
- "research and deliver a spec" means the specification owns the current request and research supports it;
- "write the spec and wait for approval before planning" means stop at the specification;
- "implement this; create a spec or plan only if needed" means implementation owns the request and both artifacts remain conditional.

Then select the owner. Research that supports a requested MVP or V1 boundary does not take ownership from that boundary:

- current-system explanation or evidence-only research: `understand-code` or `research-decision`
- where a proposed change belongs: `locate-change`
- MVP, V1, first increment, product boundary, or release order: `scope-product-increment`
- a requested interview or unresolved product decisions: `resolve-product-decisions`
- domain terms, states, or authority relationships: `model-domain`
- a decision or prototype: `clarify-intent` or `prototype-decision`
- design, specification, or plan: `design-change`, `specify-change`, or `plan-change`
- implementation, fix, or refactor: `implement-change`, `debug-change`, or `refactor-change`
- cleanup of an existing code, documentation, or prose artifact: `reduce-complexity`
- a technical explanation, rewrite, or delivery summary whose requested result is clear writing: `write-clearly`
- conformity of a proposal or delivery to the accepted outcome: `check-agreement`
- verification, review, or readiness: `verify-change`, `review-change`, or `finish-change`
- preparing or opening a pull request: `prepare-pr`
- assessing or resolving existing review feedback: `address-review`
- diagnosing or repairing CI failures: `fix-ci`
- ongoing pull-request monitoring or follow-through: `watch-pr`
- reusable real-surface instructions: `create-project-verification`

For PR work, select the current result rather than the artifact's name. A fresh code review uses `review-change`; existing comments use `address-review`; a one-time readiness question uses `finish-change`. Preparing a PR, fixing a check, or asking for status does not start monitoring. PR skills are independent entry points, not a delivery sequence.

Load the chosen owner's instructions, then continue through the current requested stop point. Do not stop before a current deliverable, pull a deferred deliverable into the current turn, infer a spec or plan from complexity alone, or invent an approval gate between artifacts.

For material product-boundary or priority choices inside another owner's work, compose `scope-product-increment` before the dependent commitment. That skill owns the authority check; return to the current owner once the choice is settled.

## Add conditionally

- `assess-blast-radius`: concrete downstream uncertainty
- `coordinate-change`: independently versioned components or release edges
- `research-decision`: external or comparative evidence needed by another owner
- `delegate-work`: genuinely separable work
- `resume-work`: history and live state need reconciliation
- `model-domain`: ambiguous terms, transitions, or effect ownership
- `check-agreement`: a material commitment changes scope or effects, worker integration, conflicting recovery, or final delivery-fit comparison
- `verify-change`: choosing or interpreting evidence for changed behavior, including inside implementation, debugging, or refactoring
- `finish-change`: a multi-component handoff, release-readiness claim, or unresolved delivery boundary

Activate these dependencies when their conditions occur, including mid-task; the user need not name them. Split or add a capability when its distinct decision and completion condition warrant it. Skill count is not a target. Do not impose a spec, plan, test-first loop, review, subagent, or fixed pipeline merely because routing occurred; follow the selected owner's task-specific conditions. When material work remains after compaction, compose `resume-work` before another research wave, delegation, expensive check, or recommendation; then return to the same owner and stop point.

Supporting skills run within the owner's current work. Applying a skill already loaded in current context means following it, not reading it again. Reuse current evidence against unchanged artifacts and environments. Loading verification guidance requires no other agent, approval, artifact, or repeated check.

When execution needs task tracking, follow [the work-state contract](../resume-work/references/work-state.md). Use the host's available task tools, not a parallel Markdown checklist. Tracking tasks does not require a specification, a plan document, or entering the host's planning mode.

While a question or job is pending, coordinate follow-up work with what is already queued so it runs once. Use the host's event wait or an appropriately bounded wait; avoid repeated short polls that return no new information. Continue independent work and keep user updates timely.

## Tighten before return

Before drafting a substantive user-facing technical result, load and follow [write-clearly](../write-clearly/SKILL.md), reusing its body when already loaded. This also applies to focused direct entries. Give the answer and concrete meaning inline, with documents as support. It is a communication dependency, not another report or reviewer.

Remove repeated evidence, detail that cannot change the current result, late questions, and artifacts beyond the stop point. Keep writing clarity separate from `reduce-complexity`'s artifact-complexity check. Preserve required outcomes. If the response exposes a material commitment without authority, apply [check-agreement](../check-agreement/SKILL.md) and return to the owner instead of polishing the commitment into an assumption.
