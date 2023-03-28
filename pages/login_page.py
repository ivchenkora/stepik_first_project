from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented (login part)"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self): # ПЕРЕДЕЛАТЬ ПОД РЕГИСТРАЦИЮ
        email = str(time.time()) + "@fakemail.org"
        print(email)
        email_field = self.browser.find_element_by_css_selector("#id_registration-email")
        email_field.send_keys(email)
        password_log = self.browser.find_element_by_css_selector("#id_registration-password1")
        password_log.send_keys(email)
        password_log = self.browser.find_element_by_css_selector("#id_registration-password2")
        password_log.send_keys(email)
        reg_button = self.browser.find_element_by_css_selector("#register_form > button")
        reg_button.click()
        
        """
        email_field = self.browser.find_element(#id_registration-email)
        email_field.send_keys(email)
        password_reg_first = self.browser.find_element(#id_registration-password1)
        password_reg_first.send_keys(password)
        password_reg_second = self.browser.find_element(#id_registration-password2)
        password_reg_first.send_keys(password)
        reg_button = self.browser.find_element(#register_form > button)
        reg_button.click()
        
        """