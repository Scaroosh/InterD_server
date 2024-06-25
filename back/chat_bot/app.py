import streamlit as st
import yfinance as yf
from sidebar import sidebar
from main_about import main_page, display_about_data
from technical_analysis import technical_analysis
from news import global_news_tab, news_search_tab
from chatbot import chatbot

def main():
    ticker, start_date, end_date = sidebar()
    main_page(ticker, start_date, end_date)

    ticker_obj = yf.Ticker(ticker)
    about_data, global_news, news_search, chatbot_tab = st.tabs(["About", "Global News", "News with Search", "ChatBot"])

    with about_data:
        display_about_data(ticker_obj, ticker, start_date, end_date)
        technical_analysis(ticker, start_date, end_date)
    
    with global_news:
        global_news_tab(ticker_obj)

    with news_search:
        news_search_tab()
    
    with chatbot_tab:
        chatbot()

if __name__ == "__main__":
    main()
