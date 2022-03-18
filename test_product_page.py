import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage

"""Файл с тестами страницы товара"""

'''Тест проверяет добавление незарегистрированным пользователем товара в корзину'''


@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу товара
    page.add_product_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()  # Решаем задачу
    page.product_basket_check_name()  # Проверяем наименование товара из сообщения и в карточке
    page.product_basket_check_price()  # Проверяем цену товара из сообщения и в карточке


"""Тест ищет нерабочую ссылку из переданных через фикстуру параметров. Функционал дублирует тест выше"""


@pytest.mark.skip
@pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 8, 9, pytest.param(7, marks=pytest.mark.skip)])  # Тест с 7 в
# ссылке падает, помечаем его меткой skip
def test_guest_can_add_product_to_basket_with_offer(browser, offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'  # Тест
    # запускается столько раз, сколько передано значений в списке параметров
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу товара
    page.add_product_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()  # Решаем задачу
    page.product_basket_check_name()  # Проверяем наименование товара из сообщения и в карточке
    page.product_basket_check_price()  # Проверяем цену товара из сообщения и в карточке


"""Тест проверяет что после добавления в корзину товара пользователем не появляется сообщение 
об успешном добавлении товара в корзину"""


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'  # Линк на товар без промоакции
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем переданный линк - ссылку на карточку товара
    page.add_product_to_basket()  # Добавляем товар в корзину
    page.should_not_be_success_message()  # Проверяем что не появилось сообщение об успешном добавлении товара в корзину


"""Тест проверяет что после открытия карточки товара не появляется сообщение об успешном добавлении товара в корзину"""


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'  # Линк на товар без промоакции
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем переданный линк - ссылку на карточку товара
    page.should_not_be_success_message()  # Проверяем что не появилось сообщение об успешном добавлении товара в корзину


"""Тест проверяет что после добавления товара в корзину пропадает сообщение об успешном добавлении товара в корзину"""


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'  # Линк на товар без промоакции
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем переданный линк - ссылку на карточку товара
    page.add_product_to_basket()  # Добавляем товар в корзину
    page.should_disappear_of_success_message()  # Проверяем что сообщение об успешном добавлении товара в корзину
    # пропадает

'''Тест проверяет наличие кнопки логина на основной странице'''

def test_should_be_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу
    page.should_be_login_link()  # Ищем кнопку логина на основной странице

'''Тест с проверкой возможности пользователя перейти с главной страницы на страницу логина
В качестве аргумента функции передается фикстура browser из файла conftest.py'''


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу
    page.go_to_login_page()  # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # Инициализируем LoginPage, передаем браузер и текущий URL
    # страницы - должен быть URL страницы логина
    login_page.should_be_login_page()  # Проверяем наличие login в текущем URL и наличие форм логина и регистрации
    # пользователя

