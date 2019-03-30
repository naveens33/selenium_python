from pom_selenium_framework.locators.locators import HomePageLocator

class HomePage:
    def __init__(self,driver):
        self.d=driver

    def clickSignInButton(self):
        self.d.find_element(*HomePageLocator.signinbutton).click()