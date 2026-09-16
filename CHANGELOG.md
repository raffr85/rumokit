# Changes

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
