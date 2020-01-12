from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://zero.webappsecurity.com")
driver.find_element_by_xpath("(//a[contains(text(),'microfocus')])[1]").click()

for window in driver.window_handles:
    driver.switch_to.window(window)
    print(driver.title)

driver.switch_to.window(driver.window_handles[1])
print(driver.title)

driver.switch_to.window(driver.window_handles[0])
print(driver.title)

'''
    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        if driver.title == "Legal - About | Micro Focus":
            break

assert "Zero - Log in"==driver.title
signin2=driver.find_element_by_name("submit")
Verify(False,signin2.is_enabled(),"Signin button is not disabled")
driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
signin2.click()

assert  "Zero - Account Summary"==driver.title
'''