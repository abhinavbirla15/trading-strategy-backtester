import pandas as pd

def moving_avg(close_data: pd.DataFrame, window_size: int = 20) -> pd.DataFrame:
    
    if close_data is None or close_data.empty:
        raise ValueError("Input DataFrame is empty or None.")
    
    return close_data.rolling(window=window_size).mean()

def get_moving_average_signals(ohlcv_data: pd.DataFrame) -> pd.DataFrame:

    close_prices = ohlcv_data["Close"]

    ohlcv_data["SMA_Short"] = moving_avg(close_prices, 20)
    ohlcv_data["SMA_Long"] = moving_avg(close_prices, 50)

    ohlcv_data["Signal"] = 0

    buy_signal = (
        (ohlcv_data["SMA_Short"] > ohlcv_data["SMA_Long"]) &
        (ohlcv_data["SMA_Short"].shift(1) <= ohlcv_data["SMA_Long"].shift(1))
    )

    sell_signal = (
        (ohlcv_data["SMA_Short"] < ohlcv_data["SMA_Long"]) &
        (ohlcv_data["SMA_Short"].shift(1) >= ohlcv_data["SMA_Long"].shift(1))
    )

    ohlcv_data.loc[buy_signal, "Signal"] = 1
    ohlcv_data.loc[sell_signal, "Signal"] = -1
    return ohlcv_data