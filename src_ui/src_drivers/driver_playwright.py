from src_ui.src_drivers.driver_config import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlayWright(Driver):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver


    def get_element(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        try:
            element = driver.locator(location)
        finally:
            return element

    def get_elements(self, location,driver, wait: int = 5):
        elements = self._driver.query_selector_all(location)
        return elements

    def click_on_it(self, location, wait: int = 5):
        self._driver.locator(self.identy(location)).click()

    def send_keys_to(self, location, text):
        self._driver.find_element(*self._With[location]).send_keys(text)

    def identy(self,location):
        if location[0] == "ID":
            return f"id={location[1]}"
        elif location[0] == "NAME":
            return f"[name={location[1]}]"
        elif location[0] == "TAG_NAME":
            return f"@={location[1]}"
        elif location[0] == "TEXT":
            return f'text="{location[1]}"'


