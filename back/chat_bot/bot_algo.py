import json
import websocket
import pandas as pd
import talib
import yfinance as yf
from textblob import TextBlob
import requests
from newspaper import Article
import ssl
from datetime import datetime
import time
import threading

class TradingBot:
    def __init__(self, ticker, usdt_amount):
        self.ticker = ticker
        self.usdt_amount = usdt_amount
        self.in_position = False
        self.df = pd.DataFrame()
        self.buyorders = []
        self.sellorders = []
        self.ws = None
        self.paused = False
        self.pause_event = threading.Event()
        self.pause_event.set()  # not paused initially
        self.endpoint = 'wss://fstream.binance.com/ws'
        self.our_msg = json.dumps({'method': 'SUBSCRIBE', 'params': [f'{ticker}@ticker'], 'id':1})

    def fetch_historical_data(self, start_date, end_date):
        data = yf.download(self.ticker, start=start_date, end=end_date)
        data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
        data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
        data['EMA_20'] = talib.EMA(data['Close'], timeperiod=20)
        data['EMA_50'] = talib.EMA(data['Close'], timeperiod=50)
        data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
        macd, signal, hist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        data['MACD'] = macd
        data['MACD_Signal'] = signal
        data['MACD_Hist'] = hist
        return data

    def get_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        if sentiment_polarity > 0:
            sentiment = "Positive"
        elif sentiment_polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        return sentiment, sentiment_polarity

    def fetch_news_sentiment(self):
        news_sentiment_data = []
        ticker_obj = yf.Ticker(self.ticker)
        news_articles = ticker_obj.news
        for article in news_articles:
            article_url = article['link']
            news_article = Article(article_url)
            try:
                news_article.download()
                news_article.parse()
                article_text = news_article.text
                sentiment, sentiment_polarity = self.get_sentiment(article_text)
                news_sentiment_data.append({
                    'url': article_url,
                    'title': article['title'],
                    'text': article_text,
                    'sentiment': sentiment,
                    'sentiment_polarity': sentiment_polarity
                })
            except Exception as e:
                continue
        return news_sentiment_data

    def evaluate_trading_strategy(self):
        if len(self.df) < 20 or self.paused:
            return

        # Update technical indicators
        self.df['SMA_20'] = talib.SMA(self.df['price'], timeperiod=20)
        self.df['SMA_50'] = talib.SMA(self.df['price'], timeperiod=50)
        self.df['EMA_20'] = talib.EMA(self.df['price'], timeperiod=20)
        self.df['EMA_50'] = talib.EMA(self.df['price'], timeperiod=50)
        self.df['RSI'] = talib.RSI(self.df['price'], timeperiod=14)
        macd, signal, hist = talib.MACD(self.df['price'], fastperiod=12, slowperiod=26, signalperiod=9)
        self.df['MACD'] = macd
        self.df['MACD_Signal'] = signal
        self.df['MACD_Hist'] = hist

        last_row = self.df.iloc[-1]
        sentiment_score = self.evaluate_news_sentiment()

        if last_row['RSI'] < 30 and sentiment_score > 0.1 and not self.in_position:
            print(f"Buy at {last_row['price']} - RSI: {last_row['RSI']}, Sentiment: {sentiment_score}")
            self.buyorders.append(last_row['price'])
            self.in_position = True
        elif last_row['RSI'] > 70 or sentiment_score < -0.1 and self.in_position and len(self.buyorders) != 0:
            print(f"Sell at {last_row['price']} - RSI: {last_row['RSI']}, Sentiment: {sentiment_score}")
            self.sellorders.append(last_row['price'])
            self.in_position = False

    def evaluate_news_sentiment(self):
        news_sentiment_data = self.fetch_news_sentiment()
        sentiments = [article['sentiment_polarity'] for article in news_sentiment_data]
        return sum(sentiments) / len(sentiments) if sentiments else 0

    def on_open(self, ws):
        print(f"WebSocket connection opened for {self.ticker}")
        ws.send(self.our_msg)

    def on_message(self, ws, message):
        self.pause_event.wait()  # waits until the event is set (not paused)
        out = json.loads(message)
        out = pd.DataFrame({'price': float(out['c'])}, index=[pd.to_datetime(out['E'], unit='ms')])
        self.df = pd.concat([self.df, out], axis=0)
        print(self.df.tail())  # prints last 5 rows
        self.evaluate_trading_strategy()

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws):
        print("WebSocket connection closed")

    def start(self):
        self.ws = websocket.WebSocketApp(self.endpoint, 
                                         on_message=self.on_message, 
                                         on_open=self.on_open, 
                                         on_error=self.on_error, 
                                         on_close=self.on_close)
        # on my machine it doesn't work without ssl cerification disabling
        self.thread = threading.Thread(target=self.ws.run_forever, kwargs={'sslopt': {"cert_reqs": ssl.CERT_NONE}})
        self.thread.start()

    def stop(self):
        if self.ws:
            self.ws.close()
            self.thread.join()

    def pause(self):
        self.pause_event.clear()

    def resume(self):
        self.pause_event.set()


class BotManager:
    def __init__(self):
        self.bots = {}
        self.portfolio = {'cash': 0, 'positions': {}}

    def create_bot(self, ticker, usdt_amount):
        if ticker in self.bots:
            print(f"Bot for {ticker} already exists")
            return
        bot = TradingBot(ticker, usdt_amount)
        print("Bot is created")
        self.bots[ticker] = bot
        self.portfolio['cash'] += usdt_amount

    def start_bot(self, ticker):
        if ticker in self.bots:
            self.bots[ticker].start()

    def stop_bot(self, ticker):
        if ticker in self.bots:
            self.bots[ticker].stop()

    def pause_bot(self, ticker):
        if ticker in self.bots:
            self.bots[ticker].pause()
        print("Bot is paused")

    def resume_bot(self, ticker):
        if ticker in self.bots:
            self.bots[ticker].resume()
        print("Bot is resumed")

    def delete_bot(self, ticker):
        if ticker in self.bots:
            self.bots[ticker].stop()
            del self.bots[ticker]
            print(f"Bot for {ticker} deleted")

    def get_portfolio(self):
        return self.portfolio
