'''Файл с тестами главной страницы'''

link = 'http://selenium1py.pythonanywhere.com/'

'''Тест с проверкой возможности пользователя перейти с главной страницы на страницу логина
В качестве аргумента функции передается фикстура browser из файла conftest.py'''


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
