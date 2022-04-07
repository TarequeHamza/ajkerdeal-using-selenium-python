from Pages.LoginPage import LoginPage
from Pages.CcarePage import CcarePage
from Tests.BasePage import BasePage


class CcareTest(BasePage):
    def test_ccare_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        ccare = CcarePage(self.driver)
        ccare.click_on_ccrBtn()
