import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "en":
        print("\nstart en language for test..")
        #link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        browser = webdriver.Chrome()
        #browser.get(link)
    elif language == "ru":
        print("\nstart ru language for test..")
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser = webdriver.Chrome()
        browser.get(link)
    else:
        raise pytest.UsageError("--this language was not found")
    yield browser
    print("\nquit browser..")
    browser.quit()