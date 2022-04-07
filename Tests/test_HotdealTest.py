from Pages.LoginPage import LoginPage
from Pages.HotdealPage import HotdealPage
from Tests.BasePage import BasePage

class HotdealTest(BasePage):
    def test_hotdeal_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        hotdeal = HotdealPage(self.driver)
        hotdeal.click_on_pantBtn()