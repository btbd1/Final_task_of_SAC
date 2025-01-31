from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "No one items in basket"

    def should_be_message_in_empty_basket(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en-gb": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-hans": "Your basket is empty.",
            "en-US": "Your basket is empty."
        }
        text_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        current_language_value = self.check_page_language()
        print(f"Detected language: {current_language_value}")
        for key, value in languages.items():
            if key == current_language_value:
                language_message = value
                assert language_message in text_message, "Message of empty basket not found"
                print(f'Expected result: {language_message}; got: {text_message}')
