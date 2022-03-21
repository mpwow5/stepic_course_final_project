from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

"""Файл с тестами главной страницы"""


'''Тест проверяет пустая ли корзина при переходе в нее с главной страницы'''


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу
    page.go_to_basket()  # Переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)  # Инициализируем PageObject корзины
    basket_page.is_basket_empty()  # Проверяем пустая ли корзина


"""Класс содержит тесты с проверкой функционала логина пользователя"""


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Тест с проверкой возможности пользователя перейти с главной страницы на страницу логина
    В качестве аргумента функции передается фикстура browser из файла conftest.py"""

    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
        # conftest.py) и url
        page.open()  # Открываем страницу
        page.go_to_login_page()  # Переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # Инициализируем LoginPage, передаем браузер и текущий URL
        # страницы - должен быть URL страницы логина
        login_page.should_be_login_page()  # Проверяем наличие login в текущем URL и наличие форм логина и регистрации
        # пользователя

    '''Тест проверяет наличие кнопки логина на основной странице'''

    def test_should_be_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
        # conftest.py) и url
        page.open()  # Открываем страницу
        page.should_be_login_link()  # Ищем кнопку логина на основной странице

