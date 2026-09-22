# Durable work state

Use this contract when authoring or maintaining task documents that another session must use. It does not require documents for a small inline task or authorize edits during a read-only review.

## One entry point, distinct responsibilities

Choose an existing task README, specification, plan, or handoff as the entry point. Use the project's paths, language, and conventions; make the entry point discoverable from the existing task or project index. Do not create competing summaries or a global project status for unrelated work.

- **Specification:** expected behavior, accepted examples, preservation obligations, and decisions with their source. Distinguish accepted decisions, proposals, unresolved choices, and superseded directions. A draft's presence is not approval.
- **Plan:** ordered units referencing that contract, their dependencies, current status, and evidence. Keep the expected completion check separate from the result actually obtained. Use stable identifiers when other artifacts refer to a requirement, decision, or unit.
- **Continuation state:** where the work stands and the next authorized action. Link to the contract and evidence instead of copying them.

These roles may be sections of one document. Keep the current state near the entry point and label older records as history. An appendix must not silently override a section still presented as current.

## Compact continuation block

Keep only fields relevant to this work:

- **Outcome and authority:** requested result, stop point, binding decisions and their sources; links to the current contract and plan.
- **Artifact and progress:** repositories or paths, revisions or relevant uncommitted state, completed units, current unit, and remaining work. Separate implemented, locally verified, published, and activated states.
- **Evidence and limits:** check or observation, result, exact artifact/environment it covers, and what change would invalidate it. Record unavailable prerequisites and the conditions for retrying them.
- **Next action:** the bounded authorized step; material open choices or blockers and their owners. Include pending questions, running operations or workers and their handles when continuation depends on them.

Identify when this state was reconciled. A timestamp alone does not make old evidence valid. Store pointers and non-secret configuration, not credentials or whole transcripts.

## Maintain at material transitions

Update the affected state when a decision changes, a unit completes, a material blocker changes, or work is handed off. Do this during the work; do not depend on a pre-compaction hook or create a checkpoint for every tool call.

When a direction changes, update the current summary, dependent units and gates together, and mark the old direction superseded. Preserve its historical evidence without leaving it as an actionable instruction. Record new progress without rewriting the expected behavior to fit the implementation.

Before handoff, check that the entry point, contract, plan, and next action agree. Update the relevant sections rather than adding another dated conclusion that leaves the old summary current.
