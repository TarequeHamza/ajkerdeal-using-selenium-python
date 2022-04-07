import time

from Locators.locators import LoginPageLocators
from Pages.HomePage import HomePage


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_login(self):
        self.find_element(*self.locator.LOGIN_BTN).click()

    def set_email(self, email):
        self.find_element(*self.locator.SET_EMAIL).send_keys(email)

    def set_password(self, password):
        time.sleep(5)
        self.find_element(*self.locator.SET_PASS).send_keys(password)

    def confirm_login(self):
        self.find_element(*self.locator.CLICK_LOGIN_BTN).click()

    def clik_jog(self):
        self.find_element(*self.locator.CCR_BTN).click()
