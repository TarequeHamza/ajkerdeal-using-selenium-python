import time

from Pages.RegistrationPage import RegistrationPage
from Tests.BasePage import BasePage


class RegistrationTest(BasePage):

    def test_registration_page(self):
        registration = RegistrationPage(self.driver)
        registration.click_on_login()
        time.sleep(4)
        registration.click_on_register()
        registration.enter_name("roqib")
        registration.enter_phone("01783920102")
        registration.enter_email("roqib.cu@gmail.com")
        registration.enter_password("TestCase01")
        registration.enter_again("TestCase01")
        registration.click_on_register_btn()
        registration.click_on_registration()



