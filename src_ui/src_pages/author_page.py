from src_ui.src_pages.base_page import Base_Page
from src_ui.src_drivers.driver_config import Meted, Driver


class AuthorPage(Base_Page):
    def __init__(self, driver: Driver):
        super().__init__(driver)
    _locations = {"book-container": (Meted.CLASS_NAME, "book-container"),
                  "card_footer": (Meted.CLASS_NAME, "card-footer"),
                  "book_name": (Meted.CLASS_NAME, "card-title"),
                  "book_details": (Meted.CLASS_NAME, "card-text"),
                  "author_name": (Meted.CLASS_NAME, "list-group"),
                  "google_map":(Meted.XPATH,'//*[@id="mapDiv"]/div/div/div[4]/div/div/div/div'),
                  "google_frame":(Meted.ID,'iframeId')
                  }

    def get_book_container(self):
        books = self._driver.get_elements(self._locations["book-container"])
        return books

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
        card_footer = self._driver.get_element(self._locations["card_footer"], book).text
        return card_footer

    def get_home_location(self):
        google_frame = self._driver.get_element(self._locations["google_frame"])
        self._driver.get_frame(google_frame)
        google_map_text = self._driver.get_element(self._locations["google_map"]).text.split("\n")
        home_location = google_map_text[0].split(" ")
        homeLatitude = home_location[0]
        homeLongitude = home_location[1]
        self._driver.switch_to_default()
        return homeLatitude,homeLongitude

