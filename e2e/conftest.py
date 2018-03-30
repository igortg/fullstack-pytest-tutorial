import pytest
import chromedriver_binary
from selenium.webdriver.chrome import options, webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'http://localhost:4200'
headless= False

@pytest.fixture(scope='session')
def chrome_driver():
    '''
    This fixture is the Selenium Webdriver. Must be used in all tests that want to control the browser and
    access page HTML elements.
    '''
    chrome_options = options.Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1366,768')
    if headless:
        chrome_options.add_argument('--headless')
    chrome = webdriver.WebDriver(options=chrome_options)
    chrome.get(BASE_URL)
    yield chrome
    chrome.quit()


class BrowserHelper:
    '''
    Base class to build Page Helpers.
    '''

    def __init__(self, selenium_driver, base_url=''):
        self.selenium = selenium_driver
        self.base_url = base_url

    def find_by_css(self, css_selector):
        '''
        Find an element by css selector.

        :param css_selector: the css selector
        '''
        return self.selenium.find_element(By.CSS_SELECTOR, css_selector)

    def find_many_by_css(self, css_selector):
        '''
        Find an element by css selector.

        :param css_selector: the css selector
        '''
        return self.selenium.find_elements(By.CSS_SELECTOR, css_selector)

    def navigate_to(self, relative_path):
        '''
        Route to another page relative to the `base_url`.

        :param str relative_path: path relative to `base_url`
        '''
        self.selenium.get(self.base_url + relative_path)


    def wait_for(self, expected_condition, timeout=1):
        '''
        Wait for an expected condition of the page.

        :param expected_condition: selenium webdriver expected condition object
        :param int timeout: for how long it will wait for the expected condition before fail
        '''
        WebDriverWait(self.selenium, timeout).until(expected_condition)


@pytest.fixture(scope='session')
def browser(chrome_driver):
    return BrowserHelper(chrome_driver, BASE_URL)


@pytest.fixture(autouse=True)
def clean_up(chrome_driver):
    '''
    Clean up session info on browser storage and redirect to the front page after each test, so all tests have the
    same starting point.
    '''
    yield
    chrome_driver.execute_script('window.localStorage.clear();')
    chrome_driver.execute_script('window.sessionStorage.clear();')
