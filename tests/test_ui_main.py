import pytest
import logging
from src_api.api.account_api import Account_Api
from src_api.api.authors_api import Authors_Api
from src_api.api.base_api_functions import get_session
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


USER ={
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
  "name": "string",
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
    res = api.login_account(data=User_Login.to_json())
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

def test_post_account(get_account_api,make_api_user_dto):
    User = make_api_user_dto
    api = get_account_api
    LOGGER.info(f"{User}")
    res = api.post_account(data=User.to_json())
    LOGGER.info(f"{res}")

def test_login_account(login_to_account_with_token):
    res = login_to_account_with_token
    LOGGER.info(f"{res}")

def test_refresh_token(get_account_api, login_to_account_with_token):
    User_Login = login_to_account_with_token
    api = get_account_api
    res = api.refresh_token(data=User_Login.to_json())
    LOGGER.info(f"Moshe 2 {res} , Moshe 1 {User_Login}")

def test_get_authors(get_authors_api):
    api = get_authors_api
    res = api.get_authors()
    LOGGER.info(f"{res}")

def test_post_authors(get_authors_api,create_authors_dto):
    authors_dto = create_authors_dto
    api = get_authors_api
    for i in range(1,2):
        res = api.post_authors(data=authors_dto.to_json())
    LOGGER.info(f"{res}")

def test_get_authors_by_id(get_authors_api,id="202"):
    api = get_authors_api
    res = api.get_authors_by_id(id=id)
    LOGGER.info(f"{res}")

def test_put_authors_by_id(get_authors_api,update_authors_dto):
    authors_dto1 = update_authors_dto
    api = get_authors_api
    authors_dto1.name = "yossi"
    authors_dto2 = api.post_authors(data=authors_dto1.to_json())
    res = api.put_authors_by_id(data=authors_dto2.to_json(),id=authors_dto2.id)
    assert authors_dto1 != authors_dto2
    LOGGER.info(f"{res}")



def post_cap_authors(get_authors_api,create_authors_dto):
    authors_dto = create_authors_dto
    api = get_authors_api
    for i in range(1,6777):
        res = api.post_authors(data=authors_dto.to_json())
    # LOGGER.info(f"{res}")

def delete_all_authors_created(get_authors_api):
    api = get_authors_api
    a = api.get_authors()
    for i in a:
        if i.id > 3:
            t = api.delete_authors_by_id(id=str(i.id))
            # LOGGER.info(f"{t}")

# def test_add_and_delete_10000(get_authors_api,create_authors_dto):
#     post_cap_authors(get_authors_api,create_authors_dto)
#     delete_all_authors_created(get_authors_api)


def test_delete_authors_by_id(get_authors_api):
    api = get_authors_api
    a = api.get_authors()
    print(a)
    # t = api.delete_authors_by_id(id=str(4))
    delete_all_authors_created(get_authors_api)
    # LOGGER.info(f"{t}")

def test_search_authors_by_text(get_authors_api):
    api = get_authors_api
    author = api.get_authors_by_id(id=1)
    search_res = api.search_authors_by_text(text=author.name)
    print(author)
    assert [author.name == name for name in search_res]

def test_get_books(get_books_api):
    api = get_books_api
    books = api.get_books()
    print(books)

def test_post_books(get_books_api,get_authors_api,get_create_book_dto):
    books_api = get_books_api
    authors_api = get_authors_api
    book = get_create_book_dto
    res_get_authors = authors_api.get_authors()
    book.authorId = res_get_authors[0].id
    res_post_books = books_api.post_books(data=book.to_json())
    print(res_post_books)

def test_delete_books_by_id(get_books_api):
    books_api= get_books_api
    get_books_res = books_api.get_books()
    for books in get_books_res:
        if books.id > 6:
            delete_book_res = books_api.delete_books_by_id(id=books.id)

def test_get_books_by_author_id(get_books_api):
    api  = get_books_api
    get_books_by_author_id_res = api.get_books_by_author_id(authorid="1")
    print(get_books_by_author_id_res)

def test_put_purchese_by_books_id(get_books_api):
    api = get_books_api
    put_purchese_by_books_id_res = api.put_purchese_by_books_id(id="1")
    print(put_purchese_by_books_id_res)