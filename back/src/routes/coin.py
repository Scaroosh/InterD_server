from flask import Blueprint, request
from ..useCases.coin import add_coin, delete_coin

coin_routes_blueprint = Blueprint("coin", __name__)

@coin_routes_blueprint.route("/add", methods=["POST"])
def add_coin_route():
    data = request.get_json()
    return add_coin(data)

@coin_routes_blueprint.route("/delete", methods=["DELETE"])
def delete_coin_route():
    data = request.get_json()
    return delete_coin(data)