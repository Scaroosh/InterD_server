from flask import Blueprint, request
from ..useCases.auth import register, login, delete

auth_routes_blueprint = Blueprint("auth", __name__)

@auth_routes_blueprint.route("/register", methods=["POST"])
def register_route():
    data = request.get_json()
    return register(data)

@auth_routes_blueprint.route("/login", methods=["POST"])
def login_route():
    data = request.get_json()
    return login(data)

@auth_routes_blueprint.route("/user_delete", methods=["DELETE"])
def user_delete():
    data = request.get_json()
    return delete(data)