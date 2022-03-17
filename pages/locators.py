from selenium.webdriver.common.by import By

'''Файл содержит селекторы всех элементов для тестов. Каждая константа представляет собой кортеж из двух элементов - 
что ищем и как '''

'''Селекторы на главной странице'''


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')  # Селектор кнопки логина
