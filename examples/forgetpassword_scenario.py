from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
driver.find_element_by_id("signin_button").click()
assert "Zero - Log in"==driver.title
driver.find_element_by_partial_link_text("Forgot").click()
driver.find_element_by_xpath("//*[@id='user_email']").send_keys("abc@gmail.com")
driver.find_element_by_xpath("//*[@id='send_password_form']/div[2]/input").click()