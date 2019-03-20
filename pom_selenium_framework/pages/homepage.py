from pom_selenium_framework.locators.locators import HomePageLocator

class HomePage:
    def __init__(self,driver):
        self.driver=driver

    def click_signinbutton(self):
        element=self.driver.find_element(*HomePageLocator.signin_button)
        element.click()