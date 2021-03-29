from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver=webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
driver.quit()