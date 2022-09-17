from abc import ABC
import pytest
import logging
import requests
from src_api.api.base_api import BaseApi
from src_api.models import *
from src_api.api import *
from tests import fixture_data
# from tests.fixture_restapi import *


class Api():
    def __init__(self, url: str, headers):
        self._session = requests.session()
        self._account = Account_Api(url, headers,self._session)
        self._authors = Authors_Api(url, headers,self._session)
        self._books = Books_Api(url, headers,self._session)

    def update_session_header(self, headers):
        self._session.headers.update(headers)


    @property
    def session(self):
        return self._session

    @property
    def account(self):
        return self._account

    @property
    def authors(self):
        return self._authors

    @property
    def books(self):
        return self._books



    # @pytest.fixture(scope="session")
    # def get_account_api(self):
    #     return Account_Api(URL, HEADERS)
    #
    # @pytest.fixture(scope="session")
    # def get_books_api(self, make_auth_bearer):
    #     return Books_Api(URL, make_auth_bearer)
    #
    # @pytest.fixture(scope="session")
    # def get_authors_api(self, make_auth_bearer):
    #     return Authors_Api(URL, make_auth_bearer)
    #
    # @pytest.fixture(scope="session")
    # def make_auth_bearer(make_log_in_admin):
    #     res = make_log_in_admin
    #     my_token = res.token
    #     HEADERS = {'Authorization': f'Bearer {my_token}'}
    #     return HEADERS
    #
    # @pytest.fixture(scope="session")
    # def make_log_in_admin(get_account_api, make_login_dto):
    #     User_Login = make_login_dto
    #     api = get_account_api
    #     res = api.login_account(data=User_Login)
    #     LOGGER.info(f"{res}")
    #     return res
    #
    # @pytest.fixture(scope="session")
    # def make_log_in_admin(get_account_api, make_login_dto):
    #     User_Login = make_login_dto
    #     api = get_account_api
    #     res = api.login_account(data=User_Login)
    #     LOGGER.info(f"{res}")
    #     return res
    #
    # @pytest.fixture(scope="session")
    # def make_login_dto(make_api_user_dto: ApiUserDto):
    #     return LoginDto(make_api_user_dto.email, make_api_user_dto.password)
    #
    # @pytest.fixture(scope="session")
    # def make_api_user_dto(email, password):
    #     return ApiUserDto(email, password)
