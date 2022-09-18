import time

from playwright.sync_api import Page
from src_ui.src_drivers.driver_config import Driver



class PlayWright(Driver):
    def __init__(self, driver:Page):
        super().__init__(driver)
        self._driver = driver


    def get_element(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        try:
            element = driver.locator(location)
        except :
            element = driver.query_selector(self.identy(location))
        return element

    def get_elements(self, location,driver: [] = None):
        if driver is None:
            driver = self._driver
        elements = driver.query_selector_all(self.identy(location))
        if len(elements) == 0:
            time.sleep(2)
            elements = driver.query_selector_all(self.identy(location))
        return elements

    def click_on_it(self, location):
        self.get_element(self.identy(location)).click()

    def send_keys_to(self, location, text):
        self._driver.locator(self.identy(location)).fill(text)

    def identy(self,location):
        if location[0] == "ID":
            return f"id={location[1]}"
        elif location[0] == "NAME":
            return f"[name={location[1]}]"
        elif location[0] == "TAG_NAME":
            return f"@={location[1]}"
        elif location[0] == "LINK_TEXT":
            return f'text="{location[1]}"'
        elif location[0] == "XPATH":
            return f'{location[1]}'
        elif location[0] == "CSS_SELECTOR":
            return f'{location[1]}'
        elif location[0] == "CLASS_NAME":
            return f'.{location[1]}'
    def alerts_hendler(self, wait=15):
        self._driver.on("dialog", lambda dialog: dialog.accept())
        self._driver.locator("button").click()
        pass
    def get_frame(self, location):
        pass
    def switch_to_default(self):
        pass
    def page_url(self):
        return self._driver.evaluate("document.URL")

    def get_book_img(self,location,driver=None):
        book_img = self.get_element(location,driver)
        return book_img.get_attribute("src")

    @staticmethod
    def get_text(self):
        return self.inner_text()
