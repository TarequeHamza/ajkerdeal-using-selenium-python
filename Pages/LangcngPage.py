import time

from Locators.locators import LangcngPageLocators
from Pages.HomePage import HomePage


class LangcngPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LangcngPageLocators
        super(LangcngPage, self).__init__(driver)

    def click_on_engBtn(self):
        self.find_element(*self.locator.ENG_BTN).click()
        time.sleep(20)