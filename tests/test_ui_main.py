import pytest
import logging
from src_api.api.account_api import Account_Api
from src_api.api.authors_api import Authors_Api
from src_api.api.base_api_functions import get_session
from src_api.models.api_user_dto import ApiUserDto
from src_api.models.auth_response_dto import AuthResponseDto
from src_api.models.create_author_dto import CreateAuthorDto
from src_api.models.login_dto import LoginDto

LOGGER = logging.getLogger(__name__)
HEADERS = {'accept': 'application/json'}

URL = "http://localhost:7017/"


USER ={
  "email": "user@example.com",
  "password": "string",
  "firstName": "string",
  "lastName": "string"
}

USER_Login = {
    "email": "user@example.com",
    "password": "string"
}

AuthorDto = {
  "name": "string",
  "homeLatitude": 0,
  "homeLongitude": 0
}

@pytest.fixture(scope="session")
def get_account_api():
    return Account_Api(URL,HEADERS)

@pytest.fixture(scope="session")
def get_authors_api(bearer_auth_session):
    return Authors_Api(URL,bearer_auth_session)


@pytest.fixture(scope="session")
def make_api_user_dto():
    return ApiUserDto(**USER)

@pytest.fixture(scope="session")
def make_login_dto(make_api_user_dto):
    return LoginDto(make_api_user_dto.email,make_api_user_dto.password)

@pytest.fixture(scope="session")
def create_authors_dto(make_api_user_dto):
    return CreateAuthorDto(**AuthorDto)

@pytest.fixture(scope="session")
def bearer_auth_session(login_account_token):
    res = login_account_token
    my_token = res.token
    HEADERS = {'Authorization': f'Bearer {my_token}'}
    return HEADERS


@pytest.fixture(scope="session")
def login_account_token(get_account_api,make_login_dto):
    User_Login = make_login_dto
    api = get_account_api
    res = api.login_account(data=User_Login.to_json())
    LOGGER.info(f"{res}")
    return res

def test_post_account(get_account_api,make_api_user_dto):
    User = make_api_user_dto
    api = get_account_api
    LOGGER.info(f"{USER}")
    res = api.post_account(data=User.to_json())
    LOGGER.info(f"{res}")

def test_login_account(login_account_token):
    res = login_account_token
    LOGGER.info(f"{res}")

def test_refresh_token(get_account_api,login_account_token):
    User_Login = login_account_token
    api = get_account_api
    res = api.refresh_token(data=User_Login.to_json())
    # LOGGER.info(f"Moshe 2 {res} , Moshe 1 {User_Login}")
    # assert res == User_Login

def test_get_authors(get_authors_api):
    api = get_authors_api
    res = api.get_authors()
    LOGGER.info(f"{res}")

def test_post_authors(get_authors_api,create_authors_dto):
    authors_dto = create_authors_dto
    api = get_authors_api
    res = api.post_authors(data=authors_dto.to_json())
    LOGGER.info(f"{res}")

def test_get_authors_by_id(get_authors_api,id="1"):
    api = get_authors_api
    res = api.get_authors_by_id(data=id)
    LOGGER.info(f"{res}")