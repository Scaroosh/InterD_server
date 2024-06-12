from flask import Blueprint, request, jsonify
from ..useCases.news import fetch_news

news_routes_blueprint = Blueprint("news_routes", __name__)

@news_routes_blueprint.route("/get_news", methods=["POST"])
def get_news_route():
    data = request.get_json()
    result, status_code = fetch_news(data)
    return jsonify(result), status_code
