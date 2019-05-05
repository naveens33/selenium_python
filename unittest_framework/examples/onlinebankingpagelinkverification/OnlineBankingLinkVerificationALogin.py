import unittest
from selenium import webdriver
from ddt import ddt, data

@ddt
class TestCase(unittest.TestCase):
    driver = webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get("http://zero.webappsecurity.com/")
        cls.driver.find_element_by_id("signin_button").click()
        cls.driver.find_element_by_id("user_login").send_keys("username")
        cls.driver.find_element_by_id("user_password").send_keys("password")
        cls.driver.find_element_by_name("submit").click()
        cls.driver.find_element_by_xpath("//a[text()='Zero Bank']").click()
        cls.driver.find_element_by_xpath("//strong[text()='Online Banking']").click()

    @data('Account Summary', 'Account Activity', 'Transfer Funds', 'Pay Bills')
    def test(self,linkname):
        element = self.driver.find_element_by_xpath("//span[text()='" + linkname + "']")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       element,
                                       "background: yellow; border: 2px solid green;")
        element.click()
        assert  linkname in self.driver.title
        self.driver.back()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

if __name__=='__main__':
    unittest.main()