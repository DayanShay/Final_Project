from src_api.models.api_user_dto import ApiUserDto
from src_api.models.create_author_dto import CreateAuthorDto
from src_api.models.create_book_dto import CreateBookDto
from src_api.models.login_dto import LoginDto
from src_api.models.update_author_dto import UpdateAuthorDto
from src_ui.src_pages import *
from tests.fixture_api_and_ui import Api
from tests.fixture_data import *
import time
import pytest
import logging
import json
from playwright.sync_api import sync_playwright
from src_ui.src_drivers.driver_selenium import Selenium
from src_ui.src_drivers.driver_playwright import PlayWright
from src_ui.src_drivers.driver_config import Driver
from selenium import webdriver
from src_ui.src_pages.login_page import LoginPage


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





@pytest.fixture(scope='class')
def get_api_UnAutho():
    LOGGER.info("Start tests")
    yield Api(URL, HEADERS)
    LOGGER.info("Finish tests")

@pytest.fixture(scope='class')
def get_api_Autho(get_authirized):
    LOGGER.info("Start tests")
    yield Api(URL, get_authirized)
    LOGGER.info("Finish tests")

@pytest.fixture(scope="session")
def get_authirized(make_log_in_admin):
    res = make_log_in_admin
    my_token = res.token
    HEADERS = {'Authorization': f'Bearer {my_token}'}
    return HEADERS

@pytest.fixture(scope="session")
def make_log_in_admin(get_api_unautho, make_login_dto):
    User_Login = make_login_dto
    User_Login.email = Admin_email
    api = get_api_unautho.account
    res = api.post_login(data=User_Login)
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
@pytest.fixture
def args_from_user(pytestconfig):
    url = pytestconfig.getoption("url")
    browser = pytestconfig.getoption("browse")
    path_driver = pytestconfig.getoption("path_driver")
    sys_use = pytestconfig.getoption("sys_use")
    remote = pytestconfig.getoption("remote")
    return url, browser, path_driver, sys_use, remote


@pytest.fixture
def make_driver(args_from_user) -> Driver:
    url, browser, path_driver, sys_use, remote = args_from_user
    if not remote:
        if sys_use == "selenium":
            if browser == "Chrome":
                driver = webdriver.Chrome(path_driver)
            elif browser == "Firefox":
                driver = webdriver.Firefox(path_driver)
            driver.maximize_window()
            driver.get(url)
            yield Selenium(driver)
            driver.quit()
        elif sys_use == "playwright":
            with sync_playwright() as p:
                if browser == "Chrome":
                    driver = p.chromium.launch(headless=False)
                elif browser == "firefox":
                    driver = p.firefox.launch(headless=False)
                page = driver.new_page()
                page.goto(url)
                yield PlayWright(page)
                driver.close()
    else:
        driver = driver_remote(browser)
        driver.get(url)
        yield Selenium(driver)
        driver.quit()


@pytest.fixture
def get_to_main_page(make_driver):
    login_page = LoginPage(make_driver)
    return login_page

@pytest.fixture(scope="session")
def make_api_user_dto(email=None, password=None):
    user_for_test = ApiUserDto(**USER_no_email_and_no_pass)
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


@pytest.fixture(scope="session")
def get_user_dto_for_tests():
    return ApiUserDto(**USER_no_email_and_no_pass)

@pytest.fixture(scope="session")
def get_login_dto_for_tests():
    return LoginDto(**USER_Login)
#
#
# @pytest.fixture(scope="class")
# def make_log_in_admin(get_api_unautho, make_login_dto):
#     User_Login = make_login_dto
#     User_Login.email = Admin_email
#     api = get_api_unautho.Account
#     res = api.post_login(data=User_Login)
#     LOGGER.info(f"{res}")
#     return res
#
#
# @pytest.fixture(scope="class")
# def make_auth_bearer(make_log_in_admin, get_api_unautho):
#     api = get_api_unautho
#     res = make_log_in_admin
#     my_token = res.token
#     HEADERS = {'Authorization': f'Bearer {my_token}'}
#     api = Api(URL, HEADERS)
#     LOGGER.info(f"Authorization: Bearer {my_token}")
#     return api
#
#
# @pytest.fixture(scope="function")
# def get_create_book_dto():
#     return CreateBookDto(**Create_Book_Dto_test)
#
#
# @pytest.fixture(scope="function")
# def create_authors_dto():
#     return CreateAuthorDto(**Create_Author_Dto_test)
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
