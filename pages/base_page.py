import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators

"""Класс описывает базовую страницу, от которой будут наследованы остальные страницы.
Класс содержит вспомогательные методы по работе с драйвером"""


class BasePage:
    '''Конструктор, вызывается при инициализации объекта BasePage.'''

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)  # Указываем неявное ожидание

    '''Метод ищет кнопку с переходом на страницу логина и нажимает на нее'''

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    '''Метод ищет кнопку с переходом на страницу логина'''

    def should_be_login_link(self):
        assert self.is_element_presented(*BasePageLocators.LOGIN_LINK), 'Login link not found'

    '''Метод для открытия страницы в браузере. Browser - из фикстуры, link из файлов с тестами'''

    def open(self):
        self.browser.get(self.link)

    '''Метод ищет указанный элемент и перехватывает исключение, если элемент не найден. 
    В качестве аргументов передаем как мы ищем локатор и сам локатор'''

    def is_element_presented(self, how_locator, what_locator):
        try:
            self.browser.find_element(how_locator, what_locator)
        except NoSuchElementException:
            return False
        return True

    """Метод для решения капчи в появляющемся алерте на страницах с промо"""

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    """Метод проверяет что элемент не появляется на странице в течении заданного времени"""

    def is_not_element_presented(self, how_locator, what_locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how_locator,
                                                                                                        what_locator)))
            # Ищем элемент в течении 4 секунд. После того как элемент не появляется - ловим исключение и возвращаем
            # True - элемент не найден.
        except TimeoutException:
            return True
        return False  # Если исключение не было поймано - возвращаем False

    """Метод проверяет что элемент пропадает после заданного времени"""

    def is_disappeared(self, how_locator, what_locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                expected_conditions.presence_of_element_located((how_locator, what_locator)))  # В течении 4 секунд с
            # заданным интервалом в 1 секунду проверяем что элемент исчез со страницы. Если за это время элемент не
            # исчезает, ловим исключение и возвращаем False. Если элемент исчез - возвращаем True
        except TimeoutException:
            return False
        return True

    """Метод позволяет перейти в корзину"""

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    """ Метод проверяет залогинен ли пользователь"""

    def should_be_authorized_user(self):
        assert self.is_element_presented(*BasePageLocators.USER_ICON), 'Пользователь незарегистрирован'
