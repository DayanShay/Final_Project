from src_api.models import LoginDto, ApiUserDto
from src_ui.src_drivers.driver_config import Meted, Driver
from src_ui.src_pages.base_page import Base_Page


class LoginPage(Base_Page):
    def __init__(self, driver:Driver):
        super().__init__(driver)
        self.locations = {"Email_box": (Meted.ID,"email"),
                          "Password_box": (Meted.ID,"password"),
                          "Submit_button": (Meted.CSS_SELECTOR,'#root > div > form > button'),
                          "Register_button": (Meted.CSS_SELECTOR, '#root > div > button'),
                          "FirstName_box": (Meted.ID, "firstName"),
                          "LastName_box": (Meted.ID, "lastName"),
                          "Back_To_Login_button": (Meted.CSS_SELECTOR, '#root > div > button')
                          }


    def fill_email(self,text):
        self._driver.send_keys_to(self.locations["Email_box"], text=text)

    def fill_password(self,text):
        self._driver.send_keys_to(self.locations["Password_box"], text=text)

    def click_submit(self):
        Submit_button = self._driver.get_element(self.locations["Submit_button"])
        self._driver.click_on_it(Submit_button)

    def click_back_to_login(self):
        Back_To_Login_button = self._driver.get_element(self.locations["Back_To_Login_button"])
        self._driver.click_on_it(Back_To_Login_button)

    def click_register(self):
        register_btn = self._driver.get_element(self.locations["Register_button"])
        self._driver.click_on_it(register_btn)

    def fill_first_name(self,text):
        self._driver.send_keys_to(self.locations["FirstName_box"], text=text)

    def fill_last_name(self,text):
        self._driver.send_keys_to(self.locations["LastName_box"], text=text)

    def make_register(self,user:ApiUserDto):
        self.click_register()
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.fill_first_name(user.firstName)
        self.fill_last_name(user.lastName)
        self.click_submit()

    def make_login(self,user:LoginDto):
        from src_ui.src_pages.store_page import StorePage
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.click_submit()
        return StorePage(self._driver)

