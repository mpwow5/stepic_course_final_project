from pages.locators import LoginPageLocators
from pages.base_page import BasePage

'''Файл содержит класс LoginPage, описывающий страницу логина и регистрации сайта'''


class LoginPage(BasePage):
    """Метод объединяет в себе все три проверки"""

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_registration_form()

    """Метод проверки наличия login в текущем url"""

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'В ссылке отсутствует login'

    """Метод проверки наличия на странице формы логина пользователя"""

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), 'На странице отсутствует форма логина'

    """Метод проверки наличия на странице формы регистрации пользователя"""

    def should_be_registration_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), 'На странице отсутствует форма регистрации'
