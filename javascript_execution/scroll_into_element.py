from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
terms = driver.find_element_by_id('terms_of_use_link')
driver.execute_script("arguments[0].scrollIntoView(true)",terms)