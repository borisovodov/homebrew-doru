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
releases. Dóru is Apple Silicon only: macOS 13 (Ventura) or later, and the
cask declares `depends_on arch: :arm64`. The app has no self-update
mechanism, so Homebrew is the update channel: each release bumps `version`
and `sha256` in `Casks/doru.rb` (the `livecheck` block tracks the GitHub
releases).
