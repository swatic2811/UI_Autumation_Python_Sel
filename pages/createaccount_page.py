from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import Createaccount_Page_locators
from pages.myaccount_page import MyAccountPage

class CreateAccountPage(BasePage):

    def __init__(self, x):
        self.driver = x
        self.locator = Createaccount_Page_locators.CreateAccountPage
        super().__init__(x)

    def selectTitle(self, titlevalue):
        genderXPath = self.locator.SELECTTITLE.format(title=titlevalue)
        BasePage.click(self, By.XPATH, genderXPath)
        return self

    def enterFirstName(self, firstname):
        BasePage.entertext(self, By.ID, self.locator.FIRSTNAME, firstname)
        return self

    def enterLastName(self, lastname):
        BasePage.entertext(self, By.ID, self.locator.LASTNAME, lastname)
        return self

    def enterPassword(self, password):
        BasePage.entertext(self, By.ID, self.locator.PASSWORD, password)
        return self

    def selectBirthDay(self, day):
        BasePage.selectDropDownValueByValue(self, By.ID, self.locator.BIRTHDAY, day)
        return self

    def selectBirthMonth(self, month):
        BasePage.selectDropDownValueByValue(self, By.ID, self.locator.BIRTHMONTH, month)
        return self

    def selectBirthYear(self, year):
        BasePage.selectDropDownValueByValue(self, By.ID, self.locator.BIRTHYEAR, year)
        return self

    def checkNewsLetterCheckBox(self):
        BasePage.click(self, By.XPATH, self.locator.NEWSLETTERCHECKBOX)
        return self

    def checkReceiveSpecialOffersCheckBox(self):
        BasePage.click(self, By.XPATH, self.locator.SPECIALOFFERCHECKBOX)
        return self

    def enterCompanyName(self, companyname):
        BasePage.entertext(self, By.ID, self.locator.COMPANTNAME, companyname)
        return self

    def enterAddress1(self, address1):
        BasePage.entertext(self, By.ID, self.locator.ADDRESS1, address1)
        return self

    def enterAddress2(self, address2):
        BasePage.entertext(self, By.ID, self.locator.ADDRESS2, address2)
        return self

    def enterCity(self, city):
        BasePage.entertext(self, By.ID, self.locator.CITY, city)
        return self

    def enterPostCode(self, postcode):
        BasePage.entertext(self, By.ID, self.locator.POSTCODE, postcode)
        return self

    def enterOtherInfo(self, otherinfo):
        BasePage.click(self, By.ID, self.locator.OTHERINFO)
        BasePage.entertext(self, By.ID, self.locator.OTHERINFO, otherinfo)
        return self

    def enterPostCode(self, postcode):
        BasePage.entertext(self, By.ID, self.locator.POSTCODE, postcode)
        return self

    def enterPhoneNumber(self, phonenumber):
        BasePage.entertext(self, By.ID, self.locator.PHONENUMBER, phonenumber)
        return self

    def enterMobileNumber(self, mobilenumber):
        BasePage.entertext(self, By.ID, self.locator.MOBILENUMBER, mobilenumber)
        return self

    def selectState(self, statename):
        BasePage.selectdropdownvaluebytext(self, By.ID, self.locator.STATE, statename)
        return self

    def selectCountry(self, countryname):
        BasePage.selectdropdownvaluebytext(self, By.ID, self.locator.COUNTRY, countryname)
        return self

    def clickToRegister(self):
        BasePage.click(self, By.XPATH, self.locator.RIGSTERBUTTON)
        class_instance = MyAccountPage(self.driver)
        return class_instance
