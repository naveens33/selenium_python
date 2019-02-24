from selenium import webdriver

driver =webdriver.Chrome(r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()

driver.get("http://zero.webappsecurity.com/")
signin=driver.find_element_by_id("signin_button")
signin.click()

driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_name("submit").click()

assert "Zero - Account Summary"==driver.title

#driver.close()
#driver.quit()