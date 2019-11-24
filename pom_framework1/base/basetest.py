from selenium import webdriver

class BaseTest():
    driver=""
    def __init__(self,browsername,url):
        if browsername=="chrome":
            self.driver = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
        elif browsername=="firefox":
            self.driver = webdriver.Firefox(executable_path=r'D:/Naveen/Selenium/geckodriver-v0.22.0-win64/geckodriver.exe')
        self.driver.maximize_window()
        self.driver.get(url)
