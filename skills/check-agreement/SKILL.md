---
name: check-agreement
description: Use before a material change in scope or effects, after conflicting handoffs, or when checking delivery against the accepted outcome.
---

# Check the Agreement

Compare proposed or delivered behavior with the agreement that governs this task. Support the current owner; an explicit conformity review owns the comparison. This check is advisory, not an authorization service or a reason to create another file.

## Reconcile the change

Start with the intent receipt from this task, usually the earlier write-back in the same conversation. Follow an existing spec or task reference when it carries the agreement. Use the latest authorized change to each affected decision. If no prior receipt exists, identify the original request or decision you recovered and say when the comparison is retrospective. If the source is missing, leave its authority unconfirmed.

For each material changed outcome or effect, identify:

- what the agreement requires or forbids, and its source;
- what the proposal or actual artifact changes, including additional effects;
- the decision or delegated criteria that cover that change;
- the preserved behavior and evidence still needed.

Inspect actual diffs and execution state for delivered work. Keep worker-only output, uninspected artifacts, and unavailable evidence distinct from integrated or verified behavior. Group by consequential outcome, not every line of code.

At delivery, close the receipt in the normal reply. Identify the artifact actually checked (commit or PR head, or the relevant worktree contents for uncommitted work). For each material promise, pair the agreed example or requirement with the observed result and the check that produced it. Group items that share evidence. State which were supported, contradicted, or left unverified. Inspect the reverse direction too: flag material effects in the diff that the agreement does not cover. An open product choice stays open even if the implementation behaves consistently.

Keep the comparison as short as the decision allows. For example, “You asked for input order. On this checkout the public API returned [B, A] for [B, A].” A passing suite needs an observation that would distinguish the wrong behavior before it supports that claim. If the agreement or artifact changes, refresh only affected conclusions. When the task uses a handoff record, leave the result or a usable evidence reference there. A receipt records evidence within the checked boundary; it grants no release authority.

Before introducing shared persistence, financial or permission policy, or a new operational dependency, explain the unmet requirement, adequate existing alternatives, and the proposed effect on constraints, failure, and operating cost. A new mechanism is not automatically wrong; technical necessity is not automatically permission to change the agreed behavior.

## Return the disposition

Classify each material difference as aligned, unresolved, or conflicting. Mark evidence gaps separately. Continue aligned work under existing authority. Before a dependent commitment to an unresolved outcome, load and follow [clarify-intent](../clarify-intent/SKILL.md), reusing its full body when already loaded. Exclude a rejected or unrelated mechanism; do not ask for approval again or carry it into a plan because a worker already built it.

Apply this comparison before a newly exposed material commitment, when integrating worker changes, after a conflicting recovery, and before claiming delivery fit. Reuse a valid comparison of unchanged decisions and artifacts. Ordinary edits already covered by the agreement need no repeated approval or comparison report.

Return the differences, disposition, and next authorized action. For a user-facing comparison, load and follow [write-clearly](../write-clearly/SKILL.md), reusing its full body when already loaded. If the user changes the agreement, update its dependent plans and checks; do not rewrite expectations to make the implementation pass.
