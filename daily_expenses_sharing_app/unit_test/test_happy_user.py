from unit_test.test_main import client, test_user, mock_db_session, mock_smtp_instance, mock_get_user
from unit_test.test_main import mock_verify_password, mock_get_user_data, mock_auth_get_user, mock_verify_token
from unit_test.test_helper_functions import get_user

def test_create_user(client, mock_db_session, mock_get_user):
    mock_get_user.return_value = None
    payload = {"email": "userdemo@gmail.com", "password": "123456", "name": "Demo User", "mobile":"9874563210"}
    response = client.post("/api/v1/user/create-user", json=payload)
    actual_response = response.json()
    print("response:", actual_response)
    assert response.status_code == 200 
    assert actual_response["message"] == "user registered successfully. Please login with your email and password."

    added_instance = mock_db_session.add.call_args[0][0]
    assert added_instance.email == "userdemo@gmail.com"
    assert added_instance.name == "Demo User"


    mock_db_session.add.assert_called_once_with(added_instance)
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once_with(added_instance)
    mock_db_session.close.assert_called_once()

def test_login(client, mock_db_session, mock_auth_get_user, mock_verify_password):
    mock_auth_get_user.return_value = get_user()
    response = client.post("api/v1/user/login-user", json={"email": "userdemo@gmail.com", "password": "123456"})
    actual_response = response.json()
    print(actual_response)
    assert response.status_code == 200
    assert actual_response["name"] == "Demo User"
    assert actual_response["is_active"] == True
    assert actual_response["access_token"] != None
    assert actual_response["token_type"] == "bearer"


def test_get_user(client, mock_db_session, mock_get_user_data, mock_verify_token):
    mock_get_user_data.return_value = get_user()
    response = client.get("api/v1/user/get-user/me", headers={"Authorization": "Bearer mock_token"})
    actual_response = response.json()
    print(actual_response)
    assert response.status_code == 200
    assert actual_response["name"] == "Demo User"
    assert actual_response["email"] == "userdemo@gmail.com"
    assert actual_response["mobile"] == "7896541230"

