from selenium import webdriver

class DriverManager:
    def __init__(self,browser,url):
        if browser=="chrome":
            self.driver = webdriver.Chrome(r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        elif browser=="firefox":
            pass
        self.driver.maximize_window()
        self.driver.get(url)
