import time

from Locators.locators import MfashionPageLocators
from Pages.HomePage import HomePage

class MfashionPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = MfashionPageLocators
        super(MfashionPage, self).__init__(driver)

    def click_on_hijabBtn(self):
        self.find_element(*self.locator.HIJAB_BTN).click()
        time.sleep(20)

