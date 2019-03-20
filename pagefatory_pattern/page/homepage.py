from pageobject_support import cacheable, callable_find_by as find_by
from selenium.webdriver.common.by import By

class HomePage():
    signin_button = find_by(how=By.ID, using='signin_button')

    def __init__(self,driver):
        self._driver=driver

    def click_siginin_button(self):
        self.signin_button().click()