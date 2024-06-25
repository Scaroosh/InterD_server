from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

class DataStream(ABC):
    """
    Abstract base class for data streams.
    """

    @abstractmethod
    def fetch_data(self, symbol: str, start_date: datetime, end_date: datetime, interval: str) -> pd.DataFrame:
        """
        Fetch historical data for a given symbol and time range.

        Args:
            symbol (str): The ticker symbol of the asset.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.
            interval (str): The data granularity (e.g., '1d', '1h', '15m').

        Returns:
            pd.DataFrame: Historical data with columns: Open, High, Low, Close, Volume.
        """
        pass

    @abstractmethod
    def get_available_intervals(self) -> list:
        """
        Get a list of available data intervals.

        Returns:
            list: List of available interval strings.
        """
        pass

    @abstractmethod
    def change_interval(self, data: pd.DataFrame, new_interval: str) -> pd.DataFrame:
        """
        Change the granularity of the data.

        Args:
            data (pd.DataFrame): The original data.
            new_interval (str): The new interval to convert the data to.

        Returns:
            pd.DataFrame: Resampled data with the new interval.
        """
        pass

class DataFetchException(Exception):
    """Custom exception for data fetching errors."""
    pass

class YahooFinanceDataStream(DataStream):
    """
    Implementation of DataStream for Yahoo Finance.
    """

    def __init__(self):
        self.available_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

    def fetch_data(self, symbol: str, start_date: datetime, end_date: datetime, interval: str) -> pd.DataFrame:
        if interval not in self.available_intervals:
            raise ValueError(f"Invalid interval. Available intervals are: {self.available_intervals}")

        # Check for 1-minute data restriction
        if interval == '1m' and (end_date - start_date).days > 7:
            raise DataFetchException(f"{symbol}: 1m data not available for start_date={start_date} and end_date={end_date}. Only 7 days worth of 1m granularity data are allowed to be fetched per request.")

        # Check for 15-minute data restriction
        if interval == '15m' and (end_date - start_date).days > 60:
            raise DataFetchException(f"{symbol}: 15m data not available for start_date={start_date} and end_date={end_date}. Only 60 days worth of 15m granularity data are allowed to be fetched per request.")

        try:
            data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
            if data.empty:
                raise DataFetchException(f"No data found for {symbol} with interval {interval} from {start_date} to {end_date}.")
            return data
        except Exception as e:
            raise DataFetchException(f"Failed to fetch data for {symbol}: {str(e)}")

    def get_available_intervals(self) -> list:
        return self.available_intervals

    def change_interval(self, data: pd.DataFrame, new_interval: str) -> pd.DataFrame:
        if new_interval not in self.available_intervals:
            raise ValueError(f"Invalid interval. Available intervals are: {self.available_intervals}")

        # Define a mapping of interval strings to pandas offset aliases
        interval_mapping = {
            '1m': '1T', '2m': '2T', '5m': '5T', '15m': '15T', '30m': '30T',
            '60m': '60T', '90m': '90T', '1h': '1H', '1d': '1D',
            '5d': '5D', '1wk': 'W', '1mo': 'M', '3mo': '3M'
        }

        # Resample the data to the new interval
        resampled_data = data.resample(interval_mapping[new_interval]).agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Volume': 'sum'
        })

        return resampled_data.dropna()

if __name__ == "__main__":
    yahoo_stream = YahooFinanceDataStream()

    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    symbol = "BTC-USD"
    interval = "1m"

    try:
        data = yahoo_stream.fetch_data(symbol, start_date, end_date, interval)
        print(f"Fetched {len(data)} rows of {interval} data for {symbol}")
        print(data.head())

        weekly_data = yahoo_stream.change_interval(data, "1h")
        print(f"\nChanged granularity to weekly:")
        print(weekly_data)

        print(f"\nAvailable intervals: {yahoo_stream.get_available_intervals()}")
    except DataFetchException as e:
        print(f"Error: {e}")
