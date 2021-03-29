from selenium import webdriver
import autoit

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'http://the-internet.herokuapp.com/upload')
#driver.find_element_by_id("file-upload").send_keys("D:\\hello124.png")
driver.find_element_by_id("drag-drop-upload").click()
#autoit.win_wait("Open",2)
import time
time.sleep(3)
autoit.control_focus("Open","Edit1")
autoit.control_set_text("Open","Edit1","D:\\hello124.png")
autoit.control_click("Open","Button1")