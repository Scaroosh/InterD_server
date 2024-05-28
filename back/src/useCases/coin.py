from flask import jsonify
from db_utils import get_users_database
from .auth import does_user_exist
from bson.objectid import ObjectId

users = get_users_database()

def add_coin(data):
    if does_user_exist(data["id"]):
        users.find_one_and_update({"_id": ObjectId(data["id"])}, { "$set": {"wallet": {"coins": data["coins"]}}})
        return jsonify({"message": "Coins updated succesfully."}), 200
    return jsonify({"message": "User does not exist"}), 400

def delete_coin(data):
    if does_user_exist(data["id"]):
        users.find_one_and_update({"_id": ObjectId(data["id"])}, { "$unset": {"wallet": {"coins": data["coin"]}}})
        return jsonify({"message": "Coin removed succesfully."}), 200
    return jsonify({"message": "User does not exist"}), 400