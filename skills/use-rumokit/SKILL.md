---
name: use-rumokit
description: Use when selecting RumoKit skills for new or resumed software work.
---

# Use RumoKit

When the user invokes a focused skill that fits, keep it as owner. Follow its clarification, evidence and response obligations. Otherwise select one owner below.

## Load the selected instructions

Load the full body of the owner and each applicable dependency before its work. Reuse instructions already delivered, including this router when supplied by a hook. A catalog entry or successful read call alone does not establish delivery. If output was truncated, retrieve just the missing section, or read the affected skill separately. If it remains unavailable, identify the fallback.

Respect the user's workflow and host instruction hierarchy. An installed framework alone does not activate its lifecycle. If mandatory instructions conflict, explain the consequence once. Changing plugin settings requires authority.

## Establish intent first

Load and follow `clarify-intent` for each new result before committing to scope or solution, including implementation. Reuse settled decisions on continuation. If the user corrects the target, resolve it before another dependent action. Earlier sessions cannot replace the current request. Ask about material decisions still open; an explicit instruction already supplies authority within its scope.

## Choose one owner

Choose the result due now. Research owns “investigate first, spec later.” Specification owns “research and deliver a spec.” Honor an explicit stop after a spec. An implementation request keeps any supporting spec or plan conditional. Research for an MVP decision supports the scope owner.

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

Use `review-change` for fresh PR findings and `finish-change` for one-time readiness. Start monitoring only when requested. For a material product priority inside another task, use `scope-product-increment` before committing, then return to the owner.

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

Apply dependencies as their conditions arise. They add no automatic phase, reviewer or approval. After compaction with material work remaining, use `resume-work` before new research, delegation, costly checks or recommendations. Reuse fresh evidence and pending jobs; use bounded or event-driven waits while doing independent work.

Track tasks through [the work-state contract](../resume-work/references/work-state.md) using available native tools. Keep progress inline when unavailable, subject to the user's or project's chosen record.

## Tighten before return

Carry authorized work through its requested stopping point. When a prerequisite blocks part of it, try an available in-scope alternative and finish separable work. Stop at explicit gates or when only a human decision, new access or external action outside scope can move it forward.

Use [write-clearly](../write-clearly/SKILL.md) for substantive technical answers, including direct skill entries. Give the result and its meaning in chat. Remove repetition, preserve required outcomes and apply [check-agreement](../check-agreement/SKILL.md) if a material commitment still lacks authority.
