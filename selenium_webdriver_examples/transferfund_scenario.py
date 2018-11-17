from selenium import webdriver
from selenium.webdriver.support.ui import Select

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

driver.find_element_by_xpath("//*[@id='transfer_funds_tab']/a").click()
fromaccount=Select(driver.find_element_by_xpath("//*[@id='tf_fromAccountId']"))
fromaccount.select_by_index(2)

toaccount=Select(driver.find_element_by_xpath("//*[@id='tf_toAccountId']"))
#toaccount.select_by_value("5")
toaccount.select_by_visible_text("Brokerage(Avail. balance = $ 197)")

driver.find_element_by_xpath("//*[@id='tf_amount']").send_keys("100")
driver.find_element_by_css_selector("#tf_description").send_keys("Brokerage Ammount")
driver.find_element_by_css_selector("#btn_submit").click()

assert "Please verify that the following transaction is correct by selecting the Submit button below." in driver.find_element_by_xpath("//*[@id='transfer_funds_content']/form/div/div/div[1]/div/p").text
fromaccount=driver.find_element_by_xpath("//*[@id='tf_fromAccountId']")
assert False==fromaccount.is_enabled()
driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",driver.find_element_by_id('tf_fromAccountId'), "background: yellow; border: 2px solid green;")
#driver.quit()