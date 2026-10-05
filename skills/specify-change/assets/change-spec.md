# Change specification

Use this shape in the chosen host artifact, conversation, or required project document. Omit sections that add no decision-relevant content. This template does not request a new file.

## Outcome and boundaries

Explain what changes, for whom, why, and what stays outside the change. Give the reader a short standalone summary before technical detail.

## Agreement and starting evidence

Identify the accepted record, current revision or last reconciliation, and any related plan. Link the verified behavior and constraints needed to understand this change. Follow the project's language and naming conventions.

State settled product and technical choices with their authority and the concrete user example. Distinguish accepted decisions, proposals, assumptions, and unresolved choices; the presence of a draft is not approval. When replacing a decision, mark the superseded direction and update its dependents. Use identifiers only when other records refer to them.

## Behavior and acceptance

Describe actors, inputs, outputs, states, transitions, invariants, and interfaces where needed. Separate required behavior from proposed mechanisms. For material additions, identify the guarantee supplied and the gap in existing capabilities.

For representative cases, state the situation, expected behavior, forbidden effect, and authoritative observation that would demonstrate compliance. These are expectations, not executed checks. Link observed results from the task record instead of copying them into the contract.

## Preservation and failure behavior

State what must remain true and what must never happen. Cover relevant errors, retries, concurrency, recovery, migration, and mixed-version behavior. Keep optional improvements outside the required contract.

## Open decisions

Record only material unresolved choices, their owner, and their consequence.
