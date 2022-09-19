from src_api.models import *
from src_ui.src_pages import *
from src_ui.src_drivers.book_store_api_interface import Api
from tests.fixture_data import *
import pytest
import logging
from playwright.sync_api import sync_playwright
from src_ui.src_drivers import *
from selenium import webdriver

LOGGER = logging.getLogger(__name__)
HEADERS = {'accept': 'application/json'}

URL = "http://localhost:7017/"


@pytest.fixture(scope='class')
def get_api_UnAutho():
    LOGGER.info("Start tests")
    yield Api(URL, HEADERS)
    LOGGER.info("Finish tests")


@pytest.fixture
def args_from_user(pytestconfig) -> list[str]:
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
            driver = selenium_driver_operator(url, browser, path_driver)
            yield driver
            driver.close_page()
        elif sys_use == "playwright":
            playwright = playwright_driver_operator(url, browser)
            driver = playwright[0]
            yield driver
            driver.close_page()
            PW = playwright[1]
            driver.close_page()
            PW.stop()
    else:
        driver = driver_remote(browser,url)
        yield driver
        driver.close_page()


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


def selenium_driver_operator(url, browser, path_driver):
    if browser == "Chrome":
        driver = webdriver.Chrome(path_driver)
    elif browser == "Firefox":
        driver = webdriver.Firefox(path_driver)
    driver.maximize_window()
    driver.get(url)
    return Selenium(driver)


def playwright_driver_operator(url, browser):
    PW = sync_playwright().start()
    if browser == "Chrome":
        driver = PW.chromium.launch(headless=False)
    elif browser == "Firefox":
        driver = PW.firefox.launch(headless=False)
    page = driver.new_page()
    page.goto(url)
    return PlayWright(page),PW


def driver_remote(browser,url):
    if browser == "Chrome":
        driver_options = webdriver.ChromeOptions()
    elif browser == "Firefox":
        driver_options = webdriver.FirefoxOptions()
    else:
        raise AssertionError("Currently Driver not supporting that kind of browser")
    browser_new = browser.lower()
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'javascriptEnabled': True,
                              "browserName":f"{browser_new}"},
        options= driver_options
    )
    driver.get(url)
    return Selenium(driver)





def make_login_account(user: ApiUserDto):
    login_user = LoginDto(user.email, user.password)
    return login_user



def make_register_account(info: dict):
    reguster_user = ApiUserDto(**info)
    return reguster_user

def make_dup_user_msg(email):
    dup_msg = '{"DuplicateUserName":' + f'["Username \'{email}\' is already taken."]'"}"
    return dup_msg



@pytest.fixture(scope="function")
def create_authors_dto() -> CreateAuthorDto:
    return CreateAuthorDto(**Create_Author_Dto_test)


@pytest.fixture(scope="function")
def get_create_book_dto() -> CreateBookDto:
    return CreateBookDto(**Create_Book_Dto_test)


def make_sesion_autho(api, user_login):
    res = api.account.post_login(data=user_login)
    my_token = res.token if not isinstance(res, dict) else ""
    HEADERS = {'Authorization': f'Bearer {my_token}'}
    api.update_session_header(HEADERS)
    return api


def make_sesion_Unautho(api):
    HEADERS = {'Authorization': ''}
    api.update_session_header(HEADERS)
    return api


def make_purches_msg(book_name):
    return f'Thank you for your purchase of {book_name}'


def delete_all_authors_and_books_created(api_from_test):
    api = api_from_test
    authors = api.authors.get_authors()
    for author in authors:
        if author.id > 3:
            api.authors.delete_authors_by_id(id=str(author.id))
    books = api.books.get_books()
    for book in books:
        if book.id > 6:
            api.books.delete_books_by_id(id=str(book.id))
            
            