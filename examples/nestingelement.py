from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")
elements = driver.find_elements_by_xpath("//div[@class='span3']/div/h4")
for element in elements:
    sibling=element.find_element(By.XPATH,"following-sibling::p")
    print(sibling.text)