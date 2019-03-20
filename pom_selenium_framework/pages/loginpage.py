from pom_selenium_framework.locators.locators import LoginPageLocator

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def getPageTitle(self):
        return self.driver.title

    def setText_login(self,text):
        self.driver.find_element(*LoginPageLocator.login_textfield).send_keys(text)

    def setText_password(self,text):
        self.driver.find_element(*LoginPageLocator.password_textfield).send_keys(text)

    def click_siginbutton(self):
        self.driver.find_element(*LoginPageLocator.signin_button).click()