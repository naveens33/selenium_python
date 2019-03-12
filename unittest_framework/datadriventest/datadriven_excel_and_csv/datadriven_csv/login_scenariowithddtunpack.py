import unittest
from selenium import webdriver
from ddt import ddt, data,unpack
from unittest_framework.datadriventest.datadriven_excel_and_csv.datadriven_csv.readcsvdata import getData

@ddt
class TestClass(unittest.TestCase):
    driver = webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get("http://zero.webappsecurity.com/")
        signin = cls.driver.find_element_by_id("signin_button")
        signin.click()

    @data(*getData())
    @unpack
    def test(self,uname,pword):
        self.driver.find_element_by_id("user_login").send_keys(uname)
        self.driver.find_element_by_id("user_password").send_keys(pword)
        self.driver.find_element_by_name("submit").click()
        assert "Zero - Log in" == self.driver.title

    @classmethod
    def tearDownClass(cls):
        pass

if __name__=='__main__':
    unittest.main()