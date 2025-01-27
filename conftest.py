import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")  # Получаем значение аргумента --language
    browser_name = request.config.getoption('browser_name')  # Получаем значение аргумента --browser_name
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, etc."
    )
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox')
