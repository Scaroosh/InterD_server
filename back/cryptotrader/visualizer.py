import plotly.graph_objs as go
from plotly.subplots import make_subplots

class Visualizer:
    @staticmethod
    def plot_data(data):
        """
        Create an interactive plot using Plotly.js
        
        Args:
            data (pd.DataFrame): DataFrame containing price and indicator data
        """
        # Determine the number of rows needed for subplots
        num_rows = 3
        if 'RSI' in data.columns:
            num_rows += 1

        # Create subplots
        fig = make_subplots(rows=num_rows, cols=1, 
                            shared_xaxes=True, 
                            vertical_spacing=0.05,
                            row_heights=[0.6, 0.2, 0.2] + ([0.2] if 'RSI' in data.columns else []))

        # Add candlestick chart
        fig.add_trace(go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'],
                                     name='Price'),
                      row=1, col=1)

        # Add volume bar chart
        fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume', marker_color='rgba(0,0,0,0.5)'),
                      row=2, col=1)

        # Add moving averages to main price chart if available
        if 'SMA_5' in data.columns:
            fig.add_trace(go.Scatter(x=data.index, y=data['SMA_5'], name='SMA 5', line=dict(color='red')),
                          row=1, col=1)
        if 'EMA_5' in data.columns:
            fig.add_trace(go.Scatter(x=data.index, y=data['EMA_5'], name='EMA 5', line=dict(color='purple')),
                          row=1, col=1)

        # Add Bollinger Bands if available
        if 'Upper_BB' in data.columns and 'Lower_BB' in data.columns:
            fig.add_trace(go.Scatter(x=data.index, y=data['Upper_BB'], name='Upper BB', 
                                     line=dict(color='rgba(0,0,255,0.3)'), mode='lines'),
                          row=1, col=1)
            fig.add_trace(go.Scatter(x=data.index, y=data['Lower_BB'], name='Lower BB', 
                                     line=dict(color='rgba(0,0,255,0.3)'), 
                                     fill='tonexty', fillcolor='rgba(0,0,255,0.1)', mode='lines'),
                          row=1, col=1)
            if 'Middle_BB' in data.columns:
                fig.add_trace(go.Scatter(x=data.index, y=data['Middle_BB'], name='Middle BB', 
                                         line=dict(color='rgba(0,0,255,0.5)', dash='dash'), mode='lines'),
                              row=1, col=1)

        # Add MACD if available
        if 'MACD' in data.columns and 'Signal' in data.columns and 'Hist' in data.columns:
            fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], name='MACD', line=dict(color='blue')),
                          row=3, col=1)
            fig.add_trace(go.Scatter(x=data.index, y=data['Signal'], name='Signal', line=dict(color='orange')),
                          row=3, col=1)
            fig.add_trace(go.Bar(x=data.index, y=data['Hist'], name='Histogram', marker_color='green'),
                          row=3, col=1)

        # Add RSI if available
        if 'RSI' in data.columns:
            fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], name='RSI'),
                          row=num_rows, col=1)
            fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought", row=num_rows, col=1)
            fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold", row=num_rows, col=1)

        # Update layout
        fig.update_layout(title='Stock Analysis',
                          xaxis_rangeslider_visible=False,
                          height=900 + (300 if 'RSI' in data.columns else 0),
                          width=1200,
                          showlegend=False)

        # Update y-axis labels
        fig.update_yaxes(title_text="Price", row=1, col=1)
        fig.update_yaxes(title_text="Volume", row=2, col=1)
        fig.update_yaxes(title_text="MACD", row=3, col=1)
        if 'RSI' in data.columns:
            fig.update_yaxes(title_text="RSI", row=num_rows, col=1)


        fig.show()


    def plot_portfolio_performance(self, price_data, portfolio_data):
        """
        Plot the asset price and portfolio value over time.
        
        :param price_data: DataFrame containing the asset price data
        :param portfolio_data: DataFrame containing the portfolio value data
        """
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, subplot_titles=('Asset Price', 'Portfolio Value'))

        # Plot asset price
        fig.add_trace(
            go.Scatter(x=price_data.index, y=price_data['Close'], name='Asset Price'),
            row=1, col=1
        )

        # Plot portfolio value
        fig.add_trace(
            go.Scatter(x=portfolio_data.index, y=portfolio_data['Value'], name='Portfolio Value'),
            row=2, col=1
        )

        fig.update_layout(height=800, title_text="Portfolio Performance", showlegend=True)
        fig.update_xaxes(title_text="Date", row=2, col=1)
        fig.update_yaxes(title_text="Price", row=1, col=1)
        fig.update_yaxes(title_text="Value", row=2, col=1)

        fig.show()


if __name__ == "__main__":
    from dataFeed import YahooFinanceDataStream
    from indicators import Indicators
    from datetime import datetime, timedelta

    # Fetch data
    yahoo_stream = YahooFinanceDataStream()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    symbol = "AAPL"
    interval = "1d"

    data = yahoo_stream.fetch_data(symbol, start_date, end_date, interval)

    # Calculate indicators
    data['SMA_5'] = Indicators.sma(data['Close'], 5)
    data['EMA_5'] = Indicators.ema(data['Close'], 5)
    data['RSI'] = Indicators.rsi(data['Close'])
    data['MACD'], data['Signal'], data['Hist'] = Indicators.macd(data['Close'])
    data['Upper_BB'], data['Middle_BB'], data['Lower_BB'] = Indicators.bollinger_bands(data['Close'])

    # Visualize data
    Visualizer.plot_data(data)
