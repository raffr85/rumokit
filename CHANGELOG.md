# Changes

## 2.1.0

- Teach `verify-change` to reuse sufficient tests and protect distinct failures that the existing suite would miss.
- Capture a short intent receipt before implementing material behavior. At
  delivery, compare the agreement with the checked revision and show any
  mismatch or gap in the same conversation.
- Ask which behavior to implement when two outcomes fit the request and the
  choice belongs to the user. A settled or delegated decision can proceed.
- Check which existing rules survive a spec revision. For consequential
  handoffs, test whether the next implementer can use the artifact by itself.
- Compare a PR finding with behavior on the base revision, including defects
  exposed by new callers of unchanged code.
- Shorten the startup router. Recover incomplete skill reads, check relevant
  alternative evidence when a source is unavailable, and continue authorized work.
- Add reproducible, synthetic review, handoff, repair and product-decision
  exercises. See the [validation results](docs/VALIDATION.md).

## 2.0.0

- Use available native task tools without a parallel `todo.md`. Keep tracking
  inline when those tools are unavailable; task files require a user request or
  established project convention. Recover existing tasks after interruption.
- Make specification and plan templates content shapes rather than file
  creation instructions. Separate accepted requirements, planned checks, and
  observed progress, and reference the chosen task record without live mirrors.
- Rename the public `remove-slop` skill to `reduce-complexity`. Update discovery,
  callers, and documentation without changing its procedure or adding an alias.
  Existing explicit invocations need the new name after installation. This
  identifier change makes the release incompatible with those invocations.
- Shorten acknowledgments to general study references rather than mapping each
  capability to another project's vocabulary.
- Add independent `resolve-product-decisions`, `model-domain`, `check-agreement`, and
  `write-clearly` capabilities, with condition-specific automatic activation.
  Separate product interviewing, domain modeling, agreement reconciliation,
  and readable communication from the existing clarification and cleanup owners.
- Compare material proposed effects with the accepted agreement before
  implementation and worker integration, after conflicting recovery, and at
  delivery. Preserve delegated technical choices and necessary new mechanisms.
- Make plans carry decision-rich interfaces, failure checks, and independently
  verifiable units without transcribing implementation or forcing a tracker.
- Reconcile worker lifetimes and reuse current evidence and pending reviews on
  resumption. Report competing mandatory routers rather than silently stacking
  their processes or changing active installations.

Publishing this release does not update active installations.
The catalog has no fixed size or prohibition on new skills and triggers.

## 1.1.0

- Add independent skills for PR preparation, review-feedback resolution, CI
  diagnosis and repair, and requested PR monitoring. Preserve existing authority
  and distinguish local work, publication, checks, readiness, and merge.
- Shorten catalog descriptions and clarify routing between a fresh review,
  existing feedback, readiness, and ongoing monitoring.
- Load specialized state and recovery verification from a conditional reference,
  preserving its requirements. Keep common evidence rules in the entry point.
- Maintain existing project verification instructions, identify the intended
  running instance, and preserve evidence and unrelated resources during cleanup.
- Check catalog and resource integrity without fixing the total skill count.

Structural checks and bounded decision exercises do not establish comparative
efficiency or end-to-end forge integration. Publishing this release does not
update active installations.

## 1.0.6

- Check proposed mechanisms against required behavior and existing capabilities
  before carrying them into a specification, plan, or estimate.
- Compose anti-slop within design, specification, and planning. Preserve accepted
  obligations while questioning unsupported mechanisms and duplicate rules.
- Carry user constraints and corrections into the recommendation, distinguish
  illustrative examples from requirements, and explain the concrete result in chat.
- Keep required protections and capabilities. No new skills, hooks, workflow
  stages, model-specific rules, or runtime dependencies.
- Summarize validation evidence without changing historical results or their
  limits. Clarify the legacy adapter's migration instructions and allow reviewed
  synthetic public scenarios while excluding private task material.

## 1.0.5

- Separate broad investigation from the authorized repair scope, including
  worker assignments and selection of returned patches.
- Include changes needed for the requested result and compatibility, without
  treating discovered defects or a dependency inventory as an implementation list.
- Explain the original symptom's status and verification limits in the response,
  not only in an attached report. No skills, hooks, or workflow stages were added.
- Restore an explicit search-and-reuse decision before adding implementation.
  Connect the existing anti-slop skill to implementation and review, sharing its
  criteria and preservation rules instead of requiring a separate cleanup request.

## 1.0.4

- Bind source and tool selection to the current task. Keep other sessions'
  requests and approvals separate, including handoffs from the same repository.
- Re-establish the target after a user correction before continuing dependent
  searches or tool actions. Preserve explicitly requested cross-session work.
- Keep causal repairs conditional until their decisive evidence is available,
  and distinguish local source from the revision producing the live failure.

Both 1.0.3 and the changed instructions recovered the corrected target in the
two paired Sol/xhigh scenarios. These checks did not reproduce the desktop
failure or establish a reliability gain. See `docs/VALIDATION.md` for the limits.

## 1.0.3

- Share a small durable-state contract across specification, planning,
  implementation, handoff, and resumption. Preserve existing project conventions
  and keep current state distinct from historical decisions.
- Add decision authority, observed unit status, and continuation fields to the
  existing templates without requiring a new document or approval stage.
- Resume from the task entry point and artifact evidence, reconcile in-flight
  work, and update current summaries when accepted directions change.

The bounded documentation handoff check and its limits are recorded in
`docs/VALIDATION.md`. Publishing this release does not update active installations.

## 1.0.2

- Resolve material intent uncovered during preparation instead of substituting
  an open-decisions list for clarification; preserve inventory-only requests.
- Distinguish executable plans from conditional maps and create a behavioral
  contract when shared behavior requires one, without a mandatory artifact chain.
- Keep proposed business behavior distinct from accepted scope inside a design,
  including effects on existing state and activation timing.
- Ground correction recommendations in actual callers, committed effects, and
  consumer outcomes; recover known environment resolutions before asking for
  authentication or configuration changes.
- Remove rejected agent-added mechanisms along with their prose, and keep broad
  research questions distinct from the narrow experiments used to investigate them.
- Bound worker context and assignments, retain owner responsibility for exposed
  decisions, and account for delegated work in cost comparisons.

These instruction changes do not establish improved comparative efficiency.
See `docs/VALIDATION.md` for the checks and their limits. Updating the source or
publishing this release does not update active installations.

## 1.0.1

- Install the skills and startup hook together as one `rumokit` plugin in Codex.
  Remove the root Agent Plugins manifest that made Codex 0.153.1 skip the hook.
  Keep the native Codex and Claude-compatible manifests and all 22 skills.
- Reuse the existing startup hook across Codex, Devin, and Claude Code. Retain the
  separate Codex adapter only for legacy installations.
- Rewrite the README around installation, first use, and the intended result.
  Add release, license, and live package-check badges.
- Add the native Claude Code marketplace and document direct GitHub installation
  for Devin, so neither requires a manual clone for normal installation.
- Check packaging and hook behavior on Linux and macOS in GitHub Actions.
- Leave workflow instructions and the published 1.0.0 acceptance results unchanged.

## 1.0.0

- License the core and the separately packaged Codex adapter under MIT,
  copyright 2026 Rafael Affonso.
- Add public-facing documentation, installation instructions, contribution
  guidance, and credits. Keep research influences separate from measured results.
- Align the package descriptions and author metadata with the public release.
- Promote the accepted rc.1 skill and hook contents without behavioral changes.
- Pass the defined clarification, product, technical, own-verification and
  native-activation acceptance boundaries on Codex/Astra and Devin/Opus.
- Record measured consumption and comparator limitations in `docs/VALIDATION.md`.
- Publishing this release does not install or upgrade user configurations.

## 1.0.0-rc.1

- Make instruction loading explicit: a selected skill must have its full body in
  context. A catalog name, description, or announcement is not a loaded skill.
- Reuse the complete router when the host already supplied it at startup; do
  not invoke it again only to obtain the same instructions.
- On direct implementation entry, load clarification and verification when
  their decisions are needed, while reusing already loaded instructions.
- Preserve the existing verification contract and conditional delegation,
  specification, planning, review, and focused skill entry points.
- Document the observed Devin installation path and its isolation limitation.

Package checks alone do not establish behavioral acceptance or comparative
efficiency. No active user installation is upgraded by editing this source.

## 0.2.0-alpha.24

- Rename Steelman to RumoKit without changing the portable workflow contracts.
- Use package IDs `rumokit` and `rumokit-codex`, router `use-rumokit`, and adapter
  directory `adapters/rumokit-codex`.
- Retain historical evaluation artifacts under their original identities.
