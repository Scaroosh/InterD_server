# executes trader based on strategy signals
import pandas as pd
from strategy import Strategy
from portfolio import Portfolio

class Trader:
    def __init__(self, strategy: Strategy, portfolio: Portfolio):
        self.strategy = strategy
        self.portfolio = portfolio

    def backtest(self, data: pd.DataFrame):
        signals = self.strategy.generate_signals(data)
        for date, signal in signals.items():
            price = data.loc[date, 'Close']
            if signal == 1:  # Buy signal
                self.portfolio.buy('CRYPTO', 1, price, date)
            elif signal == -1:  # Sell signal
                self.portfolio.sell('CRYPTO', 1, price, date)

        self.portfolio.calculate_returns(data)
