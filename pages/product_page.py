from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        self.browser.find_element(*Locators.ADD_TO_BASKET).click()

    def check_item_added_to_basket(self):
        self.check_item_name()
        self.check_item_price()

    def check_item_name(self):
        name_text = self.browser.find_element(*Locators.ITEM_NAME).text
        alert_success_text = self.browser.find_element(*Locators.ALERT_SUCCESS).text
        assert name_text == alert_success_text, f'Item name not in alert success'

    def check_item_price(self):
        price_text = self.browser.find_element(*Locators.ITEM_PRICE).text
        alert_info_text = self.browser.find_element(*Locators.ALERT_INFO).text
        assert price_text == alert_info_text, f"Item price doesn't match with alert info"
