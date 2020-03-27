from selenium import webdriver

driver=webdriver.Firefox(executable_path=r'D:\Naveen\Selenium\geckodriver-v0.26.0-win64/geckodriver.exe')
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
driver.quit()