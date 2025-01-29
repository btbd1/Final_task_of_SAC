from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "No one items in basket"

    def should_be_message_in_empty_basket(self):
        text_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        substring_en = "Your basket is empty."
        assert substring_en in text_message, "Message of empty basket not found"

    # def should_be_message_in_empty_basket(self):
    #     languages = {
    #         "ar": "سلة التسوق فارغة",
    #         "ca": "La seva cistella està buida.",
    #         "cs": "Váš košík je prázdný.",
    #         "da": "Din indkøbskurv er tom.",
    #         "de": "Ihr Warenkorb ist leer.",
    #         "en": "Your basket is empty.",
    #         "el": "Το καλάθι σας είναι άδειο.",
    #         "es": "Tu carrito esta vacío.",
    #         "fi": "Korisi on tyhjä",
    #         "fr": "Votre panier est vide.",
    #         "it": "Il tuo carrello è vuoto.",
    #         "ko": "장바구니가 비었습니다.",
    #         "nl": "Je winkelmand is leeg",
    #         "pl": "Twój koszyk jest pusty.",
    #         "pt": "O carrinho está vazio.",
    #         "pt-br": "Sua cesta está vazia.",
    #         "ro": "Cosul tau este gol.",
    #         "ru": "Ваша корзина пуста",
    #         "sk": "Váš košík je prázdny",
    #         "uk": "Ваш кошик пустий.",
    #         "zh-cn": "Your basket is empty.",
    #         "en-US": "Your basket is empty."
    #     }
    #     text_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
    #     current_language_value = self.check_page_language()
    #     for key, value in languages.items():
    #         if key == current_language_value:
    #             language_message = value
    #             print(language_message)
    #             assert language_message in text_message, "Message of empty basket not found"
