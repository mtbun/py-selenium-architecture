from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOGIN_SPAN = (By.CSS_SELECTOR, "#pt-login-2 span")
    USERNAME_FIELD = (By.ID, "wpName1")
    PASSWORD_FIELD = (By.ID, "wpPassword1")
    LOGIN_BUTTON = (By.ID, "wpLoginAttempt")
    PROFILE_USERNAME = (By.CSS_SELECTOR, '#pt-userpage-2>a>span')
    LOGIN_ERROR_FIELD = (By.CSS_SELECTOR, "div.mw-message-box.cdx-message.cdx-message--block.mw-message-box-error.cdx-message--error > div")
    
    # navigate to login page
    def navigate_to_login_page(self):
        self.click(*self.ENGLISH_LANGUAGE)
        self.click(*self.LOGIN_SPAN)

    # fill the all fields on login form
    def fill_login_fields(self, username, password):
        self.fill_input_field(*self.USERNAME_FIELD, username)
        self.fill_input_field(*self.PASSWORD_FIELD, password)

    # fill the all fields on login for and clikc login button
    def login(self, username, password):
        self.fill_login_fields(username, password)
        self.click(*self.LOGIN_BUTTON)