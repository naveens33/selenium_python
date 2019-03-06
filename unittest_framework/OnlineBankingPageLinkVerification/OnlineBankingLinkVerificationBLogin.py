import unittest
from selenium import webdriver

class TestCase(unittest.TestCase):
    driver = webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get("http://zero.webappsecurity.com/")
        cls.driver.find_element_by_xpath("//strong[text()='Online Banking']").click()

    def setUp(self):
        pass

    def test(self):
        links=('Account Summary','Account Activity','Transfer Funds','Pay Bills')
        for li in links:
            element=self.driver.find_element_by_xpath("//span[text()='"+li+"']")
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element,
                                  "background: yellow; border: 2px solid green;")
            element.click()
            assert "Zero - Log in" ==self.driver.title
            self.driver.back()

    def tearDown(self):
        #self.driver.quit()
        pass

if __name__=='__main__':
    unittest.main()