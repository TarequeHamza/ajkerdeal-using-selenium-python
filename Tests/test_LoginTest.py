import time

from Pages.LoginPage import LoginPage
from Tests.BasePage import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()
