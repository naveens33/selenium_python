import allure
import unittest
from selenium import webdriver

@allure.story('Login to Zero Bank website')
@allure.feature('Login Feature')
class AllureReportExample(unittest.TestCase):

    @allure.testcase("Login to Zero Bank website")
    def test_login(self):
        with allure.step("Open application"):
            driver = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
            driver.maximize_window()
            driver.get("http://zero.webappsecurity.com")
        with allure.step("Verify Page Title"):
            assert "Zero - Personal Banking - Loans - Credit Cards" == driver.title
    '''
    def test_login(self):
        self.open_application()
        self.verify_page_title()

    @allure.step("Open application")
    def open_application(self):
        self.driver = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://zero.webappsecurity.com")

    @allure.step("Verify Page Title")
    def verify_page_title(self):
        assert "Zero - Personal Banking - Loans - Credit Cards" == self.driver.title
    '''

if __name__ == '__main__':
    unittest.main()