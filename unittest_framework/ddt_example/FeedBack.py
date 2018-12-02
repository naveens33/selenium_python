import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
import datetime
import time

@ddt
class OnlineStatement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("http://zero.webappsecurity.com/index.html")
        self.driver.find_element_by_xpath("//strong[text()='Feedback']").click()


    @data(('Prem', 'prem@gmail.com','login issue','login not working'), ('Kathick', 'karthick@gmail.com','balance issue','invalid transaction'))
    @unpack
    def test_method(self,name,email,subject,description):
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("email").send_keys(email)
        self.driver.find_element_by_id("subject").send_keys(subject)
        self.driver.find_element_by_id("comment").send_keys(description)
        self.driver.find_element_by_name("submit").click()
        conf=self.driver.find_element_by_xpath("//div[@class='offset3 span6']").text
        self.assertTrue(name in conf)
        ts = time.time()
        date=str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'));
        date=date.replace("-","_")
        date =date.replace(":","_")
        date =date.replace(" ","_")
        self.driver.save_screenshot("D:\\screenshot_feedback"+date+".png")

    def tearDown(self):
        self.driver.close()
