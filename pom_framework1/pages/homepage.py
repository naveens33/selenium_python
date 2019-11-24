from selenium.webdriver.common.by import By
from pom_framework1.pages.basepage import BasePage

class HomePage(BasePage):

    signin_button=By.ID,"signin_button"
    search_textfield=By.ID,"searchTerm"

    def click_signin_button(self):
        self.click(self.signin_button)

    def do_search(self,text):
        self.type(self.search_textfield,text)