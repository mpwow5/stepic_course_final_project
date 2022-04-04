from selenium.webdriver.common.by import By

"""The file contains selectors of all elements for tests"""

"""Abstract base page selectors - can be used on any page of the site"""


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Selector for login button
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # Selector for login button, used for check error message
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a')  # Selector for opening basket button
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # Selector for authorized user icon


"""Main page selectors"""


class MainPageLocators:
    pass


"""Login page selectors"""


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')  # Selector for user login form
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')  # Selector for user register form
    EMAIL_FIELD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-email')  # Selector for email field in
    # registration form
    PASSWORD_FIELD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password1')  # Selector for password field in
    # registration form
    PASSWORD_CONFIRM_FIELD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password2')  # Selector for confirming
    # password field in registration form
    REGISTER_BUTTON = (By.NAME, 'registration_submit')  # Selector for button "Register"


"""Selector for product page"""


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')  # Selector for "Add to basket" button
    PRODUCT_ADD_TO_BASKET_NAME = (By.CSS_SELECTOR, 'div.alertinner>strong')  # Selector for product name from pop-up
    # window after adding product to basket
    PRODUCT_ADD_TO_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner>p>strong')  # Selector for product price from pop-up
    # window after adding product to basket
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div>h1')  # Selector for product name from product page
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')  # Selector for product price from product page
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')  # Selector for pop-up message after successfully adding
    # product to basket


'''Selectors for basket page'''


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')  # Selector for empty basket message
