import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from main import app
from database.orm_setup import get_session
from schemas.auth_schema import TokenData

@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="session")
def test_user():
    return {"email": "parentdemo@gmail.com", "password": 123456}

@pytest.fixture(scope="function")
def mock_db_session():
    mock_session = MagicMock()

    def override_get_db():
        try:
            yield mock_session
        finally:
            pass

    app.dependency_overrides[get_session] = override_get_db

    return mock_session

@pytest.fixture(scope="module")
def mock_smtp_instance():
    with patch('smtplib.SMTP') as mock_smtp_cls:
        yield mock_smtp_cls

@pytest.fixture(scope="module")
def mock_get_parent():
    with patch('services.create_new_parent.get_parent') as mock:
        yield mock

@pytest.fixture(scope="module")
def mock_get_parent_data():
    with patch('services.get_parent_data.get_parent') as mock:
        yield mock

@pytest.fixture(scope="module")
def mock_auth_get_parent():
    with patch('services.authenticate_parent.get_parent') as mock:
        yield mock

@pytest.fixture(scope="module")
def mock_verify_password():
    with patch('services.authenticate_parent.verify_password') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture(scope="module")
def mock_verify_token():
    with patch(f'utils.get_current_parent.verify_token') as mock:
        mock.return_value = TokenData(parent_id=10, email="parentdemo@gmail.com", is_active=True)
        yield mock
