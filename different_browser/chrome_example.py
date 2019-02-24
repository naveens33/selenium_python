from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/")
driver.quit()