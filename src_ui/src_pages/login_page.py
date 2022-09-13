from src_ui.src_drivers.driver_config import Meted
from src_ui.src_pages.base_page import Base_Page



class LogIn(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.locations = {"Login": (Meted.TEXT,"Log In"),
                          "Email_box": (Meted.ID,"email"),
                          "Password_box": (Meted.ID,"password"),
                          "Submit_button": (Meted.CSS_SELECTOR,"#root > div > form > button"),
                          "Register_button": (Meted.TEXT, "Register!"),
                          "FirstName_box": (Meted.ID, "firstName"),
                          "LastName_box": (Meted.ID, "lastName"),
                          "Back_To_Login_button": (Meted.TEXT, "button")
                          }

    def click_log_in(self):
        self._driver.click_on_it(self.locations["Login"])

    def click_store_page_logo(self):
        self._driver.click_on_it(self.locations_base["Book_Store_Logo_button"])

    def click_store_page_button(self):
        self._driver.click_on_it(self.locations_base["Store_button"])

    def click_authors_button(self):
        self._driver.click_on_it(self.locations_base["Authors_button"])

    def fill_email(self,text):
        self._driver.send_keys_to(self.locations["Email_box"],text=text)

    def fill_password(self,text):
        self._driver.send_keys_to(self.locations["Password_box"],text=text)

    def click_submit(self):
        self._driver.click_on_it(self.locations["Submit_button"])

    def click_back_to_login(self):
        self._driver.click_on_it(self.locations["Back_To_Login_button"])

    def click_register(self):
        self._driver.click_on_it(self.locations["Register_button"])

    def fill_first_name(self,text):
        self._driver.send_keys_to(self.locations["Email_box"],text=text)

    def fill_last_name(self,text):
        self._driver.send_keys_to(self.locations["Password_box"],text=text)

    def make_login(self,email,password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_submit()