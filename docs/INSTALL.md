# Install RumoKit

Use the instructions for your coding agent. Install the agent's CLI first and
complete its normal authentication. RumoKit needs no separate account or API key.

Review the [security guidance](SECURITY.md) before enabling hooks. Executable
hooks use a POSIX shell; Windows-native hook execution has not been validated.

## Codex

### Install from GitHub

```sh
codex plugin marketplace add raffr85/rumokit
codex plugin add rumokit@rumokit
```

RumoKit includes all 22 skills and the startup hook in one plugin.
Launch `codex`, open `/hooks`, and review and trust RumoKit's `SessionStart`
hook. Then start a new task in your client. The hook only reads the bundled
router instructions. The install path is checked against Codex CLI 0.153.1.

To pin a release instead of following the default branch, use this first command:

```sh
codex plugin marketplace add raffr85/rumokit --ref v1.0.4
```

Then run `codex plugin add rumokit@rumokit`.

### Check the installation

```sh
codex plugin list --marketplace rumokit
```

Check that `rumokit` is installed and enabled. In a new task, the skill picker
should include `rumokit:use-rumokit` and the other focused skills.
Check the hook output or startup context to confirm that the hook ran.

If the hook is unavailable or untrusted, you can still select
`rumokit:use-rumokit` explicitly. Skill discovery and hook execution are
separate checks.

### Use a local checkout or an existing app link

If you already have a clone, register its catalog from the repository root:

```sh
codex plugin marketplace add .
codex plugin add rumokit@rumokit
```

Use either the GitHub source or the local checkout for this catalog, not both.

A generated `codex://plugins/…?marketplacePath=…` link opens a plugin in a
catalog on that computer. You can install it through the app. The link is not a
portable installer for another user's computer. For public installation, use
the GitHub commands above.

If you installed through an app link, inspect its source in Codex before
registering another copy. A local source and a GitHub source can contain the
same plugin name at different versions.

### Update

For a GitHub installation that follows the default branch:

```sh
codex plugin marketplace upgrade rumokit
codex plugin add rumokit@rumokit
```

Check the installed version, review any changed hook, and start a new task.
A catalog pinned to a tag stays on that tag. Update a local checkout at its
source and reinstall through the same catalog.

If you previously installed the separate `rumokit-codex` adapter from version
1.0.0, remove it after updating the main plugin:

```sh
codex plugin remove rumokit-codex@rumokit
```

Run that command only if the old adapter is installed. New installations need
only `rumokit`; the old adapter is retained for compatibility.

### Uninstall

For the GitHub or local catalog named `rumokit`:

```sh
codex plugin remove rumokit@rumokit
codex plugin marketplace remove rumokit
```

Remove the old adapter first if it is still installed. For installations in
another catalog, use that catalog's plugin entry instead. Start a new task so
previously loaded instructions do not remain in context.

## Devin CLI

### Install

```sh
devin plugins install --local raffr85/rumokit
```

Review the plugin trust request, then start a new session. Check the installation:

```sh
devin plugins info rumokit
devin plugins list
```

The root plugin contains the skills and startup hook. The v1 acceptance case
used Devin CLI 3000.10.27.

`--local` installs for the current user on this machine, without adding the plugin
to synced personal plugins. It can affect sessions in other projects. Omit
`--local` only if you want the plugin synced through your Devin personal account.

### Update or uninstall

To fetch the latest version:

```sh
devin plugins update rumokit
```

Review the changes and start a new session. To uninstall the machine-local plugin:

```sh
devin plugins remove --local rumokit
```

Start a new session after removal. A synced personal installation has a separate
removal path in Devin.

### Use a local checkout

For plugin development, run `devin plugins install --local .` from the RumoKit
repository root. Devin links to that directory, so keep it in place. Reviewed
edits take effect in the next session without an update command.

## Claude Code

### Install from GitHub

Run these commands inside Claude Code:

```text
/plugin marketplace add raffr85/rumokit
/plugin install rumokit@rumokit
```

Follow Claude Code's trust prompts, then start a new session. Open `/plugin`
and check the Installed tab for RumoKit. The plugin includes the skills and
`SessionStart` hook. To invoke a focused skill directly:

```text
/rumokit:understand-code
```

A full behavioral acceptance run on Claude Code has not been completed.

### Update or uninstall

From your terminal, refresh the catalog and update the installed plugin:

```sh
claude plugin marketplace update rumokit
claude plugin update rumokit@rumokit
```

Review any changed hooks and start a new session. To uninstall, open `/plugin`
inside Claude Code, select RumoKit in the Installed tab, and choose Uninstall.

### Try a local copy for one session

For a session-only trial, use a clone instead of the persistent installation:

```sh
git clone --branch v1.0.4 --depth 1 https://github.com/raffr85/rumokit.git
cd rumokit
claude --plugin-dir .
```

Follow the trust prompts. Keep the clone in place for later sessions using this
command. To start without this copy, launch `claude` without `--plugin-dir`.
Any separately installed persistent copy remains enabled until you remove it.

## Other Agent Skills clients

Use your client's skill installation mechanism to load the directories under
`skills/`. Keep the supporting files inside each skill directory. Select
`use-rumokit` for routed work or invoke a focused skill directly.

Skills-only installation does not add a startup hook. Automatic routing needs
a supported host integration. Portability of the instructions does not mean
that every client or model has been behaviorally validated.

## Confirm activation

In a new session, check both the available skills and, if enabled, the startup
hook output. Try an explanation-only request in a disposable project. Confirm
that the agent loads `understand-code`, explains the requested behavior, and
does not edit files. This checks loading and basic scope, not overall quality.

Keep your domain and tool plugins. Choose one default workflow router for the
task. Multiple routers can impose conflicting planning, approval, test, or
delegation rules.

For an isolated trial, use the host's supported profile isolation. A disposable
project alone does not isolate user-wide plugins or instructions.

## Host documentation

- [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Codex hook review](https://learn.chatgpt.com/docs/hooks#review-and-trust-hooks)
- [Devin CLI plugins](https://docs.devin.ai/cli/extensibility/plugins/overview)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Agent Skills specification](https://agentskills.io/specification)
