from pages.product_page import ProductPage

"""Файл с тестами страницы товара"""

'''Тест проверяет добавление незарегистрированным пользователем товара в корзину'''


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)  # Инициализуем PageObject, передаем в конструктор экземпляр браузера (из
    # conftest.py) и url
    page.open()  # Открываем страницу товара
    page.add_product_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()  # Решаем задачу
    page.product_basket_check_name()  # Проверяем наименование товара из сообщения и в карточке
    page.product_basket_check_price()  # Проверяем цену товара из сообщения и в карточке
