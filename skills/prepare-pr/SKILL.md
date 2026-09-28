---
name: prepare-pr
description: Use when preparing, opening, or improving the reviewability of a pull request or merge request.
---

# Prepare a pull request

Deliver a reviewable change description and reviewer entry points. Create or update the remote request only when the user authorized that result. Preparation does not start ongoing monitoring.

## Establish the target

Follow `clarify-intent`, loading its body only if not already in context. Reuse the settled outcome and permissions. Resolve the repository, branch, comparison base, current head, and existing pull request through the available forge tools or CLI. Do not assume that the current directory or most recent PR is the target. Preserve draft status unless changing it is part of the request.

Inspect the actual diff, commit history, working-tree changes, repository contribution guidance, and current check results. Distinguish local work from the published head. For dependent PRs, use `coordinate-change` to identify the intended base and review order without rewriting the stack.

## Make the change reviewable

Explain the intended behavior and why it changes. Identify the files that carry the decision, distinguish mechanical or generated changes, and name compatibility, migration, or rollout constraints when relevant. For generated changes, identify the inputs and generation command, and state whether reproduction was verified. If that relationship is unavailable or unexplained, flag it for review rather than labeling the output harmless because it is generated.

Use the repository's PR template when present. Keep the description specific to the actual diff, with the checks performed on the named revision and their gaps. Separate expected behavior from behavior already implemented. A known defect remains visible even when the request only asks for preparation.

Prefer description and reviewer guidance when behavior must remain unchanged. Flag unrelated edits or a proposed split without dropping user work or silently changing the PR's scope. Use `review-change` for requested technical findings; preparing a description does not require another full review.

If history cleanup is authorized, use a clean isolated checkout or first preserve and account for staged, unstaged, and relevant untracked work. Capture the original head and tree, and verify content identity after a commit-only rewrite. Tree equality does not prove preservation of uncommitted work; check that state separately. A rebase onto changed content needs an explicit comparison of the intended change against the new base; tree equality alone is not applicable. Stop on unexplained differences. Rewriting history and force-pushing require their own authority and shared-branch checks.

## Return or publish the artifact

Return the title, description, and useful review order. If creation or update was requested, perform that authorized operation and confirm the resulting URL, target branches, and remote state. Reuse existing authorization rather than asking again. A prepared draft, an updated PR, passing checks, and merge readiness are distinct results. Do not merge or deploy as part of preparation.
