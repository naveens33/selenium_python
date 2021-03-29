from selenium import webdriver
import requests

driver = webdriver.Chrome(executable_path=r'D:\Naveen\Selenium\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get(r'http://the-internet.herokuapp.com/broken_images')
images = driver.find_elements_by_xpath('//div[@class="example"]/img')
count = 0
for image in images:
    response = requests.get(image.get_attribute("src"))
    count += 1 if response.status_code == 200 else 0

print(count)


