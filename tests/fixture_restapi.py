import pytest
import logging
from src_api.api.account_api import Account_Api
from src_api.api.authors_api import Authors_Api
from src_api.api.book_api import Books_Api
from src_api.models.api_user_dto import ApiUserDto
from src_api.models.auth_response_dto import AuthResponseDto
from src_api.models.book import Book
from src_api.models.create_author_dto import CreateAuthorDto
from src_api.models.create_book_dto import CreateBookDto
from src_api.models.login_dto import LoginDto
from src_api.models.update_author_dto import UpdateAuthorDto


LOGGER = logging.getLogger(__name__)
HEADERS = {'accept': 'application/json'}

URL = "http://localhost:7017/"

USER = {
    "email": "admin@sela.co.il",
    "password": "1234",
    "firstName": "string",
    "lastName": "string"
}

USER_Login = {
    "email": USER["email"],
    "password": USER["password"]
}

Create_Author_Dto_test = {
    "name": "Sela Inc",
    "homeLatitude": 32.09720633857184,
    "homeLongitude": 34.82631068248099
}
Update_Author_Dto_test = {
    "name": "Moshe",
    "homeLatitude": 0,
    "homeLongitude": 0,
    "id": 1
}
Create_Book_Dto_test = {
    "name": "string",
    "description": "string",
    "price": 0,
    "amountInStock": 3,
    "imageUrl": "string",
    "authorId": 1
}


@pytest.fixture(scope="session")
def get_account_api():
    return Account_Api(URL,HEADERS)

@pytest.fixture(scope="session")
def get_create_book_dto():
    return CreateBookDto(**Create_Book_Dto_test)

@pytest.fixture(scope="session")
def get_books_api(bearer_auth_session):
    return Books_Api(URL,bearer_auth_session)

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
    return CreateAuthorDto(**Create_Author_Dto_test)

@pytest.fixture(scope="session")
def update_authors_dto(make_api_user_dto):
    return UpdateAuthorDto(**Update_Author_Dto_test)




@pytest.fixture(scope="session")
def login_to_account_with_token(get_account_api, make_login_dto):
    User_Login = make_login_dto
    api = get_account_api
    res = api.login_account(data=User_Login)
    LOGGER.info(f"{res}")
    return res


@pytest.fixture(scope="session")
def bearer_auth_session(login_to_account_with_token):
    res = login_to_account_with_token
    my_token = res.token
    HEADERS = {'Authorization': f'Bearer {my_token}'}
    return HEADERS



@pytest.fixture(scope="session")
def get_authors_by_id(get_authors_api,id="1"):
    api = get_authors_api
    res = api.get_authors_by_id(data=id)
    LOGGER.info(f"{res}")
