import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, ..., etc.")

user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("general.useragent.override", user_agent)
        # driver = webdriver.Firefox(fp)
        # driver.set_window_size(1024, 768)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser <browser_name> still is not implemented")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()