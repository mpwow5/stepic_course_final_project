from selenium.webdriver.common.by import By

from pages.base_page import BasePage

'''Файл содержит класс MainPage, описывающий главную страницу сайта'''


class MainPage(BasePage):
    '''Метод ищет кнопку с переходом на страницу логина и нажимает на нее'''

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()

    '''Метод ищет кнопку с переходом на страницу логина'''

    def should_be_login_link(self):
        assert self.is_element_presented(By.CSS_SELECTOR, "#login_link_invalid"), 'Login link not found'  # Указываем
        # заведомо нерабочий селектор
