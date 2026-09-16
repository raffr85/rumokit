---
name: scope-product-increment
description: Use when defining or recommending an MVP, V1, first product increment, product boundary, or release order across materially different user or business outcomes; clarify any human-owned outcome priority before a preferred boundary or order.
---

# Scope a Product Increment

Own the boundary of the requested product increment. Research and technical design may support the decision, but they do not choose the product's purpose.

Honor the current stopping point. Do not produce a specification, plan, or implementation merely because it may follow later.

## Clear authority before commitment

Before selecting a preferred boundary or order, establish what settles the priority: an explicit user decision or sufficient delegated criteria, a source designated as authoritative by the user or project governance, or evidence that rules out every materially different outcome. Explain the decisive basis briefly in the recommendation; no fixed label or separate ceremony is needed.

A source is not authoritative merely because it was discovered, is detailed, is a ticket, or was included in a request to inspect the repository. Greater readiness, safety, speed, or simplicity does not eliminate alternative product outcomes. Do not ask the user to repeat a settled decision.

When materially different outcomes remain credible and priority is unresolved, compose `clarify-intent`. Return the conditional boundaries needed to explain the consequence, ask a neutral question, and stop before the dependent recommendation. A later question does not authorize an earlier commitment.

## Build the decision frame

Investigate enough to distinguish facts from choices. Identify every material outcome established by the request, accepted decisions, existing product behavior, and any outcome required for the result to remain coherent.

After the first evidence pass, inspect more evidence only when a named gap could settle the priority or eliminate an alternative. Otherwise, ask about the unresolved choice before another research wave or preferred boundary.

Before recommending a boundary or order, record for each outcome:

- its role in the first product;
- proposed treatment: include, stage activation, defer, or exclude;
- the consequence of that treatment.

Evidence may settle legality, impossibility, safety prerequisites, and technical dependencies. Maturity, lower blast radius, missing thresholds, or implementation cost can order work after the desired product outcome is known. They do not select which user or business outcome matters first.

A request for a recommendation delegates synthesis. It does not supply an unstated goal such as fastest delivery, broadest coverage, or highest commercial value.

Do not confuse implementation order with product priority. A foundation can ship first technically while a different operator-visible outcome defines the first coherent product. State both when they differ.

## Return the increment

When authority is resolved, return:

- the product outcome and boundary;
- included, staged, deferred, and excluded outcomes with reasons;
- technical prerequisites and implementation order, kept distinct from product priority;
- assumptions, evidence gaps, and the current stopping point.

When authority is unresolved, return the credible conditional boundaries and one neutral, consequence-bearing question through `clarify-intent`. Complete when the current product boundary is settled or the exact human decision blocking it is visible.
