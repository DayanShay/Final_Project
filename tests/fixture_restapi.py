from src_api.models.api_user_dto import ApiUserDto
from src_api.models.create_author_dto import CreateAuthorDto
from src_api.models.create_book_dto import CreateBookDto
from src_api.models.login_dto import LoginDto
from src_api.models.update_author_dto import UpdateAuthorDto
from src_ui.src_pages import *
from tests.store_book_api_class import Api
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


@pytest.fixture(scope='class')
def get_api_UnAutho():
    LOGGER.info("Start tests")
    yield Api(URL, HEADERS)
    LOGGER.info("Finish tests")


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
            driver = selenium_driver_operator(url, browser, path_driver)
        elif sys_use == "playwright":
            driver = playwright_driver_operator(url, browser)
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
    return PlayWright(page)


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

def test_open_page(get_to_main_page):
    page = get_to_main_page
    page.click_authors_button()
    time.sleep(2)