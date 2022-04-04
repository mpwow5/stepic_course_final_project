from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

"""File contains tests for main page"""

"""Test checks is the cart empty after going to it from the main page
    1. Open main page
    2. Go to basket page
    3. Basket is empty"""


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()


"""Class contains tests for checking register user"""


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Test checks that the user can go from main page to login page
        1. Open main page
        2. Go to login page
        3. Current page have 'login' in URL, register and login form'"""

    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    '''The test checks for the presence of a login button on the main page
    1. Open main page
    2. Login link is presented on main page'''

    def test_should_be_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
