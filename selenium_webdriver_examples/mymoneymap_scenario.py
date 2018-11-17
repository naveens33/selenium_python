from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
signin=driver.find_element_by_id("signin_button")
signin.click()
username=driver.find_element_by_id("user_login")
username.send_keys("username")
password=driver.find_element_by_id("user_password")
password.send_keys("password")
signin_button=driver.find_element_by_name("submit")
signin_button.click()
assert "Zero - Account Summary" in driver.title

driver.find_element_by_xpath("//*[@id='money_map_tab']/a").click()
#driver.implicitly_wait(10)
#ImplictWait have an impact in overall testing performance,
#since the implicit wait will be used in all FindElement calls.
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='gridview-1015-bd-Deposits']/td/table/tbody/tr[2]/td[1]/div")))
#Explicit Wait, is a one-timer used for a particular search.
#It is more extendible in the means that we can set it up to wait for any condition.
#Usually, some of the prebuilt ExpectedConditions to wait for elements to become clickable, visible, invisible, etc.,

assert "Direct Deposits"==element.text
assert "Other Deposits"==driver.find_element_by_xpath("//*[@id='gridview-1015-bd-Deposits']/td/table/tbody/tr[3]/td[1]/div").text

driver.quit()