import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase1(unittest.TestCase):

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

    def test_selectedcurrency(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Pay Bills')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Purchase Foreign Currency')]").click()
        wait = WebDriverWait(self.driver, 10)
        currency = wait.until(EC.visibility_of_element_located(
           (By.XPATH, "//select[@id='pc_currency']")))
        select = Select(currency)
        select.select_by_value("CHF")
        wait = WebDriverWait(self.driver, 10)
        sellrate = wait.until(EC.visibility_of_element_located(
            (By.ID, "sp_sell_rate")))
        completetext=sellrate.text
        value=completetext.split(' ')[4]
        amount="10"
        self.driver.find_element_by_id("pc_amount").send_keys(amount)
        self.driver.find_element_by_xpath("//input[@id='pc_inDollars_false']").click()
        self.driver.find_element_by_id("pc_calculate_costs").click()
        ans=round(float(value)*float(amount),2)
        wait = WebDriverWait(self.driver, 10)
        lable = wait.until(EC.visibility_of_element_located(
            (By.ID, "pc_conversion_amount")))
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              lable,
                              "background: yellow; border: 2px solid green;")
        conversion_amount=lable.text
        print(str(ans)+" "+conversion_amount)
        assert str(ans) in conversion_amount
        self.driver.save_screenshot("purchascreen.png")

    def tearDown(self):
        pass
