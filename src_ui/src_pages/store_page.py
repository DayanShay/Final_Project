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
                  "buy": (Meted.TAG_NAME, "button"),
                  "book_img": (Meted.CLASS_NAME, "card-img-top")}



    def click_buy(self, book):
        cart_footer = self._driver.get_element(self._locations["card_footer"],book)
        buy_button = self._driver.get_element(self._locations["buy"],cart_footer)
        return self._driver.alerts_hendler(buy_button)

    def get_book_img(self,book):
        book_img = self._driver.get_book_img(self._locations["book_img"],book)
        return book_img



    def get_book_price(self, book):
        book_price = self.get_card_footer(book).split(" ")[1]
        return book_price

    def get_ammount_in_stock_of_book(self, book):
        ammount_in_stock = self.get_card_footer(book).split(" ")[5]
        return ammount_in_stock

    def get_book_name(self,book):
        book_name = self._driver.get_element(self._locations["book_name"], book)
        book_name = self._driver.get_text(book_name)
        return book_name

    def get_book_details(self,book):
        book_details = self._driver.get_element(self._locations["book_details"], book)
        book_details = self._driver.get_text(book_details)
        return book_details

    def get_book_author_name(self,book):
        book_author_name = self._driver.get_element(self._locations["author_name"], book)
        book_author_name = self._driver.get_text(book_author_name)
        return book_author_name[4::1]

    def get_card_footer(self, book):
        card_footer = self._driver.get_element(self._locations["card_footer"], book)
        card_footer = self._driver.get_text(card_footer)
        return card_footer[:-8:1]

    def get_book_container(self):
        books = self._driver.get_elements(self._locations["book-container"])
        return books