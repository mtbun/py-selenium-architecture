import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# These values determine the number of times tests will be run after failure and the delay time
RETRY_COUNT = 2
RETRY_DELAY = 1

def pytest_addoption(parser):
    """
    This function adds command line options for pytest.

    Parameters:
        parser (argparse.ArgumentParser): The pytest argument parser.

    Command Line Options:
        --browser (str, optional): Specify the browser to run the tests (chrome, firefox, edge). Defaults to chrome.
        --headless (bool, optional): Run the tests in headless mode. Defaults to False.
        --local (bool, optional): Run the tests locally without using the remote driver. Defaults to False.
    """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser to run the tests (chrome, firefox, edge)")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run the tests in headless mode")
    parser.addoption("--local", action="store_true", default=False,
                     help="Run the tests locally without using the remote driver")

@pytest.fixture(scope="function")
def driver(request):
    """
    This function creates and returns a WebDriver instance based on the specified options.

    Parameters:
        browser (str): The browser to be used for the WebDriver (chrome, firefox, edge).
        headless (bool): Whether to run the browser in headless mode or not.
        local (bool, optional): Whether to run the tests locally or using the remote driver. Defaults to False.

    Returns:
        selenium.webdriver.WebDriver: A WebDriver instance for the specified browser and options.
    """
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    local = request.config.getoption("--local")
    
    if local:
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            if headless:
                firefox_options.headless = True
            driver = webdriver.Firefox(options=firefox_options)
        elif browser == "edge": 
            edge_options = webdriver.EdgeOptions()
            if headless:
                edge_options.use_chromium = True
                edge_options.add_argument("--headless")
            driver = webdriver.Edge(options=edge_options)
        else:
            raise ValueError("Invalid browser option. Supported options: chrome, firefox, edge")
    else:
        selenium_grid_url = "http://hub:4444/wd/hub"  # Selenium Hub URL (hub:4444)
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            if headless:
                firefox_options.headless = True
            driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=DesiredCapabilities.FIREFOX, options=firefox_options)
        elif browser == "edge": 
            edge_options = webdriver.EdgeOptions()
            if headless:
                edge_options.use_chromium = True
                edge_options.add_argument("--headless")
            driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=DesiredCapabilities.EDGE, options=edge_options)
        else:
            raise ValueError("Invalid browser option. Supported options: chrome, firefox, edge")

    driver.set_window_size(968, 1002)

    yield driver

    driver.quit()


# Retry method after failure
def pytest_configure(config):
    config.addinivalue_line("reruns", RETRY_COUNT)
    config.addinivalue_line("reruns_delay", RETRY_DELAY)
