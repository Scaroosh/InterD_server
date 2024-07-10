from flask import jsonify
from db_utils import get_bots_database, get_users_database
from bson.objectid import ObjectId
from chat_bot.bot_algo import BotManager
from .auth import does_user_exist
bot_manager = BotManager()
bots = get_bots_database()
users = get_users_database()

def create_bot(owner_id, ticker, usdt_amount):
    if not does_user_exist(owner_id):
        return {"message": "Owner not found"}
    
    bot_id = bots.insert_one({
        "owner": ObjectId(owner_id),
        "ticker": ticker,
        "amount": usdt_amount,
        "active": False
    }).inserted_id
    bot_manager.create_bot(ticker, usdt_amount)
    return {"message": f"Bot for {ticker} created with {usdt_amount} USDT", "bot_id": str(bot_id)}

def start_bot(bot_id):
    bot_data = get_bot_data(bot_id)
    if not bot_data:
        return {"message": "Bot not found"}
    bot_manager.start_bot(bot_data['ticker'])
    bots.update_one({"_id": ObjectId(bot_id)}, {"$set": {"active": True}})
    return {"message": f"Bot {bot_id} started"}

def pause_bot(bot_id):
    bot_data = get_bot_data(bot_id)
    if not bot_data:
        return {"message": "Bot not found"}
    bot_manager.pause_bot(bot_data['ticker'])
    return {"message": f"Bot {bot_id} paused"}

def resume_bot(bot_id):
    bot_data = get_bot_data(bot_id)
    if not bot_data:
        return {"message": "Bot not found"}
    bot_manager.resume_bot(bot_data['ticker'])
    return {"message": f"Bot {bot_id} resumed"}

def stop_bot(bot_id):
    bot_data = get_bot_data(bot_id)
    if not bot_data:
        return {"message": "Bot not found"}
    bot_manager.stop_bot(bot_data['ticker'])
    bots.update_one({"_id": ObjectId(bot_id)}, {"$set": {"active": False}})
    return {"message": f"Bot {bot_id} stopped"}

def delete_bot(bot_id):
    bot_data = get_bot_data(bot_id)
    if not bot_data:
        return {"message": "Bot not found"}
    bot_manager.delete_bot(bot_data['ticker'])
    bots.delete_one({"_id": ObjectId(bot_id)})
    return {"message": f"Bot {bot_id} deleted"}

def get_portfolio():
    portfolio = bot_manager.get_portfolio()
    return portfolio

def get_bot_data(bot_id):
    return bots.find_one({"_id": ObjectId(bot_id)})