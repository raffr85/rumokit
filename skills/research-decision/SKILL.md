---
name: research-decision
description: Use when researching external evidence, current practice, or alternatives for a software decision.
---

# Research a Decision

Produce decision-ready evidence. Do not own product priority or an increment boundary.

Honor temporal scope. If evidence is the current result and a later artifact is deferred, stop at research. If the current result includes an MVP, V1, first increment, product boundary, or release order, return evidence to `scope-product-increment`. If another downstream artifact is current, return evidence to that artifact's owner.

## Frame the question

State the decision, the material unknowns, and what evidence would change the answer. Inspect relevant local code first when system fit matters. For a broad applicability question, examine credible uses and alternatives before choosing one to prototype. Explain which part of the decision the selected case can answer; a convenient narrow test must not silently replace the broader question. Honor an explicitly bounded experiment instead of expanding it into a survey.

Prefer primary sources: official documentation, standards, original research, source code, and authoritative operational records. Use secondary sources to discover or contrast.

## Separate evidence from authority

Research establishes feasibility, maturity, risk, uncertainty, and contradictions. It may eliminate an option when evidence makes it illegal, impossible, unsafe, or irrelevant. It does not convert technical readiness into product priority. Keep unresolved authority visible to the owner instead of selecting the most mature or conservative outcome.

## Reuse evidence

Keep a compact ledger of the decision gap, source or artifact identity, result, and freshness. When source freshness matters, establish repository and revision identity once and reuse it. Repeat a large read, repository inventory, remote check, or failed prerequisite only after a relevant state change, contradictory evidence, or a named gap that the repeat can resolve.

## Investigate proportionally

- Search competing explanations, not only confirmation of the leading idea.
- Record source date, scope, and applicability when they matter.
- Distinguish a documented fact from an inference and a recommendation. Limit conclusions to what the source or experiment observed, including when a narrow hypothesis fails.
- Surface contradictions instead of averaging them away.
- Stop when another search is unlikely to alter the material conclusion.

Do not default to parallel researchers or exhaustive surveys. Use `delegate-work` only for independent research units.

Before another search or delegation wave, name the decision gap, evidence sought, and how plausible results could change the conclusion. Otherwise synthesize.

After a compaction that leaves research work open, use `resume-work` before searching, delegating, or changing a conclusion.

Keep private URLs, hostnames, identifiers, and content within trusted local or approved connectors. Sanitize public-web queries.

When an accepted correction replaces a direction, invalidate its dependent recommendations, rollout gates, and next-artifact guidance.

## Return a decision packet

Include:

- the question and constraints;
- sourced findings and competing options;
- contradictions, gaps, and what evidence supports, rejects, or leaves unresolved;
- decision-relevant implications without silently choosing a human-owned outcome;
- the next decision required from the owner or user.
