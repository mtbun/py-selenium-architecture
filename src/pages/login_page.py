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
    
    # Navigate to the login page
    def navigate_to_login_page(self):
        """
        This method navigates to the login page by clicking on the login span.

        Returns:
            None
        """
        self.click(*self.ENGLISH_LANGUAGE)  # Assuming ENGLISH_LANGUAGE is defined in BasePage
        self.click(*self.LOGIN_SPAN)

    # Fill all fields on the login form
    def fill_login_fields(self, username, password):
        """
        This method fills in the username and password fields on the login form.

        Parameters:
            username (str): The username to be entered in the username field.
            password (str): The password to be entered in the password field.

        Returns:
            None
        """
        self.fill_input_field(*self.USERNAME_FIELD, username)
        self.fill_input_field(*self.PASSWORD_FIELD, password)

    # Fill all fields on the login form and click the login button
    def login(self, username, password):
        """
        This method fills in the login fields (username and password) and clicks the login button.

        Parameters:
            username (str): The username to be entered in the username field.
            password (str): The password to be entered in the password field.

        Returns:
            None
        """
        self.fill_login_fields(username, password)
        self.click(*self.LOGIN_BUTTON)
