from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver=webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/")
driver.quit()