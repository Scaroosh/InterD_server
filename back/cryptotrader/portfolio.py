import pandas as pd

class Portfolio:
    def __init__(self, initial_cash: float):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.holdings = {}
        self.trades = []

    def buy(self, symbol: str, amount: float, price: float, date: pd.Timestamp):
        cost = amount * price
        if cost <= self.cash:
            self.cash -= cost
            self.holdings[symbol] = self.holdings.get(symbol, 0) + amount
            self.trades.append({
                'date': date,
                'symbol': symbol,
                'action': 'buy',
                'amount': amount,
                'price': price
            })
        else:
            print(f"Insufficient funds to buy {amount} {symbol} at {price}")

    def sell(self, symbol: str, amount: float, price: float, date: pd.Timestamp):
        if symbol in self.holdings and self.holdings[symbol] >= amount:
            self.cash += amount * price
            self.holdings[symbol] -= amount
            self.trades.append({
                'date': date,
                'symbol': symbol,
                'action': 'sell',
                'amount': amount,
                'price': price
            })
        else:
            print(f"Insufficient {symbol} to sell {amount}")

    def calculate_returns(self, data: pd.DataFrame):
        portfolio_value = pd.Series(index=data.index, dtype=float)
        for date in data.index:
            value = self.cash
            for symbol, amount in self.holdings.items():
                value += amount * data.loc[date, 'Close']
            portfolio_value[date] = value

        self.returns = portfolio_value.pct_change()
        self.cumulative_returns = (1 + self.returns).cumprod() - 1
        self.total_return = self.cumulative_returns.iloc[-1]

    def print_summary(self):
        print(f"Initial Cash: ${self.initial_cash:.2f}")
        print(f"Final Cash: ${self.cash:.2f}")
        print("Holdings:")
        for symbol, amount in self.holdings.items():
            print(f"  {symbol}: {amount}")
        print(f"Total Return: {self.total_return:.2%}")
        print(f"Number of Trades: {len(self.trades)}")

if __name__ == "__main__":
    from dataFeed import YahooFinanceDataStream
    from strategy import RSIStrategy
    from trader import Trader
    from portfolio import Portfolio
    from visualizer import Visualizer
    from datetime import datetime, timedelta

    # Fetch historical data
    data_feed = YahooFinanceDataStream()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    data = data_feed.fetch_data("MSFT", start_date, end_date, "1m")

    # Initialize strategy, portfolio, and trader
    strategy = RSIStrategy(rsi_period=14, overbought=70, oversold=30)
    portfolio = Portfolio(initial_cash=1000000)
    trader = Trader(strategy, portfolio)

    # Run backtest
    trader.backtest(data)

    # Print results
    portfolio.print_summary()

    # Prepare portfolio value data
    portfolio_value = pd.DataFrame(index=data.index)
    portfolio_value['Value'] = portfolio.cash
    for date in data.index:
        for symbol, amount in portfolio.holdings.items():
            portfolio_value.loc[date, 'Value'] += amount * data.loc[date, 'Close']

    # Visualize results
    visualizer = Visualizer()
    visualizer.plot_data(data)
    visualizer.plot_portfolio_performance(data, portfolio_value)
