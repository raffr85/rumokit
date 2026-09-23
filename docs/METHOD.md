# Catalog method

RumoKit grows by distinct capability, not by lifecycle coverage, upstream imitation, or benchmark-specific patches.

## Keep or split a skill

Keep a skill separate when all four statements hold:

1. Users or the router can recognize its trigger.
2. Its result has a distinct completion condition.
3. It prevents a named failure that broader guidance does not handle well.
4. Hiding it inside another skill would make routing, stopping, or verification ambiguous.

Otherwise, keep the behavior inside its narrowest owner. Do not create a skill for generic competence, a one-off incident, or a rule that a deterministic check can enforce.

A local decision not to add machinery is not a standing constraint. Add or split a skill when the criteria above are met, including when one owner has become ambiguous enough that agents misroute or misapply it. Add a stage, hook, or runtime when the required behavior has a distinct boundary and advisory instructions cannot supply or verify it. Require evidence of that need; do not preserve an overloaded skill merely to minimize catalog size.

## Write the skill

- Put only triggering conditions in the frontmatter description.
- State the owned result and stopping point near the top.
- Investigate facts before asking the user.
- Use conditions tied to observable task properties. Avoid universal rituals with exemption lists.
- Keep the common path in `SKILL.md`. Add a reference or asset only when the main path does not need it.
- When a decision rule moves to another skill, identify every owner that needs it and make the required or conditional dependency explicit. Check direct invocation as well as router entry; a rule that stays unloaded cannot guide the task. Clarification is required for new requested results, not conditional on the agent already noticing ambiguity.
- Keep host tool names, model slugs, and subagent syntax outside the portable core.
- Preserve user authority. Guidance never grants permission for another action.
- Keep the owner's response-relevance pass inline. Implementation, fixes, refactoring and review use `remove-slop` on the changed artifact, reusing an equivalent check; explicit cleanup remains a direct capability. Do not load it for every progress message. Neither mechanism can narrow required outcomes, erase meaningful caveats, or clean an unresolved decision into an assumption.

## Reuse a prior failure without overfitting

A failure can justify a capability hypothesis. It cannot write a benchmark-specific rule.

Ask:

- What general decision failed?
- Which observable condition should change the behavior?
- In which unrelated task would the same condition appear?
- What harm would the rule cause when that condition is absent?

Keep the original case as a regression. Do not optimize for its exact files, diff size, test count, token budget, or execution topology.

## Separate construction from efficacy

Construction checks can establish:

- valid manifests and skill metadata;
- resolvable references and assets;
- concise, discriminating descriptions;
- public and private repository separation;
- absence of placeholders and stale skill names.

Construction checks cannot establish routing reliability, instruction compliance, software quality, lower cost, or cross-host portability.

When a product claim needs evaluation, compare the complete relevant framework with a matched control on the same starting artifact. Keep original prompts intact. Judge the resulting software with independent semantic evidence and human review. Treat trigger, delivery, behavior, outcome, calibration, and cost as separate results.

Establish a minimum outcome contract before comparing efficiency. A candidate that produces a narrower, partial, or different result may have lower raw consumption, but cost per equivalent outcome is not established. Report its cost separately and classify the comparison as unmatched.

Track elicitation as behavior of its own: whether a material human choice was surfaced before commitment, whether the question changed the result, whether avoidable questions were asked, and whether an unstated assumption narrowed the outcome. Do not reward either constant questioning or silent conservatism.

Let each candidate reach its natural in-scope stopping point before adjudication. A failed quality gate is a result to record, not a reason to discard or interrupt useful work. Preserve and compare the best complete artifact even when it misses the oracle; it may still reveal a better approach than the reference. Stop early only for contamination, unsafe or unauthorized action, destructive divergence, a hard resource limit, or a genuine blocker.

If the oracle expects an artifact outside the prompt's current temporal scope, record an oracle mismatch. Do not count that mismatch as candidate failure.

Keep pre-registered protocols and rubrics frozen. If semantic review exposes a measurement flaw, record a post-hoc diagnostic correction and version the repaired oracle for the next run rather than rewriting the historical test.

## Change or remove behavior

Update a skill when real use exposes a reusable decision failure. Split one when two triggers or stopping points conflict. Merge skills when they repeatedly activate together and one result subsumes the other.

Disable or remove behavior when it displaces a better native strategy, adds ceremony without outcome value, raises false refusals, depends on an unavailable host capability, or duplicates a cheaper mechanism.

The total number of skills is not a success metric. Neither minimization nor expansion is a goal: the active set should contain every capability with a concrete, distinct job and no capability without one.
