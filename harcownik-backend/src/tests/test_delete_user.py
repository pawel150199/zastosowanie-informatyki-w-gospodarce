from fastapi.testclient import TestClient

from src.main import app
from test_params import PASSWORD, TEAMADMIN, WEBADMIN
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
        "username": TEAMADMIN,
        "password": PASSWORD
    }
)
TEAMADMIN_TOKEN = response.json()["access_token"]

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
    "Authorization": f"Bearer {TEAMADMIN_TOKEN}"
}

# Create users to delete which are in group 1
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
        "group": 1
    }   
)

USER1_ID = response.json()['id']

response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json = {
        "first_name": "scout_test2",
        "last_name": "scout_test2",
        "email": "scout_test2@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
        "group": 1
    }   
)

USER2_ID = response.json()['id']

response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json = {
        "first_name": "scout_test3",
        "last_name": "scout_test3",
        "email": "scout_test3@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
        "group": 1
    }   
)

USER3_ID = response.json()['id']


response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json = {
        "first_name": "scout_test4",
        "last_name": "scout_test4",
        "email": "scout_test4@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
        "group": 1
    }   
)

USER4_ID = response.json()['id']


# Create users to delete which are in group null
response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json = {
        "first_name": "scout_test5",
        "last_name": "scout_test5",
        "email": "scout_test5@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
    }   
)

USER5_ID = response.json()['id']


response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json = {
        "first_name": "scout_test6",
        "last_name": "scout_test6",
        "email": "scout_test6@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
    }   
)

USER6_ID = response.json()['id']


response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json= {
        "first_name": "scout_test7",
        "last_name": "scout_test7",
        "email": "scout_test7@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
    }   
)

USER7_ID = response.json()['id']


response = client.post(
    "/users/scout",
    headers = WEBADMIN_HEADERS,
    json = {
        "first_name": "scout_test8",
        "last_name": "scout_test8",
        "email": "scout_test8@harcownik.com",
        "level": "test",
        "function": "test",
        "password": PASSWORD,
    }   
)

USER8_ID = response.json()['id']


# WEBADMIN
def test_webdmin_delete_user_not_in_group():
    response = client.delete(
        f"/user/delete/{USER1_ID}",
        headers = WEBADMIN_HEADERS
    )
    assert response.status_code == 200


def test_webdmin_delete_user_in_group():
    response = client.delete(
        f"/user/group/delete/{USER5_ID}",
        headers = WEBADMIN_HEADERS,  
    )
    assert response.status_code == 200


# TEAMADMIN
def test_teamadmin_delete_user_not_in_group():
    response = client.delete(
        f"/user/delete/{USER2_ID}",
        headers = TEAMADMIN_HEADERS,   
    )

    delete_response = client.delete(
        f"/user/delete/{USER2_ID}",
        headers = WEBADMIN_HEADERS,   
    )

    assert response.status_code == 401
    assert delete_response.status_code == 200
    assert response.json()['detail'] == "The user doesn't have enough privileges"


def test_teamadmin_delete_user_in_group():
    response = client.delete(
        f"/user/group/delete/{USER6_ID}",
        headers = TEAMADMIN_HEADERS,   
    )
    assert response.status_code == 200


# SCOUT
def test_scout_delete_user_not_in_group():
    response = client.delete(
        f"/user/delete/{USER3_ID}",
        headers = SCOUT_HEADERS,  
    )

    delete_response = client.delete(
        f"/user/delete/{USER3_ID}",
        headers = WEBADMIN_HEADERS,  
    )

    assert response.status_code == 401
    assert delete_response.status_code == 200
    assert response.json()['detail'] == "The user doesn't have enough privileges"


def test_scout_delete_user_in_group():
    response = client.delete(
        f"/user/delete/group/{USER7_ID}",
        headers = SCOUT_HEADERS,   
    )

    delete_response = client.delete(
        f"/user/delete/group/{USER7_ID}",
        headers = WEBADMIN_HEADERS,   
    )

    assert response.status_code == 401
    assert delete_response.status_code == 200
    assert response.json()['detail'] == "The user doesn't have enough privileges"


# NOT LOGGED USER
def test_scout_delete_user_not_in_group():
    response = client.delete(
        f"/user/delete/{USER4_ID}",   
    )

    delete_response = client.delete(
        f"/user/delete/{USER4_ID}",
        headers = WEBADMIN_HEADERS,   
    )

    assert response.status_code == 401
    assert delete_response.status_code == 200
    assert response.json()['detail'] == "Not authenticated"


def test_scout_delete_user_in_group():
    response = client.delete(
        f"/user/group/delete/{USER8_ID}",  
    )

    delete_response = client.delete(
        f"/user/group/delete/{USER8_ID}",  
        headers = WEBADMIN_HEADERS, 
    )

    assert response.status_code == 401
    assert delete_response.status_code == 200
    assert response.json()['detail'] == "Not authenticated"
