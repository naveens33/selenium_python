import unittest
from selenium import webdriver
import xlrd

class TestCase1(unittest.TestCase):
    username = []
    password = []
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        inst.driver.maximize_window()
        inst.getdata(inst)

    def setUp(self):
        self.driver.get("http://zero.webappsecurity.com/index.html")
        signin = self.driver.find_element_by_id("signin_button")
        signin.click()

    def test_method(self):
        for i in range(0,len(self.username)):
            unelement = self.driver.find_element_by_id("user_login")
            pwelement = self.driver.find_element_by_id("user_password")
            unelement.send_keys(self.username[i])
            pwelement.send_keys(self.password[i])
            self.driver.find_element_by_name("submit").click()
            # assert "Zero - Account Summary" in self.driver.title
            self.assertEqual("Zero - Log in", self.driver.title)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

    def getdata(self):
        wb = xlrd.open_workbook("Credential.xlsx")
        sheet = wb.sheet_by_index(0)
        for i in range(1,sheet.nrows):
                self.username.append(sheet.cell_value(i,0))
                self.password.append(sheet.cell_value(i,1))

if __name__ == '__main__':
    unittest.main()