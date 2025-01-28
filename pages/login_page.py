from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = "login"
        current_url = self.get_current_url()
        print(current_url)
        assert substring in current_url, "Substring 'login' is not detected in url"

    def should_be_login_form(self):
        assert self.is_element_present(*Locators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*Locators.REGISTER_FORM), "Register form is not presented"
