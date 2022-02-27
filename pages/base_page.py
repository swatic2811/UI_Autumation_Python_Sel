from selenium.webdriver.support.ui import WebDriverWait
from webdriver.WebdriverBasePage import WebdriverBasePage


class BasePage(WebdriverBasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

