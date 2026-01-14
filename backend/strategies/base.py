import pandas as pd
from .moving_avg import moving_avg

def base_strategy(ohlcv_data: pd.DataFrame, strategy_name: str) -> pd.DataFrame:

    if strategy_name != "moving_average":
        raise ValueError(f"Strategy '{strategy_name}' is not recognized.")
    
    df=ohlcv_data.copy()

    short_window = 20
    long_window = 50

    close_prices = df["Close"]

    df["SMA_Short"] = moving_avg(close_prices, short_window)
    df["SMA_Long"] = moving_avg(close_prices, long_window)

    df["Signal"] = 0

    buy_signal = (
        (df["SMA_Short"] > df["SMA_Long"]) &
        (df["SMA_Short"].shift(1) <= df["SMA_Long"].shift(1))
    )

    sell_signal = (
        (df["SMA_Short"] < df["SMA_Long"]) &
        (df["SMA_Short"].shift(1) >= df["SMA_Long"].shift(1))
    )

    df.loc[buy_signal, "Signal"] = 1
    df.loc[sell_signal, "Signal"] = -1

    return df