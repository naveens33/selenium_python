from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
signin = driver.find_element_by_id('signin_button')
signin.click()
assert 'Zero - Log in' == driver.title
driver.find_element_by_id('user_login').send_keys('username')
driver.find_element_by_id('user_password').send_keys('password')
driver.find_element_by_name('submit').click()

driver.find_element_by_xpath("//a[text()='Pay Bills']").click()
driver.find_element_by_xpath("//a[text()='Purchase Foreign Currency']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID,'purchase_cash'))).click()
time.sleep(2)
import PIL.ImageGrab
im = PIL.ImageGrab.grab()
im.save("screenshot3.png", "PNG")
alert = driver.switch_to.alert
alert.accept()

