from Pages.LoginPage import LoginPage
from Pages.GadgetsPage import GadgetsPage
from Tests.BasePage import BasePage

class GadgetsTest(BasePage):
    def test_gadgets_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        gadgets = GadgetsPage(self.driver)
        gadgets.click_on_swBtn()
