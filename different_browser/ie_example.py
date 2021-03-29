from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager

driver=webdriver.Ie(executable_path=IEDriverManager().install())
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
driver.quit()