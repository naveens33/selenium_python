from pom_selenium_framework.locators.locators import LoginPageLocator

class LoginPage:
    def __init__(self,driver):
        self.d=driver

    def getTitle(self):
        return self.d.title

    def setText_Login(self,text):
        self.d.find_element(*LoginPageLocator.logintextfield).send_keys(text)

    def setText_Password(self,text):
        self.d.find_element(*LoginPageLocator.passwordfield).send_keys(text)

    def clickSignInButton(self):
        self.d.find_element(*LoginPageLocator.signinbutton).click()
