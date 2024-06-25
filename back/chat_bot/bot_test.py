import streamlit as st
from bot_algo import BotManager

# Initialize BotManager
if 'bot_manager' not in st.session_state:
    st.session_state.bot_manager = BotManager()

# Streamlit UI
st.title("Crypto Trading Bot Manager")

# Create Bot Section
st.header("Create a New Bot")
ticker = st.selectbox("Select Ticker", ["btcusdt", "ethusdt"])
usdt_amount = st.number_input("USDT Amount", min_value=1, value=1000)
if st.button("Create Bot"):
    st.session_state.bot_manager.create_bot(ticker, usdt_amount)
    if 'created_bots' not in st.session_state:
        st.session_state.created_bots = []
    st.session_state.created_bots.append(ticker)
    st.success(f"Bot for {ticker} created with {usdt_amount} USDT")

# Update selectbox options based on created bots
created_bots = st.session_state.created_bots if 'created_bots' in st.session_state else []

# Start Bot Section
st.header("Start Bot")
start_ticker = st.selectbox("Select Bot to Start", created_bots)
if st.button("Start Bot"):
    st.session_state.bot_manager.start_bot(start_ticker)
    st.success(f"Bot for {start_ticker} started")

# Pause Bot Section
st.header("Pause Bot")
pause_ticker = st.selectbox("Select Bot to Pause", created_bots)
if st.button("Pause Bot"):
    st.session_state.bot_manager.pause_bot(pause_ticker)
    st.success(f"Bot for {pause_ticker} paused")

# Resume Bot Section
st.header("Resume Bot")
resume_ticker = st.selectbox("Select Bot to Resume", created_bots)
if st.button("Resume Bot"):
    st.session_state.bot_manager.resume_bot(resume_ticker)
    st.success(f"Bot for {resume_ticker} resumed")

# Stop Bot Section
st.header("Stop Bot")
stop_ticker = st.selectbox("Select Bot to Stop", created_bots)
if st.button("Stop Bot"):
    st.session_state.bot_manager.stop_bot(stop_ticker)
    st.success(f"Bot for {stop_ticker} stopped")

# Delete Bot Section
st.header("Delete Bot")
delete_ticker = st.selectbox("Select Bot to Delete", created_bots)
if st.button("Delete Bot"):
    st.session_state.bot_manager.delete_bot(delete_ticker)
    st.session_state.created_bots.remove(delete_ticker)
    st.success(f"Bot for {delete_ticker} deleted")

# Display Portfolio
st.header("Portfolio")
portfolio = st.session_state.bot_manager.get_portfolio()
st.write(portfolio)
