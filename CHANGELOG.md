# Changes

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
