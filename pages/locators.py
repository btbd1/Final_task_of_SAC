from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_INFO = (By.CSS_SELECTOR, ".alert-info strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
