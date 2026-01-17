# 📈 Trading Strategy Backtester (Full Stack)

A **full-stack trading strategy backtesting application** that allows users to test algorithmic trading strategies on historical stock market data and visualize performance metrics through an interactive dashboard.

Built with **FastAPI (backend)** and **React + Vite (frontend)**, this project demonstrates practical knowledge of **quantitative trading logic, data analysis, API design, and frontend visualization**.

---

## 🚀 Features

- 📊 Fetches real historical stock data using Yahoo Finance
- 🧠 Implements multiple trading strategies:
  - Moving Average Crossover
  - RSI (Relative Strength Index)
  - EMA (Exponential Moving Average)
  - RSI + EMA Combined Strategy
- ⚙️ Custom backtesting engine to simulate trades
- 📉 Performance metrics calculation:
  - Total Trades
  - Winning & Losing Trades
  - Win Rate
  - Final Equity
  - Maximum Drawdown
- 📈 Interactive equity curve visualization
- 🎯 User-driven inputs:
  - Stock symbol
  - Date range
  - Strategy selection
- 🌐 Fully integrated REST API + frontend dashboard

---

## 🧱 Tech Stack

### Backend
- **Python**
- **FastAPI**
- **Pandas**
- **yFinance**
- Custom backtesting engine
- Modular strategy architecture

### Frontend
- **React**
- **Vite**
- **TypeScript**
- **Axios**
- **Recharts** (for data visualization)
- Basic custom CSS styling

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

## Docs

Interactive API docs available at `/docs` when server is running.
