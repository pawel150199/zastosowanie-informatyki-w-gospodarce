from fastapi.testclient import TestClient

from src.main import app
from test_params import PASSWORD, TEAMADMIN, WEBADMIN, SCOUT
client = TestClient(app)



response = client.post(
    "/login/access-token",
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data = {
        "username": WEBADMIN,
        "password": PASSWORD
    }
)
WEBADMIN_TOKEN = response.json()["access_token"]

response = client.post(
    "/login/access-token",
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data = {
        "username": TEAMADMIN,
        "password": PASSWORD
    }
)
TEAMADMIN_TOKEN = response.json()["access_token"]

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
SCOUT_TOKEN = response.json()["access_token"]

WEBADMIN_HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {WEBADMIN_TOKEN}"
}

TEAMADMIN_HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TEAMADMIN_TOKEN}"
}

SCOUT_HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SCOUT_TOKEN}"
}


# WEBADMIN
def test_webdmin_add_scout():
    response = client.post(
        "/users/scout",
        headers = WEBADMIN_HEADERS,
        json = {
            "first_name": "scout_test1",
            "last_name": "scout_test1",
            "email": "scout_test1@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
        }   
    )

    delete_response = client.delete(
        f"/user/delete/{response.json()['id']}",
        headers = WEBADMIN_HEADERS
    )

    assert response.status_code == 200
    assert delete_response.status_code == 200


def test_webdmin_add_webadmin():
    response = client.post(
        "/users/admin",
        headers = WEBADMIN_HEADERS,
        json = {
            "first_name": "scout_test2",
            "last_name": "scout_test2",
            "email": "scout_test2@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
            "is_webadmin": True,
        }   
    )
    
    delete_response = client.delete(
        f"/user/delete/{response.json()['id']}",
        headers = WEBADMIN_HEADERS
    )

    assert response.status_code == 200
    assert delete_response.status_code == 200


# TEAMADMIN
def test_teamadmin_add_scout():
    response = client.post(
        "/users/scout",
        headers = TEAMADMIN_HEADERS,
        json = {
            "first_name": "scout_test3",
            "last_name": "scout_test3",
            "email": "scout_test3@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
        }   
    )
    
    delete_response = client.delete(
        f"/user/delete/{response.json()['id']}",
        headers = WEBADMIN_HEADERS
    )

    assert response.status_code == 200
    assert delete_response.status_code == 200


def test_teamadmin_add_webadmin():
    response = client.post(
        "/users/admin",
        headers = TEAMADMIN_HEADERS,
        json = {
            "first_name": "scout_test4",
            "last_name": "scout_test4",
            "email": "scout_test4@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
            "is_webadmin": True,
        }   
    )

    assert response.status_code == 401


# SCOUT
def test_scout_add_scout():
    response = client.post(
        "/users/scout",
        headers = SCOUT_HEADERS,
        json = {
            "first_name": "scout_test5",
            "last_name": "scout_test5",
            "email": "scout_test5@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
            "is_webadmin": False,
        }   
    )
    print(response.json())
    assert response.status_code == 401
    assert response.json()['detail'] == "The user doesn't have enough privileges"


def test_scout_add_webadmin():
    response = client.post(
        "/users/admin",
        headers = SCOUT_HEADERS,
        json = {
            "first_name": "scout_test6",
            "last_name": "scout_test6",
            "email": "scout_test6@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
            "is_webadmin": True,
        }   
    )
    assert response.status_code == 401
    assert response.json()['detail'] == "The user doesn't have enough privileges"


# NOT LOGGED USER
def test_notlogged_add_scout():
    response = client.post(
        "/users/scout",
        json = {
            "first_name": "scout_test7",
            "last_name": "scout_test7",
            "email": "scout_test7@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
        }   
    )
    assert response.status_code == 401
    assert response.json()['detail'] == "Not authenticated"


def test_notlogged_add_webadmin():
    response = client.post(
        "/users/admin",
        json = {
            "first_name": "scout_test7",
            "last_name": "scout_test7",
            "email": "scout_test7@harcownik.com",
            "level": "test",
            "function": "test",
            "password": PASSWORD,
            "is_webadmin": True
        }   
    )
    assert response.status_code == 401
    assert response.json()['detail'] == "Not authenticated"
