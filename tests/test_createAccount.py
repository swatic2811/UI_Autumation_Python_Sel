import pytest
from selenium.common.exceptions import WebDriverException
from pages.login_page import LoginPage
from tests.basetest import BaseTest
from utils.ConfigReaderUtil import ConfigReaderUtil


class TestWeb(BaseTest):

    def test_createAccount(self):
        finalData = self.getData('test_createAccount')  # enter your test case name
        loginPageObject = LoginPage(self.driver)
        loginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
        loginPageObject.clickToSingIn()
        loginPageObject.enterEmailAddress(finalData['Email'])
        createAccountPageObject = loginPageObject.clickToCreateAccount()
        createAccountPageObject.selectTitle(finalData['Title'])
        createAccountPageObject.enterFirstName(finalData['FirstName'])
        createAccountPageObject.enterLastName(finalData['LastName'])
        createAccountPageObject.enterPassword(finalData['Password'])
        createAccountPageObject.selectBirthDay(finalData['Birthday'])
        createAccountPageObject.selectBirthMonth(finalData['BirthMonth'])
        createAccountPageObject.selectBirthYear(finalData['BirthYear'])
        createAccountPageObject.checkNewsLetterCheckBox()
        createAccountPageObject.checkReceiveSpecialOffersCheckBox()
        createAccountPageObject.enterCompanyName(finalData['CompanyName'])
        createAccountPageObject.enterAddress1(finalData['Address1'])
        createAccountPageObject.enterAddress2(finalData['Address2'])
        createAccountPageObject.enterCity(finalData['City'])
        createAccountPageObject.selectState(finalData['State'])
        createAccountPageObject.enterPostCode(finalData['PostCode'])
        createAccountPageObject.selectCountry(finalData['Country'])
        createAccountPageObject.enterOtherInfo(finalData['OtherInfo'])
        createAccountPageObject.enterPhoneNumber(finalData['PhoneNumber'])
        createAccountPageObject.enterMobileNumber(finalData['MobileNumber'])
        myAccountPageObject = createAccountPageObject.clickToRegister()
        myAccountPageObject.verifyMyAccountPage()
        myAccountPageObject.clickToSingOutButton()
