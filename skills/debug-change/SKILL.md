---
name: debug-change
description: Use when the requested result is to diagnose or fix a defect, regression, failing test, unexpected runtime behavior, or unexplained discrepancy at its root cause.
---

# Debug a Change

Reproduce and localize the cause that owns the failure. Fix it only when the user requested a fix.

## Establish the symptom

Capture the exact observed and expected behavior, environment, revision, input, and boundary. Reproduce safely when possible. If reproduction is unavailable, say what substitute evidence is being used and lower confidence accordingly.

Trace from the symptom through executed code, state, data, configuration, and external dependencies. Compare a working case when useful. Do not start with a favorite explanation.

Before asking the user to repair authentication or configuration, check the failing invocation's execution context and available history of the same problem. An error from one CLI process does not establish account-wide state. Use `resume-work` when prior resolutions may apply; verify the relevant boundary without exposing credentials or changing global settings as a diagnostic shortcut.

## Narrow with discriminating evidence

Form the smallest current hypothesis and run the cheapest observation that could disprove it. Every retry should add information. Read callers and sibling paths before changing a shared function.

A fail-before test is valuable when it faithfully reproduces the defect and is cheap to retain. Do not force test-first when the failure lives in a surface the test cannot observe.

## Fix the owner when authorized

When a fix is requested, change the boundary responsible for the invalid state or behavior. Avoid symptom suppression, duplicated guards, unrelated cleanup, and broad rewrites. Add `assess-blast-radius` when the owner is shared and `coordinate-change` when the cause crosses versioned components.

Changing the accepted behavior instead of restoring it is a product decision. Use `clarify-intent` if that choice is not already authorized; editing a specification or test expectation does not authorize it.

For diagnosis only, stop with the supported root cause and remaining uncertainty. When a fix changes shared state, concurrency, recovery, resource-sensitive processing, or a consumer contract, apply `review-change` to the resulting path before closing. Reuse an equivalent review of the same artifact; this can be inline and requires no separate approval or reviewer.

After a fix, apply `verify-change` to the original symptom, regression evidence, and relevant preservation checks. Use `finish-change` for a multi-component handoff or release-readiness claim. These support the current work without a separate approval or reporting phase. Report why the fix addresses the cause and what behavior was verified.
