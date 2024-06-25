import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

def main_page(ticker, start_date, end_date):
    st.header('Cryptocurrency Prediction')

    col1, col2 = st.columns([1, 9])
    with col1:
        st.image('chat_bot/icons/' + ticker + '.png', width=75)
    with col2:
        st.write(f"## {ticker}")


def display_about_data(ticker_obj, ticker, start_date, end_date):
    ticker_obj = yf.Ticker(ticker)
    info = ticker_obj.info
    st.write(f"**Description:** {info.get('description', 'N/A')}")
    st.write(f"**Previous Close:** ${info.get('previousClose', 'N/A'):.2f}")
    st.write(f"**Open:** ${info.get('open', 'N/A'):.2f}")
    st.write(f"**Day Low:** ${info.get('dayLow', 'N/A'):.2f}")
    st.write(f"**Day High:** ${info.get('dayHigh', 'N/A'):.2f}")
    st.write(f"**Volume:** {info.get('volume', 'N/A'):,}")
    st.write(f"**Regular Market Previous Close:** ${info.get('regularMarketPreviousClose', 'N/A'):.2f}")
    st.write(f"**Circulating Supply:** {info.get('circulatingSupply', 'N/A'):,}")
    st.write(f"**200 Day Average:** ${info.get('twoHundredDayAverage', 'N/A'):.2f}")
    st.write(f"**50 Day Average:** ${info.get('fiftyDayAverage', 'N/A'):.2f}")
    st.write(f"**Market Cap:** ${info.get('marketCap', 'N/A'):,}")

    raw_data = ticker_obj.history(start=start_date, end=end_date)
    fig = go.Figure(data=[go.Candlestick(x=raw_data.index, open=raw_data['Open'], high=raw_data['High'], low=raw_data['Low'], close=raw_data['Close'])])
    fig.update_layout(title=ticker + " candlestick : Open, High, Low and Close", yaxis_title=ticker + ' Price')
    st.plotly_chart(fig)

    history_data = raw_data.copy()
    history_data.index = pd.to_datetime(history_data.index, format='%Y-%m-%d %H:%M:%S').date
    history_data.index.name = "Date"
    history_data.sort_values(by='Date', ascending=False, inplace=True)
    st.write(history_data)
