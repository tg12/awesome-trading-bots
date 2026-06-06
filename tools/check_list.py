"""Validate the awesome-trading-bots README.

A dependency-free CI check (standard library only) that confirms the list stays
well-structured and link-clean. It verifies:

* every required section heading is present and in the expected order;
* the Contents table of contents links to anchors that actually exist;
* the Viprasol contact block is present;
* any local image referenced by the README exists on disk;
* there are no malformed Markdown links; and
* the same project is not listed twice *within a single section* (intentional
  cross-references between sections, e.g. a framework that is both a bot and an
  execution engine, are allowed and are reported as informational only).

Exits non-zero on any hard failure so it can gate CI.
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
    "## Stock & multi-asset trading bots",
    "## Forex trading bots",
    "## Options, futures & derivatives",
    "## Prediction-market bots",
    "## Backtesting & research frameworks",
    "## Contributing",
    "## Contact — Viprasol Tech Private Limited",
    "## License",
]

LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
REPO_RE = re.compile(r"https?://github\.com/([^/)\s]+)/([^/)\s#]+)")


def github_repo_key(url: str) -> str | None:
    """Return a normalised ``owner/repo`` key for a GitHub project URL."""
    match = REPO_RE.match(url)
    if not match:
        return None
    owner, repo = match.group(1), match.group(2)
    return f"{owner.lower()}/{repo.lower().removesuffix('.git')}"


def slugify(heading: str) -> str:
    """Mimic GitHub's anchor slug generation for a heading line."""
    text = heading.lstrip("#").strip().lower()
    # GitHub drops most punctuation, then turns each remaining space into a single
    # hyphen *without* collapsing runs (so "a & b" -> "a--b").
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", "-")


def split_sections(text: str) -> dict[str, str]:
    """Map each ``## heading`` to the body text beneath it."""
    sections: dict[str, str] = {}
    current = "_preamble"
    buf: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            sections[current] = "\n".join(buf)
            current = line.strip()
            buf = []
        else:
            buf.append(line)
    sections[current] = "\n".join(buf)
    return sections


def validate(text: str) -> tuple[list[str], list[str], int, int]:
    """Validate README ``text``.

    Returns ``(errors, info, num_links, num_unique_repos)``. The README passes
    when ``errors`` is empty.
    """
    errors: list[str] = []
    info: list[str] = []

    # 1. Required sections present and in order.
    last_index = -1
    for section in REQUIRED_SECTIONS:
        idx = text.find(section)
        if idx == -1:
            errors.append(f"missing required section: {section!r}")
        elif idx < last_index:
            errors.append(f"section out of order: {section!r}")
        else:
            last_index = idx

    # 2. Contact essentials.
    if "support@viprasol.com" not in text:
        errors.append("missing Viprasol contact email")
    if "Built and maintained by" not in text:
        errors.append("missing 'Built and maintained by' attribution line")

    # 3. Local images must exist.
    for rel in re.findall(r'src="([^"]+\.png)"', text):
        if not rel.startswith("http") and not (ROOT / rel).exists():
            errors.append(f"referenced asset not found: {rel}")

    # 4. Table-of-contents anchors must resolve to real headings.
    headings = {slugify(line) for line in text.splitlines() if line.startswith("## ")}
    contents_block = text.split("## Contents", 1)[-1].split("\n## ", 1)[0]
    for anchor in re.findall(r"\]\(#([a-z0-9-]+)\)", contents_block):
        if anchor not in headings:
            errors.append(
                f"table-of-contents anchor has no matching heading: #{anchor}"
            )

    # 5. Collect links and check for malformed Markdown links.
    links = LINK_RE.findall(text)
    if "](http" in text:
        # Count balanced link tokens vs raw occurrences to catch broken syntax.
        raw = len(re.findall(r"\]\(http", text))
        if raw != len(links):
            errors.append(
                f"malformed Markdown link(s): {raw} link-opens but {len(links)} parsed"
            )

    # 6. Duplicate project links *within the same section* are errors;
    #    cross-section reuse is allowed (informational).
    repo_count: dict[str, int] = {}
    for heading, body in split_sections(text).items():
        seen: set[str] = set()
        for url in LINK_RE.findall(body):
            key = github_repo_key(url)
            if key is None:
                continue
            repo_count[key] = repo_count.get(key, 0) + 1
            if key in seen:
                errors.append(f"duplicate project within {heading!r}: {key}")
            seen.add(key)

    cross_referenced = sum(1 for c in repo_count.values() if c > 1)
    if cross_referenced:
        info.append(
            f"{cross_referenced} project(s) cross-referenced across sections (allowed)"
        )

    return errors, info, len(links), len(repo_count)


def main() -> int:
    text = README.read_text(encoding="utf-8")
    errors, info, num_links, num_repos = validate(text)

    if errors:
        print("README validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        f"README OK - {num_links} links, {num_repos} unique GitHub projects, "
        f"{len(REQUIRED_SECTIONS)} required sections."
    )
    for note in info:
        print(f"  note: {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
