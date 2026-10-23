# homebrew-doru

Homebrew cask tap for [Dóru](https://doru.family) — local-first genealogy for
the AI era.

Install:

```sh
brew tap borisovodov/doru
brew trust borisovodov/doru   # Homebrew 7+: third-party taps are untrusted by default
brew install --cask doru
```

Test locally without publishing (from this directory):

```sh
brew tap borisovodov/doru "$PWD"
brew install --cask doru
brew audit --cask doru
brew style doru
brew livecheck doru
```

The cask installs the signed and notarized dmg from the project's GitHub
releases. Dóru is Apple Silicon only on macOS: macOS 13 (Ventura) or later,
and the cask declares `depends_on arch: :arm64`. On Linux, the cask installs
the AppImage into `~/Applications` (x86_64 and arm64). The app has no
self-update mechanism (`auto_updates false`), so Homebrew is the update
channel: each release bumps `version` and the `sha256` entries in
`Casks/doru.rb` (the `livecheck` block tracks the GitHub releases). The cask
uses Homebrew 7 cask DSL (`on_system_conditional`, `app_image`); older
Homebrew versions cannot parse it.
