from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
import math

class ProductPage(BasePage): 

    def should_be_properly_added_to_basket(self):
        self.press_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_correct_name_message_after_added()
        self.should_be_correct_price_message_after_added()

    def press_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        button.click()
        
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
    
    def should_be_correct_name_message_after_added(self):
        book_title_text = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MAIN).text
        book_title_text_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED_MESSAGE).text
        assert book_title_text in book_title_text_message, "Added book named incorrectly in confirm message"
        
    def should_be_correct_price_message_after_added(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_COST_MAIN).text
        bucket_value = self.browser.find_element(*ProductPageLocators.BUCKET_COST_MESSAGE).text
        assert book_price in bucket_value, "Bucket value is incorrect"
