from selenium.webdriver.common.by import By

'''Файл содержит селекторы всех элементов для тестов. Каждая константа представляет собой кортеж из двух элементов - 
что ищем и как '''

'''Селекторы абстрактной базовой страницы - подходят для любой страницы на сайте'''


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Селектор кнопки логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # Заведомо некорректный селектор для
    # проверки сообщения об ошибке
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a')  # Селектор перехода в корзину


'''Селекторы на главной странице'''


class MainPageLocators:
    pass


'''Селекторы на странице логина'''


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')  # Селектор формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')  # Селектор формы регистрации


'''Селекторы на карточках товара'''


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')  # Селектор кнопки "Добавить в корзину"
    PRODUCT_ADD_TO_BASKET_NAME = (By.CSS_SELECTOR, 'div.alertinner>strong')  # Селектор наименования товара из
    # всплывающего сообщения после добавления товара в корзину
    PRODUCT_ADD_TO_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner>p>strong')  # Селектор цены из всплывающего
    # сообщения после добавления товара в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div>h1')  # Селектор имени товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')  # Селектор цены товара. Селектор не уникальный, но первый в
    # списке нам подходит
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')  # Селектор сообщения успешного добавления товара в
    # корзину - ищется первый элемент, для теста подходит


'''Селекторы в корзине'''


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')  # Селектор сообщения пустой корзины
