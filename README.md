# homebrew-doru

Homebrew cask tap for [Dóru](https://doru.family) — local-first genealogy for
the AI era. This directory is a complete cask tap; publish it as the
`borisovodov/homebrew-doru` GitHub repository.

Install from the published tap:

```sh
brew tap borisovodov/doru
brew install --cask doru
```

Test locally without publishing (from this directory):

```sh
brew tap borisovodov/doru "$PWD"
brew install --cask doru
brew audit --new-cask doru
brew livecheck doru
```

The cask installs the signed and notarized dmg from the project's GitHub
releases. Requirements: macOS 13 (Ventura) or later on Apple Silicon. Intel
builds are not produced yet, so the cask declares `depends_on arch: :arm64`
and has no `on_intel` block.
