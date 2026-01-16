import pandas as pd

def calculate_metrics(trade_data: pd.DataFrame) -> pd.DataFrame:
    df = trade_data.copy()

    trades = df[df['PnL'] != 0]

    total_trades = len(trades)
    winning_trades = len(trades[trades['PnL'] > 0])
    losing_trades = len(trades[trades['PnL'] < 0])

    total_profit = trades[trades['PnL'] > 0]['PnL'].sum()
    total_loss = trades[trades['PnL'] < 0]['PnL'].sum()
    final_equity = total_profit + total_loss

    win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0

    cum_pnl = trades['PnL'].cumsum()
    peak = cum_pnl.cummax()
    drawdown = cum_pnl - peak
    max_drawdown = abs(drawdown.min()) if total_trades > 0 else 0

    return pd.DataFrame({
        'Total Trades': [total_trades],
        'Winning Trades': [winning_trades],
        'Losing Trades': [losing_trades],
        'Win Rate (%)': [win_rate],
        'Final Equity': [final_equity],
        'Max Drawdown': [max_drawdown]
    })