<p align="center">
  <img src="assets/logo.png" width="120" alt="Viprasol Tech logo">
</p>

<h1 align="center">Awesome Trading Bots <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a></h1>

<p align="center">
  <strong>A curated list of the best open-source trading bots, frameworks, and libraries — for crypto, stocks, forex, options, and prediction markets.</strong>
</p>

<p align="center">
  <em>Curated by <a href="https://viprasol.com">Viprasol Tech</a> — Fintech Experts. Full-Stack Builders.</em>
</p>

<p align="center">
  <a href="https://github.com/Viprasol-Tech/awesome-trading-bots/actions/workflows/lint.yml"><img src="https://img.shields.io/github/actions/workflow/status/Viprasol-Tech/awesome-trading-bots/lint.yml?style=flat-square&logo=githubactions&logoColor=white&label=lint" alt="Lint"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Viprasol-Tech/awesome-trading-bots?style=flat-square&color=blue" alt="License: MIT"></a>
  <a href="https://t.me/viprasol_help"><img src="https://img.shields.io/badge/Telegram-support-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="https://github.com/Viprasol-Tech/awesome-trading-bots/stargazers"><img src="https://img.shields.io/github/stars/Viprasol-Tech/awesome-trading-bots?style=flat-square&logo=github" alt="Stars"></a>
</p>

---

> ## ⚠️ Disclaimer
> Trading bots can lose money. Everything here is for **educational purposes only** and is **not financial advice**. Trading involves substantial risk, including the **total loss of capital**, and past or backtested performance does not predict future results. Always paper-trade first, read each project's own disclaimer and license, and comply with the laws and platform terms in your jurisdiction.

---

## Contents

- [Viprasol open-source bots](#viprasol-open-source-bots)
- [Crypto trading bots](#crypto-trading-bots)
- [Stock & multi-asset trading bots](#stock--multi-asset-trading-bots)
- [Forex trading bots](#forex-trading-bots)
- [Options & derivatives](#options--derivatives)
- [Prediction-market bots](#prediction-market-bots)
- [Backtesting & research frameworks](#backtesting--research-frameworks)
- [Libraries & data](#libraries--data)
- [Learning resources](#learning-resources)
- [Contributing](#contributing)

## Viprasol open-source bots

Free, MIT-licensed, working bots built and maintained by [Viprasol Tech](https://viprasol.com):

- [kalshi-trading-bot](https://github.com/Viprasol-Tech/kalshi-trading-bot) — Framework for Kalshi prediction markets (RSA-PSS auth, strategy engine, backtester, risk manager).
- [ai-trading-bot](https://github.com/Viprasol-Tech/ai-trading-bot) — Broker-agnostic AI/ML signal-ensemble trading framework.
- [crypto-trading-bot](https://github.com/Viprasol-Tech/crypto-trading-bot) — Multi-exchange crypto bot with grid & DCA strategies.
- [ai-crypto-trading-bot](https://github.com/Viprasol-Tech/ai-crypto-trading-bot) — AI alpha engine: feature engineering, scoring, Kelly sizing.
- [solana-trading-bot](https://github.com/Viprasol-Tech/solana-trading-bot) — Solana DEX AMM math, slippage, and cross-pool arbitrage.
- [stock-trading-bot](https://github.com/Viprasol-Tech/stock-trading-bot) — Cross-sectional momentum ranking & portfolio rebalancing.
- [forex-trading-bot](https://github.com/Viprasol-Tech/forex-trading-bot) — Pip/lot math, risk-based position sizing, trend strategy.
- [options-trading-bot](https://github.com/Viprasol-Tech/options-trading-bot) — Black-Scholes pricing, Greeks, and strategy payoffs.
- [polymarket-trading-bot](https://github.com/Viprasol-Tech/polymarket-trading-bot) — Edge, YES/NO arbitrage, and Kelly sizing for binary markets.

## Crypto trading bots

- [Freqtrade](https://github.com/freqtrade/freqtrade) — Popular free crypto trading bot in Python with backtesting, ML, and Telegram control.
- [Hummingbot](https://github.com/hummingbot/hummingbot) — Open-source market-making and arbitrage bot for crypto exchanges.
- [Jesse](https://github.com/jesse-ai/jesse) — Advanced crypto trading framework focused on simplicity and backtesting.
- [OctoBot](https://github.com/Drakkar-Software/OctoBot) — Modular crypto trading bot with a web UI and strategy marketplace.
- [Kelp](https://github.com/stellar/kelp) — Open-source trading and market-making bot (Stellar and others).

## Stock & multi-asset trading bots

- [QuantConnect LEAN](https://github.com/QuantConnect/Lean) — Open-source algorithmic trading engine (equities, futures, options, crypto).
- [Nautilus Trader](https://github.com/nautechsystems/nautilus_trader) — High-performance event-driven trading platform in Python/Rust.
- [vn.py](https://github.com/vnpy/vnpy) — Full-featured quant trading platform.
- [OpenBB](https://github.com/OpenBB-finance/OpenBB) — Open-source investment research platform.

## Forex trading bots

- **Viprasol:** see [`forex-trading-bot`](#viprasol-open-source-bots) above — risk-based FX position sizing and a trend strategy.
- [MetaTrader MQL community](https://www.mql5.com/en/code) — Large library of open Expert Advisors (MQL4/MQL5) for MT4/MT5.

## Options & derivatives

- **Viprasol:** see [`options-trading-bot`](#viprasol-open-source-bots) above — Black-Scholes pricing, Greeks, and payoffs.
- [QuantLib](https://github.com/lballabio/QuantLib) — Comprehensive quantitative finance library for derivatives pricing.

## Prediction-market bots

- **Viprasol:** see [`kalshi-trading-bot`](#viprasol-open-source-bots) and [`polymarket-trading-bot`](#viprasol-open-source-bots) above.
- [Manifold Markets](https://github.com/manifoldmarkets/manifold) — Open-source play-money prediction-market platform.

## Backtesting & research frameworks

- [Backtrader](https://github.com/mementum/backtrader) — Popular Python backtesting framework.
- [vectorbt](https://github.com/polakowo/vectorbt) — Fast, vectorised backtesting and research.
- [Zipline (reloaded)](https://github.com/stefan-jansen/zipline-reloaded) — Pythonic algorithmic trading library.
- [bt](https://github.com/pmorissette/bt) — Flexible backtesting for portfolio-based strategies.

## Libraries & data

- [CCXT](https://github.com/ccxt/ccxt) — Unified crypto exchange trading API for 100+ exchanges.
- [pandas-ta](https://github.com/twopirllc/pandas-ta) — Technical-analysis indicators for pandas.
- [TA-Lib](https://github.com/TA-Lib/ta-lib-python) — Classic technical-analysis library.
- [yfinance](https://github.com/ranaroussi/yfinance) — Download market data from Yahoo Finance.

## Learning resources

- [Awesome Quant](https://github.com/wilsonfreitas/awesome-quant) — A broader curated list of quant-finance libraries and tools.
- [Algorithmic trading basics](https://www.investopedia.com/terms/a/algorithmictrading.asp) — Introductory reading on algo trading.

## Contributing

Found a great open-source trading bot that's missing? Contributions are welcome —
see [CONTRIBUTING.md](CONTRIBUTING.md). Please keep entries open-source, actively
maintained, and accurately described.

## Contact — Viprasol Tech Private Limited

- 🌐 Website: [viprasol.com](https://viprasol.com)
- ✉️ Email: [support@viprasol.com](mailto:support@viprasol.com)
- 💬 Telegram: [t.me/viprasol_help](https://t.me/viprasol_help) · 📱 WhatsApp: +91 96336 52112
- 🐙 GitHub: [@Viprasol-Tech](https://github.com/Viprasol-Tech) · 💼 [LinkedIn](https://www.linkedin.com/in/viprasol/) · 𝕏 [@viprasol](https://twitter.com/viprasol)

> *Viprasol Tech — fintech software, algorithmic trading systems, MT4/MT5 bots, AI voice agents, and B2B SaaS. Need a custom build? [Get in touch](mailto:support@viprasol.com).*

## License

[MIT](LICENSE) © 2025 Viprasol Tech Private Limited. List content is provided as-is;
each linked project is governed by its own license.
