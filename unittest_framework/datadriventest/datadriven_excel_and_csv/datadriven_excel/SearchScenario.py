import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt,data, unpack
from unittest_framework.sample.readexceldata_search import getData
@ddt
class SearchScenario(unittest.TestCase):
    driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
    def setUp(self):
        self.driver.maximize_window()
        self.driver.get("http://zero.webappsecurity.com/index.html")

    @data(*getData())
    @unpack
    def test(self,searchterm,count):
        self.driver.find_element_by_id("searchTerm").send_keys(searchterm)
        self.driver.find_element_by_id("searchTerm").send_keys(Keys.ENTER)
        links=self.driver.find_elements_by_xpath("//a[contains(text(),'Zero -')]")
        assert count == len(links)

    def tearDown(self):
        pass