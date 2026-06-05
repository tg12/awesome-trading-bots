"""Validate the awesome-trading-bots README.

A dependency-free CI check: confirms required sections exist, the Viprasol contact
block is present, the logo asset referenced by the README exists on disk, and
there are no duplicate links. Exits non-zero on any failure.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

REQUIRED_SECTIONS = [
    "## Contents",
    "## Viprasol open-source bots",
    "## Crypto trading bots",
    "## Contributing",
    "## Contact — Viprasol Tech Private Limited",
]


def main() -> int:
    errors: list[str] = []
    text = README.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing required section: {section!r}")

    if "support@viprasol.com" not in text:
        errors.append("missing Viprasol contact email")

    # Referenced local logo must exist.
    for rel in re.findall(r'src="([^"]+\.png)"', text):
        if not rel.startswith("http") and not (ROOT / rel).exists():
            errors.append(f"referenced asset not found: {rel}")

    links = re.findall(r"\]\((https?://[^)]+)\)", text)

    # No duplicate *project* entries (owner/repo links). Brand/contact links such
    # as the homepage or socials are allowed to recur.
    repo_links = [link for link in links if re.match(r"https?://github\.com/[^/)]+/[^/)]+", link)]
    seen: set[str] = set()
    for link in repo_links:
        if link in seen:
            errors.append(f"duplicate project link: {link}")
        seen.add(link)

    if errors:
        print("README validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"README OK — {len(links)} links across {len(REQUIRED_SECTIONS)} required sections.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
