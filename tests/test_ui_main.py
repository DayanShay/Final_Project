import pytest
import logging
from tests.fixture_data import *
from tests.fixture_restapi import *


def test_delete_book_by_id_and_website_check():

def test_delete_book_unauthorize(get_api,get_authirized):
    api = get_api

    res = api.authors.delete_authors_by_id(id=800)
    print(f"moshe1 {api.session.headers,api.session.auth}")
    print(res)

    headers = get_authirized
    api.update_session_header(headers)

    res = api.authors.delete_authors_by_id(id=800)
    print(f"moshe2 {api.session.headers,api.session.auth}")
    print(res)
    assert res


def test_post_account(get_api_valid,make_api_user_dto):
    User = make_api_user_dto
    User.email = Admin_email
    # User.password = ""
    api = get_api_valid.Account
    res = api.post_account(data=User)
    LOGGER.info(f"{res}")

def test_login_account(make_log_in_admin):
    res = make_log_in_admin
    LOGGER.info(f"{res}")

# def test_refresh_token(get_api_valid, make_log_in_admin):
#     User_Login = make_log_in_admin
#     res = get_api_valid.Account.refresh_token(data=User_Login)
#     LOGGER.info(f"Moshe 2 {res} , Moshe 1 {User_Login}")
#     assert res.userId == User_Login.userId
#     assert res.token != User_Login.token
#     assert res.refreshToken != User_Login.refreshToken

def test_get_authors(get_api_valid):
    api = get_api_valid.Authors
    res = api.get_authors()
    LOGGER.info(f"{res}")

def test_post_authors(get_api, create_authors_dto,):
    authors_dto = create_authors_dto
    api = get_api
    api.update_session_header()
    for i in range(1,2):
        res = api.Authors.post_authors(data=authors_dto)
    LOGGER.info(f"{res}")

def test_get_authors_by_id(get_api_valid,id="1"):
    api = get_api_valid.Authors
    res = api.get_authors_by_id(id=id)
    LOGGER.info(f"{res}")

def test_put_authors_by_id(get_api_valid,update_authors_dto):
    authors_dto1 = update_authors_dto
    api = get_api_valid.Authors
    authors_dto2 = api.post_authors(data=authors_dto1)
    assert authors_dto2.name == authors_dto1.name
    authors_dto2.name = "yossi"
    res = api.put_authors_by_id(data=authors_dto2,id=authors_dto2.id)
    res_get = api.get_authors_by_id(id=authors_dto2.id)
    assert res_get.name == authors_dto2.name
    LOGGER.info(f"{res_get}")

def post_cap_authors(get_api_valid,create_authors_dto):
    authors_dto = create_authors_dto
    api = get_api_valid.Authors
    for i in range(1,100):
        res = api.post_authors(data=authors_dto)
    # LOGGER.info(f"{res}")

def delete_all_authors_created(get_api_valid):
    api = get_api_valid.Authors
    a = api.get_authors()
    for i in a:
        if i.id > 3:
            t = api.delete_authors_by_id(id=str(i.id))
            # LOGGER.info(f"{t}")

# def test_add_and_delete_10000(get_authors_api,create_authors_dto):
#     post_cap_authors(get_authors_api,create_authors_dto)
#     delete_all_authors_created(get_authors_api)


def test_delete_authors_by_id(get_api_valid):
    api = get_api_valid.Authors
    a = api.get_authors()
    print(a)
    # t = api.delete_authors_by_id(id=str(4))
    delete_all_authors_created(api)
    # LOGGER.info(f"{t}")

def test_search_authors_by_text(get_api_valid):
    api = get_api_valid.Authors
    author = api.get_authors_by_id(id=1)
    search_res = api.search_authors_by_text(text=author.name)
    print(author)
    assert [author.name == name for name in search_res]

def test_get_books(get_api_valid):
    api = get_api_valid.Books
    books = api.get_books()
    print(books)

def test_post_books(get_api_valid,get_create_book_dto):
    api = get_api_valid
    books_api = api.Books
    authors_api = api.Authors
    book = get_create_book_dto
    res_get_authors = authors_api.get_authors()
    book.authorId = res_get_authors[0].id
    for i in range(1,3):
        res_post_books = books_api.post_books(data=book)
    print(res_post_books)

def test_delete_books_by_id(get_api_valid):
    books_api= get_api_valid.Books
    get_books_res = books_api.get_books()
    for books in get_books_res:
        if books.id > 6:
            delete_book_res = books_api.delete_books_by_id(id=books.id)
            print(delete_book_res)


def test_get_books_by_author_id(get_api_valid):
    api  = get_api_valid.Books
    get_books_by_author_id_res = api.get_books_by_author_id(authorid="1")
    print(get_books_by_author_id_res)

def test_put_purchese_by_books_id(get_api_valid):
    api = get_api_valid.Books
    put_purchese_by_books_id_res = api.put_purchese_by_books_id(id="1")
    print(put_purchese_by_books_id_res)