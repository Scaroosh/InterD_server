# generates signals to buy and sell
from abc import ABC, abstractmethod
import pandas as pd
from indicators import Indicators

class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        pass

class RSIStrategy(Strategy):
    def __init__(self, rsi_period: int = 14, overbought: int = 70, oversold: int = 30):
        self.rsi_period = rsi_period
        self.overbought = overbought
        self.oversold = oversold

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        rsi = Indicators.rsi(data['Close'], self.rsi_period)
        signals = pd.Series(index=data.index, dtype=int)
        signals.loc[rsi < self.oversold] = 1  # Buy signal
        signals.loc[rsi > self.overbought] = -1  # Sell signal
        signals.fillna(0, inplace=True)  # No signal
        return signals
