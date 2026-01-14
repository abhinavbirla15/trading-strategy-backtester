from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.load_data import load_stock_data
from strategies.base import base_strategy

app = FastAPI(
    title="Trading Strategy Backtester",
    description="A Python-based trading strategy backtesting API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "Backend running successfully", "version": "0.1.0"}


@app.get("/api/v1/stock-data")
def generate_signals(
    symbol: str = Query(..., description="Stock ticker symbol (e.g., AAPL, GOOGL)"),
    start_date: str = Query(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD format"),
    strategy: str = Query("moving_average", description="Trading strategy to apply")
):
    """
    Generate trading signals based on the specified strategy.
    """
    try:
        ohlcv_data = load_stock_data(symbol.upper(), start_date, end_date)
        signals_data = base_strategy(ohlcv_data, strategy)
        # Convert NaN values to None for JSON compatibility
        signals_data = signals_data.replace({float('nan'): None})
        records = signals_data.to_dict(orient="records")
        return {
            "symbol": symbol.upper(),
            "start_date": start_date,
            "end_date": end_date,
            "strategy": strategy,
            "count": len(records),
            "data": records
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating signals: {str(e)}")