import streamlit as st
from news_manager import NewsManager

# Initialize NewsManager
news_manager = NewsManager()

# Streamlit UI
st.title("Crypto News Sentiment Analysis")

# User Inputs
ticker = st.text_input("Enter Ticker Symbol (e.g., BTC-USD):")
source = st.selectbox("Select News Source", ["YahooFinance", "CryptoNews"])
max_articles = st.number_input("Number of Articles", min_value=1, value=10)

if st.button("Get News Sentiment"):
    if not ticker or not source:
        st.error("Please provide both ticker symbol and news source.")
    else:
        try:
            articles = news_manager.get_news(ticker, source, max_articles)
            for article in articles:
                with st.expander(article['title']):
                    st.write(f"**URL:** {article['url']}")
                    st.write(f"**Sentiment:** {article['sentiment']} **Sentiment Polarity:** {article['sentiment_polarity']}")
                    st.write(article['text'])
        except Exception as e:
            st.error(f"Error: {str(e)}")
