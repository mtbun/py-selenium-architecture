import pytest
from selenium import webdriver

# These values determine the number of times tests will be run after failure and the delay time
RETRY_COUNT = 2
RETRY_DELAY = 1

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser to run the tests (chrome, firefox, edge)")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run the tests in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    selenium_grid_url = "http://hub:4444/wd/hub"  # Selenium Hub URL (hub:4444)

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities={'browserName': 'chrome'}, options=chrome_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless:
            firefox_options.headless = True
        driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities={'browserName': 'firefox'}, options=firefox_options)
    elif browser == "edge": 
        edge_options = webdriver.EdgeOptions()
        if headless:
            edge_options.use_chromium = True
            edge_options.add_argument("--headless")
        driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities={'browserName': 'edge'}, options=edge_options)
    else:
        raise ValueError("Invalid browser option. Supported options: chrome, firefox, edge")

    driver.set_window_size(968, 1002)

    yield driver

    driver.quit()


# Retry method after failure
def pytest_configure(config):
    config.addinivalue_line("reruns", RETRY_COUNT)
    config.addinivalue_line("reruns_delay", RETRY_DELAY)
