from selenium import webdriver
import autoit

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'http://the-internet.herokuapp.com/basic_auth')
autoit.win_activate("the-internet.herokuapp.com/basic_auth - Google Chrome")
autoit.send("rajkumar{TAB}myPassword{ENTER}")

