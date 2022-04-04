import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators

"""Class BasePage describes base page which from other pages will be inherited.
Class contains methods for working with the Webdriver """


class BasePage:

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    '''The method searches for a button with a link to the login page and clicks on it'''

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    '''The method checks is a link to login page button exist'''

    def should_be_login_link(self):
        assert self.is_element_presented(*BasePageLocators.LOGIN_LINK), 'Login link not found'

    '''The method opens page in a browser. Browser is passed from file conftest.py, link is passed from test_files'''

    def open(self):
        self.browser.get(self.link)

    '''The method searches for the specified element and catches an exception if the element is not found.'''

    def is_element_presented(self, how_locator, what_locator):
        try:
            self.browser.find_element(how_locator, what_locator)
        except NoSuchElementException:
            return False
        return True

    """Method for solving captcha in alert that appears on promo pages"""

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

    """The method checks that element not appearing on the page within the specified time."""

    def is_not_element_presented(self, how_locator, what_locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how_locator,
                                                                                                        what_locator)))
        except TimeoutException:
            return True
        return False

    """The method checks that the element disappears after a specified time."""

    def is_disappeared(self, how_locator, what_locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                expected_conditions.presence_of_element_located((how_locator, what_locator)))
        except TimeoutException:
            return False
        return True

    """The method opens the basket page"""

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    """The method checks if the user is authorized"""

    def should_be_authorized_user(self):
        assert self.is_element_presented(*BasePageLocators.USER_ICON), 'Пользователь незарегистрирован'
