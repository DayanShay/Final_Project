from src_ui.src_pages.author_page import AuthorPage
from src_ui.src_pages.base_page import Base_Page
from src_ui.src_drivers.driver_config import Meted, Driver


class SearchPage(Base_Page):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locations = {"book-container": (Meted.CLASS_NAME, "book-container"),
                  "card_footer": (Meted.CLASS_NAME, "card-footer"),
                  "book_name": (Meted.CLASS_NAME, "card-title"),
                  "book_details": (Meted.CLASS_NAME, "card-text"),
                  "author_name": (Meted.CLASS_NAME, "card-title"),
                  "author_container": (Meted.CLASS_NAME, "author-container"),
                  "author_book_name": (Meted.CLASS_NAME, "list-group-item"),
                  "to_author_page": (Meted.TAG_NAME, "button"),
                  "book_img": (Meted.CLASS_NAME, "card-img-top")
                  }

    def get_book_container(self):
        books = self._driver.get_elements(self._locations["book-container"])
        return books

    def get_book_price(self, book):
        book_price = self.get_book_card_footer(book)[1]
        return book_price

    def get_ammount_in_stock_of_book(self, book):
        ammount_in_stock = self.get_book_card_footer(book)[5]
        return ammount_in_stock

    def get_book_name(self, book):
        book_name_location = self._driver.get_element(self._locations["book_name"], book)
        book_name = self._driver.get_text(book_name_location)
        return book_name

    def get_book_details(self, book):
        book_details_location = self._driver.get_element(self._locations["book_details"], book)
        book_details = self._driver.get_text(book_details_location)
        return book_details

    def get_book_author_name(self, book):
        book_author_name_location = self._driver.get_element(self._locations["author_name"], book)
        book_author_name = self._driver.get_text(book_author_name_location)[4::1]
        return book_author_name

    def get_book_card_footer(self, book):
        card_footer_location = self._driver.get_element(self._locations["card_footer"], book)
        card_footer = self._driver.get_text(card_footer_location)
        return card_footer

    def get_author_container(self):
        authors = self._driver.get_elements(self._locations["author_container"])
        return authors

    def get_card_footer(self, footer):
        card_footer_location = self._driver.get_element(self._locations["card_footer"], footer)
        return card_footer_location.split(" ")

    def get_author_name(self, author):
        author_name_location = self._driver.get_element(self._locations["author_name"], author)
        author_name = self._driver.get_text(author_name_location)
        return author_name

    def click_go_to_author_page(self, author):
        self._driver.click_on_it(self._locations["to_author_page"], author)
        return AuthorPage(self._driver)


    def get_book_img(self,book):
        book_img = self._driver.get_book_img(self._locations["book_img"],book)
        return book_img