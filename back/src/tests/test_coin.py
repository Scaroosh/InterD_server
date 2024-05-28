from flask import Flask
from src.routes.auth import register, login, delete
from src.routes.coin import add_coin, delete_coin

app = Flask(__name__)

def test_add_delete_coin():
    fake_user = {"email": "test@test.com", "password": "test", "username": "test123"}
    add_data = {"id": "", "coins": {"BTC": 0.001} }
    delete_data = {"id": "", "coin": "BTC"}

    # Creating fake_user to test
    with app.app_context():
        response, status_code = register(fake_user)

    assert status_code == 201
    assert response.json["message"] == "Register successful!"
    
    with app.app_context():
        response, status_code = login(fake_user)

    assert status_code == 200
    assert response.json["message"] != None
    assert response.json["user_id"] != None
    user_id = {"user_id": response.json["user_id"]}

    # Adding coins
    add_data["id"] = response.json["user_id"]
    delete_data["id"] = response.json["user_id"]

    with app.app_context():
        response, status_code = add_coin(add_data)
    
    assert status_code == 200
    assert response.json["message"] == "Coins updated succesfully."

    # Deleting coin
    with app.app_context():
        response, status_code = delete_coin(delete_data)
    
    assert status_code == 200
    assert response.json["message"] == "Coin removed succesfully."


    # deleting fake_user
    with app.app_context():
        response, status_code = delete(user_id)

    assert status_code == 200
    assert response.json["message"] != None
