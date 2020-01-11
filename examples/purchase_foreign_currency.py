from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome(r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
try:

    driver.maximize_window()
    driver.get("http://zero.webappsecurity.com/index.html")
    signin = driver.find_element_by_id("signin_button")

    signin.click()
    username = driver.find_element_by_id("user_login")
    username.send_keys("username")
    password = driver.find_element_by_id("user_password")
    password.send_keys("password")
    signin_button = driver.find_element_by_name("submit")
    signin_button.click()
    assert "Zero - Account Summary" in driver.title

    driver.find_element_by_xpath("//a[contains(text(),'Pay Bills')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Currency')]").click()
    #driver.implicitly_wait(3)
    #time.sleep(2)
    wait=WebDriverWait(driver,3)
    currencyele=wait.until(EC.visibility_of_element_located((By.ID,"pc_currency")))
    curreny=Select(currencyele)
    curreny.select_by_visible_text("Denmark (krone)")
    sellrate=wait.until(EC.visibility_of_element_located((By.ID,"sp_sell_rate")))
    sellratevalue=sellrate.text.split(' ')[4]

    amount=100
    driver.find_element_by_id("pc_amount").send_keys(amount)
    selectedcurrency=driver.find_element_by_id("pc_inDollars_false")
    if selectedcurrency.is_selected()==False:
        selectedcurrency.click()
    driver.find_element_by_id("pc_calculate_costs").click()

    conversionamount=wait.until(EC.visibility_of_element_located((By.ID,"pc_conversion_amount")))
    conversionamountvalue=conversionamount.text.split(' ')[4]

    expectedamount=amount*float(sellratevalue)
    assert round(expectedamount,2) == float(conversionamountvalue)

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                          conversionamount,
                              "background: yellow; border: 2px solid green;")

    driver.save_screenshot("purchasescreen.png")

except Exception as err:
    print("Error: "+str(err))

finally:
    #driver.close()
    pass