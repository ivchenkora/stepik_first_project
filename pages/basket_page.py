from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
            
        return False
        
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
        
    def should_not_see_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_FORM), \
            "Success message is presented, but should not be"
    
    def should__see_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IF_EMPTY), \
            "Success message is presented, but should not be"
        
        