import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

"""File contains tests for product page"""

"""Adding an item to the cart by an unregistered user:
    1. Open product page
    2. Add product to basket
    3. Enter CAPTCHA
    4. Check product name in pop-up windows matches name in product cart
    5. Check product price in pop-up windows matches price in product cart"""


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_basket_check_name()
    page.product_basket_check_price()


"""Searching for a broken URL from the parameters passed through the fixture. Test steps are similar to the test 
above """


@pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 8, 9, pytest.param(7, marks=pytest.mark.skip)])
def test_guest_can_add_product_to_basket_with_offer(browser, offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_basket_check_name()
    page.product_basket_check_price()


"""Test checks that after adding a product to the cart by user, no message appears
about the successful addition of the product to the cart
    1. Open product page
    2. Add product to basket
    3. No pop-up message should be appeared"""


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


"""Test checks that after opening a product page, no message appears
about the successful addition of the product to the cart
    1. Open product page
    2. No pop-up message should be appeared"""


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


"""Test checks that after adding a product to cart, pop-up message dissapearing
    1. Open product page
    2. Add product to basket
    3. Pop-up message disappears"""


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_of_success_message()


'''The test checks for the presence of a login button on the product page
    1. Open product page
    2. Login link is presented on product page'''


def test_should_be_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


"""Test checks that the user can go from product page to login page
    1. Open product page
    2. Go to login page
    3. Current page have 'login' in URL, register and login form'"""


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


"""Test checks is the cart empty after going to it from the product page
    1. Open product page
    2. Go to basket page
    3. Basket is empty"""


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()


"""Test checks is the cart empty after going to it from the login page
    1. Open login page
    2. Go to basket page
    3. Basket is empty"""


def test_guest_cant_see_product_in_basket_opened_from_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()


"""Class contains tests for registered user"""


class TestUserAddToBasketFromProductPage:
    """Fixture for register new user"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user()

    """Test checks that after opening a product page, no message appears
    about the successful addition of the product to the cart for registered user
        1. Open product page
        2. No pop-up message should be appeared"""

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    """Adding an item to the cart by an registered user:
    1. Open product page
    2. Add product to basket
    3. Check product name in pop-up windows matches name in product cart
    4. Check product price in pop-up windows matches price in product cart"""

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.product_basket_check_name()
        page.product_basket_check_price()
