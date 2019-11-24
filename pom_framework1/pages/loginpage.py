from selenium.webdriver.common.by import By
from pom_framework1.pages.basepage import BasePage

class LoginPage(BasePage):

    login_textfield=By.ID,"user_login"
    password_textfield=By.ID,"user_password"
    signin_button=By.NAME,"submit"

    def do_login(self,uname,pword):
        self.type(self.login_textfield,uname)
        self.type(self.password_textfield, pword)
        self.click(self.signin_button)