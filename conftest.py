import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''Функция позволяет получить данные, переданные в командной строке. По умолчанию указываем язык сайта - Английский.'''


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Язык сайта')


'''Фикстура позволяет запускать браузер перед каждым тестом и закрывать его после завершения теста.
Встроенная фикстару request обратывает полученные из командной строки данные'''


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')  # Получаем выбранный язык из командной строки
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print('\nЗапуск браузера')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nВыход из браузера')
    browser.quit()
