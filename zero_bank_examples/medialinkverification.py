from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('http://zero.webappsecurity.com/')

parent_window_handle = driver.current_window_handle
driver.find_element_by_xpath("(//a[contains(text(),'privacy')])[1]").click()

windows = driver.window_handles
#driver.switch_to.window(windows[1])

for window in windows:
    driver.switch_to.window(window)
    if driver.title == "Legal Information | Micro Focus":
        break

driver.find_element_by_link_text('Free Trials').click()
driver.close()
driver.switch_to.window(parent_window_handle)
driver.find_element_by_id('signin_button').click()