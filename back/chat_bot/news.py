import streamlit as st
from newspaper import Article
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import time
import re

def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, sentiment_polarity

def global_news_tab(ticker_obj): # Global News from YFinance
    news_sentiment_data = []
    news_articles = ticker_obj.news
    for article in news_articles:
        article_url = article['link']
        news_article = Article(article_url)
        try:
            news_article.download()
            news_article.parse()
            article_text = news_article.text
            sentiment, sentiment_polarity = get_sentiment(article_text)
            article_data = {
                'url': article_url,
                'title': article['title'],
                'text': news_article.text,
                'sentiment': sentiment,
                'sentiment_polarity': sentiment_polarity
            }
            news_sentiment_data.append(article_data)
            with st.expander(article['title']):
                st.write(f"**Sentiment:** {sentiment} **Sentiment Polarity:** {sentiment_polarity}")
                st.write(news_article.text)
        except Exception as e:
            st.error(f"Error fetching article: {e}")
            st.markdown("---")

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# from cryptonews.net
def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('h1', class_='article_title')
    title = title_tag.text.strip() if title_tag else "Title not found"
    title = sanitize_filename(title)
    article_text = ''
    article_content = soup.find('div', class_='content_text')
    if article_content:
        for p in article_content.find_all('p'):
            article_text += p.text.strip() + '\n'
    if not article_text.strip():
        return None
    sentiment, sentiment_polarity = get_sentiment(article_text)
    return {
        'url': url,
        'title': title,
        'text': article_text,
        'sentiment': sentiment,
        'sentiment_polarity': sentiment_polarity
    }

def scrape_articles_from_search(url, max_articles=10):
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
            article_data = scrape_article(full_article_url)
            if article_data:
                articles.append(article_data)
                article_count += 1
                if article_count >= max_articles:
                    return articles
        page += 1
        time.sleep(2)
    return articles

def news_search_tab():
    query = st.text_input("Enter search keywords:")
    rubric_id = "-1"
    max_articles = st.number_input("Enter the maximum number of articles to scrape:", min_value=1, value=10)
    if query and rubric_id:
        search_url = f'https://cryptonews.net/?q={query}&rubricId={rubric_id}'
        articles = scrape_articles_from_search(search_url, max_articles)
        for article in articles:
            with st.expander(article['title']):
                st.write(f"**URL:** {article['url']}")
                st.write(f"**Sentiment:** {article['sentiment']} **Sentiment Polarity:** {article['sentiment_polarity']}")
                st.write(article['text'])
