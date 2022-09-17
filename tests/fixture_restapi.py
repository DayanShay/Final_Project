import pytest
import logging
from src_api.models.api_user_dto import ApiUserDto
from src_api.models.create_author_dto import CreateAuthorDto
from src_api.models.create_book_dto import CreateBookDto
from src_api.models.login_dto import LoginDto
from src_api.models.update_author_dto import UpdateAuthorDto
from tests.fixture_api_and_ui import Api
from tests.fixture_data import *

accountinterface = "1"

LOGGER = logging.getLogger(__name__)
HEADERS = {'accept': 'application/json'}

URL = "http://localhost:7017/"


# USER = {
#     "email": "",
#     "password": "",
#     "firstName": "string",
#     "lastName": "string"
# }
#
# USER_Login = {
#     "email": USER["email"],
#     "password": USER["password"]
# }
#
# Create_Author_Dto_test = {
#     "name": "Sela Inc",
#     "homeLatitude": 32.09720633857184,
#     "homeLongitude": 34.82631068248099
# }
# Update_Author_Dto_test = {
#     "name": "Moshe",
#     "homeLatitude": 0,
#     "homeLongitude": 0,
#     "id": 1
# }
# Create_Book_Dto_test = {
#     "name": "string",
#     "description": "string",
#     "price": 0,
#     "amountInStock": 2,
#     "imageUrl": "string",
#     "authorId": 1
# }


# @pytest.fixture(scope="session")
# def get_api():
#     LOGGER.info("Start tests")
#     yield Api(URL, HEADERS)
#     LOGGER.info("Finish tests")


@pytest.fixture(scope='session')
def get_api_valid():
    LOGGER.info("Start tests")
    yield Api(URL, HEADERS)
    LOGGER.info("Finish tests")

@pytest.fixture(scope="session")
def get_authirized(make_log_in_admin):
    res = make_log_in_admin
    my_token = res.token
    HEADERS = {'Authorization': f'Bearer {my_token}'}
    return HEADERS

@pytest.fixture(scope="session")
def make_log_in_admin(get_api_valid, make_login_dto):
    User_Login = make_login_dto
    User_Login.email = Admin_email
    api = get_api_valid.account
    res = api.login_account(data=User_Login)
    LOGGER.info(f"{res}")
    return res




# @pytest.fixture(scope="session")
# def get_account_api():
#     return Account_Api(URL, HEADERS)
#
#
# @pytest.fixture(scope="session")
# def get_books_api(make_auth_bearer):
#     return Books_Api(URL, make_auth_bearer)
#
#
# @pytest.fixture(scope="session")
# def get_authors_api(make_auth_bearer):
#     return Authors_Api(URL, make_auth_bearer)


@pytest.fixture(scope="session")
def make_api_user_dto(email=None, password=None):
    user_for_test = ApiUserDto(**USER)
    if email:
        user_for_test.email = email
    if password:
        user_for_test.password = password
    LOGGER.info("Moshe")
    return user_for_test
#
#
@pytest.fixture(scope="session")
def make_login_dto(make_api_user_dto):
    return LoginDto(make_api_user_dto.email, make_api_user_dto.password)
#
#
# @pytest.fixture(scope="class")
# def make_log_in_admin(get_api_valid, make_login_dto):
#     User_Login = make_login_dto
#     User_Login.email = Admin_email
#     api = get_api_valid.Account
#     res = api.login_account(data=User_Login)
#     LOGGER.info(f"{res}")
#     return res
#
#
# @pytest.fixture(scope="class")
# def make_auth_bearer(make_log_in_admin, get_api_valid):
#     api = get_api_valid
#     res = make_log_in_admin
#     my_token = res.token
#     HEADERS = {'Authorization': f'Bearer {my_token}'}
#     api = Api(URL, HEADERS)
#     LOGGER.info(f"Authorization: Bearer {my_token}")
#     return api
#
#
@pytest.fixture(scope="module")
def get_create_book_dto():
    return CreateBookDto(**Create_Book_Dto_test)
#
#
@pytest.fixture(scope="module")
def create_authors_dto(make_api_user_dto):
    return CreateAuthorDto(**Create_Author_Dto_test)
#
#
@pytest.fixture(scope="module")
def update_authors_dto(make_api_user_dto):
    return UpdateAuthorDto(**Update_Author_Dto_test)
#
#
# @pytest.fixture(scope="module")
# def update_authors_dto(make_api_user_dto):
#     return UpdateAuthorDto(**Update_Author_Dto_test)

# @pytest.fixture(scope="session")
# def get_authors_by_id(get_authors_api, id="1"):
#     api = get_authors_api
#     res = api.get_authors_by_id(id=id)
#     LOGGER.info(f"{res}")
#     return res
