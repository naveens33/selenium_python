import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt,data,unpack
from selenium.webdriver.support.ui import Select

@ddt
class AddNewPayeeScenarios(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://zero.webappsecurity.com")
        cls.driver.find_element_by_id("signin_button").click()
        cls.driver.find_element_by_id("user_login").send_keys("username")
        cls.driver.find_element_by_id("user_password").send_keys("password")
        cls.driver.find_element_by_name("submit").click()
        cls.driver.find_element_by_xpath("//a[text()='Pay Bills']").click()

    def setUp(self):
        self.driver.find_element_by_xpath("//a[text()='Add New Payee']").click()

    @unpack
    @data(("prem","bangalore","13541274","friend"),
              ("somi", "mumbai", "1354385486", "Relation"))
    def testaddnewpayee(self,name,addrs,acc,details):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located((By.ID, "np_new_payee_name"))).send_keys(name)
        self.driver.find_element_by_id("np_new_payee_address").send_keys(addrs)
        self.driver.find_element_by_id("np_new_payee_account").send_keys(acc)
        self.driver.find_element_by_id("np_new_payee_details").send_keys(details)
        self.driver.find_element_by_id("add_new_payee").click()
        msg=self.driver.find_element_by_id("alert_content").text
        self.assertTrue(name in msg,"Not successful")
        payee_ele=wait.until(EC.visibility_of_element_located((By.ID, "sp_payee")))
        payee=Select(payee_ele)
        '''
        for option in payee.options:
            if name==option.text:
                break
        else:
            print("Name Not Found")
        '''
        #options_text=[]
        #for option in payee.options:
        #    options_text.append(option.text)
        #self.assertTrue(name in options_text, "Name Not found")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass