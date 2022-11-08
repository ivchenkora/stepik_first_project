import time
from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    time.sleep(5)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    