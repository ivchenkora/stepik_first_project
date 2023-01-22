import time
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import MainPageLocators
from .pages.locators import LoginPageLocators
from .pages.locators import ProductPageLocators

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                         # открываем страницу
    page.should_be_properly_added_to_basket()           # выполняем метод