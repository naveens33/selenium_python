import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data, unpack

@ddt
class SearchScenario(unittest.TestCase):
    driver = webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')

    @classmethod
    def setUpClass(self):
        self.driver.maximize_window()
        self.driver.get("http://zero.webappsecurity.com/")

    @data(("Account",2), ("Map",1))
    @unpack
    def test_Account(self,searchterm,count):
        search=self.driver.find_element_by_id("searchTerm")
        search.clear()
        search.send_keys(searchterm)
        search.send_keys(Keys.ENTER)
        links=self.driver.find_elements_by_xpath("//a[contains(text(),'Zero -')]")
        assert len(links) == count
        for link in links:
            assert searchterm in link.text
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  link,
                                  "background: yellow; border: 2px solid green;")


    def tearDown(self):
        self.driver.back()