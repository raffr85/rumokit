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

- Reuse current concepts and conventions when they fit.
- Remove or simplify before introducing a new layer.
- Put validation and error translation at the boundary that owns them.
- Keep state and failure behavior explicit.
- Make retryable or resumable side effects idempotent, or expose why they cannot be.
- Preserve unrelated user changes.
- Update concrete callers when a contract changes; do not leave a new API beside unmigrated callers without a compatibility reason.

Add `assess-blast-radius` for shared boundaries and `coordinate-change` for independently versioned components. Delegate only through `delegate-work` when a unit is genuinely separable.

Use the host's supported editing operations and permitted working and temporary paths. After a failed write, inspect whether it changed the artifact, then correct the operation against that state. Reuse already-produced content when the host allows it; a tool-format or permission error does not require redesigning or repeatedly emitting the whole file.

## Prove the resulting behavior

When the change affects identity, permissions, persistent state, or a consumer-facing contract, apply `review-change` to the completed diff against the starting contract before closing. Reconcile each material behavior change with an accepted decision or preservation obligation. This can be an inline review within implementation; independent delegation is conditional on its added value. Reuse an equivalent review already completed against the same artifact.

Load and follow `verify-change` when choosing and interpreting evidence within this implementation, including negative and preserved behavior where material. It does not create a separate phase or require another agent. Reuse relevant current checks rather than rerunning them to satisfy a reporting ritual.

For a multi-component handoff or release-readiness claim, apply `finish-change` to reconcile the final inventory, evidence, and remaining actions.

Return how the implemented behavior meets the accepted outcome, material files or contracts changed, evidence obtained, and missing or unverified expectations. If part remains incomplete, say what the user still cannot do. Do not merge, deploy, publish, or broaden scope without authority.
