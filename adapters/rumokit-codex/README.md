# RumoKit Codex adapter

This optional adapter loads RumoKit's router instructions at session start and
after context resets. Install the `rumokit` core as well; this package contains
no skills and does not work as a standalone workflow.

Review and trust its hook in Codex before relying on automatic routing. The hook
reads only the bundled static context file. It does not enforce model behavior,
change permissions, select a model, or contact a network service.

Follow the [installation guide](https://github.com/raffr85/rumokit/blob/v1.0.0/docs/INSTALL.md)
in the RumoKit core. The adapter is packaged separately because the tested Codex
loader does not activate lifecycle hooks from the schema-declared portable core.

[MIT](LICENSE). Copyright (c) 2026 Rafael Affonso.
