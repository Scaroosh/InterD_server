from chat_bot.news_manager import NewsManager

news_manager = NewsManager()

def fetch_news(data):
    ticker = data.get('ticker')
    source = data.get('source')
    max_articles = data.get('max_articles', 10)
    if not ticker or not source:
        return {"message": "Missing ticker or source"}, 400
    try:
        articles = news_manager.get_news(ticker, source, max_articles)
        return {"articles": articles}, 200
    except ValueError as e:
        return {"message": str(e)}, 400
