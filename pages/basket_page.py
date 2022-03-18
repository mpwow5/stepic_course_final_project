import pytest

from pages.base_page import BasePage
from pages.locators import BasketPageLocators

'''Файл содержит класс BasketPage, описывающий корзину на сайте'''

class BasketPage(BasePage):
    '''Метод проверяет пустая ли корзина'''

    def is_basket_empty(self):
        assert 'Your basket is empty' in self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE).text, "Basket is not empty"  # Проверяем вхождение ключевой
        # фразы о пустой корзине в тексте найденного элемента
