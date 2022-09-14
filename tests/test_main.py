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
    return url,browser,path_driver,sys_use,remote

@pytest.fixture
def make_driver(args_from_user) -> Driver:
    url, browser,path_driver,sys_use,remote = args_from_user
    if not remote:
        if sys_use == "selenium":
            if browser == "Chrome":
                driver = webdriver.Chrome(path_driver)
            elif browser == "Firefox":
                driver = webdriver.Firefox(path_driver)
            driver.get(url)
            driver.set_window_size(800,800)
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


def test_open_page_and_click_log_in(get_to_main_page):
    page = get_to_main_page
    page.make_login(email="admin@sela.co.il", password="1234")
    store_page = page.click_store_page_button()
    books = store_page.get_card_group()
    for book in books:
        store_page.click_buy(book)


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
                              "browserName":f"{browser_new}"},
        options= driver_options
    )
    return driver
