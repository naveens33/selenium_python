from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
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

fromaccele=driver.find_element_by_xpath("//*[@id='tf_fromAccountId']")
fromaccselect=Select(fromaccele)
fromaccselect.select_by_visible_text("Loan(Avail. balance = $ 780)")

toaccele=driver.find_element_by_css_selector("#tf_toAccountId")
toaccselect=Select(toaccele)
toaccselect.select_by_index(2)

driver.find_element_by_css_selector("#tf_amount").send_keys("1000")
driver.find_element_by_css_selector("#tf_description").send_keys("Payment")

driver.find_element_by_css_selector("#btn_submit").click()

fromaccele=driver.find_element_by_xpath("//*[@id='tf_fromAccountId']")
assert False==fromaccele.is_enabled()

toaccele=driver.find_element_by_xpath("//*[@id='tf_toAccountId']")
assert  False==toaccele.is_enabled()

assert  False==driver.find_element_by_css_selector("#tf_amount").is_enabled()
assert  False==driver.find_element_by_css_selector("#tf_description").is_enabled()

driver.find_element_by_xpath("//*[@id='btn_submit']").click()

assert "Confirm" in driver.find_element_by_xpath("//*[@id='transfer_funds_content']/div/div/h2").text
assert "You successfully submitted your transaction."==driver.find_element_by_css_selector("#transfer_funds_content > div > div > div.alert.alert-success").text
