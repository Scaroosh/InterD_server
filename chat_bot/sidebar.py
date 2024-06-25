import streamlit as st
from datetime import date, timedelta

# Sidebar Code
def sidebar():
    ticker = st.sidebar.selectbox('Select your Crypto', ["BTC-USD", "ETH-USD"])
    start_date = st.sidebar.date_input('Start Date', date.today() - timedelta(days=365))
    end_date = st.sidebar.date_input('End Date')
    return ticker, start_date, end_date
