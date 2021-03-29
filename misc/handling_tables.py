from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'http://the-internet.herokuapp.com/challenging_dom')
rows = driver.find_elements_by_xpath("//table/tbody/tr")
for row in rows:
    for td in row.find_elements_by_xpath("td"):
        if td.text == "Apeirian4":
            row.find_element_by_xpath("td[7]/a[2]").click()