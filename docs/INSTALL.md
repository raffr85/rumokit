# Install RumoKit

Get the v1.0.0 source from the [release page](https://github.com/raffr85/rumokit/releases/tag/v1.0.0)
or clone the tagged version:

```sh
git clone --branch v1.0.0 --depth 1 https://github.com/raffr85/rumokit.git
cd rumokit
```

Run the commands below from the RumoKit root, where `plugin.json` and `skills/` are located.
The commands assume your chosen coding-agent CLI is installed and on your PATH.

Review the [trust model](SECURITY.md) before enabling hooks. RumoKit does not need
its own account or API key; your host still needs its normal authentication.
The executable hooks use a POSIX shell. Windows-native hook execution is not
validated by this release.

For a trial, use a disposable project and the host's supported profile isolation.
A disposable project alone does not isolate user-wide plugins or instructions.
The persistent installation commands below change plugin state for the current
host profile. They are not clean-profile or benchmark setup commands.

## Codex

The install path is checked against Codex CLI 0.153.1. The portable core provides
the skills. The optional `rumokit-codex` adapter supplies the startup instruction
that asks Codex to load the portable router.

Register the repository's bundled catalog and install the core:

```sh
codex plugin marketplace add .
codex plugin add rumokit@rumokit
```

If you prefer not to clone the source yourself, replace `marketplace add .` with:

```sh
codex plugin marketplace add raffr85/rumokit --ref v1.0.0
```

Then run the same core and adapter installation commands. Use one catalog
registration method, not both.

For automatic startup routing, also install the adapter:

```sh
codex plugin add rumokit-codex@rumokit
```

Inspect the installed entries:

```sh
codex plugin list --marketplace rumokit
```

Both packages should report version `1.0.0`. Review and trust the adapter's
`SessionStart` hook through your client's hook-review controls. Start a new
session after installation or a trust change. Installation alone does not prove
that the hook ran.

The catalog in `.agents/plugins/marketplace.json` points to the root and
`adapters/rumokit-codex`; it does not duplicate the skills. These paths are
relative to the repository root. The tested loader accepts the core path `./`.
Do not install the adapter alone or rewrite the core manifest to force hook loading.

To invoke a focused skill, use Codex's skill picker and choose its installed name.
If the hook is unavailable or untrusted, select `use-rumokit` explicitly when you
want the router. Native skill discovery remains available without the adapter.

To remove this installation, run only the commands for packages you installed:

```sh
codex plugin remove rumokit-codex@rumokit
codex plugin remove rumokit@rumokit
codex plugin marketplace remove rumokit
```

Restart the session so previously loaded instructions do not remain in context.
These commands target the catalog named `rumokit`, not another catalog containing
a separate RumoKit installation.

## Devin CLI

The accepted case used Devin CLI 3000.10.27. Install the root plugin:

```sh
devin plugins install --local .
```

Review the plugin trust request before accepting. Inspect the registered plugin:

```sh
devin plugins info rumokit
devin plugins list
```

Start a new session after installation. The root's Claude-compatible hook supplies
the router, and Devin's native skill invocation loads the selected workflow.

`--local` means installation for the current user on this machine, without adding
it to synced personal plugins. It can affect sessions in other projects. It does
not disable other plugins, imported instructions, or global skills.
The local directory remains linked; keep it in place and review edits before
starting another session.

To remove this machine-local installation:

```sh
devin plugins remove --local rumokit
```

This removal command is not the path for a synced personal installation.
Restart the session after removal.

## Claude Code

Load the root plugin for one session:

```sh
claude --plugin-dir .
```

Follow the host's trust prompts. The root contains the skills and its
`SessionStart` hook. A direct skill invocation uses the plugin namespace:

```text
/rumokit:understand-code
```

To start without this session-local plugin, end the session and launch `claude`
without `--plugin-dir`. No persistent installation is created by this command.
An existing persistent RumoKit installation would need separate removal.

This is a documented loading path for the compatible package format. Version 1.0
does not claim a completed behavioral acceptance case on Claude Code.

## Other Agent Skills clients

Use your client's documented skill installation mechanism to load the directories
under `skills/`. Keep any supporting files in each directory. Select `use-rumokit`
for routed work or invoke a focused skill directly.

Automatic bootstrap behavior needs a supported host integration. Importing skills
alone does not install either bundled hook. No model choice or permission policy
is changed by the portable instructions.

## Check activation

In a new session, check that the actual skill catalog includes `use-rumokit` and
the focused skills you need. When a hook is enabled, check the host's hook output
or startup context, not just the installed-plugin list.

Try an explanation-only request in a disposable project. Confirm that the host
loads `understand-code`, explains the requested behavior, and does not edit files.
This checks loading and basic scope; it is not proof of overall effectiveness.

Keep domain and tool plugins you need, but choose one default workflow router
for the task. Other routers can introduce competing planning, approval, testing,
or delegation rules.

## Migrate from Steelman

RumoKit is a renamed package, not an automatic in-place upgrade. Install the new
package in your chosen profile and retire the old Steelman package and router
there. Do not leave both names enabled as competing workflow routers.

Renaming source files does not update installed caches or trust decisions.
Start a new session and repeat the activation check. Historical evaluation files
retain their original Steelman name.

## Host references

- [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Codex 0.153.1 catalog path resolution](https://github.com/openai/codex/blob/rust-v0.153.1/codex-rs/core-plugins/src/marketplace.rs)
- [Devin CLI plugins](https://docs.devin.ai/cli/extensibility/plugins/overview)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Agent Skills specification](https://agentskills.io/specification)
