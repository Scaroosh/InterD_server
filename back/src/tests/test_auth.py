from flask import Flask
from src.routes.auth import register, login, delete

app = Flask(__name__)

def test_register_and_login_new_user():
    data = {"email": "test@example.com", "password": "test", "username": "test"}
    # testing register
    with app.app_context():
        response, status_code = register(data)

    assert status_code == 201
    assert response.json["message"] == "Register successful!"
    # testing login
    with app.app_context():
        response, status_code = login(data)

    assert status_code == 200
    assert response.json["message"] != None
    assert response.json["user_id"] != None
    user_id = {"user_id": response.json["user_id"]}
    # testing delete
    with app.app_context():
        response, status_code = delete(user_id)

    assert status_code == 200
    assert response.json["message"] != None
