from flask import Blueprint, request
from ..useCases.coinbase import save_keys, delete_keys, get_coins

coinbase_routes_blueprint = Blueprint("coinbase", __name__)

@coinbase_routes_blueprint.route("/get_coins", methods=["POST"])
def get_coins_route():
    data = request.get_json()
    return get_coins(data)

@coinbase_routes_blueprint.route("/save_keys", methods=["POST"])
def save_keys_route():
    data = request.get_json()
    return save_keys(data)

@coinbase_routes_blueprint.route("/delete_keys", methods=["POST"])
def delete_keys_route():
    data = request.get_json()
    return delete_keys(data)