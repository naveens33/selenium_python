from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'http://the-internet.herokuapp.com/dynamic_controls')

driver.find_element_by_xpath("//button[text()='Remove']").click()

wait=WebDriverWait(driver,5)
message = wait.until(EC.visibility_of_element_located((By.ID,'message'))).text
assert message == "It's gone!"
try:
    driver.find_element_by_id('checkbox')
except NoSuchElementException as err:
    pass