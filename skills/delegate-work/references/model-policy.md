# Delegation role policy

RumoKit defines portable roles, not provider-specific model names:

- **explorer:** maps evidence, alternatives, or unknowns without changing shared state;
- **implementer:** produces a bounded change in isolated writable state;
- **reviewer:** independently challenges an artifact and returns supported findings;
- **integrator:** reconciles compatible units when explicitly assigned by the primary owner.

Resolve delegation mode, role configuration, reasoning, and budget from:

1. an explicit user choice, including inline-only or a permitted fallback;
2. an accepted project or host policy;
3. the current host's inherited default.

Reuse preferences already established in the conversation or applicable configuration. Do not ask the user to select models or approve each worker again. Without a stated preference, choose inline or delegation by the skill's separability and value criteria, inheriting the host default for workers. This is an operational default, not a claim that the user chose it.

Before the first delegation, briefly state the units and reason, the requested model/reasoning or inherited default, and the source of that choice. Ask only when a material cost or quality tradeoff lacks governing criteria, a spending limit needs changing, or an explicit configuration is unavailable without an authorized fallback. Explain the concrete choice; continue independent authorized work while it is unresolved. Reopen preferences only when the choice materially changes. Do not persist a new profile or change global settings without a request.

The host adapter maps roles to available capabilities. Check whether model and reasoning controls actually exist and accept the chosen values; do not invent unsupported arguments or silently substitute for a binding choice. If optional overrides are unavailable, inherit the host default and disclose that limit. Record requested configuration and observable execution identity separately. A prompt label, transcript claim, or worker self-report is not provider attestation.

Use different models or reasoning settings only for a concrete benefit such as complementary tool access, cost, latency, or an independent review perspective. Heterogeneity and fan-out are options, not quality guarantees.
