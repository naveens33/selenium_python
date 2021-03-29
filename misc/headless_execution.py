from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime

'''
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Chrome(GeckoDriverManager().install(),options=options)
'''

options = webdriver.ChromeOptions()
options.headless = True
start =  datetime.now()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.maximize_window()
driver.get(r'http://zero.webappsecurity.com/')
print(driver.title)
end = datetime.now()
print(end-start)