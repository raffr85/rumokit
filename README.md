# RumoKit

[![Release](https://img.shields.io/github/v/release/raffr85/rumokit)](https://github.com/raffr85/rumokit/releases/latest)
[![Package checks](https://github.com/raffr85/rumokit/actions/workflows/package-checks.yml/badge.svg)](https://github.com/raffr85/rumokit/actions/workflows/package-checks.yml)
[![License](https://img.shields.io/github/license/raffr85/rumokit)](LICENSE)

Help your coding agent build what you actually meant.

RumoKit guides coding agents to clarify the intended outcome, carry out the work,
and verify the finished result against what you agreed. Its skills cover
product decisions, code exploration, implementation, debugging, review,
cross-repository changes, and pull-request delivery.

Specs, plans, TDD, and subagents are tools to use when the task needs them.
There is no required sequence of stages or fixed model choice. RumoKit uses
your agent's existing tools and permissions, with no extra runtime or telemetry.

## Install

Choose your coding agent. You do not need a RumoKit account or API key.

### Codex

```sh
codex plugin marketplace add raffr85/rumokit
codex plugin add rumokit@rumokit
```

The single plugin includes the skills and startup hook. Open `/hooks` in the
Codex CLI to review and trust the hook, then start a new task. No separate
adapter is needed.

### Devin CLI

```sh
devin plugins install --local raffr85/rumokit
```

Review the trust request, then start a new session. This installs for the current
user on this machine, without syncing the plugin to Devin Cloud.

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add raffr85/rumokit
/plugin install rumokit@rumokit
```

Follow Claude Code's trust prompts, then start a new session. A full behavioral
acceptance run on Claude Code has not been completed.

See the [installation guide](docs/INSTALL.md) for activation checks, updates,
removal, and other Agent Skills clients.

## Use it on your next task

With the startup hook active, describe the result you want:

> Add a waitlist to this workshop panel. Preserve existing registrations.

A missing product decision matters here: does a freed seat automatically confirm
the next person, or create an offer they must accept? RumoKit directs the agent
to ask about that choice before implementing it. It also directs the agent to
inspect facts it can find itself, instead of asking you to explain the codebase.

After you agree on the behavior, the work includes checking that registrations
survive the change and that interrupted requests do not lose a seat. This is
an illustrative example, not a quoted evaluation transcript.

You can also request a focused skill without starting the whole workflow:

| Task | Skill |
| --- | --- |
| Explain existing behavior without editing files | `understand-code` |
| Find where a change belongs | `locate-change` |
| Diagnose and fix a defect | `debug-change` |
| Coordinate a change across repositories | `coordinate-change` |
| Review a diff for supported findings | `review-change` |
| Prepare or open a reviewable pull request | `prepare-pr` |
| Assess or resolve existing review feedback | `address-review` |
| Diagnose or repair failed CI checks | `fix-ci` |
| Monitor or shepherd a pull request | `watch-pr` |
| Remove unnecessary code or prose | `remove-slop` |

Use your agent's skill picker or request the skill by name. Select `use-rumokit`
to start the router explicitly. The [full catalog](docs/DESIGN.md#catalog)
describes every skill. These are independent capabilities, not required stages.

## What RumoKit changes

- Clarification focuses on unresolved decisions that affect the result. Existing
  answers and authorization carry forward.
- The agent keeps the agreed outcome and constraints visible. A conversation can
  be enough; durable specs and plans are used when the work calls for them.
- Delegation follows the task and your preferences. Work can stay inline or use
  bounded subagents, including implementation across repositories.
- Verification checks the delivered behavior, not just whether tests pass.
  The handoff distinguishes completed work from missing evidence.

Keep the domain skills and tools you need. Choose one default workflow router
per task to avoid competing rules about approvals, planning, or delegation.
RumoKit supplies instructions, not enforcement or additional permissions.

## Evidence

The v1 skills passed a controlled workshop-waitlist acceptance case on Codex
with Astra and on Devin with Opus. Checks covered the product decision, existing
data, concurrency, interrupted requests, and the delivered browser interaction.

The [validation report](docs/VALIDATION.md) includes technical results, token
consumption, comparator details, and limitations. These are maintainer-reported
results from one known case, not a public reproducible benchmark or a guarantee
of savings on your tasks. RumoKit is actively evolving and still needs human
oversight. Later workflow changes have focused checks documented separately;
the original acceptance results do not validate those changes.

## Contribute

Rafael Affonso maintains RumoKit. Bug reports, documentation fixes, and
contributions are welcome. Read the [contribution guide](CONTRIBUTING.md),
[design](docs/DESIGN.md), [credits](CREDITS.md), and [security guidance](docs/SECURITY.md).

## License

[MIT](LICENSE). Copyright (c) 2026 Rafael Affonso.
Free to use, modify, and redistribute, including commercially, under the license terms.
