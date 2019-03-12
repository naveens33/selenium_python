import unittest
from selenium import webdriver
import xlrd
from ddt import ddt, data

@ddt
class TestClass(unittest.TestCase):
    driver = webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
    uname=[]
    pword=[]

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get("http://zero.webappsecurity.com/")
        signin = cls.driver.find_element_by_id("signin_button")
        signin.click()
        cls.getData(cls)

    @data(0,1,2,3)
    def test(self,i):
        self.driver.find_element_by_id("user_login").send_keys(self.uname[i])
        self.driver.find_element_by_id("user_password").send_keys(self.pword[i])
        self.driver.find_element_by_name("submit").click()

        assert "Zero - Log in" == self.driver.title

    def getData(self):
        wb=xlrd.open_workbook("Credential.xlsx")
        sheet=wb.sheet_by_index(0)
        for i in range(1,sheet.nrows):
            self.uname.append(sheet.cell_value(i,0))
            self.pword.append(sheet.cell_value(i, 1))

    @classmethod
    def tearDownClass(cls):
        pass

if __name__=='__main__':
    unittest.main()