---
name: debug-change
description: Use when diagnosing or fixing defects, regressions, failing tests, or unexpected runtime behavior.
---

# Debug a Change

Reproduce and localize the cause that owns the failure. Fix it only when the user requested a fix.

## Establish the symptom

Capture the exact observed and expected behavior, environment, revision, input, and boundary. Reproduce safely when possible. If reproduction is unavailable, say what substitute evidence is being used and lower confidence accordingly.

Trace from the symptom through executed code, state, data, configuration, and external dependencies. Compare a working case when useful. Do not start with a favorite explanation.

Before asking the user to repair authentication or configuration, check the failing invocation's execution context and available history of the same problem. An error from one CLI process does not establish account-wide state. Use `resume-work` when prior resolutions may apply; verify the relevant boundary without exposing credentials or changing global settings as a diagnostic shortcut.

## Narrow with discriminating evidence

Form the smallest current hypothesis and run the cheapest observation that could disprove it. Every retry should add information. Read callers and sibling paths before changing a shared function.

Before prescribing a correction, verify the causal premise that makes it appropriate. Bind explanatory source and configuration to the failing runtime's revision; unmatched local code is a candidate explanation, not proof of the live cause. Distinguish a directly observed fault from alternatives still compatible with the evidence. If a decisive check is unavailable or fails, keep the recommendation conditional and name the missing observation. A request for the fix does not confirm the hypothesis.

A fail-before test is valuable when it faithfully reproduces the defect and is cheap to retain. Do not force test-first when the failure lives in a surface the test cannot observe.

## Fix the owner when authorized

When a fix is requested, select repairs by their demonstrated connection to the requested outcome: correcting its cause, preserving behavior affected by that correction, or enabling its verification and delivery. Keep other defects as separate findings, even when real or inexpensive to fix. Investigate unresolved causal links before including their repairs. This permits deep, multi-component fixes; it does not limit the number of repositories. Avoid symptom suppression, duplicated guards, unrelated cleanup, and broad rewrites. Add `assess-blast-radius` when the owner is shared and `coordinate-change` when the cause crosses versioned components.

Changing the accepted behavior instead of restoring it is a product decision. Use `clarify-intent` if that choice is not already authorized; editing a specification or test expectation does not authorize it.

For diagnosis only, stop with the supported root cause and remaining uncertainty. When a fix changes shared state, concurrency, recovery, resource-sensitive processing, or a consumer contract, apply `review-change` to the resulting path before closing. Reuse an equivalent review of the same artifact; this can be inline and requires no separate approval or reviewer.

After a fix, apply `remove-slop` to the repair diff and `verify-change` to the original symptom, regression evidence, and relevant preservation checks. Reuse equivalent checks against that same diff. Use `finish-change` for a multi-component handoff or release-readiness claim. These support the current work without a separate approval or reporting phase. Lead the user-facing result with the original symptom's status, the changed components and why they were necessary, and what the checks actually exercised. Separate local evidence from unobserved integrated behavior; an attached report does not replace this explanation.
