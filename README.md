# homebrew-taps

Personal Homebrew tap for applications I distribute through Homebrew. It is
a complete cask tap; install the tap, then any cask from it:

```sh
brew tap borisovodov/taps
brew trust borisovodov/taps   # Homebrew 7+: third-party taps are untrusted by default
brew install --cask <cask>
```

## Casks

| Cask | Description | Homepage |
|---|---|---|
| [doru](Casks/doru.rb) | Local-first genealogy for the AI era | https://doru.family |

Dóru's cask installs the signed and notarized macOS dmg (Apple Silicon,
macOS 13 or later) and the AppImage on Linux (x86_64 and arm64). The app has
no self-update mechanism (`auto_updates false`), so Homebrew is the update
channel: each release bumps `version` and the `sha256` entries in
`Casks/doru.rb` (the `livecheck` block tracks the GitHub releases). The cask
uses Homebrew 7 cask DSL (`on_system_conditional`, `app_image`); older
Homebrew versions cannot parse it.

## Updates

The `update-casks.yml` workflow checks for new releases of the tracked
projects every hour and commits cask updates (version and sha256 entries,
taken from the release assets' API digests) directly to `main` — no manual
bumps needed. It can also be triggered manually (workflow_dispatch).
