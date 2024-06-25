from datetime import datetime, timedelta
import pandas as pd

class Indicators:
    @staticmethod
    def sma(data: pd.Series, period: int) -> pd.Series:
        """
        Simple Moving Average (SMA)
        
        Args:
            data (pd.Series): Price series
            period (int): Number of periods for SMA calculation
        
        Returns:
            pd.Series: SMA values
        """
        return data.rolling(window=period).mean()

    @staticmethod
    def ema(data: pd.Series, period: int) -> pd.Series:
        """
        Exponential Moving Average (EMA)
        
        Args:
            data (pd.Series): Price series
            period (int): Number of periods for EMA calculation
        
        Returns:
            pd.Series: EMA values
        """
        return data.ewm(span=period, adjust=False).mean()

    @staticmethod
    def rsi(data: pd.Series, period: int = 14) -> pd.Series:
        """
        Relative Strength Index (RSI)
        
        Args:
            data (pd.Series): Price series
            period (int): Number of periods for RSI calculation (default: 14)
        
        Returns:
            pd.Series: RSI values
        """
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def stochastic_oscillator(high: pd.Series, low: pd.Series, close: pd.Series, k_period: int = 14, d_period: int = 3) -> tuple:
        """
        Stochastic Oscillator
        
        Args:
            high (pd.Series): High price series
            low (pd.Series): Low price series
            close (pd.Series): Close price series
            k_period (int): Number of periods for %K line (default: 14)
            d_period (int): Number of periods for %D line (default: 3)
        
        Returns:
            tuple: (%K, %D) Stochastic Oscillator values
        """
        lowest_low = low.rolling(window=k_period).min()
        highest_high = high.rolling(window=k_period).max()
        
        k = 100 * ((close - lowest_low) / (highest_high - lowest_low))
        d = k.rolling(window=d_period).mean()
        
        return k, d

    @staticmethod
    def macd(data: pd.Series, fast_period: int = 12, slow_period: int = 26, signal_period: int = 9) -> tuple:
        """
        Moving Average Convergence Divergence (MACD)
        
        Args:
            data (pd.Series): Price series
            fast_period (int): Number of periods for fast EMA (default: 12)
            slow_period (int): Number of periods for slow EMA (default: 26)
            signal_period (int): Number of periods for signal line (default: 9)
        
        Returns:
            tuple: (MACD line, Signal line, MACD histogram)
        """
        ema_fast = Indicators.ema(data, fast_period)
        ema_slow = Indicators.ema(data, slow_period)
        
        macd_line = ema_fast - ema_slow
        signal_line = Indicators.ema(macd_line, signal_period)
        macd_histogram = macd_line - signal_line
        
        return macd_line, signal_line, macd_histogram

    @staticmethod
    def bollinger_bands(data: pd.Series, period: int = 20, num_std: float = 2) -> tuple:
        """
        Bollinger Bands
        
        Args:
            data (pd.Series): Price series
            period (int): Number of periods for moving average (default: 20)
            num_std (float): Number of standard deviations for bands (default: 2)
        
        Returns:
            tuple: (Upper Band, Middle Band, Lower Band)
        """
        middle_band = Indicators.sma(data, period)
        std_dev = data.rolling(window=period).std()
        
        upper_band = middle_band + (std_dev * num_std)
        lower_band = middle_band - (std_dev * num_std)
        
        return upper_band, middle_band, lower_band

    @staticmethod
    def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
        """
        Average True Range (ATR)
        
        Args:
            high (pd.Series): High price series
            low (pd.Series): Low price series
            close (pd.Series): Close price series
            period (int): Number of periods for ATR calculation (default: 14)
        
        Returns:
            pd.Series: ATR values
        """
        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())
        
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()
        
        return atr

if __name__ == "__main__":
    from dataFeed import DataFetchException, YahooFinanceDataStream
    yahoo_stream = YahooFinanceDataStream()

    # Fetch daily data for the last month
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    symbol = "BTC-USD"
    interval = "1h"

    try:
        data = yahoo_stream.fetch_data(symbol, start_date, end_date, interval)
        print(f"Fetched {len(data)} rows of {interval} data for {symbol}")
        print(data.head())

        # Calculate indicators
        data['SMA_5'] = Indicators.sma(data['Close'], 5)
        data['EMA_5'] = Indicators.ema(data['Close'], 5)
        data['RSI'] = Indicators.rsi(data['Close'])
        data['Stoch_K'], data['Stoch_D'] = Indicators.stochastic_oscillator(data['High'], data['Low'], data['Close'])
        data['MACD'], data['Signal'], data['Hist'] = Indicators.macd(data['Close'])
        data['Upper_BB'], data['Middle_BB'], data['Lower_BB'] = Indicators.bollinger_bands(data['Close'])
        data['ATR'] = Indicators.atr(data['High'], data['Low'], data['Close'])

        print(data)

        # Change granularity to weekly
        weekly_data = yahoo_stream.change_interval(data, "1wk")
        print(f"\nChanged granularity to weekly:")
        print(weekly_data)

        # Print available intervals
        print(f"\nAvailable intervals: {yahoo_stream.get_available_intervals()}")
    except DataFetchException as e:
        print(f"Error: {e}")