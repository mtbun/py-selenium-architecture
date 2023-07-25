import selenium.webdriver
from src.config import DEV_BASE_URL, TEST_BASE_URL, PROD_BASE_URL, ENVIRONMENT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage():
    def __init__(self, driver):
        """
        BasePage constructor to initialize the BasePage object.

        Parameters:
            driver (WebDriver): The WebDriver instance to be used for interactions with the browser.
        """
        self.driver = driver
        self.BASE_URL = self.get_base_url()
        self.navigate_to_base_url()

    ENGLISH_LANGUAGE = (By.CSS_SELECTOR, "#js-link-box-en > strong")

    def get_base_url(self):
        """
        Get the base URL based on the current environment.

        Returns:
            str: The base URL corresponding to the current environment.
        """
        if ENVIRONMENT == 'test':
            return TEST_BASE_URL
        elif ENVIRONMENT == 'prod':
            return PROD_BASE_URL
        else:
            return DEV_BASE_URL

    def navigate_to_base_url(self):
        """
        Navigate to the base URL in the current browser window.
        """
        self.driver.get(self.BASE_URL)
        
    def find_element(self, by, value):
        """
        Find a web element on the page using the specified locator.

        Parameters:
            by (str): The method used to find the element (e.g., By.ID, By.NAME, By.XPATH, etc.).
            value (str): The value of the locator used to find the element.

        Returns:
            WebElement: The web element found using the specified locator.
        """
        return self.driver.find_element(by, value)

    def delay(self, seconds):
        """
        Pause the execution for the specified number of seconds.

        Parameters:
            seconds (int): The number of seconds to pause the execution.
        """
        time.sleep(seconds)
    
    def wait_for_element(self, by, value, timeout=10):
        """
        Wait for a web element to be present on the page using the specified locator.

        Parameters:
            by (str): The method used to find the element (e.g., By.ID, By.NAME, By.XPATH, etc.).
            value (str): The value of the locator used to find the element.
            timeout (int, optional): The maximum time to wait for the element to be present (default is 10 seconds).

        Returns:
            WebElement: The web element that is present on the page.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        """
        Click on a web element using the specified locator.

        Parameters:
            by (str): The method used to find the element (e.g., By.ID, By.NAME, By.XPATH, etc.).
            value (str): The value of the locator used to find the element.
        """
        element = self.wait_for_element(by, value)
        element.click()
    
    def fill_input_field(self, by, value, text):
        """
        Fill an input field with the specified text using the specified locator.

        Parameters:
            by (str): The method used to find the input field (e.g., By.ID, By.NAME, By.XPATH, etc.).
            value (str): The value of the locator used to find the input field.
            text (str): The text to be entered into the input field.
        """
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)
