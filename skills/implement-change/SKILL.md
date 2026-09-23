---
name: implement-change
description: Use when the requested result is authorized implementation of new or changed behavior in an existing codebase.
---

# Implement a Change

Own the requested behavior through a working, evidenced result.

## Confirm the target

Load and follow `clarify-intent` before selecting the implementation, including when this skill is invoked directly. Load dependencies through the host's skill tool or by reading their full `SKILL.md`; reuse bodies already in context. Their names and descriptions alone are not their instructions. Reuse the established outcome, accepted example, preservation obligations, and stopping point on continuation instead of eliciting them again. Inspect the real execution path and working state before editing. Keep this agreement as the acceptance source; implementation convenience does not change it.

Use an existing specification or plan when one is accepted. Create one only when the change's uncertainty, dependency structure, risk, or handoff requires it.

During review repairs, distinguish restoring accepted behavior from proposing different behavior. Do not make a finding disappear by changing the specification or expected test result to match the code. If a repair would change a material accepted outcome, state the old and proposed behavior and use `clarify-intent` unless existing authorization covers that choice. Documentation corrections that preserve accepted behavior need no new approval.

Do not add a policy bypass for test convenience or hypothetical future operations without an accepted requirement. When the user rejects an agent-added policy or capability, remove its dependent mechanisms and checks within the authorized scope, not only its wording. Inspect dependencies and preserve unrelated user work; do not retain the rejected behavior as an optional switch.

## Change the owning path

Before adding code, a dependency, or an abstraction, trace the relevant flow and choose the simplest adequate option: omit work the accepted outcome does not need; reuse an existing implementation or pattern; use the language's standard library, a native platform capability, or an installed dependency; then add the missing behavior. Search the relevant code before claiming reuse is unavailable. Judge adequacy against the actual requirements, failure behavior, and local conventions, not line count.

- Put validation and error translation at the boundary that owns them.
- Keep state and failure behavior explicit.
- Make retryable or resumable side effects idempotent, or expose why they cannot be.
- Preserve unrelated user changes.
- Update concrete callers when a contract changes; do not leave a new API beside unmigrated callers without a compatibility reason.

Add `assess-blast-radius` for shared boundaries and `coordinate-change` for independently versioned components. Delegate only through `delegate-work` when a unit is genuinely separable.

Use the host's supported editing operations and permitted working and temporary paths. After a failed write, inspect whether it changed the artifact, then correct the operation against that state. Reuse already-produced content when the host allows it; a tool-format or permission error does not require redesigning or repeatedly emitting the whole file.

## Maintain existing task state

When the work uses a durable specification, plan, or handoff, follow [the durable work-state contract](../resume-work/references/work-state.md). Update progress and evidence at material transitions so the next session can continue without reconstructing the conversation. Keep current summaries and next actions aligned with accepted changes; a dated appendix alone does not update them. This maintains existing task state, not a requirement to create documents for every edit.

## Prove the resulting behavior

Apply `remove-slop` to the completed diff as part of implementation. Inspect the resulting artifact, not just the plan or passing tests. Reuse an equivalent check already performed on that diff; this needs no separate stage, report, or agent.

When the change affects identity, permissions, persistent state, or a consumer-facing contract, apply `review-change` to the completed diff against the starting contract before closing. Reconcile each material behavior change with an accepted decision or preservation obligation. This can be an inline review within implementation; independent delegation is conditional on its added value. Reuse an equivalent review already completed against the same artifact.

Load and follow `verify-change` when choosing and interpreting evidence within this implementation, including negative and preserved behavior where material. It does not create a separate phase or require another agent. Reuse relevant current checks rather than rerunning them to satisfy a reporting ritual.

For a multi-component handoff or release-readiness claim, apply `finish-change` to reconcile the final inventory, evidence, and remaining actions.

Return how the implemented behavior meets the accepted outcome, material files or contracts changed, evidence obtained, and missing or unverified expectations. If part remains incomplete, say what the user still cannot do. Do not merge, deploy, publish, or broaden scope without authority.
