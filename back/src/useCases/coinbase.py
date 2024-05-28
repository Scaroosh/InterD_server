from flask import jsonify
from coinbase.rest import RESTClient
import os
from db_utils import get_users_database
from bson.objectid import ObjectId
from .auth import does_user_exist

users = get_users_database()

def do_keys_exist(id):
    user = users.find_one({"_id": ObjectId(id)})
    if ('coinbase' in user):
        if ('api_key' in user["coinbase"] and 'api_secret' in user["coinbase"]):
            return True
    return False

def save_keys(data):
    if data["id"] and data["api_key"] and data["api_secret"]:
        if does_user_exist(data["id"]):
            users.find_one_and_update({"_id": ObjectId(data["id"])}, { "$set": {"coinbase": {"api_key": data["api_key"], "api_secret": data["api_secret"]}}})
            return jsonify({"message": "Keys saved succesfully"}), 200
        else:
            return jsonify({"message": "User not found"}), 400
    return jsonify({"message": "Missing arguments"}), 400

def delete_keys(data):
    if does_user_exist(data["id"]):
        users.find_one_and_update({"_id": ObjectId(data["id"])}, { "$unset": {"coinbase": ""}})
        return jsonify({"message": "Keys removed succesfully"}), 200
    return jsonify({"message": "User not found"}), 400

def get_coins(data):
    if 'id' in data: # Get from database
        user = users.find_one({"_id": ObjectId(data["id"])})
        if do_keys_exist(data["id"]):
            api_key = user["coinbase"]["api_key"]
            api_secret = user["coinbase"]["api_secret"]
            client = RESTClient(api_key, api_secret, timeout=10)
            accounts = client.get_accounts()
            coins = []
            for account in accounts["accounts"]:
                if float(account["available_balance"]["value"]) != 0:
                    coins.append(account["available_balance"])
            return jsonify({"message": "Coins fetched from coinbase succesfully", "coins": coins}), 200
        return jsonify({"message": "User does not have api keys saved"}), 401

    elif not 'api_key' in data and not 'api_secret' in data:
        return jsonify({"message": "Missing keys"}), 400
    try:
        client = RESTClient(api_key=data["api_key"], api_secret=data["api_secret"], timeout=10)
        accounts = client.get_accounts()
        coins = []
        for account in accounts["accounts"]:
            if float(account["available_balance"]["value"]) != 0:
                coins.append(account["available_balance"])
        return jsonify({"message": "Coins fetched from coinbase succesfully", "coins": coins}), 200
    except:
        return jsonify({"message": "Couldn't retrieve coinbase information with keys"}), 401