import os
from playwright.sync_api import Page
from src_ui.src_drivers.driver_config import Driver


class PlayWright(Driver):
    def __init__(self, driver: Page):
        super().__init__(driver)
        self._driver = driver
        self.text1 = []

    def get_element(self, location: tuple[[], str], driver: [] = None):
        if driver is None:
            driver = self._driver
        element = driver.query_selector(self.identy(location))
        return element

    def get_elements(self, location, driver: [] = None):
        if driver is None:
            driver = self._driver
        elements = driver.query_selector_all(self.identy(location))
        temp_elements = driver.query_selector_all(self.identy(location))
        return temp_elements if len(elements) <= len(temp_elements) else temp_elements

    def click_on_it(self, element):
        element.click()

    def send_keys_to(self, location, text=""):
        self._driver.locator(self.identy(location)).fill(text)

    def alerts_hendler(self, element=None):
        def handle_dialog(dialog):
            dialog.accept()
            self.text1.append(dialog.message)

        self._driver.on("dialog", handle_dialog)
        self.click_on_it(element)
        text = self.text1
        self.text1 = []
        return text

    def get_frame(self, google_frame, location):
        frame_text = google_frame.content_frame().inner_text(self.identy(location))
        if frame_text == "" or None:
            frame_text = google_frame.content_frame().inner_text(self.identy(location))
        return frame_text

    def page_url(self):
        return self._driver.evaluate("document.URL")

    def get_book_img(self, location, book):
        book_img = self.get_element(location, book)
        return book_img.get_attribute("src")

    def get_text(self, element):
        return element.inner_text()

    def refrash_page(self):
        self._driver.reload()

    def close_page(self):
        self._driver.close()

    def get_screen_shoot(self):
        pic_name = f"img.png"
        pic = self._driver.screenshot(path=fr"{pic_name}")
        os.remove(pic_name)
        return pic

    def identy(self, location):
        actions = {"ID": f'id={location[1]}',
                   "NAME": f'[name={location[1]}]',
                   "TAG_NAME": f'{location[1]}',
                   "LINK_TEXT": f'text="{location[1]}"',
                   "CLASS_NAME": f'.{location[1]}',
                   "CSS_SELECTOR": f'{location[1]}',
                   "XPATH": f'{location[1]}'
                   }
        return actions[location[0]]
