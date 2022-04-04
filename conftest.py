import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Website language')


"""Fixture allows open browser before test and close browser after completing test-case"""


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print('\nStarting browser')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nExit browser')
    browser.quit()
