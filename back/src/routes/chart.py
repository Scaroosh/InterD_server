from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import json

chart_routes_blueprint = Blueprint('chart_routes', __name__)

def fetch_financial_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data, slow=26, fast=12, signal=9):
    exp1 = data['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = data['Close'].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    hist = macd - signal_line
    return macd, signal_line, hist

def generate_plot(data, ticker, indicators):
    rows = 1 + sum(indicators.values())
    row = 1
    fig = make_subplots(rows=rows, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Candlestick'), row=row, col=1)
    row += 1

    if indicators.get('volume'):
        fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume'), row=row, col=1)
        row += 1

    if indicators.get('rsi'):
        rsi = calculate_rsi(data)
        fig.add_trace(go.Scatter(x=data.index, y=rsi, mode='lines', name='RSI'), row=row, col=1)
        row += 1

    if indicators.get('macd'):
        macd, signal, hist = calculate_macd(data)
        fig.add_trace(go.Scatter(x=data.index, y=macd, mode='lines', name='MACD Line'), row=row, col=1)
        fig.add_trace(go.Scatter(x=data.index, y=signal, mode='lines', name='Signal Line'), row=row, col=1)
        fig.add_trace(go.Bar(x=data.index, y=hist, name='Histogram'), row=row, col=1)
        row += 1

    fig.update_layout(height=200 * rows, title=f"{ticker} Stock Data")
    return fig.to_json()

@chart_routes_blueprint.route('/data', methods=['POST'])
def get_data():
    request_data = request.json
    ticker = request_data['ticker']
    days = int(request_data.get('days', 30))
    indicators = request_data.get('indicators', {})

    # Validate ticker
    try:
        yf.Ticker(ticker).info
    except:
        return jsonify({"error": "Invalid ticker symbol"}), 400

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    data = fetch_financial_data(ticker, start_date, end_date)
    plot_json = generate_plot(data, ticker, indicators)
    return jsonify(plot_json)