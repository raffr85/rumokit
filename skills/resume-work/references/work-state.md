# Work state

Use this contract when tracking execution or preserving an agreement for continuation. It does not require a tracker for a small inline task or authorize changes during a read-only review.

## Tasks belong in the host

When tasks need tracking, inspect the current host's available task tools and reuse its existing task list. Create and update tasks there, preserving identifiers and status. Keep dependencies and agreement or evidence references in supported fields or the conversation; do not create files to extend a limited task tool. A tool name mentioned by a skill is not proof that the tool is available. Task creation is not implementation, and a completed task status is not verification evidence.

Do not create or maintain a parallel `todo.md` or other checklist file. If task tools are unavailable, keep the current unit, remaining work, and next action briefly in the conversation. Do not invent a tool, a task service, or a file fallback. Use a task file when the user explicitly requests it or an established project convention requires it; that file is then the task record, not an additional checklist to synchronize.

Read and update the chosen task record at material transitions. Recover existing tasks, running operations, and pending questions before creating replacements after interruption or compaction. If the record cannot be recovered, report the limitation and reconstruct only the missing state from relevant evidence.

## One entry point, distinct responsibilities

Keep the accepted agreement, execution sequence, and progress distinct without requiring distinct files. Honor the user's or project's chosen location and format. A recoverable host artifact, task record, or conversation can be the entry point; use an existing project document when persistence, portability, or handoff requires it. Do not copy a native record into the repository merely to match a template. Create a document only for a concrete need not met by the existing record.

- **Specification:** expected behavior, accepted examples, preservation obligations, and decisions with their source. Distinguish accepted decisions, proposals, unresolved choices, and superseded directions. A draft's presence is not approval.
- **Plan:** ordered units referencing that contract, their dependencies, and expected completion checks. Keep live status in the chosen task record; link observed evidence there when supported, otherwise from the conversation. Do not maintain a second live copy. Use stable identifiers when other artifacts refer to a requirement, decision, or unit.
- **Continuation state:** where the work stands and the next authorized action. Link to the contract and evidence instead of copying them.

These roles may share one record. A transient checklist does not replace a behavioral contract needed by another session or tool; verify that the chosen location can preserve and expose the required content. A requested handoff may summarize progress as a dated snapshot linked to the task record, not a second live checklist. Label older records as history. An appendix must not silently override a section still presented as current.

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
