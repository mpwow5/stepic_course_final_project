from pages.locators import ProductPageLocators
from pages.base_page import BasePage

'''Файл содержит класс ProductPage, описывающий страницу товара'''


class ProductPage(BasePage):
    """Метод описывает добавления товара корзину"""

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)  # Ищем кнопку
        # добавления товара
        add_to_basket_button.click()  # Добавляем товар в корзину

    """Метод проверяет наименование товара из карточки и сравнивает его с наименованием товара из всплывающего 
    сообщения """

    def product_basket_check_name(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text, 'Price in product cart and price in basket message ' \
                                                     'is different'  # Проверяем совпадения наименования
        # из всплывающего сообщения и наименования товара из карточки

    """Метод проверяет цену товара из карточки и сравнивает его с ценой товара из всплывающего 
    сообщения """

    def product_basket_check_price(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, 'Price in product cart and price in basket message is ' \
                                                      'different'  # Проверяем совпадения цены из
        # всплывающего сообщения и цены товара из карточки

    """Метод проверяет что сообщение об успешном добавлении товара в корзину не появляется"""

    def should_not_be_success_message(self):
        assert self.is_not_element_presented(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not " \
                                                                                        "displayed "

    """Метод проверяет что сообщение об успешном добавлении товара в корзину пропадает"""

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not disappeared'
