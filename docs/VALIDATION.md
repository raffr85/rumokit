# Validation and claim limits

These are maintainer-reported results from a controlled acceptance case.
The external evaluator was separate from the candidate, not an independent
public auditor. Raw private artifacts are not distributed, so this report alone
is not a publicly reproducible benchmark.

## 1.0 acceptance — 2026-09-16

The accepted `1.0.0-rc.1` skills and hooks were promoted unchanged to `1.0.0`.
The package contains 22 portable skills and thin native bootstrap integrations,
not an enforcement runtime. Acceptance is not a guarantee of future agent behavior.

The controlled case starts with an existing local Python/SQLite workshop panel.
The request leaves a material product choice open: how a freed seat should pass
to a waiting person. A private, fixed customer answers only questions asked by
the candidate. No ready-made specification, plan, implementation or test solution
is supplied. The accepted choice reserves an exclusive FIFO offer requiring
explicit acceptance, rather than automatic confirmation.

RumoKit passed on both Codex with Astra/medium and Devin with Opus 5/medium:

- Ask about the material queue decision before implementing it.
- Deliver the agreed offer, accept, decline, cancellation and persistence behavior.
- Preserve the original database and seven existing behavior checks.
- Pass eleven external HTTP checks, including concurrency and lost responses.
- Pass three real-Chrome scenarios plus recovered feedback/control usability.
- Produce its own evidence of legacy-state preservation, concurrency and
  interrupted-response recovery through the real server boundary.
- Load native workflow instructions and apply them; installed skill counts alone
  do not satisfy activation.

Codex also exercised the delivered JavaScript against its real HTTP server using
a minimal DOM. Devin exercised a real socket response loss and replay. Neither
candidate demonstrated its own visual browser inspection; separate Chrome
evaluation supplies that separate observation.

## Consumption

All figures include the recorded candidate work and any descendants. Cached input
is counted once. Units are `uncached input + 0.1 × cached input + 5 × output`:
a fixed normalization, not dollars, subscription usage, or a provider invoice.

| Host/model | RumoKit raw tokens | Stack raw tokens | RumoKit units | Stack units |
|---|---:|---:|---:|---:|
| Codex / Astra medium | 1,021,210 | 2,543,043 | 271,301.2 | 528,525.4 |
| Devin / Opus 5 medium | 2,018,659 | 2,594,724 | 439,898.7 | 518,606.0 |

The comparator is the frozen pstack 0.9.28 + Superpowers 6.3.0 workflow stack,
not every plugin installed on a user's machine. The Codex comparator is a
historical execution of the same case/configuration whose final artifact passed
the same technical checks. The observed reduction is 48.7% in normalized units
and 59.8% in raw tokens on Codex. This supports a narrow efficiency result for
this case, not an expected saving on arbitrary tasks. It was not faster on Codex.

On Devin, the stack received transport-only hook compatibility fixes; skill and
bootstrap instruction contents were preserved. Its final artifact has a
reproduced recovered-control defect. RumoKit used 15.2% fewer normalized units
and passed that check, but this is not an equal-quality cost estimate because
the comparator's product failed. A shared-loopback port collision also added
comparator overhead. Even discounting five complete port-related responses left
RumoKit below the comparator's remaining units; that sensitivity check does not
reconstruct an interference-free run. No clean speed advantage is claimed.

## What this does not establish

- One known acceptance case per configuration is not a statistical benchmark,
  a blind public leaderboard result, an ablation, or proof that the plugin caused
  every improvement.
- There is no new no-plugin arm in this closing comparison.
- The result does not validate every skill, language, repository topology, model,
  subscription, or host. Portable principles do not imply identical performance.
- Fewer tokens, more tests, or more skill invocations are not quality evidence
  without checking the final artifact against the requested outcome.
- This release does not claim SOTA, production readiness of generated software,
  tool confinement, automatic approval, or correctness guarantees.

The acceptance campaign preserves its protocols, immutable sources, native
transcripts, exact client answers, token reconciliation, delivered code, external
results and cleanup receipts separately from this distributable package. Raw
local traces and private host/account details are not bundled for publication.
