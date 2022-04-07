import time

from Locators.locators import RetrunrefundpPageLocators
from Pages.HomePage import HomePage


class RetrunrefundpPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = RetrunrefundpPageLocators
        super(RetrunrefundpPage, self).__init__(driver)

    def click_on_rrpBtn(self):
        time.sleep(2)
        scroll_pause_time = 2
        screen_height = self.driver.execute_script("return window.screen.height;")
        i = 1

        while True:
            self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
            if (screen_height) * i > scroll_height:
                break

        self.find_element(*self.locator.RRP_BTN).click()
        time.sleep(20)
