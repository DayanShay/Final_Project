from src_ui.src_drivers import *
from playwright.sync_api import sync_playwright
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver





def selenium_driver_operator(url, browser):
    if browser == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "Firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
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
    page.set_default_timeout(30000)  # 30's Max to find element in page.
    page.goto(url)
    return PlayWright(page), PW


def driver_remote(browser, url, remote_url):
    if browser == "Chrome":
        driver_options = webdriver.ChromeOptions()
    elif browser == "Firefox":
        driver_options = webdriver.FirefoxOptions()
    else:
        raise AssertionError("Currently Driver not supporting that kind of browser")
    browser_new = browser.lower()
    driver = webdriver.Remote(
        command_executor=f'{remote_url}',
        desired_capabilities={'javascriptEnabled': True,
                              "browserName": f"{browser_new}"},
        options=driver_options
    )
    driver.get(url)
    return Selenium(driver)