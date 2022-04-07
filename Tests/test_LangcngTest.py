from Pages.LoginPage import LoginPage
from Pages.LangcngPage import LangcngPage
from Tests.BasePage import BasePage


class LangcngTest(BasePage):
    def test_langcng_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        langcng = LangcngPage(self.driver)
        langcng.click_on_engBtn()
