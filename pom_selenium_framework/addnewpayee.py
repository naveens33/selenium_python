import unittest
from pom_selenium_framework.pages.drivermanager import DriverManager
from pom_selenium_framework.pages.homepage import HomePage
from pom_selenium_framework.pages.loginpage import LoginPage
from pom_selenium_framework.pages.accountsummarypage import AccountSummaryPage
from pom_selenium_framework.pages.paybillspage import PayBillsPage


class AddNewPayee(unittest.TestCase):
    def setUp(self):
        self.obj=DriverManager("http://zero.webappsecurity.com")
        homepage=HomePage(self.obj.driver)
        homepage.clickSignInButton()
        loginpage=LoginPage(self.obj.driver)
        assert "Zero - Log in"==loginpage.getTitle()
        loginpage.setText_Login("username")
        loginpage.setText_Password("password")
        loginpage.clickSignInButton()
        aspage=AccountSummaryPage(self.obj.driver)
        assert  "Zero - Account Summary"==aspage.getTitle()
        aspage.clickpaybillslink()

    def test(self):
        paybills=PayBillsPage(self.obj.driver)
        paybills.clickaddnewpayeelink()
        paybills.setTextPayeeName("Prem Kumar")

    def tearDown(self):
        pass