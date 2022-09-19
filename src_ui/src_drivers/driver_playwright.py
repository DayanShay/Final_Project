import time

from playwright.sync_api import Page
from src_ui.src_drivers.driver_config import Driver



class PlayWright(Driver):
    def __init__(self, driver:Page):
        super().__init__(driver)
        self._driver = driver
        self.text1 = []


    def get_element(self, location: tuple[[], str],driver: [] = None, wait: int = 5):
        if driver is None:
            driver = self._driver
        element = driver.query_selector(self.identy(location))
        return element

    def get_elements(self, location,driver: [] = None):
        if driver is None:
            driver = self._driver
        elements = driver.query_selector_all(self.identy(location))
        if len(elements) == 0:
            elements = driver.query_selector_all(self.identy(location))
            if len(elements) == 0:
                self.refrash_page()
                time.sleep(3)
                elements = driver.query_selector_all(self.identy(location))
        return elements

    def click_on_it(self, element):
        element.click()

    def send_keys_to(self, location, text):
        self._driver.locator(self.identy(location)).fill(text)

    def identy(self,location):
        if location[0] == "ID":
            return f"id={location[1]}"
        elif location[0] == "NAME":
            return f"[name={location[1]}]"
        elif location[0] == "TAG_NAME":
            return f"{location[1]}"
        elif location[0] == "LINK_TEXT":
            return f'text="{location[1]}"'
        elif location[0] == "XPATH":
            return f'{location[1]}'
        elif location[0] == "CSS_SELECTOR":
            return f'{location[1]}'
        elif location[0] == "CLASS_NAME":
            return f'.{location[1]}'
    def alerts_hendler(self,element=None):
        def handle_dialog(dialog):
            dialog.accept()
            self.text1.append(dialog.message)
        self._driver.on("dialog", handle_dialog)
        self.click_on_it(element)
        return self.text1


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

    def refrash_page(self):
        self._driver.reload()

