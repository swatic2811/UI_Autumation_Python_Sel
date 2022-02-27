from selenium.webdriver.common.by import By
from pages.createaccount_page import CreateAccountPage
from pages.myaccount_page import MyAccountPage
from locators import login_page_locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, x):
        self.driver = x
        self.locator = login_page_locators.LoginPageLocator
        super().__init__(self.driver)

    def navigateToApplication(self, url):
        BasePage.navigateto(self, url)
        BasePage.page_has_loaded(self)
        return self

    def clickToSingIn(self):
        BasePage.click(self, By.XPATH, self.locator.SINGINBUTTON)
        return self

    def enterUserName(self, username):
        BasePage.entertext(self, By.NAME, self.locator.USERNAME, username)
        return self

    def enterPassword(self, password):
        BasePage.entertext(self, By.NAME, self.locator.PASSWORD, password)
        return self

    def clickToSingInButton(self):
        BasePage.click(self, By.NAME, self.locator.SUBMITLOGINBUTTON)
        instance = MyAccountPage(self.driver)
        return instance

    def enterEmailAddress(self, emailaddress):
        BasePage.entertext(self, By.ID, self.locator.EMAILADDRESS, emailaddress)
        return self

    def clickToCreateAccount(self):
        BasePage.click(self, By.ID, self.locator.SUBMITCREATE)
        instance = CreateAccountPage(self.driver)
        return instance
