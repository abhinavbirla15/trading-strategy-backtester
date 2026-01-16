import pandas as pd

def exponential_moving_avg(prices: pd.Series, period: int) -> pd.Series:
    ema = prices.ewm(span=period, adjust=False).mean()
    return ema