from selenium import webdriver

driver=webdriver.Ie(executable_path=r'D:/Naveen/Selenium/IEDriverServer_x64_3.14.0/IEDriverServer.exe')
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
driver.quit()