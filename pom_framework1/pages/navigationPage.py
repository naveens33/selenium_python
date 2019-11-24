from pom_framework1.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class NavigationPage(BasePage):

    links=By.XPATH,"//ul[contains(@class,'nav-tabs')]/li/a"

    def navigate_to(self,link_text):
        element=self.get_element_by_text(self.links,link_text)
        element.click()