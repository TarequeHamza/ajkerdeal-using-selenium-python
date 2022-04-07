import time

from Locators.locators import GadgetsPageLocators
from Pages.HomePage import HomePage

class GadgetsPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = GadgetsPageLocators
        super(GadgetsPage, self).__init__(driver)

    def click_on_swBtn(self):
        self.find_element(*self.locator.SW_BTN).click()
        time.sleep(20)
