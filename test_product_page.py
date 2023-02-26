import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.locators import LoginPageLocators
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/excession_51/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу 
    page.press_view_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_see_products_in_basket()
    basket_page.should__see_basket_is_empty_message()

"""
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                         # открываем страницу
    page.should_be_properly_added_to_basket()           # выполняем метод


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                         # открываем страницу
    page.press_add_to_basket()
    page.should_not_see_success_message_after_adding_product_to_basket()
    
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                         # открываем страницу
    page.should_not_see_success_message()               # выполняем метод
    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                         # открываем страницу
    page.press_add_to_basket()
    page.should_message_disappeared_after_adding_product_to_basket()
"""
    
    
    
    
    
    
    
    
    