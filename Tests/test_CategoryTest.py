from Pages.LoginPage import LoginPage
from Pages.CategoryPage import CategoryPage
from Tests.BasePage import BasePage

class CategoryTest(BasePage):
    def test_Category_page(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_on_login()
        loginpage.set_email("tareque.hamzah@gmail.com")
        loginpage.set_password("TestCase01")
        loginpage.confirm_login()

        category = CategoryPage(self.driver)
        category.click_on_watchBtn()
        category.click_on_tablewatchBtn()
