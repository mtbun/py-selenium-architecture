from src.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import json

def get_login_credentials(file_path):
    """
    This function reads login credentials from a JSON file and returns them as a dictionary.

    Parameters:
        file_path (str): The file path of the JSON file containing login credentials.

    Returns:
        dict: A dictionary containing login credentials (username, password, invalidUsername, invalidPassword, empty).
    """
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

login_info = get_login_credentials(file_path="src\\testData\\loginCredentials.json")
username = login_info["username"]
password = login_info["password"]
invalid_username = login_info["invalidUsername"]
invalid_password = login_info["invalidPassword"]
empty = login_info["empty"]


def test_valid_login(driver):
    """
    Test to check successful login and verify if the correct username is listed after login.

    Parameters:
        driver (selenium.webdriver.WebDriver): The WebDriver instance for the test.

    Assertions:
        Verifies that the displayed username matches the expected username after successful login.
    """
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login(username, password)
    PROFILE_USERNAME = login_page.find_element(*login_page.PROFILE_USERNAME).text

    assert username == PROFILE_USERNAME


def test_invalid_login_withInvalidPassword(driver):
    """
    Test to check unsuccessful login with an invalid password.

    Parameters:
        driver (selenium.webdriver.WebDriver): The WebDriver instance for the test.

    Assertions:
        Verifies that the profile username is not presented and the correct error message appears.
    """
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login(username, invalid_password)

    # Ensure profile username is not presented
    try:
        PROFILE_USERNAME = login_page.find_element(*login_page.PROFILE_USERNAME)
        raise elemenFinded("the profile name element is presented")
    except:
        pass

    ERROR_MESSAGE = login_page.find_element(*login_page.LOGIN_ERROR_FIELD).text
    assert ERROR_MESSAGE == "Incorrect username or password entered. Please try again."


@pytest.mark.skip(reason="Test is not ready yet.")
def test_invalid_login_withInvalidUsername(driver):
    """
    Test to check unsuccessful login with an invalid username. (Not implemented yet)
    This test is currently skipped.
    """
    pass

@pytest.mark.skip(reason="Test is not ready yet.")
def test_invalid_login_withEmptyPassword(driver):
    """
    Test to check unsuccessful login with an empty password. (Not implemented yet)
    This test is currently skipped.
    """
    pass