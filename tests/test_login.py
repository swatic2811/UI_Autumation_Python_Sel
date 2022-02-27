import pytest
from selenium.common.exceptions import WebDriverException
from pages.login_page import LoginPage
from tests.basetest import BaseTest
from utils.ConfigReaderUtil import ConfigReaderUtil


class TestWeb(BaseTest):

    @pytest.mark.parametrize("test_loginUsers", [
        {"username": "swatic.2811@gmail.com", "pwd": "Delhi.001"},
        {"username": "swatic.2822@gmail.com", "pwd": "Delhi.001"}], indirect=True)
    def test_login(self, test_loginUsers):
        name, pwd = test_loginUsers
        loginPageObject = LoginPage(self.driver)
        loginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
        loginPageObject.clickToSingIn()
        loginPageObject.enterUserName(name)
        loginPageObject.enterPassword(pwd)
        myAccountPageObject = loginPageObject.clickToSingInButton()
        myAccountPageObject.verifyMyAccountPage()
        myAccountPageObject.clickToSingOutButton()
