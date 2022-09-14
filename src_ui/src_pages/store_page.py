import time
from src_ui.src_pages.base_page import Base_Page
from src_ui.src_drivers.driver_config import Meted, Driver


class StorePage(Base_Page):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locations = {"book-container": (Meted.CLASS_NAME, "book-container"),
                  "card_footer": (Meted.CLASS_NAME, "card-footer"),
                  "book_name": (Meted.CLASS_NAME, "card-title"),
                  "book_details": (Meted.CLASS_NAME, "card-text"),
                  "author_name": (Meted.CLASS_NAME, "list-group"),
                  "buy": (Meted.TAG_NAME, "button")}



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
        self._driver.click_on_it(self._locations["buy"], book)
        self._driver.alerts_hendler()

    def get_book_price(self, book):
        book_price = self.get_card_footer(book).split(" ")[1]
        return book_price

    def get_ammount_in_stock_of_book(self, book):
        ammount_in_stock = self.get_card_footer(book).split(" ")[5]
        return ammount_in_stock

    def get_book_name(self,book):
        book_name = self._driver.get_element(self._locations["book_name"], book).text
        return book_name

    def get_book_details(self,book):
        book_details = self._driver.get_element(self._locations["book_details"], book).text
        return book_details

    def get_book_author_name(self,book):
        book_author_name = self._driver.get_element(self._locations["author_name"], book).text[4::1]
        return book_author_name

    def get_card_footer(self, book):
        card_footer = self._driver.get_element(self._locations["card_footer"], book).text[:-8:1]
        return card_footer

    def get_book_container(self):
        books = self._driver.get_elements(self._locations["book-container"])
        return books