from abc import ABC, abstractmethod


class Driver(ABC):
    """
    abstractmethod for creating driver
    """

    def __init__(self, driver):
        self._driver = driver

    @abstractmethod
    def get_element(self, location,driver, wait: int = 5):
        pass

    @abstractmethod
    def get_elements(self, location,driver, wait: int = 5):
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


class Meted:
    ID = "ID"
    NAME = "NAME"
    TAG_NAME = "TAG_NAME"
    TEXT = "TEXT"
    CLASS_NAME = "CLASS_NAME"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
    CSS_SELECTOR = "CSS_SELECTOR"
