from src_ui.src_pages.author_page import AuthorPage
from src_ui.src_pages.base_page import Base_Page
from src_ui.src_drivers.driver_config import Meted, Driver


class AuthorsPage(Base_Page):
    def __init__(self, driver: Driver):
        super().__init__(driver)
        self._locations = {"author_container": (Meted.CLASS_NAME, "author-container"),
                           "author_name": (Meted.CLASS_NAME, "card-title"),
                           "to_author_page": (Meted.TAG_NAME, "button"),
                           "card_footer": (Meted.CLASS_NAME, "card-footer"),
                           }

    def get_author_container(self):
        authors = self._driver.get_elements(self._locations["author_container"])
        return authors

    def get_card_footer(self, author):
        card_footer = self._driver.get_element(self._locations["card_footer"], author)
        return card_footer

    def get_author_name(self, author):
        author_name = self._driver.get_element(self._locations["author_name"], author).text
        return author_name

    def click_go_to_author_page(self, author):
        to_author_page = self._driver.get_element(self._locations["to_author_page"],author)
        self._driver.click_on_it(to_author_page)
        return AuthorPage(self._driver)
