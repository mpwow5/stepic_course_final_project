from pages.main_page import MainPage

"""Файл с тестами главной страницы"""

'''Тест с проверкой возможности пользователя перейти с главной страницы на страницу логина
В качестве аргумента функции передается фикстура browser из файла conftest.py'''


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу
    page.go_to_login_page()  # Выполняем метод страницы (класс BaseObject) и переходим на страницу логина
