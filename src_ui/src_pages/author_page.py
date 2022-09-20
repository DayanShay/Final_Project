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
                  "google_map": (Meted.XPATH, '//*[@id="mapDiv"]/div/div/div[4]/div/div/div/div'),
                  "google_frame": (Meted.ID, 'iframeId'),
                  "author_name_top": (Meted.CLASS_NAME, 'bg-secondary'),
                  "book_img": (Meted.CLASS_NAME, "card-img-top")
                  }

    def get_author_name_top(self):
        author_name_top = self._driver.get_element(self._locations["author_name_top"])
        author_name = self._driver.get_text(author_name_top)
        return author_name

    def get_book_container(self):
        books = self._driver.get_elements(self._locations["book-container"])
        return books

    def get_book_price(self, book):
        book_price = self.get_card_footer(book).split(" ")[1]
        return book_price

    def get_ammount_in_stock_of_book(self, book):
        ammount_in_stock = self.get_card_footer(book).split(" ")[5]
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
        book_author_name = self._driver.get_text(book_author_name_location)
        return book_author_name[4::1]

    def get_card_footer(self, book):
        card_footer_location = self._driver.get_element(self._locations["card_footer"], book)
        card_footer = self._driver.get_text(card_footer_location)
        return card_footer

    def get_home_location(self):
        google_frame = self._driver.get_element(self._locations["google_frame"])
        google_map_text_location = self._driver.get_frame(google_frame,self._locations["google_map"])
        google_map_text = google_map_text_location.split("\n")
        home_location = google_map_text[0].split(" ")
        homeLatitude = home_location[0]
        homeLongitude = home_location[1]
        return self.convert_to_float_number(homeLatitude, homeLongitude)

    def convert_to_float_number(self, homeLatitude, homeLongitude):
        latitude = homeLatitude.replace("'", "-").replace("°", "-").replace('"', "")
        longitude = homeLongitude.replace("'", "-").replace("°", "-").replace('"', "")
        N = 'N' in latitude
        d, m, s = map(float, latitude[:-1].split('-'))
        latitude1 = (d + m / 60. + s / 3600.) * (1 if N else -1)
        W = 'W' in longitude
        d, m, s = map(float, longitude[:-1].split('-'))
        longitude1 = (d + m / 60. + s / 3600.) * (-1 if W else 1)
        return round(latitude1 + 0.0000001, 4), round(longitude1 + 0.000005, 4)

    def get_book_img(self, book):
        book_img = self._driver.get_book_img(self._locations["book_img"], book)
        return book_img
