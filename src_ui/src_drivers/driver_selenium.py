import time

from src_ui.src_drivers.driver_config import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from selenium.webdriver.common.action_chains import ActionChains as AC


class Selenium(Driver):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    def get_element(self, location: tuple[[], str], driver: [] = None, wait: int = 30):
        if driver is None:
            driver = self._driver
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(self.identy(location)))
        return element

    def get_elements(self, location: tuple[[], str], driver: [] = None, wait: int = 30):
        if driver is None:
            driver = self._driver
        elements = WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located(self.identy(location)))
        elements_temp = WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located(self.identy(location)))
        return elements_temp if len(elements) <= len(elements_temp) else elements

    def click_on_it(self, element):
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            element.click()

    def send_keys_to(self, location, text: str = ""):
        self._driver.find_element(*self.identy(location)).send_keys(text)

    def identy(self, location):
        actions = {"ID": By.ID,
                   "NAME": By.NAME,
                   "TAG_NAME": By.TAG_NAME,
                   "LINK_TEXT": By.LINK_TEXT,
                   "CLASS_NAME": By.CLASS_NAME,
                   "CSS_SELECTOR": By.CSS_SELECTOR,
                   "XPATH": By.XPATH
                   }
        return actions[location[0]], location[1]

    def alerts_hendler(self, buy_button, wait=30):
        self.click_on_it(buy_button)
        allert1 = WebDriverWait(self._driver, wait).until(EC.alert_is_present())
        if allert1:
            text_1 = allert1.text
            allert1.accept()
            try:
                allert2 = WebDriverWait(self._driver, wait).until(EC.alert_is_present())
            except (NoAlertPresentException, TimeoutException):
                return text_1
            if allert2:
                text_2 = allert2.text
                allert2.accept()
                return text_1, text_2

    def get_frame(self, google_frame,location, wait=30):
        driver = self._driver
        WebDriverWait(driver, wait).until(EC.frame_to_be_available_and_switch_to_it(google_frame))
        home_location_in_map = WebDriverWait(driver, wait).until(EC.presence_of_element_located(self.identy(location)))
        google_map_text = self.get_text(home_location_in_map)
        self._driver.switch_to.default_content()
        return google_map_text

    def switch_to_default(self):
        self._driver.switch_to.default_content()

    def page_url(self):
        return self._driver.current_url

    def get_book_img(self, location, driver=None):
        if driver is None:
            driver = self._driver
        book_img = self.get_element(location, driver)
        return book_img.get_attribute("src")

    def get_text(self, element):
        return element.text

    def refrash_page(self):
        self._driver.refresh()

    def close_page(self):
        self._driver.quit()

    def get_screen_shoot(self):
        pic = self._driver.get_screenshot_as_png()
        return pic
