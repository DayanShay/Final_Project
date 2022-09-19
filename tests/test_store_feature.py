import json
import time

import pytest
import logging
from src_api.models import *
from tests.fixture_data import *
from tests.fixture_restapi import *


class Test_store_page_features:

    def test_check_contant_of_store_page(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        api = get_api_UnAutho
        store_page = page.click_store_page_button()
        books_from_store = store_page.get_book_container()
        books_from_api = api.books.get_books()
        assert len(books_from_store) == len(books_from_api)
        for i in range(len(books_from_store)):
            book_name = store_page.get_book_name(books_from_store[i])
            assert book_name == books_from_api[i].name
            author_name = store_page.get_book_author_name(books_from_store[i])
            author = api.authors.get_authors_by_id(id=books_from_api[i].authorId)
            assert author_name == author.name
            book_price = store_page.get_book_price(books_from_store[i])
            assert book_price == str(books_from_api[i].price)
            book_details = store_page.get_book_details(books_from_store[i])
            assert book_details == books_from_api[i].description
            ammount_in_stock = store_page.get_ammount_in_stock_of_book(books_from_store[i])
            assert ammount_in_stock == str(books_from_api[i].amountInStock)
            photo_url = store_page.get_book_img(books_from_store[i])
            assert photo_url == books_from_api[i].imageUrl

    def test_check_contant_of_store_page_after_post(self, get_to_main_page, get_api_UnAutho,
                                                    create_authors_dto, get_create_book_dto):
        page = get_to_main_page
        user_login = self.make_login_dto(USER_Admin)
        api = self.make_sesion_autho(get_api_UnAutho, user_login)
        author = create_authors_dto
        book = get_create_book_dto
        res_post_author = api.authors.post_authors(data=author)
        book.authorId = res_post_author.id
        res_post_book = api.books.post_books(data=book, id=book.authorId)
        books_from_api = api.books.get_books()
        store_page = page.click_store_page_button()
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        last_book_from_web = books_from_store[-1]
        author_name_web = store_page.get_book_author_name(last_book_from_web)
        author_name_api = api.authors.get_authors_by_id(id=res_post_book.authorId)
        assert books_from_api[-1].name == res_post_book.name
        assert store_page.get_book_name(last_book_from_web) == res_post_book.name
        assert author_name_web == author_name_api.name
        assert store_page.get_book_price(last_book_from_web) == str(res_post_book.price)
        assert store_page.get_book_details(last_book_from_web) == res_post_book.description
        assert store_page.get_ammount_in_stock_of_book(last_book_from_web) == str(res_post_book.amountInStock)
        assert store_page.get_book_img(last_book_from_web) == res_post_book.imageUrl

    def test_check_contant_of_store_page_after_put(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        user_login = self.make_login_dto(USER_Admin)
        api = self.make_sesion_autho(get_api_UnAutho, user_login)
        res_get_books = api.books.get_books()
        book = res_get_books[-1]
        book.name = "Sela QA & Automation testing 101"
        res_put_book = api.books.put_books_by_id(data=book, id=book.id)
        books_from_api = api.books.get_books()
        store_page = page.click_store_page_button()
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        last_book_from_web = books_from_store[-1]
        author_name_web = store_page.get_book_author_name(last_book_from_web)
        author_name_api = api.authors.get_authors_by_id(id=book.authorId)
        assert res_put_book == 'No Content'
        assert book != res_put_book
        assert books_from_api[-1].name == book.name
        assert store_page.get_book_name(last_book_from_web) == book.name
        assert author_name_web == author_name_api.name
        assert store_page.get_book_price(last_book_from_web) == str(book.price)
        assert store_page.get_book_details(last_book_from_web) == book.description
        assert store_page.get_ammount_in_stock_of_book(last_book_from_web) == str(book.amountInStock)
        assert store_page.get_book_img(last_book_from_web) == book.imageUrl

    def test_check_contant_of_store_page_after_delete(self, get_to_main_page, get_api_UnAutho):
        page = get_to_main_page
        user_login = self.make_login_dto(USER_Admin)
        api = self.make_sesion_autho(get_api_UnAutho, user_login)
        res_get_books = api.books.get_books()
        book = res_get_books[-1]
        store_page = page.click_store_page_button()
        store_page.page_refrash()
        post_book_web = store_page.get_book_container()[-1]
        res_delete_book = api.books.delete_books_by_id(id=book.id)
        books_from_api = api.books.get_books()
        assert res_delete_book == 'No Content'
        assert book not in books_from_api
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        assert post_book_web not in books_from_store

    def test_purcuhes_with_no_log_in(self, get_to_main_page, get_api_UnAutho, create_authors_dto, get_create_book_dto):
        page = get_to_main_page
        api = self.make_sesion_Unautho(get_api_UnAutho)
        store_page = page.click_store_page_button()
        books_from_store = store_page.get_book_container()
        books_from_api_before = api.books.get_books()
        book_from_api_before = books_from_api_before[-1]
        book_from_web_before = books_from_store[-1]
        ammount_in_stock_before = store_page.get_ammount_in_stock_of_book(book_from_web_before)
        msg_purchse = store_page.click_buy(book_from_web_before)
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        book_from_web_after = books_from_store[-1]
        ammount_in_stock_after = store_page.get_ammount_in_stock_of_book(book_from_web_after)
        res_put = api.books.put_purchese_by_books_id(id=book_from_api_before.id)
        books_from_api_after = api.books.get_books()
        book_from_api_after = books_from_api_after[-1]
        assert int(ammount_in_stock_after) == int(ammount_in_stock_before) == book_from_api_before.amountInStock
        assert res_put == Unauthorized_msg or perchuse_error_api
        assert book_from_api_before == book_from_api_after
        assert must_be_signed in msg_purchse

    def test_purcuhes_valid(self, get_to_main_page, get_api_UnAutho, create_authors_dto,
                            get_create_book_dto):
        page = get_to_main_page
        Auser_login = self.make_login_dto(USER_Admin)
        api = self.make_sesion_autho(get_api_UnAutho, Auser_login)
        store_page = page.make_login(Auser_login)
        books_from_store = store_page.get_book_container()
        books_from_api_before = api.books.get_books()
        book_from_api_before = books_from_api_before[-1]
        book_from_web_before = books_from_store[-1]
        ammount_in_stock_before_web = store_page.get_ammount_in_stock_of_book(book_from_web_before)
        msg_purchse = store_page.click_buy(book_from_web_before)
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        book_from_web_after = books_from_store[-1]
        books_from_api_after = api.books.get_books()
        book_from_api_after = books_from_api_after[-1]
        ammount_in_stock_after_web = store_page.get_ammount_in_stock_of_book(book_from_web_after)
        book_name = store_page.get_book_name(book_from_web_after)
        res_put = api.books.put_purchese_by_books_id(id=book_from_api_after.id)
        assert res_put.name == book_name
        assert int(ammount_in_stock_after_web) == int(ammount_in_stock_before_web)-1
        assert book_from_api_before.amountInStock-1 == book_from_api_after.amountInStock
        assert self.make_purches_msg(book_name) in msg_purchse


    def test_purcuhes_no_ammount_in_stock(self, get_to_main_page, get_api_UnAutho, create_authors_dto, get_create_book_dto):
        user_login = self.make_login_dto(USER_Admin)
        page = get_to_main_page
        store_page = page.make_login(user_login)
        api = self.make_sesion_autho(get_api_UnAutho, user_login)
        author = create_authors_dto
        book = get_create_book_dto
        res_post_author = api.authors.post_authors(data=author)
        book.authorId = res_post_author.id
        book.amountInStock = 0
        res_post_book = api.books.post_books(data=book, id=book.authorId)
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        books_from_api_before = api.books.get_books()
        book_from_api_before = books_from_api_before[-1]
        book_from_web_before = books_from_store[-1]
        ammount_in_stock_before = store_page.get_ammount_in_stock_of_book(book_from_web_before)
        msg_purchse = store_page.click_buy(book_from_web_before)
        store_page.page_refrash()
        books_from_store = store_page.get_book_container()
        book_from_web_after = books_from_store[-1]
        ammount_in_stock_after = store_page.get_ammount_in_stock_of_book(book_from_web_after)
        res_put = api.books.put_purchese_by_books_id(id=book_from_api_before.id)
        books_from_api_after = api.books.get_books()
        book_from_api_after = books_from_api_after[-1]
        assert int(ammount_in_stock_after) == int(ammount_in_stock_before)
        assert book_from_api_before == book_from_api_after
        assert msg_purchse != self.make_purches_msg(book.name)
        self.delete_all_authors_and_books_created(api)




    @staticmethod
    def make_sesion_autho(api, user_login):
        res = api.account.post_login(data=user_login)
        my_token = res.token
        HEADERS = {'Authorization': f'Bearer {my_token}'}
        api.update_session_header(HEADERS)
        return api

    @staticmethod
    def make_sesion_Unautho(api):
        HEADERS = {'Authorization': ''}
        api.update_session_header(HEADERS)
        return api


    def make_login_dto(self, userdto: ApiUserDto):
        user_for_test = LoginDto(userdto["email"], userdto["password"])
        return user_for_test


    def make_purches_msg(self, book_name):
        return f'Thank you for your purchase of {book_name}'

    @pytest.fixture(scope="function")
    def get_create_book_dto(self) -> CreateBookDto:
        return CreateBookDto(**Create_Book_Dto_test)

    @pytest.fixture(scope="function")
    def create_authors_dto(self) -> CreateAuthorDto:
        return CreateAuthorDto(**Create_Author_Dto_test)

    @staticmethod
    def delete_all_authors_and_books_created(api_from_test):
        api = api_from_test
        authors = api.authors.get_authors()
        for author in authors:
            if author.id > 3:
                t = api.authors.delete_authors_by_id(id=str(author.id))
        books = api.books.get_books()
        for book in books:
            if book.id > 6:
                t = api.books.delete_books_by_id(id=str(book.id))
