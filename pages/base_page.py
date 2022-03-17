import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

"""Класс описывает базовую страницу, от которой будут наследованы остальные страницы.
Класс содержит вспомогательные методы по работе с драйвером"""


class BasePage:
    '''Конструктор, вызывается при инициализации объекта BasePage.'''

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)  # Указываем неявное ожидание

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
