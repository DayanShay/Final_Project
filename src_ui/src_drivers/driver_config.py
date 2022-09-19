from abc import ABC, abstractmethod

from selenium.webdriver.chrome.webdriver import WebDriver


class Driver(ABC):
    """
    abstractmethod for creating driver
    """

    def __init__(self, driver:WebDriver):
        self._driver = driver

    @abstractmethod
    def get_element(self, location,driver=None, wait: int = 5):
        pass

    @abstractmethod
    def get_elements(self, location,driver=None):
        pass

    @abstractmethod
    def click_on_it(self, element):
        pass

    @abstractmethod
    def send_keys_to(self, location, text):
        pass

    @abstractmethod
    def identy(self, location):
        pass

    @abstractmethod
    def alerts_hendler(self,element):
        pass

    @abstractmethod
    def page_url(self):
        pass
    @abstractmethod
    def get_text(self):
        pass
    @abstractmethod
    def get_book_img(self,book):
        pass
    @abstractmethod
    def refrash_page(self):
        pass


class Meted:
    ID = "ID"
    NAME = "NAME"
    TAG_NAME = "TAG_NAME"
    LINK_TEXT = "LINK_TEXT"
    CLASS_NAME = "CLASS_NAME"
    XPATH = "XPATH"
    CSS_SELECTOR = "CSS_SELECTOR"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
