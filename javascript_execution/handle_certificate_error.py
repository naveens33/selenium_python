from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager

# Using Chrome Options - Adding arguments
from webdriver_manager.firefox import GeckoDriverManager

'''
options =  webdriver.ChromeOptions()
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
'''

# DesiredCapabilities
'''
caps =DesiredCapabilities().CHROME.copy()
caps["acceptInsecureCerts"]= True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),desired_capabilities=caps)
'''

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs=True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile)

driver.maximize_window()
driver.get('https://expired.badssl.com/')
print(driver.find_element_by_tag_name("h1").text)
