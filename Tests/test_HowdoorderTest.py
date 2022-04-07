from Pages.LoginPage import LoginPage
from Pages.HowdoorderPage import HowdoorderPage
from Tests.BasePage import BasePage


class HowdoorderTest(BasePage):
    def test_howdoorder_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        howdoorder = HowdoorderPage(self.driver)
        howdoorder.click_on_hdoBtn()
