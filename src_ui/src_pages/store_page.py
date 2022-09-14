import time
from src_ui.src_pages.base_page import Base_Page
from src_ui.src_drivers.driver_config import Meted, Driver


class StorePage(Base_Page):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locations = {"book-container": (Meted.CLASS_NAME, "book-container"),
                  "card_group": (Meted.CLASS_NAME, "card-group"),
                  "card_footer": (Meted.CLASS_NAME, "card-footer"),
                  "buy": (Meted.TAG_NAME, "button")}

    def get_card_group(self):
        books = self._driver.get_elements(self._locations["book-container"])
        return books

    # def get_book_title(self,book):
    #     self._driver.get_element("title location",book)
    #
    # def get_book_by_title(self,title):
    #     books = self.get_book_container()
    #     for book in books:
    #         if self.get_book_title(book) == title:
    #             return book
    #     return None

    def click_buy(self, book):
        buy_button = self._driver.get_element(self._locations["buy"], book)
        try:
            buy_button.click()
        except:
            buy_button.click()
        self._driver.alerts_hendler()
