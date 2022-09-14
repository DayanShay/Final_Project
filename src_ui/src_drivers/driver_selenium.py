from src_ui.src_drivers.driver_config import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Selenium(Driver):
    def __init__(self, driver:Driver):
        super().__init__(driver)

    def get_element(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(self.identy(location)))
        return element

    def get_elements(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        elements = WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located(self.identy(location)))
        return elements

    def click_on_it(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        button = WebDriverWait(driver, wait).until(EC.element_to_be_clickable(self.identy(location)))
        self._driver.switch_to
        button.click()


    def send_keys_to(self, location: tuple[[], str], text:str):
        self._driver.find_element(*self.identy(location)).send_keys(text)

    def identy(self,location):
        actions = {"ID":By.ID,
                   "NAME":By.NAME,
                   "TAG_NAME":By.TAG_NAME,
                   "LINK_TEXT": By.LINK_TEXT,
                   "CLASS_NAME":By.CLASS_NAME,
                   "CSS_SELECTOR":By.CSS_SELECTOR,
                   "XPATH":By.XPATH,
                   "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT
                   }
        return actions[location[0]],location[1]

    def alerts_hendler(self,wait = 15):
        allert = WebDriverWait(self._driver, wait).until(EC.alert_is_present())
        print(allert.text)
        allert.accept()
        allert2 = WebDriverWait(self._driver, wait).until(EC.alert_is_present())
        if allert2:
            print(allert2.text)
            allert.accept()



