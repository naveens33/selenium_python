from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
try:
    driver.maximize_window()
    driver.get("http://zero.webappsecurity.com/index.html")
    signin=driver.find_element_by_id("signin_button")
    signin.click()
    username=driver.find_element_by_id("user_login")
    username.send_keys("username")
    password=driver.find_element_by_id("user_password")
    password.send_keys("password")
    signin_button=driver.find_element_by_name("submit")
    signin_button.click()
    assert "Zero - Account Summary" == driver.title

    driver.find_element_by_xpath("//a[contains(text(),'Pay Bills')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Purchase Foreign Currency')]").click()

    #driver.implicitly_wait(2)
    wait =WebDriverWait(driver,10)
    ele=wait.until(EC.visibility_of_element_located((By.ID,"pc_currency")))

    driver.find_element_by_id("pc_calculate_costs").click()

    alert_box=driver.switch_to.alert
    assert "Please, ensure that you have filled all the required fields with valid values." in alert_box.text
    alert_box.accept()

except(Exception):
    print(Exception.with_traceback())

finally:
    #driver.close()
    pass
