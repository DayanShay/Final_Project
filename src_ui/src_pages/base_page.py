import time

from selenium.webdriver.chrome.webdriver import WebDriver
from src_ui.src_drivers.driver_config import Meted, Driver


class Base_Page:
    def __init__(self, driver:Driver):
        self._driver = driver
        self.locations_base = {"Login": (Meted.LINK_TEXT,"Log In"),
                               "Book_Store_Logo_button": (Meted.LINK_TEXT, "Book Store"),
                               "login_button": (Meted.ID, "contact-link"),
                               "Store_button": (Meted.LINK_TEXT, "Store"),
                               "Authors_button": (Meted.LINK_TEXT, "Authors"),
                               "Search_fild": (Meted.ID, "searchtext"),
                               "Search_btn": (Meted.XPATH,'//*[@id="root"]/nav/div/form/button'),
                               "Search_location": (Meted.CLASS_NAME, "d-flex")}

    def click_log_in(self):
        from src_ui.src_pages.login_page import LoginPage
        Login_button = self._driver.get_element(self.locations_base["Login"])
        self._driver.click_on_it(Login_button)
        return LoginPage(self._driver)

    def click_store_page_logo(self):
        from src_ui.src_pages.store_page import StorePage
        Book_Store_Logo_button = self._driver.get_element(self.locations_base["Book_Store_Logo_button"])
        self._driver.click_on_it(Book_Store_Logo_button)
        return StorePage(self._driver)

    def click_store_page_button(self):
        from src_ui.src_pages.store_page import StorePage
        Store_button = self._driver.get_element(self.locations_base["Store_button"])
        self._driver.click_on_it(Store_button)
        return StorePage(self._driver)

    def click_authors_button(self):
        from src_ui.src_pages.authors_page import AuthorsPage
        Authors_button = self._driver.get_element(self.locations_base["Authors_button"])
        self._driver.click_on_it(self.locations_base[Authors_button])
        return AuthorsPage(self._driver)

    def search(self,text):
        from src_ui.src_pages.search_page import SearchPage
        search_place = self._driver.get_element(self.locations_base["Search_location"])
        self._driver.send_keys_to(self.locations_base["Search_fild"],search_place,text)
        Search_btn = self._driver.get_element(self.locations_base["Search_btn"], search_place)
        self._driver.click_on_it(Search_btn)
        if not text:
            Search_btn = self._driver.get_element(self.locations_base["Search_btn"],search_place)
            self._driver.click_on_it(Search_btn)
        return SearchPage(self._driver)


    def get_page_url(self):
        time.sleep(2)
        return self._driver.page_url()

    def page_refrash(self):
        self._driver.refrash_page()
