from selenium.webdriver.common.by import By

class HomePageLocator:
    signinbutton=(By.ID,"signin_button")

class LoginPageLocator:
    logintextfield=(By.NAME,"user_login")
    passwordfield=(By.CSS_SELECTOR,"#user_password")
    signinbutton=(By.XPATH,"//*[@id='login_form']/div[2]/input")

class AccountSummaryPageLocator:
    paybillslink=(By.XPATH,"//a[text()='Pay Bills']")

class PayBillsPageLocator:
    addnewpayeelink=(By.XPATH,"//a[text()='Add New Payee']")

    #Below locator are for AddNewPayee tab section
    payeenametextfield=(By.ID,'np_new_payee_name')
