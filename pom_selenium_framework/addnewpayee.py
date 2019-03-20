import unittest
from pom_selenium_framework.pages.drivermanager import DriverManager
from pom_selenium_framework.pages.homepage import HomePage
from pom_selenium_framework.pages.loginpage import LoginPage

class AddNewPayee(unittest.TestCase):
    def setUp(self):
        obj=DriverManager("chrome","http://zero.webappsecurity.com/index.html")
        home_page=HomePage(obj.driver)
        home_page.click_signinbutton()
        login_page=LoginPage(obj.driver)
        assert "Zero - Log in" == login_page.getPageTitle()
        login_page.setText_login("username")
        login_page.setText_password("password")
        login_page.click_siginbutton()


    def test(self):
        pass
    def tearDown(self):
        pass
