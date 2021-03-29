from selenium import webdriver

driver = webdriver.Ie(executable_path=r'D:\Naveen\Selenium\IEDriverServer_x64_3.150.1\IEDriverServer.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
driver.quit()