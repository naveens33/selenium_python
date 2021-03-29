from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

browser_name = input("Enter Browser Name(chrome, firefox, ie, opera, edge): ")

if browser_name == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser_name == "ie":
    driver = webdriver.Ie(IEDriverManager().install())
elif browser_name == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browser_name == "opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())

driver.get("http://zero.webappsecurity.com/")