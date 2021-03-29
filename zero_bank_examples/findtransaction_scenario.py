from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import strptime

def go_to_year(year):
    while(True):
        Y = int(driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text)
        if year<Y:
            driver.find_element_by_xpath("//span[text()='Prev']").click()
        elif year>Y:
            driver.find_element_by_xpath("//span[text()='Next']").click()
        else:
            break

def go_to_month(month):
    while(True):
        M = driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text[:3]
        M = strptime(M, '%b').tm_mon
        if month<M:
            driver.find_element_by_xpath("//span[text()='Prev']").click()
        elif month>M:
            driver.find_element_by_xpath("//span[text()='Next']").click()
        else:
            break


driver=webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")
driver.find_element_by_id("signin_button").click()
driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_name("submit").click()

driver.find_element_by_xpath("//a[text()='Account Activity']").click()
driver.find_element_by_xpath("//a[text()='Find Transactions']").click()

wait = WebDriverWait(driver, 3)
wait.until(EC.visibility_of_element_located((By.ID, "aa_fromDate"))).click()

select_date("5-Sep-2016")