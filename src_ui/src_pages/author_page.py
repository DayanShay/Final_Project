from src_ui.src_pages.base_page import Base_Page


class AuthorPage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.locations = {}


