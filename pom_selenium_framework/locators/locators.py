from selenium.webdriver.common.by import By

class HomePageLocator:
    signin_button=(By.ID,"signin_button")
    search_textfield=(By.ID,"searchTerm")

class LoginPageLocator:
    login_textfield=(By.XPATH,"//*[@id='user_login']")
    password_textfield=(By.CSS_SELECTOR,"#user_password")
    signin_button=(By.NAME,"submit")