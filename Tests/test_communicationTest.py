from Pages.LoginPage import LoginPage
from Pages.communicationPage import CommunicationPage
from Tests.BasePage import BasePage


class CommunicationTest(BasePage):
    def test_communication_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        communication = CommunicationPage(self.driver)
        communication.click_on_cmmuBtn()
