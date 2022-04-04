from pages.locators import LoginPageLocators
from pages.base_page import BasePage
import time

"""Class LoginPage describes Login page with register and login methods """


class LoginPage(BasePage):
    """The method contains all the methods listed below in one"""

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_registration_form()

    """The method checks if current url contains word 'login'"""

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'The URL is not user login page'

    """The method checks is a user login form on current page"""

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), 'На странице отсутствует форма логина'

    """The method checks is a user register form on current page"""

    def should_be_registration_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), 'На странице отсутствует форма регистрации'

    """The method allows to register new user"""

    def register_new_user(self):
        random_email = str(time.time()) + '@test.ru'
        password = '123456_AQWRT'
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_REGISTRATION).send_keys(random_email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()





