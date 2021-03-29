from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
signin = driver.find_element_by_id('signin_button')
signin.click()
#driver.find_element_by_link_text('Forgot your password ?').click()
#driver.find_element_by_partial_link_text('Forgot').click()