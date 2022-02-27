import time
from utils.logger import LOGGER
import pytest
import selenium.webdriver.support.wait as wait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select



class WebdriverBasePage(object):
    filepath = ""



    def __init__(self, x):
        self.driver = x

    def navigateto(self, url):
        self.driver.get(url)

    def elementWaitCondition(self, byelement, byindentifier):
        self.web_driver_wait = wait.WebDriverWait(self.driver, 30)
        self.web_driver_wait.until(
            expected_conditions.presence_of_element_located((byelement, byindentifier)), "element is not present")

    def entertext(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.clear()
            element.send_keys(mvalue)
            logger.info("\nEnter value : " + byindentifier + " value :" + mvalue)

        except WebDriverException as e:
            logger.error(e.msg)
            raise e

    def click(self, byelement, byindentifier):
        logger = LOGGER.get_logger()
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.click()
            logger.info("Click to " + byindentifier)

        except WebDriverException as e:
            logger.error(e.msg)

            raise e

    def submit(self, byelement, byindentifier):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.submit()
            logger.info("Submit to " + byindentifier)
        except WebDriverException as e:
            logger.error(e.msg)
            raise e

    def selectdropdownvaluebytext(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_visible_text(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value" + mvalue + "Selected")
        except WebDriverException as e:
            logger.error(e.msg)
            raise e

    def driverquit(self):
        self.driver.quit()

    def pressTab(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)

    def isElementPresent(self, byelement, byindentifier):
        try:
            isElementPresent = False
            self.elementWaitCondition(byelement, byindentifier)
            if len(self.driver.find_elements(by=byelement, value=byindentifier)) > 0:
                isElementPresent = True
            else:
                isElementPresent = False

            return isElementPresent
        except WebDriverException as e:
            raise e

    def isElementEnabled(self, byelement, byindentifier):
        try:
            isElementEnabled = False
            self.elementWaitCondition(byelement, byindentifier)
            isElementEnabled = self.driver.find_element(by=byelement, value=byindentifier).is_enabled()
            return isElementEnabled;
        except WebDriverException as e:
            raise e

    def isDisplayed(self, byelement, byindentifier):
        try:
            isDisplayedStatus = False
            self.elementWaitCondition(byelement, byindentifier)
            isElementEnabled = self.driver.find_element(by=byelement, value=byindentifier).is_displayed()
            return isElementEnabled
        except WebDriverException as e:
            raise e

    def isAlertIsPresent(self):
        try:
            self.web_driver_wait.until(
                expected_conditions.alert_is_present(), "Alert is not present")

        except WebDriverException as e:
            raise e

    def selectDropDownValueByIndex(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_index(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            logger.error(e.msg)
            raise e

    def selectDropDownValueByVisibleText(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_visible_text(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            logger.error(e.msg)
            raise e

    def selectDropDownValueByValue(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_value(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            logger.error(e.msg)
            raise e

    def clickAndHold(self, byelement, byindentifier):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            logger.info( "\nClick and Hold to " + byindentifier)
        except WebDriverException as e:

            raise e

    def contextClick(self, byelement, byindentifier):
        try:
            logger = LOGGER.get_logger()
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            logger.info("\nContext Click to" + byindentifier)
        except WebDriverException as e:

            raise e

    def doubleClick(self, byelement, byindentifier):
        try:
            logger = LOGGER.get_logger()
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            logger.info( "\nDouble Click to " + byindentifier)
        except WebDriverException as e:

            raise e

    def dragAndDrop(self, sourcebyelement, sourcebyindentifier, targetbyelement,
                    targetbyindentifier):
        try:
            logger = LOGGER.get_logger()
            sourceelement = self.driver.find_element(by=sourcebyelement, value=sourcebyindentifier)
            targetelement = self.driver.find_element(by=targetbyelement, value=targetbyindentifier)
            actions = ActionChains(self.driver)
            actions.click_and_hold(sourceelement).move_to(targetelement).release()
            logger.info("\nDrag element " + sourcebyindentifier + "Drop Element " + targetbyindentifier)
        except WebDriverException as e:

            raise e

    def clickByActionClass(self, byelement, byindentifier):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.click(element).perform()
            logger.info("\nClick to " + byindentifier)
        except WebDriverException as e:

            raise e

    def clickToElementByJavaScript(self, byelement, byindentifier):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            self.driver.execute_script("arguments[0].click();", element)
            logger.info("\nClick to " + byindentifier)
        except WebDriverException as e:

            raise e

    def scrollToView(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except WebDriverException as e:
            raise e

    def deSelectDropDownValueByIndex(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_index(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:

            raise e

    def deSelectDropDownValueByVisibleText(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_visible_text(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:

            raise e

    def deSelectDropDownValueByValue(self, byelement, byindentifier, mvalue):
        try:
            logger = LOGGER.get_logger()
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_value(mvalue)
            logger.info("\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")

        except WebDriverException as e:

            raise e

    def back(self):
        self.driver.back()

    def page_has_loaded(self):
        for i in range(10):
            page_state = self.driver.execute_script('return document.readyState;')
            time.sleep(3)
            if(page_state == 'complete'):
                break;



