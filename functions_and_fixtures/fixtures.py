import pytest
import logging
from src_api.models import *
from src_ui.src_drivers import *
from src_ui.src_pages import *
from functions_and_fixtures.screenshot_if_faild import *
from functions_and_fixtures.fixture_data import *

LOGGER = logging.getLogger(__name__)



@pytest.fixture(scope='class')
def get_api_UnAutho(pytestconfig):
    api_url = pytestconfig.getoption("api_url")
    LOGGER.info("Start tests2")
    yield Api(api_url, HEADERS)
    LOGGER.info("Finish tests2")


@pytest.fixture
def args_from_user(pytestconfig) -> list[str]:
    url = pytestconfig.getoption("url")
    browser = pytestconfig.getoption("browse")
    sys_use = pytestconfig.getoption("sys_use")
    remote = pytestconfig.getoption("remote")
    remote_url = pytestconfig.getoption("remote_url")
    return url, browser, sys_use, remote, remote_url


@pytest.fixture
def get_base_url(pytestconfig):
    url = pytestconfig.getoption("url")
    return url


@pytest.fixture
def make_driver(args_from_user, request) -> Driver:
    url, browser, sys_use, remote, remote_url = args_from_user
    if not remote:
        if sys_use == "selenium":
            driver = selenium_driver_operator(url, browser)
            yield driver
            screenshot_if_faild(driver, request)
            driver.close_page()
        elif sys_use == "playwright":
            playwright = playwright_driver_operator(url, browser)
            driver = playwright[0]
            yield driver
            screenshot_if_faild(driver, request)
            driver.close_page()
            PW = playwright[1]
            PW.stop()
    else:
        if sys_use != "playwright":
            driver = driver_remote(browser, url, remote_url)
            yield driver
            driver.close_page()
        else:
            raise AttributeError("Selenium Grid not supporting PlayWright")

@pytest.fixture
def get_to_main_page(make_driver):
    login_page = LoginPage(make_driver)
    return login_page


@pytest.fixture(scope="function")
def create_authors_dto() -> CreateAuthorDto:
    return CreateAuthorDto(**Create_Author_Dto_test)

@pytest.fixture(scope="function")
def get_create_book_dto() -> CreateBookDto:
    return CreateBookDto(**Create_Book_Dto_test)

