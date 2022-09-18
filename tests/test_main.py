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


@pytest.fixture
def args_from_user(pytestconfig):
    url = pytestconfig.getoption("url")
    browser = pytestconfig.getoption("browse")
    path_driver = pytestconfig.getoption("path_driver")
    sys_use = pytestconfig.getoption("sys_use")
    remote = pytestconfig.getoption("remote")
    return url, browser, path_driver, sys_use, remote


# @pytest.fixture
# def make_driver(args_from_user) -> Driver:
#     url, browser, path_driver, sys_use, remote = args_from_user
#     if not remote:
#         if sys_use == "selenium":
#             if browser == "Chrome":
#                 driver = webdriver.Chrome(path_driver)
#             elif browser == "Firefox":
#                 driver = webdriver.Firefox(path_driver)
#             driver.maximize_window()
#             driver.get(url)
#             yield Selenium(driver)
#             driver.quit()
#         elif sys_use == "playwright":
#             with sync_playwright() as p:
#                 if browser == "Chrome":
#                     driver = p.chromium.launch(headless=False)
#                 elif browser == "firefox":
#                     driver = p.firefox.launch(headless=False)
#                 page = driver.new_page()
#                 page.goto(url)
#                 yield PlayWright(page)
#                 driver.close()
#     else:
#         driver = driver_remote(browser)
#         driver.get(url)
#         yield Selenium(driver)
#         driver.quit()


@pytest.fixture
def get_to_main_page(make_driver):
    login_page = LoginPage(make_driver)
    return login_page


def test_open_page_and_click_log_in(get_to_main_page,get_authors_api):
    page = get_to_main_page
    store_page = page.make_login(email="admin@sela.co.il", password="string")

    # get search results of text = "" after 2 clicks give all in store.
    # search_page = store_page.search("")
    # books = search_page.get_book_container()
    # for book in books:
    #     book_author_name = search_page.get_book_author_name(book)
    #     book_name = search_page.get_book_name(book)
    #     book_details = search_page.get_book_details(book)
    #     book_price = search_page.get_book_price(book)
    #     ammount_in_stock = search_page.get_ammount_in_stock_of_book(book)
    #     print("\nauthor name:",book_author_name,
    #           "\nbook_name:",book_name,
    #           "\nbook_details:",book_details,
    #           "\nbook_price:",book_price,
    #           "\nammount_in_stock:",ammount_in_stock)
    # authors = search_page.get_author_container()
    # for author in authors:
    #     author_name = search_page.get_author_name(author)
    #     print(author_name)
    # time.sleep(3)

    # test all locations in maps
    authors_page = store_page.click_authors_button()
    authors_temp = authors_page.get_author_container()
    for i in range(len(authors_temp)):
        authors = authors_page.get_author_container()
        author_page = authors_page.click_go_to_author_page(authors[i])
        home_location = author_page.get_home_location()
        la, lo = author_page.convert_to_float_number(*home_location)
        api_autor = get_authors_api.get_authors_by_id(id=(i+1))
        LOGGER.info(f"{la},{lo}")
        assert la == round(api_autor.homeLatitude,4)
        assert lo == round(api_autor.homeLongitude,4)
        authors_page = author_page.click_authors_button()

    # click on all autors found in page(first time log in to autors page)
    # authors_page = store_page.click_authors_button()
    # authors_temp = authors_page.get_author_container()
    # for i in range(len(authors_temp)):
    #     authors = authors_page.get_author_container()
    #     author_name = authors_page.get_author_name(authors[i])
    #     print(author_name)
    #     authors_page.click_go_to_author_page(authors[i])
    #     time.sleep(3)
    #     authors_page = authors_page.click_authors_button()

    # click on purcuse for each book once
    # books = store_page.get_book_container()
    # for i,book in enumerate(books):
    #     ammount = store_page.get_ammount_in_stock_of_book(book)
    #     if int(ammount) > 0:
    #         store_page.click_buy(books[i])


def driver_remote(browser):
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
                              "browserName": f"{browser_new}"},
        options=driver_options
    )
    return driver
