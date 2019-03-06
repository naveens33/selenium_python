import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnlineStatement(unittest.TestCase):
    driver = webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')

    def setUp(self):
        self.driver.maximize_window()
        self.driver.get("http://zero.webappsecurity.com/")
        signin = self.driver.find_element_by_id("signin_button")
        signin.click()

        self.driver.find_element_by_id("user_login").send_keys("username")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_name("submit").click()

        assert "Zero - Account Summary" == self.driver.title
        self.driver.find_element_by_xpath("//a[contains(text(),'Online Statements')]").click()

    def test(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='2011']")))
        element.click()
        li=self.driver.find_elements_by_xpath("//a[contains(text(),'/11(')]")
        assert 2==len(li)

    def tearDown(self):
       self.driver.find_element_by_xpath("//li[@class='dropdown'][2]").click()
       self.driver.find_element_by_xpath("//a[text()='Logout']").click()
       self.driver.quit()