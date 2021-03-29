from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()
    driver.get('http://zero.webappsecurity.com/')
    signin = driver.find_element_by_id('signin_button')
    signin.click()
    assert 'Zero - Log in' == driver.title
    driver.find_element_by_id('user_login').send_keys('username')
    driver.find_element_by_id('user_password').send_keys('password')
    driver.find_element_by_name('submit').click()

    driver.find_element_by_xpath("//a[text()='Pay Bills']").click()
    driver.find_element_by_xpath("//a[text()='Purchase Foreign Currency']").click()

    wait = WebDriverWait(driver,10)
    currele = wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@id='pc_currency']")))
    curr=Select(currele)
    curr.select_by_visible_text('Denmark (krone)')

    sell_rate = wait.until(EC.visibility_of_element_located((By.ID,"sp_sell_rate"))).text
    amount =100
    expected = float(sell_rate.split(' ')[4])*100
    driver.find_element_by_id('pc_amount').send_keys(str(amount))
    selected_currency = driver.find_element_by_id('pc_inDollars_false')
    if not selected_currency.is_selected():
        selected_currency.click()
    driver.find_element_by_css_selector('input#pc_calculate_costs').click()
    conversion_amount=wait.until(EC.visibility_of_element_located((By.ID,"pc_conversion_amount"))).text
    actual = float(conversion_amount.split(' ')[4])
    print(expected, actual)
    assert expected == actual
except Exception as err:
    print(err)
finally:
    #driver.quit()
    pass