# Trading Strategy Backtester

A Python API for fetching historical stock data using FastAPI and yfinance.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

## API

### Health Check

```
GET /
```

### Get Stock Data

```
GET /api/v1/stock-data?symbol=AAPL&start_date=2024-01-01&end_date=2024-06-01&limit=100
```

Parameters:

- `symbol` - Stock ticker (required)
- `start_date` - YYYY-MM-DD format (required)
- `end_date` - YYYY-MM-DD format (required)
- `limit` - Max records, default 100 (optional)

## Docs

Interactive API docs available at `/docs` when server is running.
