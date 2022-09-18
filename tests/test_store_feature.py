import json
import time

import pytest
import logging
from src_api.models import *
from tests.fixture_data import *
from tests.fixture_restapi import *


class Test_store_page_features:

    def test_check_present_of_all_product_in_store_page(self,get_to_main_page,get_api_valid):
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

    def test_store2(self):
        pass
    def test_store3(self):
        pass
    def test_store4(self):
        pass
    def test_store5(self):
        pass
    def test_store6(self):
        pass
    def test_store7(self):
        pass
    def test_store8(self):
        pass






    @pytest.mark.parametrize("test_input,expected", [(USER_no_email_and_no_pass, Invalid_msg),
                                                     (USER_invalid_email_and_no_pass,
                                                      [Invalid_email_msg, Invalid_password_msg,
                                                       No_password_filled_msg]),
                                                     (USER_invalid_email_with_pass, [Invalid_email_msg]),
                                                     (USER_noemail_Generic_pass,
                                                      [Invalid_email_msg, No_email_filled_msg]),
                                                     (USER_noemail_invalid_low_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_noemail_invalid_high_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_withemail_invalid_low_password, [Invalid_password_msg]),
                                                     (USER_withemail_invalid_high_password, [Invalid_password_msg])
                                                     ])
    def test_register_on_Api_with_Invalid_data(self, get_api_valid, get_to_main_page, test_input: dict, expected):
        api = get_api_valid
        invalid_register_user = ApiUserDto(**test_input)
        res_register_invalid = api.account.post_account(data=invalid_register_user)
        assert res_register_invalid["code"] == 400
        for msg in expected:
            assert msg in res_register_invalid["msg"]
        invalid_login_user = self.make_login_dto(invalid_register_user)
        res_login_invalid = api.account.post_login(data=invalid_login_user)
        for msg in expected:
            assert msg in res_login_invalid["msg"]
        page = get_to_main_page
        page.click_log_in()
        store_page = page.make_login(invalid_login_user)
        assert store_page.get_page_url() == "http://localhost/"

    @pytest.mark.parametrize("test_input,expected", [(USER_no_email_and_no_pass, Invalid_msg),
                                                     (USER_invalid_email_and_no_pass,
                                                      [Invalid_email_msg, Invalid_password_msg,
                                                       No_password_filled_msg]),
                                                     (USER_invalid_email_with_pass, [Invalid_email_msg]),
                                                     (USER_noemail_Generic_pass,
                                                      [Invalid_email_msg, No_email_filled_msg]),
                                                     (USER_noemail_invalid_low_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_noemail_invalid_high_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_withemail_invalid_low_password, [Invalid_password_msg]),
                                                     (USER_withemail_invalid_high_password, [Invalid_password_msg])
                                                     ])
    def test_register_on_Website_with_Invalid_data(self, get_to_main_page, get_api_valid, expected, test_input: dict):
        page = get_to_main_page

        register_user = ApiUserDto(**test_input)
        login_user = self.make_login_dto(register_user)
        page.make_register(register_user)
        assert page.get_page_url() == "http://localhost/register"
        page.click_back_to_login()
        page.make_login(login_user)
        assert page.get_page_url() == "http://localhost/"
        api = get_api_valid
        invalid_login_user = self.make_login_dto(register_user)
        res_login_invalid = api.account.post_login(data=invalid_login_user)
        for msg in expected:
            assert msg in res_login_invalid["msg"]

    @pytest.mark.parametrize("test_input", [(USER_Admin)])
    def test_register_on_Website_with_Adminuser(self, get_to_main_page, get_api_valid, test_input: dict):
        page = get_to_main_page
        register_user = ApiUserDto(**test_input)
        login_user = self.make_login_dto(register_user)
        page.make_register(register_user)
        assert page.get_page_url() == "http://localhost/register"
        page.click_back_to_login()
        store_page = page.make_login(login_user)
        api = get_api_valid
        login_user = self.make_login_dto(register_user)
        res_login = api.account.post_login(data=login_user)
        assert store_page.get_page_url() == "http://localhost/store"
        assert res_login.token is not None

    @pytest.mark.parametrize("test_input", [(USER_testuser)])
    def test_register_on_Website_with_Testuser(self, get_to_main_page, get_api_valid, test_input: dict):
        page = get_to_main_page
        register_user = ApiUserDto(**test_input)
        login_user = self.make_login_dto(register_user)
        page.make_register(register_user)
        assert page.get_page_url() == "http://localhost/register"
        page.click_back_to_login()
        store_page = page.make_login(login_user)
        api = get_api_valid
        login_user = self.make_login_dto(register_user)
        res_login = api.account.post_login(data=login_user)
        assert store_page.get_page_url() == "http://localhost/store"
        assert res_login.token is not None

    @pytest.mark.parametrize("test_input", [(USER_Admin)])
    def test_register_on_API_with_valid_Adminuser(self, get_api_valid, get_to_main_page, test_input: dict):
        api = get_api_valid
        register_user = ApiUserDto(**test_input)
        res_register1 = api.account.post_account(data=register_user)
        assert res_register1 == 'OK'
        login_user = self.make_login_dto(register_user)
        res_login = api.account.post_login(data=login_user)
        assert res_login.token is not None
        page = get_to_main_page
        store_page = page.make_login(login_user)
        assert store_page.get_page_url() == "http://localhost/store"

    @pytest.mark.parametrize("test_input", [(USER_testuser)])
    def test_register_on_Website_with_valid_Testuser(self, get_api_valid, get_to_main_page, test_input: dict):
        api = get_api_valid
        register_user = ApiUserDto(**test_input)
        res_register1 = api.account.post_account(data=register_user)
        assert res_register1 == 'OK'
        login_user = self.make_login_dto(register_user)
        res_login = api.account.post_login(data=login_user)
        assert res_login.token is not None
        page = get_to_main_page
        store_page = page.make_login(login_user)
        assert store_page.get_page_url() == "http://localhost/store"

    @pytest.mark.parametrize("test_input", [(USER_testuser), (USER_Admin)])
    def test_register_Dup_accounts_on_API(self, get_api_valid, get_to_main_page, test_input: dict):
        api = get_api_valid
        register_user = ApiUserDto(**test_input)
        res_register1 = api.account.post_account(data=register_user)
        dup_msg = self.make_dup_user_msg(register_user.email)
        assert res_register1["msg"] == dup_msg
        login_user = self.make_login_dto(register_user)
        res_login = api.account.post_login(data=login_user)
        assert res_login.token is not None
        page = get_to_main_page
        store_page = page.make_login(login_user)
        assert store_page.get_page_url() == "http://localhost/store"

    def make_login_dto(self, userdto: ApiUserDto):
        user_for_test = LoginDto(userdto.email, userdto.password)
        return user_for_test

    def make_dup_user_msg(self, email):
        return '{"DuplicateUserName":' + f'["Username \'{email}\' is already taken."]'"}"
