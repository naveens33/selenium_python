import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnlineStatement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("http://zero.webappsecurity.com/index.html")
        signin = self.driver.find_element_by_id("signin_button")
        signin.click()
        username = self.driver.find_element_by_id("user_login")
        username.send_keys("username")
        password = self.driver.find_element_by_id("user_password")
        password.send_keys("password")
        signin_button = self.driver.find_element_by_name("submit")
        signin_button.click()
        assert "Zero - Account Summary" in self.driver.title

    def test_method(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Online Statements')]").click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='2011']")))
        element.click()
        links=self.driver.find_elements_by_xpath("//a[contains(text(),'11(')]")
        assert 2== links.__len__()
        self.driver.save_screenshot("screenshot.png")

    def tearDown(self):
        self.driver.close()
