import selenium.webdriver
from src.config import DEV_BASE_URL, TEST_BASE_URL, PROD_BASE_URL, ENVIRONMENT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.BASE_URL = self.get_base_url()
        self.navigate_to_base_url()

    ENGLISH_LANGUAGE = (By.CSS_SELECTOR, "#js-link-box-en > strong")

    def get_base_url(self):
        if ENVIRONMENT == 'test':
            return TEST_BASE_URL
        elif ENVIRONMENT == 'prod':
            return PROD_BASE_URL
        else:
            return DEV_BASE_URL

    def navigate_to_base_url(self): 
        self.driver.get(self.BASE_URL)
        
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def delay(self, seconds):
        time.sleep(seconds)
    
    def wait_for_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()
    
    def fill_input_field(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)