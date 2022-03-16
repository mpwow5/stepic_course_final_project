import pytest
from selenium import webdriver


'''Фикстура позволяет запускать браузер перед каждым тестом и закрывать его после завершения теста'''


@pytest.fixture(scope='function')
def browser():
    print('\nЗапуск браузера')
    browser = webdriver.Chrome()
    yield browser
    print('\nВыход из браузера')
    browser.quit()

