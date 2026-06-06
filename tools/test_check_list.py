"""Tests for the awesome-trading-bots README validator.

Run from the repo root with:

    python -m pytest -q tools

These exercise the pure helper functions and the end-to-end ``main`` check
against the real README, plus synthetic failure cases to prove the validator
actually catches problems.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# Import the sibling module by path so the test works regardless of sys.path.
_spec = importlib.util.spec_from_file_location(
    "check_list", Path(__file__).parent / "check_list.py"
)
assert _spec and _spec.loader
check_list = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_list)


# --------------------------------------------------------------------------- #
# slugify                                                                      #
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize(
    ("heading", "expected"),
    [
        ("## Crypto trading bots", "crypto-trading-bots"),
        ("## Stock & multi-asset trading bots", "stock--multi-asset-trading-bots"),
        ("## Options, futures & derivatives", "options-futures--derivatives"),
        (
            "## Contact — Viprasol Tech Private Limited",
            "contact--viprasol-tech-private-limited",
        ),
        ("## License", "license"),
    ],
)
def test_slugify_matches_github_rules(heading: str, expected: str) -> None:
    assert check_list.slugify(heading) == expected


def test_slugify_does_not_collapse_space_runs_from_ampersand() -> None:
    # An ampersand is dropped but its surrounding spaces each become a hyphen.
    assert check_list.slugify("## A & B") == "a--b"


# --------------------------------------------------------------------------- #
# github_repo_key                                                              #
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://github.com/freqtrade/freqtrade", "freqtrade/freqtrade"),
        ("https://github.com/CCXT/CCXT", "ccxt/ccxt"),
        ("https://github.com/owner/repo.git", "owner/repo"),
        ("https://github.com/owner/repo#readme", "owner/repo"),
        ("https://viprasol.com", None),
        ("https://www.investopedia.com/terms/a/algorithmictrading.asp", None),
    ],
)
def test_github_repo_key(url: str, expected: str | None) -> None:
    assert check_list.github_repo_key(url) == expected


# --------------------------------------------------------------------------- #
# split_sections                                                              #
# --------------------------------------------------------------------------- #
def test_split_sections_partitions_by_heading() -> None:
    text = "intro\n## One\nbody one\n## Two\nbody two"
    sections = check_list.split_sections(text)
    assert sections["_preamble"].strip() == "intro"
    assert "body one" in sections["## One"]
    assert "body two" in sections["## Two"]
    assert "body one" not in sections["## Two"]


# --------------------------------------------------------------------------- #
# end-to-end against the real README                                           #
# --------------------------------------------------------------------------- #
def test_real_readme_passes(capsys: pytest.CaptureFixture[str]) -> None:
    assert check_list.main() == 0
    out = capsys.readouterr().out
    assert "README OK" in out


def test_real_readme_has_all_required_sections() -> None:
    text = README.read_text(encoding="utf-8")
    for section in check_list.REQUIRED_SECTIONS:
        assert section in text, f"missing {section!r}"


def test_real_readme_required_sections_in_order() -> None:
    text = README.read_text(encoding="utf-8")
    indices = [text.find(s) for s in check_list.REQUIRED_SECTIONS]
    assert all(i != -1 for i in indices)
    assert indices == sorted(indices)


def test_real_readme_contact_block_present() -> None:
    text = README.read_text(encoding="utf-8")
    assert "support@viprasol.com" in text
    assert "Built and maintained by" in text


def test_real_readme_has_no_duplicate_within_section() -> None:
    sections = check_list.split_sections(README.read_text(encoding="utf-8"))
    for heading, body in sections.items():
        seen: set[str] = set()
        for url in check_list.LINK_RE.findall(body):
            key = check_list.github_repo_key(url)
            if key is None:
                continue
            assert key not in seen, f"duplicate {key} in {heading!r}"
            seen.add(key)


def test_real_readme_is_substantial() -> None:
    """Guards against accidental content loss in future edits."""
    text = README.read_text(encoding="utf-8")
    links = check_list.LINK_RE.findall(text)
    repos = {k for url in links if (k := check_list.github_repo_key(url)) is not None}
    assert len(repos) >= 60, f"expected a rich list, found {len(repos)} unique repos"


# --------------------------------------------------------------------------- #
# synthetic failure cases (validator must catch problems)                      #
# --------------------------------------------------------------------------- #
def test_validate_fails_when_section_missing() -> None:
    broken = README.read_text(encoding="utf-8").replace("## License", "## Licence-typo")
    errors, _info, _links, _repos = check_list.validate(broken)
    assert any("required section" in e for e in errors)


def test_validate_fails_on_duplicate_within_section() -> None:
    text = README.read_text(encoding="utf-8")
    # Inject two copies of the same repo right under the Crypto heading.
    dup = text.replace(
        "## Crypto trading bots\n",
        "## Crypto trading bots\n\n"
        "- [Dup](https://github.com/freqtrade/freqtrade) - dup.\n"
        "- [Dup2](https://github.com/freqtrade/freqtrade) - dup.\n",
        1,
    )
    errors, _info, _links, _repos = check_list.validate(dup)
    assert any("duplicate project within" in e for e in errors)


def test_validate_fails_on_missing_toc_anchor() -> None:
    text = README.read_text(encoding="utf-8")
    broken = text.replace(
        "- [License](#license)", "- [License](#nonexistent-anchor)", 1
    )
    errors, _info, _links, _repos = check_list.validate(broken)
    assert any("table-of-contents anchor" in e for e in errors)


def test_validate_passes_on_real_readme() -> None:
    errors, _info, links, repos = check_list.validate(
        README.read_text(encoding="utf-8")
    )
    assert errors == []
    assert links > 0 and repos > 0
