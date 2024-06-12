from flask import Flask
from flask_cors import CORS
from db_utils import get_dbclient

app = Flask(__name__)
CORS(app)

def connect_to_database():
    try:
        get_dbclient().admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB Database!")
    except Exception as e:
        print(e)

def handle_routes(app):
    from src.routes.auth import auth_routes_blueprint
    from src.routes.coin import coin_routes_blueprint
    from src.routes.coinbase import coinbase_routes_blueprint
    from src.routes.bot import bot_routes_blueprint

    app.register_blueprint(auth_routes_blueprint, url_prefix='/auth')
    app.register_blueprint(coin_routes_blueprint, url_prefix='/coin')
    app.register_blueprint(coinbase_routes_blueprint, url_prefix='/coinbase')
    app.register_blueprint(bot_routes_blueprint, url_prefix='/bot')

connect_to_database()
handle_routes(app)