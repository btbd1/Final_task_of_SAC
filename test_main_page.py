import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:  # class for testing all about login
    def test_quest_should_see_login(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.check_is_basket_empty
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):  # main -> empty basket
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_in_empty_basket()
