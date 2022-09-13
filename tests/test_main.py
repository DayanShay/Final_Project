import time
import pytest
import logging
from selenium import webdriver
import json
from playwright.sync_api import sync_playwright
from src_ui.src_pages.login_page import LogIn
from src_ui.src_drivers.driver_selenium import Selenium
from src_ui.src_drivers.driver_playwright import PlayWright
from src_ui.src_drivers.driver_config import Driver
from selenium import webdriver

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def args_from_user(pytestconfig):
    url = pytestconfig.getoption("url")
    browser = pytestconfig.getoption("browse")
    path_driver = pytestconfig.getoption("path_driver")
    sys_use = pytestconfig.getoption("sys_use")
    return url,browser,path_driver,sys_use

@pytest.fixture
def make_driver(args_from_user) -> Driver:
    url, browser,path_driver,sys_use = args_from_user
    if sys_use == "selenium":
        if browser == "Chrome":
            driver = webdriver.Chrome(path_driver)
        elif browser == "firefox":
            driver = webdriver.Firefox(path_driver)
        driver.get(url)
        driver.maximize_window()
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

@pytest.fixture
def get_to_main_page(make_driver):
    login_page = LogIn(make_driver)
    return login_page


def test_open_page_and_click_log_in(get_to_main_page):
    page = get_to_main_page
    page.make_login(email="admin@sela.co.il",password="1234")
    time.sleep(5)

@pytest.fixture
def driver_remote():
    from selenium import webdriver

    firefox_options = webdriver.FirefoxOptions()
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        options= chrome_options
    )
    driver.get("http://www.google.com")
    time.sleep(10)
    driver.quit()