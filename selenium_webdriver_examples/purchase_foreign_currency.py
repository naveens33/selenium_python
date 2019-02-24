from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
try:
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
    assert "Zero - Account Summary" == driver.title

    driver.find_element_by_xpath("//a[contains(text(),'Pay Bills')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Purchase Foreign Currency')]").click()

    #driver.implicitly_wait(2)
    wait =WebDriverWait(driver,10)
    ele=wait.until(EC.visibility_of_element_located((By.ID,"pc_currency")))
    currency_select=Select(ele)
    currency_select.select_by_index(3)

    wait =WebDriverWait(driver,10)
    ele=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@id='sp_sell_rate']")))

    sell_rate=ele.text
    actual_value=float(sell_rate.split(' ')[4])

    driver.find_element_by_id("pc_amount").send_keys("1000")

    if driver.find_element_by_id("pc_inDollars_false").is_selected() == False:
        driver.find_element_by_id("pc_inDollars_false").click()

    driver.find_element_by_id("pc_calculate_costs").click()

    lable=driver.find_element_by_id("pc_conversion_amount")
    assert str(round(actual_value*1000,2)) in lable.text

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              lable,
                              "background: yellow; border: 2px solid green;")

    driver.save_screenshot("purchasescreen.png")

except(Exception):
    print(Exception.with_traceback())

finally:
    driver.close()
    pass
