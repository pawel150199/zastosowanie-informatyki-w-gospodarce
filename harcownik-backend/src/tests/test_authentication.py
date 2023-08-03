from fastapi.testclient import TestClient

from src.main import app 
from test_params import PASSWORD, SCOUT

client = TestClient(app)

def test_scout_authentication_ok():
    response = client.post(
        "/login/access-token",
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data = {
            "username": SCOUT,
            "password": PASSWORD
        }
    )
    assert response.status_code == 200
    assert response.json()['access_token'], "Access token is empty"


def test_scout_authentication_not_ok_user():
    response = client.post(
        "/login/access-token",
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data = {
            "username": "random_letters",
            "password": PASSWORD
        }
    )
    assert response.status_code == 403
    assert response.json()['detail'] == "no user"


def test_scout_authentication_not_ok_password():
    response = client.post(
        "/login/access-token",
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data = {
            "username": SCOUT,
            "password": "random_letters"
        }
    )
    assert response.status_code == 403
    assert response.json()['detail'] == "password not correct"
