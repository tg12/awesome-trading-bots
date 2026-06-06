# Contributing to Awesome Trading Bots

Thanks for helping keep this list useful! Curated by
[Viprasol Tech](https://viprasol.com).

## Adding a project

Open a pull request that adds your entry under the most relevant section, using
this format:

```markdown
- [Project Name](https://github.com/owner/repo) — One-line description of what it does.
```

Please make sure the project is:

- **Open-source** with a public repository.
- **Actively maintained** (or clearly marked if archived).
- **Accurately described** in a single, neutral sentence.
- **Placed in the right section** and kept in roughly alphabetical / relevance order.

## Where to add your entry

| If your project is mainly... | Add it under |
| --- | --- |
| A crypto bot | **Crypto trading bots** |
| A stock / multi-asset engine | **Stock & multi-asset trading bots** |
| FX-focused | **Forex trading bots** |
| Options / futures / derivatives | **Options, futures & derivatives** |
| A prediction-market tool | **Prediction-market bots** |
| A backtester / research framework | **Backtesting & research frameworks** |
| An order router / execution engine | **Execution engines & order routing** |
| A data feed | **Market data & feeds** |
| An indicator library | **Technical analysis & indicators** |
| ML / RL for trading | **Machine learning & alpha research** |
| Portfolio / risk tooling | **Portfolio, risk & analytics** |
| An exchange / broker SDK | **Exchange & broker APIs** |

A project may be cross-referenced from more than one section, but it must not be
listed twice *within the same section* (the validator enforces this).

## Checks

A lightweight, dependency-free CI check verifies the README's structure,
table-of-contents anchors, link formatting, and that no project is duplicated
within a section. A small `pytest` suite covers the validator itself. Run both
locally before opening a PR:

```bash
python tools/check_list.py
python -m pytest -q tools
```

## Code of Conduct

By participating you agree to our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions

Reach us on [Telegram](https://t.me/viprasol_help) or at
[support@viprasol.com](mailto:support@viprasol.com).
