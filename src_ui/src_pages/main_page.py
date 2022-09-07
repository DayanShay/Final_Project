from src_ui.src_drivers.driver_config import Meted
from src_ui.src_pages.base_page import Base_Page



class Main_Page(Base_Page):
    def __init__(self,driver):
        self._driver = driver
        self.locations = {"log_in": (Meted.ID,"contact-link")}

    def click_log_in(self):
        self._driver.click_on_it(self.locations["log_in"])
