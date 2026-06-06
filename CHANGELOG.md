# Changelog

All notable changes to this list are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project loosely
follows [Semantic Versioning](https://semver.org/) for its structure and tooling.

## [0.2.0] - 2025-06-06

### Added
- **Doubled the curated list** to 76 unique GitHub projects across far more
  categories: execution engines & order routing, market data & feeds, technical
  analysis & indicators, machine learning & alpha research, portfolio/risk &
  analytics, and exchange & broker APIs.
- **"What makes a good trading bot?"** evaluation checklist for readers.
- **Mermaid landscape diagram** mapping the trading-bot ecosystem.
- **"By programming language"** index and a **bot framework comparison table**.
- **Roadmap** (checkboxes) and a short **FAQ**.
- **Related awesome lists** section for cross-discovery.
- **Test suite** (`tools/test_check_list.py`, 23 tests) covering the validator's
  helpers and end-to-end behaviour, including synthetic failure cases.
- CI now runs the validator *and* the test suite.

### Changed
- Flagship README rewrite: richer badge row, clearer structure, expanded
  disclaimer, and the standard Viprasol contact block.
- Rewrote `tools/check_list.py` into a richer, still dependency-free validator:
  it now checks section ordering, table-of-contents anchor integrity, malformed
  links, and duplicate projects *within a section* (cross-section references are
  allowed), and exposes a testable `validate(text)` function.
- Expanded `CONTRIBUTING.md` with clearer entry criteria and local checks.

## [0.1.0] - 2025

### Added
- Initial curated list with core categories (crypto, stocks, forex, options,
  prediction markets, backtesting, libraries, learning resources).
- Dependency-free README validator and CI workflow.
- Contributing guide, code of conduct, and "Add a project" issue template.

[0.2.0]: https://github.com/Viprasol-Tech/awesome-trading-bots/releases/tag/v0.2.0
[0.1.0]: https://github.com/Viprasol-Tech/awesome-trading-bots/releases/tag/v0.1.0
