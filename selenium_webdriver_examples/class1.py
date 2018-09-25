from selenium import webdriver

driver=webdriver.Chrome(r"D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/index.html')
signin1=driver.find_element_by_id('signin_button')
signin1.click()
username=driver.find_element_by_id('user_login')
username.send_keys('username')
password=driver.find_element_by_id('user_password')
password.send_keys('password')
signin2=driver.find_element_by_name('submit')
signin2.click()
assert 'Zero - Account Summary' in driver.title
driver.quit()