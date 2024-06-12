import yfinance as yf
from abc import ABC, abstractmethod
from newspaper import Article
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import re
import time

class NewsSource(ABC):
    @abstractmethod
    def get_articles(self, ticker, max_articles):
        pass

    def get_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        if sentiment_polarity > 0:
            sentiment = "Positive"
        elif sentiment_polarity < 0:
            sentiment is "Negative"
        else:
            sentiment = "Neutral"
        return sentiment, sentiment_polarity

    def sanitize_filename(self, filename):
        return re.sub(r'[\\/*?:"<>|]', "", filename)

class YahooFinanceNews(NewsSource):
    def get_articles(self, ticker, max_articles):
        ticker_obj = yf.Ticker(ticker)
        news_sentiment_data = []
        news_articles = ticker_obj.news[:max_articles]
        for article in news_articles:
            article_url = article['link']
            news_article = Article(article_url)
            try:
                news_article.download()
                news_article.parse()
                article_text = news_article.text
                sentiment, sentiment_polarity = self.get_sentiment(article_text)
                article_data = {
                    'url': article_url,
                    'title': article['title'],
                    'text': news_article.text,
                    'sentiment': sentiment,
                    'sentiment_polarity': sentiment_polarity
                }
                news_sentiment_data.append(article_data)
            except Exception as e:
                continue
        return news_sentiment_data

class CryptoNews(NewsSource):
    def get_articles(self, ticker, max_articles):
        search_url = f'https://cryptonews.net/?q={ticker}&rubricId=-1'
        articles = self.scrape_articles_from_search(search_url, max_articles)
        return articles

    def scrape_article(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('h1', class_='article_title')
        title = title_tag.text.strip() if title_tag else "Title not found"
        title = self.sanitize_filename(title)
        article_text = ''
        article_content = soup.find('div', class_='content_text')
        if article_content:
            for p in article_content.find_all('p'):
                article_text += p.text.strip() + '\n'
        if not article_text.strip():
            return None
        sentiment, sentiment_polarity = self.get_sentiment(article_text)
        return {
            'url': url,
            'title': title,
            'text': article_text,
            'sentiment': sentiment,
            'sentiment_polarity': sentiment_polarity
        }

    def scrape_articles_from_search(self, url, max_articles=10):
        articles = []
        page = 1
        article_count = 0
        while True:
            page_url = f"{url}&page={page}"
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            page_articles = soup.find_all('div', class_='row news-item start-xs')
            if not page_articles:
                break
            for article in page_articles:
                article_url = article.find('a', href=True)['href']
                full_article_url = f"https://cryptonews.net{article_url}"
                article_data = self.scrape_article(full_article_url)
                if article_data:
                    articles.append(article_data)
                    article_count += 1
                    if article_count >= max_articles:
                        return articles
            page += 1
            time.sleep(2)
        return articles

class NewsManager:
    def __init__(self):
        self.sources = {
            'YahooFinance': YahooFinanceNews(),
            'CryptoNews': CryptoNews()
        }

    def get_news(self, ticker, source_name, max_articles=10):
        source = self.sources.get(source_name)
        if not source:
            raise ValueError(f"News source {source_name} is not supported.")
        return source.get_articles(ticker, max_articles)
