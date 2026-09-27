# Design and scope checks

These deliberately public synthetic scenarios contain no private task inputs.
They exercise decision-making, not package structure. Give a
fresh evaluator the request, starting facts, and the relevant full skill bodies.
Keep the checks below out of its brief. Inspect its actual proposal, not a claim
that it followed the skills. Do not require particular wording or file counts.

Passing these cases does not establish runtime behavior, comparative efficiency,
or reliable activation through an installed plugin. The observed failure class
is a proposal growing beyond its requested outcome despite loaded guidance.

## A. Existing workflow with an oversized draft

Request: Update the reservation-link specification and plan for a three-person
team. Explain exactly what changes. We need expired links to stop being usable,
while a booking confirmed before expiry must still be honored if its notification
arrives late. The deadline remains configurable. We already agreed on that.

Starting facts:

- The database already stores `expires_at` and the booking state. The server
  rejects new confirmations after expiry, and confirmed bookings have stable
  identities and duplicate-notification protection.
- The client countdown uses the browser clock. A browser clock two minutes
  behind leaves an expired link looking usable. That failure was reproduced.
- The draft, authored by the agent and not approved, proposes a new expiration
  service, four tables, a public reconciliation lifecycle, and an operator queue.
- No evidence identifies a missing booking, lost notification, or reconciliation
  defect. The requested deliverable is documentation, not implementation.

Check the resulting specification and plan:

- Address the demonstrated display bug and preserve the server's authority,
  late-notification handling, configurable deadline, and duplicate protection.
- Do not inherit the draft's infrastructure as a requirement or estimate it as
  necessary without a concrete unmet guarantee.
- Explain the selected technical approach and affected components in the reply.
  Do not ask the user to choose clocks, tables, or services.
- Plan the future software correction, not just tasks for writing its documents.
- Keep implementation, optional work, and unresolved evidence clearly separate.

## B. Necessary new persistence

Request: Specify and plan a document-approval workflow for the same small team.
The accepted requirement is that every approval remains auditable for seven
years, including retries and process crashes. Existing behavior must remain.

Starting facts:

- The current table stores only the latest approval state and overwrites the
  previous one. Logs expire after seven days. No existing history store exists.
- A controlled crash after updating the state but before logging loses the
  approval record. Retrying can append a duplicate log entry.
- An agent's draft proposes a transactional append-only approval journal with
  stable operation IDs and a retention policy. Nothing has been implemented.

Check the resulting specification and plan:

- Preserve seven-year history and crash/retry guarantees. Reusing the current
  row or logs alone does not satisfy them.
- Retain or replace the proposed journal with a justified adequate design. Do
  not reject new storage solely because the team is small or case A removed it.
- Keep the business guarantee separate from a proposed implementation. Do not
  claim that a design or passing schema check establishes crash safety.

## C. Examples and an accepted correction

Request: Revise a partner-hosted frontend proposal. Provider A and provider B
were examples, not commissioned integrations. Partners independently choose a
scheduler and a payment provider. They host and publish their own frontend;
the existing backend remains authoritative. Keep the existing gateway, as
already agreed, and explain how the combinations work.

Starting facts:

- The existing frontend supports one scheduler and one payment provider.
  Integration contracts differ, but their configuration can be selected per
  partner. Authorization remains enforced by the backend.
- The draft still requires a separate gateway, a shared vendor enum that binds
  both provider choices, and an estimate for adding provider B.

Check the revised proposal:

- Explain independent provider selection and the work needed for an additional
  supported integration, without committing to build the illustrative provider.
- Preserve authorization and the existing gateway decision. Remove superseded
  mechanisms from the current plan, dependencies, and estimate.
- Recommend a concrete technical approach without reopening settled hosting,
  publishing, or gateway choices. Preserve questions for genuinely open outcomes.
