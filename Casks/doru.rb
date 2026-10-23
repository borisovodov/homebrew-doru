cask "doru" do
  version "0.0.11"

  on_arm do
    sha256 "072808bd2e78c03c0fe5b41c976546b99f8bc6e87f44482ca9e62b6e35263630"

    url "https://github.com/borisovodov/doru/releases/download/v#{version}/doru-mac-arm64.dmg"
  end

  name "Dóru"
  desc "Local-first genealogy for the AI era"
  homepage "https://doru.family/"

  livecheck do
    url :url
    strategy :github_latest
  end

  depends_on arch: :arm64
  depends_on macos: :ventura

  app "Doru.app"

  zap trash: [
    "~/Library/Application Support/Doru",
    "~/Library/Preferences/org.doru.doru.plist",
    "~/Library/Saved Application State/org.doru.doru.savedState",
  ]
end
