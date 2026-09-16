# Contribute to RumoKit

Contributions are welcome. RumoKit is maintained by Rafael Affonso.
Submit changes under the project's [MIT license](LICENSE), and preserve any
required copyright and license notices for material you contribute.

## Report a problem

Open an [issue](https://github.com/raffr85/rumokit/issues) on the official repository. Include:

- RumoKit version, host version, model, and reasoning setting when known.
- The outcome you requested and the behavior you observed.
- A small, sanitized example that reproduces the problem.
- Which skills and other workflow plugins were active.
- Whether the failure involved loading, clarification, execution, or verification.

Remove private code, credentials, internal URLs, account details, and personal
data. Do not upload a complete agent transcript without reviewing it first.
For a security-sensitive report, see [reporting security concerns](docs/SECURITY.md#reporting-security-concerns).

## Propose a change

Explain the concrete failure the change addresses and why the current skills
cannot handle it. A new skill is appropriate when it has a distinct trigger and
completion condition. There is no fixed skill-count target.

Keep portable instructions independent of vendor tool names, model identifiers,
and subscription assumptions. Put necessary host mappings in adapters.
Preserve direct skill entry points and the user's existing authorization.

Prefer a focused change over a broad rewrite. Do not weaken the requested
outcome to make a test pass. Include the observed benefit, regressions checked,
and remaining uncertainty. See [the maintenance method](docs/METHOD.md).

## Check your change

From the repository root, run the package tests with Python 3.10 or later:

```sh
python3 -B -m unittest discover -s tests -v
```

These tests check packaging and hook output. They do not prove that a model
follows the workflow. For behavior changes, exercise a representative task in
the affected host and inspect the final artifact against the requested outcome.
For adapter changes, also check the real loader; executing a hook directly is
not enough.

When comparing configurations, report quality, corrections, time, and token
components separately. Preserve failures and configuration differences. Do not
claim a general improvement from one successful run.
