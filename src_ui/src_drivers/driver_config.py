from abc import ABC, abstractmethod
from selenium import webdriver


class Driver(ABC):
    """
    abstractmethod for creating driver
    """

    def __init__(self, driver:webdriver):
        self._driver = driver

    @abstractmethod
    def get_element(self, location,driver=None, wait: int = 5):
        pass

    @abstractmethod
    def get_elements(self, location,driver=None, wait: int = 5):
        pass

    @abstractmethod
    def click_on_it(self, location, wait: int = 5):
        pass

    @abstractmethod
    def send_keys_to(self, location, text):
        pass

    @abstractmethod
    def identy(self, location):
        pass

    @abstractmethod
    def alerts_hendler(self):
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
