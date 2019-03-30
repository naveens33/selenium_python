from selenium import webdriver

class DriverManager:
    def __init__(self,url):
        self.driver = webdriver.Chrome(r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(url)