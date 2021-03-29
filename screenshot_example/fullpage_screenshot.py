from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless =True
driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe',options=options)
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')
S = lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot('screenshot4.png')
driver.quit()