import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_conf():
    browser.config.browser_name = 'edge'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture(scope="session")
def url_browser(browser_conf):
    browser.open('https://www.ecosia.org/')
    yield
    browser.quit()



