# RumoKit

Help your coding agent build what you actually meant.

RumoKit is a portable workflow plugin for coding agents. It helps the agent
clarify your intended outcome, choose the work the task needs, and check the
finished result against what you agreed.

It provides 22 focused skills for understanding code, product decisions,
implementation, debugging, review, verification, and coordinated changes.
The workflow selects relevant skills instead of loading the entire catalog.
You can also invoke a focused skill directly.

Specs, plans, TDD, and subagents are conditional tools, not a mandatory pipeline.
RumoKit uses your chosen host, tools, permissions, and model preferences.
It adds no daemon, MCP server, telemetry, or separate agent runtime.

## What this looks like

Suppose you ask: "Add a waitlist when a workshop is full."

Working code can still implement the wrong product decision. Should the next
person receive a confirmed seat, or an offer they must accept? RumoKit directs
the agent to inspect the existing behavior, ask you about that unresolved
decision, implement the agreed behavior, and verify the final interaction,
including recovery from an interrupted request.

This illustrates the workflow; it is not a quoted transcript. Clarification
does not mean repeating questions you have answered or asking you for facts the
agent can inspect.

## Install

Download a [release](https://github.com/raffr85/rumokit/releases) or clone the source,
then follow the [installation guide](docs/INSTALL.md)
for your host. The core contains the same skills across hosts. Codex uses an
additional bootstrap adapter.

| Host | v1 status | Setup |
|---|---|---|
| Codex CLI 0.153.1, Astra medium | Passed the defined acceptance case | Core plus the trusted Codex adapter |
| Devin CLI 3000.10.27, Opus 5 medium | Passed the defined acceptance case | Root plugin |
| Claude Code | Compatible package layout; no completed Claude acceptance case | Root plugin |
| Other Agent Skills clients | Portable format; behavior not validated | Native skill discovery |

Portability means the same workflow principles can be used across hosts.
It does not promise equal performance from every model or client.

## Use

With the bootstrap active, describe the result you want in your own words:

> Add a waitlist to this workshop panel. Preserve existing registrations and
> clarify unresolved product decisions before implementing them.

Focused skills also work independently. Ask your host to use the named skill:

- `understand-code`: explain how a feature works without changing it.
- `locate-change`: find where a proposed change belongs and what it affects.
- `debug-change`: reproduce a failure, trace its cause, and verify the fix.
- `remove-slop`: clean an existing artifact while preserving its behavior or meaning.
- `review-change`: review a change and return findings supported by evidence.

The [full catalog](docs/DESIGN.md#catalog) includes product scoping, research,
design, specifications, plans, implementation, and cross-repository coordination.
See the install guide for host-specific invocation and activation checks.

## How the workflow adapts

The router, `use-rumokit`, establishes the intended result and selects the skill
responsible for delivering it. Supporting skills are added for specific work.
A direct skill invocation keeps its own scope rather than starting a new pipeline.

The working agreement records what success means, which decisions you accepted,
and what must remain unchanged. It can stay in the conversation. Specs and plans
are used when requested or needed for decisions, dependencies, risk, or handoff;
they do not create extra approval stages.

Work can stay inline or use bounded subagents, including for implementation
across repositories. Your explicit preferences take priority over project policy
and host defaults. RumoKit does not select a fixed model or reasoning level.
See [delegation preferences](skills/delegate-work/SKILL.md).

Verification checks the final artifact against the agreed outcome. Passing tests
alone does not establish that the right product was built. Missing evidence and
unfinished behavior must remain visible in the handoff.

Keep domain skills and tools you need. Use one default workflow router per task
to avoid competing instructions about planning, approvals, tests, or delegation.
RumoKit provides guidance, not enforcement or additional permissions.

## Validation

Version 1.0.0 passed a controlled acceptance case on Codex and Devin. The case
evaluated clarification, agreed product behavior, preservation of existing data,
concurrency, interrupted requests, and the delivered browser interaction.

The [validation report](docs/VALIDATION.md) includes consumption, comparator
results, and limitations. These are maintainer-reported results from one known
case, not a public reproducible benchmark, a universal saving, or a SOTA claim.
RumoKit does not guarantee that generated software is correct or production-ready.

## Contribute and learn more

Rafael Affonso maintains RumoKit. Everyone is welcome to use, adapt, and contribute
to it. See [contribution guidelines](CONTRIBUTING.md), [credits](CREDITS.md),
[design](docs/DESIGN.md), and the [trust model](docs/SECURITY.md).

*Rumo* is Portuguese for direction. The project was developed as Steelman;
[existing installations need an explicit migration](docs/INSTALL.md#migrate-from-steelman).

## License

[MIT](LICENSE). Copyright (c) 2026 Rafael Affonso.

You may use, modify, and redistribute RumoKit, including commercially, under the
license terms. Keep the copyright and permission notice with copies or substantial
portions of the software. The software is provided without warranty.
