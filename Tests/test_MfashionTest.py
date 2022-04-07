from Pages.LoginPage import LoginPage
from Pages.MfashionPage import MfashionPage
from Tests.BasePage import BasePage

class MfashionTest(BasePage):
    def test_mfashion_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        mfashion = MfashionPage(self.driver)
        mfashion.click_on_hijabBtn()
