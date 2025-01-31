from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")  # Получаем значение аргумента --language
    browser_name = request.config.getoption('browser_name')  # Получаем значение аргумента --browser_name
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        sleep(2)
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        options.add_argument("--start-maximized")  # Открывать браузер на весь экран
        options.add_argument("--disable-gpu")  # Отключает GPU
        options.add_argument("--disable-software-rasterizer")  # Отключает рендеринг через CPU
        options.add_argument(
            "--disable-features=UseTensorFlowLiteForGpuInference")  # отключает использование TensorFlow Lite для GPU-ускорения
        options.add_argument("--disable-dev-shm-usage")  # Избегает проблем с разделяемой памятью
        # options.add_argument("--disable-extensions")  # Отключает все расширения
        # options.add_argument("--remote-debugging-port=9222")  # Использует отладочный порт
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        sleep(2)
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
