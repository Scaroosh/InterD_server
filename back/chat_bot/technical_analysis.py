import yfinance as yf
import plotly.graph_objects as go
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cryptotrader.indicators import Indicators

def technical_analysis(ticker, start_date, end_date):
    indicators = Indicators()
    data = yf.download(ticker, start=start_date, end=end_date)

    # Simple Moving Average (SMA)
    data['SMA_20'] = indicators.sma(data['Close'], 20)
    data['SMA_50'] = indicators.sma(data['Close'], 50)

    # Exponential Moving Average (EMA)
    data['EMA_20'] = indicators.ema(data['Close'], 20)
    data['EMA_50'] = indicators.ema(data['Close'], 50)

    # Relative Strength Index (RSI)
    data['RSI'] = indicators.rsi(data['Close'], 14)

    # Moving Average Convergence Divergence (MACD)
    macd, signal, hist = indicators.macd(data['Close'])
    data['MACD'] = macd
    data['MACD_Signal'] = signal
    data['MACD_Hist'] = hist

    candlestick = go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    )

    close_trace = go.Scatter(x=data.index, y=data['Close'], name='Close Price', mode='lines')
    sma_20_trace = go.Scatter(x=data.index, y=data['SMA_20'], name='SMA 20', mode='lines')
    sma_50_trace = go.Scatter(x=data.index, y=data['SMA_50'], name='SMA 50', mode='lines')
    ema_20_trace = go.Scatter(x=data.index, y=data['EMA_20'], name='EMA 20', mode='lines')
    ema_50_trace = go.Scatter(x=data.index, y=data['EMA_50'], name='EMA 50', mode='lines')
    rsi_trace = go.Scatter(x=data.index, y=data['RSI'], name='RSI')
    macd_trace = go.Scatter(x=data.index, y=data['MACD'], name='MACD')
    macd_signal_trace = go.Scatter(x=data.index, y=data['MACD_Signal'], name='MACD Signal')
    macd_hist_trace = go.Scatter(x=data.index, y=data['MACD_Hist'], name='MACD Histogram')

    layout = go.Layout(
        title=f"{ticker} Price and Technical Indicators",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=False
    )
    fig_data = [candlestick, close_trace, sma_20_trace, sma_50_trace, ema_20_trace, ema_50_trace, rsi_trace, macd_trace, macd_signal_trace, macd_hist_trace]
    fig = go.Figure(fig_data, layout=layout)

    st.plotly_chart(fig)
    return fig, fig_data