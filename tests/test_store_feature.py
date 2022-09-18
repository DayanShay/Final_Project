import json
import time

import pytest
import logging
from src_api.models import *
from tests.fixture_data import *
from tests.fixture_restapi import *


class Test_store_page_features:

    def test_check_contant_of_store_page(self,get_to_main_page,get_api_valid):
        page = get_to_main_page
        api = get_api_valid
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

    def test_check_contant_of_store_page_after_pust(self,get_to_main_page,get_api_valid):
        pass
    def test_check_contant_of_store_page_after_put(self,get_to_main_page,get_api_valid):
        pass
    def test_check_contant_of_store_page_after_delete(self,get_to_main_page,get_api_valid):
        pass

    def make_login_dto(self, userdto: ApiUserDto):
        user_for_test = LoginDto(userdto.email, userdto.password)
        return user_for_test

    def make_dup_user_msg(self, email):
        return '{"DuplicateUserName":' + f'["Username \'{email}\' is already taken."]'"}"
