from chat_bot.bot_algo import BotManager

bot_manager = BotManager()

def create_bot(ticker, usdt_amount):
    bot_manager.create_bot(ticker, usdt_amount)
    return {"message": f"Bot for {ticker} created with {usdt_amount} USDT"}

def start_bot(ticker):
    bot_manager.start_bot(ticker)
    return {"message": f"Bot for {ticker} started"}

def pause_bot(ticker):
    bot_manager.pause_bot(ticker)
    return {"message": f"Bot for {ticker} paused"}

def resume_bot(ticker):
    bot_manager.resume_bot(ticker)
    return {"message": f"Bot for {ticker} resumed"}

def stop_bot(ticker):
    bot_manager.stop_bot(ticker)
    return {"message": f"Bot for {ticker} stopped"}

def delete_bot(ticker):
    bot_manager.delete_bot(ticker)
    return {"message": f"Bot for {ticker} deleted"}

def get_portfolio():
    portfolio = bot_manager.get_portfolio()
    return portfolio
