import pytest
import logging


from tests.fixture_restapi import *



def test_post_account(get_account_api,make_api_user_dto):
    User = make_api_user_dto
    api = get_account_api
    res = api.post_account(data=User)
    LOGGER.info(f"{res}")

def test_login_account(login_to_account_with_token):
    res = login_to_account_with_token
    LOGGER.info(f"{res}")

def test_refresh_token(get_account_api, login_to_account_with_token):
    User_Login = login_to_account_with_token
    api = get_account_api
    res = api.refresh_token(data=User_Login)
    LOGGER.info(f"Moshe 2 {res} , Moshe 1 {User_Login}")

def test_get_authors(get_authors_api):
    api = get_authors_api
    res = api.get_authors()
    LOGGER.info(f"{res}")

def test_post_authors(get_authors_api,create_authors_dto):
    authors_dto = create_authors_dto
    api = get_authors_api
    for i in range(1,200):
        res = api.post_authors(data=authors_dto)
    LOGGER.info(f"{res}")

def test_get_authors_by_id(get_authors_api,id="202"):
    api = get_authors_api
    res = api.get_authors_by_id(id=id)
    LOGGER.info(f"{res}")

def test_put_authors_by_id(get_authors_api,update_authors_dto):
    authors_dto1 = update_authors_dto
    api = get_authors_api
    authors_dto2 = api.post_authors(data=authors_dto1)
    assert authors_dto2.name == authors_dto1.name
    authors_dto2.name = "yossi"
    res = api.put_authors_by_id(data=authors_dto2,id=authors_dto2.id)
    res_get = api.get_authors_by_id(id=authors_dto2.id)
    assert res_get.name == authors_dto2.name
    LOGGER.info(f"{res_get}")



def post_cap_authors(get_authors_api,create_authors_dto):
    authors_dto = create_authors_dto
    api = get_authors_api
    for i in range(1,100):
        res = api.post_authors(data=authors_dto)
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
    for i in range(1,3):
        res_post_books = books_api.post_books(data=book)
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