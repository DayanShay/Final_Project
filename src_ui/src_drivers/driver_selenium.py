from src_ui.src_drivers.driver_config import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Selenium(Driver):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver

    def get_element(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(location))
        return element

    def get_elements(self, location,driver, wait: int = 5):
        elements = WebDriverWait(self._driver, wait).until(EC.presence_of_all_elements_located(location))
        return elements

    def click_on_it(self, location, wait: int = 5):
        self._driver.find_element(*self.identy(location)).click()

    def send_keys_to(self, location, text):
        self._driver.find_element(*self._With[location]).send_keys(text)

    def identy(self,location):
        if location[0] == "ID":
            return (By.ID, location[1])
        elif location[0] == "NAME":
            return (By.NAME, location[1])
        elif location[0] == "TAG_NAME":
            return (By.TAG_NAME, location[1])
        elif location[0] == "TEXT":
            return (By.LINK_TEXT, location[1])


