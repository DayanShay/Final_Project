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
        self._driver.find_element(*self.identy(location)).send_keys(text)

    def identy(self,location):
        actions = {"ID":By.ID,
                   "NAME":By.NAME,
                   "TAG_NAME":By.TAG_NAME,
                   "PARTIAL_LINK_TEXT":By.PARTIAL_LINK_TEXT,
                   "CLASS_NAME":By.CLASS_NAME,
                   "CSS_SELECTOR":By.CSS_SELECTOR,
                   "XPATH":By.XPATH,
                   }
        return actions[location[0]],location[1]


