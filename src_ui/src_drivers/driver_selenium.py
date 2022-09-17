from src_ui.src_drivers.driver_config import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from selenium.webdriver.common.action_chains import ActionChains as AC


class Selenium(Driver):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    def get_element(self, location: tuple[[], str], driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        flag = True
        i = 0
        element = None
        while flag and i < 3:
            try:
                element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(self.identy(location)))
                flag = False
            except TimeoutException:
                try:
                    element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(self.identy(location)))
                    flag = False
                except TimeoutException:
                    flag = True
            i += 1
        return element

    def get_elements(self, location: tuple[[], str], driver: [] = None, wait: int = 10):
        if driver is None:
            driver = self._driver
        flag = True
        i = 0
        elements = None
        while flag and i < 3:
            try:
                elements = WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located(self.identy(location)))
                flag = False
            except:
                try:
                    elements = WebDriverWait(driver, wait).until(
                        EC.presence_of_all_elements_located(self.identy(location)))
                    flag = False
                except:
                    flag = True
            i += 1
        return elements

    def click_on_it(self, location: tuple[[], str], driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        button = self.get_element(location, driver)
        flag = True
        i = 0
        while flag and i < 3:
            try:
                button.click()
                flag = False
            except TimeoutException:
                try:
                    button.click()
                    flag = False
                except ElementClickInterceptedException:
                    flag = True
            i += 1

    def send_keys_to(self, location: tuple[[], str], driver: [] = None, text: str = None):
        if driver is None:
            driver = self._driver
        driver.find_element(*self.identy(location)).send_keys(text)

    def identy(self, location):
        actions = {"ID": By.ID,
                   "NAME": By.NAME,
                   "TAG_NAME": By.TAG_NAME,
                   "LINK_TEXT": By.LINK_TEXT,
                   "CLASS_NAME": By.CLASS_NAME,
                   "CSS_SELECTOR": By.CSS_SELECTOR,
                   "XPATH": By.XPATH,
                   "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT
                   }
        return actions[location[0]], location[1]

    def alerts_hendler(self, wait=15):
        allert1 = WebDriverWait(self._driver, wait).until(EC.alert_is_present())
        if allert1:
            print(allert1.text)
            allert1.accept()
            try:
                allert2 = WebDriverWait(self._driver, wait).until(EC.alert_is_present())
                if allert2:
                    print(allert2.text)
                    allert2.accept()
            except:
                pass

    def get_frame(self, location):
        flag = True
        i = 0
        while flag and i < 3:
            try:
                WebDriverWait(self._driver, 10).until(EC.frame_to_be_available_and_switch_to_it(location))
                flag = False
            except TimeoutException:
                try:
                    WebDriverWait(self._driver, 10).until(EC.frame_to_be_available_and_switch_to_it(location))
                    flag = False
                except:
                    flag = True
            i += 1

    def switch_to_default(self):
        self._driver.switch_to.default_content()
