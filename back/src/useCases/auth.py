from flask import jsonify
from db_utils import get_users_database
from bson.objectid import ObjectId

users = get_users_database()

def does_username_exist(username):
    res = users.find_one({"username": username})
    return res is not None

def does_email_exist(email):
    res = users.find_one({"email": email})
    return res is not None

def does_email_and_password_exist(email, password):
    res = users.find_one({"email": email, "password": password})
    return res is not None

def does_username_and_password_exist(username, password):
    res = users.find_one({"username": username, "password": password})
    return res is not None

def get_user_id_by_email(email, password):
    res = users.find_one({"email": email, "password": password})
    return str(res["_id"])

def get_user_id_by_username(username, password):
    res = users.find_one({"username": username, "password": password})
    return str(res["_id"])

def does_user_exist(id):
    res = users.find_one({"_id": ObjectId(id)})
    return res is not None

def register(data):
    if not does_email_exist(data["email"]) and not does_username_exist(data["username"]):
        users.insert_one(
            {
                "email": data["email"],
                "username": data["username"],
                "password": data["password"],
            }
        )
        return jsonify({"message": "Register successful!"}), 201

    return jsonify({"message": "An account with that email already exists!"}), 400

def login(data):
    if "email" in data and does_email_and_password_exist(data["email"], data["password"]):
        user_id = get_user_id_by_email(data["email"], data["password"])
        return jsonify({"message": "Successfully Logged In", "user_id": user_id}), 200
    if "username" in data and does_username_and_password_exist(data["username"], data["password"]):
        user_id = get_user_id_by_username(data["email"], data["password"])
        return jsonify({"message": "Successfully Logged In", "user_id": user_id}), 200

    return jsonify({"message": "Incorrect login or password"}), 400

def delete(data):
    if does_user_exist(data["user_id"]):
        users.delete_one({
            "_id": ObjectId(data["user_id"])
        })
        return jsonify({"message": "Successfully deleted id" + data["user_id"]}), 200
    return jsonify({"message": "User not found"}), 400