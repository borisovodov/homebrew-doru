#!/usr/bin/env python3
"""Rewrite Casks/doru.rb for a new release: version and the three sha256 values.

Usage: update-cask.py <version> <arm-dmg-hash> <arm64-linux-hash> <x86_64-linux-hash>
"""
import re
import sys

version, arm, arm64_linux, x86_64_linux = sys.argv[1:5]
path = "Casks/doru.rb"
text = open(path, encoding="utf-8").read()
text = re.sub(r'version "[^"]+"', f'version "{version}"', text, count=1)
text = re.sub(r'(arm:\s+)"[0-9a-f]{64}"', rf'\1"{arm}"', text)
text = re.sub(r'(arm64_linux:\s+)"[0-9a-f]{64}"', rf'\1"{arm64_linux}"', text)
text = re.sub(r'(x86_64_linux:\s+)"[0-9a-f]{64}"', rf'\1"{x86_64_linux}"', text)
open(path, "w", encoding="utf-8").write(text)
print(f"updated {path} to {version}")
