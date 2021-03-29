import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")
signin=driver.find_element_by_id("signin_button")
signin.click()
assert "Zero - Log in"==driver.title
signin2=driver.find_element_by_name("submit")
driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
signin2.click()

driver.find_element_by_link_text('Account Activity').click()
time.sleep(1)
acc_ele = driver.find_element_by_id('aa_accountId')
account = Select(acc_ele)
account.select_by_visible_text('Loan')
time.sleep(1)
table = driver.find_element_by_tag_name('table')
for row in table.find_elements_by_xpath('tbody/tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)