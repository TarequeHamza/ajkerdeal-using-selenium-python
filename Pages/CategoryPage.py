import time

from Locators.locators import CategoryPageLocators
from Pages.HomePage import HomePage

class CategoryPage(HomePage):
    def __init__(self,driver):
        self.driver = driver
        self.locator = CategoryPageLocators
        super(CategoryPage, self).__init__(driver)

    def click_on_watchBtn(self):
        self.find_element(*self.locator.WATCH_BTN).click()

    def click_on_tablewatchBtn(self):
        time.sleep(20)
        self.find_element(*self.locator.TABLE_BTN).click()