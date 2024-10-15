from unit_test.test_main import client, mock_db_session, mock_smtp_instance, mock_get_parent_data, mock_auth_get_parent, mock_verify_password, mock_verify_token
from unit_test.test_helper_functions import get_parent, get_parent_response

def test_get_parent(client, mock_db_session, mock_get_parent_data, mock_verify_token):
    mock_get_parent_data.return_value = get_parent()
    response = client.get("/api/v1/parent/get-parent", headers={"Authorization": f"Bearer jwt_token"})
    actual_response = response.json()
    print("response:", actual_response)
    assert response.status_code == 200 
    assert actual_response == get_parent_response()
    