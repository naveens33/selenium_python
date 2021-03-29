from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

driver=webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/")
time.sleep(5.0)
element=driver.find_element_by_xpath('//a[text()="Zero Bank"]')
location = element.location
size = element.size
png = driver.get_screenshot_as_png() # saves screenshot of entire page
driver.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']


im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot_element.png')