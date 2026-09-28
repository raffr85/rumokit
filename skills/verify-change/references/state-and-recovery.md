# State and recovery checks

Use this reference when correctness depends on state, time, retries, interacting rules, asynchronous work, or a changing UI context. Keep the accepted outcome and evidence boundaries established by `verify-change`.

## Exercise the material combination

When behavior depends on state, time, retries, or interacting rules, check their combination rather than each rule only in isolation:

1. Derive a material invariant from the accepted outcome: what must remain true, and under which conditions? Set the expected result independently of the implementation's formulas or helpers.
2. Construct a short sequence that could violate it. Select a relevant transition, boundary, interruption, or repeated action; check the result on both sides of that change. Include interacting rules that could change the answer, not every imaginable combination.
3. Execute the sequence and inspect its user-visible consequences, not only an intermediate value. For example, a cancelled reservation releasing capacity also needs to stop occupying the availability shown to the next customer.

## Locate the authoritative effect

For asynchronous or shared-state behavior, distinguish input capture, the authoritative effect, completion reported to the caller, and observation by a consumer. Verify the guarantee at the boundary that owns it; these moments need not coincide. When an intervening change can alter correctness, exercise the relevant ordering on either side of that effect: work not yet applied, versus work applied but its response delayed or lost. A gate after forwarding a request may delay only delivery; establish which boundary the test actually controls. Use observable milestones or explicit gates, not a sleep assumed to place the operation at that boundary.

## Check the current consumer

For stateful interfaces, choose a consequential item, actor, or view change during that sequence. After outstanding work resolves, check both authoritative state and the current consumer's state, actions, and feedback against the accepted consistency contract. Retained input and late responses must belong to the intended item, actor, and revision; ignoring an obsolete response alone does not prove that the current view is correct. Do not expand this into every possible ordering or an exhaustive UI matrix.

## Follow recovery to its result

Wait for the relevant outcome, including an expected rejection, cancellation, or failure, before asserting its consequences. A lost response does not establish that an effect failed. When recovery is part of the accepted behavior, exercise the relevant failure, restore the dependency, and follow the accepted recovery path to its resulting effect. If that path includes a user action, perform it and check usable controls or feedback, not only that the error disappeared. The path may require retry or reload; do not silently require automatic recovery. Absence of automatic retry does not establish retry safety. Recovery evidence transfers only to operations with equivalent guarantees. To infer absence of data, first confirm a successful completed load; an empty screen during loading or after a failed request proves no such absence.
