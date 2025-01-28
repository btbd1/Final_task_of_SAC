from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators as Locators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*Locators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*Locators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):  # переход на новую страницу
        link = self.browser.find_element(*Locators.LOGIN_LINK)
        link.click()
