from flask import Blueprint, request, jsonify
from ..useCases.bot import create_bot, start_bot, pause_bot, resume_bot, stop_bot, delete_bot, get_portfolio

bot_routes_blueprint = Blueprint("bot", __name__)

@bot_routes_blueprint.route("/create_bot", methods=["POST"])
def create_bot_route():
    data = request.get_json()
    owner_id = data.get('owner_id')
    ticker = data.get('ticker')
    usdt_amount = data.get('usdt_amount')
    if not owner_id or not ticker or not usdt_amount:
        return jsonify({"message": "Missing owner_id, ticker, or usdt_amount"}), 400
    result = create_bot(owner_id, ticker, usdt_amount)
    return jsonify(result), 200

@bot_routes_blueprint.route("/start_bot", methods=["POST"])
def start_bot_route():
    data = request.get_json()
    bot_id = data.get('bot_id')
    if not bot_id:
        return jsonify({"message": "Missing bot_id"}), 400
    result = start_bot(bot_id)
    return jsonify(result), 200

@bot_routes_blueprint.route("/pause_bot", methods=["POST"])
def pause_bot_route():
    data = request.get_json()
    bot_id = data.get('bot_id')
    if not bot_id:
        return jsonify({"message": "Missing bot_id"}), 400
    result = pause_bot(bot_id)
    return jsonify(result), 200

@bot_routes_blueprint.route("/resume_bot", methods=["POST"])
def resume_bot_route():
    data = request.get_json()
    bot_id = data.get('bot_id')
    if not bot_id:
        return jsonify({"message": "Missing bot_id"}), 400
    result = resume_bot(bot_id)
    return jsonify(result), 200

@bot_routes_blueprint.route("/stop_bot", methods=["POST"])
def stop_bot_route():
    data = request.get_json()
    bot_id = data.get('bot_id')
    if not bot_id:
        return jsonify({"message": "Missing bot_id"}), 400
    result = stop_bot(bot_id)
    return jsonify(result), 200

@bot_routes_blueprint.route("/delete_bot", methods=["POST"])
def delete_bot_route():
    data = request.get_json()
    bot_id = data.get('bot_id')
    if not bot_id:
        return jsonify({"message": "Missing bot_id"}), 400
    result = delete_bot(bot_id)
    return jsonify(result), 200

@bot_routes_blueprint.route("/portfolio", methods=["GET"])
def get_portfolio_route():
    result = get_portfolio()
    return jsonify(result), 200