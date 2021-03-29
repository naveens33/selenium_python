from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'C:\Users\naveen.s\PycharmProjects\selenium-python\alert_pop_box\PromptAlert.html')
driver.find_element_by_tag_name('button').click()
alert = driver.switch_to.alert
alert.send_keys("36")
alert.accept()
