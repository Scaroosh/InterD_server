# from chat_bot.news_manager import NewsManager

# news_manager = NewsManager()
from db_utils import get_news_database

def fetch_news(data):
    ticker = data.get('ticker')
    source = data.get('source')
    if not ticker or not source:
        return {"message": "Missing ticker or source"}, 400
    try:
        db = get_news_database()
        articles = list(db.find({"source": source}, { "_id" : 0 }).sort([('timestamp', -1)]).limit(1))
        # articles = news_manager.get_news(ticker, source, max_articles)
        return {"articles": articles}, 200
    except ValueError as e:
        return {"message": str(e)}, 400
