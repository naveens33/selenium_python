from selenium import webdriver

def verify_text(expected,actual):
    if expected!=actual:
        print("Verification failed: ",expected,actual)

driver =webdriver.Chrome(r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')

driver.maximize_window()

driver.get("http://zero.webappsecurity.com/")

signin=driver.find_element_by_id("signin_button")

signin.click()

assert "Zero - Log in" ==driver.title

#verify_text("Zero - Log in",driver.title)

driver.find_element_by_id("user_login").send_keys("username")

driver.find_element_by_id("user_password").send_keys("password")

driver.find_element_by_name("submit").click()

#driver.close()

driver.quit()
