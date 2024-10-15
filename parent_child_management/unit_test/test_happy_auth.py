from unit_test.test_main import client, test_user, mock_db_session, mock_smtp_instance, mock_get_parent, mock_verify_password, mock_auth_get_parent
from unit_test.test_helper_functions import get_parent

def test_register_parent(client, mock_db_session, mock_get_parent):
    mock_get_parent.return_value = None
    response = client.post("/api/v1/auth/register", json={"email": "parentdemo@gmail.com", "password": "123456", "firstname": "Parent Demo"})
    actual_response = response.json()
    print("response:", actual_response)
    assert response.status_code == 200 
    assert actual_response["message"] == "Parent registered successfully. Please check your email for the activation link."

    added_instance = mock_db_session.add.call_args[0][0]
    assert added_instance.email == "parentdemo@gmail.com"
    assert added_instance.firstname == "Parent Demo"


    mock_db_session.add.assert_called_once_with(added_instance)
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once_with(added_instance)
    mock_db_session.close.assert_called_once()
    
def test_verify_account(client, mock_db_session, mock_get_parent):
    mock_get_parent.return_value = get_parent()
    response = client.get("/api/v1/auth/verify-account", params={"parent_id": 10})
    actual_response = response.json()
    print("response:", actual_response)
    assert response.status_code == 200 
    assert actual_response["message"] == "Account activated successfully."


    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()
    mock_db_session.close.assert_called_once()

def test_login(client, mock_db_session, mock_auth_get_parent, mock_verify_password):
    mock_auth_get_parent.return_value = get_parent()
    response = client.post("/api/v1/auth/login", json={"email": "parentdemo@gmail.com", "password": "123456"})
    actual_response = response.json()
    print(actual_response)
    assert response.status_code == 200
    assert actual_response["name"] == "Parent"
    assert actual_response["is_active"] == True
    assert actual_response["access_token"] != None
    assert actual_response["token_type"] == "bearer"