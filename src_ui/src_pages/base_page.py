from src_ui.src_drivers.driver_config import Meted


class Base_Page():
    def __init__(self, driver):
        self._driver = driver
        self.locations_base = {"Book_Store_Logo_button": (Meted.TEXT, "Book Store"),
                               "login_button": (Meted.ID, "contact-link"),
                               "Store_button": (Meted.TEXT, "Store"),
                               "Authors_button": (Meted.TEXT, "Authors")}