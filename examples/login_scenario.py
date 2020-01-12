from selenium import webdriver

def Verify(expected,actual,message):
    if expected!=actual:
        print(message)


driver=webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")
signin=driver.find_element_by_id("signin_button")
signin.click()
assert "Zero - Log in"==driver.title
signin2=driver.find_element_by_name("submit")
Verify(False,signin2.is_enabled(),"Signin button is not disabled")
driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
signin2.click()

assert  "Zero - Account Summary"==driver.title
#driver.close()
#driver.quit()