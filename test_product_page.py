import pytest

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
