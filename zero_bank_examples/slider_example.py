from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.bankbazaar.com/axis-car-loan.html')
driver.maximize_window()
driver.implicitly_wait(30)
frame = driver.find_element_by_xpath("//iframe[@name='Car Loan Calculator']")
driver.switch_to.frame(frame)
element = driver.find_element_by_xpath("((//div[@id='slider'])[1]/div/div[2])[1]")
driver.execute_script("arguments[0].setAttribute('style', 'left: 50%');",
                              element)
import time
time.sleep(5)
element.click()
#action = ActionChains(driver)
#action.double_click(element)
pass
#action.click_and_hold(driver.find_elements_by_xpath("(//div[@id='slider'])[1]")).move_by_offset(50,0).release();
#action.drag_and_drop_by_offset(driver.find_elements_by_xpath("(//div[@id='slider'])[1]"), 50, 0).perform();

