from pages.locators import ProductPageLocators
from pages.base_page import BasePage

"""Class ProductPage describes product page and contains methods for adding product to cart"""


class ProductPage(BasePage):
    """The method describes adding a product to the cart"""

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    """The method search the product name from the card and compares it with the product name from the pop-up
    messages after adding product to cart"""

    def product_basket_check_name(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text, 'Name in product cart and name in basket message ' \
                                                     'is different'

    """The method search the price of the product from the card and compares it with the price of the product from 
    the pop-up messages """

    def product_basket_check_price(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, 'Price in product cart and price in basket message is ' \
                                                      'different'

    """The method checks that the message about the successful adding product to the cart does not appear"""

    def should_not_be_success_message(self):
        assert self.is_not_element_presented(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not " \
                                                                                        "displayed "

    """The method checks that the message about the successful adding product to the cart disappears"""

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not disappeared'
