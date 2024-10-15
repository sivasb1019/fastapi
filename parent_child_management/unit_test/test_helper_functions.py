from models.parents import Parent
from schemas.auth_schema import TokenData

def get_token(client, mock_db_session, mock_auth_get_parent, mock_verify_password):
    mock_auth_get_parent.return_value = get_parent()
    response = client.post("/api/v1/auth/login", json={"email": "parentdemo@gmail.com", "password": "123456"})
    return response.json()["access_token"]

def get_token_data():
    return TokenData(parent_id=10, email="parentdemo@gmail.com", is_active=True)

def get_parent():
    return Parent(id=10, firstname="Parent", middlename=None, lastname="Demo", email="parentdemo@gmail.com", 
                  profile_photo=None, age=27, dob=None, mobile=None, is_active=True,
                  address_line_1=None, address_line_2=None, city=None, state=None, country=None, pincode=None)


def get_parent_response():
    return {'id': 10, 'firstname': 'Parent', 'middlename': None, 'lastname': 'Demo', 'email': 'parentdemo@gmail.com', 
            'profile_photo': None, 'age': 27, 'dob': None, 'mobile': None, 'address_line_1': None, 'address_line_2': None, 
            'city': None, 'state': None, 'country': None, 'pincode': None}