from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver=webdriver.Edge(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
driver.quit()