---
name: review-change
description: Use when asked to review a diff, branch, pull request, implementation, design, or plan, or when a change owner needs a focused technical review of a material risk.
---

# Review a Change

Find material defects and risks. When supporting authorized implementation, return findings to that owner, which retains its existing authority to fix them. When review itself is the requested result, do not modify the artifact unless fixes are also authorized. Neither mode requires another agent.

## Establish review scope

Identify the intended behavior and accepted examples from the user's request and decisions, comparison base, current artifact, relevant specification, and deployment or compatibility context. Separate agreed requirements from still-unconfirmed product assumptions. Inspect the actual diff and enough surrounding code to understand ownership and callers.

Use `assess-blast-radius` when a changed boundary may affect consumers not visible in the diff. Use `coordinate-change` for cross-repository contracts or release ordering.

## Hunt for consequential failures

Prioritize:

1. incorrect behavior, data loss, security or privacy failure;
2. broken state, concurrency, recovery, compatibility, or integration behavior;
3. missing or misleading validation on a material path;
4. unnecessary complexity and maintainability problems supported by the actual diff and callers.

Trace each candidate finding to executable behavior, a violated contract, or a credible concrete scenario. Check whether nearby code already handles it. Do not report personal style preferences, speculative architecture, or issues unrelated to the change.

For changed handlers and coordinating code, follow failure and cleanup paths as well as success. Check what happens to dependent or waiting work when an earlier operation fails: can it complete, fail, or be cancelled according to the contract? When context can change while work is pending, check that late errors remain attributable to the operation that produced them. Separate a broken guarantee from optional resilience that would require a new policy.

For changed collection-processing or resource-sensitive paths, trace the data through its actual readers and writers. Identify who owns each mutable value and where isolation is required. Check repeated copies, scans, sorts, queries, and serialization for work that can be removed without weakening that isolation or changing semantics. Prefer a direct data path over duplicating defensive work in every helper. Support a material cost claim with a representative measurement when available; a passing budget alone does not establish an efficient implementation.

Distinguish a capability that the artifact implements or deliberately preserves from one it merely mentions, considers, or postpones. Treat a material scope reduction without an accepted user decision as an outcome finding, even when the narrower artifact is internally coherent.

Do not rely only on tests, explanations, or expected values authored with the change; seek an independent requirement, caller, or observable when the finding depends on behavior.

For a changed contract, identify the previous behavior from the starting revision, an existing caller, or an accepted decision; then compare the final behavior and its authorization. Check changes to defaults, omissions, permissions, and errors where consumers depend on them. A consistent new code/test/spec trio can still contain an unapproved behavior change.

Apply `remove-slop` to the changed artifact within this review, reusing an equivalent check already completed. A supported simpler equivalent can justify a finding without inventing a future bug. Identify the unnecessary construct, its replacement or removal, and the behavior that must survive. Keep these findings below correctness and safety issues; a read-only review does not authorize cleanup edits.

## Report findings first

For each finding, give severity, precise location, triggering conditions, consequence, and supporting evidence. Keep the set deduplicated and ordered by impact.

Then list material assumptions or unresolved questions. If no actionable finding remains, say so and name the residual coverage gap. A clean review does not mean the change has been independently verified.
