from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'http://the-internet.herokuapp.com/context_menu')

action = ActionChains(driver)
action.context_click(driver.find_element_by_id('hot-spot')).perform()