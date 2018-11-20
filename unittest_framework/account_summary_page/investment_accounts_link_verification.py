import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        inst.driver.maximize_window()

    def setUp(self):
        self.driver.get("http://zero.webappsecurity.com/index.html")
        signin = self.driver.find_element_by_id("signin_button")
        signin.click()
        username = self.driver.find_element_by_id("user_login")
        username.send_keys("username")
        password = self.driver.find_element_by_id("user_password")
        password.send_keys("password")
        self.driver.find_element_by_name("submit").click()
        #assert "Zero - Account Summary" in self.driver.title
        self.assertEqual("Zero - Account Summary",self.driver.title)

    def test_method(self):
        self.driver.find_element_by_xpath("//h2[contains(text(),'Cash Accounts')]")
        self.driver.find_element_by_xpath("//tr[1]/td/a[contains(text(),'Brokerage')]").click()
        self.assertEqual("Zero - Account Activity",self.driver.title)
        heading=self.driver.find_element_by_xpath("//*[@id='ui-tabs-1']/h2").text
        self.assertEqual("Show Transactions",heading)
        select = Select(self.driver.find_element_by_name('accountId'))
        selectedoption=select.first_selected_option
        self.assertEqual("Brokerage",selectedoption.text)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(inst):
        pass
        #inst.driver.quit()

if __name__ == '__main__':
    unittest.main()