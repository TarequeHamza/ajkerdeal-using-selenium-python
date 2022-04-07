from Pages.LoginPage import LoginPage
from Pages.AjkerdilbPage import AjkerdilbPage
from Tests.BasePage import BasePage


class AjkerdilbTest(BasePage):
    def test_ajkerdilb_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        ajkerdilb = AjkerdilbPage(self.driver)
        ajkerdilb.click_on_adbBtn()
