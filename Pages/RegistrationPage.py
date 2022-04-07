from Locators.locators import RegistrationPageLocators
from Pages.HomePage import HomePage


class RegistrationPage(HomePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = RegistrationPageLocators
        super(RegistrationPage, self).__init__(driver)

    def click_on_login(self):
        self.find_element(*self.locator.LOGIN_BTN).click()

    def click_on_register(self):
        self.find_element(*self.locator.REGISTER_BTN).click()

    def enter_name(self, name):
        self.find_element(*self.locator.NAME).send_keys(name)

    def enter_phone(self, phone):
        self.find_element(*self.locator.PHONE).send_keys(phone)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def enter_again(self, again):
        self.find_element(*self.locator.AGAIN).send_keys(again)

    def click_on_register_btn(self):
        self.find_element(*self.locator.MALE).click()

    def click_on_registration(self):
        self.find_element(*self.locator.REGISTRATION_BTN).click()
