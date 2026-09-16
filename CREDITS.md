# Credits

RumoKit is maintained by Rafael Affonso and licensed under [MIT](LICENSE).
Its design draws on the projects and research below. These acknowledgments
describe influences, not affiliations, endorsements, or dependencies you must install.
Linked projects retain their own licenses.

## Workflow influences

- [Superpowers](https://github.com/obra/superpowers), by Jesse Vincent: discoverable
  workflows, focused skills, progressive loading, and verification before completion.
- [pstack](https://github.com/cursor/plugins/tree/main/pstack), by Lauren Tan:
  task-specific workflows, explicit delegation preferences, root-cause analysis,
  and project-specific verification. The
  [pstack-claude port](https://github.com/michael-denyer/pstack-claude), by Michael
  Denyer, was also a reference and the source of the comparison stack.
- [Matt Pocock's skills](https://github.com/mattpocock/skills): investigating facts,
  eliciting human decisions, and separating research, specification, planning,
  and implementation outputs.
- [Ponytail](https://github.com/DietrichGebert/ponytail), by DietrichGebert:
  understanding existing work, searching for reuse, and simplifying without
  removing necessary behavior or safety checks.
- OpenAI's Codex Security and Product Design plugins: separating routing from
  focused work and checking an artifact against its authoritative target.
  Their proprietary contents are not included or relicensed by RumoKit.

RumoKit combines these influences into task-adaptive instructions. It does not
require their original workflows, approval stages, or model choices.

## Formats

The instructions use [Agent Skills](https://agentskills.io/specification).
Native Codex and Claude-compatible manifests connect the same skills and startup
hook to supported clients. The earlier package also used the
[Agent Plugins](https://agent-plugins.org/specification) root manifest; version
1.0.1 uses the native manifests to keep Codex installation to one package.

## Research influences

These papers informed design decisions. None evaluated or endorsed RumoKit.
Their findings apply to their own tasks and experimental conditions.

- [SkillsBench](https://arxiv.org/abs/2602.12670) and
  [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988): relevance and cost of
  instructions supplied to an agent.
- [Learning to Ask](https://arxiv.org/abs/2409.00557): clarification when information
  needed for a decision is missing.
- [SWT-Bench](https://arxiv.org/abs/2406.12952) and
  [Rethinking the Value of Agent-Generated Tests](https://arxiv.org/abs/2602.07900):
  evaluating tests by the behavior they distinguish, rather than their count.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798):
  the limits of self-review without external feedback.
- [Stop Overvaluing Multi-Agent Debate](https://arxiv.org/abs/2502.08788):
  weighing extra agents against simpler ways to obtain useful evidence.

RumoKit's own measured results and limitations are in the
[validation report](docs/VALIDATION.md).
