import unittest
from selenium import webdriver
import xlrd
from ddt import ddt,data,unpack
from unittest_framework.datadriventest.datadriven_excel_and_csv.datadriven_excel.readexceldata import getData

@ddt
class TestCase1(unittest.TestCase):
    username = []
    password = []
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        inst.driver.maximize_window()
        inst.driver.get("http://zero.webappsecurity.com/index.html")
        signin = inst.driver.find_element_by_id("signin_button")
        signin.click()

    def setUp(self):
        pass

    @data(*getData())
    def test_method(self,data):
        unelement = self.driver.find_element_by_id("user_login")
        pwelement = self.driver.find_element_by_id("user_password")
        unelement.send_keys(data[0])
        pwelement.send_keys(data[1])
        self.driver.find_element_by_name("submit").click()
            # assert "Zero - Account Summary" in self.driver.title
        self.assertEqual("Zero - Log in", self.driver.title)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()