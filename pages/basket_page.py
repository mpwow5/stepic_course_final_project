from pages.base_page import BasePage
from pages.locators import BasketPageLocators

"""Class BasketPage describes basket page and contains methods for working with the Webdriver"""


class BasketPage(BasePage):
    """The method checks that the basket is empty"""

    def is_basket_empty(self):
        assert 'Your basket is empty' in self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE).text, "Basket is not empty"
