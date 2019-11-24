import unittest
from pom_framework1.base.basetest import BaseTest
from pom_framework1.pages.homepage import HomePage
from pom_framework1.pages.loginpage import LoginPage
from pom_framework1.pages.navigationPage import NavigationPage
from pom_framework1.pages.accountactivitypage import AccountActivityPage

class FindTransaction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base=BaseTest("chrome","http://zero.webappsecurity.com")
        home=HomePage(base.driver)
        home.click_signin_button()
        login=LoginPage(base.driver)
        login.do_login("username","password")
        navigate=NavigationPage(base.driver)
        navigate.navigate_to("Account Activity")
        accountactivity=AccountActivityPage(base.driver)
        accountactivity.navigate_to("Find Transactions")
        pass

    def setUp(self):
        pass

    def test(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass