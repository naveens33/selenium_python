import unittest
from pagefatory_pattern.page.drivermanager  import  DriverManager
from pagefatory_pattern.page.homepage import HomePage

class TestCase(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        obj=DriverManager("chrome","http://zero.webappsecurity.com/index.html")
        self.driver=obj.driver
        home_page=HomePage(self.driver)
        home_page.click_siginin_button()


    def test_addnewpayee(self):
        pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()