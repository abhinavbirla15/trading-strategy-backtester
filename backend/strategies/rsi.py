import pandas as pd

def relative_strength_index(prices: pd.Series, period: int = 14) -> pd.Series:
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_rsi_signals(ohlcv_data: pd.DataFrame) -> pd.DataFrame:

    close_prices = ohlcv_data["Close"]
    ohlcv_data["RSI"] = relative_strength_index(close_prices, period=14)

    ohlcv_data["Signal"] = 0

    buy_signal = ohlcv_data["RSI"] < 30
    sell_signal = ohlcv_data["RSI"] > 70

    ohlcv_data.loc[buy_signal, "Signal"] = 1
    ohlcv_data.loc[sell_signal, "Signal"] = -1
    return ohlcv_data