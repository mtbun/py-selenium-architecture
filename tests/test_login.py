from src.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import json

'''
This function getting credentials from a json
In this example, This function used for get login credentials from a json
'''
def get_login_credentials(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

login_info = get_login_credentials(file_path="src\\testData\\loginCredentials.json")
username = login_info["username"]
password = login_info["password"]
invalid_username = login_info["invalidUsername"]
invalid_password = login_info["invalidPassword"]
empty = login_info["empty"]

'''
This test checks successful login
Verify username listed correctly after login
'''
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login(username, password)
    PROFILE_USERNAME = login_page.find_element(*login_page.PROFILE_USERNAME).text

    assert username == PROFILE_USERNAME

'''
This test checks unsuccessful login with invalid password
Verify username is not presented 
Verify right error message appeared
'''
def test_invalid_login_withInvalidPassword(driver):
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
    pass

@pytest.mark.skip(reason="Test is not ready yet.")
def test_invalid_login_withEmptyPassword(driver):
    pass