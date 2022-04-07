from Pages.LoginPage import LoginPage
from Pages.HelpcenterPage import HelpcenterPage
from Tests.BasePage import BasePage


class HelpcenterTest(BasePage):
    def test_helpcenter_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        communication = HelpcenterPage(self.driver)
        communication.click_on_hlcBtn()
