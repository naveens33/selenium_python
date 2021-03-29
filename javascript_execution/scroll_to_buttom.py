from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")