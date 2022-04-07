import time

from Locators.locators import HotdealPageLocators
from Pages.HomePage import HomePage

class HotdealPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator =HotdealPageLocators
        super(HotdealPage, self).__init__(driver)

    def click_on_pantBtn(self):
        self.find_element(*self.locator.PANT_BTN).click()
        time.sleep(20)