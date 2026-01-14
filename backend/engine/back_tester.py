import pandas as pd

def back_tester(ohlcv_data: pd.DataFrame) -> pd.DataFrame:
    df=ohlcv_data.copy()

    df['position'] = 0
    df['entry_price'] = 0.0
    df['exit_price'] = 0.0
    df['PnL'] = 0.0
    
    entry_price = 0.0
    in_position = False
    
    for index in range(len(df)-1):

        signal = df.iloc[index]['Signal']

        if in_position:
            df.loc[index+1, 'position'] = 1
        
        if signal == 1 and not in_position:
            df.loc[index+1, 'entry_price'] = df.loc[index+1, 'Open']
            entry_price = df.loc[index+1, 'entry_price']
            in_position = True

        elif signal == -1 and in_position:
            df.loc[index+1, 'exit_price'] = df.loc[index+1, 'Close']
            df.loc[index+1, 'PnL'] = df.loc[index+1, 'exit_price'] - entry_price
            df.loc[index+1, 'position'] = 0
            in_position = False
    
    if in_position:
        exit_price = df.iloc[-1]['Close']
        df.loc[df.index[-1], 'exit_price'] = exit_price
        df.loc[df.index[-1], 'PnL'] = exit_price - entry_price
        df.loc[df.index[-1], 'position'] = 0

    return df
    