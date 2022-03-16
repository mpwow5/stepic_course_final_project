from selenium.common.exceptions import NoSuchElementException

"""Класс описывает базовую страницу, от которой будут наследованы остальные страницы.
Класс содержит вспомогательные методы по работе с драйвером"""
class BasePage:
    '''Конструктор, вызывается при инициализации объекта BasePage.'''

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicity_wait(timeout)  # Указываем неявное ожидание

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
